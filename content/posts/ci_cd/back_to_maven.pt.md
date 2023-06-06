---
title: "De volta a Maven?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "A busca da simplicidade e uma pequena viagem para redescobrir o poder do Maven".
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---



# Voltar ao Maven?

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

## 10 anos de Gradle. Em busca de alívio e uma pequena viagem para redescobrir o poder do Maven.



### Maximizar o potencial dos programadores - precisamos de mais ferramentas que poupem tempo

Os tópicos que são frequentemente ignorados ou raramente discutidos interessam-me. Muitas vezes, utilizam-se tecnologias
fixes, mas quase ninguém fala sobre os problemas associados a elas. Actualmente, o desenvolvimento tornou-se muito
dispendioso. Com palavras-chave como "serverless", "low code", "IaC", "big data", "cloud", "DevOps", "you build it you
run it", etc., os programadores já estão fartos. etc., os programadores já têm tarefas adicionais mais do que
suficientes para resolver. Mais tarefas significa que quase não há especialistas especialistas e há sempre algo que é
negligenciado. É por isso que a automatização e a poupança de tempo são mega importantes. "Não me faça pensar" e
"Trabalha fora da caixa" já são características de boa qualidade que eu ainda não vejo no Gradle. Ainda não consigo ver.
Para ser justo, o Gradle não é a única ferramenta moderna que faz nosso trabalho ao invés de torná-lo torná-lo mais
fácil.

### A busca ilusória da simplicidade e da automatização

Desde o SOAP, tenho uma aversão profunda a configurações baseadas em XML. Com o Gradle, eu esperava que escrever scripts
bind seria muito fácil. Infelizmente, minhas esperanças e motivação diminuíram diminuíram a cada vez. O Gradle busca a
flexibilidade e sacrifica a automação e a qualidade por isso. Desenvolvedores seguem cegamente a tendência Os
desenvolvedores seguem cegamente a tendência sem levar em conta o impacto na confiabilidade do software. Para tornar o
Gradle Build scripts simples e de baixa manutenção requer uma forte disciplina. Tal disciplina já é rara em código fonte
e, portanto, é ainda mais rara nos scripts de construção.

### Traduções e soluções alternativas - Quando os scripts de compilação se tornam um desafio

O Gradle não funciona de forma muito diferente no fundo do que o Maven. Por conseguinte, são necessárias algumas
traduções. Recursos como o Catálogo de Dependências, o Plugin de Lançamento do Maven, o Dependabot e muitos outros são,
na verdade, soluções alternativas para funções básicas funções básicas que o Maven já traz. Com a flexibilidade do
Gradle, muitas vezes vêm configurações de construção complexas, que são difíceis de manter. Os plugins do Gradle muitas
vezes têm problemas de compatibilidade, limites ou avanços limitados. Estes problemas surgem devido à natureza evolutiva
do ecossistema Gradle, à diversidade dos ambientes em que o Gradle é usado e à implementação e é usado, e a
implementação específica e o esforço de manutenção necessário para cada plugin. Tudo está interligado.

### O efeito dominó do Gradle - Um cenário de pesadelo no mundo real

Já vi muitos microsserviços que tinham apenas alguns anos e já não eram passíveis de manutenção devido ao Gradle. devido
ao Gradle. É importante mencionar que esta não é a primeira vez que vejo algo assim, e não, eles não eram
desenvolvedores juniores. Minha **tarefa era fazer um upgrade do Spring Boot 2.x para o 2.7**. Spoiler: Desisti ao fim
de um ano Eu desisti! Os problemas em resumo: * O arquivo de compilação do Gradle requer -> Downgrade da minha versão
local do Java para 11 (WTF) (Normalmente o Java é  compatível com downward - mais uma vez, existem ferramentas de
contorno como o SdkMan...) * A atualização do Spring Boot requer -> Atualização do Gradle (WTF) * A atualização do
Gradle requer -> Atualização do plugin * A atualização do plugin requer -> Atualização do Groovy (WTF) * A actualização
do Groovy requer -> Actualização da estrutura de testes e dos testes (WTF) * A actualização da estrutura de teste requer
-> Actualizações de dependências. * \[...]  Além disso, alguns plugins não funcionam com as versões mais recentes do
Gradle, alguns já não são desenvolvidos, alguns são incompatíveis com outras versões do Gradle, alguns já não são
desenvolvidos, alguns são incompatíveis com outras versões do Gradle.  são incompatíveis com outros plugins, funcionam
apenas com Gradle KTS, não com Gradle Groovy, ou simplesmente têm  simplesmente têm limites. Mesmo os plugins de
grandes fornecedores como Spring têm funcionalidade limitada em comparação com seus plugins Maven.  funcionalidade
limitada. Acabo por ter um ficheiro de compilação do Gradle curto e porreiro que ninguém consegue manter,  nem mesmo os
programadores que o escreveram, e eles continuam a adorar o Gradle. Eu conheço muito poucas pessoas que  entendem os
scripts do Gradle e os escrevem a sério.

