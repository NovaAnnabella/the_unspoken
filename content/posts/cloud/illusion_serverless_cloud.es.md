---
title: "Ilusión del Serverless y la Nube"
date: 2023-05-23
author: "Nova Annabella"
slug: illusion_serverless_cloud
tags: [ Development, Serverless, Cloud, Microservices, Scalability, Architecture, Infrastructure ]
categories: [ Technology, Software, Cloud ]
description: "Desafíos y realidades de las capacidades serverless en la nube. Ideas valiosas para las empresas que consideran migrar a la nube."
draft: false
images:
  - "/images/content/onprem_vs_cloud.png"
card: "summary_large_image"
---

# La ilusión de las funciones serverless en la nube

![aws_costs_twitter_1](/images/content/onprem_vs_cloud.png)

### Introducción

Estoy decepcionado de cuántas veces el marketing triunfa sobre el sentido común. Muchos gerentes se ponen por encima de
sus propios expertos, los desarrolladores. Esto también es cierto cuando se trata de migrar a la nube. Spoiler: Si
necesitas ahorrar dinero, deberías evitar la nube. Porque la nueva palabra de moda "serverless" en la nube significa: Tú
te encargas del software, nosotros nos encargamos del hardware. Sin embargo, si tienes un administrador capaz, motivado
e inquisitivo, puedes administrar Serverless por ti mismo (por ejemplo, [KNative](https://knative.dev)).

![aws_costs_twitter_1](/images/content/aws_costs_twitter_1.png)

### Funciones serverless vs. microservicios:

#### Microservicios

Un microservicio típico sin estado se encarga de una función/dominio específico y se implementa en un entorno de
orquestación de contenedores. Este entorno se encarga de la infraestructura, seguridad, cortafuegos, registro, métricas,
secretos, redes, copias de seguridad y más. Una gran ventaja es que un microservicio se puede implementar localmente con
pocos recursos y es agnóstico en términos de la nube o el servidor (se puede implementar en cualquier lugar).

#### Funciones serverless

Una pequeña broma antes: Paradójico pero cierto: las funciones serverless dependen en gran medida del entorno del
servidor. :)
Una función serverless típica también se encarga de una única función/dominio y se escribe en código sin frameworks para
que sea más rápido que un microservicio (también es un buen ejercicio para los MicroServices). Una gran ventaja es que
las funciones serverless se escalan automáticamente. Sin embargo, cada función serverless requiere una cantidad
considerable de código de enlace (GlueCode) para definir la infraestructura: seguridad, cortafuegos, redes, registro,
métricas, secretos, caché, copias de seguridad y mucho más. Por lo tanto, una función sencilla como copiar un archivo,
incluyendo una API, puede implicar rápidamente 1500 líneas de código (incluyendo IaC).
Los costos de administración se desplazan de la administración al desarrollo en una relación de 1:N (1 a N funciones
serverless). El conocimiento y la implementación ya no están
centralizados y pueden volverse inestables rápidamente. Además, existen costos de mantenimiento más elevados. Las
pruebas integradas reales también son poco comunes con serverless, o solo son posibles con mucho esfuerzo. En última
instancia, la complejidad de las funciones serverless es significativamente mayor que la de un microservicio individual.
Una mayor complejidad también significa una menor capacidad de mantenimiento. Los nuevos miembros del equipo tienen más
dificultades y necesitan mucho más conocimiento previo.

### Serverless y la nube en general

La mayoría de las tecnologías en la nube no están actualizadas. Por ejemplo, Node.js, Java, Python y otras
lenguajes o tecnologías a menudo no son fáciles de actualizar, generalmente solo esperar ayuda.
Incluso tecnologías modernas y estándar como MongoDB, MySQL, Kafka, NATS, RabbitMQ, Redis, Prometheus, InfluxDB,
Grafana,
Kibana, Elastic Search, etc. o bien no están disponibles o tienen precios elevados.
Sin estos servicios estándar, a menudo nos encontramos en la Edad de Piedra virtual y utilizamos soluciones obsoletas,
como
webhooks para la comunicación externa. Además, el margen de maniobra en temas como la regulación,
cumplimiento, protección de datos y seguridad en caso de fallos está severamente limitado.

Por lo tanto, la nube debe ser utilizada de manera agnóstica para poder cambiar rápidamente entre AWS, Azure, Google,
localmente, etc. y para
comparar costos.
En la nube también suelen haber límites, lo que lleva a soluciones creativas que, a su vez, aumentan la complejidad.
aumentan. Las pruebas integradas también pueden resultar costosas, ya que cada desarrollador necesita su propio entorno
de desarrollo en
la nube
dado que muchos servicios en la nube son difíciles o imposibles de probar a nivel local.
Pero incluso sin pruebas, la nube es costosa. Mientras que en los sistemas locales se trata principalmente de
costos de hardware, en la nube también hay que pagar por el tráfico, algunos servicios estándar y a menudo incluso por
múltiples
e incluso por múltiples impuestos. Además, es fácil perder la visión en la nube, porque no se trata de
no se trata de la facilidad de uso, sino del dinero. Los costos están tan ocultos que solo se perciben cuando ya es
demasiado
tarde.

Los fundamentos de la arquitectura y la infraestructura deben reinventarse en la nube y especialmente en el ámbito de
sin servidor
tienen que reinventarse, ya que la implementación depende en gran medida de las funciones disponibles.
Cada vez que he diseñado la arquitectura, pienso: "Esto podría haber sido un solo servicio".
podría haber sido".

Para mí, serverless es una idea interesante y escala bien, pero no reduce los costos. Al contrario,
requiere mucho más conocimiento y tiempo en desarrollo. Serverless o la nube requieren disciplina y conocimientos
previos.
Si no se cuenta con los conocimientos necesarios para los sistemas locales, no será más fácil con la nube.
¿Cómo deben los desarrolladores adquirir conocimientos adicionales sobre infraestructura?

Prefiero un clúster de Kubernetes bien gestionado en lugar de una arquitectura en la nube.
Las personas no escalan. Muchos desarrolladores no tienen disciplina para escribir código.
Lamentablemente, esto es cierto para el 80 por ciento de los desarrolladores. Entonces, ¿cómo podrán estos
desarrolladores
utilizar la nube?

Es importante que las organizaciones comprendan plenamente los desafíos y las implicaciones de la arquitectura
serverless y
la nube. Esto requiere no solo conocimientos técnicos, sino también un enfoque estratégico.
Una migración mal considerada a la nube puede llevar a la complejidad, mayores costos y sobrecarga de los
desarrolladores.

En resumen, serverless en la nube es un concepto prometedor, pero que debe considerarse cuidadosamente. Se deben tener
en cuenta
los costos, la complejidad, la mantenibilidad y las habilidades del equipo de desarrollo.
Cada empresa tiene diferentes requisitos y prioridades. Se debe tomar una decisión informada sobre si
Serverless en la nube es la solución adecuada o si enfoques alternativos como
por ejemplo, un clúster de Kubernetes bien gestionado, son la mejor opción.

La implementación exitosa de serverless y la computación en la nube requiere una combinación de experiencia técnica,
planificación estratégica y una comprensión clara de los requisitos comerciales. Solo así se puede desenmascarar la
ilusión de
serverless y tomar la decisión correcta para el desarrollo de software propio.

### Conclusión

La introducción de funciones sin servidor (serverless) en la nube promete flexibilidad, escalabilidad y alivio para
los desarrolladores en cuanto a tareas de infraestructura. Sin embargo, no hay que dejarse cegar por esta ilusión.
La migración a la nube y el uso de funciones sin servidor conllevan una serie de desafíos.

Los desarrolladores deben aprender un nuevo "lenguaje" además del desarrollo propiamente dicho y asumir más
responsabilidad sin el apoyo adecuado.
La complejidad de las funciones sin servidor suele ser mayor que la de los microservicios, ya que los desarrolladores
deben
asumir muchas tareas adicionales, como la definición de infraestructura, seguridad y escalabilidad. Las pruebas
integradas reales son
dificultosas y el conocimiento previo y la experiencia en operaciones son aún más importantes en la nube.

La nube en sí misma plantea otros desafíos. Muchas tecnologías en la nube no están actualizadas
y el uso de servicios modernos estándar puede ser costoso o incluso imposible. Las regulaciones, el cumplimiento
y
la protección de datos limitan el alcance. Además, los costos en la nube fácilmente se descontrolan
y se pierde rápidamente la visión general de los gastos.

En resumen, es necesario sopesar cuidadosamente las ventajas y desventajas de las funciones sin servidor y la nube.
Las empresas deben considerar sus requisitos específicos, la experiencia existente en el equipo y los efectos a largo
plazo de una
migración a la nube.
Una decisión informada basada en un análisis integral es crucial para el éxito y la rentabilidad del proyecto.

En última instancia, depende de las empresas brindar un soporte adecuado a sus desarrolladores, evaluar de manera
realista los costos y la complejidad
de la nube y considerar soluciones alternativas como clústeres de Kubernetes bien gestionados.
Con una estrategia clara y una comprensión sólida de sus propias necesidades, las empresas pueden aprovechar al máximo
los beneficios de la
nube y las capacidades sin servidor y ver a través de la ilusión.

### Contacto

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).

