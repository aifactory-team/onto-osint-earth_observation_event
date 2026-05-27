# 2026-05-27 분석 보고서

## 신규 소스 중요도 평가

| 소스 ID | 제목 | 태그 | 중요도 | 근거 |
|---------|------|------|--------|------|
| src-013 | 압록강 신교량 세관시설 건설 (38 North) | new | **중간** | KP 인프라 건설, WorldView-3 0.31m, 38 North 분석, koreaBoost |
| src-014 | 두만강 교량 완공 임박 (38 North + RFA) | new | **중간** | KP/RU 국경, PlanetScope, 38 North+RFA 교차, koreaBoost |
| src-015 | TROPOMI 훙가통가 메탄 파괴 검출 (Nature Communications) | new | **높음** | Sentinel-5P TROPOMI, 동료 심사 논문, 신규 기후 메커니즘 발견 |
| src-001 | Kilauea Ep48 5/27-29 window 확대 | update | **높음** | 분출 임박(예보 창 확대), USGS HVO 공식, 열적외 전조 지속 |
| src-002 | Santa Rosa 97% 진압 | update | **중간** | 87%→97%, mop-up 단계 종료 임박 |
| src-003 | 캐나다 산불 지속 | update | **높음** | 대피 확대 지속, 5위성 교차검증, 재해 우선순위 |
| src-004 | Bismarck Sea day19+ | update | **높음** | NASA EO 지속 보도, 부석 확산, 항해 위험 |
| src-005 | Mayon Day141+ | update | **중간** | PHIVOLCS AL3, 스트롬볼리안 지속, PDC 위험 |
| src-006 | Kanlaon post-explosion | update | **중간** | 5/26 폭발 후속, PHIVOLCS AL2 유지 |
| src-007 | Bezymianny FL100 | update | **낮음** | VAAC 유지, 완화 추세 |
| src-008 | Great Sitkin SAR | update | **낮음** | AVO WATCH 유지, 변화 미미 |
| src-009 | Shishaldin SO2 | update | **낮음** | AVO ADVISORY 유지, 변화 미미 |
| src-010 | Dukono 190/일 | update | **낮음** | VAAC Darwin 유지, 변화 미미 |
| src-011 | Kharg Island 유출 | update | **중간** | 3위성 교차검증, 유출 확산 |
| src-012 | Antelope Reef | update | **낮음** | AMTI 지속, 변화 미미 |
| src-016 | Bellingcat 남레바논 | update | **중간** | PlanetScope before/after 업데이트 |

## 도메인별 흐름 분석

### Disaster (자연재해) — 11건 업데이트

- **산불:** 캐나다 산불 31일+ 지속, 대피 확대. Santa Rosa 97% 진압 — 추적 종료 임박.
- **화산:** 8기 화산 동시 모니터링 유지(Kilauea, Bismarck Sea, Mayon, Kanlaon, Bezymianny, Great Sitkin, Shishaldin, Dukono). Kilauea Ep48 예보 창 5/27-29 확대 — 분출 임박. Bismarck Sea day19+ 부석 확산. Mayon Day141+.
- **주요 신호:** Kilauea Ep48 5/27-29 창 내 분수분출 개시 가능성. 다음 사이클 WARNING/RED 가능.

### Human Activity (인간활동) — 3건 (신규 2 + 업데이트 1)

- **건설:** 압록강 신교량 세관시설 건설(KP, WorldView-3, 38 North). 두만강 교량 완공 임박(KP/RU, PlanetScope, 38 North+RFA). 대북 제재 회피 우려 — 전략적 함의.
- **유출:** Kharg Island 원유 유출 확산 지속(Sentinel-1/2/3 3위성 교차검증).

### Climate & Environment (기후·환경) — 1건 신규

- **메탄:** TROPOMI 훙가통가 화산 플룸 메탄 파괴 검출. 2022년 분출 후 성층권 수증기 주입 → OH 라디칼 증가 → 메탄 분해 촉진. 화산 분출이 온실가스에 미치는 반직관적(메탄 감소) 효과 최초 검증. Nature Communications 동료 심사.
- 캐나다 산불 56Mt 탄소 방출 지속(교차 참조, Disaster→Climate).

### Agriculture & Maritime (농업·해양) — 0건 신규

- 금일 신규 없음. 기존 추적 항목 유지.

### Defense (국방·안보) — 1건 업데이트

- 남중국해 Antelope Reef 건설 지속(AMTI, WorldView-3). Bellingcat 남레바논 PlanetScope 업데이트.

## 온톨로지 변경 요약

- 새 Event: 3건 (압록강 세관, 두만강 교량, 훙가통가 메탄)
- 새 Location: 2건 (ent-loc-069 Yalu River Bridge, ent-loc-071 Tumen River Bridge)
- 스키마 구조 변경: 없음
- 새 클래스/관계: 없음

## 추론 결과 요약

- korea_geo_focus: 2건 (temp-evt-1601, temp-evt-1602 — 한반도 GeoFocus 복귀)
- sensor_capability_match: 3건 (WV-3 hiResBoost, TROPOMI tracegasBoost, S1 sarBoost)
- official_source_trust: 4건 (USGS HVO, PHIVOLCS, Nature Comms+ESA, NASA EO)
- analyst_org_trust: 2건 (38 North x2)
- temporal_progression: 4건 (Kilauea Ep48, Canada 31일+, Bismarck day19+, Mayon 141일+)
- multi_satellite_confirmation: 2건 유지 (Canada 5위성, Kharg 3위성)
- before_after_credibility: 2건 (WV-3 압록강, PlanetScope 두만강)
- 한반도 GeoFocus: 2건 신규 (전일 0건에서 복귀)
