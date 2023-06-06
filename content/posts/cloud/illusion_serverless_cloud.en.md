---
title: "Illusion Serverless & Cloud"
date: 2023-05-24
author: "Nova Annabella"
slug: illusion_serverless_cloud
tags: [ Development, Serverless, Cloud, Microservices, Scalability, Architecture, Infrastructure ]
categories: [ Technology, Software, Cloud ]
description: "Challenges and Realities of Serverless Functions in the Cloud. Valuable Insights for Enterprises Considering Migration to the Cloud."
draft: false
images:
  - "/images/content/onprem_vs_cloud.png"
card: "summary_large_image"
---



# The illusion of serverless functions in the cloud

![aws_costs_twitter_1](/images/content/onprem_vs_cloud.png)

### Introduction

I am disappointed how often marketing wins out over common sense. Many managers put themselves over their own experts -
the developers. This is also true when it comes to migrating to the cloud. Spoiler: If you need to save money need to
save money should avoid the cloud. Because the new buzzword "serverless" in the cloud means: You take care of the You
take care of the software, we'll take care of the hardware. However, if you have a capable, motivated and curious
administrator, you can can also run Serverless themselves (e.g. [KNative](https://knative.dev)).
![aws_costs_twitter_1](/images/content/aws_costs_twitter_1.png)

### Serverless Functions vs Microservices:



#### Microservices

A typical stateless microservice takes care of a specific function/domain and is deployed in a Container Orchestration
environment. This environment takes care of infrastructure, security, firewall, Logging, Metrics, Secrets, Networking,
Backups and much more. A major advantage is that a microservice can be deployed locally with few resources and is
cloud/server agnostic (deployable anywhere).

#### Serverless functions

A little joke beforehand: Paradoxical, but true - serverless features depend heavily on the server environment. :) A
typical serverless function also takes care of only one specific function/domain and is written without frameworks in
pure code to be faster than a microservice (Also a good exercise for MicroServices). A big Advantage is that Serverless
functions scale automatically. However, each serverless function requires a considerable amount of GlueCode to define
the infrastructure - security, firewall, network, logging, metrics, Secrets, caching, backups, and more. Therefore, a
simple function such as copying a file including API can quickly involve 1500 lines of code (including IaC). include.
Administration costs shift from administration to development at a ratio of 1:N (1 to serverless functions). The
knowledge and the implementation are thus no longer bundled and can quickly become unstable. In addition, there are
increased maintenance costs. Also, true integrative testing is rare with Serverless or requires a great deal of effort.
Ultimately, the complexity of serverless functions is significantly higher than that of a single microservice. Higher
complexity also means lower maintainability. New team members have a harder time and require significantly more prior
knowledge.

### Serverless and the cloud in general

Most cloud technologies are not up to date. For example, Node.js, Java, Python and other languages or technologies are
languages or technologies are often not easy to update, usually only waiting helps. Even modern and standard
technologies like MongoDB, MySQL, Kafka, NATS, RabbitMQ, Redis, Prometheus, InfluxDB, Grafana, Kibana, Elastic Search,
etc. are either not available or overpriced. Without such standard services, you are often in the virtual stone age and
using outdated solutions, e.g. Webhooks for external communication. In addition, the room for maneuver on topics such as
regulation, compliance, data protection and failover are severely limited. The cloud should therefore be run
agnostically so that it can quickly switch between AWS, Azure, Google, on-premise, etc. and be able to compare costs.
Limitations are also common in the cloud, leading to creative workarounds that in turn increase complexity increase.
Integrative testing can also be expensive, as each developer needs their own development environment in the cloud as
many cloud services have little or no local testability. But even without testing, the cloud is expensive. Whereas with
on-premise systems it is mainly hardware costs, in the cloud you also have to pay for traffic, some standard services
and often even for the and often even for multiple taxation. In addition, it is easy to lose track of things in the
cloud, because it is not about It's not about user-friendliness, but about money. The costs are so hidden that you only
notice them when it is too late. is too late. The fundamentals of architecture and infrastructure have to be reinvented
in the cloud and especially in serverless have to be reinvented, as the implementation depends heavily on the features
available. Whenever I design the architecture, I think, "This could have been a single service. could have been". To
me, serverless is an interesting idea and it scales well, but it doesn't lower the cost. On the On the contrary, it
requires much more knowledge and time in development. Serverless or the cloud require discipline and prior knowledge. If
the knowledge is not there for on-premise systems, it will not be easier with the cloud. How should developers acquire
additional infrastructure knowledge? I would prefer a well-managed Kubernetes cluster over cloud architecture. The
staff doesn't scale. Many developers have no discipline in writing code. Unfortunately, that's true for 80 percent of
developers. So how are these developers going to be able to operate the cloud? the cloud? It is important that
enterprises fully understand the challenges and implications of serverless architecture and the cloud. comprehensively.
This requires not only technical knowledge, but also a strategic approach. A ill-considered migration to the cloud can
lead to complexity, higher costs and overtaxing of developers. In summary, serverless in the cloud is a promising
concept, but one that should be considered carefully. should be considered carefully. Cost, complexity, maintainability
and the capabilities of the development team need to be be taken into account. Every company has different requirements
and priorities. An informed decision should be made as to whether Serverless in the cloud is the right solution or
whether alternative approaches such as e.g. well Kubernetes cluster are the better choice. Successful deployment of
serverless and cloud computing requires a combination of technical expertise strategic planning and a clear
understanding of business requirements. Only then can the illusion of serverless be and make the right decision for your
own software development.

### Fazit

The introduction of serverless capabilities in the cloud promises flexibility, scalability, and relief for developers
from infrastructure tasks. However, one should not be blinded by this illusion. The move to the cloud and the use of
serverless functions brings with it a number of challenges. Developers have to learn a new "language" in addition to
the actual development and take on more responsibility without the appropriate support. take on more responsibility. The
complexity of serverless functions is often higher than that of microservices, as developers have to take on many
additional tasks, such as infrastructure definition, security, and maintenance. such as infrastructure definition,
security, and scaling. True integrative testing is difficult, and prior knowledge and experience for operations are even
more important in the cloud. The cloud itself brings additional challenges. Many cloud technologies are not up to date
and using modern off-the-shelf services can be expensive or even impossible. Regulatory requirements, compliance and
data protection limit the scope. In addition, costs in the cloud easily get out of hand, and the overview of
expenditures is quickly lost. All in all, the advantages and disadvantages of serverless and cloud must be carefully
weighed up. Companies should consider their specific requirements, the expertise available within the team, and the
long-term implications of migrating to the cloud. of migrating to the cloud. Making an informed decision based on a
comprehensive analysis is critical to the success and profitability of the project. Ultimately, it is up to enterprises
to adequately support their developers, realistically assess the cost and complexity of the Cloud realistically and
consider alternative solutions such as well-managed Kubernetes clusters. With a clear strategy and a sound understanding
of their needs, enterprises can take full advantage of the Cloud and Serverless capabilities to the fullest and see
through the illusion.

### Contact

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
