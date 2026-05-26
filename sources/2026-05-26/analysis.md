# 2026-05-26 분석 보고서

## 신규 소스 중요도 평가

| 소스 ID | 제목 | 태그 | 중요도 | 근거 |
|---------|------|------|--------|------|
| src-001 | 캐나다 산불 Swan Hills 에스컬레이션 | update | **높음** | 인명피해+대피 확대(33,000+), 5위성 교차검증, 연기 유럽 도달, 재해 우선순위 |
| src-003 | Kilauea Ep48 예보 창 개시 | update | **높음** | 분출 임박(예보 창 5/25-26 활성화), USGS HVO 공식, 열적외 전조 |
| src-004 | Bismarck Sea 부석 70km² 200km+ | update | **높음** | 5위성 3기관, NASA EO 공식, 신규 섬 가능성, 해상 위험(항로 영향) |
| src-006 | Kanlaon 폭발적 분출 5/26 | new | **높음** | 새 폭발적 에피소드(기존 SO₂ 배출 수준에서 PDC + 화산재 2500m), PHIVOLCS |
| src-005 | Mayon AL3 PDC Day 140+ | update | **중간** | 140일 연속 분출 장기 시리즈, PDC 위험도 상존 |
| src-011 | Kharg Island 유출 확산 | update | **중간** | Sentinel-1/2/3 3위성 교차검증, 전쟁 상황 악화, 환경 영향 |
| src-012 | 남중국해 Antelope+Spratly | update | **중간** | 지정학적 중요, WorldView-3 + Planet Labs, CSIS AMTI 분석 |
| src-007 | Bezymianny VAAC#45 FL100 | update | **낮음** | 이전 FL300에서 FL100으로 감소(완화 추세) |
| src-002 | Santa Rosa 87% | update | **낮음** | 진압 거의 완료, 변동 없음 |
| src-008 | Great Sitkin | update | **낮음** | 상태 유지, 변화 미미 |
| src-009 | Shishaldin | update | **낮음** | 상태 유지, 변화 미미 |
| src-010 | Dukono | update | **낮음** | 상태 유지, 변화 미미 |
| src-016 | Sentinel-1D 4위성 완성 | new | **중간** | SAR 재방문 4일 달성, 모니터링 역량 구조적 강화 |

## 도메인별 흐름 분석

### Disaster (자연재해) — 11건
- **산불:** 캐나다 산불 에스컬레이션 최대 위기 — Swan Hills 12,000 신규 대피, SWF076 통제불능. Santa Rosa 87% 진압 거의 완료.
- **화산:** 활발한 8기 화산 동시 모니터링(Kilauea, Bismarck Sea, Mayon, Kanlaon, Bezymianny, Great Sitkin, Shishaldin, Dukono). Kanlaon이 폭발적 분출로 격상. Bezymianny는 FL100으로 완화 추세.
- **주요 신호:** Kilauea Ep48 예보 창 활성화 — 24-48시간 내 분수분출 가능. Bismarck Sea 부석 확산 지속(항해 위험 + 신규 섬 가능성).

### Human Activity (인간활동) — 1건
- **유출:** Kharg Island 원유 유출이 이란 분쟁 상황에서 확산 — Sentinel-1/2/3 3위성 교차검증 신규 확인.

### Climate & Environment (기후·환경) — 1건 (교차 참조)
- 캐나다 산불 56Mt 탄소 방출 + 연기 대서양 횡단 유럽 도달(CAMS 확인). Disaster→Climate 교차 도메인.

### Agriculture & Maritime (농업·해양) — 0건 신규
- 금일 신규 없음. 엘니뇨 전망(위성 미검증), Amazon 삼림벌채 추적 지속.

### Defense (국방·안보) — 1건 업데이트
- 남중국해 Antelope Reef 1,490ac + 필리핀 Spratly 건설 지속 확인(CSIS AMTI, WorldView-3, Planet Labs).

### Satellite Operations — 1건 신규
- Sentinel-1D 4위성 콘스텔레이션 완성. SAR 모니터링 글로벌 재방문 4일 달성.

## 온톨로지 변경 요약

- 새 Event: 2건 (Kanlaon 폭발적 분출, Sentinel-1D 4위성 완성)
- 새 Location: 0건
- 스키마 구조 변경: 없음
- 새 클래스/관계: 없음

## 추론 결과 요약

- multi_satellite_confirmation: 3건 (Canada 5위성, Bismarck 5위성, Kharg 3위성)
- temporal_progression: 4건 (Canada 30일+, Kilauea Ep48 창, Bismarck day18+, Kanlaon series)
- official_source_trust: 6건 (USGS HVO, NASA EO, PHIVOLCS x2, USGS AVO x2)
- sensor_capability: 3건 (Great Sitkin sarBoost, Kharg sarBoost, Kilauea thermalBoost)
- disaster_severity: 1건 (Canada 에스컬레이션)
- crossDomainLink: 2건 (Canada→Humanitarian, Canada→Climate)
- 한반도 GeoFocus: 0건 직접 이벤트
