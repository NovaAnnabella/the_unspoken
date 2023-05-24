---
title: "回归 Maven？"
date: 2023-05-01T01:01:01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "对简单性的艰难追求和重新发现 Maven 强大之旅"
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---

# 回归 Maven？

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

## Gradle 十年：对简单性的艰难追求和重新发现 Maven 强大之旅。

### 最大化开发者潜力

#### 我们需要更多的省时工具

往往被忽视或很少讨论的主题引起了我的兴趣。通常有很酷的技术在使用，但几乎没有人谈论与之相关的问题。
在当今，开发变得非常耗时。
以“无服务器”、“低代码”、“基础设施即代码”、“大数据”、“云”、“DevOps”、“You Build it You run it” 等酷炫词汇，
开发者已经有了足够多的额外任务要处理。更多任务意味着几乎没有专家剩下，而且总有一些事情被忽视。因此，自动化和节省时间非常重要。
"不让我思考" 和 "开箱即用" 已经是好的质量特性，但我在 Gradle 中还没有看到它们。公平地说，Gradle
并不是唯一一个让我们的工作变得更艰难而不是更容易的现代工具。

### 看似简单和自动化的追求

从 SOAP 开始，我对基于 XML 的配置有一种根深蒂固的厌恶感。我曾希望使用 Gradle 编写构建脚本会轻而易举。然而，每一次都让我对希望和动力失去信心。Gradle
追求灵活性，为此牺牲了自动化和质量。开发人员盲目追随潮流，不顾对软件可靠性的影响。要保持 Gradle
构建脚本简单且易维护，需要强大的纪律性。这种纪律性在源代码中已经很少见，因此在构建脚本中更是少之又少。

### 翻译和解决方案

#### 当构建脚本成为纪律的挑战

Gradle 在后台的工作方式与 Maven 并没有太大区别。因此，需要进行一些翻译。诸如依赖目录、Maven Release 插件、Dependabot 等功能实际上是对
Maven 已经具备的基本功能的变通方法。由于 Gradle 的灵活性，构建配置通常会变得复杂且难以维护。
由于一切都彼此相互关联，Gradle 插件经常存在兼容性问题、限制或有限的进展。这些问题可能源于 Gradle 生态系统的不断发展，Gradle
部署环境的多样性，以及每个插件所需的特定实施和维护工作。

### Gradle的多米诺效应

#### 真实世界的噩梦场景

我见过很多只有2年历史的微服务，由于Gradle的原因已经无法继续维护。
值得一提的是，这不是我第一次见到这种情况，而且不是由初级开发人员造成的。

所以，我的**任务是进行Spring Boot 2.5到2.7的升级**。剧透：我在一年后放弃了！简述问题如下：

* Gradle构建文件需要 -> 将我的本地Java降级到11（什么鬼）（Java通常是向下兼容的 - 还有一些像SdkMan这样的解决工具...）
* Spring Boot升级需要 -> Gradle升级（什么鬼）
* Gradle升级需要 -> 插件升级
* 插件升级需要 -> Groovy升级（什么鬼）
* Groovy升级需要 -> 测试框架和测试更新（什么鬼）
* 测试框架更新需要 -> 依赖项更新
* \[...]
  此外，一些插件不适用于较新的Gradle版本，一些插件不再维护，与其他插件不兼容，仅适用于Gradle KTS而不是Gradle
  Groovy，或者存在错误。即使是像Spring插件这样的大公司的插件，与它们的Maven插件相比，功能也有限。
  最后，我有一个很酷的简短的Gradle构建文件，没有人能够维护它，甚至连编写它的开发人员也不能，但他们仍然热爱Gradle。

### 重新发现Maven的力量

#### 发挥Maven的魔力

以下是我最喜欢的Maven功能：
插件可以从命令行启动和配置，无需定义，并且与其他插件配置高度独立。

| 示例命令                                  | 描述                                                       | 链接                                                                       | 
|---------------------------------------|----------------------------------------------------------|--------------------------------------------------------------------------|
| `mvn versions:use -latest-versions`   | 更新版本 - 谁需要Dependabot？是的，我的项目多年来一直更新到最新版本，没有问题，也没有烦人的合并请求 | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0` | 设置项目版本...                                                | https://www.mojohaus.org/versions/versions-maven-plugin/index.html       |
| `mvn license:add-third-party`         | 列出依赖项及其许可证（甚至可以在排除的许可证上失败）                               | https://www.mojohaus.org/license-maven-plugin/index.html                 | 

这个列表可以无穷无尽地延续下去。它在某种程度上让我想起了GitHub工作流步骤。

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)

### 你不喜欢XML吗？

没问题！只需用`ruby`、`groovy`、`scala`、`yaml`、`atom`或`Java`
编写构建文件。[Polyglot扩展](https://github.com/takari/polyglot-maven)使这成为可能。
只需运行`mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml`，几毫秒后，您的构建文件就被翻译了。
可惜没有可靠的Maven <> Gradle转换器:( 是的，Maven构建文件很大，但也非常容易理解。您可以在短时间内完成细化或调试。
有趣的事实：除了Hello World示例外，当您应用更多自动化时，Gradle文件的增长甚至比Maven文件更大。

### 年龄只是个数字

#### Maven的韧性和演进

诚然，Maven已经存在一段时间了，其外观可能不符合当今的标准。然而，Maven的长寿让它能够适应和演进。Maven独立于您的项目。构建文件可以轻松重复使用。
插件在一个沙盒中运行，彼此独立，与Java或Maven的版本无关。这种设计促进了稳定性和可预测性，使得管理复杂的构建过程变得容易，避免了意外冲突。

### 结论

如今，开发环境对开发人员而言充满了许多任务和技术。在追求简单和自动化的过程中，Gradle作为一种现代构建工具应运而生，但也带来了自身的挑战。
毫无疑问，Gradle的概念是好的！但是考虑到Gradle构建脚本的复杂性和投入的时间，是否将Maven扩展更容易呢？通过插件和扩展，Maven始终可以保持更新和简化。与其不断跳跃到下一个技术，进一步发展是不是更加令人兴奋和可持续呢？

### 链接

* (Moving Back from Gradle to maven)[https://phauer.com/2018/moving-back-from-gradle-to-maven/]

### 联系方式

[GitHub 问题](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
