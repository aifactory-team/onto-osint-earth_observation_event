# 2026-05-21 온톨로지 분석 (Phase 3)

## 분석 요약

금일 Phase 3 온톨로지 추론에서 신규 이벤트 1건, 주요 업데이트 1건을 처리했다.

### 신규 이벤트

| ID | 이벤트 | 도메인 | 위성/센서 | 신뢰도 | 핵심 추론 |
|----|--------|--------|----------|--------|----------|
| ent-evt-1201 | Santa Rosa Island Fire (CA) | Disaster/wildfire | Landsat 9 OLI | 0.95 | officialBoost(NASA EO), baCredibility, priorityBoost |

### 주요 업데이트

| ID | 이벤트 | 변경 사항 | 신뢰도 |
|----|--------|----------|--------|
| evt-1101-series | Canadian wildfire smoke transatlantic | CAMS 확인: 연기 그리스/동지중해 도달(~9,000m). TROPOMI+OMPS+EarthCare 3위성 교차검증. 56Mt 탄소(역대 2위). | 0.97 (cap) |

### 업데이트 유지 (변경 없음)

- **evt-202 (Kilauea Ep48):** ADVISORY/YELLOW 유지. 9.5 urad, 5/22-26 예보 창.
- **evt-701 (Bismarck Sea):** 부석 뗏목 70km²+, 열수분출 지속.
- **evt-203 (Great Sitkin), evt-204 (Shishaldin), evt-082 (Mayon), evt-801 (Bezymianny), evt-504 (Ibu):** 활성 화산 추적 유지.
- **evt-501 (Everglades), evt-125 (Pemex), Kharg Island:** 추적 유지.
- **남중국해, NK 시설, 북극 해빙, Hektoria, Amazon Xingu, 동해 어선:** 추적 유지.

## 온톨로지 변경

- 신규 인스턴스: Location 1건 (ent-loc-070), Event 1건 (ent-evt-1201)
- 스키마 구조 변경: 없음
- 신규 클래스/관계: 없음

## 추론 통계

- 추론 트리플: 7건
- 적용 규칙: 6종 (multi_satellite_confirmation, official_source_trust, before_after_credibility, disaster_severity_priority, sensor_capability_match_tracegas, cross_domain_inference)
- multiSatBoost 대상: 1건 (evt-1101-series TROPOMI+OMPS+EarthCare)
- officialBoost 대상: 2건 (evt-1201 NASA, evt-1101-series CAMS)
- crossDomainLink: 1건 (Canadian smoke: Disaster -> Climate)

## 지식그래프 통계

- 누적 KG 트리플: 1,284건 (전일 1,263 -> +21)
- 신규 노드: 2건 (ent-loc-070, ent-evt-1201)
- 신규 엣지: 14건 (explicit)
- 추론 엣지: 7건
- 업데이트 엣지: 2건

## 도메인 커버리지

| 카테고리 | 금일 신규 | 추적 중 |
|----------|----------|--------|
| 자연재해 (Disaster) | 1건 (Santa Rosa Fire) | Kilauea, Bismarck, Mayon, Great Sitkin, Shishaldin, Bezymianny, Ibu, Everglades |
| 인간활동 (HumanActivity) | 0건 | Pemex, Kharg Island, 남중국해, NK 시설 |
| 기후/환경 (ClimateEnvironment) | 업데이트 1건 (Canadian smoke cross-domain) | 북극 해빙, Hektoria, UNEP MARS, Tanager-1 |
| 농업/해양 (AgricultureMaritime) | 0건 | 동해 어선, Amazon Xingu |

4개 카테고리 모두 기존 추적 항목 유지 중. 인간활동/농업해양 금일 신규 없음.
