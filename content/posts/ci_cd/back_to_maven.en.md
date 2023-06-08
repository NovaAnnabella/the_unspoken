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

The markdown text is already in English, and it contains a markdown image with a hyperlink to an article titled "Moving
Back from Gradle to Maven" on the website phauer.com.

## 10 Years of Gradle. In search of relief and a brief journey to rediscover the strength of Maven.

Sorry, there is no text to translate in the given markdown code. It seems to be an empty code block.

### Maximizing the potential of developers - We need more time-saving tools.

I am interested in topics that are often overlooked or rarely discussed. Cool technologies are often in use, but hardly anyone talks about the problems associated with them.
Development has become very time-consuming nowadays.
With cool buzzwords like "Serverless", "Low Code", "IaC", "Big Data", "Cloud", "DevOps", "You Build it You run it", etc., developers already have more than enough additional tasks to handle. More tasks mean that there are hardly any experts left and something is always neglected for the focus. Therefore, automation and time savings are mega important. "Don't make me think" and "Works out of the Box" are already good quality features that I cannot see in Gradle yet. To be fair, Gradle is not the only modern tool that makes work instead of simplifying it.

### The Illusory Search for Simplicity and Automation

Since SOAP, I have had a deep-rooted aversion to XML-based configurations. With Gradle, I had hoped that writing binding scripts would be child's play. Unfortunately, my hopes and motivation dwindled with each passing day. Gradle strives for flexibility at the expense of automation and quality. Developers blindly follow the trend without considering the impact on software reliability. To keep Gradle build scripts simple and easy to maintain, a strong discipline is required. Such discipline is rare even in the source code and therefore even rarer in the build scripts.

### Translations and Workarounds - When Build Scripts Become a Challenge

Gradle doesn't work much differently than Maven in the background. Therefore, some translations are necessary. Features
such as the Dependency Catalog, the Maven Release Plugin, the Dependabot, and many others are actually workarounds for
basic functions that Maven already provides. With the flexibility of Gradle, often complex build configurations arise
that are difficult to maintain. Gradle plugins often have compatibility problems, limits, or limited further
developments. These problems arise due to the evolving nature of the Gradle ecosystem, the diversity of environments in
which Gradle is used, and the specific implementation and maintenance efforts for each plugin. Everything is
interconnected.

### The domino effect of Gradle - A nightmare scenario in the real world

I have seen many microservices that were only a few years old and were already unmanageable due to Gradle. It's important to mention that this is not the first time I have seen such a thing, and no, they were not junior developers.

My task was to upgrade from Spring Boot 2.x to 2.7. Spoiler alert: I gave up after a year! The problems, in short:

* The Gradle build file required me to downgrade my local Java version to 11 (WTF). (Usually, Java is backward compatible - there are also workaround tools like SdkMan...)
* The Spring Boot update requires a Gradle update (WTF).
* The Gradle update requires a plugin update.
* The plugin update requires a Groovy update (WTF).
* The Groovy update requires test framework and test updates (WTF).
* The test framework update requires dependency updates.
* [...]
In addition, some plugins do not work with newer Gradle versions, some are no longer being developed, some are incompatible with other plugins, some only work with Gradle KTS, not with Gradle Groovy, or simply have limits. Even plugins from large providers like Spring have limited functionality compared to their Maven plugins. In the end, I have a cool, short Gradle build file that no one can maintain properly, not even the developers who wrote it, and they still love Gradle. I know only a few who can seriously understand or write Gradle scripts.

### The Rediscovery of the Strength of Maven - Harnessing the Magic Powers of Maven

Here are my favorite features of Maven:
Plugins can be started and configured directly from the command line without being defined beforehand. Plus, they are largely independent of other plugin configurations.

| Example command                       | Description                                                                                                                                                        | Link                                                                     | 
|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `mvn versions:use -latest-versions`   | Update versions - who needs Dependabot? Yes, my projects have been smoothly updated to the latest version for years, without annoying merge requests                   | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0` | Set project version...                                                                                                                                              | https://www.mojohaus.org/versions/versions-maven-plugin/index.html       |
| `mvn license:add-third-party`         | List dependencies and show their licenses (may even fail on excluded licenses)                                                                                        | https://www.mojohaus.org/license-maven-plugin/index.html                 | 

This list could go on and on. It somehow reminds me of GitHub Workflow Steps.

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)

### You don't like XML?

No problem! Just write your build file in `ruby`, `groovy`, `scala`, `yaml`, `atom`, or `Java`. The Polyglot Extension (https://github.com/takari/polyglot-maven) makes it possible. To try it out, simply run `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` and in a few milliseconds your build file will be translated. Too bad there isn't a reliable Maven <> Gradle translator :( Yes, Maven build files are large, but also very easy to understand. Modifications or debugging can be done in no time.

### Age is just a number - Maven's stability and evolution

Admittedly, Maven has been around for a while and its aesthetics may not match today's standards. However, the longevity
of Maven has allowed it to adapt and evolve. Maven works independently of your project. Build files can be easily
reused. The plugins run in a sandbox and are independent of each other and independent of the Java or Maven version.
This design promotes stability and predictability and makes it easy to manage complex build processes without unexpected
conflicts.

### Conclusion

Nowadays, the development environment is overloaded with many tasks and technologies for developers. In search of
simplicity and automation, Gradle has emerged as a modern build tool, but it has brought its own challenges. There is no
doubt that the concept of Gradle is good! However, given the complexity and time invested in Gradle build scripts, the
question arises whether it wouldn't be easier to extend Maven. With plugins and extensions, Maven could be refreshed and
simplified at any time. Wouldn't further development be much more exciting and sustainable than jumping from one
technology to the next?

### Links

The text is already in English. It is a markdown format containing a hyperlink to an article titled "Moving Back from
Gradle to Maven" on the website phauer.com.

### Contact

Here's the English translation of the markdown text: Link to the GitHub Issues page:
https://github.com/NovaAnnabella/the_unspoken/issues/new/choose.
