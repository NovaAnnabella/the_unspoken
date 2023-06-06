---
title: "Back to Maven?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "The Elusive Quest for Simplicity and a Short Journey to Rediscover the Power of Maven."
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---



# Back to Maven?

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

## 10 years of Gradle. In search of relief and a short journey to rediscover the power of Maven.



### Maximizing the potential of developers - we need more time-saving tools

Topics that are often overlooked or rarely discussed interest me. Cool technologies are often in use, but hardly anyone
talks about the problems associated with them. Development has become very costly these days. With cool buzzwords like
"serverless", "low code", "IaC", "Big Data", "Cloud", "DevOps", "You Build it You run it" etc., developers already have
more than enough additional tasks to deal with. More tasks means that there are hardly any experts and something is
always neglected for focus. Therefore, automations and time savings are mega important. "Don't make me think" and "Works
out of the Box" are already good quality features that I don't see yet in Gradle can't see yet. To be fair, Gradle is
not the only modern tool that makes our work instead of making it make it easier.

### The illusory quest for simplicity and automation

Since SOAP, I've had a deep-rooted aversion to XML-based configurations. With Gradle, I had hoped that writing bind
scripts would be a breeze. Unfortunately, my hopes and motivation diminished diminished each time. Gradle strives for
flexibility and sacrifices automation and quality for it. Developers blindly follow the developers blindly follow the
trend without regard for the impact on software reliability. To make Gradle Build scripts simple and low-maintenance
requires strong discipline. Such discipline is already rare in source code and therefore it is even rarer in the build
scripts.

### Translations and Workarounds - When Build Scripts Become a Challenge

Gradle does not work much differently in the background than Maven. Therefore, some translations are necessary. Features
like the Dependency Catalog, the Maven Release Plugin, the Dependabot and many more are actually workarounds for basic
functions that Maven already brings to the table. With Gradle's flexibility often comes complex build configurations,
that are difficult to maintain. Gradle plugins often have compatibility issues, limits, or limited advancements. These
problems arise due to the evolving nature of the Gradle ecosystem, the diversity of the environments in which Gradle is
is used, and the specific implementation and maintenance effort required for each plugin. Everything is interconnected.

### The Gradle domino effect - A nightmare scenario in the real world

I have seen many microservices that were only a few years old and already no longer maintainable due to Gradle. due to
Gradle. Important to mention that this is not the first time I have seen something like this, and no, they were not
Junior Devs. My **task was to perform a Spring Boot 2.x to 2.7 upgrade**. Spoiler: I gave up after a year I gave up!
The problems in brief: * The Gradle build file requires -> downgrade of my local Java version to 11 (WTF) (Normally
Java is  backwards compatible - again, there are workaround tools like SdkMan...) * The Spring Boot update requires ->
Gradle update (WTF) * The Gradle update requires -> Plugin update * The plugin update requires -> Groovy update (WTF) *
The groovy update requires -> test framework and test updates (WTF) * The test framework update requires -> dependency
updates. * \[...]  In addition, some plugins do not work with newer Gradle versions, some are not further  developed,
are incompatible with other plugins, work only with Gradle KTS, not with Gradle Groovy, or simply  simply have limits.
Even plugins from major vendors like Spring have limited functionality compared to their Maven plugins.  limited
functionality. I end up with a cool, short Gradle build file that no one can properly maintain,  not even the
developers who wrote it, and they still love Gradle. I know very few people who  understand Gradle scripts seriously
doer write them.

### Rediscovering the Power of Maven - Harnessing the Magic of Maven

Here are my favorite features of Maven: Plugins can be launched and configured directly from the command line, without
having to define them beforehand need to be defined. Plus, they are largely independent of other plugin configurations.
| Example Command | Description | Link | |---------------------------------------|--------------------------------------
------------------------------------------------------------------------------------------------------------------------
-------|--------------------------------------------------------------------------| | `mvn versions:use -latest-
versions` | Update versions - who needs Dependabot? Yes, my projects have been updated to the latest version for years
without any problems and without annoying merge requests | https://www.mojohaus.org/versions/versions-maven-
plugin/plugin-info.html | | `mvn versions:set -DnewVersion=1.0.0` | Set project version...
| https://www.mojohaus.org/versions/versions-maven-plugin/index.html | | `mvn license:add-third-party` | List
dependencies and show their licenses (may fail even if licenses are excluded) | https://www.mojohaus.org/license-maven-
plugin/index.html | This list could go on forever. It kind of reminds me of GitHub Workflow Steps.
![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)

### You don't like XML?

No problem! Just write your build file in `ruby`, `groovy`, `scala`, `yaml`, `atom` or `Java`. The Polygot Extension
(https://github.com/takari/polyglot-maven) makes it possible. To try it out just run `mvn io.takari.polyglot:polyglot-
translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` and in a few milliseconds your build is milliseconds your
build file is translated. Too bad there is no reliable Maven <> Gradle translator :( Yes, Maven build files are big, but
also very easy to understand. Refinements or debugging are done in no time at all. done.

### Age is just a number - Maven's stability and evolution

Granted, Maven has been around for a while and its aesthetics may not be up to today's standards. However, Maven's
longevity has allowed it to adapt and evolve. Maven works independently of your project. Build files can be easily
reused. Plugins run in a sandbox and are independent of each other and independent of the Java or Maven version. This
design promotes stability and predictability, and makes it easy to manage complex build processes without unexpected
conflicts.

### Fazit

Nowadays, the development environment is overloaded with many tasks and technologies for developers. In the search for
simplicity and automation, Gradle has emerged as a modern build tool, but it has brought its own challenges with it.
Without question, the concept of Gradle is good! However, given the complexity and the time invested in Gradle build
scripts, it begs the question of whether it wouldn't be simpler to extend Maven to extended. With plugins and
extensions, Maven could always be refreshed and simplified. Wouldn't a development not much more exciting and also more
sustainable than jumping from one technology to the next?

### Links

* [Moving Back from Gradle to maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### Contact

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
