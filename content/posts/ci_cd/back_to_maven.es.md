---
title: "¿De vuelta a Maven?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "La esquiva búsqueda de la simplicidad y un breve viaje para redescubrir el poder de Maven".
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---



# ¿Volver a Maven?

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

## 10 años de Gradle. En busca de alivio y un breve viaje para redescubrir el poder de Maven.



### Maximizar el potencial de los desarrolladores: necesitamos más herramientas que ahorren tiempo

Me interesan temas que a menudo se pasan por alto o de los que rara vez se habla. A menudo se utilizan tecnologías
geniales pero casi nadie habla de los problemas asociados a ellas. El desarrollo se ha vuelto muy costoso hoy en día.
Con palabras de moda como "serverless", "low code", "IaC", "big data", "cloud", "DevOps", "you build it you run it",
etc., los desarrolladores ya tienen suficiente. etc., los desarrolladores ya tienen más que suficientes tareas
adicionales con las que lidiar. Más tareas significa que apenas hay expertos y siempre se descuida algo para centrarse.
Por eso la automatización y el ahorro de tiempo son mega importantes. "No me hagas pensar" y "Funciona fuera de la caja"
ya son características de buena calidad que no veo en Gradle todavía. no veo todavía. Para ser justos, Gradle no es la
única herramienta moderna que nos hace el trabajo en vez de hacerlo más fácil.

### La ilusoria búsqueda de la simplicidad y la automatización

Desde SOAP, he tenido una arraigada aversión a las configuraciones basadas en XML. Con Gradle, esperaba que que escribir
scripts bind sería pan comido. Desafortunadamente, mis esperanzas y motivación disminuían disminuían cada vez. Gradle se
esfuerza por la flexibilidad y sacrifica la automatización y la calidad por ello. Los desarrolladores siguen ciegamente
la desarrolladores siguen ciegamente la tendencia sin tener en cuenta el impacto en la fiabilidad del software. Para
hacer Gradle Build scripts simples y de bajo mantenimiento requiere una fuerte disciplina. Tal disciplina ya es rara en
código fuente y por lo tanto es aún más rara en los scripts de construcción.

### Traducciones y soluciones - Cuando los scripts de compilación se convierten en un reto

Gradle no funciona de forma muy diferente en segundo plano que Maven. Por lo tanto, algunas traducciones son necesarias.
Características como el Dependency Catalog, el Maven Release Plugin, el Dependabot y muchos más son en realidad
soluciones para funciones básicas que Maven ya ofrece. Con la flexibilidad de Gradle a menudo vienen complejas
configuraciones de construcción, que son difíciles de mantener. Los plugins de Gradle a menudo tienen problemas de
compatibilidad, límites o avances limitados. Estos problemas surgen debido a la naturaleza evolutiva del ecosistema de
Gradle, la diversidad de entornos en los que Gradle se se utiliza, y el esfuerzo específico de implementación y
mantenimiento que requiere cada plugin. Todo está interconectado.

### El efecto dominó de Gradle - Un escenario de pesadilla en el mundo real

He visto muchos microservicios que tenían pocos años y ya no eran mantenibles debido a Gradle. debido a Gradle.
Importante mencionar que no es la primera vez que veo algo así, y no, no eran Junior Devs. Mi **tarea era realizar una
actualización de Spring Boot 2.x a 2.7**. Spoiler: Me rendí después de un año ¡Me rendí! Los problemas en breve: * El
archivo de construcción Gradle requiere -> Downgrade mi versión local de Java a 11 (WTF) (Normalmente Java es
compatible hacia abajo - de nuevo, hay herramientas de solución como SdkMan ...) * La actualización de Spring Boot
requiere -> Actualización de Gradle (WTF) * La actualización de Gradle requiere -> Plugin update * La actualización del
plugin requiere -> Actualización de Groovy (WTF) * La actualización de Groovy requiere -> Test framework y test updates
(WTF) * La actualización del marco de pruebas requiere -> Actualizaciones de dependencias. * \[...]  Además, algunos
plugins no funcionan con las nuevas versiones de Gradle, algunos ya no están desarrollados, algunos son incompatibles
con otras versiones de Gradle, algunos ya no están desarrollados, algunos son incompatibles con otras versiones de
Gradle.  son incompatibles con otros plugins, sólo funcionan con Gradle KTS, no con Gradle Groovy, o simplemente tienen
simplemente tienen límites. Incluso los plugins de grandes proveedores como Spring tienen una funcionalidad limitada en
comparación con sus plugins de Maven.  funcionalidad limitada. Termino con un archivo de compilación de Gradle genial y
corto que nadie puede realmente mantener,  ni siquiera los desarrolladores que lo escribieron, y aún así aman Gradle.
Conozco a muy pocas personas que  entienden los scripts de Gradle en serio los escriben.

