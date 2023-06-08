---
title: "```Maven로 돌아가시겠습니까?```"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "# 마븐의 힘에 대한 재발견과 단순성 탐구의 어려운 여정"
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# Maven으로 돌아가기?

```
[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)


``` 

위의 마크다운 텍스트를 한국어로 번역합니다.

## Gradle 10주년. 편의성을 찾아 떠난 여정, Maven의 강점 재발견.

마크다운 텍스트를 번역하세요.

### 개발자의 잠재력 극대화 - 시간을 절약하는 도구들이 필요합니다

나는 종종 간과되거나 드물게 논의되지 않는 주제에 관심이 있습니다. 종종 멋진 기술이 사용되지만, 그와 관련된 문제에 대해 거의 언급되지 않습니다. 개발은 현재 매우 복잡해졌습니다. "서버리스", "로우 코드",
"인프라 코드화", "빅 데이터", "클라우드", "데브옵스", "당신이 만든 것은 당신이 운영한다" 등과 같은 멋진 용어로 인해 개발자들은 이미 너무 많은 추가 업무를 처리해야 합니다. 더 많은 작업은 전문가가
거의 없다는 것을 의미하며 항상 초점이 잘못 맞춰지는 것을 의미합니다. 따라서 자동화와 시간 절약은 매우 중요합니다. "생각하지 마세요"와 "상자에서 바로 작동"은 이미 좋은 품질 기준입니다. Gradle에서는 아직
이런 것을 볼 수 없습니다. 공정하게 말하면, Gradle은 우리가 일을 쉽게 할 수 있도록 도와주는 유일한 현대적인 도구가 아닙니다.

### 환상적인 단순함과 자동화 탐구

SOAP 이후로 XML 기반 구성에 대한 깊게 뿌리박힌 혐오감이 생겼습니다. Gradle을 사용하면 바인드 스크립트 작성이 매우 쉬울 것으로 예상되었지만, 내 기대와 동기는 점점 줄어들고 있습니다. Gradle은
유연성에 초점을 두고 있으며, 자동화와 품질을 희생하고 있습니다. 개발자들은 소프트웨어 신뢰성에 대한 영향을 고려하지 않고 트렌드를 따르고 있습니다. Gradle 빌드 스크립트를 간단하고 유지보수하기 위해서는 강력한
디시플린이 필요합니다. 그러나 이러한 디시플린은 소스 코드에서도 드물게 발견되며 빌드 스크립트에서는 더욱 드물게 발견됩니다.

### 번역 및 해결 방법 - 빌드 스크립트가 도전이 되는 경우

Gradle는 Maven과 거의 차이가 없이 백그라운드에서 작동합니다. 따라서 몇 가지 번역이 필요합니다. 의존성 카탈로그, Maven 릴리스 플러그인, Dependabot 등의 기능은 사실 Maven이 이미 갖고
있는 기본 기능들에 대한 해결책입니다. Gradle의 유연성으로 인해 복잡한 빌드 구성이 자주 발생하며, 이는 유지 관리하기 어려울 수 있습니다.  Gradle 플러그인은 종종 호환성 문제, 제한 또는 한계적인
발전을 겪을 수 있습니다. 이러한 문제들은 Gradle 생태계의 발전하는 성격, Gradle이 사용되는 다양한 환경, 각 플러그인마다 필요한 구현 및 유지 관리 비용 때문에 발생합니다. 모든 것이 서로 연결되어
있습니다.

### Gradle의 도미노 효과 - 현실 세계에서의 악몽 시나리오

나는 Gradle 때문에 유지보수가 어려워져서 오직 몇 년밖에 안된 Microservices를 많이 본 적이 있다. 이것이 내가 이런 일을 본 것이 처음이 아니고, 그리고 이들은 Junior Devs가 아니다.

제 **임무는 Spring Boot 2.x에서 2.7로 업그레이드하는 것**이었다. 스포ILER: 나는 1 년 후에 기권했다! 간단히 말해 문제점:

