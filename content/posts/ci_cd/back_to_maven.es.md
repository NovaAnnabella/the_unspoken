---
title: "¿Volver a Maven?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "La búsqueda de simplicidad difícil de atrapar y un breve viaje para redescubrir el poder de Maven."
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# ¿Volver a Maven?

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)
``` 

Traducción:

```
[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/regreso-de-gradle-a-maven/)


```

## 10 años de Gradle. En busca de alivio y un breve viaje para redescubrir la fortaleza de Maven.

No hay texto que traducir ya que el contenido está vacío.

### Maximización del potencial de los desarrolladores - Necesitamos más herramientas que ahorren tiempo.

Los temas que a menudo se pasan por alto o se discuten raramente me interesan. A menudo hay tecnologías geniales en uso,
pero casi nadie habla de los problemas asociados con ellas. El desarrollo se ha vuelto muy exigente en estos días. Con
los geniales términos de moda como "sin servidor", "código bajo", "IaC", "Big Data", "nube", "DevOps", "Tú lo
construyes, tú lo ejecutas" etc., ya hay más que suficientes tareas adicionales para los desarrolladores. Más tareas
significan que ya hay pocas expertos y siempre se descuida algo en foco. Por lo tanto, la automatización y el ahorro de
tiempo son mega importantes. "No me hagas pensar" y "Funciona ​​de manera sorprendente" son ya buenas características de
calidad, que no puedo encontrar en Gradle. Para ser justos, Gradle no es la única herramienta moderna que nos hace
trabajar en lugar de facilitarla.

### La búsqueda ilusoria de simplicidad y automatización

Desde SOAP, tengo una profunda aversión a las configuraciones basadas en XML. Con Gradle, esperaba que escribir scripts
de unión sería pan comido. Desafortunadamente, mis esperanzas y motivación disminuyeron cada vez más. Gradle busca
flexibilidad a expensas de la automatización y calidad. Los desarrolladores siguen la tendencia ciegamente, sin
considerar las consecuencias para la confiabilidad del software. Para mantener los scripts de compilación de Gradle
simples y de fácil mantenimiento, se requiere una fuerte disciplina. Tal disciplina es rara en el código fuente y por lo
tanto aún más rara en los scripts de compilación.

### Traducciones y soluciones alternativas - Si los scripts de construcción se convierten en un desafío

Gradle no trabaja mucho diferente en segundo plano que Maven. Por lo tanto, se necesitan algunas traducciones. Funciones
como el Catálogo de Dependencias, el Plugin de Liberación de Maven, Dependabot y muchos más son en realidad soluciones
alternativas para características fundamentales que Maven ya incluye. Con la flexibilidad de Gradle a menudo surgen
configuraciones de construcción complejas que son difíciles de mantener. Los complementos de Gradle a menudo tienen
problemas de compatibilidad, límites o limitaciones de desarrollo. Estos problemas surgen debido a la naturaleza en
evolución del ecosistema de Gradle, a la diversidad de los entornos en los que se utiliza Gradle y al trabajo de
implementación y mantenimiento específico de cada complemento. Todo está conectado.

### El efecto de dominó de Gradle - Un escenario de pesadilla en el mundo real

He visto muchos microservicios que tenían sólo unos pocos años de antigüedad y que ya no eran mantenibles debido a Gradle. Es importante mencionar que esto no es la primera vez que veo algo así, y no, no eran desarrolladores junior.

Mi **tarea era actualizar Spring Boot 2.x a la versión 2.7**. Spoiler: ¡Después de un año, me rendí! Los problemas en resumen:

* El archivo de construcción de Gradle requiere -> Downgrade de mi versión local de Java a 11 (WTF) (normalmente, Java es compatible hacia atrás - también hay herramientas de trabajo de solución de problemas aquí como SdkMan...)
* La actualización de Spring Boot requiere -> Actualización de Gradle (WTF)
* La actualización de Gradle requiere -> Actualización de plugin
* La actualización de plugin requiere -> Actualización de Groovy (WTF)
* La actualización de Groovy requiere -> Actualización de marco de prueba y actualizaciones de prueba (WTF)
* La actualización de marco de prueba requiere -> Actualizaciones de dependencia
* \[...\]
  Además, algunos plugins no funcionan con versiones más nuevas de Gradle, algunos no se siguen desarrollando, son incompatibles con otros plugins, funcionan sólo con Gradle KTS, no con Gradle Groovy, o simplemente tienen límites. Incluso los plugins de grandes proveedores como Spring tienen funcionalidades limitadas en comparación con sus plugins de Maven. Al final, tengo un archivo de construcción de Gradle transparente y corto, que nadie puede mantener correctamente, ni siquiera los desarrolladores que lo escribieron, y todavía les encanta Gradle. Conozco a muy pocos que entienden y pueden escribir scripts de Gradle realmente.

### El redescubrimiento de la fuerza de Maven - Aprovechando los poderes mágicos de Maven

Aquí están mis funciones favoritas de Maven:
Los complementos se pueden iniciar y configurar directamente desde la línea de comandos sin necesidad de definirlos antes.
Además, son en gran medida independientes de otras configuraciones de complementos. 

| Ejemplo de comando                        | Descripción                                                                                                                                      | Enlace                                                                  |
|-------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| `mvn versions:use -latest-versions`       | Actualización de versiones - ¿quién necesita Dependabot? Sí, mis proyectos se han actualizado sin problemas durante años a la última versión, sin molestas solicitudes de merge.                     | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0`     | Establecer la versión del proyecto...                                                                                                           | https://www.mojohaus.org/versions/versions-maven-plugin/index.html       |
| `mvn license:add-third-party`             | Enumera las dependencias y muestra sus licencias (incluso puede fallar en las licencias excluidas)                                             | https://www.mojohaus.org/license-maven-plugin/index.html                 |

