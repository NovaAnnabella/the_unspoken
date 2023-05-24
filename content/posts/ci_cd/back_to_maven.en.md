---
title: "Back to Maven?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "The elusive quest for simplicity and a short journey to rediscovering the power of Maven"
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---

# Back to Maven?

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

## 10 years of Gradle. The elusive quest for simplicity and a short journey to rediscovering the power of Maven.

### Maximising Developer Potential

#### We need more time-saving tools

Topics that are often overlooked or rarely discussed interest me. Often cool technologies are in use, but hardly anyone
talks about the problems associated with them.
Development has become very time-consuming these days.
With cool buzzwords like "serverless", "low code", "IaC", "Big Data", "Cloud", "DevOps", "You Build it You run it" etc.,
developers already have more than enough extra tasks to deal with. More tasks, means there are hardly any experts left
and something is always neglected for focus. That's why automation and time savings are very important. "Don't make me
think" and "Works out of the Box" are already good quality features that I can't see in Gradle yet. To be fair, Gradle
is not the only modern tool that makes our work instead of making it easier.

### The illusory quest for simplicity and automation

Ever since SOAP, I've had a deep-rooted aversion to XML-based configurations. With Gradle, I had hoped that writing bind
scripts would be a breeze. Unfortunately, my hopes and motivation diminished each time. Gradle strives for flexibility
and sacrifices automation and quality for it. Developers blindly follow the trend without regard for the impact on
software reliability. Keeping Gradle build scripts simple and low-maintenance requires strong discipline. Such
discipline is already rare in source code, and therefore it is even rarer in build scripts.

### Translations and Workarounds

#### When Build Scripts Become a Discipline Challenge

Gradle doesn't work much differently in the background than Maven. Therefore, some translations are necessary. Features
like the Dependency Catalog, the Maven Release Plugin, the Dependabot and many more are actually workarounds for basic
features that Maven already brings. With Gradle's flexibility comes often complex build configurations that are hard to
maintain.
Because everything is interconnected, Gradle plugins often have compatibility issues, limits or limited advancements.
These issues can arise due to the evolving nature of the Gradle ecosystem, the diversity of environments in which Gradle
is deployed, and the specific implementation and maintenance effort required for each plugin. I know only a few who can
truly understand or write Gradle scripts.

### Gradle's The Domino Effect

#### A Real World Nightmare Scenario

I have seen a lot of microservices that were only 2 years old and were already no longer maintainable because of Gradle.
Important to mention, it's not the first time I see this and no it was not a Junior.

So my **mission was to do a Spring Boot 2.5 to 2.7 upgrade**. Spoiler: I gave up after one year! Problems in short:

* Gradle build file needs -> Downgrade my local Java to 11 (WTF) (Java usually is downwards compatible - there are also
  workaround tools like SdkMan...)
* Spring Boot update needs -> Gradle update (WTF)
* Gradle update needs -> Plugin update
* Plugin update -> need Groovy update (WTF)
* Groovy update -> needs Test Framework & Test updates (WTF)
* Test Framework update needs -> dependency updates
* \[...]
  In addition, some plugins don't work with newer Gradle versions, some are no longer maintained, are incompatible with
  other plugins, only work with Gradle KTS, not Gradle Groovy, or just have bugs. Even plugins from big players like
  Spring Plugins have limited functionality compared to their Maven plugins.
  At the end I have a cool short Gradle build file that nobody is able to maintain, not even the developers who wrote
  it, and they still love Gradle.

### Rediscovering Maven's Power

#### Harnessing Maven's Wizardry

Here are my favourite features of Maven:
Plugins can be started and configured from the command line without definition and highly independent of other plugin
configurations.

| Example Command                       | Description                                                                                                                               | Link                                                                     | 
|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `mvn versions:use -latest-versions`   | Update versions - who needs dependabot? Yes my projects updating since years to latest without issues and without annoying merge requests | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0` | Set project version...                                                                                                                    | https://www.mojohaus.org/versions/versions-maven-plugin/index.html       |
| `mvn license:add-third-party`         | List Dependencies and Their licenses (can be even fail on excluded licenses                                                               | https://www.mojohaus.org/license-maven-plugin/index.html                 | 

This list could go on forever. It reminds me somehow of GitHub Workflow Steps.

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)

### You don't like XML?

No problem! Just write your build file in `ruby`, `groovy`, `scala`, `yaml`, `atom`
or `Java`. [The Polygot Extension](https://github.com/takari/polyglot-maven) makes it possible.
Just run `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` and in a few
milliseconds your build file is translated. Too bad there is no reliable Maven <> Gradle translator :(
Yes, Maven build files are big, but also very easy to understand. Refinements or debugging are done in no time.
Fun fact: Beside the Hello World examples, Gradle files grows even way bigger than maven files when you apply more
automations.

### Age Is Just a Number

#### Maven's Resilience and Evolution

Admittedly, Maven has been around for a while and its aesthetics may not be up to today's standards. However, Maven's
longevity has allowed it to adapt and evolve. Maven works independently of your project. Build files can be easily
reused.
Plugins run in a sandbox and are independent of each other and independent of the Java or Maven version. This design
promotes stability and predictability and makes it easy to manage complex build processes without unexpected conflicts.

### Conclusion

Nowadays, the development environment is overloaded with many tasks and technologies for developers. In the quest for
simplicity and automation, Gradle has emerged as a modern build tool but has brought its own challenges.
Without question, the concept of Gradle is good! But given the complexity and time invested in Gradle build scripts, the
question arises whether it would not be easier to extend Maven. With plugins and extensions, Maven could always be
refreshed and simplified. Wouldn't further development be much more exciting and also more sustainable than jumping from
one technology to the next?

### Links

* (Moving Back from Gradle to maven)[https://phauer.com/2018/moving-back-from-gradle-to-maven/]

### Contact

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
