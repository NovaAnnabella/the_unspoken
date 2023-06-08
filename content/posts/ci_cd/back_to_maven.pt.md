---
title: "Voltar para o Maven?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "A difícil busca pela simplicidade e uma curta jornada para redescobrir o poder do Maven"
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# Voltando para o Maven?

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

Tradução:

[![maven_vs_gradle](/imagens/conteúdo/maven_vs_gradle.png)](https://phauer.com/2018/voltando-do-gradle-para-o-maven/)

## 10 Anos de Gradle. Procurando por facilidade e uma breve jornada de redescoberta da força do Maven.

Não há nada para traduzir nesse trecho de texto. Ele é apenas uma seção de código vazia no formato Markdown.

### Maximização do Potencial dos Desenvolvedores - Precisamos de mais ferramentas que economizem tempo.

Temas que muitas vezes são ignorados ou raramente discutidos me interessam. Muitas vezes, tecnologias interessantes estão em uso, mas quase ninguém fala sobre os problemas associados a elas. O desenvolvimento se tornou muito complexo nos dias de hoje. Com palavras-chave como "Serverless", "Low Code", "IaC", "Big Data", "Cloud", "DevOps", "You Build it You run it" e outros, os desenvolvedores já têm tarefas adicionais mais do que suficientes para lidar. Mais tarefas significam que há cada vez menos especialistas e sempre algo é negligenciado. Portanto, automação e economia de tempo são extremamente importantes. "Don't make me think" e "Works out of the Box" já são boas características de qualidade que eu ainda não consigo ver no Gradle. Para ser justo, o Gradle não é a única ferramenta moderna que nos causa mais trabalho em vez de facilitá-lo.

### A busca ilusória pela simplicidade e automação

Desde SOAP, eu tenho uma aversão enraizada às configurações baseadas em XML. Com Gradle, eu esperava que escrever scripts de vinculação fosse fácil como um jogo de criança. Infelizmente, minhas esperanças e minha motivação diminuíram a cada vez. Gradle visa à flexibilidade e sacrifica automação e qualidade para isso. Os desenvolvedores seguem cegamente a tendência sem considerar as consequências para a confiabilidade do software. Para manter os scripts de build do Gradle simples e fáceis de manter, é necessária uma disciplina forte. Tal disciplina é rara no código-fonte e, portanto, é ainda mais rara nos scripts de build.

### Traduções e soluções alternativas - Quando scripts de construção se tornam um desafio.

Gradle não trabalha nos bastidores muito diferente do Maven. Portanto, algumas traduções são necessárias. Recursos como
o Catálogo de Dependências, o Plugin de Lançamento do Maven, o Dependabot e muitos outros são realmente soluções
alternativas para recursos básicos que o Maven já traz. Com a flexibilidade do Gradle, muitas vezes surgem configurações
de compilação complexas que são difíceis de manter. Os plugins do Gradle frequentemente têm problemas de
compatibilidade, restrições ou desenvolvimento limitado. Esses problemas surgem devido à natureza em evolução do
ecossistema do Gradle, à variedade de ambientes nos quais o Gradle é usado e ao esforço específico de implementação e
manutenção de cada plugin. Tudo está interligado.

### O efeito dominó do Gradle: um cenário de pesadelo no mundo real

Eu vi muitos microservices que tinham apenas alguns anos de idade e já eram difíceis de manter devido ao Gradle. É importante mencionar que não é a primeira vez que vejo algo assim e não, não foram desenvolvedores juniores.

Minha **tarefa era fazer um upgrade do Spring Boot 2.x para o 2.7**. Spoiler: desisti depois de um ano! Os problemas resumidos:

* O arquivo de build do Gradle exige -> Downgrade da minha versão local do Java para o 11 (WTF) (geralmente o Java é compatível com versões anteriores - há novamente ferramentas como o SdkMan ...)
* A atualização do Spring Boot exige -> Atualização do Gradle (WTF)
* A atualização do Gradle exige -> Atualização de Plugins
* A atualização do Plugin exige -> Atualização do Groovy (WTF)
* A atualização do Groovy exige -> Atualizações de Test Framework e teste (WTF)
* A atualização do Test Framework exige -> Atualizações de dependências
* \[...]
 Além disso, alguns plugins não funcionam com versões mais recentes do Gradle, alguns não são mais desenvolvidos, não são compatíveis com outros plugins, funcionam apenas com o Gradle KTS, não com o Gradle Groovy ou têm limitações simplesmente. Até mesmo plugins de grandes fornecedores como a Spring têm funcionalidade limitada em comparação com os seus plugins Maven. No final, eu tenho um legal e curto arquivo de build Gradle, que ninguém pode manter corretamente, nem mesmo os desenvolvedores que o escreveram, e ainda amam o Gradle. Conheço apenas alguns que entendem ou podem escrever scripts do Gradle seriamente.

### A redescoberta da força do Maven - Aproveitando os poderes mágicos do Maven

Aqui estão minhas funções favoritas do Maven:
Os plugins podem ser iniciados e configurados diretamente da linha de comando, sem precisar serem definidos antecipadamente. Além disso, eles são amplamente independentes de outras configurações de plugins.

| Comando de exemplo                    | Descrição                                                                                                                                                       | Link                                                                     | 
|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `mvn versions:use -latest-versions`   | Atualiza as versões - quem precisa do Dependabot? Sim, meus projetos foram atualizados para a versão mais recente sem pedidos de merge | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion= 1.0.0` | Definir a versão do projeto...                                                                                                                                  | https://www.mojohaus.org/versions/versions-maven-plugin/index.html       |
| `mvn license:add-third-party`         | Liste as dependências e mostre suas licenças (mesmo que possa falhar em licenças excluídas)                                                                    | https://www.mojohaus.org/license-maven-plugin/index.html                 | 

Esta lista poderia continuar indefinidamente. De alguma forma, isso me lembra os passos do GitHub Workflow.

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)

### Você não gosta de XML?

Sem problema! Basta escrever o seu arquivo de construção em `ruby`, `groovy`, `scala`, `yaml` , `atom` ou `Java`. A extensão Polyglot (https://github.com/takari/polyglot-maven) torna isso possível. Para experimentar, basta executar ` mvn io.takari.polyglot: polyglot-translate-plugin: translate -Dinput=pom.xml -Doutput=pom.yaml` e em poucos milissegundos o seu arquivo de construção será traduzido. É uma pena que não haja um tradutor confiável de Maven para Gradle :(
Sim, os arquivos de construção do Maven são grandes, mas também são muito fáceis de entender. As melhorias ou depurações são feitas em um piscar de olhos.

### Idade é apenas um número - Estabilidade e Evolução de Mavens

Admitido, o Maven existe há um bom tempo e sua estética pode não corresponder aos padrões atuais. No entanto, a
longevidade do Maven permitiu que ele se adaptasse e evoluísse. O Maven trabalha de forma independente do seu projeto.
Os arquivos de compilação podem ser facilmente reutilizados. Os plugins rodam em uma sandbox e são independentes uns dos
outros e independentes da versão Java ou Maven. Este design promove a estabilidade e previsibilidade e facilita a gestão
de processos de compilação complexos sem conflitos inesperados.

### Conclusão

Hoje em dia, o ambiente de desenvolvimento está sobrecarregado com muitas tarefas e tecnologias para os desenvolvedores.
Em busca de simplicidade e automação, o Gradle surgiu como uma moderna ferramenta de construção, mas trouxe seus
próprios desafios. Sem dúvida, o conceito do Gradle é bom! Porém, diante da complexidade e do tempo investido em scripts
de construção do Gradle, a pergunta é se não seria mais fácil estender o Maven. Com plugins e extensões, o Maven pode
ser atualizado e simplificado a qualquer momento. Seria mais emocionante e sustentável continuar o desenvolvimento do
Maven do que pular de uma tecnologia para outra?

### Links

* [Voltando do Gradle para o Maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### Contato

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose). 

```
