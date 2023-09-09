---
title: "Niveaux de test : Trouver le bon équilibre"
date: 2023-05-31
author: "Nova Annabella"
slug: test_level
tags: [ Testing, Software Testing, Test Levels, Mock Tests, Unit Tests, Integration Tests, Component Tests, Contract Tests, End-to-End Tests ]
categories: [ Technology, Software Development, Quality Assurance ]
description: "Trouver le bon équilibre dans le choix des niveaux de test appropriés pour les tests de logiciels"
draft: false
images:
  - "/images/content/martin_fowler_testing.png"
card: "summary_large_image"
---


# Niveaux de test : Trouver le bon équilibre

[![testebenen](/images/content/martin_fowler_testing.png)](https://martinfowler.com/articles/microservice-testing/)


### Introduction

Le sujet des tests semble encore aujourd'hui être une terra incognita avec beaucoup d'espace pour l'interprétation. La pyramide de test traditionnelle a été remise en question et de nouvelles pyramides de tests ont vu le jour. À mon avis, il n'est pas nécessaire d'avoir une pyramide de test, mais une compréhension claire de ce qui doit être testé. Les tests à des niveaux inférieurs sont souvent moins significatifs. L'accent devrait être mis surtout sur le test du comportement, pour s'assurer que l'API ou l'interface utilisateur fonctionne comme désiré. Un aperçu complet des types de tests possibles peut être trouvé ici : [Martinfowler Testing](https://martinfowler.com/articles/microservice-testing/).


### Niveau 1 - Tests Mock & Tests Unitaires

Objectif : Exercer les plus petits éléments de logiciel testables dans l'application pour déterminer s'ils fonctionnent comme prévu.

Les tests mock et unitaires peuvent être contre-productifs et entraver souvent le processus de développement. Ces tests sont souvent
découplés du contexte et ont peu de rapport avec la réalité. Ils servent souvent uniquement à maintenir des fonctions inutiles au-dessus de l'existant
Tests unitaires. Dès que les mocks sont ajoutés, cela devient une activité auto-centrée. Les résultats attendus
des tests mock sont limités à ce qui a été défini dans le mock original. Les utilisateurs finaux
ne se soucient pas des fonctions internes. Par exemple, dans un 
scénario de connexion `loginUser(name, password, securityAlgorithmus)`. Si le test unitaire effectue une vérification nulle sur
le paramètre `securityAlgorithm`, trop de choses sont testées, car les utilisateurs ne peuvent pas 
définir le paramètre `securityAlgorithm`.

### Niveau 2 - Test d'intégration

Objet: Examiner les voies de communication et les interactions entre les composants pour détecter des défauts
d'interface. Les tests d'intégration fournissent des informations précieuses sur la performance et l'indépendance des
différentes parties de l'application. Avec moins de simulations, les tests sont plus compréhensibles. Cependant, ils
manquent toujours de contexte, et il y a un risque que les tests d'intégration ne soient simplement des tests unitaires
déguisés avec moins de simulations.

### Niveau 3 - Test de Composant

Objectif : Limiter la portée des logiciels testés à une partie du système à tester, manipulation du système par des
interfaces de code internes et utilisation de doubles de test pour isoler le code à tester des autres composants. Les
tests de composants fournissent une multitude d'informations sur la qualité et les performances de l'application. Au
lieu de Mocks, vous testez enfin votre application. La frontière entre les tests de composants et les tests de bout en
bout n'est pas significatifs. Avec un bon environnement de test, les frontières entre eux s'estompent souvent,
permettant ainsi le test du réel comportement au lieu de fonctions isolées et décontextualisées. Cependant, la création
de classes de test supplémentaires telles que les stubs de composants, les imitations et les mockups dans le code de
production peut entraîner des efforts de maintenance supplémentaires.

### Niveau 4 - Test de contrat

Le but de ce bloc de code est de vérifier les interactions à la limite d'un service externe et
s'assurer qu'il répond aux exigences contractuelles d'un service consommateur.

Les tests de contrat ressemblent souvent aux tests de composants, et la différence entre eux est minime. Certains développeurs
associent ces tests aux tests Pact, qui fonctionnent essentiellement comme des tests unitaires avec un serveur intermédiaire. Cependant la
la peine à maintenir ces tests pourrait ne pas en valoir la peine. Par exemple, un test Pact pourrait
tester l'API REST `loginUser?name=aa&password=bb` et attendre une réponse en format JSON-Schema qui a été préalablement
téléchargée sur le serveur Pact. Ce schéma est statique et sujet à des erreurs comme des formats de date incorrects ou des fuseaux horaires dans la
réponse de l'API. Les impacts négatifs peuvent être énormes.


### Niveau 5 - Tests de bout en bout (également appelés tests de boîte noire)

But: Vérification qu'un système répond aux exigences externes et atteint ses objectifs en testant l'ensemble du système de
du début à la fin.

Les tests de bout en bout sont fiables et robustes. Une fois que les obstacles à la mise en place de l'environnement de test ont été surmontés, l'effort porte ses fruits. Ces tests simulent un comportement réel et éliminent le besoin de mock up. Les erreurs sont moins fréquentes
et sont plus faciles à reproduire localement. Les sessions de débogage exhaustives et la tenue de registres dans la production
sont largement évitées, tout comme les incidents rares. Les développeurs travaillent rarement, si jamais, avec
les données de production, ce qui réduit la responsabilité et augmente la concentration. De plus, les automatisations comme
les mises à jour logicielles automatiques facilitent l'exécution, car le comportement a déjà été testé. Il y a d'autres avantages! Une fois
que les tests sont rédigés sous une forme réutilisable, ils peuvent être intégrés dans les tests de charge pour donner un
image complète de la fonctionnalité. Ces tests peuvent également être exécutés en continu dans l'environnement de production
et offrir des perspectives en temps réel sur l'état des différents workflows. Si un sous-système, comme
par exemple un service REST externe, est hors ligne, il peut être immédiatement identifié quels flux de travail des utilisateurs
sont affectés.

### Conclusion

En résumé, les tests sont un aspect essentiel du développement logiciel, et le choix des niveaux de test dépend des
exigences et objectifs spécifiques de l'application. Bien que les tests simulés et les tests unitaires peuvent être
limités en efficacité, les tests d'intégration et les tests de composants offrent des aperçus précieux sur le
comportement et les performances de l'application. Les tests de contrat aident à vérifier les interactions avec les
services externes, mais votre démarcation avec les tests de composants peut être minimale. En fin de compte, les tests
de bout en bout offrent le plus haut niveau de confiance dans la fonctionnalité du système et permettent des tests
complets de l'application entière. En choisissant les niveaux de test appropriés et leur combinaison efficace, les
développeurs peuvent garantir la qualité, la fiabilité et la robustesse de leur logiciel.

### Contact

[Problèmes GitHub](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
