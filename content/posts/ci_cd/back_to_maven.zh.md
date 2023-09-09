---
title: "回到Maven？"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "难以捉摸的寻求简单性，以及重新发现Maven力量的短暂旅程。"
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# 回到Maven？

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

## Gradle的10年。寻找缓解并简短回顾Maven的强大之力。



### 最大化开发者的潜力 - 我们需要更多节省时间的工具

我对经常被忽视或很少讨论的主题感兴趣。酷炫的技术经常被使用， 但几乎没有人谈论与之相关的问题。 发展至今已经变得非常繁琐。 随着像“无服务器”、“低代码”、“IaC”、“大数据”、“云”、“DevOps”、“你建它你运行它”
等酷炫的热词，开发人员已经有更多的额外任务要处理。更多的任务意味着几乎没有 专家存在，总是会有些什么被忽视来寻求关注。因此，自动化和节省时间变得非常 重要。“不要让我思考”和“开箱即用”已经是我在Gradle中还
看不到的好的质量标准。为了公平，Gradle不是唯一让我们干活而不是简化它的现代工具。

### 对简单性和自动化的虚幻追求

自从SOAP以来，我对基于XML的配置深感厌恶。我曾希望使用Gradle写绑定脚本会变得轻而易举，但是每次的结果都让我的希望和动力降低。Gradle追求的是灵活性，为此牺牲了自动化和质量。开发者们盲目地跟随潮流，不考虑对软件稳定性的影响。为
了使Gradle构建脚本简单且易于维护，需要强烈的纪律性。这种纪律性在源代码中就已经很少见，因此在构建脚本中就更加罕见了。

### 翻译和变通方法 - 当构建脚本成为挑战时

Gradle在后台的工作方式与Maven并无太大差异。因此，需要进行一些翻译。如Dependency Catalog，Maven Release
Plugin，Dependabot以及许多其他功能实际上都是Maven已经提供的基本功能的替代方案。由于Gradle的灵活性，经常会出现复杂的构建配置，这些配置很难维护。
Gradle插件经常存在兼容性问题，限制或有限的发展空间。这些问题是由于Gradle生态系统的发展性，Gradle的使用环境的多样性，以及每个插件的特定实施和维护成本所导致的。所有的一切都是相互关联的。

### Gradle的多米诺骨牌效应 - 现实世界中的恶梦场景

我已经看到很多微服务，它们只有几年的历史，但由于Gradle的原因已经不再维护。很重要的一点是，这并不是我第一次看到这样的情况，而且，不，它们不是初级开发人员。

我的**任务是进行一个Spring Boot 2.x到2.7的升级**。剧透：我做了一年都放弃了！问题简述：

* Gradle构建文件需要 -> 降级我本地的Java版本到11（WTF）（通常Java
  是向下兼容的 - 这里也有像SdkMan这样的解决方案工具...)
* Spring Boot更新需要 -> Gradle更新 (WTF)
* Gradle更新需要 -> 插件更新
* 插件更新需要 -> Groovy更新 (WTF)
* Groovy更新需要 -> 测试框架和测试更新 (WTF)
* 测试框架更新需要 -> 依赖性更新
* \[...\]
  此外，一些插件不能与新版本的Gradle一起使用，一些已经停止开发，与其他插件不兼容，只能用Gradle KTS，不能用Gradle Groovy，或者有一些限制。即使是像Spring这样的大型提供商的插件，与它们的Maven插件相比，也有功能限制。最后，我得到一个酷酷的，短暂的Gradle构建文件，没有人能正确地维护它，甚至包括那些写它的开发人员，他们仍然喜欢Gradle。我只知道很少有人能真正理解或编写Gradle脚本。

### 重新发现Maven的力量 - 利用Maven的魔法力量

以下是我最喜欢的Maven功能：
插件可以直接从命令行启动和配置，而无需预先定义。
而且，它们大都独立于其他插件配置。

| 示例命令                        | 描述                                                                                                                                                    | 链接                                                                     | 
|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `mvn versions:use -latest-versions`   | 更新版本 - 谁需要Dependabot? 是的，我的项目已经多年来顺利升级到最新版本，无需烦人的合并请求 | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0` | 设置项目版本...                                                                                                                                         | https://www.mojohaus.org/versions/versions-maven-plugin/index.html       |
| `mvn license:add-third-party`         | 列出依赖项并显示其许可证（甚至可以在排除的许可证上失败）                                                                                                 | https://www.mojohaus.org/license-maven-plugin/index.html                | 

这个列表可以无休止地继续下去。它在某种程度上提醒我GitHub Workflow Steps。

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)


### 你不喜欢XML吗？

没有问题！只需将你的构建文件写在`ruby`，`groovy`，`scala`, `yaml`, `atom`或`Java`中。 Polyglot扩展（https://github.com/takari/polyglot-maven）使其成为可能。 要试一试，只需执行`mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml`，然后在几毫秒内你的构建文件就会被翻译过来。 可惜没有可靠的Maven <> Gradle翻译器:(

是的，Maven构建文件很大，但也非常易于理解。 可以很快地进行修改或调试。

### 年龄只是一个数字 - Mavens的稳定性和演化

诚然，Maven已经存在很长时间了，它的美感可能不符合今天的标准。然而， Maven的长寿性使其能够适应和进化。Maven独立 于您的项目。构建文件可以简单地复用。插件在沙箱中运行，并且彼此独立，与Java或Maven版本无关。
这种设计促进了稳定性和可预测性，使得管理复杂的构建过程而不会有意外冲突变得简单。

### 结论

如今，开发环境因开发人员的许多任务和技术而过于复杂。在寻求简单化和自动化的过程中，Gradle作为一个现代化的构建工具出现了，但也带来了自己的挑战。毫无疑问，Gradle的概念是好的！但面对Gradle构建脚本所投入的复杂性和时间，人们不禁
会问，是否扩展Maven会更简单。通过插件和扩展，我们可以随时刷新和简化Maven。不是跳转到下一个技术，而是继续发展，不会更加激动人心并且更持久吗？

### 链接

* [从 Gradle 切换回 Maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### 联系方式

[GitHub问题](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose)。
