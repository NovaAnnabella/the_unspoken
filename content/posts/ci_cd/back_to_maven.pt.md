---
title: "De volta ao Maven?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "A busca evasiva pela simplicidade e uma breve viagem para redescobrir o poder do Maven."
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# De volta ao Maven?

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

## 10 anos de Gradle. Na busca por alívio e uma breve viagem para redescobrir a força do Maven.



### Maximização do Potencial dos Desenvolvedores - Precisamos de mais ferramentas que poupem tempo

Temas que muitas vezes são negligenciados ou raramente discutidos me interessam. Muitas vezes, tecnologias legais estão em uso,
mas quase ninguém fala sobre os problemas associados a eles.
Desenvolvimento tornou-se muito complexo nos dias de hoje.
Com esses buzzwords legais como "Serverless", "Low Code", "IaC", "Big Data", "Cloud", "DevOps", "You Build it You run it"
etc., desenvolvedores já têm mais que tarefas suficientes para lidar. Mais tarefas significa que mal existem
especialistas, e sempre algo é negligenciado por causa do foco. Portanto, automações e economia de tempo são muito
importante. "Não me faça pensar" e "Funciona fora da caixa" já são bons indicadores de qualidade que não consigo ver em Gradle ainda.
Para ser justo, Gradle não é a única ferramenta moderna que nos dá trabalho em vez de facilitá-lo.

### A busca ilusória por simplicidade e automação

Desde SOAP, tenho uma aversão profunda a configurações baseadas em XML. Com o Gradle, eu esperava que escrever scripts de 
vinculação seria uma brincadeira de criança. Infelizmente, minhas esperanças e minha motivação diminuíram cada vez mais. 
O Gradle busca flexibilidade, sacrificando automatização e qualidade. Desenvolvedores seguem cegamente a tendência sem considerar 
os impactos na confiabilidade do software. Para manter os scripts de construção do Gradle simples e de fácil manutenção, é necessário 
uma grande disciplina. Tal disciplina é rara no código-fonte e, portanto, ainda mais rara nos scripts de construção.

### Traduções e Soluções Alternativas - Quando Scripts de Construção se Tornam um Desafio

Gradle não trabalha muito diferente de Maven em segundo plano. Portanto, algumas traduções são necessárias. Recursos
como o Catálogo de Dependência, o Plugin de Release do Maven, o Dependabot e muitos mais são na verdade soluções
alternativas para funções básicas que Maven já possui. Com a flexibilidade do Gradle, muitas vezes surgem configurações
de build complexas, que são difíceis de manter. Os plugins do Gradle frequentemente apresentam problemas de
compatibilidade, limites ou desenvolvimentos limitados. Esses problemas surgem devido à natureza em evolução do
ecossistema Gradle, à variedade de ambientes em que o Gradle é utilizado e ao esforço específico de implementação e
manutenção para cada plugin. Tudo está interconectado.

### O Efeito Dominó do Gradle - Um cenário de pesadelo no mundo real

Eu vi muitos microserviços que tinham apenas alguns anos e já não eram mais sustentáveis devido ao Gradle.
É importante mencionar que essa não é a primeira vez que vejo isso, e não, não eram
Juniors Devs.

Minha **tarefa era realizar um upgrade do Spring Boot 2.x para 2.7**. Spoiler: Eu desisti depois de um ano
Os problemas resumidamente:

* O arquivo de build do Gradle requer -> Downgrade da minha versão local do Java para 11 (WTF) (Normalmente Java
  é compatível com versões anteriores - também existem ferramentas alternativas como SdkMan ...)
