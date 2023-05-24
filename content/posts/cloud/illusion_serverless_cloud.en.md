---
title: "Illusion Serverless & Cloud"
date: 2023-05-23
author: "Nova Annabella"
slug: illusion_serverless_cloud
tags: [ Development, Serverless, Cloud, Microservices, Scalability, Architecture, Infrastructure ]
categories: [ Technology, Software, Cloud ]
description: "Challenges and realities of serverless capabilities in the cloud. Valuable insights for companies considering a migration to the cloud"
draft: false
images:
  - "/images/content/onprem_vs_cloud.png"
card: "summary_large_image"
---

# The illusion of serverless functions in the cloud

![aws_costs_twitter_1](/images/content/onprem_vs_cloud.png)

### Introduction

I am disappointed how often marketing wins out over common sense. Many managers put themselves
over their own experts - the developers. This is also true when it comes to migrating to the cloud. Spoiler: If you need
to save money
need to save money should avoid the cloud. Because the new buzzword "serverless" in the cloud means: You take care of
the software, we take care of the hardware.
You take care of the software, we'll take care of the hardware. However, if you have a capable, motivated and
inquisitive administrator, you can
can also run Serverless themselves (e.g. [KNative](https://knative.dev)).

![aws_costs_twitter_1](/images/content/aws_costs_twitter_1.png)

### Serverless functions vs microservices:

#### microservices

A typical stateless microservice takes care of a specific function/domain and is deployed in a
container orchestration environment. This environment takes care of infrastructure, security, firewall,
logging, metrics, secrets, networking, backups and more. A big advantage is that a microservice can be deployed locally
with
few
resources and is cloud/server agnostic (can be deployed anywhere).

#### Serverless functions

A little joke beforehand: Paradoxical but true - serverless functions depend heavily on the server environment. :)
A typical serverless function also takes care of only one specific function/domain and is written without frameworks in
code to be faster than a microservice (also a good exercise for MicroServices). A big
advantage is that Serverless functions scale automatically. However, each serverless function requires a
considerable amount of GlueCode to define the infrastructure - security, firewall, network, logging, metrics,
secrets, caching, backups and much more.
Therefore, a simple function such as copying a file including API can quickly involve 1500 lines of code (incl. IaC).
can be involved.
The administration costs shift from administration to development in a ratio of 1:N (1 to Serverless
functions). The knowledge and implementation are therefore no longer
bundled and can quickly become unstable. In addition, there are increased maintenance costs.
True integrative testing is also rare with serverless, or only possible with great effort.
Ultimately, the complexity of serverless functions is significantly higher than that of a single microservice.
Higher complexity also means lower maintainability. New team members have a harder time and need significantly
more prior knowledge.

### Serverless and the cloud in general

Most cloud technologies are not up to date. For example, Node.js, Java, Python, and other
languages or technologies are often not easy to update, usually only waiting helps.
Even modern and standard technologies such as MongoDB, MySQL, Kafka, NATS, RabbitMQ, Redis, Prometheus, InfluxDB,
Grafana,
Kibana, Elastic Search etc. are either not available or overpriced.
Without such standard services, one is often in the virtual stone age and uses outdated solutions, e.g.
webhooks for external communication. In addition, the room for manoeuvre on issues such as regulation,
compliance, data protection and fail-safety is severely limited.

The cloud should therefore be run agnostically in order to be able to switch quickly between AWS, Azure, Google,
on-premise, etc. and to
compare costs.
Limits are also often present in the cloud, leading to creative workarounds, which in turn increase complexity.
increase. Integrative testing can also become expensive, as each developer needs their own development environment in
the cloud
as many cloud services are hardly or not at all testable locally.
But even without testing, the cloud is expensive. Whereas with on-premise systems it is mainly
hardware costs, in the cloud you also have to pay for traffic, some standard services and often even for multiple
and often even for multiple taxation. Moreover, it is easy to lose track of things in the cloud, because it is not about
it's not about user-friendliness, but about money. The costs are so hidden that you only notice them when it is too
late.
too late.

The basics of architecture and infrastructure have to be reinvented in the cloud and especially in the area of
serverless
have to be reinvented, as the implementation depends heavily on the available functions.
Whenever I have designed the architecture, I think: "This could have been a single service".
could have been".

For me, serverless is an interesting idea and it scales well, but it doesn't reduce costs. On the
On the contrary, it requires much more knowledge and time in development. Serverless or the cloud require discipline and
prior knowledge.
If the knowledge is not there for on-premise systems, it will not be easier with the cloud.
How should developers acquire additional infrastructure knowledge?

I would prefer a well-managed Kubernetes cluster to cloud architecture.
The people don't scale. Many developers have no discipline in writing code.
Unfortunately, this is true for 80 percent of developers. So how are these developers going to be able to use the cloud?
the cloud?

It is important that organisations fully understand the challenges and implications of serverless architecture and the
cloud.
fully understand the challenges and implications of serverless architecture and the cloud. This requires not only
technical knowledge, but also a strategic approach. A
ill-considered migration to the cloud can lead to complexity, higher costs and overburdening of developers.

In summary, serverless in the cloud is a promising concept, but one that should be considered carefully.
should be considered carefully. Cost, complexity, maintainability and the skills of the development team need to be
considered.
be taken into account.
Every company has different requirements and priorities. An informed decision should be made whether
Serverless in the cloud is the right solution or whether alternative approaches like
e.g. well Kubernetes cluster are the better choice.

Successful deployment of serverless and cloud computing requires a combination of technical expertise
strategic planning and a clear understanding of business requirements. Only then can the illusion of serverless be
and make the right decision for your own software development.

### Conclusion

The introduction of serverless functions in the cloud promises flexibility, scalability and relief of
developers from infrastructure tasks. However, one should not be blinded by this illusion. The
move to the cloud and the use of serverless functions brings with it a number of challenges.

Developers have to learn a new "language" in addition to the actual development and take on more responsibility without
the appropriate support.
take on more responsibility.
The complexity of serverless functions is often higher than that of microservices, as developers have to take on many
additional tasks, such as
developers have to take on many additional tasks such as infrastructure definition, security and scaling. True
integrative testing is
difficult and prior knowledge and experience for operations are even more important in the cloud.

The cloud itself brings further challenges. Many cloud technologies are not up-to-date
and the use of modern off-the-shelf services can be expensive or even impossible. Regulatory requirements, compliance
and
data protection limit the scope. In addition, costs in the cloud easily get out of hand,
and the overview of expenses is quickly lost.

Overall, the advantages and disadvantages of serverless and cloud need to be carefully weighed.
Companies should consider their specific requirements, the existing expertise in the team and the long-term effects of a
migration to the cloud.
of a migration to the cloud.
An informed decision based on a comprehensive analysis is crucial for the success and profitability of the project.
of the project.

Ultimately, it is up to companies to adequately support their developers, realistically assess the costs and complexity
of the
cloud realistically and consider alternative solutions such as well-managed Kubernetes clusters.
With a clear strategy and a sound understanding of their own needs, companies can make the most of the benefits of the
Cloud and serverless capabilities to their fullest potential and see through the illusion.

### Contact

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
