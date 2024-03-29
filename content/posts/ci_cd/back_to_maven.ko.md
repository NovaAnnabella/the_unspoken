---
title: "Maven으로 돌아가기?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "반응하기 어려운 단순함을 찾는 데에 대한 탐색과 Maven의 힘을 재발견하는 짧은 여행."
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# Maven으로 돌아가기?

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

## 10년간의 Gradle. 경감을 찾아서와 Maven의 힘 재발견을 위한 짧은 여행.



### 개발자의 잠재력 극대화 - 우리는 더 많은 시간을 절약할 수 있는 도구가 필요합니다

나는 자주 무시되거나 드물게 논의되는 주제에 관심이 있다. 종종 멋진 기술들이 사용되지만, 그와 관련된 문제에 대해 이야기하는 사람은 거의 없다. 개발은 오늘날 매우 번거롭게 된 상태다. 멋진 다크워드들로
"서버리스", "로우 코드", "IaC", "빅 데이터", "클라우드", "데브옵스", "너 만들면 너 가동해" 등으로 개발자들은 이미 충분한 부가적인 일들을 다루고 있다. 추가적인 업무, 이는 전문가가 거의 없다는
것을 의미하며, 늘 무언가는 초점을 잃게 된다. 그래서 자동화와 시간 절약이 매우 중요하다. "나에게 생각하게 하지 마"와 "상자 밖에서 작동"은 이미 좋은 품질 표시이지만, 나는 아직 Gradle에서 그것을 볼 수
없다. 공정하게 말하자면, Gradle은 우리에게 작업을 만드는 유일한 현대적인 도구가 아니라, 대신 그것을 완화시킨다.

### 환상적인 단순화와 자동화에 대한 검색.

SOAP 이후로 나는 XML 기반의 설정에 대한 깊은 싫증을 가지고 있습니다. Gradle을 통해 Bind 스크립트 작성이 어린아이의 놀이처럼 될 것이라고 생각했습니다. 하지만, 희망과 동기는 점점 줄어들었습니다.
Gradle은 유연성을 추구하면서 자동화와 품질을 희생합니다. 개발자들은 소프트웨어의 신뢰성에 미치는 영향을 고려하지 않고 트렌드를 맹목적으로 따릅니다. Gradle 빌드 스크립트를 간단하고 유지 관리하기 쉽게
하려면 강력한 규율이 필요합니다. 그러한 규율은 소스 코드에서도 드물게 찾을 수 있어 빌드 스크립트에서는 더욱 드물다고 할 수 있습니다.

### 번역 및 워크어라운드 - 빌드 스크립트가 도전이 될 때

Gradle은 배경에서 Maven과 크게 다르게 작동하지 않습니다. 따라서 몇 가지 번역이 필요합니다. Dependency Catalog, Maven Release Plugin, Dependabot 등의 기능은 사실
Maven이 이미 제공하는 기본 기능을 대체하기 위한 것입니다. Gradle의 유연성으로 인해 복잡한 빌드 구성이 자주 발생하며, 이는 유지 관리가 어렵습니다. Gradle 플러그인들은 종종 호환성 문제, 제한,
또는 제한된 추가 개발이 있습니다. 이런 문제들은 Gradle 생태계의 발전하는 특성, Gradle이 사용되는 다양한 환경, 그리고 각 플러그인에 대한 특정 구현 및 유지보수 노력 때문에 발생합니다. 모든 것이 서로
연결되어 있습니다.

### Gradle의 도미노 효과 - 실제 세계의 악몽 시나리오

저는 몇 년 전에 만들어진 많은 마이크로서비스를 봤는데, 벌써 Gradle 때문에 유지 보수할 수 없게 된 경우가 많았습니다. 이게 처음 본 일은 아니고, 그것들은 주니어 개발자들의 것이 아니었습니다.

제 **업무는 Spring Boot 2.x를 2.7로 업그레이드하는 것이었습니다**. 스포일러: 저는 1년 후에 포기했습니다! 문제점을 간략하게:

