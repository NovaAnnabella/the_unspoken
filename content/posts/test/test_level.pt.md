---
title: "Testebenen: Encontrar o equilíbrio certo"
date: 2023-05-31
author: "Nova Annabella"
slug: test_level
tags: [ Testing, Software Testing, Test Levels, Mock Tests, Unit Tests, Integration Tests, Component Tests, Contract Tests, End-to-End Tests ]
categories: [ Technology, Software Development, Quality Assurance ]
description: "Encontrar o equilíbrio certo na escolha dos níveis de teste adequados para testes de software"
draft: false
images:
  - "/images/content/martin_fowler_testing.png"
card: "summary_large_image"
---


# Níveis de teste: Encontrar o equilíbrio certo

[![testebenen](/images/content/martin_fowler_testing.png)](https://martinfowler.com/articles/microservice-testing/)

### Introdução

O tópico de teste parece ser até hoje um território inexplorado com muito espaço para interpretação. A pirâmide de teste tradicional foi questionada e novas pirâmides de teste surgiram. Na minha opinião, não é necessária uma pirâmide de teste, mas sim uma compreensão clara do que precisa ser testado. Os testes em níveis mais baixos geralmente são menos conclusivos. O foco deve ser principalmente no teste do comportamento, para garantir que a API ou UI funcione conforme esperado. Uma visão geral completa de possíveis tipos de teste pode ser encontrada aqui: [Testes Martinfowler](https://martinfowler.com/articles/microservice-testing/).


### Nível 1 - Testes Simulados & Testes Unitários

Objetivo: Exercer as menores partes testáveis do software na aplicação para determinar se estão funcionando conforme o esperado.

Os testes de simulação e unitários podem ser contraproducentes e frequentemente atrapalham o processo de desenvolvimento. Esses testes muitas vezes
são desvinculados do contexto e têm pouco a ver com a realidade. Eles geralmente servem apenas para manter funções desnecessárias sobre as existentes
testes unitários. Assim que os mocks são adicionados, torna-se um auto-ocupação. Os resultados esperados dos testes de simulação são limitados ao que foi definido no mock original. Os usuários finais
não se interessam por funções internas. Por exemplo, em um
cenário de login `loginUser(nome, senha, algoritmoDeSegurança)`. Se o teste unitário realiza uma verificação nula no
parâmetro `algoritmoDeSegurança`, está sendo testado demais, já que os usuários não
podem definir o parâmetro `algoritmoDeSegurança`.

### Nível 2 - Teste de Integração

Objetivo: Verificação das vias de comunicação e interações entre os componentes para detecção de falhas nas interfaces.
Os testes de integração fornecem informações valiosas sobre a performance e independência de diferentes partes do
aplicativo. Com menos simulacros, os testes se tornam mais compreensíveis. No entanto, ainda lhes falta contexto, e há
risco de que os testes de integração sejam apenas testes unitários disfarçados com menos simulacros.

### Nível 3 - Teste de Componente

Objetivo: Limitação do escopo do software testado para uma parte do sistema a ser testado, manipulação do sistema
através de interfaces de código interno e uso de dublês de teste para isolar o código a ser testado de outros
componentes. Os testes de componentes fornecem uma grande quantidade de informações sobre a qualidade e a capacidade de
desempenho do aplicativo. Em vez de Mocks, você testa finalmente o seu aplicativo. A linha entre testes de componentes e
testes de ponta a ponta não está significante. Com um bom ambiente de teste, as linhas entre eles muitas vezes se
ofuscam, tornando possível testar o real comportamento em vez de funções isoladas e sem contexto. No entanto, a criação
de classes de teste adicionais como componentes stubs, fakes e mocks no código de produção podem trazer manutenção
adicional.

### Nível 4 - Teste de Contrato

O propósito deste bloco de código é verificar as interações na fronteira de um serviço externo e garantir que ele atenda
aos requisitos de contrato de um serviço consumidor. Os testes de contrato geralmente se assemelham aos testes de
componente, e a diferença entre eles é mínima. Alguns desenvolvedores associam esses testes aos testes de Pact, que
basicamente funcionam como testes de unidade com um servidor intermediário. O esforço para manter esses testes pode não
ser recompensador. Por exemplo, um teste de Pact poderia testar a API REST `loginUser?name=aa&password=bb)` e esperar
uma resposta em esquema JSON que foi previamente carregada no servidor Pact. Este esquema é estático e suscetível a
erros como formatos de data incorretos ou fusos horários na resposta da API. Os efeitos negativos podem ser enormes.

### Nível 5 - Testes de ponta a ponta (também chamados de testes de caixa preta)

Objetivo: Verificar se um sistema atende aos requisitos externos e alcança seus objetivos, testando todo o sistema do
início ao fim. Os testes de ponta a ponta são confiáveis e robustos. Uma vez superados os obstáculos de configuração do
ambiente de teste, o esforço compensa. Esses testes simulam comportamentos reais e eliminam a necessidade de mocks. Os
erros ocorrem menos frequentemente e são mais facilmente reproduzidos localmente. O debugging extensivo e a manutenção
de logs em produção são em grande parte evitados, assim como incidentes raros. Os desenvolvedores interagem menos, se
for o caso, com dados de produção, o que reduz a responsabilidade e aumenta o foco. Além disso, automações como
atualizações de software automáticas facilitam a realização, já que o comportamento já foi testado. Há mais vantagens!
Assim que os testes são escritos de forma reutilizável, eles podem ser integrados em testes de carga para se obter uma
visão completa da funcionalidade. Esses testes também podem ser executados continuamente no ambiente de produção e
oferecer insights em tempo real sobre o status de diferentes fluxos de trabalho. Se um subsistema, como por exemplo, um
serviço REST externo, ficar offline, é possível identificar imediatamente quais fluxos de trabalho do usuário são
afetados.

### Conclusão

Em suma, o teste é um aspecto essencial do desenvolvimento de software, e a escolha dos níveis de teste depende das
exigências e objetivos específicos da aplicação. Enquanto testes de simulação e testes unitários em sua eficácia podem
ser limitados, os testes de integração e testes de componentes fornecem visões valiosas sobre o comportamento e o
desempenho da aplicação. Testes de contrato auxiliam na verificação de interações com serviços externos, mas seu
delineamento em relação a testes de componentes pode ser mínimo. Finalmente, testes de ponta a ponta oferecem o mais
alto nível de confiança em a funcionalidade do sistema e permitem testes abrangentes de toda a aplicação. Ao selecionar
os níveis de teste apropriados e a combinação eficaz dos mesmos, os desenvolvedores podem garantir a qualidade,
confiabilidade e robustez do seu software.

### Contato

[Issues do GitHub](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
