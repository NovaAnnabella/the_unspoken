---
title: "Retourner à Maven ?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "L'insaisissable quête de simplicité et un bref voyage à la redécouverte du pouvoir de Maven"
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---



# Retourner à Maven ?

[ ![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

## 10 ans de Gradle. A la recherche d'un soulagement et un petit voyage pour redécouvrir la force de Maven.



### Maximiser le potentiel des développeurs - Nous avons besoin de plus d'outils pour gagner du temps

Les sujets qui sont souvent négligés ou rarement discutés m'intéressent. Souvent, des technologies cool sont utilisées,
mais presque personne ne parle des problèmes qui y sont liés. De nos jours, le développement est devenu très complexe.
Avec les mots à la mode comme "serverless", "low code", "IaC", "big data", "cloud", "DevOps", "you build it you run it",
les développeurs ont déjà beaucoup appris. etc., les développeurs ont déjà plus qu'assez de tâches supplémentaires à
accomplir. Plus de tâches, cela signifie qu'il n'y a presque plus experts et il y a toujours quelque chose qui est
négligé pour le Focus. C'est pourquoi l'automatisation et le gain de temps sont méga importants. sont importants. "Don't
make me think" et "Works out of the box" sont déjà de bons critères de qualité, que je ne vois pas encore dans Gradle.
ne sont pas visibles. Pour être juste, Gradle n'est pas le seul outil moderne qui nous fait faire du travail au lieu de
nous le faciliter. de nous faciliter la tâche.

### La recherche illusoire de la simplicité et de l'automatisation

Depuis SOAP, j'ai une aversion profondément enracinée pour les configurations basées sur XML. Avec Gradle, j'espérais
que l'écriture de scripts Bind serait un jeu d'enfant. Malheureusement, mes espoirs et ma motivation diminuaient de
s'amenuisent au fur et à mesure. Gradle aspire à la flexibilité et sacrifie pour cela l'automatisation et la qualité.
Les développeurs et développeuses développeurs suivent aveuglément la tendance sans se soucier des conséquences sur la
fiabilité du logiciel. Pour que Gradle Build, les scripts doivent rester simples et nécessiter peu de maintenance, ce
qui nécessite une discipline forte. Une telle discipline est déjà rare dans le On la trouve rarement dans le code source
et elle est donc encore plus rare dans les scripts de build.

### Traductions et solutions de contournement - Quand les scripts de construction deviennent un défi

Gradle ne fonctionne pas beaucoup différemment de Maven en arrière-plan. C'est pourquoi quelques traductions sont
nécessaires. Des fonctionnalités comme le Dependency Catalog, le Maven Release Plugin, le Dependabot et bien d'autres
sont en fait des solutions de contournement pour des fonctions de base. fonctions que Maven apporte déjà. Avec la
flexibilité de Gradle, on obtient souvent des configurations de build complexes, qui sont difficiles à maintenir. Les
plugins Gradle ont souvent des problèmes de compatibilité, des limites ou des évolutions limitées. Ces problèmes
surviennent en raison de la nature évolutive de l'écosystème Gradle, de la diversité des environnements dans lesquels
Gradle est utilisé est utilisé, et de l'effort de mise en œuvre et de maintenance spécifique à chaque plugin. Tout est
interconnecté.

### L'effet domino de Gradle - Un scénario cauchemardesque dans le monde réel

J'ai vu beaucoup de microservices qui n'avaient que quelques années et qui n'étaient déjà plus maintenables à cause de
Gradle. étaient devenus inutiles. Il est important de mentionner que ce n'est pas la première fois que je vois cela, et
non, ce n'était pas des Junior Devs. Ma **tâche était d'effectuer une mise à niveau de Spring Boot 2.x vers 2.7**.
Spoiler : J'ai abandonné au bout d'un an abandonné ! Les problèmes en bref : * Le fichier de construction Gradle
nécessite -> Downgrade de ma version locale de Java à 11 (WTF) (Normalement, Java est  compatible en amont - il y a là
aussi des outils de contournement comme SdkMan...) * La mise à jour du Spring Boot nécessite -> Gradle-Update (WTF) * La
mise à jour Gradle nécessite -> Mise à jour du plugin * La mise à jour du plugin nécessite -> Groovy-Update (WTF) * La
mise à jour de Groovy nécessite -> Mises à jour du framework de test et des tests (WTF) * La mise à jour du framework de
test nécessite -> Mises à jour des dépendances * \[...]  De plus, certains plugins ne fonctionnent pas avec les
versions récentes de Gradle, certains ne sont plus développés  sont développés, sont incompatibles avec d'autres
plugins, ne fonctionnent qu'avec Gradle KTS, pas avec Gradle Groovy, ou  ont tout simplement des limites. Même les
plugins de grands fournisseurs comme Spring ont des limites par rapport à leurs plugins Maven.  des fonctionnalités
limitées. Au final, je me retrouve avec un fichier de construction Gradle cool et court, que personne ne peut vraiment
entretenir,  pas même les développeurs qui l'ont écrit, et ils continuent d'aimer Gradle. Je connais peu de personnes
qui  peuvent sérieusement comprendre ou écrire des scripts Gradle.

### Redécouvrir la force de Maven - Utiliser les pouvoirs magiques de Maven

Voici mes fonctions préférées de Maven : Les plugins peuvent être lancés et configurés directement à partir de la ligne
de commande, sans avoir à les définir au préalable. n'ont pas besoin d'être installés. Plus, ils sont en grande partie
indépendants des autres configurations de plugins. | Exemple de commande | Description | Lien | |----------------------
-----------------|------------------------------------------------------------------------------------------------------
---------------------------------------------------------------|--------------------------------------------------------
------------------| | `mvn versions:use -latest-versions` | Mettre à jour les versions - qui a besoin de Dependabot ?
Oui, mes projets sont mis à jour sans problème à la dernière version depuis des années, sans demandes de fusion
ennuyeuses | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html | | `mvn versions:set
-DnewVersion=1.0.0` | Définir la version du projet...
| https://www.mojohaus.org/versions/versions-maven-plugin/index.html | | `mvn license:add-third-party` | Lister les
dépendances et afficher leurs licences (peut même échouer pour les licences exclues) | https://www.mojohaus.org/license-
maven-plugin/index.html | Cette liste pourrait continuer indéfiniment. Cela me rappelle en quelque sorte les étapes du
workflow GitHub. ![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)

### Tu n'aimes pas le XML ?

Pas de problème ! Il suffit d'écrire ton fichier de construction en `ruby`, `groovy`, `scala`, `yaml`, `atom` ou `Java`.
L'extension Polygot Extension (https://github.com/takari/polyglot-maven) le rend possible. Pour essayer il suffit
d'exécuter `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` et en quelques
millisecondes, ton fichier de construction est traduit. Dommage qu'il n'y ait pas de traducteur fiable Maven <> Gradle
existe :( Oui, les fichiers de construction Maven sont gros, mais aussi très faciles à comprendre. Les retouches ou le
débogage se font en un clin d'œil. sont faits.

### L'âge n'est qu'un chiffre - Stabilité et évolution de Maven

Certes, Maven existe depuis un certain temps déjà et son esthétique ne correspond peut-être pas aux standards actuels.
Cependant, la longévité de Maven lui a permis de s'adapter et d'évoluer. Maven fonctionne indépendamment de votre
projet. Les fichiers de construction peuvent être facilement réutilisés. Les plug-ins fonctionnent dans une sandbox et
sont indépendants les uns des autres, indépendamment de la version de Java ou de Maven. Cette conception favorise la
stabilité et la prédictibilité et permet de gérer facilement des processus de construction complexes sans conflits
inattendus. gérer des conflits.

### Fazit

De nos jours, l'environnement de développement est surchargé de tâches et de technologies pour les développeurs. A la
recherche de de simplicité et d'automatisation, Gradle est apparu comme un outil de construction moderne, mais a apporté
ses propres a apporté son lot de défis. Sans aucun doute, le concept de Gradle est bon ! Mais compte tenu de la
complexité et du temps temps investi dans les scripts de construction Gradle, on peut se demander s'il ne serait pas
plus simple d'étendre Maven d'étendre les fonctionnalités de Maven. Avec des plugins et des extensions, on pourrait à
tout moment rafraîchir et simplifier Maven. Une telle approche serait-elle plus Ne serait-il pas plus intéressant et
plus durable de continuer à développer Maven plutôt que de passer d'une technologie à l'autre ?

### Liens

* [Retour de Gradle à maven] (https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### Contact

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
