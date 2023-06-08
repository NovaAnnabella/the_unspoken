---
title: "```
Maven에 다시 돌아가기?
```"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "# 마븐의 권력 재발견을 위한 짧은 여행과 간결함을 찾아 나아가는 어려운 탐색"
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# 메이븐으로 돌아가기?

```
[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)
``` 

위의 마크다운 텍스트를 한국어로 번역합니다.

## 10년간 Gradle: 편의성 탐구와 메이븐의 강점 재발견을 향한 짧은 여행.

마크다운 텍스트를 한국어로 번역하세요:  ```

### 개발자들의 잠재력 극대화 - 더 많은 시간을 절약할 수 있는 도구가 필요합니다

내가 관심을 가지는 것은 자주 간과되거나 드물게 논의되지 않는 주제들이다. 종종 멋진 기술들이 사용되지만, 연관된 문제들에 대해 거의 언급되지 않는다. 개발은 요즘 매우 복잡해졌다. "서버리스", "로우 코드",
"IaC", "빅 데이터", "클라우드", "데브옵스", "You Build it You run it"와 같은 멋진 버즈워드들은 이미 개발자들에게 충분한 추가적인 일들을 부여했다. 더 많은 일은 전문가가 거의 없다는
것을 의미하며, 항상 초점을 놓치는 것이다. 따라서 자동화와 시간 절약은 매우 중요하다. "생각하지 마세요"와 "포장러닝"은 이미 좋은 품질 기준이다. Gradle에서는 아직 이러한 기준을 볼 수 없다. 공정하게
말하면, Gradle은 일을 쉽게 해주는 대신 일을 만들어내는 모던한 도구들 중 하나일 뿐이다.

### 간단함과 자동화를 위한 환상의 탐구

Seit SOAP habe ich eine tief verwurzelte Abneigung gegen XML-basierte Konfigurationen. Mit Gradle hatte ich gehofft,
dass das Schreiben von Bind-Skripten ein Kinderspiel sein würde. Leider wurden meine Hoffnungen und meine Motivation von
Mal zu Mal geringer. Gradle strebt nach Flexibilität und opfert dafür Automatisierung und Qualität. Entwicklerinnen und
Entwickler folgen blind dem Trend ohne Rücksicht auf die Auswirkungen auf die Zuverlässigkeit der Software. Um Gradle Build Skripte einfach und wartungsarm zu halten, bedarf es einer starken Disziplin. Eine solche Disziplin ist schon im Quellcode selten zu finden und daher ist sie in den Build-Skripten noch viel seltener.

### 번역과 워크어라운드 - 빌드 스크립트가 도전이 되는 경우

Gradle는 Maven과 별반 다르지 않게 백그라운드에서 작동합니다. 그러므로 일부 번역이 필요합니다. 의존성 카탈로그, Maven 릴리스 플러그인, Dependabot 등의 기능은 실제로 Maven이 이미 갖춘
기본 기능에 대한 해결책입니다. Gradle의 유연성으로 인해 종종 복잡한 빌드 구성이 생성되며, 이는 유지 관리하기 어렵습니다. Gradle 플러그인은 종종 호환성 문제, 제한 사항 또는 제한된 개발 진행률을
가지고 있습니다. 이러한 문제는 Gradle 생태계의 발전하는 성격, Gradle이 사용되는 다양한 환경 및 각 플러그인의 구현 및 유지 관리 비용에 따라 발생합니다. 모두 서로 연결되어 있습니다.

### Gradle의 도미노 효과 - 현실 세계에서의 악몽 시나리오

저는 몇 년만에 Gradle 때문에 유지보수가 불가능해진 많은 Microservice를 보았습니다. 이러한 상황을 처음 본게 아니며 그것들은 주니어 개발자가 만든 것이 아닙니다.

**내 작업은 Spring Boot 2.x에서 2.7으로의 업그레이드였습니다**. 스포일러: 1년 후에 포기했습니다! 간단히 말하면 문제점은 다음과 같습니다:

