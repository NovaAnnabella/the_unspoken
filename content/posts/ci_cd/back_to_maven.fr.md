---
title: "Retour à Maven ?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "La recherche insaisissable de la simplicité et un bref voyage pour redécouvrir la puissance de Maven"
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# Retour à Maven ?

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/revenir-a-maven-degradle/)

## 10 ans de Gradle. À la recherche de facilité et un court voyage pour redécouvrir la force de Maven.

Désolé, il n'y a pas de texte en markdown à traduire car le markdown est un langage de balisage utilisé pour formater du texte. Voulez-vous que je traduise un texte spécifique en markdown ?

### Maximisation du potentiel des développeurs - Nous avons besoin d'outils qui économisent du temps

Les sujets souvent négligés ou rarement discutés m'intéressent. Souvent, des technologies intéressantes sont utilisées,
mais personne ne parle des problèmes qui y sont liés. Le développement est devenu très complexe de nos jours. Avec des
buzzwords comme "Serverless", "Low Code", "IaC", "Big Data", "Cloud", "DevOps", "You Build it You run it", etc., les
développeurs ont déjà suffisamment de tâches supplémentaires à gérer. Plus de tâches signifient qu'il y a peu d'experts
et que quelque chose est toujours négligé. C'est pourquoi l'automatisation et la sauvegarde de temps sont essentielles.
"Don't make me think" et "Works out of the Box" sont déjà de bonnes caractéristiques de qualité, que je ne peux pas voir
dans Gradle pour être honnête. Pour être juste, Gradle n'est pas le seul outil moderne qui nous complique la vie au lieu
de nous faciliter la tâche.

### La quête illusoire de simplicité et d'automatisation

Depuis SOAP, j'ai une aversion profondément enracinée pour les configurations basées sur XML. Avec Gradle, j'avais
espéré que l'écriture de scripts de liaison serait un jeu d'enfant. Malheureusement, mes espoirs et ma motivation ont
diminué à chaque fois. Gradle vise la flexibilité et sacrifie l'automatisation et la qualité en conséquence. Les
développeurs suivent aveuglément la tendance sans se soucier des conséquences sur la fiabilité du logiciel. Pour rendre
les scripts de construction Gradle simples et faciles à entretenir, une discipline stricte est nécessaire. Une telle
discipline est déjà rarement trouvée dans le code source et est donc encore plus rare dans les scripts de construction.

### Traductions et solutions de contournement - Lorsque les scripts de construction deviennent un défi

Gradle ne fonctionne pas beaucoup différemment de Maven en arrière-plan. Certaines traductions sont donc nécessaires. Des fonctionnalités telles que le Catalogue de dépendances, le plugin de publication Maven, Dependabot et bien d'autres sont en fait des solutions de contournement pour des fonctions fondamentales que Maven possède déjà. Avec la flexibilité de Gradle, des configurations de build complexes sont souvent créées, ce qui les rend difficiles à maintenir. Les plugins Gradle ont souvent des problèmes de compatibilité, des limites ou des évolutions limitées. Ces problèmes sont dus à la nature en évolution de l'écosystème Gradle, à la diversité des environnements dans lesquels Gradle est utilisé et au coût spécifique de mise en œuvre et de maintenance pour chaque plugin. Tout est connecté.

### L'effet domino de Gradle - Un scénario de cauchemar dans le monde réel

J'ai vu de nombreux microservices qui n'avaient que quelques années et qui étaient déjà difficiles à maintenir en raison de Gradle. Il est important de mentionner que ce n'était pas la première fois que je voyais quelque chose comme ça et non, ce n'étaient pas des développeurs juniors.

Ma **tâche consistait à effectuer une mise à niveau de Spring Boot 2.x vers 2.7**. Spoiler: j'ai abandonné après un an! Les problèmes en bref :

