# 2026-05-02 분석

## 신규 소스 중요도 평가

| 소스 | 이벤트 | 도메인 | 중요도 | 근거 |
|------|--------|--------|--------|------|
| src-001 | PNG 바이닝산맥 산사태 (TC Maila) | Disaster | **높음** | Landsat 9 전후비교, 25명 사망, Disaster Charter 발동 |
| src-007 | 전 세계 30+ 활화산 종합 현황 | Disaster | 중간 | 다중 화산 위성 모니터링 종합 — Mayon, Sheveluch, Sabancaya, Fuego, Merapi |
| src-011 | 남극 30년 접지선 후퇴 (ESA Sentinel-1) | Climate | **높음** | 12,800km² 빙하 손실, SAR 30년 데이터, 해수면 상승 기여 |
| src-013 | 상업 위성의 군사 전략 변화 | Defense | 중간 | MizarVision 관련 종합분석, Planet+Maxar 언급 |
| src-015 | 시칠리아 Niscemi 산사태 VHR 위성영상 | Disaster | **높음** | VHR 전후비교, 4km 산사태, 1,500명 대피 |
| src-016 | NASA 다중위성 조기 산림벌채 탐지 | HumanActivity | 중간 | 기술 혁신 — 100일 앞서 탐지 |
| src-018 | ESA Sentinel 3종 메탄 매핑 | Climate | 중간 | 다중위성 tiered 접근 기술 |

## 업데이트 항목 변경사항

| 이벤트 | 변경 | 출처 |
|--------|------|------|
| ent-evt-020 (조지아 산불) | NASA EO Landsat 8 위성영상 상세 공개, 50,000+ acres 확인, 120+ homes 파괴 확인 | src-004 |
| ent-evt-021 (Kilauea) | Episode 45 정리 (900ft 분수, 8.5h), Episode 46 예측 May 5-8, 11µrad tilt | src-006 |
| ent-evt-029 (Mayon) | Alert 3 유지, SO₂ 2,147 t/day, 3개 골짜기 용암 유출 지속 | src-023 |
| ent-evt-030 (Sheveluch) | 용암돔 성장 지속, 위성 열이상 관측, Aviation Orange | src-024 |
| ent-evt-032 (CAS500-2/4) | 발사 시각 확정: 5월 3일 06:59 UTC, Vandenberg SLC-4E | src-008 |

## 도메인별 흐름 분석

### Disaster (자연재해) — 가장 활발
- **신규:** PNG TC Maila 산사태(Landsat 9), Niscemi 시칠리아 산사태(VHR), 3개 중남미/인도네시아 화산
- **업데이트:** 조지아 산불(Landsat 8 확인), Kilauea Ep.46 예측, Mayon 지속, Sheveluch 지속
- 산사태(landslide) 현상이 이번 사이클 최초 2건 동시 등장 — phen-landslide mention 0→2

### ClimateEnvironment (기후·환경)
- **신규:** ESA 남극 30년 접지선 연구(Sentinel-1 SAR), ESA 메탄 3종 위성 매핑
- 빙하후퇴와 메탄 모니터링 동시 보강 — 다중위성 교차검증 이벤트

### HumanActivity (인간활동)
- **신규:** NASA 다중위성 조기 산림벌채 탐지 시스템
- 기존 GFW DIST-ALERT와 연계

### Defense (국방·안보)
- **신규:** 상업 위성의 군사 전략 변화 종합분석 (The Glass Battlefield)
- MizarVision 후속 — AI OSINT의 전략적 의미

### AgricultureMaritime (농업·해양)
- **업데이트:** CAS500-2/4 발사 확정 — 한반도 농업·산림 관측 역량 강화
- 금일 신규 이벤트 별도 없음

### Humanitarian (인도주의)
- 금일 신규 없음 (기존 가자/레바논 추적 지속)

## 온톨로지 변경 요약
- **신규 국가:** PG (파푸아뉴기니), PE (페루), GT (과테말라)
- **신규 위치:** Baining Mountains (PNG), Niscemi (Sicily)
- **phen-landslide 활성화:** mention_count 0→2 (첫 실제 이벤트 매핑)

## 추론 결과 요약
- **다중 위성 교차검증:** 4건 (ent-evt-042, 045, 046, 043)
- **센서-현상 적합성:** 3건 (SAR×빙하, trace_gas×메탄, hiRes×군사)
- **공식 출처 신뢰도:** 3건 (NASA, ESA×2)
- **전후 비교 신뢰도:** 3건 (PNG 산사태, Niscemi 산사태, 남극 접지선)
- **연쇄 재해:** 1건 (TC Maila → landslide → flood)
- **시계열 연결:** 1건 (ESA 30년 연구 → Smith Glacier)
- **재해 우선순위:** 1건 (조지아 산불 120+ 가옥 파괴)
