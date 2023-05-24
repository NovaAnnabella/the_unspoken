---
title: "¿De vuelta a Maven?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "La búsqueda elusiva de la simplicidad y un breve viaje redescubriendo el poder de Maven"
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---

# ¿De vuelta a Maven?

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

## 10 años de Gradle. En busca de la simplicidad y un breve viaje redescubriendo el poder de Maven.

### Maximizando el potencial de los desarrolladores

#### Necesitamos herramientas que ahorren tiempo

Me interesan los temas que a menudo pasan desapercibidos o rara vez se discuten. A menudo, se utilizan tecnologías
geniales, pero casi nadie habla de los problemas asociados con ellas.
El desarrollo se ha vuelto muy complicado en estos días.
Con palabras de moda como "Serverless", "Low Code", "IaC", "Big Data", "Cloud", "DevOps", "You Build it You run it",
los desarrolladores ya tienen suficientes tareas adicionales para manejar. Más tareas significan que hay muy pocos
expertos y siempre se descuida algo en el enfoque. Por lo tanto, la automatización y el ahorro de tiempo son muy
importantes. "No me hagas pensar" y "Funciona de inmediato" son buenos indicadores de calidad que aún no veo en Gradle.
Para ser justos, Gradle no es la única herramienta moderna que nos causa trabajo en lugar de facilitarlo.

### La ilusoria búsqueda de la simplicidad y la automatización

Desde SOAP, tengo un fuerte disgusto por las configuraciones basadas en XML. Con Gradle, tenía la esperanza de que
escribir scripts de construcción fuera pan comido. Desafortunadamente, mis esperanzas y mi motivación se redujeron cada
vez más. Gradle busca la flexibilidad y sacrifica la automatización y la calidad. Los desarrolladores siguen ciegamente
la tendencia sin considerar las repercusiones en la confiabilidad del software. Para mantener los scripts de
construcción
de Gradle simples y fáciles de mantener, se requiere una gran disciplina. Tal disciplina ya es rara en el código fuente,
y por lo tanto, es aún más rara en los scripts de construcción.

### Traducciones y soluciones alternativas

#### Cuando los scripts de construcción se convierten en un desafío

Gradle no funciona de manera muy diferente a Maven en el fondo. Por lo tanto, se requieren algunas traducciones.
Características como Dependency Catalog, Maven Release Plugin, Dependabot y muchos otros son en realidad soluciones
alternativas para funciones básicas que Maven ya proporciona. Con la flexibilidad de Gradle, a menudo se crean
configuraciones de construcción complejas que son difíciles de mantener.
Los plugins de Gradle a menudo tienen problemas de compatibilidad, límites o desarrollo limitado. Estos problemas surgen
debido a la naturaleza en evolución del ecosistema de Gradle, la diversidad de entornos en los que se utiliza Gradle y
el esfuerzo específico de implementación y mantenimiento requerido para cada plugin. Todo está interconectado.

### El efecto dominó de Gradle

#### Un escenario de pesadilla en el mundo real

He visto muchos microservicios que tenían solo unos pocos años y ya no eran mantenibles debido a Gradle. Es importante
mencionar que esto no es la primera vez que veo algo así, y no, no eran desarrolladores junior.

Mi **tarea era actualizar Spring Boot 2.5 a 2.7**. ¡Spoiler: Me rendí después de un año! Los problemas resumidos
brevemente fueron:

* El archivo de construcción de Gradle requería -> Retroceder mi versión local de Java a la versión 11 (WTF) (
  normalmente, Java es compatible hacia atrás, pero aquí nuevamente, hay herramientas alternativas como SdkMan...)
