---
title: "Testing Levels: Finding the Right Balance"
date: 2023-05-31
author: "Nova Annabella"
slug: test_level
tags: [ Testing, Software Testing, Test Levels, Mock Tests, Unit Tests, Integration Tests, Component Tests, Contract Tests, End-to-End Tests ]
categories: [ Technology, Software Development, Quality Assurance ]
description: "Striking the right balance in selecting appropriate test levels for software testing"
draft: false
images:
  - "/images/content/martin_fowler_testing.png"
card: "summary_large_image"
---


# Test levels: Finding the right balance

[![testebenen](/images/content/martin_fowler_testing.png)](https://martinfowler.com/articles/microservice-testing/)

### Introduction

The subject of testing still seems to be uncharted territory with a lot of room for interpretation. The traditional test
pyramid has been questioned and new test pyramids have emerged. In my opinion there is no need for a test pyramid, but a
clear understanding of what needs to be tested. The tests at lower levels are often less meaningful. The focus should be
primarily on testing behavior to ensure that the API or UI works as intended. A comprehensive overview of possible test
types can be found here: [Martinfowler Testing](https://martinfowler.com/articles/microservice-testing/).

### Level 1 - Mock Tests & Unit Tests

Goal: Exercise the smallest testable pieces of software in the application to determine if they work as expected. work.
Mock tests and unit tests can be counterproductive and often hinder the development process. These tests are often
detached from the context and have little relation to reality. They often only serve to maintain unnecessary functions
via existing unit tests. Once mocks are added, it becomes a self-dealing exercise. The expected results of mock tests
are limited to what was defined in the original mock. The end users are not interested in internal functions. For
example, in a Login scenario `loginUser(name, password, securityAlgorithm)`. If the unit test performs a null check on
the `securityAlgorithm` parameter, too much testing is done because users cannot set the `securityAlgorithm` parameter.
set the `securityAlgorithm` parameter.

### Level 2 - Integration Test

Purpose: To check communication paths and interactions between components to detect interface defects. Integration
testing provides valuable insight into the performance and independence of different parts of the application. With
fewer mocks, the tests become more understandable. However, they still lack context, and there is a danger that risk
that integration tests are simply unit tests in disguise with fewer mocks.

### Level 3 - Compontent Test

Purpose: to limit the scope of the software under test to a portion of the system under test, manipulate the system
internal code interfaces, and use of test doubles to isolate the code under test from other components. components.
Component testing provides a wealth of information about the quality and performance of the application. Instead of
Mocks you finally test your application. The boundary between unit testing and end-to-end testing is not significant.
With a good testing environment, the lines between them often blur, so testing real-world behavior instead of isolated
and contextless functions becomes possible. However, the creation of additional test classes such as component stubs,
fakes, and mocks in production code can add maintenance overhead.

### Level 4 - Contract Test

The purpose of this code block is to verify the interactions at the boundary of an external service and to ensure that
it meets the contractual requirements of a consuming service. Contract tests often resemble unit tests, and the
difference between them is minimal. Some developers associate these tests with Pact tests, which essentially act as unit
tests with a server in between. The effort to maintain these tests, however, might not be worth it. For example, a Pact
test could use the REST API `loginUser?name=aa&password=bb)` test and expect a JSON schema response that has been
previously uploaded to the Pact server has been uploaded. This schema is static and prone to errors such as incorrect
date formats or time zones in the API response. The negative impact can be enormous.

### Level 5 - End-to-end tests (also called black box tests)

Purpose: To verify that a system meets external requirements and achieves its goals by testing the entire system from
start to finish. from start to finish. End-to-end testing is reliable and robust. Once the hurdles of setting up the
test environment have been overcome, the effort pays off. These tests simulate real-world behavior and eliminate the
need for mocks. Errors occur less frequently and are easier to reproduce locally. Time-consuming debugging and keeping
logs in production are largely are largely avoided, as are rare incidents. Developers work less frequently, if at all,
with production data, which reduces responsibility and increases focus. In addition, automations such as automatic
software updates make execution easier because the behavior has already been tested. There are other benefits! Once the
tests are written in a reusable form, they can be integrated into load tests to get a comprehensive comprehensive
picture of functionality. These tests can also be run continuously in the production environment and provide real-time
insights into the status of various workflows. When a subsystem, such as such as an external REST service, goes offline,
it can be immediately identified which user workflows are are affected.

### Fazit

In summary, testing is an essential aspect of software development, and the choice of testing levels depends on the
specific requirements and goals of the application. While mock tests and unit tests can be limited in their
effectiveness, integration tests and effectiveness, integration testing and unit testing provide valuable insight into
the behavior and performance of the application. performance of the application. Contract tests help verify interactions
with external services, but your Differentiation from unit tests can be minimal. Ultimately, end-to-end testing provides
the highest level of confidence in the the functionality of the system and enable comprehensive testing of the entire
application. By selecting the appropriate test levels and combining them effectively, developers can ensure the quality,
reliability and robustness of your software.

### Contact

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
