---
title: "Voltar para o Maven?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "A difícil busca pela simplicidade e uma breve jornada pela redescoberta do poder do Maven."
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# Voltar para o Maven?

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)


``` 

Tradução: 

[![maven_vs_gradle](/imagens/conteúdo/maven_vs_gradle.png)](https://phauer.com/2018/voltando-do-gradle-para-o-maven/) 

```

## 10 anos de Gradle. Em busca de facilidade e uma breve jornada para redescobrir a força do Maven.

Desculpe-me, mas não há nada para traduzir. O markdown vazio não contém nenhum texto ou conteúdo a ser traduzido.

### Maximização do Potencial dos Desenvolvedores - Precisamos de mais ferramentas que economizem tempo

Os temas que são frequentemente negligenciados ou raramente discutidos me interessam. Muitas vezes, as tecnologias bacanas estão em uso, mas poucos falam sobre os problemas associados a elas. O desenvolvimento se tornou muito exigente nos dias de hoje. Com palavras de destaque como "Serverless", "Low Code", "IaC", "Big Data", "Cloud", "DevOps", "You Build it You run it", etc., os desenvolvedores já têm mais do que suficientes tarefas extras para lidar. Mais tarefas significam que há quase nenhum especialista restante e sempre algo que é negligenciado no foco. Por isso, automação e economia de tempo são mega importantes. "Não me faça pensar" e "Funciona Out of the Box" são bons indicadores de qualidade que ainda não vejo em Gradle. Para ser justo, Gradle não é a única ferramenta moderna que nos dificulta o trabalho em vez de facilitá-lo.

### A busca ilusória pela simplicidade e automação

Desde o SOAP, tenho uma aversão profunda às configurações baseadas em XML. Com o Gradle, esperava que escrever scripts de ligação fosse fácil. Infelizmente, minhas esperanças e motivação diminuíram a cada tentativa. O Gradle busca flexibilidade e sacrifica automação e qualidade. Desenvolvedores seguem cegamente a tendência sem considerar os efeitos na confiabilidade do software. Para manter os scripts de build de Gradle simples e fáceis de manter, é necessário uma forte disciplina. Tal disciplina é rara no código-fonte e ainda mais rara nos scripts de build.

### Traduções e Soluções Alternativas - Quando roteiros de construção se tornam um desafio

Gradle trabalha nos bastidores não muito diferente do Maven. Portanto, algumas traduções são necessárias. Recursos como
o Dependency Catalog, o Maven Release Plugin, o Dependabot e muitos outros são, na verdade, contornos para funções
básicas que o Maven já traz consigo. Com a flexibilidade do Gradle, muitas vezes surgem configurações de build complexas
e difíceis de manter. Os plugins do Gradle frequentemente apresentam problemas de compatibilidade, limitações ou
evoluções limitadas. Esses problemas surgem devido à natureza em evolução do ecossistema do Gradle, a variedade de
ambientes em que o Gradle é usado e o esforço específico de implementação e manutenção de cada plugin. Tudo está
conectado.

### O efeito dominó do Gradle - Um cenário de pesadelo no mundo real

Vi muitos microservices que tinham apenas alguns anos e já não eram mais sustentáveis devido ao Gradle. Vale mencionar que esse não é a primeira vez que vejo algo assim e não, não foram desenvolvedores juniores.

**Minha tarefa era fazer a atualização do Spring Boot 2.x para 2.7**. Spoiler: Eu desisti depois de um ano! Os problemas resumidos foram:

