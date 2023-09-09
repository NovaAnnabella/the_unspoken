---
title: "Retour à Maven?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "La recherche insaisissable de simplicité et un court voyage pour redécouvrir le pouvoir de Maven."
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# Retour à Maven ?

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

## 10 ans de Gradle. À la recherche de soulagement et un bref voyage pour redécouvrir la force de Maven.



### Maximisation du potentiel des développeurs - Nous avons besoin de plus d'outils pour gagner du temps

Les sujets souvent ignorés ou rarement discutés m'intéressent. Souvent, des technologies cool sont en jeu, mais presque
personne ne parle des problèmes qui y sont associés. Le développement est devenu très coûteux de nos jours. Avec des
mots à la mode cool comme "Serverless", "Low Code", "IaC", "Big Data", "Cloud", "DevOps", "You Build it You run it"
etc., les développeurs ont déjà plus que suffisamment de tâches supplémentaires à accomplir. Plus de tâches signifie
qu'il y a à peine des experts restent et toujours quelque chose est négligé pour le focus. C'est pourquoi les
automatisations et les économies de temps sont méga important. “Ne me fais pas penser ” et “Fonctionne dès la sortie de
la boîte” sont déjà de bonnes caractéristiques de qualité que je n’ai pas encore peut voir dans Gradle. Pour être juste,
Gradle n'est pas le seul outil moderne qui nous donne du travail au lieu de le faire faciliter.

### La quête illusoire de simplicité et d'automatisation

Depuis SOAP, j'ai une aversion profondément ancrée pour les configurations basées sur XML. Avec Gradle, j'espérais que
l'écriture de scripts Bind serait un jeu d'enfant. Malheureusement, mes espoirs et ma motivation diminuaient de fois en
fois. Gradle vise la flexibilité et sacrifie l'automatisation et la qualité. Les développeuses et développeurs suivent
aveuglément la tendance sans tenir compte des conséquences sur la fiabilité du logiciel. Pour maintenir les Scripts de
construction Gradle simples et faciles à entretenir, une discipline stricte est nécessaire. Une telle discipline est
rarement trouvée dans le code source, c'est donc encore plus rare dans les scripts de construction.

### Traductions et solutions de contournement - Quand les scripts de construction deviennent un défi

Gradle ne fonctionne pas beaucoup différemment en arrière-plan que Maven. Par conséquent, certaines traductions sont nécessaires. Des fonctionnalités comme le
Catalogue de dépendances, le Plugin de version Maven, le Dependabot et beaucoup d'autres sont en fait des solutions de contournement pour les fonctions de base
que Maven apporte déjà. Avec la flexibilité de Gradle, des configurations de construction complexes se produisent souvent,
qui sont difficiles à maintenir.
Les plugins Gradle ont souvent des problèmes de compatibilité, des limites ou des développements limités. Ces problèmes surviennent
à cause de la nature en évolution de l'écosystème Gradle, de la diversité des environnements dans lesquels Gradle est déployé,
et de l'effort d'implémentation et de maintenance spécifique pour chaque plugin. Tout est connecté.

### L'effet domino de Gradle - Un scénario cauchemardesque dans le monde réel

J'ai vu beaucoup de microservices qui n'avaient que quelques années et étaient déjà non maintenables à cause de Gradle. Il est important de mentionner que ce n'est pas la première fois que je vois cela, et non, ce n'étaient pas des
développeurs juniors.

Ma **tâche était de réaliser une mise à niveau de Spring Boot 2.x à 2.7**. Spoiler : J'ai abandonné après un an ! Les problèmes en bref :

* Le fichier de build Gradle nécessite -> Downgrade de ma version locale de Java à 11 (WTF) (Normalement, Java est
  rétrocompatible - il existe aussi des outils de contournement comme SdkMan...)
