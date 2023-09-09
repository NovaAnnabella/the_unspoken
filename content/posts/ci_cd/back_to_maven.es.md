---
title: "¿De vuelta a Maven?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "La esquiva búsqueda de simplicidad y un breve viaje para redescubrir el poder de Maven."
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# ¿De vuelta a Maven?

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

## 10 años de Gradle. En la búsqueda de alivio y un breve viaje para redescubrir la fortaleza de Maven.



### Maximización del potencial de los desarrolladores - Necesitamos más herramientas que ahorren tiempo

Los temas que a menudo se pasan por alto o rara vez se discuten me interesan. A menudo se utilizan tecnologías geniales,
pero casi nadie habla de los problemas asociados. El desarrollo se ha vuelto muy laborioso en la actualidad. Con
palabras de moda geniales como "Serverless", "Low Code", "IaC", "Big Data", "Cloud", "DevOps", "Lo construyes, lo
ejecutas" etc. los desarrolladores ya tienen suficientes tareas adicionales para manejar. Más tareas significan que
apenas hay expertos y siempre se descuida algo para el enfoque. Por lo tanto, las automatizaciones y el ahorro de tiempo
son mega importantes. "No me hagas pensar" y "Funciona fuera de la caja" ya son buenas características de calidad que
aún no puedo ver en Gradle. Para ser justos, Gradle no es la única herramienta moderna que nos da trabajo, en lugar de
facilitarlo.

### La búsqueda ilusoria de simplicidad y automatización

Desde SOAP, tengo una aversión profunda hacia las configuraciones basadas en XML. Con Gradle, esperaba que escribir
scripts de enlace sería un juego de niños. Desafortunadamente, mis esperanzas y mi motivación disminuyeron cada vez más.
Gradle busca flexibilidad y sacrifica automatización y calidad. Las desarrolladoras y los desarrolladores siguen
ciegamente la tendencia sin considerar los efectos en la fiabilidad del software. Para mantener los scripts de
construcción de Gradle simples y de bajo mantenimiento, se necesita una fuerte disciplina. Tal disciplina es rara
encontrar en el código fuente y por lo tanto es aún más rara en los scripts de construcción.

### Traducciones y soluciones alternativas - Cuando los scripts de construcción se convierten en un desafío

Gradle trabaja en segundo plano de manera bastante similar a Maven. Por lo tanto, son necesarias algunas traducciones.
Características como el Catálogo de dependencias, el Plugin de lanzamiento de Maven, el Dependabot y muchos más son en
realidad soluciones alternativas para funciones básicas que Maven ya trae incorporadas. Con la flexibilidad de Gradle, a
menudo surgen configuraciones de construcción complejas, que son difíciles de mantener. Los plugins de Gradle suelen
tener problemas de compatibilidad, límites o desarrollos limitados. Estos problemas surgen debido a la naturaleza en
constante evolución del ecosistema de Gradle, la diversidad de entornos en los que se usa Gradle y el esfuerzo de
implementación y mantenimiento específico para cada plugin. Todo está interconectado.

### El efecto dominó de Gradle - Un escenario de pesadilla en el mundo real

He visto muchos microservicios que solo tenían unos pocos años y ya no eran mantenibles debido a Gradle.
Es importante mencionar que esta no es la primera vez que veo algo así y no, no fueron
Desarrolladores junior.

Mi **tarea era realizar una actualización de Spring Boot 2.x a 2.7**. Spoiler: ¡Me di por vencido después de un año! 
Los problemas en resumen:

* El archivo de compilación Gradle requiere -> Degradar mi versión local de Java a 11 (WTF) (Normalmente Java
  es retrocompatible - también hay herramientas de solución alternativas como SdkMan...)
