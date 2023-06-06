---
title: "Illusion Serverless & Cloud"
date: 2023-05-24
author: "Nova Annabella"
slug: illusion_serverless_cloud
tags: [ Development, Serverless, Cloud, Microservices, Scalability, Architecture, Infrastructure ]
categories: [ Technology, Software, Cloud ]
description: "Défis et réalités des fonctionnalités sans serveur dans le cloud. Un aperçu précieux pour les entreprises qui envisagent une migration vers le cloud".
draft: false
images:
  - "/images/content/onprem_vs_cloud.png"
card: "summary_large_image"
---



# L'illusion des fonctions Serverless dans le cloud

![aws_costs_twitter_1](/images/content/onprem_vs_cloud.png)

### Introduction

Je suis déçu de voir à quel point le marketing l'emporte souvent sur le bon sens. De nombreux managers s'imposent au-
dessus de leurs propres experts - les développeurs. Cela vaut également pour la migration vers le cloud. Spoiler : Celui
qui économise de l'argent doit éviter le cloud. Car le nouveau mot à la mode "serverless" dans le cloud signifie : tu
t'occupes du matériel. logiciel, nous nous occupons du matériel. Toutefois, celui qui a un administrateur compétent,
motivé et curieux, peut peut aussi gérer lui-même le serverless (par ex. [KNative](https://knative.dev)).
![aws_costs_twitter_1](/images/content/aws_costs_twitter_1.png)

### Fonctions sans serveur vs microservices :



#### Microservices

Un microservice sans état typique s'occupe d'une fonction/d'un domaine spécifique et est déployé dans un environnement
d'orchestration. environnement d'orchestration de conteneurs. Cet environnement s'occupe de l'infrastructure, de la
sécurité, du pare-feu, logging, métriques, secrets, réseau, sauvegardes et bien plus encore. Un grand avantage est qu'un
microservice peut être utilisé localement avec quelques peut être testé de manière intégrée et est agnostique au niveau
du cloud/serveur (utilisable partout).

#### Fonctions Serverless

Une petite blague pour commencer : paradoxal mais vrai - les fonctions serverless dépendent fortement de l'environnement
du serveur. :) Une fonction serverless typique s'occupe également d'une seule fonction/domaine spécifique et est écrite
sans frameworks en écrite en code pur pour être plus rapide qu'un microservice (également un bon exercice pour les
MicroServices). Un grand avantage avantage est que les fonctions Serverless sont automatiquement mises à l'échelle.
Cependant, chaque fonction serverless nécessite une quantité considérable de GlueCode pour définir l'infrastructure -
sécurité, pare-feu, réseau, logging, métriques, Secrets, mise en cache, sauvegardes et bien plus encore. C'est pourquoi
une fonction simple comme la copie d'un fichier, API comprise, peut rapidement atteindre 1500 lignes de code (IaC
compris) comprend un certain nombre de lignes. Les coûts d'administration se déplacent de l'administration vers le
développement dans un rapport 1:N (1 vers les fonctions Serverless. fonctions). Les connaissances et l'implémentation ne
sont donc plus regroupées et peuvent rapidement devenir instables. À cela s'ajoutent des coûts de maintenance accrus. De
même, les véritables tests intégratifs sont rares avec le serverless, ou alors ils sont très coûteux. En fin de compte,
la complexité des fonctions serverless est nettement plus élevée que celle d'un microservice individuel. Une complexité
plus élevée signifie également une maintenabilité plus faible. Les nouveaux membres de l'équipe ont plus de mal et ont
besoin de beaucoup plus de connaissances. plus de connaissances préalables.

### Serverless et le cloud en général

