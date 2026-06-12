# Phase 4 보고서 기반 — 2026-06-12

## 보고서 포함 이벤트 (Include)

### 1순위: 자연재해 (인명피해 우선)

#### [NEW] evt-3201: 민다나오 M7.8 지진 위성 피해 평가
- **우선순위**: 최고 -- 인명피해(47+ 사망) 동반 자연재해
- **온톨로지 의의**: phen-earthquake 첫 실제 이벤트 (mention_count 0->1, 파이프라인 마일스톤)
- **위치**: Sarangani, Mindanao, Philippines (5.9N, 125.3E)
- **규모**: M7.8, 47+ 사망, 12,600+ 가옥 손상/파괴
- **위성 관측**: PhilSA VIIRS 야간 조명 before/after
- **국제 대응**: Sentinel Asia 발동 (EQ-2026-000083-PHL)
- **신뢰도**: 0.97 (cap) -- officialBoost(PhilSA+Sentinel Asia) + priorityBoost + baCredibilityBoost
- **후속 예상**: Sentinel-1 InSAR 공동변위 분석 (M7.8 규모, 표준 절차)
- **새 기관**: PhilSA (Philippine Space Agency)
- **새 위치**: Sarangani, Mindanao
- **Mermaid 방향**: evt-3201 -> phen-earthquake (첫 매핑), evt-3201 -> sat-viirs-jpss, evt-3201 -> org-philsa
- **보고서 섹션**: 1.1 (최상위)

#### [UPDATE] evt-202: Kilauea Ep49 D-Day 예보 창 개시
- **우선순위**: 높음 -- 금일 예보 창 진입
- **핵심 업데이트**: 6/12부터 분출 가능. 가장 유력 6/13-14.
- **시계열**: Ep44->Ep45->Ep46->Ep47->Ep48->Ep49 (파이프라인 기간 내 최장 시리즈)
- **위성**: USGS HVO 공식
- **신뢰도**: 0.95
- **보고서 섹션**: 1.2

#### [UPDATE] evt-082: Mayon Day158+ 4km PDC
- **우선순위**: 높음 -- PDC(화쇄류) 4km 도달은 위험 격상
- **핵심 업데이트**: Day158+, AL3 유지, 287K 이재민, 4km PDC
- **위성**: Himawari-9 AHI 열적외
- **신뢰도**: 0.97 (cap)
- **보고서 섹션**: 1.3

#### [UPDATE] evt-701/evt-2903: Bismarck Sea 부석 해상 접근 차단
- **우선순위**: 높음 -- 인도주의 영향 격상 (해상 접근 차단)
- **핵심 업데이트**: Day35+, 마누스주 해상 접근 봉쇄, 어업 중단
- **위성**: 5위성 교차검증 (Sentinel-2 + Landsat-9 + MODIS + VIIRS + Himawari-9)
- **신뢰도**: 0.90
- **cascading**: 파이프라인 최장 35일 연쇄 재해
- **보고서 섹션**: 1.4

#### [UPDATE] evt-2802: Typhoon Jangmi 피해 평가
- **우선순위**: 중간 -- 피해 평가 완료 단계
- **핵심 업데이트**: Tokyo 홍수 동일 기상 시스템 cascading
- **위성**: Himawari-9 + GPM
- **신뢰도**: 0.90
- **보고서 섹션**: 1.5

#### [UPDATE] evt-1101: Canada Wildfire 65 Active
- **우선순위**: 중간 -- 65건 활성, CIFFC Level 2
- **위성**: 5위성 4기관 교차검증
- **신뢰도**: 0.85
- **보고서 섹션**: 1.6

#### [UPDATE] evt-203: Great Sitkin WATCH/ORANGE
- **우선순위**: 낮음 -- 상태 유지
- **위성**: Sentinel-1 SAR 용암돔
- **신뢰도**: 0.85
- **보고서 섹션**: 1.7

#### [UPDATE] evt-204: Shishaldin ADVISORY/YELLOW
- **우선순위**: 낮음 -- 상태 유지
- **위성**: TROPOMI SO2
- **신뢰도**: 0.80
- **보고서 섹션**: 1.8

### 2순위: 기후-환경

#### [UPDATE] temp-evt-1902: El Nino +0.9C 강화
- **우선순위**: 중간 -- 98% 확률, 강화 추세
- **핵심 업데이트**: Nino 3.4 지수 +0.9C, 강화 지속 전망
- **위성**: Jason-3 + Sentinel-6 해수면 고도계
- **신뢰도**: 0.95
- **보고서 섹션**: 2.1

### 3순위: 인간활동/농업-해양

(금일 신규 인간활동/농업-해양 이벤트 없음. 기보도 이벤트만.)

## 보고서 제외 이벤트 (Exclude)

| 이벤트 | 사유 |
|--------|------|
| evt-3101 (Russia tanks) | 6/11 보고 완료, tag=reported |
| evt-3102 (Brazil DETER) | 6/11 보고 완료, tag=reported |
| evt-3001 (GFM v4.1.1) | 6/11 보고 완료, tag=reported |

## 4대 카테고리 커버 상태

| 카테고리 | 커버 | 이벤트 |
|----------|------|--------|
| 자연재해 (Disaster) | O | evt-3201, evt-202, evt-082, evt-701, evt-2802, evt-1101, evt-203, evt-204 |
| 인간활동 (HumanActivity) | O | (기보도 evt-3101/3102만 해당, 금일 신규 없음 -- 보고서에 "금일 신규 없음" 명시) |
| 기후-환경 (Climate) | O | temp-evt-1902 |
| 농업-해양 (AgriMarine) | O | (El Nino 해양 SST 관련으로 교차 커버) |

## Mermaid KG 시각화 구조

```
evt-3201[Mindanao M7.8] --manifests--> phen-earthquake[earthquake_damage, 첫 매핑]
evt-3201 --observedBy--> sat-viirs-jpss[VIIRS]
evt-3201 --analyzedBy--> org-philsa[PhilSA]
evt-3201 --locatedIn--> ent-loc-sarangani[Sarangani, Mindanao]
evt-3201 --inCountry--> co-ph[Philippines]
evt-3201 --severity--> HIGH[47+dead, 12600+houses]

evt-202[Kilauea Ep49] --status--> D-Day[forecast window open today]
evt-082[Mayon Day158+] --status--> PDC_4km[escalation]
evt-701[Bismarck Sea] --cascading--> sea_access_blocked[humanitarian]
```

## 보고서 특이사항

1. **파이프라인 마일스톤**: phen-earthquake 첫 실제 이벤트. 스키마 초기화 이후 44일간 earthquake_damage는 정의만 있었고 실제 위성 검증 이벤트가 없었다. evt-3201이 이 gap을 최초로 채운다.

2. **Sentinel-1 InSAR 후속 예상**: M7.8 규모 지진은 Sentinel-1 InSAR 공동변위(coseismic deformation) 분석의 표준 대상. 6-12일 재방문 주기 내 데이터 수집 예상. 보고서에 "후속 관측 예고" 섹션 포함 권고.

3. **VIIRS 야간 조명 피해 평가**: PhilSA가 VIIRS 야간 조명 before/after 데이터를 지진 피해 평가에 활용한 것은 이 파이프라인에서 처음 기록되는 센서 활용 패턴. 통상 VIIRS는 산불/선박 탐지에 사용되나, 야간 전력 차단 패턴을 통한 구조물 피해 범위 추정은 독특한 적용 사례.

4. **한반도 GeoFocus**: 금일 신규 없음. 보고서에 "금일 한반도 신규 위성 관측 이벤트 없음" 명시 필요.
