#!/usr/bin/env python3
import os
import re
import time
import textwrap
import requests
import subprocess

import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")
deepl_api_key = os.environ.get("DEEPL_API_KEY")

BASE_FILE_SUFFIX = '.de.md'
script_path = os.path.abspath(__file__)
parent_dir = os.path.dirname(script_path)
repo_path = os.path.abspath(os.path.join(parent_dir, '..'))
target_languages = {
    'de': 'German',
    "en": "English",
    "fr": "French",
    "it": "Italian",
    "es": "Spanish",
    "st": "Südtirolerisch Dialect",
    "zh": "Chinese Simplified",
    "ar": "Arabic",
    "pt": "Portuguese",
    "id": "Indonesian",
    "ru": "Russian",
    "ja": "Japanese",
    "ko": "Korean",
    "tr": "Turkish",
    "nl": "Dutch",
    "vi": "Vietnamese",
    "th": "Thai",
    "pl": "Polish",
    "hi": "Hindi",
    "fa": "Persian",
    "sw": "Swahili",
}

deepl_languages = {}


# def get_changed_files():
#     output = subprocess.check_output(["git", "status", "--porcelain"], cwd=repo_path).decode().splitlines()
#     changed_files = [line.split(maxsplit=1)[-1].strip() for line in output]
#     return [os.path.abspath(file) for file in changed_files if file.endswith('.de.md')]


def get_changed_files():
    return [file for file in
            subprocess.check_output(["git", "diff", "--name-only", "HEAD~1", "HEAD"]).decode().split("\n")
            if file.endswith(BASE_FILE_SUFFIX)
            ]


def translate_md_file():
    # print(openai.Model.list())
    deepl_available_languages()
    try:
        # print(f'Path [{repo_path}]')
        print(f'Languages {list(target_languages.keys())}')
        print(f'Languages Available {list(deepl_languages.keys())}')
        os.chdir(repo_path)
        changed_files = get_changed_files()
        print(f'Changed Files {changed_files}')
        current_iteration = 0
        total_iterations = (len(target_languages.keys()) - 1) * len(changed_files)
        for file in changed_files:
            for lang_key, lang_name in list(target_languages.items())[1:]:
                current_iteration += 1
                with \
                        open(file, 'r') as inputFile, \
                        open(file.replace(BASE_FILE_SUFFIX, f'.{lang_key}.md'), 'w') as output_file:
                    section_count = 0
                    output_text = ''
                    for line in inputFile:
                        line = line.replace('\r\n', os.linesep).replace('\n', os.linesep).replace('\r', os.linesep)
                        if output_text and line.startswith('#'):
                            translated = translate(output_text, lang_key, lang_name)
                            print_progress(current_iteration, output_file, section_count, total_iterations, translated)
                            output_file.write(translated)
                            output_text = line
                            section_count += 1
                        elif output_text or line.startswith("#"):
                            output_text += line
                        elif line.startswith('title:') or line.startswith('description:'):
                            kv = line.split(':', 1)
                            translated = translate(kv[1].replace('"', '').strip(), lang_key, lang_name) \
                                .replace('"', '').replace('\n', '').replace('\r', '')
                            print_progress(current_iteration, output_file, section_count, total_iterations, translated)
                            output_file.write(kv[0] + ': "' + translated + '"' + os.linesep)
                            section_count += 1
                        else:
                            output_file.write(line)
                    if output_text:
                        translated = translate(output_text, lang_key, lang_name)
                        print_progress(current_iteration, output_file, section_count, total_iterations, translated)
                        output_file.write(translated)
    except Exception as e:
        print(f"An error occured: {e}")
        return []


def print_progress(current_iteration, output_file, section_count, total_iterations, translated):
    print(
        f'Progress [{((current_iteration / total_iterations) * 100):.2f}%]'
        f' File [{os.path.basename(output_file.name)}]'
        f' Section [{section_count}]'
        f' Text [{translated.strip().replace(os.linesep, " ").replace("  ", "")[:120]}]'
    )


def translate(output_text, lang_key, lang_name):
    if output_text.strip() == '':
        return output_text
    elif os.linesep + os.linesep in output_text:
        title, text = output_text.split(os.linesep + os.linesep, 1)
        text = translate_with_api(text, lang_key, lang_name)
        text = textwrap.fill(text, 120).replace('  ', ' ') if not re.search(r"[\*\-\[\]#]", text) else text
        title = translate_with_api(title, lang_key, lang_name)
        return os.linesep + title + os.linesep + os.linesep + text + os.linesep
    else:
        return translate_with_api(output_text, lang_key, lang_name)


def translate_with_api(text, lang_key, lang_name):
    if lang_key in deepl_languages:
        return translate_with_gpt(text, lang_key, lang_name)
    else:
        return translate_with_gpt(text, lang_key, lang_name)


def translate_with_gpt(text, lang_key, lang_name):
    while True:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a Translator which only translate text without changing the format or content"
                    },
                    {
                        "role": "user",
                        "content": f'Translate the markdown text to {lang_name}:\n```\n{text}\n```'
                        # "content": f'Translate the markdown text to {lang_name} keep nouns, no commenting, no interpretations, no markdown format changes:\n```\n{text}\n```'
                    },
                ]
            )
            return response['choices'][0]['message']['content']
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Retrying in 5 seconds...")
            time.sleep(5)


def translate_with_deepl(text, lang_key, lang_name):
    try:
        return requests.get(
            'https://api-free.deepl.com/v2/translate',
            headers={
                "User-Agent": "TheUnspoken/1.0.0",
                "Authorization": f"DeepL-Auth-Key {deepl_api_key}",
                "Content-Type": "application/x-www-form-urlencoded",
            },
            data={
                "text": text,
                "target_lang": lang_key.upper()
            }
        ).json()["translations"][0]["text"]
    except Exception as e:
        translate_with_gpt(text, lang_key, lang_name)


def deepl_available_languages():
    for item in requests.get('https://api-free.deepl.com/v2/languages', headers={
        "Authorization": f"DeepL-Auth-Key {deepl_api_key}"
    }).json():
        deepl_languages[item['language'].lower()] = item['name']


translate_md_file()
