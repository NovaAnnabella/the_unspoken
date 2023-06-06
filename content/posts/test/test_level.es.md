---
title: "Niveles de prueba: Encontrar el equilibrio adecuado"
date: 2023-05-31
author: "Nova Annabella"
slug: test_level
tags: [ Testing, Software Testing, Test Levels, Mock Tests, Unit Tests, Integration Tests, Component Tests, Contract Tests, End-to-End Tests ]
categories: [ Technology, Software Development, Quality Assurance ]
description: "Encontrar el equilibrio adecuado al seleccionar los niveles de prueba apropiados para las pruebas de software"
draft: false
images:
  - "/images/content/martin_fowler_testing.png"
card: "summary_large_image"
---


# Niveles de prueba: Encontrar el equilibrio adecuado

[![testebenen](/images/content/martin_fowler_testing.png)](https://martinfowler.com/articles/microservice-testing/)

### Introducción

El tema de las pruebas sigue pareciendo un territorio inexplorado con mucho margen para la interpretación. La pirámide y
han surgido nuevas pirámides de pruebas. En mi opinión, no es necesaria una pirámide de pruebas, sino una comprensión
clara de lo que hay que probar. Las pruebas de los niveles inferiores suelen ser menos significativas. Hay que centrarse
sobre todo en probar el comportamiento para garantizar que la API o la interfaz de usuario funcionan como se desea. Aquí
encontrará una descripción exhaustiva de los posibles tipos de pruebas: [Martinfowler
Testing](https://martinfowler.com/articles/microservice-testing/).

### Nivel 1 - Pruebas simuladas y pruebas unitarias

Objetivo: Ejercitar las partes de software comprobables más pequeñas de la aplicación para ver si funcionan como se
espera. trabajo. Las pruebas simuladas y las pruebas unitarias pueden ser contraproducentes y a menudo entorpecen el
proceso de desarrollo. Estas pruebas suelen estar desvinculadas del contexto y tienen poca relación con la realidad. A
menudo sólo sirven para mantener funciones innecesarias a través de pruebas unitarias existentes. pruebas unitarias
existentes. Una vez que se añaden los mocks, se convierte en un ejercicio contraproducente. Los resultados de las
pruebas simuladas se limitan a lo definido en la prueba original. Los usuarios finales no están interesados en las
funciones internas. Por ejemplo, en un escenario de login `loginUser(name, password, securityAlgorithm)`. Si la prueba
unitaria hace una comprobación nula en el parámetro `securityAlgorithm`, se realizan demasiadas pruebas porque los
usuarios no pueden establecer el parámetro `securityAlgorithm`. establecer el parámetro `securityAlgorithm`.

### Nivel 2 - Prueba de integración

Finalidad: Comprobar las vías de comunicación y las interacciones entre componentes para detectar defectos de interfaz.
Las pruebas de integración proporcionan información valiosa sobre el rendimiento y la independencia de las distintas
partes de la aplicación. aplicación. Con menos mocks, las pruebas resultan más comprensibles. Sin embargo, siguen
careciendo de contexto, y existe el riesgo de que peligro de que las pruebas de integración sean simplemente pruebas
unitarias disfrazadas con menos mocks.

### Nivel 3 - Prueba de componentes

Finalidad: limitar el alcance del software sometido a prueba a una parte del sistema sometido a prueba, manipular el
sistema sistema mediante interfaces de código internas y el uso de dobles de prueba para aislar el código sometido a
prueba de otros componentes. componentes. Las pruebas de componentes proporcionan mucha información sobre la calidad y
el rendimiento de la aplicación. En lugar de mocks se prueba finalmente la aplicación. La frontera entre la prueba de
componentes y la prueba de extremo a extremo no es significativa. Con un buen entorno de pruebas, los límites entre
ambas suelen difuminarse, de modo que se prueban comportamientos reales en lugar de funciones aisladas y
descontextualizadas. comportamiento real en lugar de funciones aisladas y sin contexto. Sin embargo, la creación de Sin
embargo, la creación de clases de prueba adicionales como stubs de componentes, fakes y mocks en el código de producción
puede añadir sobrecarga de mantenimiento.

### Nivel 4 - Prueba de contrato

La finalidad de este bloque de código es comprobar las interacciones en el límite de un servicio externo y garantizar
que cumple los requisitos contractuales de un servicio consumidor. Las pruebas de contrato suelen parecerse a las
pruebas unitarias, y la diferencia entre ellas es mínima. Algunos desarrolladores asocian estas pruebas con las pruebas
Pact, que actúan esencialmente como pruebas unitarias con un servidor de por medio. El esfuerzo de Sin embargo, el
esfuerzo de mantener estas pruebas puede no merecer la pena. Por ejemplo, una prueba Pact podría utilizar la API REST
REST API `loginUser?name=aa&password=bb)` y esperar una respuesta de esquema JSON que se haya cargado previamente en el
servidor Pact. servidor. Este esquema es estático y propenso a errores como formatos de fecha o zonas horarias
incorrectos en la respuesta de la API. respuesta de la API. Los efectos negativos pueden ser enormes.

### Nivel 5 - Pruebas de extremo a extremo (también llamadas pruebas de caja negra)

Finalidad: Verificar que un sistema cumple los requisitos externos y alcanza sus objetivos probando todo el sistema de
principio a fin. de principio a fin. Las pruebas de principio a fin son fiables y sólidas. Una vez superados los
obstáculos de la creación del entorno de pruebas, el esfuerzo merece la pena. esfuerzo merece la pena. Estas pruebas
simulan el comportamiento real y eliminan la necesidad de mocks. Los errores son menos frecuentes y son más fáciles de
reproducir localmente. Se evitan en gran medida las laboriosas tareas de depuración y registro en producción, así como
los incidentes poco frecuentes. se evitan en gran medida, al igual que los incidentes poco frecuentes. Los
desarrolladores trabajan menos a menudo, si es que lo hacen, con datos de producción, lo que reduce la responsabilidad y
aumenta la concentración. Además, automatizaciones como las actualizaciones automáticas de software facilitan la
implementación, ya que el comportamiento ya se ha probado. Hay otras ventajas. Una vez en las pruebas están escritas de
forma reutilizable, pueden integrarse en pruebas de carga para obtener una completa de la funcionalidad. Estas pruebas
también pueden ejecutarse continuamente en el entorno de producción y proporcionar información en tiempo real sobre el
estado de varios flujos de trabajo. Cuando un subsistema, como servicio REST, por ejemplo, se desconecta, es posible
identificar inmediatamente qué flujos de trabajo de usuario se ven afectados. se ven afectados.

### Fazit

En resumen, las pruebas son un aspecto esencial del desarrollo de software, y la elección de los niveles de prueba
depende de los requisitos y objetivos específicos de la aplicación. Mientras que las pruebas simuladas y las pruebas
unitarias pueden tener una eficacia limitada, las pruebas de integración y eficacia, las pruebas de integración y las
pruebas unitarias proporcionan información valiosa sobre el comportamiento y el rendimiento de la aplicación.
rendimiento de la aplicación. Las pruebas de contrato ayudan a verificar las interacciones con servicios externos, pero
su diferenciación con las pruebas unitarias puede ser mínima. En última instancia, las pruebas de extremo a extremo
proporcionan el máximo nivel de confianza en la funcionalidad del sistema y permiten realizar pruebas exhaustivas. la
funcionalidad del sistema y permiten realizar pruebas exhaustivas de toda la aplicación. Seleccionando los niveles de
niveles de prueba adecuados y combinándolos eficazmente, los desarrolladores pueden garantizar la calidad, fiabilidad y
robustez de su software.

### Contacto

[Problemas en GitHub](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
