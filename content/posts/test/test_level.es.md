---
title: "Niveles de prueba: Encontrar el equilibrio correcto"
date: 2023-05-31
author: "Nova Annabella"
slug: test_level
tags: [ Testing, Software Testing, Test Levels, Mock Tests, Unit Tests, Integration Tests, Component Tests, Contract Tests, End-to-End Tests ]
categories: [ Technology, Software Development, Quality Assurance ]
description: "Encontrar el equilibrio correcto al seleccionar los niveles de prueba adecuados para las pruebas de software"
draft: false
images:
  - "/images/content/martin_fowler_testing.png"
card: "summary_large_image"
---


# Niveles de prueba: Encontrar el equilibrio correcto

[![testebenen](/images/content/martin_fowler_testing.png)](https://martinfowler.com/articles/microservice-testing/)

### Introducción

El tema de las pruebas parece hasta hoy ser un territorio nuevo con mucho espacio para la interpretación. La tradicional
pirámide de pruebas ha sido cuestionada y han surgido nuevas pirámides de pruebas. En mi opinión, no se necesita
una pirámide de pruebas, sino una comprensión clara de lo que se debe probar. Las pruebas en niveles más bajos a menudo
son menos significativas. El foco debería estar principalmente en probar el comportamiento, para asegurar que la
API
o la interfaz de usuario funcione como se desea. Una visión general completa de los posibles tipos de pruebas se puede encontrar aquí:
[Martinfowler Testing](https://martinfowler.com/articles/microservice-testing/).


### Nivel 1 - Pruebas Simuladas y Pruebas Unitarias

Objetivo: Ejercitar las partes de software más pequeñas y comprobables en la aplicación para determinar si funcionan
como se esperaba. Las pruebas simuladas y las pruebas unitarias pueden ser contraproducentes y a menudo obstruyen el
proceso de desarrollo. Estas pruebas a menudo están desconectadas del contexto y tienen poco que ver con la realidad. A
menudo solo sirven para mantener funciones innecesarias sobre las pruebas unitarias existentes. Tan pronto como se
agregan simulacros, se convierte en un autoempleo. Los resultados esperados de las pruebas simuladas se limitan a lo que
se definió en el simulacro original. Los usuarios finales no están interesados en las funciones internas. Por ejemplo,
en un escenario de inicio de sesión `loginUser (name, password, securityAlgorithmus)`. Si la prueba unitaria realiza una
verificación nula en el parámetro `securityAlgorithm`, se está probando demasiado, ya que los usuarios no pueden
establecer el parámetro `securityAlgorithm`.

### Nivel 2 - Prueba de Integración

Objetivo: Verificación de los canales de comunicación e interacciones entre componentes para la detección de defectos
en la interfaz. Las pruebas de integración proporcionan información valiosa sobre la capacidad y la independencia de
diferentes partes de la aplicación. Con menos simulacros, las pruebas son más comprensibles. Sin embargo, todavía les
falta el contexto, y existe el peligro de que las pruebas de integración simplemente sean pruebas unitarias disfrazadas
con menos simulacros.

### Nivel 3 - Prueba de Componente

Propósito: Limitar el alcance del software probado a una parte del sistema a probar, manipulación del sistema a través
de las interfaces de código interno y uso de duplicados de prueba para aislar el código a probar de otras componentes.
Las pruebas de componentes aportan una gran cantidad de información sobre la calidad y capacidad del rendimiento de la
aplicación. En lugar de Mocks, finalmente estás probando tu aplicación. La frontera entre las pruebas de componentes y
las pruebas de extremo a extremo no es significativa. Con un buen entorno de prueba, las fronteras entre ellos a menudo
se desvanecen, lo que permite probar el comportamiento real en lugar de funciones aisladas y sin contexto. Sin embargo,
la creación de clases de prueba adicionales como los stubs de componentes, los falsos y los Mocks en el código de
producción puede conllevar un esfuerzo de mantenimiento adicional.

### Nivel 4 - Prueba de Contrato

El propósito de este bloque de código es verificar las interacciones en el límite de un servicio externo y asegurarse de
que cumple con los requisitos contractuales de un servicio de consumo. Las pruebas de contrato a menudo se parecen a
las pruebas de componentes, y la diferencia entre ellas es mínima. Algunos desarrolladores asocian estas pruebas con las
pruebas de Pact, que esencialmente actúan como pruebas unitarias con un servidor intermedio. El esfuerzo para mantener
estas pruebas podría, sin embargo, no ser rentable. Por ejemplo, una prueba de Pact podría probar la API REST
`loginUser?name=aa&password=bb)` y esperar una respuesta de esquema JSON que previamente se haya subido al servidor de
Pact. Este esquema es estático y susceptible a errores como formatos de fecha incorrectos o zonas horarias en la
respuesta de la API. Los efectos negativos pueden ser enormes.

### Nivel 5 - Pruebas de extremo a extremo (también llamadas pruebas de caja negra)

Propósito: Verificación de si un sistema cumple con los requerimientos externos y alcanza sus objetivos al probar todo
el sistema desde el principio hasta el final. Las pruebas de extremo a extremo son confiables y robustas. Una vez que
se superan los obstáculos de la configuración del entorno de prueba, el esfuerzo vale la pena. Estas pruebas simulan
comportamiento real y eliminan la necesidad de mocks. Los errores ocurren menos a menudo y son más fáciles de reproducir
localmente. El debugging laborioso y el registro en la producción se evitan en gran medida, así como los incidentes
raros. Los desarrolladores trabajan con menos frecuencia, si acaso, con datos de producción, lo que reduce la
responsabilidad y aumenta el enfoque. Además, automatizaciones como las actualizaciones automáticas de software
facilitan la ejecución, ya que el comportamiento ya ha sido probado. ¡Hay más beneficios! Una vez que las pruebas se
escriben en una forma reutilizable, pueden integrarse en las pruebas de carga para obtener una imagen completa de la
funcionalidad. Estas pruebas también pueden ejecutarse continuamente en el entorno de producción y ofrecer información
en tiempo real sobre el estado de diferentes flujos de trabajo. Si un subsistema, como por ejemplo un servicio REST
externo, se desconecta, se puede identificar inmediatamente qué flujos de trabajo de usuario están afectados.

### Conclusión

En resumen, las pruebas son un aspecto esencial del desarrollo de software, y la elección de los niveles de prueba
depende de los requisitos y objetivos específicos de la aplicación. Mientras que las pruebas de simulacro y las pruebas
unitarias pueden tener su eficacia limitada, las pruebas de integración y las pruebas de componentes ofrecen valiosas
perspectivas sobre el comportamiento y el rendimiento de la aplicación. Las pruebas de contrato ayudan a comprobar las
interacciones con los servicios externos, pero su diferenciación con las pruebas de componentes puede ser mínima.
Finalmente, las pruebas de extremo a extremo proporcionan el máximo nivel de confianza en la funcionalidad del sistema y
permiten pruebas exhaustivas de toda la aplicación. Mediante la selección de los niveles de prueba adecuados y su
combinación efectiva, los desarrolladores pueden garantizar la calidad, fiabilidad y robustez de su software.

### Contacto

[Problemas de GitHub](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