* O arquivo de build do Gradle exigiu -> Downgrade da minha versão local do Java para 11 (WTF) (Normalmente, o Java é compatível com versões anteriores - existem também ferramentas de contorno como o SdkMan...)
* A atualização do Spring Boot exigiu -> Atualização do Gradle (WTF)
* A atualização do Gradle exigiu -> Atualização do plugin
* A atualização do plugin exigiu -> Atualização do Groovy (WTF)
* A atualização do Groovy exigiu -> Atualizações do framework de teste (WTF)
* As atualizações do framework de teste exigiram -> Atualizações de dependência
* \[...]
  Além disso, alguns plugins não funcionam com versões mais recentes do Gradle, alguns não são mais desenvolvidos, são incompatíveis com outros plugins, funcionam apenas com o Gradle KTS, não com o Gradle Groovy, ou têm simplesmente limitações. Mesmo plugins de grandes fornecedores como a Spring têm funcionalidades limitadas em comparação com seus plugins do Maven. No final, tenho um arquivo de build curto e legal do Gradle que ninguém pode manter direito, nem mesmo os desenvolvedores que o escreveram, e eles ainda amam o Gradle. Conheço poucos que entendem ou podem escrever scripts Gradle de forma séria.

### A redescoberta da força do Maven - Utilizando os poderes mágicos do Maven

Aqui estão minhas funções favoritas do Maven:
Os plugins podem ser iniciados e configurados diretamente da linha de comando, sem a necessidade de definir isso antes. Além disso, eles são amplamente independentes de outras configurações de plugin.

| Comando de Exemplo                    | Descrição                                                                                                                                                           | Link                                                                     | 
|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `mvn versions:use -latest-versions`   | Atualiza as versões - para quem precisa do Dependabot? Sim, meus projetos são atualizados para a versão mais recente sem solicitações de merge desagradáveis há anos | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0` | Define a versão do projeto...                                                                                                                                       | https://www.mojohaus.org/versions/versions-maven-plugin/index.html       |
| `mvn license:add-third-party`         | Lista as dependências e exibe suas licenças (até mesmo pode falhar com licenças excluídas)                                                                         | https://www.mojohaus.org/license-maven-plugin/index.html                 | 

Essa lista poderia continuar para sempre. De alguma forma, isso me lembra dos passos do GitHub Workflow.

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)

### Não gosta de XML?

Sem problema! Apenas escreva o seu arquivo de construção em `ruby`, `groovy`, `scala`, `yaml`, `atom` ou `Java`. A extensão Polygot (https://github.com/takari/polyglot-maven) torna isso possível. Para experimentar, basta executar  `mvn io.takari.polyglot: polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` e em poucos milissegundos seu arquivo de construção será traduzido. É uma pena que não haja um tradutor confiável de Maven para Gradle:(. Sim, os arquivos de construção do Maven são grandes, mas também muito fáceis de entender. Ajustes ou depurações são feitos num piscar de olhos.

### Idade é apenas um número - Estabilidade e Evolução do Maven

Para ser honesto, o Maven existe há bastante tempo e sua estética pode não corresponder aos padrões atuais. No entanto,
a longevidade do Maven permitiu que ele se adaptasse e evoluísse. O Maven trabalha independentemente do seu projeto. Os
arquivos de build podem ser facilmente reutilizados. Os plugins são executados em uma sandbox e são independentes entre
si e independentes da versão Java ou Maven. Esse design promove a estabilidade e previsibilidade e torna fácil gerenciar
processos de build complexos sem conflitos inesperados.

### Conclusão

Atualmente, o ambiente de desenvolvimento está sobrecarregado com muitas tarefas e tecnologias para os desenvolvedores.
Em busca de simplicidade e automação, o Gradle surgiu como uma moderna ferramenta de compilação, mas trouxe seus
próprios desafios. Sem dúvida, o conceito do Gradle é bom! No entanto, dada a complexidade e o tempo investido em
scripts de compilação do Gradle, surge a pergunta se não seria mais fácil estender o Maven. Com plugins e extensões, o
Maven pode ser atualizado e simplificado a qualquer momento. Seria mais emocionante e sustentável continuar
desenvolvendo o Maven em vez de pular de uma tecnologia para outra?

### Links

* [Voltando do Gradle para o Maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### Contato

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