* La actualización de Spring Boot requería -> Actualización de Gradle (WTF)
* La actualización de Gradle requería -> Actualización de plugins
* La actualización de plugins requería -> Actualización de Groovy (WTF)
* La actualización de Groovy requería -> Actualización de frameworks y pruebas (WTF)
* La actualización de frameworks de prueba requería -> Actualización de dependencias
* [...]
  Además, algunos plugins no funcionan con versiones más recientes de Gradle, algunos ya no se desarrollan, son
  incompatibles con otros plugins, solo funcionan con Gradle KTS y no con Gradle Groovy, o simplemente tienen límites.
  Incluso los plugins de grandes proveedores como Spring tienen funcionalidades limitadas en comparación con sus plugins
  de Maven. Al final, tengo un archivo de construcción de Gradle genial y conciso que nadie puede mantener
  correctamente, ni siquiera los desarrolladores que lo escribieron, y todavía aman Gradle. Solo conozco a unos pocos
  que realmente comprenden y pueden escribir scripts de Gradle.

### Redescubriendo el poder de Maven

#### Aprovechando las habilidades mágicas de Maven

Aquí están mis características favoritas de Maven:
Los plugins se pueden ejecutar y configurar directamente desde la línea de comandos sin necesidad de definirlos
previamente. Además, son en gran medida independientes de otras configuraciones de plugins.

| Comando de ejemplo                    | Descripción                                                                                                                                                                                | Enlace                                                                   | 
|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `mvn versions:use -latest-versions`   | Actualizar las versiones: ¿quién necesita Dependabot? Sí, mis proyectos se han estado actualizando sin problemas a las últimas versiones durante años, sin molestas solicitudes de fusión. | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0` | Establecer la versión del proyecto...                                                                                                                                                      | https://www.mojohaus.org/versions/versions-maven-plugin/index.html       |
| `mvn license:add-third-party`         | Enumerar las dependencias y mostrar sus licencias (incluso puede fallar en las licencias excluidas)                                                                                        | https://www.mojohaus.org/license-maven-plugin/index.html                 | 

Esta lista podría continuar infinitamente. De alguna manera, me recuerda a los pasos de los flujos de trabajo de GitHub.

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)

### ¿No te gusta el XML?

¡No hay problema! Simplemente escribe tu archivo de construcción en `ruby`, `groovy`, `scala`, `yaml`, `atom` o `Java`.
La extensión Polygot (https://github.com/takari/polyglot-maven) lo hace posible. Para probarlo, simplemente
ejecuta `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` y en pocos
milisegundos tu archivo de construcción estará traducido. Es una lástima que no haya un traductor confiable entre Maven
y Gradle :(
Sí, los archivos de construcción de Maven son extensos, pero también son muy fáciles de entender. Las correcciones o
depuraciones se realizan rápidamente.

### La edad es solo un número

#### La estabilidad y evolución de Maven

Es cierto que Maven ha estado presente durante mucho tiempo y su estética puede no cumplir con los estándares actuales.
Sin embargo, la longevidad de Maven ha permitido su adaptación y evolución. Maven funciona de forma independiente a su
proyecto. Los archivos de construcción se pueden reutilizar fácilmente.
Los plugins se ejecutan en un entorno aislado y son independientes entre sí, así como independientes de la versión de
Java o Maven. Este diseño fomenta la estabilidad y la previsibilidad, y facilita la gestión de procesos de construcción
complejos sin conflictos inesperados.

### Conclusión

En la actualidad, el entorno de desarrollo está sobrecargado de tareas y tecnologías para los desarrolladores. En busca
de la simplicidad y la automatización, Gradle ha surgido como una herramienta de construcción moderna, pero ha traído
consigo sus propios desafíos. Sin duda, el concepto de Gradle es bueno. Sin embargo, dada la complejidad y el tiempo
invertido en los scripts de construcción de Gradle, surge la pregunta de si sería más sencillo extender Maven. Con
plugins y extensiones, se podría refrescar y simplificar Maven en cualquier momento. ¿No sería más emocionante y
sostenible seguir desarrollando una tecnología en lugar de saltar de una a otra?

### Enlaces

* [Moving Back from Gradle to Maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### Contacto

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
