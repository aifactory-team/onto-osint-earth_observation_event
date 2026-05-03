# 2026-05-03 분석

## 신규 소스 중요도 평가

| 소스 | 중요도 | 도메인 | 근거 |
|------|--------|--------|------|
| src-001 (CAS500-2 발사 성공) | **높음** | AgricultureMaritime | 한국 차세대 EO 위성 발사 — GeoFocus 가산 |
| src-006 (Great Sitkin 화산) | 중간 | Disaster | 위성 열이상 확인, 신규 화산 이벤트 |
| src-007 (Krasheninnikov 화산) | 중간 | Disaster | 위성 일별 열이상, 신규 화산 이벤트 |
| src-009 (MethaneSAT 글로벌 평가) | **높음** | ClimateEnvironment | 위성 직접 관측 기반 전 지구 메탄 배출 최초 종합 평가 |
| src-011 (아마존 불법 채굴 AI) | **높음** | HumanActivity | Sentinel-2 기반 AI 탐지, 6,000ha 신규 채굴 |
| src-013 (브라질 DETER 금지 법안) | **높음** | HumanActivity | 위성 기반 환경 거버넌스 위협 |
| src-014 (Cerulean NRT 업그레이드) | 중간 | HumanActivity | Sentinel-1 기반 유류 오염 준실시간 탐지 |
| src-023 (Earth Index 공개) | 낮음 | HumanActivity | 도구 소개, 직접 이벤트 아님 |

## 업데이트 항목 변경사항

| 소스 | 이전 항목 | 변경사항 |
|------|----------|----------|
| src-001 | ent-evt-032 (CAS500-2/4 발사 예정) | 예정→성공. 궤도 진입, 스발바르 첫 교신 확인 |
| src-004 | ent-evt-021 (Kilauea Ep.45) | Ep.46 예보 창 May 4-7로 구체화 |
| src-005 | ent-evt-029 (Mayon) | 5월 2일 분출 에피소드, VAAC 권고 |
| src-008 | ent-evt-020 (조지아 산불) | 봉쇄율 갱신 (44%/64%), 면적 55,107ac |

## 도메인별 흐름

- **자연재해:** 화산 활동 집중 (Kilauea 예보, Mayon 분출, Great Sitkin·Krasheninnikov 신규). 조지아 산불 점진적 봉쇄.
- **인간활동:** 아마존 불법 채굴 AI 탐지 + DETER 금지 법안 위기. Cerulean NRT 업그레이드. Earth Index 공개.
- **기후·환경:** MethaneSAT 최초 글로벌 평가 — EPA 추정 4배 초과.
- **농업·해양:** CAS500-2/4 발사 성공 → 한반도 정밀 관측 역량 확대. CAS500-4 광대역 농업 전용.
- **국방·안보:** 금일 신규 없음 (기존 추적 항목 변동 없음).
- **인도주의:** 금일 신규 없음.

## 온톨로지 변경 요약

- 새 엔티티 7건 (Event 7)
- 새 Location 2건 (Great Sitkin, Krasheninnikov)
- 새 Organization 2건 (EDF, INPE)
- CAS500-2/4 mission_status 갱신: pre-launch → operational
- 새 Country 0건
