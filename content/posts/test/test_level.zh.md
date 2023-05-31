---
title: "测试层次：寻找平衡点"
date: 2023-05-31
author: "Nova Annabella"
slug: test_level
tags: [ Testing, Software Testing, Test Levels, Mock Tests, Unit Tests, Integration Tests, Component Tests, Contract Tests, End-to-End Tests ]
categories: [ Technology, Software Development, Quality Assurance ]
description: "在软件测试中寻找适当的测试层次的平衡点。"
draft: false
images:
  - "/images/content/martin_fowler_testing.png"
card: "summary_large_image"
---

# 测试层次：寻找平衡点

![test_level](/images/content/martin_fowler_testing.png)

### Introduction

测试仍然是一个未被探索的领域，有很多解释的空间。传统的测试金字塔已经受到挑战，出现了新的测试金字塔。在我看来，不需要一个测试金字塔，而是需要清楚地理解需要测试什么。较低级别的测试往往意义不大。重点应该放在测试行为上，确保
API 或 UI
的功能符合预期。可以在这里找到关于可能的测试类型的综合概述：[Martinfowler Testing](https://martinfowler.com/articles/microservice-testing/)。

### Level 1 - Mock 测试和单元测试

目的：测试应用程序中最小的可测试软件单元，以确定它们是否按预期运行。

Mock 测试和单元测试往往具有反效果，经常阻碍开发过程。这些测试通常与上下文脱节，与现实缺乏关联。它们往往通过现有的单元测试来保持不必要的函数。一旦添加了
Mock，它就变成了一种自我交互的活动。Mock 测试的预期结果仅限于最初定义的
Mock。最终用户并不关心内部函数。例如，在登录场景中 `loginUser(name, password, securityAlgorithmus)`
，如果单元测试检查 `securityAlgorithm` 参数的 null 值检查，那么测试的范围就过大了，因为用户无法设置 `securityAlgorithm` 参数。

### Level 2 - 集成测试

目的：验证组件之间的通信路径和交互，以检测接口缺陷。

集成测试为应用程序的各个部分的性能和独立性提供了宝贵的洞察。较少的 Mock 使得测试更加易懂。然而，集成测试仍然缺乏上下文，并且存在着风险，即集成测试只是带有较少
Mock 的伪装的单元测试。

### Level 3 - Component Test

**目的：** 限定对被测试系统的一部分进行测试，通过内部代码接口进行系统操作，并使用测试替身来隔离被测试代码与其他组件的影响。

组件测试揭示了应用程序质量和性能方面的丰富信息。在这里，你终于可以对应用程序进行真正的测试，而不是仅仅使用模拟对象。组件测试与端到端测试之间的界限并不明显。在良好的测试环境下，它们之间的界限通常模糊，可以测试真实的行为，而不仅仅是孤立和无上下文的功能。然而，在生产代码中创建额外的测试类，如组件桩、虚拟对象和模拟对象，可能会增加维护成本。

### Level 4 - Contract Test

**目的：** 验证与外部服务边界的交互，确保其符合消费服务预期的合约。

合约测试与组件测试常常相似，它们之间的区别很小。一些开发人员将这些测试与 Pact 测试联系起来，实质上 Pact
测试就像带有服务器的单元测试。维护这些测试所需的工作可能不值得。例如，Pact 测试可能会测试 REST
API `loginUser?name=aa&password=bb)`，并期望预先上传到 Pact 服务器的 JSON Schema 响应。这个 Schema 是静态的，可能会存在错误，如
API 响应中的日期格式不正确或时区错误。这样的错误可能会产生巨大的负面影响。

### 第五级 - 全面测试，也称为黑盒测试

目的：验证系统是否满足外部需求并实现其目标，对整个系统进行端到端的测试。

全面测试可靠且强大。一旦克服了设置测试环境的难题，付出的努力就会得到回报。这些测试模拟真实行为，无需使用模拟对象。错误出现的频率更低，本地复现更容易。大部分繁琐的调试和生产日志记录都被消除，罕见的问题也会减少。开发人员很少甚至根本不使用生产数据，减少责任，提高专注力。此外，由于行为已经经过测试，自动软件更新等自动化操作也更容易实现。还有其他的好处！一旦以可重复使用的方式编写了这些测试，它们可以整合到负载测试中，提供功能的全面图片。这些测试还可以在生产环境中持续运行，实时了解各个工作流程的状态。如果外部REST服务等子系统离线，可以立即确定哪些用户工作流程受到影响。

### 结论

总而言之，测试是软件开发中必不可少的一部分，测试级别的选择取决于应用程序的具体需求和目标。虽然模拟测试和单元测试的有效性有限，集成测试和组件测试可以提供有价值的洞察力，了解应用程序的行为和性能。合约测试有助于验证与外部服务的交互，但它们与组件测试之间的区别可能很小。最终，全面测试提供了对系统功能最高程度的信心，允许对整个应用程序进行全面的测试。通过选择适当的测试级别并有效地结合它们，开发人员可以确保软件的质量、可靠性和稳健性。

### 联系方式

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