* La actualización de Spring Boot requiere -> Actualización de Gradle (WTF)
* La actualización de Gradle requiere -> Actualización de plugin
* La actualización del plugin requiere -> Actualización de Groovy (WTF)
* La actualización de Groovy requiere -> Actualizaciones de marco de pruebas y pruebas (WTF)
* La actualización de marco de pruebas requiere -> Actualizaciones de dependencias
* \[...]
  Además, algunos plugins no funcionan con versiones más nuevas de Gradle, algunos ya no están en
  desarrollo, son incompatibles con otros plugins, solo funcionan con Gradle KTS, no con Gradle Groovy, o simplemente
  tienen límites. Incluso los plugins de grandes proveedores como Spring tienen funcionalidad limitada en comparación con sus plugins de Maven.
  Al final, tengo un archivo cool de construcción de Gradle, que nadie puede mantener correctamente,
  ni siquiera los desarrolladores que lo escribieron, y todavía aman a Gradle. Solo conozco a unos pocos que
  toman en serio la escritura o el entendimiento de los scripts de Gradle.

### El redescubrimiento de la fuerza de Maven - Utilizar los poderes mágicos de Maven

Aquí están mis funciones favoritas de Maven:
Los complementos se pueden iniciar y configurar directamente desde la línea de comandos, sin tener que definirlos previamente. Además, son en gran medida independientes de otras configuraciones de complementos.

| Ejemplo de comando                       | Descripción                                                                                                                                                      | Enlace                                                                    | 
|------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| `mvn versions:use -latest-versions`      | Actualización de versiones - ¿quién necesita Dependabot? Sí, mis proyectos se han actualizado sin problemas a la última versión años, sin molestas solicitudes de fusión |https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0`    | Establecer la versión del proyecto...                                                                                                                            | https://www.mojohaus.org/versions/versions-maven-plugin/index.html       |
| `mvn license:add-third-party`            | Listar dependencias y mostrar sus licencias (incluso puede fallar en licencias excluidas)                                                                       | https://www.mojohaus.org/license-maven-plugin/index.html                 | 

Esta lista podría seguir y seguir. De alguna manera me recuerda a los pasos del flujo de trabajo de GitHub.

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)


### ¿No te gusta XML?

¡No hay problema! Simplemente escribe tu archivo de construcción en `ruby`, `groovy`, `scala`, `yaml`, `atom` o `Java`. La
Extensión Polyglot (https://github.com/takari/polyglot-maven) lo hace posible. Para probarlo,
simplemente ejecuta `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` y en
pocos milisegundos, tu archivo de construcción será traducido. Lástima que no haya un traductor Maven <> Gradle
fiable :(
Sí, los archivos de construcción de Maven son grandes, pero también muy fáciles de entender. Las mejoras o la depuración se
pueden hacer en un instante.

### La edad es solo un número - Estabilidad y evolución de Mavens

Admitido, Maven ha existido por un buen tiempo y su estética puede que no cumpla con los estándares de hoy. Sin embargo,
la longevidad de Maven le ha permitido adaptarse y seguir desarrollándose. Maven trabaja independientemente de tu
proyecto. Los archivos de compilación pueden ser reutilizados fácilmente. Los plugins funcionan en un sandbox y son
independientes entre sí y de la versión de Java o Maven. Este diseño promueve la estabilidad y previsibilidad y hace que
sea fácil manejar procesos de construcción complejos sin conflictos inesperados.

### Conclusión

Hoy en día, el entorno de desarrollo está sobrecargado con muchas tareas y tecnologías para los desarrolladores. En la
búsqueda de simplicidad y automatización, Gradle ha surgido como una herramienta de construcción moderna, pero ha traído
sus propios desafíos. Sin duda, ¡el concepto de Gradle es bueno! Pero dada la complejidad y el tiempo invertido en los
scripts de compilación de Gradle, surge la pregunta de si no sería más fácil extender Maven. Con los plugins y
extensiones, Maven podría ser revitalizado y simplificado en cualquier momento. ¿No sería mucho más emocionante y
también más sostenible seguir desarrollándose en lugar de saltar de una tecnología a otra?

### Enlaces

* [Regresando de Gradle a maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### Contacto

[Problemas de GitHub](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