* Gradle 빌드 파일 -> 로컬 Java 버전 11로 다운그레이드 필요 (WTF) (일반적으로 Java는 하위 호환성이 있으며 SdkMan과 같은 Workaround Tools도 있다...)
* Spring Boot 업데이트 -> Gradle 업데이트 필요 (WTF)
* Gradle 업데이트 -> 플러그인 업데이트 필요
* 플러그인 업데이트 -> Groovy 업데이트 필요 (WTF)
* Groovy 업데이트 -> 테스트 프레임워크 및 테스트 업데이트 필요 (WTF)
* 테스트 프레임워크 업데이트 -> 종속성 업데이트 필요
* \[...]
또한 일부 플러그인은 최신 Gradle 버전에서 작동하지 않거나 더 이상 개발되지 않으며, 다른 플러그인과 호환되지 않으며, Gradle KTS로만 작동하거나 Gradle Groovy로는 작동하지 않거나 제한이 있는 경우도 있다. Maven 플러그인과 비교하여 대형 공급 업체의 플러그인도 기능이 제한되어 있다. 마지막에는 아무도 올바르게 유지 보수 할 수 없는 멋진 짧은 Gradle 빌드 파일이 남았다. 심지어 이것을 쓴 개발자들도 여전히 Gradle을 좋아한다. Gradle 스크립트를 진정으로 이해하고 작성할 수 있는 사람은 몇 명밖에 모르겠다.

### Maven의 강점 재발견 - Maven의 요술같은 능력 활용

여기엔 Maven의 내가 좋아하는 기능들이 있습니다:
플러그인은 미리 정의 할 필요없이 명령줄에서 직접 시작하고 구성 할 수 있습니다. 또한 다른 플러그인 구성과 대부분 독립적입니다.

| 예시 명령어                            | 설명                                                                                                                                                            | 링크                                                                     | 
|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `mvn versions:use -latest-versions`   | 의존성 업데이트- Dependabot이 필요한가요? 네, 몇 년 동안 내 프로젝트들은 성가신 병합 요청 없이 최신 버전으로 문제없이 업데이트되었습니다. | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0` | 프로젝트 버전 설정...                                                                                                                                         | https://www.mojohaus.org/versions/versions-maven-plugin/index.html       |
| `mvn license:add-third-party`         | 종속성을 나열하고 그들의 라이선스 보기 (제외 된 라이선스에서도 실패 할 수 있음)                                                                          | https://www.mojohaus.org/license-maven-plugin/index.html                 | 

이 목록은 계속될 수 있습니다. 그것이 GitHub Workflow 단계를 어떻게 생각나게 합니다.

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)
```

### 니가 XML을 좋아하지 않다고?

문제 없이!  `ruby`,`groovy`,`scala`,`yaml`,`atom` 또는 `Java`로 Build 파일을 작성하세요. Polygot Extension (https://github.com/takari/polyglot-maven)를 사용하면 가능합니다. 시도해보려면
`mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` 를 실행하면 몇 밀리 초 만에 Build 파일이 번역됩니다. 안타깝게도 신뢰성있는 Maven <-> Gradle 번역기가 없습니다 :(
네, Maven Build 파일은 큽니다. 그러나 이해하기 쉽습니다. 변경 사항 또는 디버깅은 순식간에 처리됩니다.

### 나이는 단지 숫자에 불과합니다 - Mavens의 안정성과 진화

물론 Maven은 상당히 오래되었고 그 에스테틱스는 현재의 표준에 부합하지 않을 수도 있습니다. 그러나 Maven의 지속성은 적응하고 발전할 수 있게 만들었습니다. Maven은 프로젝트와 독립적으로 작동합니다. 빌드
파일은 쉽게 재사용할 수 있습니다. 플러그인은 샌드박스에서 실행되며 Java 또는 Maven 버전과 상관없이 독립적으로 작동합니다. 이러한 디자인은 안정성과 예측 가능성을 촉진하며 예기치 않은 충돌 없이 복잡한 빌드
프로세스를 관리하기 쉽게 만듭니다.

### 결론

지금은 개발자를 위한 다양한 작업과 기술들이 개발 환경을 과부하시키고 있다. 단순함과 자동화를 추구하며 현대적인 빌드 도구로 등장한 Gradle은 자체적인 문제를 안고 있다. 의심할 여지 없이, Gradle의 개념은
좋다! 하지만, Gradle 빌드 스크립트에 투자되는 복잡성과 시간을 고려할 때, Maven을 확장하는 것이 더 단순하지 않을까? 플러그인과 확장 기능을 통해 Maven은 언제든지 새롭고 간단하게 유지될 수 있다.
기술을 옮기는 대신 지속적으로 개발하여 진보하는 것이 더욱 흥미롭고 지속가능할 것이다!

### 링크

* [Gradle에서 Maven으로 돌아가기](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### 연락처

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
