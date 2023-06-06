---
title: "Níveis de teste: Encontrar o equilíbrio correcto"
date: 2023-05-31
author: "Nova Annabella"
slug: test_level
tags: [ Testing, Software Testing, Test Levels, Mock Tests, Unit Tests, Integration Tests, Component Tests, Contract Tests, End-to-End Tests ]
categories: [ Technology, Software Development, Quality Assurance ]
description: "Encontrar o equilíbrio certo na selecção dos níveis de teste adequados para testes de software"
draft: false
images:
  - "/images/content/martin_fowler_testing.png"
card: "summary_large_image"
---


# Níveis de teste: Encontrar o equilíbrio correcto

[![testebenen](/images/content/martin_fowler_testing.png)](https://martinfowler.com/articles/microservice-testing/)

### Introdução

O tema dos testes parece ser ainda um território desconhecido, com muita margem para interpretação. A tradicional
pirâmide de testes tradicional foi posta em causa e surgiram novas pirâmides de testes. Na minha opinião, não há
necessidade de uma pirâmide de testes, mas sim uma compreensão clara do que precisa de ser testado. Os testes dos níveis
inferiores são frequentemente menos significativos. A tónica deve ser colocada principalmente no teste do comportamento
para garantir que a API ou a IU funciona como pretendido. Uma visão abrangente dos possíveis tipos de teste pode ser
encontrada aqui: [Martinfowler Testing](https://martinfowler.com/articles/microservice-testing/).

### Nível 1 - Testes de simulação e testes unitários

Objectivo: Exercitar as partes de software testáveis mais pequenas da aplicação para ver se funcionam como esperado.
trabalho. Testes de simulação e testes unitários podem ser contraproducentes e muitas vezes atrapalham o processo de
desenvolvimento. Estes testes são frequentemente Estes testes são frequentemente desligados do contexto e têm pouca
relação com a realidade. Muitas vezes servem apenas para manter funções desnecessárias através de testes unitários
existentes. Uma vez que os testes de simulação são adicionados, torna-se um exercício auto-destrutivo. Os resultados
esperados Os resultados esperados dos testes de simulação são limitados ao que foi definido na simulação original. Os
utilizadores finais não estão interessados em funções internas. Por exemplo, em um cenário de cenário de login
`loginUser(nome, senha, securityAlgorithm)`. Se o teste unitário fizer uma verificação nula em o parâmetro
`securityAlgorithm`, muitos testes são feitos porque os usuários não podem definir o parâmetro `securityAlgorithm`.
definir o parâmetro `securityAlgorithm'.

### Nível 2 - Teste de integração

Objectivo: Verificar as vias de comunicação e as interacções entre componentes para detectar defeitos de interface. Os
testes de integração fornecem informações valiosas sobre o desempenho e a independência das diferentes partes da
aplicação. Aplicação. Com menos simulações, os testes tornam-se mais compreensíveis. No entanto, eles ainda carecem de
contexto, e há o risco de que Os testes de integração são simplesmente testes unitários disfarçados com menos
simulações.

### Nível 3 - Teste de componentes

Objectivo: limitar o âmbito do software em ensaio a uma parte do sistema em ensaio, manipular o sistema através de
interfaces de código internas e da utilização de duplos de teste para isolar o código em teste de outros componentes.
componentes. O teste de componentes fornece uma grande quantidade de informações sobre a qualidade e o desempenho da
aplicação. Em vez de mocks, você finalmente testa sua aplicação. A fronteira entre o teste de componentes e o teste de
ponta a ponta não é significativa. Com um bom ambiente de teste, as fronteiras entre eles tornam-se muitas vezes ténues,
de modo que o teste do comportamento real em vez de funções isoladas e sem contexto. No entanto, a criação de classes de
teste adicionais No entanto, a criação de classes de teste adicionais, como stubs de componentes, fakes e mocks no
código de produção, pode aumentar as despesas de manutenção.

### Nível 4 - Teste do contrato

O objectivo deste bloco de código é verificar as interacções na fronteira de um serviço externo e garantir que cumpre os
requisitos contratuais de um serviço consumidor. Os testes de contrato muitas vezes se assemelham a testes de unidade,
e a diferença entre eles é mínima. Alguns programadores associam estes testes a testes Pact, que actuam essencialmente
como testes unitários com um servidor no meio. O esforço O esforço de manter esses testes pode não valer a pena, no
entanto. Por exemplo, um teste Pact poderia usar a REST API `loginUser?name=aa&password=bb)` e esperar uma resposta de
esquema JSON que foi previamente carregada para o servidor Pact. servidor. Esse esquema é estático e propenso a erros,
como formatos de data ou fusos horários incorretos na resposta da API. resposta da API. Os efeitos negativos podem ser
enormes.

### Nível 5 - Testes de extremo a extremo (também designados por testes de caixa negra)

Objectivo: Verificar se um sistema cumpre os requisitos externos e atinge os seus objectivos, testando todo o sistema do
princípio ao fim. do início ao fim. O teste de ponta a ponta é fiável e robusto. Uma vez ultrapassados os obstáculos da
configuração do ambiente de teste, o esforço compensa. Estes testes simulam o comportamento real e eliminam a
necessidade de mocks. Os erros ocorrem com menos frequência e são mais fáceis de reproduzir localmente. A depuração e o
registo demorados na produção são largamente evitados, assim como os incidentes raros. são largamente evitados, assim
como os incidentes raros. Os programadores trabalham com menos frequência, se é que trabalham, com dados de produção, o
que reduz a responsabilidade e aumenta a produtividade. dados de produção, o que reduz a responsabilidade e aumenta a
concentração. Além disso, as automatizações, tais como as actualizações automáticas de software facilitam a
implementação, uma vez que o comportamento já foi testado. Há outras vantagens! Uma vez que Uma vez que os testes são
escritos numa forma reutilizável, podem ser integrados em testes de carga para obter uma para obter uma visão global da
funcionalidade. Estes testes também podem ser executados continuamente no ambiente de produção e fornecer informações em
tempo real sobre o estado de vários fluxos de trabalho. Quando um subsistema, como o serviço Quando um subsistema, como
o serviço REST, por exemplo, fica offline, é possível identificar imediatamente quais os fluxos de trabalho dos
utilizadores que são afectados. são afectados.

### Fazit

Em resumo, o teste é um aspecto essencial do desenvolvimento de software e a escolha dos níveis de teste depende de dos
requisitos e objectivos específicos da aplicação. Embora os testes de simulação e os testes unitários possam ser
limitados em termos de eficácia, os testes de integração e os testes unitários fornecem informações valiosas sobre o
comportamento e o desempenho da aplicação. Embora os testes de simulação e os testes unitários possam ser limitados na
sua eficácia, os testes de integração e os testes unitários fornecem informações valiosas sobre o comportamento e o
desempenho da aplicação. desempenho da aplicação. Os testes de contrato ajudam a verificar as interacções com serviços
externos, mas a sua A sua diferenciação em relação aos testes unitários pode ser mínima. Em última análise, os testes de
extremo a extremo proporcionam o mais elevado nível de confiança na funcionalidade do sistema e permitem a realização de
testes exaustivos. Os testes de ponta a ponta fornecem o mais alto nível de confiança na funcionalidade do sistema e
permitem testes abrangentes de toda a aplicação. Ao seleccionar os níveis de teste níveis de teste adequados e
combinando-os eficazmente, os programadores podem garantir a qualidade, fiabilidade e robustez do seu software.

### Contacto

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
