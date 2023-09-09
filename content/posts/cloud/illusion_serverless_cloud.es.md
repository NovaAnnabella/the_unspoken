---
title: "Servidor sin servidor e ilusión en la nube"
date: 2023-05-24
author: "Nova Annabella"
slug: illusion_serverless_cloud
tags: [ Development, Serverless, Cloud, Microservices, Scalability, Architecture, Infrastructure ]
categories: [ Technology, Software, Cloud ]
description: "Desafíos y realidades de las funciones sin servidor en la nube. Valiosos conocimientos para empresas que están considerando una migración a la nube."
draft: false
images:
  - "/images/content/onprem_vs_cloud.png"
card: "summary_large_image"
---


# La Ilusión de Funciones Serverless en la Nube

![aws_costs_twitter_1](/images/content/onprem_vs_cloud.png)

### Introducción

Estoy decepcionado con la frecuencia con que el marketing supera al sentido común. Muchos gerentes se imponen
sobre sus propios expertos, los desarrolladores. Esto también se aplica a la migración a la nube. Spoiler: quien necesita ahorrar
dinero debería evitar la nube. Porque la nueva palabra de moda "Serverless" en la nube significa: Te ocupas del
software, nosotros nos ocupamos de la hardware. Sin embargo, quien tenga un administrador capaz, motivado y curioso, puede
operar por sí mismo Serverless (por ejemplo, [KNative](https://knative.dev)).

![aws_costs_twitter_1](/images/content/aws_costs_twitter_1.png)


### Funciones sin servidor vs Microservicios:



#### Microservicios

Un microservicio sin estado típico se ocupa de una función/dominio específico y se despliega en un entorno de
orquestación de contenedores. Este entorno se ocupa de la infraestructura, la seguridad, el firewall, registro,
métricas, secretos, red, backups y mucho más. Una gran ventaja es que un microservicio puede ser localmente probado con
pocos recursos integrados y es agnóstico a la nube/servidor (utilizable en cualquier lugar).

#### Funciones Sin Servidor

Una pequeña broma para empezar: Paradoja, pero cierto - las funciones sin servidor dependen mucho del entorno del servidor. :)
Una función sin servidor típica se encarga también de una sola función/dominio y se escribe sin marcos
en
código puro para ser más rápido que un microservicio (también un buen ejercicio para MicroServices). Una gran
ventaja es que las funciones sin servidor se escalan automáticamente. Sin embargo, cada función sin servidor requiere una
cantidad considerable de GlueCode para definir la infraestructura - Seguridad, cortafuegos, red, registro de operaciones, métricas,
secretos, caché, copias de seguridad y mucho más.
Por lo tanto, una simple función como copiar un archivo, incluyendo API, puede fácilmente abarcar 1500 líneas de código (incl. IaC).
Los costes de administración se desplazan de la administración al desarrollo en una proporción de 1:N (1 a Funciones sin servidor). El conocimiento y la implementación ya no están
agrupados y pueden volverse inestables rápidamente. Además, los costos de mantenimiento aumentan.
Las pruebas de integración reales también son raras o sólo están asociadas con un gran esfuerzo en Serverless.
En última instancia, la complejidad de las funciones sin servidor es significativamente mayor que la de un solo microservicio.
Una mayor complejidad también significa una menor mantenibilidad. Los nuevos miembros del equipo lo tienen más difícil y necesitan significativamente
más conocimiento previo.

### Serverless y la Nube en General

La mayoría de las tecnologías en la nube no están actualizadas. Por ejemplo, Node.js, Java, Python y otros
lenguajes o tecnologías a menudo no son fáciles de actualizar, en su mayoría solo espera.
También las tecnologías modernas y estándar como MongoDB, MySQL, Kafka, NATS, RabbitMQ, Redis, Prometheus, InfluxDB, Grafana,
Kibana, Elastic Search, etc. no están disponibles o son demasiado caras.
Sin estos servicios estándar, a menudo te encuentras en la Edad de Piedra virtual y usas soluciones obsoletas, por ejemplo,
Webhooks para la comunicación externa. Además, el margen de maniobra en temas como la regulación,
cumplimiento, protección de datos y seguridad de fallas es muy limitado.

Por lo tanto, la nube debe operarse de manera agnóstica, para poder cambiar rápidamente entre AWS, Azure, Google, On-Premise, etc. y
para poder comparar costos.
Los límites también suelen estar presentes en la nube, lo que lleva a soluciones creativas que a su vez aumentan la complejidad.
También las pruebas integradoras pueden resultar costosas, ya que a cada desarrollador le hace falta su propio entorno de desarrollo en la nube
dado que muchos servicios en la nube son difíciles o imposibles de probar localmente.
Pero incluso sin pruebas, la nube es cara. Mientras que en los sistemas locales principalmente
incurren costos de hardware, en la nube también tienes que pagar por el tráfico, algunos servicios estándar y a menudo incluso por la
doble imposición. Además, en la nube puedes perder fácilmente la visión general, porque no se trata de
facilidad de uso, sino de dinero. Los costos están tan ocultos que solo los notarás cuando sea demasiado
tarde.

Los fundamentos de la arquitectura y la infraestructura deben reinventarse en la nube y especialmente en el área de Serverless,
ya que la implementación depende en gran medida de las funciones disponibles.
Siempre que diseño la arquitectura, me surge la idea: "Esto también podría haber sido un solo servicio".

Para mí, Serverless es una idea interesante y es fácil de escalar, pero no reduce los costos. Por el
contrario, requiere mucho más conocimiento y tiempo en el desarrollo. Serverless o la nube requieren disciplina y
conocimiento previo.
Si no se tiene el conocimiento para los sistemas locales, no será más fácil con la nube.
¿Cómo se supone que los desarrolladores adquirirán además conocimientos de infraestructura?

Prefiero un clúster de Kubernetes bien administrado a la arquitectura en la nube.
Los empleados no escalan. Muchos desarrolladores no tienen disciplina al escribir código.
Desafortunadamente, esto es cierto para el 80 por ciento de los desarrolladores. Entonces, ¿cómo se supone que estos desarrolladores van a manejar la nube?

Es importante que las empresas comprendan a fondo los desafíos e impactos de la arquitectura sin servidor y la nube.
Esto requiere no solo conocimientos técnicos, sino también un enfoque estratégico. Una
migración imprudente a la nube puede llevar a la complejidad, costos más altos y sobrecargar a los desarrolladores.

En resumen, Serverless en la nube es un concepto prometedor que debe ser considerado cuidadosamente.
Los costos, la complejidad, la mantenibilidad y las habilidades del equipo de desarrollo deben
ser tomados en cuenta.
Cada empresa tiene diferentes requerimientos y prioridades. Deberías tomar una decisión informada sobre si
Serverless en la nube es la solución correcta o si existen enfoques alternativos como
por ejemplo, un buen clúster de Kubernetes es la mejor opción.

El uso exitoso de Serverless y Cloud Computing requiere una combinación de experiencia técnica,
planificación estratégica y una clara comprensión de los requisitos comerciales. Solo de esta manera puedes ver a través de la ilusión de Serverless
y tomar la decisión correcta para tu propio desarrollo de software.


### Conclusión

La introducción de funciones sin servidor en la nube promete flexibilidad, escalabilidad y alivio de los desarrolladores
de tareas de infraestructura. Sin embargo, no se debe ser cegado por esta ilusión. El cambio a la nube y el uso de
funciones sin servidor conlleva una serie de desafíos. Los desarrolladores deben aprender un nuevo "idioma" además del
desarrollo real y asumir más responsabilidad sin el apoyo correspondiente. La complejidad de las funciones sin servidor
es a menudo mayor que la de los microservicios, ya que los desarrolladores tienen que asumir muchas tareas adicionales
como la definición de infraestructura, seguridad y escalabilidad. Las pruebas integradas reales son difíciles y el
conocimiento previo y la experiencia para la operación son aún más importantes en la nube. La nube misma trae consigo
más desafíos. Muchas tecnologías en la nube no están actualizadas y el uso de servicios estándar modernos puede ser
costoso o incluso imposible. Los requisitos regulatorios, el cumplimiento y la protección de datos limitan el margen de
maniobra. Además, los costos en la nube pueden salirse fácilmente de control, y es fácil perder la supervisión de los
gastos. En general, es necesario sopesar cuidadosamente los pros y los contras de las funciones sin servidor y la nube.
Las empresas deben tener en cuenta sus requisitos específicos, el conocimiento existente en el equipo y los impactos a
largo plazo de una migración a la nube. Una decisión informada basada en un análisis exhaustivo es crucial para el éxito
y la rentabilidad del proyecto. En última instancia, corresponde a las empresas apoyar adecuadamente a sus
desarrolladores, estimar de manera realista los costos y la complejidad de la nube y considerar soluciones alternativas
como clusters Kubernetes bien gestionados. Con una estrategia clara y un entendimiento sólido de sus propias
necesidades, las empresas pueden aprovechar al máximo las ventajas de la nube y las funciones sin servidor y ver a
través de la ilusión.

### Contacto

[Problemas de GitHub](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
