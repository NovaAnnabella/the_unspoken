---
title: "Illusion Serverless & Cloud"
date: 2023-05-24
author: "Nova Annabella"
slug: illusion_serverless_cloud
tags: [ Development, Serverless, Cloud, Microservices, Scalability, Architecture, Infrastructure ]
categories: [ Technology, Software, Cloud ]
description: "Desafios e realidades das capacidades sem servidor na nuvem. Informações valiosas para as empresas que estão a considerar uma migração para a nuvem".
draft: false
images:
  - "/images/content/onprem_vs_cloud.png"
card: "summary_large_image"
---



# A ilusão das funções sem servidor na nuvem

![aws_costs_twitter_1](/images/content/onprem_vs_cloud.png)

### Introdução

Fico desiludido com a frequência com que o marketing triunfa sobre o bom senso. Muitos gestores colocam-se a si próprios
sobre os seus próprios especialistas - os programadores. Isto também se aplica à migração para a nuvem. Spoiler: Se
precisa de poupar dinheiro se precisa de poupar dinheiro deve evitar a nuvem. Porque a nova palavra de ordem "sem
servidor" na nuvem significa: Você trata do software, nós tratamos do hardware. Você trata do software, nós tratamos do
hardware. No entanto, se tiver um administrador capaz, motivado e curioso, pode também pode operar sem servidor por
conta própria (por exemplo, [KNative](https://knative.dev)).
![aws_costs_twitter_1](/images/content/aws_costs_twitter_1.png)

### Funções sem servidor vs microsserviços:



#### Microsserviços

Um microsserviço sem estado típico ocupa-se de uma função/domínio específico e é implantado num ambiente de orquestração
de contentores. Esse ambiente cuida da infraestrutura, da segurança, do firewall, registo de dados, métricas, segredos,
rede, cópias de segurança e muito mais. Uma grande vantagem é que um microsserviço pode ser implantado localmente com
poucos recursos e é agnóstico em relação à nuvem/servidor (pode ser implantado em qualquer lugar).

#### Funções sem servidor

Uma pequena piada antes de começar: Paradoxal, mas verdadeiro - as funções sem servidor dependem muito do ambiente do
servidor. :) Uma função sem servidor típica também cuida apenas de uma função/domínio específico e é escrita em código
puro sem estruturas para ser mais rápida do que um microsserviço. código para ser mais rápido do que um microsserviço
(também um bom exercício para MicroServices). Uma grande vantagem é que as funções sem servidor escalam automaticamente.
No entanto, cada função serverless requer uma quantidade considerável de GlueCode para definir a infraestrutura -
segurança, firewall, rede, registo, métricas, segredos, cache, backups e muito mais. Por conseguinte, uma função simples
como a cópia de um ficheiro incluindo API pode envolver rapidamente 1500 linhas de código (incluindo IaC). podem estar
envolvidos. Os custos de administração passam da administração para o desenvolvimento num rácio de 1:N (1 para funções
sem servidor). funções sem servidor). O conhecimento e a implementação não são mais agrupados e podem rapidamente
tornar-se instáveis. Além disso, há um aumento nos custos de manutenção. Os verdadeiros testes integrativos também são
raros com o serverless, ou só são possíveis com grande esforço. Em última análise, a complexidade das funções sem
servidor é significativamente maior do que a de um único microsserviço. Maior complexidade também significa menor
capacidade de manutenção. Os novos membros da equipa têm mais dificuldade e precisam de mais conhecimento prévio.

### Serverless e a nuvem em geral