* Gradle 빌드 파일이 필요로 함 -> 내 로컬 Java 버전을 11로 다운그레이드 (WTF) (보통 Java는 하위 호환성이 있습니다. 여기에도 SdkMan 같은 워크어라운드 도구들이 있습니다.)
* Spring Boot 업데이트가 필요로 함 -> Gradle 업데이트 (WTF)
* Gradle 업데이트가 필요로 함 -> 플러그인 업데이트
* 플러그인 업데이트가 필요로 함 -> Groovy 업데이트 (WTF)
* Groovy 업데이트가 필요로 함 -> 테스트 프레임워크와 테스트 업데이트 (WTF)
* 테스트 프레임워크 업데이트가 필요로 함 -> 의존성 업데이트
* \[...]
  더욱이, 어떤 플러그인들은 새 버전의 Gradle과 동작하지 않고, 일부는 더 이상 개발되지 않거나, 다른 플러그인들과 호환되지 않거나, Gradle Groovy와 함께는 동작하지 않고 Gradle KTS와만 동작하거나, 단순히 제한이 있습니다. Spring과 같은 큰 제공업체의 플러그인조차도 Maven 플러그인에 비해서 기능상 제한이 있습니다. 결국, 제가 가진 것은 아무도 제대로 유지 보수할 수 없는 멋진 짧은 Gradle 빌드 파일이었습니다. 심지어 그것을 작성한 개발자조차도, 그들은 여전히 Gradle을 사랑합니다. 저는 Gradle 스크립트를 진정으로 이해하거나 쓸 수 있는 사람을 몇 명 뿐 압니다.

### Maven의 강점 재발견 - Maven의 마법적인 능력을 활용하다

다음은 Maven의 내가 좋아하는 기능들입니다:
플러그인을 먼저 정의하지 않고도 명령 행에서 직접 시작하고 구성할 수 있습니다. 게다가, 그들은 대부분 다른 플러그인 구성과 독립적입니다.

| 예제 명령                          | 설명                                                                                                                                                  | 링크                                                                     | 
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `mvn versions:use -latest-versions` | 버전 업데이트 - Dependabot이 필요한가요? 예, 내 프로젝트들은 수년 동안 문제없이 최신 버전으로 업데이트되었습니다, 성가신 병합 요청 없이 | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0` | 프로젝트 버전 설정...                                                                                                                               | https://www.mojohaus.org/versions/versions-maven-plugin/index.html       |
| `mvn license:add-third-party`       | 의존성 목록 및 해당 라이선스 표시 (제외된 라이선스에서 실패할 수도 있음)                                                                                  | https://www.mojohaus.org/license-maven-plugin/index.html                 | 

이 목록은 계속될 수 있습니다. 이것은 나에게 어떤 식으로든 GitHub 워크플로우 단계를 상기시킵니다.

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)


### 당신은 XML을 좋아하지 않나요?

문제 없어요! 당신의 빌드 파일을 `ruby`, `groovy`, `scala`, `yaml`, `atom` 또는 `Java`로 작성하면 됩니다. Polygot
확장 프로그램(https://github.com/takari/polyglot-maven)이 가능하게 해줍니다. 테스트하려면
`mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml`을 실행하면
당신의 빌드 파일이 몇 밀리 초 안에 번역됩니다. 안타깝게도 신뢰할 수 있는 Maven <> Gradle 번역기가 없다니 :(
네, Maven 빌드 파일은 크지만 매우 이해하기 쉽습니다. 수정 또는 디버깅은 순식간에
끝납니다.

### 나이는 그저 숫자일 뿐 - Mavens의 안정성과 진화

인정합니다, 메이븐은 이미 꽤 오래되었고 그 미학이 현재의 표준에 부합하지 않을 수 있습니다. 그러나 메이븐의 오랜 세월은 적응하고 발전하는 데 도움이 되었습니다. Maven은 프로젝트와 상관없이 독립적으로
작동합니다. 빌드 파일은 쉽게 재사용할 수 있습니다. 플러그인은 샌드박스에서 실행되며 각각 독립적이고 Java 또는 메이븐 버전에 영향을 받지 않습니다. 이런 디자인은 안정성과 예측성을 촉진하며 기대치를 벗어나지
않는 복잡한 빌드 프로세스를 관리하기 쉽게 만듭니다.

### 결론

요즘 개발 환경은 개발자를 향한 많은 업무와 기술로 장식되어 있습니다. 단순함과 자동화를 추구하며 Gradle이 현대적인 빌드 도구로 등장했습니다. 하지만 이 과정에서 독특한 과제들을 동반해왔습니다. 의심할 여지
없이 Gradle의 개념은 좋습니다! 그러나 Gradle 빌드 스크립트에 투자된 복잡함과 시간을 고려하면 Maven을 확장하는 것이 더 쉬울 수도 있다는 의문이 생깁니다. 플러그인과 확장 기능을 사용하면 Maven을
언제든지 새롭게 갱신하고 단순화시킬 수 있습니다. 기술에서 다음 기술로 설기를 하기보다 개선을 계속하는 것이 더 흥미롭고 지속 가능하지 않을까요?

### 링크

* [Gradle에서 Maven으로 돌아가기](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### 연락처

[GitHub 이슈](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
