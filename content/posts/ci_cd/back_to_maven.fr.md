---
title: "Retour à Maven?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "La recherche insaisissable de simplicité et un bref voyage pour redécouvrir le pouvoir de Maven"
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# Retour à Maven?

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

## 10 ans de Gradle. À la recherche de soulagement et un court voyage pour redécouvrir la force de Maven.

You didn't provide any text to be translated. Please provide the text you want translated into French.

### Maximisation du potentiel des développeurs - Nous avons besoin de plus d'outils permettant de gagner du temps

Les sujets souvent négligés ou rarement discutés m'intéressent. Souvent, des technologies sympas sont en place, mais
presque personne ne parle des problèmes qui y sont associés. Le développement est devenu très laborieux de nos jours.
Avec les mots à la mode cool comme “Serverless”, “Low Code”, “IaC”, “Big Data”, “Cloud”, “DevOps”, “You Build it You run
it” etc. les développeurs ont déjà plus que suffisamment de tâches supplémentaires à accomplir. Plus de tâches signifie
qu'il y a de moins en moins d'experts et que quelque chose est toujours négligé pour se concentrer. C'est pourquoi les
automatisations et les économies de temps sont très importants. “Ne me faites pas penser” et “Fonctionne dès la sortie
de la boîte” sont déjà de bons indicateurs de qualité que je ne peux pas voir dans Gradle. Pour être juste, Gradle
n'est pas le seul outil moderne qui nous donne du travail au lieu de le faciliter.

### La recherche illusoire de simplicité et d'automatisation

Depuis SOAP, j'ai une aversion profondément enracinée contre les configurations basées sur XML. Avec Gradle, j'espérais
que l'écriture de scripts de liaison serait un jeu d'enfant. Malheureusement, mes espoirs et ma motivation ont diminué à
chaque fois. Gradle vise la flexibilité et sacrifie l'automatisation et la qualité. Les développeurs et développeuses
suivent aveuglément la tendance sans tenir compte de ses impacts sur la fiabilité du logiciel. Pour que les scripts de
construction Gradle soient simples et nécessitent peu d'entretien, une discipline rigoureuse est nécessaire. Une telle
discipline est rarement observée dans le code source, et elle est donc encore plus rare dans les scripts de
construction.

### Traductions et solutions de contournement - Quand les scripts de construction deviennent un défi

Gradle ne fonctionne pas beaucoup différemment en arrière-plan que Maven. Par conséquent, certaines traductions sont nécessaires. Des fonctionnalités comme le
Catalogue des dépendances, le plugin Maven Release, le Dependabot et beaucoup d'autres sont en fait des solutions de contournement pour les fonctions de base
que Maven apporte déjà avec lui. Avec la flexibilité de Gradle, des configurations de build complexes sont souvent créées,
qui sont difficiles à maintenir.
Les plugins Gradle ont souvent des problèmes de compatibilité, des limites ou des développements limités. Ces problèmes surviennent
en raison de la nature évolutive de l'écosystème Gradle, de la diversité des environnements dans lesquels Gradle est utilisé
et de l'effort spécifique de mise en œuvre et de maintenance pour chaque plugin. Tout est lié ensemble.

### L'effet domino de Gradle - Un scénario de cauchemar dans le monde réel

J'ai vu beaucoup de microservices qui n'avaient que quelques années et étaient déjà ingérables à cause de Gradle. Il est important de mentionner que ce n'est pas la première fois que je vois cela et non, ce n'étaient pas des développeurs juniors.

Ma **tâche était de réaliser une mise à niveau de Spring Boot 2.x à 2.7**. Spoiler : J'ai abandonné après un an!
Les problèmes en bref :

* Le fichier de construction Gradle nécessite -> Downgrade de ma version locale de Java à 11 (WTF) (Java est normalement
  compatible avec les versions précédentes - il y a aussi ici encore des outils de contournement comme SdkMan...)
