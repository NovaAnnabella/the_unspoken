---
title: "Niveles de Pruebas: Encontrando el Equilibrio Adecuado"
date: 2023-05-31
author: "Nova Annabella"
slug: test_level
tags: [ Testing, Software Testing, Test Levels, Mock Tests, Unit Tests, Integration Tests, Component Tests, Contract Tests, End-to-End Tests ]
categories: [ Technology, Software Development, Quality Assurance ]
description: "Encontrando el equilibrio adecuado al elegir los niveles de pruebas apropiados para el testing de software."
draft: false
images:
  - "/images/content/martin_fowler_testing.png"
card: "summary_large_image"
---

# Niveles de Pruebas: Encontrando el Equilibrio Correcto

[![test_level](/images/content/martin_fowler_testing.png)](https://martinfowler.com/articles/microservice-testing/)

### Introducción

El tema de las pruebas de software todavía parece ser un territorio desconocido con mucho margen para interpretación. La
pirámide de pruebas tradicional ha sido cuestionada y han surgido nuevas pirámides de pruebas. En mi opinión, no se
requiere una pirámide de pruebas, sino más bien una comprensión clara de lo que se debe probar. Las pruebas de nivel más
bajo tienden a tener menos significado. El enfoque principal debería estar en probar el comportamiento, asegurando que
la API o la interfaz de usuario funcionen según lo deseado. Se puede encontrar una visión general exhaustiva de los
posibles tipos de pruebas aquí: [Martinfowler Testing](https://martinfowler.com/articles/microservice-testing/).

### Nivel 1 - Pruebas Mock y Pruebas Unitarias

Propósito: Ejercitar las partes más pequeñas del software probable en la aplicación para determinar si se comportan como
se espera.

Las pruebas mock y las pruebas unitarias pueden ser contraproducentes y a menudo obstaculizan el proceso de desarrollo.
Estas pruebas a menudo están desconectadas del contexto y carecen de relevancia para la realidad. Suelen mantener
funciones innecesarias únicamente a través de las pruebas unitarias existentes. Una vez que se agregan mocks, se
convierte en una actividad autoengañosa. Los resultados esperados de las pruebas mock se limitan a lo que se definió en
el mock inicial. A los usuarios finales no les preocupan las funciones internas. Por ejemplo, en un escenario de inicio
de sesión `loginUser(nombre, contraseña, algoritmoSeguridad)`. Si la prueba unitaria verifica una verificación nula en
el parámetro `algoritmoSeguridad`, entonces se está probando demasiado, ya que los usuarios no pueden establecer el
parámetro `algoritmoSeguridad`.

### Nivel 2: Prueba de Integración

Propósito: Verificar las vías de comunicación y las interacciones entre los componentes para detectar defectos de
interfaz.

Las pruebas de integración ofrecen información valiosa sobre el rendimiento y la independencia de las diferentes partes
de la aplicación.
Con menos mocks, las pruebas se vuelven más comprensibles. Sin embargo, todavía carecen de contexto y existe el riesgo
de que las pruebas de integración sean simplemente pruebas unitarias disfrazadas con menos mocks.

### Nivel 3: Prueba de Componente

Propósito: Limitar el alcance del software evaluado a una parte del sistema bajo prueba, manipulando el sistema a través
de interfaces de código interno y utilizando duplicados de prueba para aislar el código evaluado de otros componentes.

Las pruebas de componente revelan una gran cantidad de información sobre la calidad y el rendimiento de la aplicación.
En lugar de mocks, finalmente se prueba la aplicación en sí. La diferencia entre las pruebas de componente y las pruebas
de extremo a extremo no es significativa. Con un entorno de pruebas adecuado, las fronteras entre ellos a menudo se
difuminan, lo que permite probar el comportamiento real en lugar de funciones aisladas y sin contexto. Sin embargo, la
creación de clases de prueba adicionales, como stubs de componentes, falsificaciones y mocks en el código de producción,
puede generar una carga de mantenimiento adicional.

### Nivel 4: Prueba de Contrato

Propósito: Verificar las interacciones en el límite de un servicio externo, asegurando que cumpla con el contrato
esperado por un servicio consumidor.

Las pruebas de contrato a menudo son similares a las pruebas de componente, y la diferencia entre ellas es mínima.
Algunos desarrolladores asocian estas pruebas con las pruebas de Pact, que funcionan básicamente como pruebas unitarias
con un servidor en el medio. El esfuerzo requerido para mantener estas pruebas puede no ser rentable. Por ejemplo, una
prueba de Pact puede evaluar la API REST `loginUser?name=aa&password=bb` y esperar una respuesta de esquema JSON que se
haya cargado previamente en el servidor de Pact. Este esquema es estático, lo que lo hace propenso a errores como
formatos de fecha incorrectos o zonas horarias incorrectas en la respuesta de la API. El impacto negativo puede ser
enorme.

### Nivel 5 - Pruebas de extremo a extremo, también conocidas como pruebas de caja negra

Propósito: Verificar que un sistema cumpla con los requisitos externos y logre sus objetivos, probando todo el sistema
de principio a fin.

Las pruebas de extremo a extremo son confiables y robustas. Una vez superado el obstáculo de configurar el entorno de
pruebas, el esfuerzo vale la pena. Estas pruebas simulan el comportamiento real, eliminando la necesidad de
simulaciones. Los errores se vuelven menos frecuentes y más fáciles de reproducir localmente. El tedioso proceso de
depuración y registro de producción se reduce considerablemente, al igual que los incidentes raros. Los desarrolladores
trabajan con datos de producción con menos frecuencia, lo que reduce la responsabilidad y aumenta el enfoque. Además,
las automatizaciones, como las actualizaciones automáticas de software, se vuelven más sencillas ya que el
comportamiento ya ha sido probado. ¡Hay beneficios adicionales! Una vez que las pruebas se escriben de manera
reutilizable, se pueden integrar en pruebas de carga, lo que proporciona una imagen integral de la funcionalidad. Estas
pruebas también se pueden ejecutar de forma continua en el entorno de producción, brindando información en tiempo real
sobre el estado de los diferentes flujos de trabajo. Si un subsistema, como un servicio REST externo, se desconecta, se
puede identificar de inmediato qué flujos de trabajo de usuario se ven afectados.

### Conclusion

En conclusión, las pruebas son un aspecto esencial del desarrollo de software y la elección de los niveles de prueba
depende de las necesidades y objetivos específicos de la aplicación. Si bien las pruebas simuladas y las pruebas
unitarias pueden ser limitadas en su efectividad, las pruebas de integración y las pruebas de componentes brindan
información valiosa sobre el comportamiento y rendimiento de la aplicación. Las pruebas de contrato ayudan a verificar
las interacciones con servicios externos, pero su distinción de las pruebas de componentes puede ser mínima. En última
instancia, las pruebas de extremo a extremo ofrecen el mayor nivel de confianza en la funcionalidad del sistema,
permitiendo pruebas exhaustivas de toda la aplicación. Al seleccionar los niveles de prueba adecuados y combinarlos de
manera efectiva, los desarrolladores pueden garantizar la calidad, confiabilidad y solidez de su software.

### Contacto

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