* A atualização do Spring Boot requer -> Atualização do Gradle (WTF)
* A atualização do Gradle requer -> Atualização de plugin
* A atualização do plugin requer -> Atualização do Groovy (WTF)
* A atualização do Groovy requer -> Atualizações de framework e teste (WTF)
* Atualização do framework de teste requer -> Atualizações de dependência
* \[...]
  Além disso, alguns plugins não funcionam com versões mais recentes do Gradle, alguns não são mais desenvolvidos, são incompatíveis com outros plugins, funcionam somente com Gradle KTS e não com Gradle Groovy, ou
  simplesmente têm limites. Até plugins de grandes fornecedores como Spring têm funcionalidades limitadas em comparação com seus plugins Maven.
  No final, tenho um arquivo de build do Gradle legal e conciso que ninguém pode manter adequadamente,
  nem mesmo os desenvolvedores que o escreveram, e eles ainda amam o Gradle. Eu apenas conheço poucos que
  realmente entendem ou conseguem escrever scripts Gradle.

### A Redescoberta da Força de Maven - Usando os Poderes Mágicos de Maven

Aqui estão minhas funções favoritas do Maven:
Os plugins podem ser iniciados e configurados diretamente da linha de comando, sem precisar serem definidos previamente.
Além disso, eles são amplamente independentes de outras configurações do plugin.

| Comando de exemplo                    | Descrição                                                                                                                                                           | Link                                                                     | 
|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `mvn versions:use -latest-versions`   | Atualizar versões - quem precisa do Dependabot? Sim, meus projetos têm sido atualizados sem problemas para a versão mais recente há anos, sem irritantes solicitações de merge | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0` | Definir a versão do projeto...                                                                                                                                      | https://www.mojohaus.org/versions/versions-maven-plugin/index.html       |
| `mvn license:add-third-party`         | Listar dependências e mostrar suas licenças (pode até falhar com licenças excluídas)                                                                                | https://www.mojohaus.org/license-maven-plugin/index.html                 | 

Essa lista poderia continuar indefinidamente. De alguma forma me lembra os Passos do Workflow do GitHub.

![maven_plugin_command_line_args](/imagens/conteudo/maven_plugin_command_line_args.png)

### Você não gosta de XML?

Sem problemas! Basta escrever seu Build File em `ruby`, `groovy`, `scala`, `yaml`, `atom` ou `Java`. A Extensão
Poliglota (https://github.com/takari/polyglot-maven) torna isso possível. Para testar,
basta executar `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` e em
poucos milissegundos seu Build File é traduzido. Pena que não há um tradutor Maven <> Gradle confiável
:( 
Sim, os arquivos de Build do Maven são grandes, mas também muito fáceis de entender. Melhorias ou depuração podem ser
feitas num piscar de olhos.

### Idade é apenas um número - Estabilidade e Evolução do Mavens

Admitidamente, o Maven já existe há algum tempo e sua estética pode não atender aos padrões atuais. No entanto, a
longevidade do Maven permitiu que ele se adaptasse e evoluísse. O Maven funciona independentemente do seu projeto. Os
arquivos de construção podem ser facilmente reutilizados. Os plugins funcionam em uma sandbox e são independentes um do
outro e independentes da versão do Java ou do Maven. Este design promove a estabilidade e previsibilidade, tornando
fácil gerenciar processos de construção complexos sem inesperados conflitos a gerir.

### Conclusão

Hoje em dia, o ambiente de desenvolvimento está sobrecarregado com muitas tarefas e tecnologias para desenvolvedores. Na
busca por simplicidade e automação, o Gradle surgiu como uma moderna ferramenta de construção, mas trouxe seus próprios
desafios. Sem dúvida, o conceito do Gradle é bom! No entanto, diante da complexidade e do tempo investido nos scripts de
construção Gradle, surge a pergunta se não seria mais fácil estender o Maven para ampliar. Com plugins e extensões, o
Maven poderia ser atualizado e simplificado a qualquer momento. Não seria uma evolução muito mais emocionante e também
mais sustentável, do que pular de uma tecnologia para outra?

### Links

* [Voltando do Gradle para o maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### Contato

[Problemas do GitHub](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