* Gradle 빌드 파일에서 -> 내 로컬 Java 버전을 11로 다운그레이드해야함 (WTF) (보통 Java는 하위 호환성을 제공하기 때문에 SdkMan과 같은 Workaround-도구도 있겠네요...)
* Spring Boot 업데이트에서 -> Gradle 업데이트 필요 (WTF)
* Gradle 업데이트에서 -> Plugin 업데이트 필요
* Plugin 업데이트에서 -> Groovy 업데이트 필요 (WTF)
* Groovy 업데이트에서 -> Test framework와 Test 업데이트 필요 (WTF)
* Test framework 업데이트에서 -> Dependency 업데이트 필요
* \[...\]
  또한 일부 플러그인은 최신 Gradle 버전과 호환되지 않거나 더 이상 개발되지 않거나 다른 플러그인과 호환되지 않거나 
  Gradle KTS로만 작동하고 Gradle Groovy로 작동하지 않거나 제한이 있습니다. Spring과 같은 대규모 공급자의 플러그인
  조차도 그들의 Maven 플러그인과 비교하여 기능이 제한됩니다.결국, 나는 아무도 제대로 유지 보수 할 수 없는 멋진 짧은
  Gradle 빌드 파일을 만들었으며, 심지어 그것을 만든 개발자들마저도 Gradle을 여전히 좋아합니다.
  Gradle 스크립트를 진지하게 이해하거나 작성 할 수있는 사람은 몇 없습니다.

### 메이븐의 강점 재발견 - 메이븐의 마법력 활용하기

여기는 메이븐의 내가 좋아하는 기능 목록입니다:
플러그인은 미리 정의할 필요 없이 명령 줄에서 직접 시작 및 구성할 수 있습니다. 게다가, 그들은 다른 플러그인 구성과 거의 독립적입니다.

| 예시 명령어                             | 설명                                                                                                                                                                                                | 링크                                                                     |
|----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `mvn versions:use -latest-versions`   | 버전 업데이트 - Dependabot이 필요한가요? 예, 내 프로젝트는 누구와도 충돌 없이 몇 년 동안 최신 버전으로 문제없이 업데이트되었습니다. 불편한 병합 요청 없이! | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0` | 프로젝트 버전 설정...                                                                                                                                                                                 | https://www.mojohaus.org/versions/versions-maven-plugin/index.html       |
| `mvn license:add-third-party`         | 종속성을 나열하고 라이선스를 표시합니다 (제외된 라이선스에서 실패 할 수 있음)                                                                                                                                                                                                                 | https://www.mojohaus.org/license-maven-plugin/index.html                 | 

이 목록은 끝없이 계속될 수 있습니다. 그것은 어떤 방식으로는 GitHub Workflow Steps를 생각나게 합니다.

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)

### XML을 좋아하지 않습니까?

문제 없어요! 단지 `ruby`, `groovy`, `scala`, `yaml`, `atom` 또는 `Java`로 Build File 을 작성해주시면 됩니다. Polygot
Extension (https://github.com/takari/polyglot-maven) 덕분에 가능합니다. 시도해 보려면
단지 `mvn io.takari.polyglot:polyglot-translate-plugin: translate -Dinput=pom.xml -Doutput=pom.yaml` 를 실행하면
몇 밀리 초 안에 Build File 이 번역됩니다. 유감스럽게도 믿을만한 Maven <> Gradle 번역기가 없네요 :(
맞습니다, Maven Build Files는 큽니다. 그러나 이해하기 쉬워요. 개선 또는 디버깅은 순식간에 완료됩니다.

### 나이는 숫자일 뿐 - 메이븐의 안정성과 진화

정말로, Maven은 꽤 오랜 시간 동안 존재하고 그 미적 감각은 현재 기준에 부합하지 않을 수도 있다. 그러나 Maven의 내구성은 맞춤화하고 발전할 수 있게 만들어줬다. Maven은 프로젝트와 독립적으로
작동한다. 빌드 파일은 간단하게 재사용될 수 있다. 플러그인은 샌드박스에서 실행되며 서로 독립적이며 자바나 Maven 버전과도 독립적이다. 이러한 디자인은 안정성과 예측 가능성을 촉진하며 예상치 못한 충돌 없이
복잡한 빌드 프로세스를 관리하기 쉽게 만든다.

### 결론

지금은 개발자들을 위한 여러 가지 작업과 기술로 인해 개발 환경이 과부하입니다. 간편함과 자동화를 추구하면서도, Gradle은 최신 빌드 도구로 등장했지만, 고유의 문제점을 가지고 있습니다. 의심할 여지없이
Gradle의 개념은 좋습니다! 그러나 Gradle 빌드 스크립트에 투자되는 복잡성과 시간을 고려하면 Maven을 확장하는 것이 더 쉬울지 생각해봐야 합니다. 플러그인과 확장 기능을 사용하여 Maven을 언제든지
업그레이드하고 간소화할 수 있을 것입니다. 기술에서 기술로 뛰어가는 것보다 계속해서 발전시키는 것이 더 흥미롭고 지속 가능하지 않을까요?

### 링크

* [Gradle에서 Maven으로 돌아가기](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### 연락처

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