### Rediscovering the Power of Maven - Aprovechar la magia de Maven

Estas son mis características favoritas de Maven: Los plugins pueden iniciarse y configurarse directamente desde la
línea de comandos sin necesidad de definirlos previamente. no necesitan ser definidos. Además, son en gran medida
independientes de otras configuraciones de plugins. | Ejemplo Comando Descripción Enlace |-----------------------------
----------|-------------------------------------------------------------------------------------------------------------
--------------------------------------------------------|---------------------------------------------------------------
-----------| | Actualizar versiones - ¿Quién necesita Dependabot? Sí, mis proyectos se han actualizado a la última
versión durante años sin ningún problema y sin molestas solicitudes de fusión |
https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html | | `mvn versions:set -DnewVersion=1.0.0` |
Establecer la versión del proyecto...
| https://www.mojohaus.org/versions/versions-maven-plugin/index.html | `mvn license:add-third-party` | Listar
dependencias y mostrar sus licencias (puede fallar incluso si las licencias están excluidas) |
https://www.mojohaus.org/license-maven-plugin/index.html | Esta lista podría ser interminable. Me recuerda un poco a
los pasos del flujo de trabajo de GitHub.
![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)

### ¿No te gusta XML?

No hay problema. Sólo tienes que escribir tu archivo de compilación en `ruby`, `groovy`, `scala`, `yaml`, `atom` o
`Java`. La extensión Polygot Extension (https://github.com/takari/polyglot-maven) lo hace posible. Para probarla
simplemente ejecute `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` y en
unos pocos milisegundos su construcción es milisegundos su archivo de construcción se traduce. Es una pena que no exista
un traductor Maven <> Gradle fiable. :( Sí, los archivos de construcción de Maven son grandes, pero también muy fáciles
de entender. Refinamientos o depuración se hacen en ningún momento. Hecho.

### Age is just a number - Maven's stability and evolution

Es cierto que Maven existe desde hace bastante tiempo y que su estética puede no responder a los estándares actuales.
Sin embargo, la longevidad de Maven le ha permitido adaptarse y evolucionar. Maven trabaja independientemente de su
proyecto. Los archivos de compilación se pueden reutilizar fácilmente. Los plugins se ejecutan en un sandbox y son
independientes entre sí e independientes de la versión de Java o Maven. Este diseño promueve la estabilidad y la
previsibilidad y hace que sea fácil de manejar complejos procesos de construcción sin conflictos inesperados.
inesperados.

### Fazit

Hoy en día, el entorno de desarrollo está sobrecargado de muchas tareas y tecnologías para los desarrolladores. En la
búsqueda de la simplicidad y la automatización, Gradle ha surgido como una herramienta de construcción moderna, pero ha
traído su propia desafíos. Sin duda, ¡el concepto de Gradle es bueno! Pero dada la complejidad y el tiempo invertido en
los scripts de construcción de Gradle, surge la pregunta de si no sería más sencillo extender Maven. extendido. Con
plugins y extensiones, Maven siempre podría actualizarse y simplificarse. ¿No sería desarrollo no sería mucho más
emocionante y también más sostenible que saltar de una tecnología a otra?

### Enlaces

* [Moving Back from Gradle to maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### Contacto

[Problemas en GitHub](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