* La mise à jour de Spring Boot nécessite -> Mise à jour de Gradle (WTF)
* La mise à jour de Gradle nécessite -> Mise à jour du plugin
* La mise à jour du plugin nécessite -> Mise à jour de Groovy (WTF)
* La mise à jour de Groovy nécessite -> Mises à jour du framework de test et des tests (WTF)
* La mise à jour du framework de test nécessite -> Mises à jour des dépendances
* \[...]
  De plus, certains plugins ne fonctionnent pas avec les versions plus récentes de Gradle, certains ne sont plus développés, sont incompatibles avec d'autres plugins, ne fonctionnent qu'avec Gradle KTS, pas avec Gradle Groovy, ou
  ont simplement des limites. Même les plugins de grands fournisseurs comme Spring ont une fonctionnalité limitée par rapport à leurs plugins Maven. À la fin, j'ai un cool court fichier de build Gradle que personne ne peut vraiment maintenir,
  pas même les développeurs qui l'ont écrit, et ils aiment toujours Gradle. Je connais peu de personnes
  qui peuvent vraiment comprendre ou écrire des scripts Gradle.

### La redécouverte de la force de Maven - Utiliser les pouvoirs magiques de Maven

Voici mes fonctions préférées de Maven :
Les plugins peuvent être lancés et configurés directement à partir de la ligne de commande, sans qu'ils aient besoin d'être définis au préalable. De plus, ils sont largement indépendants des autres configurations de plugins.

| Commande Exemplaire                    | Description                                                                                                                                               | Lien                                                                     | 
|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `mvn versions:use -latest-versions`   | Mettre à jour les versions - qui a besoin de Dependabot ? Oui, mes projets sont mis à jour sans problème depuis des années vers la dernière version, sans demandes de fusion gênantes | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0` | Définir la version du projet...                                                                                                                               | https://www.mojohaus.org/versions/versions-maven-plugin/index.html       |
| `mvn license:add-third-party`         | Énumérer les dépendances et afficher leurs licences (peut même échouer avec des licences exclues)                                                            | https://www.mojohaus.org/license-maven-plugin/index.html                 | 

Cette liste pourrait continuer indéfiniment. Cela me rappelle un peu les étapes du flux de travail GitHub.

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)


### Tu n'aimes pas le XML ?

Pas de problème! Il suffit d'écrire votre fichier de construction en `ruby`, `groovy`, `scala`, `yaml`, `atom` ou `Java`. L'extension Polyglot (https://github.com/takari/polyglot-maven) le rend possible. Pour l'essayer, exécutez simplement `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` et en quelques millisecondes votre fichier de construction est traduit. Dommage qu'il n'y ait pas de traducteur Maven <> Gradle fiable :( 
Oui, les fichiers de construction Maven sont volumineux, mais aussi très faciles à comprendre. Les améliorations ou le débogage sont faits en un rien de temps.

### L'âge n'est qu'un nombre - Stabilité et évolution de Mavens

Certes, Maven existe depuis un certain temps et son esthétique ne correspond peut-être pas aux normes d'aujourd'hui.
Cependant, la longévité de Maven lui a permis de s'adapter et d'évoluer. Maven fonctionne indépendamment
de votre projet. Les fichiers de construction peuvent être facilement réutilisés.
Les plugins fonctionnent dans un bac à sable et sont indépendants les uns des autres et indépendants de la version de Java ou de Maven.
Cette conception favorise la stabilité et la prévisibilité et facilite la gestion des processus de construction complexes sans conflits inattendus.

### Conclusion

De nos jours, l'environnement de développement est surchargé de nombreuses tâches et technologies pour les développeurs. En cherchant
la simplicité et l'automatisation, Gradle est apparu comme un outil de construction moderne, mais a apporté ses propres
défis. Sans aucun doute, le concept de Gradle est bon ! Cependant, face à la complexité et au
temps investi dans les scripts de construction Gradle, la question se pose s'il ne serait pas plus facile d'étendre Maven à
. Avec des plugins et des extensions, Maven pourrait être rafraîchi et simplifié à tout moment. Ne serait-ce pas
beaucoup plus excitant et également plus durable de continuer à développer au lieu de sauter d'une technologie à l'autre?

### Liens

* [Retour de Gradle à maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### Contact

[Problèmes GitHub](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