* Le fichier de génération Gradle exige la rétrogradation de ma version Java locale à la version 11 (WTF) (Normalement, Java est rétrocompatible - il existe également des outils de contournement tels que SdkMan...)
* La mise à jour de Spring Boot nécessite -> Mise à jour de Gradle (WTF)
* La mise à jour de Gradle nécessite -> Mise à jour du plug-in
* La mise à jour du plug-in nécessite -> Mise à jour de Groovy (WTF)
* La mise à jour de Groovy nécessite -> Mise à jour du framework de test et des mises à jour de tests (WTF)
* La mise à jour du framework de test nécessite -> Mises à jour des dépendances
* \[...]
  En outre, certains plugins ne fonctionnent pas avec des versions plus récentes de Gradle, certains ne sont plus en développement, sont incompatibles avec d'autres plugins, ne fonctionnent qu'avec Gradle KTS, pas avec Gradle Groovy, ou ont tout simplement des limites. Même les plugins des grands fournisseurs tels que Spring ont des fonctionnalités limitées par rapport à leurs plugins Maven. À la fin, j'ai une courte et cool date de génération Gradle que personne ne peut vraiment entretenir, même pas les développeurs qui l'ont écrite, et ils adorent toujours Gradle. Je connais peu de gens qui peuvent comprendre et écrire sérieusement des scripts Gradle.

### La redécouverte de la force de Maven - Utiliser les pouvoirs magiques de Maven

Voici mes fonctions préférées de Maven :
Les plugins peuvent être démarrés et configurés directement depuis la ligne de commande sans avoir à être définis au préalable. De plus, ils sont largement indépendants des autres configurations de plugins.

| Commande d'exemple                          | Description                                                                                                                                                           | Lien                                                                           |
|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| `mvn versions:use -latest-versions`         | Mettre à jour les versions - Qui a besoin de Dependabot ? Oui, mes projets sont mis à jour depuis des années sans demande de fusion fastidieuse.                       | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html     |
| `mvn versions:set -DnewVersion=1.0.0`       | Définir la version du projet...                                                                                                                                       | https://www.mojohaus.org/versions/versions-maven-plugin/index.html           |
| `mvn license:add-third-party`               | Listez les dépendances et affichez leurs licences (il peut même échouer lorsqu'il y a des licences exclues)                                                          | https://www.mojohaus.org/license-maven-plugin/index.html                     | 

Cette liste pourrait continuer pour toujours. Cela me rappelle d'une certaine manière les étapes Workflow de GitHub.

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)

```

### Vous n'aimez pas XML ?

Pas de problème! Il suffit d'écrire votre fichier de construction en `ruby`, `groovy`, `scala`, `yaml`,`atom` ou `Java`. L'extension Polygot (https://github.com/takari/polyglot-maven) le rend possible. Pour essayer, exécutez simplement `mvn io.takari.polyglot: polyglot-translate-plugin: translate -Dinput=pom.xml -Doutput=pom.yaml` et votre fichier de construction sera traduit en quelques millisecondes. Dommage qu'il n'y ait pas de traducteur fiable Maven <> Gradle :( Les fichiers de construction de Maven sont volumineux mais aussi très faciles à comprendre. Les modifications ou le débogage sont effectués en un rien de temps.

### L'âge n'est qu'un numéro - la stabilité et l'évolution des Mavens

Reconnaissons-le, Maven existe depuis un certain temps déjà et son esthétique ne correspond peut-être pas aux normes actuelles. Toutefois, la durabilité de Maven lui a permis de s'adapter et de se développer. Maven fonctionne indépendamment de votre projet. Les fichiers de construction peuvent être facilement réutilisés. Les plugins s'exécutent dans un bac à sable et sont indépendants les uns des autres et indépendants de la version de Java ou de Maven. Cette conception favorise la stabilité et la prévisibilité et facilite la gestion de processus de construction complexes sans conflits inattendus.

### Conclusion

De nos jours, l'environnement de développement est surchargé de tâches et de technologies pour les développeurs. À la recherche de simplicité et d'automatisation, Gradle est apparu en tant qu'outil de construction moderne, mais il a apporté ses propres défis. Il ne fait aucun doute que le concept de Gradle est bon ! Cependant, compte tenu de la complexité et du temps investi dans les scripts de construction Gradle, la question se pose de savoir s'il ne serait pas plus facile d'étendre Maven. Avec des plugins et des extensions, Maven peut être rafraîchi et simplifié à tout moment. Le développement ultérieur ne serait-il pas plus excitant et durable que de passer d'une technologie à l'autre ?

### Liens

* [Retour de Gradle à Maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### Contact

[Problèmes GitHub](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).```
