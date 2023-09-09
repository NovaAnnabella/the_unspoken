---
title: "Test Levels: Finding the Right Balance"
date: 2023-05-31
author: "Nova Annabella"
slug: test_level
tags: [ Testing, Software Testing, Test Levels, Mock Tests, Unit Tests, Integration Tests, Component Tests, Contract Tests, End-to-End Tests ]
categories: [ Technology, Software Development, Quality Assurance ]
description: "Finding the right balance when choosing the appropriate test levels for software testing"
draft: false
images:
  - "/images/content/martin_fowler_testing.png"
card: "summary_large_image"
---


# Test Levels: Finding the Right Balance

The given markdown text is already in English, hence, there's no need for any translation:
[![testebenen](/images/content/martin_fowler_testing.png)](https://martinfowler.com/articles/microservice-testing/)

### Introduction

The topic of testing still seems to be uncharted territory with a lot of room for interpretation to this day. The traditional test pyramid has been questioned and new test pyramids have emerged. In my opinion, there is no need for a test pyramid, but a clear understanding of what needs to be tested. Tests at lower levels are often less meaningful. The focus should primarily be on testing behavior to ensure that the 
API
or UI works as desired. A comprehensive overview of possible types of tests can be found here:
[Martinfowler Testing](https://martinfowler.com/articles/microservice-testing/).


### Level 1 - Mock Tests & Unit Tests

Goal: To exercise the smallest testable parts of the software in the application to determine if they work as expected.

Mock tests and unit tests can be counterproductive and often hinder the development process. These tests are often
disconnected from the context and have little relation to reality. They often only serve to maintain unnecessary functions over existing
unit tests. As soon as mocks are added, it becomes a self-occupation. The expected
results of mock tests are limited to what was defined in the original mock. The end users
are not interested in internal functions. For example, in a
login scenario `loginUser(name, password, securityAlgorithmus)`. If the unit test does a null check on
the `securityAlgorithm` parameter, too much is being tested, as users cannot
set the `securityAlgorithm` parameter.


### Level 2 - Integration Test

Purpose: Check the communication paths and interactions between components for the detection of interface defects.
Integration tests provide valuable insights into the performance and independence of various parts of the application.
With fewer mocks, the tests become more understandable. However, they still lack context, and there is a risk that
integration tests are just disguised unit tests with fewer mocks.

### Level 3 - Component Test

Purpose: Limiting the scope of the software tested to a part of the system to be tested, manipulation of the system
via internal code interfaces and use of test doubles to isolate the code to be tested from other
components.

Component tests provide a wealth of information about the quality and performance of the application. Instead of
mocks you finally test your application. The border between component testing and end-to-end testing is not
significant. With a good test environment, the borders often blur between them, so that testing the real
behavior instead of isolated and contextless functions becomes possible. However, the creation of additional
test classes like component stubs, fakes and mocks in the production code can bring additional maintenance effort.


### Level 4 - Contract Test

The purpose of this code block is to check the interactions at the border of an external service and ensure that it
meets the contract requirements of a consuming service. Contract tests often resemble component tests, and the
difference between them is minimal. Some developers associate these tests with Pact tests, which essentially act as unit
tests with a server in between. However, the effort to maintain these tests may not be worthwhile. For example, a Pact
test could test the REST API `loginUser?name=aa&password=bb)` and expect a JSON schema response that has been previously
uploaded to the Pact server. This schema is static and susceptible to errors such as incorrect date formats or time
zones in the API response. The negative effects can be enormous.

### Level 5 - End-to-End Tests (also called Black-Box Tests)

Purpose: Checking whether a system fulfills external requirements and achieves its objectives by testing the entire system from beginning to end.

End-to-end tests are reliable and robust. Once the hurdles of test environment setup are over, the effort pays off. These tests simulate real behavior and eliminate the need for mocks. Mistakes occur less often and can be reproduced locally more easily. Extensive debugging and logging in production are largely avoided, as are rare incidents. Developers work less often, if at all, with production data, which reduces responsibility and increases focus. In addition, automation such as automatic software updates makes performance easier as the behavior has already been tested. There are more benefits! Once the tests are written in a reusable form, they can be integrated into load tests to get a comprehensive picture of functionality. These tests can also be run continuously in the production environment and provide real-time insights into the status of various workflows. If a subsystem, such as an external REST service, goes offline, it can immediately be identified which user workflows are affected.


### Conclusion

In summary, testing is a crucial aspect of software development, and the choice of test levels depends on the specific requirements and goals of the application. While mock tests and unit tests may be limited in their effectiveness, integration tests and component tests provide valuable insights into the behavior and performance of the application. Contract tests help to verify interactions with external services, but your demarcation to component tests may be minimal. Ultimately, end-to-end tests provide the highest level of trust in the functionality of the system and allow comprehensive testing of the entire application. By selecting the appropriate test levels and their effective combination, developers can ensure the quality, reliability and robustness of your software.

### Contact

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
