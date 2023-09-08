---
title: "Back to Maven?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "The elusive search for simplicity and a short journey to rediscover the power of Maven"
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# Back to Maven?

The text is already in English and there is no translation required. Here is the text back:

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

## 10 years of Gradle. In search of relief and a short journey to rediscover the strength of Maven.

You didn't provide any text to translate. Please provide the text you want to translate.

### Maximizing the Potential of Developers - We Need More Time-Saving Tools

I am interested in topics that are often overlooked or rarely discussed. Often there are cool technologies in use, but
hardly anyone talks about the associated problems. Development has become very complex these days. With cool buzzwords
such as "Serverless", "Low Code", "IaC", "Big Data", "Cloud", "DevOps", "You Build it You run it" etc., developers
already have more than enough additional tasks to cope with. More tasks mean that there are hardly any experts left and
something is always neglected for the focus. Therefore, automation and time savings are mega important. "Don't make me
think" and "Works out of the box" are already good quality features that I cannot see in Gradle yet. To be fair, Gradle
is not the only modern tool that gives us work, instead of making it easier for us.

### The illusory search for simplicity and automation

Since SOAP, I have had a deep-rooted aversion to XML-based configurations. With Gradle, I had hoped
that writing bind-scripts would be a breeze. Unfortunately, my hopes and my motivation diminished
from time to time. Gradle strives for flexibility and sacrifices automation and quality for it. Developers
blindly follow the trend without regard for the impact on the reliability of the software. To keep Gradle
build scripts simple and low-maintenance, it requires strong discipline. Such discipline is already rare in the
source code and that's why it's even rarer in the build scripts.

### Translations and Workarounds - When Build Scripts Become a Challenge

Gradle doesn't work much differently in the background than Maven. Therefore, some translations are necessary. Features
like the Dependency Catalog, the Maven Release Plugin, the Dependabot, and many more are actually workarounds for basic
functions that Maven already brings with it. With the flexibility of Gradle, complex build configurations often arise,
which are difficult to maintain. Gradle plugins often have compatibility problems, limits, or limited further
developments. These problems arise due to the evolving nature of the Gradle ecosystem, the variety of environments in
which Gradle is used, and the specific implementation and maintenance effort for each plugin. Everything is
interconnected.

### The Domino Effect of Gradle - A Nightmare Scenario in the Real World

I have seen many microservices that were only a few years old and were already unmanageable due to Gradle. It is important to mention that this is not the first time I have seen this, and no, it was not junior devs.

My **task was to perform a Spring Boot 2.x to 2.7 upgrade**. Spoiler: I gave up after a year. The problems in brief:

* The Gradle build file requires -> Downgrade of my local Java version to 11 (WTF) (Normally Java is backward
  compatible - there are also workaround tools like SdkMan...)
* The Spring Boot update requires -> Gradle update (WTF)
* The Gradle update requires -> Plugin update
* The plugin update requires -> Groovy update (WTF)
* The Groovy update requires -> Test Framework and test updates (WTF)
* The test framework update requires -> Dependency updates
* \[...]
  Furthermore, some plugins do not work with newer Gradle versions, some are no longer being further developed,
  are incompatible with other plugins, do work only with Gradle KTS, not with Gradle Groovy, or simply have limits. Even plugins from large vendors like Spring have limited functionality compared to their Maven plugins. In the end, I have a cool, short Gradle build file that no one can properly maintain, not even the developers who wrote it, and they still love Gradle. I know only a few who can seriously understand or write Gradle scripts.

### The Rediscovery of the Strength of Maven - Utilizing the Magic Powers of Maven

Here are my favorite features of Maven:
Plugins can be launched and configured directly from the command line without having to be defined beforehand. Plus, they are largely independent of other plugin configurations.

| Example Command                      | Description                                                                                                                           | Link                                                                     | 
|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `mvn versions:use -latest-versions`   | Update versions - who needs Dependabot? Yes, my projects have been updated to the latest version smoothly for years without annoying merge requests | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0` | Set project version...                                                                                                                           | https://www.mojohaus.org/versions/versions-maven-plugin/index.html       |
| `mvn license:add-third-party`         | List dependencies and display their licenses (can even fail with excluded licenses)                                           | https://www.mojohaus.org/license-maven-plugin/index.html                 | 

This list could go on forever. It somewhat reminds me of GitHub Workflow Steps.

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)

### Don't you like XML?

No problem! Simply write your build file in `ruby`, `groovy`, `scala`, `yaml`, `atom`, or `Java`. The Polyglot Extension (https://github.com/takari/polyglot-maven) makes it possible. To try it out, just run `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` and your build file will be translated in a few milliseconds. It's a shame there's no reliable Maven <> Gradle translator :( Yes, Maven build files are big, but they're also very easy to understand. Refinements or debugging can be done in no time.

### Age is just a number - Mavens Stability and Evolution

Admittedly, Maven has been around for quite a while and its aesthetics may not meet today's standards. However, the
longevity of Maven has allowed it to adapt and evolve. Maven operates independently from your project. Build files can
easily be reused. Plugins run in a sandbox and are independent of each other and independent of the Java or Maven
version. This design promotes stability and predictability, and makes it easy to manage complex build processes without
unexpected conflicts.

### Conclusion

Nowadays the development environment is overloaded with many tasks and technologies for developers. In the search for
simplicity and automation, Gradle has emerged as a modern build tool, but has brought its own challenges. Without
question, the concept of Gradle is good! But given the complexity and the time invested in Gradle build scripts, the
question arises whether it wouldn't be simpler to extend Maven. With plugins and extensions, Maven could be refreshed
and simplified at any time. Wouldn't further development be much more exciting and also more sustainable than jumping
from one technology to the next?

### Links

* [Moving Back from Gradle to maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### Contact

The text provided is already in English. It is a markdown hyperlink to GitHub Issues:
[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
