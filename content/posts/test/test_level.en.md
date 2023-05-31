---
title: "Test Levels: Finding the Right Balance"
date: 2023-05-31
author: "Nova Annabella"
slug: test_level
tags: [ Testing, Software Testing, Test Levels, Mock Tests, Unit Tests, Integration Tests, Component Tests, Contract Tests, End-to-End Tests ]
categories: [ Technology, Software Development, Quality Assurance ]
description: "Finding the right balance in choosing the appropriate test levels for software testing."
draft: false
images:
  - "/images/content/martin_fowler_testing.png"
card: "summary_large_image"
---

# Test Levels: Finding the Right Balance

[![test_level](/images/content/martin_fowler_testing.png)](https://martinfowler.com/articles/microservice-testing/)

### Introduction

The topic of testing still seems to be uncharted territory with a lot of room for interpretation. The traditional test
pyramid has been challenged and new test pyramids have emerged. In my opinion, it doesn't require a test pyramid, but
rather a clear understanding of what needs to be tested. The lower-level tests tend to be less meaningful. The main
focus should be on testing the behavior, ensuring that the API or UI functions as desired. A comprehensive overview of
possible test types can be found here: [Martinfowler Testing](https://martinfowler.com/articles/microservice-testing/).

### Level 1 - Mock Tests & Unit Tests

Purpose: Exercise the smallest pieces of testable software in the application to determine whether they behave as
expected.

Mock tests and unit tests can be counterproductive and often hinder the development process. These tests are often
detached from the context and lack relevance to reality. They tend to maintain unnecessary functions purely through
existing unit
tests. Once mocks are added, it becomes a self-engaging activity. The expected results of mock tests are limited to what
was defined in the initial mock. The end-users are not concerned with internal functions. For example, in a login
scenario `loginUser(name, password, securityAlgorithmus)`. If the unit test checks for a null check on
the `securityAlgorithm` parameter, then it is testing too much as users cannot set the `securityAlgorithm` parameter.

### Level 2 - Integration Test

Purpose: Verify the communication paths and interactions between components to detect interface defects.

Integration tests provide valuable insights into the performance and independence of various parts of the application.
With fewer mocks, the tests become more understandable. However, they still lack context, and there is a risk that
integration tests are simply disguised unit tests with fewer mocks.

### Level 3 - Component Test

Purpose: Limit the scope of the exercised software to a portion of the system under test, manipulating the system
through internal code interfaces and using test doubles to isolate the code under test from other components.

Component tests reveal a wealth of information about the quality and performance of the application. Instead of mocks,
you finally test your application. The boundary between component tests and end-to-end tests is not significant. With a
good testing environment, the boundaries between them often blur, allowing for testing of real behavior rather than
isolated and contextless functions. However, the creation of additional test classes like component stubs, fakes, and
mocks in the production code can introduce maintenance overhead.

### Level 4 - Contract Test

Purpose: Verify interactions at the boundary of an external service, asserting that it meets the contract expected by a
consuming service.

Contract tests are often similar to component tests, and the distinction between them is minimal. Some developers
associate these tests with Pact tests, which essentially function as unit tests with a server in between. The effort
involved in maintaining these tests might not be worthwhile. For instance, a Pact test may test the REST
API `loginUser?name=aa&password=bb)` and expect a JSON schema response that was uploaded to the Pact server beforehand.
This schema is static, making it prone to errors such as incorrect date formats or time zones in the API response. The
negative impact can be enormous

### Level 5 - End-to-End Tests aka Black Box Tests

Purpose: Verify that a system meets external requirements and achieves its goals, testing the entire system from end to
end.

End-to-end tests are reliable and robust. Once the hurdle of setting up the testing environment is overcome, the effort
pays off. These tests simulate real behavior, eliminating the need for mocks. Bugs become less frequent and easier to
reproduce locally. Extensive debugging and production logging are largely eliminated, as are rare incidents. Developers
work less frequently, if at all, with production data, reducing responsibility and increasing focus. Moreover,
automations such as automatic software updates become easier since the behavior has already been tested. There are
additional benefits as well! Once the tests are written in a reusable manner, they can be integrated into load tests,
providing a comprehensive picture of functionality. These tests can also run continuously in the production environment,
giving real-time insights into the status of various workflows. If a subsystem, such as an external REST service, goes
offline, it can be immediately identified which user workflows are affected.

### Conclusion

In conclusion, testing is an essential aspect of software development, and the choice of test levels depends on the
specific needs and goals of the application. While mock tests and unit tests can be limited in their effectiveness,
integration tests and component tests provide valuable insights into the behavior and performance of the application.
Contract tests help verify interactions with external services, but their distinction from component tests may be
minimal. Ultimately, end-to-end tests offer the highest level of confidence in the system's functionality, allowing for
comprehensive testing of the entire application. By selecting the appropriate test levels and combining them
effectively, developers can ensure the quality, reliability, and robustness of their software.

### Contact

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
