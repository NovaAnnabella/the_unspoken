---
title: "Back to Maven?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "The elusive search for simplicity and a short journey to rediscover the power of Maven."
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# Back to Maven?

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

## 10 years of Gradle. In search of relief and a short journey to the rediscovery of the strength of Maven.



### Maximizing the Potential of Developers - We Need More Time-Saving Tools

Topics that are often overlooked or rarely discussed interest me. Often there are cool technologies in use, but hardly
anyone talks about the problems associated with them. Development has become very complex these days. With cool
buzzwords such as "Serverless", "Low Code", "IaC", "Big Data", "Cloud", "DevOps", "You Build it You Run it" etc.
developers already have more than enough additional tasks to cope with. More tasks mean that there are hardly any
experts left and something is always neglected for focus. Therefore, automations and time savings are mega important.
"Don't make me think" and "Works out of the box" are already good quality features, which I still can't see in Gradle.
To be fair, Gradle is not the only modern tool that makes work for us instead of simplifying it.

### The illusory search for simplicity and automation

Since SOAP, I have had a deep-rooted aversion to XML-based configurations. With Gradle, I had hoped that writing bind-scripts would be a breeze. Unfortunately, my hopes and my motivation decreased with each iteration. Gradle strives for flexibility and sacrifices automation and quality for it. Developers blindly follow the trend without regard for the impact on the reliability of the software. To keep Gradle build scripts simple and low-maintenance, strong discipline is required. Such discipline is rare to find in the source code and therefore it is even rarer in the build scripts.

### Translations and Workarounds - When Build Scripts Become a Challenge

Gradle doesn't work much differently in the background than Maven. Therefore, some translations are necessary. Features
such as the Dependency Catalog, the Maven Release Plugin, the Dependabot, and many more are actually workarounds for
basic functions that Maven already provides. With the flexibility of Gradle, complex build configurations often arise,
which are difficult to maintain. Gradle plugins often have compatibility issues, limits, or limited further
developments. These problems arise due to the evolving nature of the Gradle ecosystem, the variety of environments in
which Gradle is used and the specific implementation and maintenance effort for each plugin. Everything is
interconnected.

### The Domino Effect of Gradle - A Nightmare Scenario in the Real World

I have seen many microservices that were only a few years old and already unmaintainable due to Gradle. It's important to mention that this is not the first time I've seen something like this, and no, they were not junior developers.

My **task was to carry out a Spring Boot 2.x to 2.7 upgrade**. Spoiler: I gave up after a year. The problems in brief:

* The Gradle build file requires -> Downgrade of my local Java version to 11 (WTF) (normally Java is 
  backward compatible - there are also workaround tools like SdkMan...)
* The Spring Boot update requires -> Gradle update (WTF)
* The Gradle update requires -> Plugin update
* The Plugin update requires -> Groovy update (WTF)
* The Groovy update requires -> Test framework and test updates (WTF)
* The Test framework update requires -> Dependency updates
* \[...]
  Additionally, some plugins do not work with newer Gradle versions, some are no longer being further
  developed, are incompatible with other plugins, only work with Gradle KTS, not with Gradle Groovy, or
  simply have limits. Even plugins from big providers like Spring have limited functionality compared to their Maven plugins.
  In the end, I have a cool, short Gradle build file that nobody can properly maintain,
  not even the developers who wrote it, and they still love Gradle. I know only a few who
  can seriously understand or write Gradle scripts.

### The Rediscovery of the Strength of Maven - Utilizing the Magic Powers of Maven

Here are my favorite features of Maven:
Plugins can be started and configured directly from the command line without having to be defined in advance. Plus, they are largely independent of other plugin configurations.

| Example Command                       | Description                                                                                                                                          | Link                                                                     |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `mvn versions:use -latest-versions`   | Update versions - who needs Dependabot? Yes, my projects have been smoothly updated to the latest version for years, without annoying merge requests | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0` | Set project version...                                                                                                                               | https://www.mojohaus.org/versions/versions-maven-plugin/index.html       |
| `mvn license:add-third-party`         | List dependencies and display their licenses (can even fail with excluded licenses)                                                                  | https://www.mojohaus.org/license-maven-plugin/index.html                 |

This list could go on forever. It somehow reminds me of GitHub Workflow Steps.

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)

### You Don't Like XML?

No problem! Just write your Build File in `ruby`, `groovy`, `scala`, `yaml`, `atom` or `Java`. The Polyglot
Extension (https://github.com/takari/polyglot-maven) makes it possible. To try it out,
simply run `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` and in
a few milliseconds your Build File is translated. It's a shame there's no reliable Maven <> Gradle translator. 
Yes, Maven Build Files are large, but also very easy to understand. Corrections or debugging are done in seconds.

### Age is Just a Number - Maven's Stability and Evolution

Admittedly, Maven has been around for quite a while and its aesthetics may not meet today's standards. However, Maven's
longevity has made it possible to adapt and evolve. Maven works independently from your project. Build files can simply
be reused. The plugins run in a sandbox and are independent of each other and independent of the Java or Maven version.
This design promotes stability and predictability and makes it easy to manage complex build processes without unexpected
conflicts.

### Conclusion

Nowadays, the development environment is overloaded with many tasks and technologies for developers. In the search for
simplicity and automation, Gradle has emerged as a modern build tool, but it has brought its own challenges. Without
question, the concept of Gradle is good! However, given the complexity and the time invested in Gradle build scripts,
the question arises whether it wouldn't be easier to extend Maven. With plugins and extensions, Maven could be freshened
up and simplified at any time. Wouldn't further development be much more exciting and also more sustainable than jumping
from one technology to the next?

### Links

* [Moving Back from Gradle to maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### Contact

The text you provided is already in English. The marked down link directs to a page to choose a new issue on GitHub. The translation remains: 
[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
