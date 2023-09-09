---
title: "Serveur sans illusion et Cloud"
date: 2023-05-24
author: "Nova Annabella"
slug: illusion_serverless_cloud
tags: [ Development, Serverless, Cloud, Microservices, Scalability, Architecture, Infrastructure ]
categories: [ Technology, Software, Cloud ]
description: "Défis et réalités des fonctions sans serveur dans le Cloud. Aperçus précieux pour les entreprises envisageant une migration vers le cloud"
draft: false
images:
  - "/images/content/onprem_vs_cloud.png"
card: "summary_large_image"
---


# L'illusion des fonctions sans serveur dans le Cloud

![aws_costs_twitter_1](/images/content/onprem_vs_cloud.png)

### Introduction

Je suis déçu de voir combien de fois le marketing triomphe du bon sens. Beaucoup de managers se placent
au-dessus de leurs propres experts - les développeurs. Cela s'applique également à la migration vers le cloud. Spoiler : ceux qui
doivent économiser de l'argent devraient éviter le cloud. Car le nouveau buzzword "Serverless" dans le cloud signifie: tu t'occupes du
logiciel, nous nous occupons du matériel. Cependant, celui qui a un administrateur compétent, motivé et curieux peut
aussi gérer Serverless lui-même (par exemple [KNative](https://knative.dev)).

![aws_costs_twitter_1](/images/content/aws_costs_twitter_1.png)

### Fonctions Serverless vs Microservices:



#### Microservices

Un microservice sans état typique s'occupe d'une fonction/domaine spécifique et est déployé dans un
environnement d'orchestration de conteneurs. Cet environnement prend en charge l'infrastructure, la sécurité, le pare-feu,
la journalisation, les métriques, les secrets, le réseau, les sauvegardes et bien plus encore. Un grand avantage est qu'un microservice peut être testé localement avec
peu de
ressources et est agnostique aux nuages/servers (peut être utilisé partout).

#### Fonctions sans serveur

Une petite blague pour commencer : Paradoxe, mais vrai - Les fonctions sans serveur dépendent fortement de l'environnement du serveur. :)
Une fonction typique sans serveur se soucie également d'une seule fonction / domaine et est écrite sans frameworks
en
code pur pour être plus rapide qu'un microservice (également un bon exercice pour les microservices). Un grand
avantage est que les fonctions sans serveur sont automatiquement échelonnées. Cependant, chaque fonction sans serveur nécessite
une quantité considérable de GlueCode pour définir l'infrastructure - sécurité, pare-feu, réseau, journalisation, métriques,
secrets, mise en cache, sauvegardes et bien plus encore.
Par conséquent, une fonction simple tel que la copie d'un fichier, y compris l'API, peut facilement représenter 1500 lignes de code (y compris IaC).
Les coûts d'administration sont donc déplacés de l'administration au développement dans un rapport de 1:N (1 à
fonctions sans serveur). Les connaissances et la mise en œuvre ne sont donc plus 
regroupées et peuvent rapidement devenir instables. De plus, les coûts de maintenance augmentent.
De plus, les tests d'intégration réels sont rares ou nécessitent un grand effort avec Serverless.
En fin de compte, la complexité des fonctions sans serveur est nettement plus élevée que celle d'un seul microservice. 
Une complexité plus élevée signifie également une maintenabilité plus faible. Les nouveaux membres de l'équipe ont plus de difficultés et ont besoin de beaucoup
plus de connaissances préalables.

### Serverless et le Cloud en général

La plupart des technologies cloud ne sont pas à jour. Par exemple, Node.js, Java, Python et autres
langages ou technologies ne sont souvent pas faciles à mettre à jour, bien souvent il n'y a pas d'autre solution que d'attendre.
De plus, des technologies modernes et standard comme MongoDB, MySQL, Kafka, NATS, RabbitMQ, Redis, Prometheus, InfluxDB, Grafana,
Kibana, Elastic Search etc. ne sont soit pas disponibles, soit trop chères.
Sans ces services standard, on se retrouve souvent dans l'âge de pierre virtuel et on utilise des solutions obsolètes, par exemple
des webhooks pour la communication externe. En outre, la marge de manœuvre en matière de réglementation,
de conformité, de protection des données et de sécurité en cas de panne est largement limitée.

Le cloud devrait donc être exploité de manière agnostique, afin de passer rapidement entre AWS, Azure, Google, On-Premise etc. et
pour comparer les coûts.
Il y a souvent des limites dans le cloud qui mènent à des solutions de contournement créatives, ce qui augmente à son tour la complexité.
Les tests intégratifs peuvent également coûter cher, car chaque développeur a besoin de son propre environnement de développement dans le cloud
car de nombreux services cloud ne sont peu ou pas testables localement.
Mais même sans tests, le cloud est cher. Alors que dans le cas des systèmes sur site, il s'agit principalement de
coûts de matériel, dans le cloud, il faut en plus payer pour le trafic, certains services standard et souvent même pour la
double imposition. De plus, on perd facilement la vue d'ensemble dans le cloud, car il ne s'agit pas de
la convivialité, mais de l'argent. Les coûts sont si bien dissimulés qu'on ne les remarque que lorsqu'il est trop tard.

Les bases de l'architecture et de l'infrastructure doivent être réinventées dans le cloud et en particulier dans le domaine des serveurs 
puisque l'implémentation dépend fortement des fonctions disponibles.
Chaque fois que j'ai conçu l'architecture, je pense : "Cela aurait pu être un seul service".

Pour moi, le serverless est une idée intéressante et elle est bien scalable, mais elle ne réduit pas les coûts. Au
contraire, elle nécessite beaucoup plus de connaissances et de temps pour le développement. Le serverless ou le cloud nécessitent de la discipline et
une expertise préalable.
Si la connaissance des systèmes sur site n'est pas disponible, cela ne sera pas plus facile avec le cloud.
Comment les développeurs peuvent-ils en plus acquérir des connaissances en infrastructure ?

Je préférerais un cluster Kubernetes bien géré à l'architecture cloud.
Les employés ne sont pas scalables. Beaucoup de développeurs n'ont pas de discipline dans l'écriture de code.
Malheureusement, cela s'applique à 80% des développeurs. Comment ces développeurs pourraient-ils alors utiliser le cloud ?

Il est important que les entreprises comprennent pleinement les défis et les implications de l'architecture sans serveur et du cloud.
Cela nécessite non seulement des connaissances techniques, mais aussi une approche stratégique. Une migration irréfléchie vers le cloud peut entraîner une complexité accrue, des coûts plus élevés et une surcharge des développeurs.

En résumé, le serverless dans le cloud est un concept prometteur, mais qui doit être examiné attentivement.
Les coûts, la complexité, la maintenabilité et les capacités de l'équipe de développement doivent être pris en compte.
Chaque entreprise a des exigences et des priorités différentes. Il faut prendre une décision éclairée sur le fait que 
le serverless dans le cloud est la bonne solution ou si des alternatives comme.
par exemple un bon cluster Kubernetes sont un meilleur choix.

L'utilisation réussie des serverless et du cloud computing nécessite une combinaison d'expertise technique,
de planification stratégique et d'une compréhension claire des exigences commerciales. C'est la seule façon de voir à travers l'illusion du serverless
et de prendre la bonne décision pour son propre développement logiciel.

### Conclusion

L'introduction de fonctions sans serveur dans le cloud promet flexibilité, évolutivité et soulagement de
développeurs des tâches d'infrastructure. Cependant, on ne devrait pas se laisser tromper par cette illusion. Le
changement vers le cloud et l'utilisation de fonctions sans serveur entraînent une série de défis.

Les développeurs doivent apprendre un nouveau "langage" à côté du développement réel et assumer
plus de responsabilités sans le soutien approprié.
La complexité des fonctions sans serveur est souvent plus élevée que celle des microservices, car les développeurs ont beaucoup de tâches supplémentaires
tâches telles que la définition de l'infrastructure, la sécurité et l'évolutivité. De véritables tests d'intégration sont
difficiles et les connaissances préalables ainsi que l'expérience pour le fonctionnement sont encore plus importantes dans le cloud.

Le cloud lui-même présente d'autres défis. Beaucoup de technologies cloud ne sont pas à jour
et l'utilisation de services standard modernes peut être coûteuse, voire impossible. Des exigences réglementaires, la conformité et
la protection des données limitent la marge de manœuvre. En outre, les coûts dans le cloud peuvent facilement déraper,
et on perd rapidement le contrôle des dépenses.

Dans l'ensemble, il est nécessaire de peser soigneusement les avantages et les inconvénients du sans serveur et du cloud.
Les entreprises devraient tenir compte de leurs exigences spécifiques, des connaissances existantes dans l'équipe et des impacts à long terme
d'une migration vers le cloud.
Une décision éclairée basée sur une analyse complète est cruciale pour le succès et la rentabilité
du projet.

En fin de compte, il appartient aux entreprises de soutenir adéquatement leurs développeurs, d'évaluer réaliste les coûts et la complexité du
Le cloud et d'envisager des solutions alternatives comme des clusters Kubernetes bien gérés.
Avec une stratégie claire et une bonne compréhension de leurs propres besoins, les entreprises peuvent tirer le meilleur parti du
Cloud et des fonctions sans serveur et voir à travers l'illusion.


### Contact

[Problèmes GitHub](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
