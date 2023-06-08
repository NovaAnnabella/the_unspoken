---
title: "回到Maven？"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "寻找简单性的难以捉摸的追求和重新发现Maven的力量的短途旅行"
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# 回到 Maven？

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)


``` 

将此Markdown文本翻译成简体中文：


[！[maven_vs_gradle]（/ images / content / maven_vs_gradle.png）]（https://phauer.com/2018/moving-back-from-gradle-to-maven/）


```

## Gradle 十年。寻求方便之旅和重新发现 Maven 的力量。

翻译如下： ```

### 开发人员潜力的最大化 - 我们需要更多节省时间的工具

我对经常被忽视或很少讨论的主题感兴趣。通常使用了很酷的技术，但几乎没有人谈论相关的问题。开发变得非常耗费时间和精力。使用“无服务器”、“低代码”、“IaC”、“Big Data”、“云计算”、“DevOps”、“You Build it
You run it”等很酷的流行语，意味着开发人员已经有足够多的任务要处理了。更多的任务意味着几乎没有专家，并且总是会有某些事情被忽略。因此，自动化和节省时间非常重要。“不要让我思考”和“开箱即用”已经是很好的质量标志，但在Gradle中
我还没有看到。公平地说，Gradle不是唯一一个让我们感到麻烦的现代工具，而不是让我们更轻松。

### 虚幻的寻求简单化和自动化

自从使用 SOAP 后，我对 XML 基于的配置深恶痛绝。我希望使用 Gradle 可以轻松编写绑定脚本，但是我的希望和动力逐渐消失。Gradle 追求灵活性，为此牺牲了自动化和质量。开发者盲目追随潮流，不考虑对软件可靠性的影响。为了使
Gradle 构建脚本简单且易于维护，需要强大的纪律。这种纪律在源代码中已经很少见，因此在构建脚本中更少见。

### 翻译和解决方案 - 当构建脚本成为挑战时

Gradle 在后台的工作与 Maven 并没有太大的区别。因此需要进行一些翻译。诸如依赖目录、Maven Release 插件、Dependabot 等功能实际上都是对 Maven 已经具备的基本功能的解决方案。由于 Gradle
的灵活性，通常会产生难以维护的复杂构建配置。 Gradle 插件经常面临兼容性问题、限制或受到瓶颈影响，这些问题是由于 Gradle 生态系统的发展性质，以及在使用 Gradle
的多样化环境和每个插件的特定实现和维护成本造成的。所有这些都是相互关联的。

### Gradle的多米诺骨牌效应 - 真实世界中的噩梦情景

我见过很多年轻的微服务，由于Gradle的缘故而难以维护。需要强调的是，这并不是我第一次看到这样的情况，而且也不是由初级开发人员所造成的。

我的任务是将Spring Boot 2.x升级到2.7。剧透：我放弃了！简要列出的问题如下：

- Gradle Build文件需要将我的本地Java版本降级至11（WTF）（通常情况下，Java是向下兼容的 - 这里有一些类似SdkMan的解决工具...）
- Spring Boot更新需要Gradle更新（WTF）
- Gradle更新需要插件更新
- 插件更新需要Groovy更新（WTF）
- Groovy更新需要测试框架和测试更新（WTF）
- 测试框架更新需要依赖项更新
- 等等...

此外，一些插件与较新的Gradle版本不兼容，一些插件不再维护，不兼容其他插件，只能使用Gradle KTS而不能使用Gradle Groovy，或者仅仅具有某些限制。即使是像Spring这样的大供应商的插件与其Maven插件相比,也具有功能上的限制。最终，我得到了一个很棒但是短小的Gradle Build文件，但是甚至连编写它的开发人员也无法进行适当的维护，并且他们仍然喜欢Gradle。我只知道很少人可以真正理解或编写Gradle脚本。

### 重新发现Maven的强大 - 发挥Maven的魔力

这里是我最喜欢的Maven功能：
插件可以直接从命令行启动和配置，而不需要事先定义。此外，它们在很大程度上独立于其他插件配置。

| 示例命令                            | 描述                                                                                                                                                                                                                                                | 链接                                                                     |
|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `mvn versions:use -latest-versions`   | 更新版本-谁需要Dependabot？ 是的，我的项目已经在多年中被顺利更新到最新的版本，而无需烦人的合并请求                                                                                                                                           | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0` | 设置项目版本...                                                                                                                                                                                                                            | https://www.mojohaus.org/versions/versions-maven-plugin/index.html       |
| `mvn license:add-third-party`         | 列出依赖项并显示其许可证（甚至可能失败于已排除的许可证）                                                                                                                                                                                    | https://www.mojohaus.org/license-maven-plugin/index.html                 | 

这个列表可以无休止地继续下去。它让我想起了GitHub工作流程步骤。

！[maven_plugin_command_line_args]（/ images / content / maven_plugin_command_line_args.png）

### 你不喜欢 XML 吗？

没问题！只需用 `ruby`、`groovy`、`scala`、`yaml`、`atom` 或 `Java` 编写你的构建文件。Polygot 扩展程序（https://github.com/takari/polyglot-maven）使其成为可能。要尝试，请运行 `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` 并在几毫秒内转换你的构建文件。遗憾的是，没有可靠的 Maven<>Gradle 转换器 :(。是的，Maven 构建文件很大，但也很容易理解。修正或调试不费吹灰之力。

### 年龄仅仅是一个数字 - Mavens 的稳定性和演变

承认，Maven已经存在了很长时间，其美学可能不符合当前的标准。然而，Maven的持久性使其能够适应并不断发展。Maven独立于您的项目。构建文件可以轻松重用。插件在沙盒中运行，彼此独立且独立于Java或Maven版本。这种设计促进了稳定性
和可预测性，并使复杂的构建过程易于管理，而不会出现意外冲突。

### 结论

现今，开发环境对于开发者来说已经过载很多任务和技术。在寻求简单性和自动化的过程中，Gradle成为了一种现代构建工具，但也带来了自己的挑战。毫无疑问，Gradle的概念是好的!但鉴于Gradle构建脚本的复杂性和所需时间，我们是否应该考虑扩
展Maven，使其更简单。通过插件和扩展，可以随时提升和简化Maven。相较于跳跃到下一个技术，进一步开发不是更有趣，也更有价值吗?

### 链接

* [从Gradle回到Maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### 联系人

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose)。
