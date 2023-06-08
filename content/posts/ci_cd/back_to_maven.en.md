---
title: "Back to Maven?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "The elusive search for simplicity and a brief journey to rediscover the power of Maven."
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# Back to Maven?

This markdown text is already in English and contains an image of a comparison between Maven and Gradle build tools,
with a hyperlink to an article on moving back from Gradle to Maven.

## 10 years of Gradle. In search of ease and a short journey to rediscovering the strength of Maven.

This markdown text is empty and does not contain any content to translate.

### Maximizing the Potential of Developers - We need more time-saving tools.

Topics that are often overlooked or rarely discussed interest me. Often, cool technologies are used, but hardly anyone
talks about the problems that are associated with them. Development has become very complex nowadays. With cool
buzzwords like "Serverless", "Low Code", "IaC", "Big Data", "Cloud", "DevOps", "You Build it You run it", etc.,
developers already have enough additional tasks to handle. More tasks mean that there are hardly any experts left and
something is always neglected for the focus. Therefore, automations and time savings are very important. "Don't make me
think" and "Works out of the Box" are already good quality features that I cannot see in Gradle yet. To be fair, Gradle
is not the only modern tool that makes work for us instead of making it easier.

### The illusory search for simplicity and automation

Since SOAP, I have a deep aversion to XML-based configurations. With Gradle, I had hoped that writing binding scripts would be child's play. Unfortunately, my hopes and motivation dwindled from time to time. Gradle strives for flexibility and sacrifices automation and quality for it. Developers blindly follow the trend without regard for the impact on software reliability. To keep Gradle build scripts simple and easy to maintain, strong discipline is needed. Such discipline is already rare in source code and therefore even rarer in build scripts.

### Translations and Workarounds  - When Build Scripts Become a Challenge

Gradle does not work much differently in the background than Maven. Therefore, some translations are necessary. Features
such as the Dependency Catalog, the Maven Release Plugin, Dependabot, and many more are actually workarounds for basic
functions that Maven already brings. With the flexibility of Gradle, complex build configurations often arise that are
difficult to maintain. Gradle plugins often have compatibility issues, limits, or limited further development. These
problems arise due to the evolving nature of the Gradle ecosystem, the diversity of the environments in which Gradle is
used, and the specific implementation and maintenance effort for each plugin. Everything is interconnected.

### The Domino Effect of Gradle - A Nightmare Scenario in the Real World

I have seen many microservices that were only a few years old and were already not maintainable due to Gradle. It is important to mention that this is not the first time I have seen something like this, and no, they were not junior devs.

My **task was to perform a Spring Boot 2.x to 2.7 upgrade**. Spoiler: I gave up after a year! The problems, in short:

* The Gradle build file requires -> downgrading my local Java version to 11 (WTF) (Usually Java is backward compatible - there are workaround tools like SdkMan...)
* The Spring Boot update requires -> Gradle update (WTF)
* The Gradle update requires -> plugin update
* The plugin update requires -> Groovy update (WTF)
* The Groovy update requires -> test framework and test updates (WTF)
* The test framework update requires -> dependency updates
* \[...\]
  In addition, some plugins do not work with newer Gradle versions, some are no longer being developed, are incompatible with other plugins, only work with Gradle KTS, not with Gradle Groovy, or have limits. Even plugins from big providers like Spring have restricted functionality compared to their Maven plugins. In the end, I have a cool, short Gradle build file that nobody can maintain properly, not even the developers who wrote it, and they still love Gradle. I only know a few who can understand or write Gradle scripts seriously.

### Rediscovering the Strength of Maven - Leveraging the Magic Powers of Maven

Here are my favorite features of Maven:
Plugins can be started and configured directly from the command line without having to define them beforehand. Plus, they are largely independent of other plugin configurations.

| Example command                         | Description                                                                                                          | Link                                                                     |
|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `mvn versions:use -latest-versions`     | Update versions - who needs Dependabot? Yes, my projects have been smoothly updated to the latest version for years, no annoying merge requests required  | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0`   | Set project version...                                                                                               | https://www.mojohaus.org/versions/versions-maven-plugin/index.html       |
| `mvn license:add-third-party`           | List dependencies and show their licenses (can even fail on excluded licenses)                                      | https://www.mojohaus.org/license-maven-plugin/index.html                 |

This list could go on forever. It reminds me somehow of GitHub Workflow Steps.

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)

### You don't like XML?

No problem! Simply write your Build File in `ruby`, `groovy`, `scala`, `yaml`, `atom` or `Java`. The Polygot Extension (https://github.com/takari/polyglot-maven) makes it possible. To try it out, simply run `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` and within a few milliseconds your Build File will be translated. Too bad there isn't a reliable Maven <> Gradle translator :( Yes, Maven Build Files are big, but they are also very easy to understand. Adjustments or debugging are done in no time.

### Age is just a number - Maven's stability and evolution

Admittedly, Maven has been around for quite some time and its aesthetics may not meet today's standards. However,
Maven's durability has allowed it to adapt and evolve. Maven works independently of your project. Build files can be
easily reused. Plugins run in a sandbox and are independent of each other and independent of the Java or Maven version.
This design promotes stability and predictability and makes it easy to manage complex build processes without unexpected
conflicts.

### Conclusion

Nowadays, the development environment is overloaded with many tasks and technologies for developers. In search of
simplicity and automation, Gradle has emerged as a modern build tool, but it has brought its own challenges. Without
question, the concept of Gradle is good! However, given the complexity and time invested in Gradle build scripts, the
question arises whether it would not be easier to extend Maven. With plugins and extensions, Maven could be refreshed
and simplified at any time. Would further development not be much more exciting and sustainable than jumping from one
technology to the next?

### Links

The text is already in English and it is a markdown link that leads to an article titled "Moving Back from Gradle to Maven" on the website https://phauer.com/2018/moving-back-from-gradle-to-maven/.

### Contact

This markdown text is already in English. It is a hyperlink to the "GitHub Issues" page of a repository named
"the_unspoken" on the GitHub platform provided by the user "NovaAnnabella".
