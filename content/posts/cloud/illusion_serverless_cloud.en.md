---
title: "Illusion Serverless & Cloud"
date: 2023-05-24
author: "Nova Annabella"
slug: illusion_serverless_cloud
tags: [ Development, Serverless, Cloud, Microservices, Scalability, Architecture, Infrastructure ]
categories: [ Technology, Software, Cloud ]
description: "Challenges and realities of serverless functions in the cloud. Valuable insights for companies considering a migration to the cloud."
draft: false
images:
  - "/images/content/onprem_vs_cloud.png"
card: "summary_large_image"
---


# The Illusion of Serverless Functions in the Cloud

![aws_costs_twitter_1](/images/content/onprem_vs_cloud.png)

### Introduction

I'm disappointed with how often marketing triumphs over common sense. Many managers overrule their own experts - the developers. This also applies to the migration to the cloud. Spoiler: those who need to save money should avoid the cloud. For the new buzzword "Serverless" in the cloud means: You take care of the software, we take care of the hardware. However, if you have a capable, motivated and curious administrator, you can run Serverless yourself (e.g., [KNative](https://knative.dev)).

![aws_costs_twitter_1](/images/content/aws_costs_twitter_1.png)

### Serverless Functions vs Microservices:



#### Microservices

A typical stateless microservice takes care of a specific function/domain and is deployed in a 
container orchestration environment. This environment takes care of infrastructure, security, firewall,
logging, metrics, secrets, network, backups and much more. A big advantage is that a microservice can be tested locally with
few
resources and is cloud/server-agnostic (usable everywhere).

#### Serverless Functions

A little joke to start: Paradoxically, but true - Serverless functions depend heavily on the server environment. :)
A typical serverless function also takes care of only one particular function/domain and is written without frameworks
in
pure code to be faster than a microservice (also a good exercise for MicroServices). A big
advantage is that serverless functions are automatically scaled. However, each serverless function requires a
considerable amount of glue code to define the infrastructure - security, firewall, network, logging, metrics,
secrets, caching, backups and much more.
Therefore, a simple function like copying a file including API can quickly include 1500 lines of code (incl. IaC).
The administration costs shift from administration to development in a 1:N ratio (1 to serverless
functions). The knowledge and the implementation are thus no longer
bundled and can quickly become unstable. This also comes with increased maintenance costs.
Real integrative tests are also rare with serverless or only associated with a lot of effort.
Ultimately, the complexity of serverless functions is significantly higher than that of a single microservice.
Higher complexity also means less maintainability. New team members have a harder time and require significantly
more prior knowledge.

### Serverless and the Cloud in General

Most cloud technologies are not up to date. For example, Node.js, Java, Python and other languages or technologies are often not easy to update, usually, the only option is to wait.
Even modern and standard technologies like MongoDB, MySQL, Kafka, NATS, RabbitMQ, Redis, Prometheus, InfluxDB, Grafana, Kibana, Elastic Search etc. are either not available or overpriced.
Without such standard services, you often find yourself in the virtual Stone Age, using outdated solutions, e.g. webhooks for external communication. In addition, the scope of action on issues such as regulation, compliance, data protection and fail-safety is severely limited.

Therefore, the cloud should be operated agnostically in order to switch quickly between AWS, Azure, Google, On-Premise etc. and compare costs. 
Limitations are often present in the cloud, resulting in creative workarounds that increase complexity. Integrative testing can also become expensive, as each developer needs their own development environment in the cloud, as many cloud services can hardly or not at all be tested locally.
Even without tests, the cloud is expensive. While on-premise systems predominantly incur hardware costs, additional charges in the cloud are for traffic, some standard services and often even for multiple taxation. Moreover, you can easily lose track in the cloud, because it's not about user-friendliness, but about money. The costs are so hidden that you only notice them when it's too late.

The basics of architecture and infrastructure must be reinvented in the cloud, especially in the area of serverless, as the implementation strongly depends on the available features. 
Every time I design the architecture, the thought comes to me: "This could have been a single service as well".

To me, serverless is an interesting idea and it scales well, but it doesn't reduce costs. On the contrary, it requires more knowledge and time in development. Serverless or the cloud requires discipline and prior knowledge. 
If the knowledge for on-premise systems is not available, it won't get easier with the cloud. 
How are developers supposed to acquire additional infrastructure knowledge?

I would prefer a well-managed Kubernetes cluster to cloud architecture.
The staff doesn't scale. Many developers don't have discipline in writing code. 
Unfortunately, this applies to 80 percent of developers. So how are these developers supposed to operate the cloud?

It's crucial that companies fully understand the challenges and impacts of serverless architecture and the cloud. This requires not just technical knowledge, but also a strategic approach. An unconsidered migration to the cloud can lead to complexity, higher costs and developers being overwhelmed.

To sum up, serverless in the cloud is a promising concept that should be carefully considered. Costs, complexity, maintainability, and the capabilities of the development team must be considered. 
Each company has different requirements and priorities. You should make an informed decision as to whether serverless in the cloud is the right solution, or if alternative approaches like a good Kubernetes cluster are a better choice.

Successful adoption of serverless and cloud computing requires a combination of technical expertise, strategic planning, and a clear understanding of business requirements. Only then can the illusion of serverless be understood and the right decision for your own software development be made.

### Conclusion

The introduction of serverless functions in the cloud promises flexibility, scalability, and relief from
Developers of infrastructure tasks. However, one should not be blinded by this illusion. The
Switching to the cloud and using serverless functions brings a number of challenges.

Developers must learn a new "language" in addition to actual development and without appropriate support
take on more responsibility.
The complexity of serverless functions is often higher than that of microservices, as developers have many additional
Tasks such as infrastructure definition, security, and scaling must be taken over. Real integrative tests are
difficult and previous knowledge and experience for operation are even more important in the cloud.

The cloud itself brings further challenges. Many cloud technologies are not up to date
and the use of modern standard services can be expensive or even impossible. Regulatory requirements, compliance, and
Data protection limit the scope. In addition, the costs in the cloud can easily get out of hand,
and the overview of the expenses is quickly lost.

Overall, it is important to carefully weigh the pros and cons of serverless and cloud.
Companies should consider their specific requirements, the existing know-how in the team, and the long-term effects
of a migration to the cloud.
A well-founded decision based on a comprehensive analysis is crucial for the success and profitability
of the project.

In the end, it is up to companies to adequately support their developers, realistically assess the costs and complexity of the
cloud and consider alternative solutions such as well-managed Kubernetes clusters.
With a clear strategy and a solid understanding of their own needs, companies can take full advantage of the
Cloud and serverless functions optimally and see through the illusion.

### Contact

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