* La mise à jour de Spring Boot nécessite -> Mise à jour de Gradle (WTF)
* La mise à jour de Gradle nécessite -> Mise à jour du plugin
* La mise à jour du plugin nécessite -> Mise à jour de Groovy (WTF)
* La mise à jour de Groovy nécessite -> Mise à jour du framework de test et des tests (WTF)
* La mise à jour du framework de test nécessite -> Mise à jour des dépendances
* \[...]
  De plus, certains plugins ne fonctionnent pas avec des versions plus récentes de Gradle, certains ne sont plus développés,
  sont incompatibles avec d'autres plugins, ne fonctionnent qu'avec Gradle KTS, pas avec Gradle Groovy, ou
  ont simplement des limites. Même les plugins de grands fournisseurs comme Spring ont une fonctionnalité limitée par rapport à leurs plugins Maven.
  À la fin, j'ai un fichier de construction Gradle cool et court que personne ne peut vraiment entretenir,
  pas même les développeurs qui l'ont écrit, et ils aiment toujours Gradle. Je connais peu de personnes qui
  comprennent ou peuvent écrire sérieusement des scripts Gradle.

### La redécouverte de la force de Maven - Utiliser les pouvoirs magiques de Maven

Voici mes fonctions préférées de Maven :
Les plugins peuvent être lancés et configurés directement à partir de la ligne de commande, sans avoir à être définis au préalable. De plus, ils sont largement indépendants des autres configurations de plugins.

| Commande exemple                  | Description                                                                                                                                          | Lien                                                                     | 
|-----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `mvn versions:use -latest-versions`   | Mise à jour des versions - qui a besoin de Dependabot? Oui, mes projets sont mis à jour sans problème à la dernière version depuis des années, sans demandes de fusion ennuyeuses | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0` | Définir la version du projet...                                                                                                                       | https://www.mojohaus.org/versions/versions-maven-plugin/index.html       |
| `mvn license:add-third-party`         | Listez les dépendances et affichez leurs licences (peut même échouer avec des licences exclues)                                                      | https://www.mojohaus.org/license-maven-plugin/index.html                 | 

Cette liste pourrait continuer indéfiniment. Cela me rappelle un peu les étapes de travail de GitHub.

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)


### Tu n'aimes pas le XML ?

Pas de problème ! Écrivez simplement votre fichier de construction en `ruby`, `groovy`, `scala`, `yaml`, `atom` ou `Java`. L'extension Polyglot (https://github.com/takari/polyglot-maven) le rend possible. Pour essayer, exécutez simplement `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` et en quelques millisecondes, votre fichier de construction est traduit. Dommage qu'il n'y ait pas de traducteur Maven <> Gradle fiable :( 
Oui, les fichiers de construction Maven sont grands, mais aussi très faciles à comprendre. Les corrections ou le débogage sont effectués en un rien de temps.

### L'âge n'est qu'un nombre - Stabilité et évolution de Mavens

Certes, Maven existe depuis un certain temps et son esthétique peut ne pas correspondre aux normes actuelles. Cependant,
la longévité de Maven lui a permis de s'adapter et d'évoluer. Maven fonctionne indépendamment de votre projet. Les
fichiers de construction peuvent être facilement réutilisés. Les plugins fonctionnent dans un bac à sable et sont
indépendants les uns des autres et indépendants de la version Java ou Maven. Cette conception favorise la stabilité et
la prévisibilité, et facilite la gestion de processus de construction complexes sans conflits inattendus.

### Conclusion

De nos jours, l'environnement de développement est surchargé de nombreuses tâches et technologies pour les développeurs. À la recherche
de simplicité et d'automatisation, Gradle est apparu comme un outil de build moderne, mais a apporté ses propres
défis. Sans aucun doute, le concept de Gradle est bon ! Cependant, face à la complexité et au
temps investi dans les scripts de build Gradle, on peut se demander s'il ne serait pas plus simple d'étendre Maven à
la place. Avec des plugins et des extensions, Maven pourrait être rafraîchi et simplifié à tout moment. Ne serait-ce pas
plus excitant et aussi plus durable de continuer à développer plutôt que de sauter d'une technologie à l'autre ?

### Liens

* [Retour de Gradle à Maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### Contact

[Problèmes GitHub](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
