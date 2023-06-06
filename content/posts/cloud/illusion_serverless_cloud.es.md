---
title: "Ilusión sin servidor y en la nube"
date: 2023-05-24
author: "Nova Annabella"
slug: illusion_serverless_cloud
tags: [ Development, Serverless, Cloud, Microservices, Scalability, Architecture, Infrastructure ]
categories: [ Technology, Software, Cloud ]
description: "Retos y realidades de las capacidades sin servidor en la nube. Información valiosa para las empresas que se plantean migrar a la nube".
draft: false
images:
  - "/images/content/onprem_vs_cloud.png"
card: "summary_large_image"
---



# La ilusión de las funciones sin servidor en la nube

![aws_costs_twitter_1](/images/content/onprem_vs_cloud.png)

### Introducción

Me decepciona la frecuencia con que el marketing triunfa sobre el sentido común. Muchos directivos se anteponen por
encima de sus propios expertos: los desarrolladores. Esto también se aplica a la migración a la nube. Spoiler: Si
necesita ahorrar dinero necesita ahorrar dinero debe evitar la nube. Porque la nueva palabra de moda "sin servidor" en
la nube significa: Tú te encargas del software, nosotros del hardware. Usted se encarga del software, nosotros del
hardware. Sin embargo, si dispone de un administrador capaz, motivado e inquieto, puede también pueden operar ellos
mismos sin servidor (por ejemplo, [KNative](https://knative.dev)).
![aws_costs_twitter_1](/images/content/aws_costs_twitter_1.png)

### Serverless functions vs microservices:



#### Microservicios

Un microservicio sin estado típico se encarga de una función/dominio específico y se despliega en un entorno de
orquestación de contenedores. entorno de orquestación de contenedores. Este entorno se encarga de la infraestructura, la
seguridad, el cortafuegos registro, métricas, secretos, redes, copias de seguridad y mucho más. Una gran ventaja es que
un microservicio puede desplegarse localmente con pocos recursos recursos y es agnóstico a la nube/servidor (puede
desplegarse en cualquier lugar).

#### Funciones sin servidor

Una pequeña broma de antemano: Paradójico, pero cierto - las funciones serverless dependen en gran medida del entorno
del servidor. :) Una función serverless típica también se encarga de una sola función/dominio específico y está escrita
en código puro sin frameworks para ser más rápida que un microservicio. código para ser más rápida que un microservicio
(también es un buen ejercicio para los microservicios). Una gran ventaja es que las funciones Serverless escalan
automáticamente. Sin embargo, cada función serverless requiere una cantidad considerable de GlueCode para definir la
infraestructura - seguridad, firewall, red, logging, métricas secretos, almacenamiento en caché, copias de seguridad y
mucho más. Por lo tanto, una función simple como copiar un archivo incluyendo API puede implicar rápidamente 1500 líneas
de código (incl. IaC). pueden estar implicadas. Los costes de administración pasan de la administración al desarrollo en
una proporción de 1:N (1 a Serverless funciones). Por lo tanto, el conocimiento y la implementación ya no están y pueden
volverse rápidamente inestables. Además, aumentan los costes de mantenimiento. Las verdaderas pruebas integradoras
también son raras con serverless, o solo son posibles con un gran esfuerzo. En última instancia, la complejidad de las
funciones sin servidor es significativamente mayor que la de un único microservicio. Una mayor complejidad también
significa una menor capacidad de mantenimiento. Los nuevos miembros del equipo tienen más dificultades y necesitan
conocimientos previos.

### Serverless y la nube en general

La mayoría de las tecnologías de nube no están actualizadas. Por ejemplo, Node.js, Java, Python y otros lenguajes o
tecnologías son lenguajes o tecnologías no suelen ser fáciles de actualizar, normalmente sólo ayuda esperar. Incluso las
tecnologías modernas y estándar como MongoDB, MySQL, Kafka, NATS, RabbitMQ, Redis, Prometheus, InfluxDB, Grafana,
Kibana, Elastic Search, etc. no están disponibles o tienen un precio excesivo. Sin estos servicios estándar, a menudo se
está en la edad de piedra virtual y se utilizan soluciones obsoletas, por ejemplo webhooks para la comunicación externa.
Además, el margen de maniobra en cuestiones como la normativa la protección de datos y la seguridad contra fallos. Por
tanto, la nube debe gestionarse de forma agnóstica para poder cambiar rápidamente entre AWS, Azure, Google, on-premise,
etc. y para comparar costes. Las limitaciones también son comunes en la nube, lo que conduce a soluciones creativas, que
a su vez aumentan la complejidad. aumentar. Las pruebas integradoras también pueden resultar caras, ya que cada
desarrollador necesita su propio entorno de desarrollo en la nube ya que muchos servicios en la nube apenas o nada
pueden probarse localmente. Pero incluso sin pruebas, la nube es cara. Mientras que con los sistemas locales se trata
sobre todo de costes de hardware, en la nube también hay que pagar por el tráfico, algunos servicios estándar y a menudo
incluso por múltiples y a menudo incluso por múltiples impuestos. Además, en la nube es fácil perder la noción de las
cosas, porque no se trata de no se trata de facilidad de uso, sino de dinero. Los costes están tan ocultos que sólo te
das cuenta de ellos cuando ya es demasiado tarde. es demasiado tarde. Los fundamentos de la arquitectura y la
infraestructura tienen que reinventarse en la nube y, especialmente, en serverless tienen que reinventarse, ya que la
implementación depende en gran medida de las características disponibles. Siempre que he diseñado la arquitectura,
pienso: "Esto podría haber sido un único servicio". podría haber sido". Para mí, serverless es una idea interesante y
escala bien, pero no reduce los costes. Al contrario, requiere mucho más conocimiento y tiempo en el desarrollo. El
serverless o la nube requieren disciplina y conocimientos previos. Si el conocimiento no está ahí para los sistemas on-
premise, no será más fácil con la nube. ¿Cómo se supone que los desarrolladores van a adquirir conocimientos adicionales
sobre infraestructuras? Preferiría un clúster Kubernetes bien gestionado a una arquitectura en la nube. La gente no
escala. Muchos desarrolladores no tienen disciplina a la hora de escribir código. Por desgracia, esto es cierto para el
80 por ciento de los desarrolladores. Entonces, ¿cómo van a ser capaces estos desarrolladores de ejecutar la nube? ¿la
nube? Es importante que las organizaciones comprendan plenamente los retos y las implicaciones de la arquitectura sin
servidor y la nube. comprender plenamente los retos y las implicaciones de la arquitectura sin servidor y la nube. Esto
requiere no solo conocimientos técnicos, sino también un enfoque estratégico. A na migración a la nube mal meditada
puede generar complejidad, mayores costes y sobrecargar a los desarrolladores. En resumen, la arquitectura sin servidor
en la nube es un concepto prometedor, pero que debe considerarse cuidadosamente. debe considerarse cuidadosamente. Hay
que tener en cuenta el coste, la complejidad, la capacidad de mantenimiento y las habilidades del equipo de desarrollo.
tenerse en cuenta. Cada empresa tiene requisitos y prioridades diferentes. Debe tomarse una decisión informada sobre si
Serverless en la nube es la solución adecuada o si los enfoques alternativos como por ejemplo, Kubernetes Cluster son la
mejor opción. El despliegue exitoso de la computación sin servidor y en la nube requiere una combinación de experiencia
técnica planificación estratégica y una clara comprensión de los requisitos empresariales. Solo entonces se puede
ilusionar con el serverless y tomar la decisión correcta para su propio desarrollo de software.

### Fazit

La introducción de funciones sin servidor en la nube promete flexibilidad, escalabilidad y alivio de las tareas de
infraestructura. desarrolladores de las tareas de infraestructura. Sin embargo, no hay que dejarse cegar por esta
ilusión. El paso a la nube y el uso de funciones sin servidor conlleva una serie de retos. Los desarrolladores tienen
que aprender un nuevo "lenguaje" además del desarrollo propiamente dicho y asumir más responsabilidad sin el apoyo
adecuado. Asumir más responsabilidad. La complejidad de las funciones sin servidor suele ser mayor que la de los
microservicios, ya que los desarrolladores tienen que asumir muchas tareas adicionales, como por ejemplo los
desarrolladores tienen que asumir muchas tareas adicionales, como la definición de la infraestructura, la seguridad y el
escalado. Las verdaderas pruebas integradoras son difícil y el conocimiento y la experiencia previos para las
operaciones son aún más importantes en la nube. La propia nube plantea otros retos. Muchas tecnologías de nube no están
actualizadas y el uso de servicios modernos estándar puede resultar caro o incluso imposible. Los requisitos normativos,
el cumplimiento y la protección de datos limitan el alcance. Además, los costes en la nube se escapan fácilmente de las
manos, y la visión de conjunto de los gastos se pierde rápidamente. En definitiva, hay que sopesar cuidadosamente las
ventajas y desventajas de la tecnología sin servidor y de la nube. Las empresas deben tener en cuenta sus requisitos
específicos, la experiencia existente en el equipo y los efectos a largo plazo de una migración a la nube. de una
migración a la nube. Una decisión informada basada en un análisis exhaustivo es crucial para el éxito y la rentabilidad
del proyecto. del proyecto. En última instancia, corresponde a las empresas apoyar adecuadamente a sus desarrolladores,
evaluar de forma realista los costes y la complejidad de la nube de forma realista y considerar soluciones alternativas
como los clústeres Kubernetes bien gestionados. Con una estrategia clara y una comprensión sólida de sus propias
necesidades, las empresas pueden aprovechar al máximo las ventajas de la nube y las capacidades sin servidor y ver a
través de la ilusión.

### Contacto

[Problemas en GitHub](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