Esta lista podría seguir eternamente. Me recuerda un poco a los pasos del flujo de trabajo de GitHub.

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)

### ¿No te gusta el XML?

¡No hay problema! Simplemente escribe tu archivo de construcción en `ruby`, `groovy`, `scala`, `yaml`, `atom` o `Java`. La extensión Polygot (https://github.com/takari/polyglot-maven) lo hace posible. Para probarlo, simplemente ejecuta `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` y en pocos milisegundos tu archivo de construcción estará traducido. Es una lástima que no exista un traductor Maven <> Gradle confiable :(. Sí, los archivo de construcción de Maven son grandes, pero también son muy fáciles de entender. Las correcciones o la depuración se realizan en un abrir y cerrar de ojos.

### La edad sólo es un número - Estabilidad y evolución de los Mavens

De hecho, Maven ha existido por un tiempo considerable y su estética quizás no se ajuste a los estándares actuales. Sin
embargo, la longevidad de Maven ha permitido que se adapte y evolucione. Maven trabaja de manera independiente a su
proyecto. Los archivos de construcción pueden reutilizarse fácilmente. Los complementos se ejecutan en un entorno
protegido y son independientes entre sí y de la versión de Java o de Maven. Este diseño fomenta la estabilidad y
previsibilidad, lo que facilita la gestión de procesos de construcción complejos sin conflictos inesperados.

### Conclusión

Hoy en día, el entorno de desarrollo está sobrecargado con muchas tareas y tecnologías para los desarrolladores. En
busca de simplicidad y automatización, Gradle ha surgido como una herramienta de construcción moderna, pero ha traído
sus propios desafíos. ¡Sin duda, el concepto de Gradle es bueno! Pero dado la complejidad y el tiempo invertido en los
scripts de construcción de Gradle, surge la pregunta de si no sería más fácil ampliar Maven. Con plugins y extensiones,
Maven podría ser actualizado y simplificado en cualquier momento. ¿No sería más emocionante y sostenible continuar su
desarrollo en lugar de saltar de una tecnología a otra?

### Enlaces

* [Regresar de Gradle a Maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### Contacto

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose). 

(No hay cambios en el formato o contenido del texto original)