La plupart des technologies cloud ne sont pas à la pointe du progrès. Par exemple, Node.js, Java, Python et d'autres
langages ou technologies ne sont souvent pas faciles à mettre à jour, la plupart du temps, la seule solution est
d'attendre. Même les technologies modernes et standard comme MongoDB, MySQL, Kafka, NATS, RabbitMQ, Redis, Prometheus,
InfluxDB, Grafana, Kibana, Elastic Search, etc. ne sont pas disponibles ou sont trop chers. Sans de tels services
standard, on se trouve souvent à l'âge de pierre virtuel et on utilise des solutions obsolètes, par ex. Webhooks pour la
communication avec l'extérieur. A cela s'ajoute le fait que la marge de manœuvre sur des sujets tels que la
réglementation, conformité, la protection des données et la sécurité contre les défaillances est fortement limitée. Le
cloud devrait donc être géré de manière agnostique, afin de pouvoir passer rapidement d'AWS, Azure, Google, On-Premise,
etc. et de comparer les coûts. pouvoir comparer les coûts. Les limites sont aussi souvent présentes dans le cloud, ce
qui conduit à des solutions de contournement créatives qui, à leur tour, augmentent la complexité. augmentent la
complexité. Les tests intégratifs peuvent également être coûteux, car chaque développeur dispose de son propre
environnement de développement dans le cloud. car de nombreux services en nuage sont peu ou pas testables localement.
Mais même sans tests, le cloud est coûteux. Alors que dans les systèmes sur site, ce sont surtout les coûts de Dans le
cloud, il faut payer en plus le trafic, certains services standard et souvent même la taxation. payer des taxes
multiples. De plus, on perd facilement la vue d'ensemble dans le cloud, car il ne s'agit pas d'une question d'argent. la
facilité d'utilisation, mais l'argent. Les coûts sont tellement cachés qu'on ne les remarque que lorsqu'il est trop
tard. il est trop tard. Les bases de l'architecture et de l'infrastructure doivent être réinventées dans le cloud, et
en particulier dans le domaine du serverless. doivent être réinventés, car la mise en œuvre dépend fortement des
fonctionnalités disponibles. Chaque fois que j'ai conçu l'architecture, je me dis : "Cela aurait pu être un service
unique". aurait pu". Pour moi, le serverless est une idée intéressante et il est bien évolutif, mais il ne réduit pas
les coûts. Au contraire Au contraire, cela demande beaucoup plus de connaissances et de temps de développement. Le
serverless ou le cloud exigent de la discipline et de la des connaissances préalables. Si les connaissances ne sont pas
acquises pour les systèmes sur site, cela ne sera pas plus facile avec le cloud. Comment les développeurs peuvent-ils
acquérir des connaissances supplémentaires en matière d'infrastructure ? Je préférerais un cluster Kubernetes bien géré
à l'architecture cloud. Les collaborateurs n'évoluent pas. De nombreux développeurs n'ont aucune discipline dans
l'écriture de code. Malheureusement, c'est le cas de 80 % des développeurs. Alors comment ces développeurs peuvent-ils
encore utiliser le cloud ? peuvent-ils faire ? Il est important que les entreprises comprennent les défis et les
implications de l'architecture sans serveur et du cloud. comprendre de manière globale. Cela nécessite non seulement des
connaissances techniques, mais aussi une approche stratégique. Une Une migration vers le cloud non réfléchie peut
entraîner une complexité, une augmentation des coûts et une surcharge des développeurs. En résumé, le Serverless in the
Cloud est un concept prometteur, mais qui doit être examiné avec soin. devrait être considéré. Les coûts, la complexité,
la maintenabilité et les capacités de l'équipe de développement doivent être pris en compte. doivent être pris en
compte. Chaque entreprise a des besoins et des priorités différents. Il faut prendre une décision éclairée pour savoir
si Serverless dans le cloud est la bonne solution ou si des approches alternatives, telles que par exemple, un cluster
Kubernetes est un meilleur choix. L'utilisation réussie du serverless et du cloud computing requiert une combinaison
d'expertise technique. une planification stratégique et une compréhension claire des besoins de l'entreprise. Ce n'est
qu'ainsi qu'il est possible d'éviter l'illusion du serverless et prendre la bonne décision pour son propre développement
logiciel.

### Fazit

L'introduction de fonctions sans serveur dans le cloud promet flexibilité, évolutivité et décharge des développeurs des
tâches d'infrastructure. Il ne faut toutefois pas se laisser aveugler par cette illusion. Le site passage au cloud et
l'utilisation de fonctions serverless s'accompagnent d'un certain nombre de défis. Les développeurs doivent apprendre
un nouveau "langage" en plus du développement proprement dit et, sans soutien approprié, ils doivent assumer de
nouvelles responsabilités. prendre plus de responsabilités. La complexité des fonctions sans serveur est souvent plus
élevée que celle des microservices, car les développeurs doivent faire face à de nombreuses tâches supplémentaires.
doivent assumer des tâches telles que la définition de l'infrastructure, la sécurité et la mise à l'échelle. Les
véritables tests intégratifs sont difficiles et les connaissances préalables ainsi que l'expérience pour l'exploitation
sont encore plus importantes dans le cloud. Le cloud lui-même présente d'autres défis. De nombreuses technologies cloud
ne sont pas à la pointe du progrès. et l'utilisation de services standard modernes peut être coûteuse, voire impossible.
Les exigences réglementaires, la conformité et protection des données limitent la marge de manœuvre. De plus, les coûts
dans le cloud dérapent facilement, et la vue d'ensemble des dépenses se perd rapidement. Dans l'ensemble, il convient
de peser soigneusement les avantages et les inconvénients du serverless et du cloud. Les entreprises devraient tenir
compte de leurs besoins spécifiques, du savoir-faire existant au sein de l'équipe et des effets à long terme. tenir
compte d'une migration vers le cloud. Une décision éclairée, basée sur une analyse complète, est déterminante pour la
réussite et la rentabilité du projet. du projet. En fin de compte, il appartient aux entreprises d'apporter un soutien
adéquat à leurs développeurs, d'évaluer les coûts et la complexité du cloud. évaluer le cloud de manière réaliste et
d'envisager des solutions alternatives telles que des clusters Kubernetes bien gérés. Avec une stratégie claire et une
bonne compréhension de leurs besoins, les entreprises peuvent tirer parti de tirer le meilleur parti du cloud et des
fonctionnalités sans serveur et de voir clair dans l'illusion.

### Contact

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