A maioria das tecnologias de computação em nuvem não está actualizada. Por exemplo, Node.js, Java, Python e outras
linguagens ou tecnologias não estão actualizadas. linguagens ou tecnologias muitas vezes não são fáceis de actualizar,
normalmente só a espera ajuda. Mesmo as tecnologias modernas e padrão, como MongoDB, MySQL, Kafka, NATS, RabbitMQ,
Redis, Prometheus, InfluxDB, Grafana, Kibana, Elastic Search, etc., ou não estão disponíveis ou são demasiado caras. Sem
esses serviços normalizados, está-se frequentemente na idade da pedra virtual e utilizam-se soluções desactualizadas,
por exemplo webhooks para comunicação externa. Além disso, a margem de manobra em questões como a regulamentação,
conformidade, protecção de dados e segurança contra falhas é severamente limitada. A nuvem deve, por conseguinte, ser
gerida de forma agnóstica para poder alternar rapidamente entre AWS, Azure, Google, on-premise, etc. e para comparar os
custos. As limitações também são comuns na nuvem, levando a soluções criativas que, por sua vez, aumentam a
complexidade. aumentar. Os testes de integração também podem tornar-se dispendiosos, uma vez que cada programador
precisa do seu próprio ambiente de desenvolvimento na nuvem uma vez que muitos serviços na nuvem são dificilmente ou
nada testáveis localmente. Mas mesmo sem testes, a nuvem é cara. Enquanto nos sistemas locais os custos são
principalmente hardware, na nuvem também é preciso pagar pelo tráfego, por alguns serviços padrão e, muitas vezes, até
por múltiplos e, muitas vezes, até por múltiplas tributações. Além disso, é fácil perder o controlo das coisas na nuvem,
porque não se trata de não se trata de facilidade de utilização, mas de dinheiro. Os custos estão tão escondidos que só
nos apercebemos deles quando é demasiado tarde. é demasiado tarde. Os princípios básicos da arquitectura e da infra-
estrutura têm de ser reinventados na nuvem e, especialmente, no serverless têm de ser reinventados, pois a implementação
depende muito dos recursos disponíveis. Sempre que concebo a arquitectura, penso: "Isto poderia ter sido um único
serviço". poderia ter sido". Para mim, o serverless é uma ideia interessante e tem uma boa escala, mas não reduz os
custos. Pelo contrário Pelo contrário, requer muito mais conhecimento e tempo de desenvolvimento. Serverless ou a nuvem
requerem disciplina e conhecimento prévio. Se o conhecimento não existe para sistemas locais, não será mais fácil com a
nuvem. Como é que os programadores devem adquirir conhecimentos adicionais sobre infra-estruturas? Eu preferiria um
cluster Kubernetes bem gerido a uma arquitectura em nuvem. As pessoas não escalam. Muitos programadores não têm
disciplina para escrever código. Infelizmente, isto é verdade para 80 por cento dos programadores. Então, como é que
estes programadores vão ser capazes de executar a nuvem? a nuvem? É importante que as organizações compreendam
plenamente os desafios e as implicações da arquitectura sem servidor e da nuvem. Compreender plenamente os desafios e as
implicações da arquitectura sem servidor e da nuvem. Isto requer não só conhecimentos técnicos, mas também uma abordagem
estratégica. A migração irreflectida para a nuvem pode levar à complexidade, a custos mais elevados e a uma sobrecarga
dos programadores. Em resumo, a arquitectura sem servidor na nuvem é um conceito promissor, mas que deve ser
considerado cuidadosamente. deve ser considerado com cuidado. É necessário ter em conta o custo, a complexidade, a
capacidade de manutenção e as competências da equipa de desenvolvimento. ser tidos em conta. Cada empresa tem requisitos
e prioridades diferentes. Deve ser tomada uma decisão informada sobre se Sem servidor na nuvem é a solução certa ou se
abordagens alternativas como e.g. bem Kubernetes Cluster são a melhor escolha. A implantação bem-sucedida da computação
sem servidor e em nuvem requer uma combinação de conhecimentos técnicos planeamento estratégico e uma compreensão clara
dos requisitos comerciais. Só então a ilusão de serverless pode ser e tomar a decisão certa para o seu próprio
desenvolvimento de software.

### Fazit

A introdução de funções sem servidor na nuvem promete flexibilidade, escalabilidade e alívio das tarefas de
infraestrutura. Os desenvolvedores de software podem se livrar das tarefas de infraestrutura. No entanto, não nos
devemos deixar cegar por esta ilusão. A A mudança para a nuvem e o uso de funções sem servidor traz consigo uma série de
desafios. Os programadores têm de aprender uma nova "linguagem" para além do desenvolvimento real e assumir mais
responsabilidades sem o apoio adequado. assumir mais responsabilidades. A complexidade das funções sem servidor é
frequentemente mais elevada do que a dos microsserviços, uma vez que os programadores têm de assumir muitas tarefas
adicionais, tais como os programadores têm de assumir muitas tarefas adicionais, como a definição da infra-estrutura, a
segurança e o escalonamento. Os verdadeiros testes integrativos são difícil e o conhecimento e a experiência prévios em
operações são ainda mais importantes na nuvem. A própria nuvem traz outros desafios. Muitas tecnologias de computação
em nuvem não estão actualizadas e a utilização de serviços modernos prontos a utilizar pode ser dispendiosa ou mesmo
impossível. Os requisitos regulamentares, a conformidade e a protecção de dados limitam o âmbito de aplicação. Para além
disso, os custos na nuvem saem facilmente do controlo, e a visão geral das despesas perde-se rapidamente. Em suma, as
vantagens e desvantagens do serverless e da nuvem precisam de ser cuidadosamente ponderadas. As empresas devem
considerar os seus requisitos específicos, a experiência existente na equipa e os efeitos a longo prazo de uma migração
para a nuvem. de uma migração para a nuvem. Uma decisão informada, baseada numa análise abrangente, é crucial para o
sucesso e a rentabilidade do projecto. do projecto. Em última análise, cabe às empresas apoiar adequadamente os seus
programadores, avaliar de forma realista os custos e a complexidade da migração para a nuvem de forma realista e
considerar soluções alternativas, como clusters Kubernetes bem geridos. Com uma estratégia clara e uma sólida
compreensão das suas próprias necessidades, as empresas podem tirar o máximo partido dos benefícios da nuvem e das
capacidades sem servidor e ver através da ilusão.

### Contacto

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
