---
title: "回到玛文？"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "难以捉摸的对简单的追求和重新发现Maven力量的短暂旅程。"
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---



# 回到Maven？

[！[maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

## 10年的Gradle。为了寻求解脱，重新发现Maven的力量的短暂旅程。



###最大限度地发挥开发者的潜力--我们需要更多的省时工具

那些经常被忽视或很少被讨论的话题让我感兴趣。经常有一些很酷的技术在使用、 但几乎没有人谈及与之相关的问题。 现在的开发成本已经很高了。 随着 "无服务器"、"低代码"、"IaC"、"大数据"、"云"、"DevOps"、"你建立它你运行它
"等很酷的流行语，开发者已经受够了。 等等，开发人员已经有足够多的额外任务要处理。更多的任务意味着，几乎没有任何 专家，而且有些事情总是被忽略的重点。这就是为什么自动化和节省时间是巨大的 重要。"不要让我思考 "和 "开箱即用
"已经是高质量的功能了，我在Gradle中还没有看到。 还看不到。公平地说，Gradle并不是唯一让我们的工作变得更容易的现代工具，而不是让它 让它变得更容易。

###对简单性和自动化的虚幻追求

从SOAP开始，我就对基于XML的配置有一种根深蒂固的厌恶。有了Gradle，我曾希望 编写绑定脚本会变得轻而易举。不幸的是，我的希望和动力每次都在减少 每次都会减少。Gradle追求的是灵活性，并为此牺牲了自动化和质量。开发人员盲目地跟随
开发人员盲目地跟风，而不考虑对软件可靠性的影响。为了使Gradle 构建脚本简单化和低维护性，需要强大的纪律性。这种纪律性在 源代码中已经很少了，因此在构建脚本中就更少了。

### 翻译和变通方法 - 当构建脚本成为一种挑战时

Gradle在后台的工作与Maven没有太大区别。因此，一些翻译是必要的。一些功能，如 依赖目录、Maven发布插件、Dependabot等功能实际上是对Maven已有的基本功能的变通。
的基本功能。Gradle的灵活性往往伴随着复杂的构建配置、 难以维护。 Gradle插件往往有兼容性问题，有局限性或进步有限。这些问题的出现 由于Gradle生态系统的不断发展，Gradle所处环境的多样性
使用环境的多样性，以及每个插件所需的具体实施和维护工作。一切都是相互关联的。

### Gradle多米诺骨牌效应--现实世界中的噩梦般的情景

我见过很多只有几年历史的微服务，由于Gradle的存在，已经无法维护了。 由于Gradle的原因。值得一提的是，这并不是我第一次看到这样的事情，而且，他们不是 初级开发人员。 我的**任务是进行Spring Boot
2.x到2.7的升级**。Spoiler：一年后我放弃了 我放弃了!问题简述： * Gradle构建文件要求 -> 将我的本地Java版本降级到11 (WTF) (通常情况下，Java是向下兼容的。  向下兼容--
同样，也有像SdkMan这样的变通工具...) * Spring Boot的更新需要 -> Gradle更新（WTF）。 *Gradle更新需要 -> 插件更新 * 插件更新需要 -> Groovy更新 (WTF) *
Groovy的更新需要 -> 测试框架和测试的更新 (WTF) * 测试框架的更新需要 -> 依赖关系的更新。 * \[...]
此外，有些插件不能与较新的Gradle版本一起使用，有些已经不再开发，有些与其他Gradle版本不兼容，有些已经不再开发，有些与其他Gradle版本不兼容。  与其他插件不兼容，只适用于Gradle KTS，不适用Gradle
Groovy，或者只是有  只是有限制。即使是Spring等大厂商的插件，与他们的Maven插件相比，功能也很有限。  功能有限。我最终得到了一个很酷很短的Gradle构建文件，但没有人能够真正维护它、
即使是编写文件的开发者也不能，而他们仍然喜欢Gradle。我知道很少有人能  认真写Gradle脚本的人。

###重新发现Maven的力量--驾驭Maven的魅力

以下是我最喜欢的Maven的特点： 插件可以直接从命令行启动和配置，无需事先定义。 需要定义。另外，它们基本上不受其他插件配置的影响。 | 例子 命令 | 说明 | 链接 | |------------------------------
---------|--------------------------------------------------------------------------------------------------------------
-------------------------------------------------------|----------------------------------------------------------------
----------| | `mvn versions:use -latest-versions` | 更新版本 - 谁需要Dependabot？是的，我的项目多年来一直更新到最新版本，没有任何问题，也没有恼人的合并请求 |
https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html | | `mvn versions:set -DnewVersion=1.0.0` |
设置项目版本...
| https://www.mojohaus.org/versions/versions-maven-plugin/index.html | | `mvn license:add-third-party` |
列出依赖关系并显示其许可证(即使排除了许可证也可能失败) | https://www.mojohaus.org/license-maven-plugin/index.html |
这个列表可以永远继续下去。这有点让我想起了GitHub的工作流程步骤。 !
[maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)

###你不喜欢XML？

没问题!只要用`ruby`、`groovy`、`scala`、`yaml`、`atom`或`Java`编写你的构建文件。Polygot 扩展（https://github.com/takari/polyglot-
maven）使之成为可能。要尝试它 只需运行`mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml
-Doutput=pom.yaml`，在几毫秒内，你的构建文件就会变成 几毫秒后，你的构建文件就被翻译了。很遗憾，没有可靠的Maven <> Gradle翻译器。 :(
是的，Maven构建文件很大，但也很容易理解。完善或调试工作很快就能完成。 完成了。

###年龄只是一个数字--Maven的稳定性和进化性

诚然，Maven已经存在了相当长的时间，其审美可能不符合当今的标准。 然而，Maven的长寿使其得以适应和发展。Maven独立工作 独立于你的项目。构建文件可以很容易地被重复使用。
插件在沙盒中运行，相互独立，与Java或Maven版本无关。 这种设计提高了稳定性和可预测性，便于管理复杂的构建过程，避免意外的冲突。 冲突。

###法兹特

如今，开发环境中的许多任务和技术对开发者来说都是超负荷的。在寻找 追求简单和自动化，Gradle作为一个现代的构建工具出现了，但也带来了它自己的 挑战。毫无疑问，Gradle的概念是好的!但鉴于其复杂性和
时间，那么问题来了，扩展Maven是否更简单呢？ 扩展。有了插件和扩展，Maven总是可以被刷新和简化。难道不是吗？ 进一步发展不是比从一种技术跳到另一种技术更令人兴奋，也更具有可持续性吗？

###链接

* [从Gradle搬回maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

###联系

[GitHub问题](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose)。
