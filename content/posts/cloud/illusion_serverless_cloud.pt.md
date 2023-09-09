---
title: "Ilusão Serverless & Cloud"
date: 2023-05-24
author: "Nova Annabella"
slug: illusion_serverless_cloud
tags: [ Development, Serverless, Cloud, Microservices, Scalability, Architecture, Infrastructure ]
categories: [ Technology, Software, Cloud ]
description: "Desafios e realidades das funções sem servidor na nuvem. Percepções valiosas para empresas que estão considerando uma migração para a nuvem"
draft: false
images:
  - "/images/content/onprem_vs_cloud.png"
card: "summary_large_image"
---


# A Ilusão das Funções Serverless na Cloud

![aws_costs_twitter_1](/images/content/onprem_vs_cloud.png)

### Introdução

Estou desapontado com a frequência com que o marketing vence o bom senso. Muitos gerentes se sobrepõem
aos seus próprios especialistas - os desenvolvedores. Isso também se aplica à migração para a nuvem. Spoiler: Quem precisa economizar
dinheiro, deve evitar a nuvem. Porque a nova palavra da moda "Serverless" na nuvem significa: você cuida do
software, nós cuidamos do hardware. No entanto, aquele que tem um administrador capaz, motivado e curioso,
pode operar Serverless por conta própria (por exemplo, [KNative](https://knative.dev)).

![aws_costs_twitter_1](/images/content/aws_costs_twitter_1.png)


### Funções Serverless vs Microservices:



#### Microserviços

Um microserviço típico sem estado cuida de uma função/dominio específico e é implantado em um ambiente de orquestração
de contêiner. Este ambiente cuida da infraestrutura, segurança, firewall, log, métricas, segredos, rede, backups e muito
mais. Uma grande vantagem é que um microserviço pode ser testado localmente com poucos recursos e é agnóstico em relação
à nuvem/servidor (pode ser usado em qualquer lugar).

#### Funções Serverless

Uma pequena piada para começar: Paradoxo, mas verdade - as funções sem servidor dependem muito do ambiente do servidor. :)
Uma função típica sem servidor também cuida de apenas uma função/dominio específico e é escrita sem frameworks
em
código puro, para ser mais rápido que um microserviço (também um bom exercício para microserviços). Uma grande
vantagem é que as funções sem servidor são escaladas automaticamente. No entanto, cada função sem servidor requer uma
quantidade considerável de GlueCode para definir a infraestrutura - segurança, firewall, rede, registro, métricas,
segredos, cache, backups e muito mais.
Portanto, uma função simples como copiar um arquivo, incluindo API, pode facilmente cobrir 1500 linhas de código (incl. IaC).
Os custos administrativos mudam da administração para o desenvolvimento em uma proporção de 1:N (1 para funções
sem servidor). O conhecimento e a implementação, portanto, não são mais
agrupados e podem se tornar instáveis rapidamente. Além disso, os custos de manutenção aumentam.
Testes integrativos reais raramente são possíveis com o sem servidor ou estão associados a um grande esforço.
Por fim, a complexidade das funções sem servidor é significativamente maior do que a de um único microserviço.
Maior complexidade também significa menor manutenibilidade. Novos membros da equipe têm mais dificuldade e precisam de muito
mais conhecimento prévio.

### Serverless e a Cloud em geral

A maioria das tecnologias em nuvem não estão atualizadas. Por exemplo, Node.js, Java, Python e outras
linguagens ou tecnologias muitas vezes não são fáceis de atualizar, na maioria das vezes só se pode esperar.
Também as tecnologias modernas e padrão, como MongoDB, MySQL, Kafka, NATS, RabbitMQ, Redis, Prometheus, InfluxDB, Grafana,
Kibana, Elastic Search etc., ou não estão disponíveis ou são muito caras.
Sem esses serviços padrão, muitas vezes se está na era digital da pedra e se usa soluções desatualizadas, como
Webhooks para a comunicação externa. Além disso, o espaço para ação em questões como regulamentação,
conformidade, proteção de dados e segurança de falhas é muito limitado.

A nuvem, portanto, deve ser operada de forma agnóstica para se poder alternar rapidamente entre AWS, Azure, Google, On-Premise, etc. e
para poder comparar custos.
Limitações também são frequentes na nuvem, o que leva a soluções alternativas criativas que por sua vez aumentam a complexidade
também aumenta. Testes integrativos também podem ser caros, pois cada desenvolvedor precisa de seu próprio ambiente de desenvolvimento na nuvem
pois muitos serviços de nuvem são dificilmente ou não testáveis localmente.
Mas até mesmo sem testes, a nuvem é cara. Enquanto em sistemas On-Premise principalmente
os custos de hardware são incorridos, na nuvem você tem que pagar adicionalmente pelo tráfego, alguns serviços padrão e muitas vezes até mesmo pelo
para a dupla tributação. Além disso, é fácil perder a visão geral na nuvem, porque não é sobre
amigável ao usuário, mas sobre dinheiro. Os custos são tão escondidos que você só os nota quando é tarde demais.

Os fundamentos da arquitetura e da infraestrutura devem ser reinventados na nuvem e especialmente na área serverless
pois a implementação depende fortemente das funções disponíveis.
Sempre depois de desenhar a arquitetura, me ocorre o pensamento: "Isso poderia ter sido um único serviço".

Para mim, Serverless é uma ideia interessante e é bem escalável, mas não reduz os custos. Pelo
contrário, requer muito mais conhecimento e tempo de desenvolvimento. Serverless ou a nuvem exigem disciplina e
conhecimento prévio.
Se o conhecimento para sistemas On-Premise não está disponível, não será mais fácil com a nuvem.
Como os desenvolvedores devem adquirir conhecimento adicional sobre infraestrutura?

Eu preferiria um cluster Kubernetes bem gerenciado sobre a arquitetura em nuvem.
Os funcionários também não escalam. Muitos desenvolvedores não têm disciplina na escrita de código.
Infelizmente, isso se aplica a 80 por cento dos desenvolvedores. Então, como esses desenvolvedores poderiam operar a nuvem
poder?

É importante que as empresas entendam completamente os desafios e impactos da arquitetura sem servidor e da nuvem.
Isso requer não apenas conhecimento técnico, mas também uma abordagem estratégica. Uma migração precipitada para a nuvem pode levar a complexidade, custos mais altos e sobrecarga para os desenvolvedores.

Em resumo, Serverless na nuvem é um conceito promissor que, no entanto, deve ser cuidadosamente
considerado. Custos, complexidade, manutenibilidade e as habilidades da equipe de desenvolvimento devem ser
consideradas.
Cada empresa tem suas próprias exigências e prioridades. Você deve tomar uma decisão fundamentada sobre se
Serverless na nuvem é a solução certa ou se abordagens alternativas como
por exemplo, um bom cluster Kubernetes são a melhor escolha.

O uso bem sucedido de Serverless e Cloud Computing requer uma combinação de expertise técnica
planejamento estratégico e uma compreensão clara dos requisitos do negócio. Só assim se pode ver através da ilusão de Serverless e tomar a decisão certa para o próprio desenvolvimento de software.

### Conclusão

A introdução de funções sem servidor na nuvem promete flexibilidade, escalabilidade e alívio de
desenvolvedores de tarefas de infraestrutura. No entanto, não se deve se cegar com essa ilusão. O
mudança para a nuvem e o uso de funções sem servidor apresentam uma série de desafios.

Desenvolvedores devem aprender uma nova "linguagem" além do desenvolvimento real e assumir
mais responsabilidade sem o devido apoio.
A complexidade das funções sem servidor é muitas vezes maior do que a dos microsserviços, uma vez que os desenvolvedores têm muitos adicionais
tarefas como definição de infraestrutura, segurança e escalabilidade para assumir. Testes integrativos reais são
difíceis e o conhecimento prévio e a experiência para a operação são ainda mais importantes na nuvem.

A própria nuvem traz mais desafios. Muitas tecnologias de nuvem não estão atualizadas
e o uso de serviços padrão modernos pode ser caro ou até impossível. Regulamentações, conformidade e
proteção de dados limitam a margem de manobra. Além disso, os custos na nuvem podem facilmente sair do controle,
e a visão geral dos gastos é rapidamente perdida.

No geral, é preciso pesar cuidadosamente os prós e contras de Serverless e Cloud.
As empresas devem considerar suas necessidades específicas, o know-how existente na equipe e o impacto a longo prazo
de uma migração para a nuvem.
Uma decisão bem fundamentada com base em uma análise abrangente é crucial para o sucesso e a rentabilidade
do projeto.

No final das contas, cabe às empresas apoiar adequadamente seus desenvolvedores, avaliar realisticamente os custos e a complexidade do
nuvem e considerar soluções alternativas como clusters Kubernetes bem gerenciados.
Com uma estratégia clara e uma compreensão sólida de suas próprias necessidades, as empresas podem aproveitar ao máximo as vantagens do
nuvem e funções sem servidor e ver através da ilusão.

### Contato

[Problemas do GitHub](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