### Redescobrindo o poder do Maven - Aproveitando a magia do Maven

Eis as minhas características favoritas do Maven: Os plug-ins podem ser iniciados e configurados directamente a partir
da linha de comandos sem ter de os definir previamente. Os plugins não precisam de ser definidos. Além disso, eles são
amplamente independentes de outras configurações de plugins. | Exemplo Comando | Descrição | Link | |------------------
---------------------|--------------------------------------------------------------------------------------------------
-------------------------------------------------------------------|----------------------------------------------------
----------------------| | Atualizar versões - quem precisa do Dependabot? Sim, os meus projectos foram actualizados para
a versão mais recente durante anos sem quaisquer problemas e sem pedidos de fusão irritantes |
https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html | | `mvn versions:set -DnewVersion=1.0.0` |
Definir a versão do projeto...
| https://www.mojohaus.org/versions/versions-maven-plugin/index.html | | `mvn license:add-third-party` | Lista as
dependências e mostra suas licenças (pode falhar mesmo se as licenças forem excluídas) |
https://www.mojohaus.org/license-maven-plugin/index.html | Esta lista poderia continuar para sempre. Ela me lembra um
pouco as etapas do fluxo de trabalho do GitHub.
![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)

### Não gostas de XML?

Não tem problema! Basta escrever seu arquivo de compilação em `ruby`, `groovy`, `scala`, `yaml`, `atom` ou `Java`. A
extensão Polygot Extension (https://github.com/takari/polyglot-maven) torna isso possível. Para experimentá-la
simplesmente execute `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` e em
poucos milissegundos seu arquivo de compilação estará milissegundos o seu ficheiro de compilação é traduzido. É uma pena
que não exista um tradutor Maven <> Gradle fiável. :( Sim, os ficheiros de compilação Maven são grandes, mas também
muito fáceis de compreender. Refinamentos ou depuração são feitos num instante. Feito.

### A idade é apenas um número - a estabilidade e a evolução do Maven

É certo que o Maven já existe há bastante tempo e que a sua estética pode não corresponder aos padrões actuais. No
entanto, a longevidade do Maven permitiu-lhe adaptar-se e evoluir. O Maven funciona de forma independente do seu
projecto. Os ficheiros de compilação podem ser facilmente reutilizados. Os plug-ins são executados numa sandbox e são
independentes uns dos outros e da versão Java ou Maven. Este design promove a estabilidade e a previsibilidade e
facilita a gestão de processos de compilação complexos sem conflitos inesperados. conflitos inesperados.

### Fazit

Actualmente, o ambiente de desenvolvimento está sobrecarregado com muitas tarefas e tecnologias para os programadores.
Na busca simplicidade e automação, o Gradle surgiu como uma ferramenta de construção moderna, mas trouxe seus próprios
desafios com ele. Sem dúvida, o conceito do Gradle é bom! Mas dada a complexidade e o tempo investido nos scripts de
construção do Gradle, surge a questão de saber se não seria mais simples estender o Maven. alargado. Com plugins e
extensões, o Maven pode ser sempre actualizado e simplificado. Será que um Não seria muito mais interessante e
sustentável continuar a desenvolver do que saltar de uma tecnologia para outra?

### Ligações

* [Voltando do Gradle para o maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### Contacto

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
