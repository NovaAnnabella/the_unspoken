---
title: "Retour à Maven ?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "La recherche insaisissable de la simplicité et un court voyage pour redécouvrir la puissance de Maven"
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# Retour à Maven?

[ ![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)
``` 

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/revenir-de-gradle-a-maven/)

## 10 ans de Gradle. À la recherche de la facilité et d'un court voyage pour redécouvrir la force de Maven.

As a Translator, I need content to translate. Please provide me the content in Markdown format.

### Maximisation du potentiel des développeurs - Nous avons besoin de plus d'outils pour gagner du temps

Les sujets souvent négligés ou rarement discutés m'intéressent. Souvent, il y a des technologies cool en action, mais
presque personne ne parle des problèmes qui y sont associés. Le développement est devenu très coûteux de nos jours. Avec
des buzzwords cool comme "Serverless", "Low Code", "IaC", "Big Data", "Cloud", "DevOps", "You Build it You run it",
etc., les développeurs ont déjà assez de tâches supplémentaires à accomplir. Plus de tâches signifie qu'il y a de moins
en moins d'experts et que quelque chose est toujours négligé pour se concentrer sur autre chose. C'est pourquoi
l'automatisation et les gains de temps sont extrêmement importants. "Don't make me think" et "Works out of the Box" sont
déjà de bonnes caractéristiques de qualité que je ne peux pas voir dans Gradle. Pour être juste, Gradle n'est pas le
seul outil moderne qui nous pose des problèmes au lieu de les résoudre.

### La quête illusoire de la simplicité et de l'automatisation

Depuis SOAP, j'ai une aversion profondément enracinée pour les configurations basées sur XML. Avec Gradle, j'espérais
que l'écriture de scripts de liaison serait un jeu d'enfant. Malheureusement, mes espoirs et ma motivation ont diminué
de plus en plus à chaque fois. Gradle vise la flexibilité au détriment de l'automatisation et de la qualité. Les
développeurs suivent aveuglément les tendances sans se soucier des conséquences sur la fiabilité du logiciel. Pour
maintenir les scripts de construction Gradle simples et faciles à entretenir, une forte discipline est nécessaire. Une
telle discipline est déjà rarement présente dans le code source et elle est donc encore plus rare dans les scripts de
construction.

### Traductions et solutions de contournement - Lorsque les scripts de construction posent un défi

Gradle fonctionne fondamentalement de la même manière que Maven en arrière-plan. Par conséquent, certaines traductions sont nécessaires. Des fonctionnalités telles que le catalogue de dépendances, le plugin Maven Release, Dependabot et bien d'autres sont en fait des solutions de contournement pour des fonctionnalités de base que Maven apporte déjà. La flexibilité de Gradle entraîne souvent des configurations de construction complexes, qui sont difficiles à maintenir. Les plugins Gradle ont souvent des problèmes de compatibilité, des limites ou des développements limités. Ces problèmes sont dus à la nature en évolution de l'écosystème Gradle, à la diversité des environnements dans lesquels Gradle est utilisé, et à la charge de mise en œuvre et de maintenance spécifiques pour chaque plugin. Tout est connecté.

### L'effet domino de Gradle - un scénario cauchemardesque dans le monde réel

J'ai vu de nombreux microservices qui n'avaient que quelques années et qui étaient déjà ingérables en raison de Gradle. Il est important de mentionner que ce n'est pas la première fois que je vois ça et non, ce n'étaient pas des développeurs juniors.

**Ma tâche était de mettre à jour Spring Boot 2.x vers 2.7.** Spoiler : j'ai abandonné après un an ! Les problèmes en bref :

* Le fichier de construction Gradle nécessite -> une baisse de ma version locale de Java à 11 (WTF) (Normalement, Java est rétrocompatible - il y a également des outils de contournement tels que SdkMan...)
* La mise à jour de Spring Boot nécessite -> une mise à jour de Gradle (WTF)
* La mise à jour de Gradle nécessite -> une mise à jour du plug-in
* La mise à jour du plug-in nécessite -> une mise à jour de Groovy (WTF)
* La mise à jour de Groovy nécessite -> des mises à jour du cadre de tests (WTF)
* La mise à jour du cadre de tests nécessite -> des mises à jour des dépendances
* [...]

De plus, certains plug-ins ne fonctionnent pas avec les versions les plus récentes de Gradle, certains ne sont plus développés, sont incompatibles avec d'autres plug-ins, ne fonctionnent qu'avec Gradle KTS, pas avec Gradle Groovy, ou ont tout simplement des limites. Même les plug-ins de grands fournisseurs tels que Spring ont une fonctionnalité limitée par rapport à leurs plug-ins Maven. Au final, j'ai une belle petite fichier de construction Gradle, que personne ne peut gérer correctement, pas même les développeurs qui l'ont écrit, et ils aiment toujours Gradle. Je connais très peu de personnes qui comprennent sérieusement les scripts Gradle ou qui peuvent les écrire.

### La redécouverte de la force de Maven - Utiliser les pouvoirs magiques de Maven

Voici mes fonctionnalités préférées de Maven:
Les plugins peuvent être démarrés et configurés directement depuis la ligne de commande sans avoir besoin d'être définis au préalable. De plus, ils sont largement indépendants des autres configurations de plugins.

| Commande exemple                        | Description                                                                                                                                                                               | Lien                                                                     |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `mvn versions:use -latest-versions`     | Mettre à jour les versions - qui a besoin de Dependabot? Oui, mes projets sont mis à jour depuis des années avec la dernière version sans demandes de fusion ennuyeuses.                        | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0`   | Définir la version du projet...                                                                                                                                                           | https://www.mojohaus.org/versions/versions-maven-plugin/index.html       |
| `mvn license:add-third-party`           | Lister les dépendances et afficher leurs licences (peut même échouer dans le cas de licences exclues)                                                                                     | https://www.mojohaus.org/license-maven-plugin/index.html                 | 

Cette liste pourrait continuer indéfiniment. Cela me rappelle un peu les étapes du flux de travail de GitHub.

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)


