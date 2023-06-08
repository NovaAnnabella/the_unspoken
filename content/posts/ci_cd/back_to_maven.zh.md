---
title: "回到Maven？"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "追寻简单的艰难之路，以及重新发现Maven的优势"
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# 回到Maven？

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/) 

请注意：这是一段Markdown文本，无需翻译。

## Gradle 十周年。寻求简化的途径及重新发现 Maven 的优势之旅。

将Markdown文本翻译成中文简体：```\`\`\` ```

### 最大化开发者潜力 - 我们需要更多节省时间的工具

我对常常被忽略或很少讨论的主题感兴趣。通常会使用酷炫的技术，但几乎没有人谈论与之相关的问题。开发现在变得非常复杂。有了“Serverless”，“Low Code”，“IaC”，“Big
Data”，“Cloud”，“DevOps”，“You Build it You run
it”等酷炫的术语，开发者已经有更多的额外任务要解决。更多的任务意味着几乎没有专家，总有一些事情会被忽视。因此，自动化和时间节约是非常重要的。“Don’t make me think”和“Works out of the
Box”已经是很好的质量标准，在Gradle中却看不到。公正地说，Gradle并不是唯一一个让我们更加辛苦而不是更加便利的现代工具。

### 虚幻的简单和自动化探索

自从了解了 SOAP，我对基于 XML 的配置深恶痛绝。我曾希望在使用 Gradle 时编写绑定脚本会很容易，但是我的希望和动力逐渐消磨。Gradle
追求灵活性，为此牺牲了自动化和质量。开发人员盲目地追随潮流，而不考虑对软件可靠性的影响。为了使 Gradle 构建脚本简单且易于维护，需要一种强烈的纪律。这种纪律在源代码中已经很少见到，因此在构建脚本中更加罕见。

### 翻译和解决方案 - 当构建脚本变成挑战时

Gradle与Maven在后台处理时并没有太大的不同。因此需要进行一些翻译。像Dependency Catalog、Maven Release Plugin、Dependabot和许多其他功能实际上都是对Maven已经具备的基本功能的变通方
法。在Gradle的灵活性下，通常会出现复杂的构建配置，这些配置很难维护。Gradle插件经常存在兼容性问题、限制或受到限制的发展。这些问题源于Gradle生态系统的发展性质、Gradle被应用的多样性以及每个插件的特定实现和维护工作量。一
切都相互关联。

### Gradle的多米诺效应 - 真实世界中的噩梦场景

我见过许多只有几年历史的微服务，由于Gradle的原因已经无法维护。需要指出的重要一点是，这不是我第一次看到这种情况，也不是因为初级开发人员。

我的任务是升级Spring Boot 2.x到2.7。结局：经过一年的尝试，我放弃了！主要问题如下：

* Gradle Build文件需要->将我的本地Java版本降级到11（WTF）（通常Java是向下兼容的-这里也有类似SdkMan的解决工具...)
* Spring Boot升级需要->Gradle升级（WTF）
* Gradle升级需要->Plugin升级
* Plugin升级需要->Groovy升级（WTF）
* Groovy升级需要->测试框架和测试更新（WTF）
* 测试框架更新需要->依赖项更新
* \[...]
此外，一些插件与较新版本的Gradle不兼容，一些插件不再维护，与其他插件不兼容，仅与Gradle KTS而不是Gradle Groovy一起使用，或仅有限功能。即使是像Spring这样的大厂商的插件与它们的Maven插件相比也有限制功能。最终我获得了一个很酷的、简短的Gradle构建文件，但没有人能够正确维护它，甚至是编写它的开发人员，他们仍然喜爱Gradle。我只知道很少有人真正理解或编写Gradle脚本。

### 重新发现Maven的力量-利用Maven的魔力

以下是我最喜爱的Maven功能：
插件可以直接从命令行启动和配置，无需预先定义，而且它们在很大程度上独立于其他插件配置。

| 示例命令                           | 描述                                                                                                                                              | 链接                                                                   |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| `mvn versions: use -latest-versions` | 更新版本-谁需要Dependabot？是的，我的项目多年来一直能够无需繁琐的合并请求就能轻松升级到最新版本。| https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0` | 设置项目版本...                                                                                                                                                 | https://www.mojohaus.org/versions/versions-maven-plugin/index.html       |
| `mvn license:add-third-party`        | 列出依赖项并显示其许可证（即使在排除许可证的情况下，也可能会失败）                                                                                 | https://www.mojohaus.org/license-maven-plugin/index.html                 | 

这种清单看似无穷无尽。这让我想起了 GitHub Work flow步骤。

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)

### 你不喜欢 XML？

没问题！只需用`ruby`、`groovy`、`scala`、`yaml`、`atom`或`Java`编写您的构建文件。Polygot扩展程序（https://github.com/takari/polyglot-maven）让这成为可能。要尝试一下，请运行`mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml`，您的构建文件将在几毫秒内被翻译。可惜没有可靠的Maven<>Gradle翻译器:(是的，Maven构建文件很大，但也非常易于理解。可以轻松地进行修补或调试。

### 年龄只是一个数字 - Maven 的稳定性和演化

承认，Maven已经存在了相当长的时间，其美学可能不符合当今的标准。但是Maven的耐久性使其能够适应和发展。Maven与您的项目无关，构建文件可以轻松地重复使用。插件在沙盒中运行，彼此独立，与Java或Maven版本无关。这种设计促进了稳
定性和可预测性，并使管理复杂的构建过程变得容易且没有意外的冲突。

### 结论

现在，开发环境对开发人员而言充满了许多任务和技术。在寻求简单和自动化的同时，Gradle作为一种现代构建工具出现了，但也带来了自己的挑战。毫无疑问，Gradle的概念很好！但鉴于Gradle构建脚本所投入的复杂性和时间，是否扩展Maven会
更容易呢？通过插件和扩展，可以随时刷新和简化Maven。与跳转到下一个技术相比，进一步发展是不是更有趣和可持续的呢？

### 链接

* [从Gradle迁回Maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### 联系我们

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose). 

请将此条目翻译为中文简体
