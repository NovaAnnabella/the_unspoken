---
title: "Niveaux de test : Trouver le bon équilibre"
date: 2023-05-31
author: "Nova Annabella"
slug: test_level
tags: [ Testing, Software Testing, Test Levels, Mock Tests, Unit Tests, Integration Tests, Component Tests, Contract Tests, End-to-End Tests ]
categories: [ Technology, Software Development, Quality Assurance ]
description: "Trouver le bon équilibre dans le choix des niveaux de test appropriés pour les tests logiciels"
draft: false
images:
  - "/images/content/martin_fowler_testing.png"
card: "summary_large_image"
---


# Niveaux de test : Trouver le bon équilibre

[ ![testebenen](/images/content/martin_fowler_testing.png)](https://martinfowler.com/articles/microservice-testing/)

### Introduction

Le thème du testing semble encore aujourd'hui être un terrain vierge avec une très grande liberté d'interprétation. La
traditionnelle pyramide de test a été remise en question et de nouvelles pyramides de test ont vu le jour. A mon avis,
il ne faut pas de pyramide de test, mais une compréhension claire de ce qui doit être testé. Les tests de niveau
inférieur sont souvent moins significatifs. L'accent devrait être mis avant tout sur les tests de comportement, afin de
s'assurer que la API ou l'UI fonctionne comme prévu. Un aperçu complet des types de tests possibles peut être consulté
ici : [Martinfowler Testing](https://martinfowler.com/articles/microservice-testing/).

### Niveau 1 - Tests fictifs et tests unitaires

Objectif : exercer les plus petites parties testables du logiciel dans l'application afin de déterminer si elles
fonctionnent comme prévu. fonctionnent. Les mock-tests et les tests unitaires peuvent être contre-productifs et
entravent souvent le processus de développement. Ces tests sont souvent détachés du contexte et ont peu de rapport avec
la réalité. Ils ne servent souvent qu'à maintenir des fonctions inutiles via des tests d'unit existants. maintenir des
tests unitaires. Dès que des mocks sont ajoutés, cela devient une auto-occupation. Les résultats attendus résultats des
tests de mock sont limités à ce qui a été défini dans le mock original. Les utilisateurs finaux ne s'intéressent pas aux
fonctions internes. Par exemple, dans un scénario de connexion `loginUser(name, password, securityAlgorithm)`. Si le
test unitaire effectue un contrôle nul sur sur le paramètre `securityAlgorithm`, le test est trop important, car les
utilisateurs ne peuvent pas peuvent définir.

### Niveau 2 - Test d'intégration

Objectif : vérifier les voies de communication et les interactions entre les composants afin de détecter les défauts
d'interface. défauts d'interface. Les tests d'intégration fournissent des informations précieuses sur les performances
et l'indépendance des différentes parties de l'application. de l'application. Avec moins de mocks, les tests deviennent
plus compréhensibles. Cependant, ils manquent toujours de contexte et il y a un risque de voir des le risque existe que
les tests d'intégration soient simplement des tests unitaires déguisés avec moins de mocks.

### Niveau 3 - Test de contenu

Objectif : limiter la portée du logiciel testé à une partie du système à tester, manipuler le système via des interfaces
de code internes et l'utilisation de doublons de test pour isoler le code à tester d'autres composants Composants. Les
tests de composants fournissent un grand nombre d'informations sur la qualité et les performances de l'application. Au
lieu de mocks, tu testes enfin ton application. La frontière entre les tests de composants et les tests de bout en bout
n'est pas significative. significative. Avec un bon environnement de test, les frontières entre les deux s'estompent
souvent, de sorte que le test du réel comportement au lieu de fonctions isolées et hors contexte devient possible.
Toutefois, la création de classes de test supplémentaires classes de test telles que les stubs de composants, les fakes
et les mocks dans le code de production implique une maintenance supplémentaire.

### Niveau 4 - Test du contrat

L'objectif de ce bloc de code est de vérifier les interactions à la frontière d'un service externe et de de s'assurer
qu'il répond aux exigences contractuelles d'un service consommateur. Les tests contractuels ressemblent souvent à des
tests de composants, et la différence entre eux est minime. Certains développeurs associent ces tests aux tests Pact,
qui fonctionnent essentiellement comme des tests unitaires avec un serveur entre les deux. Le effort pour maintenir ces
tests pourrait cependant ne pas en valoir la peine. Par exemple, un test Pact pourrait utiliser la REST API
`loginUser?name=aa&password=bb)` et attendre une réponse de schéma JSON qui a été préalablement envoyée sur le serveur
Pact a été téléchargée. Ce schéma est statique et sujet à des erreurs telles que des formats de date ou des fuseaux
horaires incorrects dans la réponse de l'API. réponse de l'API. Les conséquences négatives peuvent être énormes.

### Niveau 5 - Tests de bout en bout (également appelés tests de la boîte noire)

Objectif : vérifier qu'un système répond à des exigences externes et atteint ses objectifs, en testant l'ensemble du
système de bout en bout. testé du début à la fin. Les tests de bout en bout sont fiables et robustes. Dès que les
obstacles de la mise en place de l'environnement de test sont surmontés, l'investissement est rentable. efforts sont
rentabilisés. Ces tests simulent un comportement réel et éliminent le besoin de mock. Les erreurs sont moins fréquentes
et sont plus faciles à reproduire localement. Le débogage coûteux et la tenue de protocoles en production sont évités.
sont en grande partie évités, tout comme les incidents rares. Les développeurs travaillent moins souvent, voire pas du
tout, avec des données de production, ce qui réduit la responsabilité et augmente la concentration. En outre, les
automatismes tels que les les mises à jour automatiques des logiciels sont exécutées parce que le comportement a déjà
été testé. Il y a d'autres avantages ! Une fois que les tests sont écrits sous une forme réutilisable, ils peuvent être
intégrés dans des tests de charge afin d'obtenir une vue d'ensemble de la fonctionnalité. obtenir une image complète de
la fonctionnalité. Ces tests peuvent également être exécutés en continu dans l'environnement de production être exécutés
et fournir un aperçu en temps réel de l'état des différents flux de travail. Lorsqu'un sous-système, tel que par
exemple, un service REST externe, est mis hors ligne, il est possible d'identifier immédiatement les workflows des
utilisateurs sont concernés.

### Fazit

En résumé, les tests sont un aspect essentiel du développement de logiciels et le choix des niveaux de test dépend des
objectifs de l'application. des exigences et des objectifs spécifiques de l'application. Alors que les mock-tests et les
tests unitaires ont une efficacité limitée, ils peuvent peuvent être limités, les tests d'intégration et les tests de
composants offrent un aperçu précieux du comportement et des performances de l'application. performances de
l'application. Les tests contractuels aident à vérifier les interactions avec des services externes, mais ton
démarcation avec les tests de composants peut être minime. En fin de compte, les tests de bout en bout offrent le plus
haut niveau de confiance dans la fonctionnalité du système. la fonctionnalité du système et permettent de tester
l'ensemble de l'application. En choisissant les tests appropriés niveaux de test et leur combinaison efficace, les
développeurs peuvent garantir la qualité, la fiabilité et la robustesse de ton logiciel.

### Contact

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