```

### Vous n'aimez pas le XML ?

Pas de problème! Il suffit d'écrire votre fichier de construction en `ruby`, `groovy`, `scala`, `yaml`, `atom` ou `Java`. L'extension Polygot (https://github.com/takari/polyglot-maven) le rend possible. Pour essayer, il suffit d'exécuter `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` et en quelques millisecondes, votre fichier de construction est traduit. Dommage qu'il n'y ait pas de traducteur fiable Maven <> Gradle :( Oui, les fichiers de construction de Maven sont volumineux, mais ils sont également très faciles à comprendre. Les corrections ou le débogage sont rapidement effectués.

### L'âge n'est qu'un nombre - La stabilité et l'évolution des Maven

Admettons, Maven existe depuis un certain temps et son esthétique peut ne pas correspondre aux normes actuelles.
Cependant, la durabilité de Maven lui a permis de s'adapter et d'évoluer. Maven fonctionne indépendamment de votre
projet. Les fichiers de construction peuvent être facilement réutilisés. Les plugins s'exécutent dans une sandbox et
sont indépendants les uns des autres et indépendants de la version Java ou Maven. Cette conception favorise la stabilité
et la prévisibilité et rend facile la gestion de processus de construction complexes sans conflits inattendus.

### Conclusion

De nos jours, l'environnement de développement est surchargé pour les développeurs avec de nombreuses tâches et technologies. À la recherche de simplicité et d'automatisation, Gradle est apparu comme un outil de construction moderne, mais a apporté ses propres défis. Il est indéniable que le concept de Gradle est bon! Cependant, face à la complexité et au temps investi dans les scripts de construction de Gradle, la question se pose de savoir s'il ne serait pas plus facile d'étendre Maven. Avec des plugins et des extensions, Maven pourrait être rafraîchi et simplifié à tout moment. Ne serait-il pas plus passionnant et durable de faire évoluer, plutôt que de sauter d'une technologie à l'autre?

### Liens

* [Retour de Gradle à maven](https://phauer.com/2018/retour-de-gradle-a-maven/)

### Contact

[Problèmes GitHub](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).```
