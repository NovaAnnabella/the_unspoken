---
title: "¿Volver a Maven?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "La búsqueda escurridiza de la simplicidad y un breve viaje para redescubrir el poder de Maven."
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# ¿Volver a Maven?

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

## 10 años de Gradle: En busca de la simplicidad y un breve viaje para redescubrir la fortaleza de Maven.

No hay nada que traducir en este texto ya que está en blanco.

### Maximización del potencial de los desarrolladores - Necesitamos más herramientas que ahorren tiempo

Los temas que a menudo son pasados por alto o rara vez se discuten son de mi interés. A menudo hay tecnologías geniales
en uso, pero casi nadie habla de los problemas asociados con ellas. El desarrollo se ha vuelto muy complicado en estos
días. Con las geniales palabras de moda como "Serverless", "Low Code", "IaC", "Big Data", "Cloud", "DevOps", "You Build
it You run it", etc. los desarrolladores ya tienen más que suficientes tareas adicionales para manejar. Más tareas
significan que hay muy pocos expertos y que siempre algo se descuida en lo que se enfoca. Por eso, las automatizaciones
y ahorros de tiempo son extremadamente importantes. "No me hagas pensar" y "Funciona desde la caja" son ya buenas
cualidades de calidad que no puedo ver en Gradle todavía. Para ser justos, Gradle no es la única herramienta moderna que
nos causa trabajo en lugar de facilitarlo.

### La búsqueda ilusoria de simplicidad y automatización

Desde SOAP, tengo una aversión arraigada hacia las configuraciones basadas en XML. Con Gradle esperé que escribir
scripts de enlace fuera pan comido. Lamentablemente, mis esperanzas y motivación disminuyeron cada vez más. Gradle
persigue la flexibilidad a expensas de la automatización y calidad. Los desarrolladores siguen ciegamente la tendencia
sin tener en cuenta las consecuencias en la confiabilidad del software. Para mantener los scripts de construcción de
Gradle simples y fáciles de mantener, se necesita una fuerte disciplina. Esta disciplina es rara de encontrar incluso en
el código fuente y, por lo tanto, es aún más rara en los scripts de construcción.

### Traducciones y soluciones alternativas - Cuando los scripts de construcción se convierten en un desafío

Gradle trabaja en segundo plano no muy diferente de Maven. Por lo tanto, se necesitan algunas traducciones.
Características como el Catálogo de Dependencias, el Plugin de Lanzamiento de Maven, el Dependabot y muchos más son en
realidad soluciones alternativas para funciones básicas que Maven ya tiene. Con la flexibilidad de Gradle, a menudo se
crean configuraciones de compilación complejas que son difíciles de mantener. Los complementos de Gradle a menudo tienen
problemas de compatibilidad, limitaciones o limitaciones en el desarrollo. Estos problemas surgen debido a la naturaleza
en evolución del ecosistema de Gradle, la diversidad de entornos en los que se implementa Gradle y el esfuerzo
específico de implementación y mantenimiento para cada complemento. Todo está conectado.

### El efecto dominó de Gradle - Un escenario de pesadilla en el mundo real

He visto muchos microservicios que solo tenían unos pocos años y ya no eran mantenibles debido a Gradle. Es importante mencionar que no es la primera vez que he visto algo así y que no, no eran desarrolladores junior.

Mi **tarea fue realizar una actualización de Spring Boot 2.x a 2.7**. Spoiler: ¡Después de un año, me di por vencido! Los problemas resumidos son:

* El archivo de construcción de Gradle requiere -> Retroceso de mi versión local de Java a 11 (WTF) (Por lo general, Java es compatible hacia atrás - hay herramientas de solución alternativa como SdkMan...)
* La actualización de Spring Boot requiere -> Actualización de Gradle (WTF)
* La actualización de Gradle requiere -> Actualización de complementos
* La actualización de complementos requiere -> Actualización de Groovy (WTF)
* La actualización de Groovy requiere -> Actualizaciones del marco de pruebas y pruebas (WTF)
* La actualización del marco de pruebas requiere -> Actualizaciones de las dependencias
* \[...]
Además, algunos complementos no funcionan con versiones más recientes de Gradle, algunos ya no se desarrollan, son incompatibles con otros complementos, solo funcionan con Gradle KTS, no con Gradle Groovy, o tienen límites. Incluso los complementos de grandes proveedores como Spring tienen funcionalidades limitadas en comparación con sus complementos de Maven. Al final, tengo un archivo de construcción de Gradle fresco y corto que nadie puede mantener correctamente, ni siquiera los desarrolladores que lo escribieron, y aún les encanta Gradle. Conozco a muy pocos que realmente entienden o pueden escribir scripts de Gradle.

### Redescubriendo la fuerza de Maven - Aprovechando los poderes mágicos de Maven

Aquí están mis funciones favoritas de Maven: Los plugins pueden ser iniciados y configurados directamente desde la línea de comando sin necesidad de ser definidos previamente. Además, son en gran parte independientes de otras configuraciones de plugin.

| Comando de ejemplo                     | Descripción                                                                                                                                                          | Enlace                                                                   | 
|----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `mvn versions:use -latest-versions`    | Actualiza las versiones: ¿quién necesita Dependabot? Sí, mis proyectos se han actualizado sin problemas a la última versión durante años sin necesidad de molestas solicitudes de fusión. | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0`  | Establece la versión del proyecto...                                                                                                                                  | https://www.mojohaus.org/versions/versions-maven-plugin/index.html       |
| `mvn license:add-third-party`          | Lista las dependencias y muestra sus licencias (incluso puede fallar con licencias excluidas)                                                                         | https://www.mojohaus.org/license-maven-plugin/index.html                 | 

Esta lista podría continuar indefinidamente. De alguna manera me recuerda a los pasos de GitHub Workflow.

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)

### ¿No te gusta el XML?

¡No hay problema! Solo escribe tu archivo de construcción en `ruby`, `groovy`, `scala`, `yaml`, `atom` o `Java`. La extensión Polyglot (https://github.com/takari/polyglot-maven) lo hace posible. Para probarlo, simplemente ejecuta `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` y en pocos milisegundos se traducirá tu archivo de construcción. Es una lástima que no haya un traductor fiable de Maven a Gradle :( Los archivos de construcción de Maven son grandes pero también muy fáciles de entender. Las correcciones o la depuración se realizan en un instante.

### La edad es solo un número - la estabilidad y evolución de Mavens

A decir verdad, Maven ya tiene bastante tiempo y su estética quizás no cumpla con los estándares actuales. Sin embargo,
la durabilidad de Maven le ha permitido adaptarse y evolucionar. Maven trabaja de forma independiente a su proyecto. Los
archivos de construcción pueden ser fácilmente reutilizados. Los complementos se ejecutan en un sandbox y son
independientes entre sí y de la versión de Java o Maven. Este diseño fomenta la estabilidad y la predictibilidad, y
facilita la gestión de procesos de construcción complejos sin conflictos inesperados.

### Conclusión

En la actualidad, el entorno de desarrollo está sobrecargado con muchas tareas y tecnologías para los desarrolladores.
En busca de simplicidad y automatización, Gradle ha surgido como una herramienta moderna de compilación, pero ha traído
sus propios desafíos. Sin duda, ¡el concepto de Gradle es bueno! Pero debido a la complejidad y tiempo invertido en los
scripts de compilación de Gradle, surge la pregunta si no sería más fácil ampliar Maven. Con plugins y extensiones,
Maven podría actualizarse y simplificarse en cualquier momento. ¿No sería un desarrollo mucho más emocionante y
sostenible que saltar de una tecnología a otra?

### Enlaces

* [Volviendo de Gradle a maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### Contacto

[Problemas de GitHub](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).```
