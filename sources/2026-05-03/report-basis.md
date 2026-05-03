# 2026-05-03 보고서 기초 (Report Basis)

## 포함 항목 (new + update)

| 소스 | 제목 | 태그 | 도메인 | 포함 근거 |
|------|------|------|--------|----------|
| src-001 | CAS500-2/4 발사 성공 | update | AgricultureMaritime | 한국 EO 위성 발사 성공 — GeoFocus |
| src-004 | Kilauea Ep.46 예보 May 4-7 | update | Disaster | USGS 공식 예보 갱신 |
| src-005 | Mayon 5/2 분출 Himawari-9 | update | Disaster | 위성 관측 확인 분출 |
| src-006 | Great Sitkin 용암돔 위성 열이상 | new | Disaster | 신규 화산, 위성 관측 |
| src-007 | Krasheninnikov 용암류 위성 열이상 | new | Disaster | 신규 화산, 위성 관측 |
| src-008 | 조지아 산불 봉쇄율 갱신 | update | Disaster | Landsat 8 영상 |
| src-009 | MethaneSAT 글로벌 메탄 평가 | new | ClimateEnvironment | 위성 직접 관측 최초 종합 평가 |
| src-011 | 아마존 불법 채굴 AI 탐지 | new | HumanActivity | Sentinel-2 기반, 6,000ha |
| src-013 | 브라질 DETER 금지 법안 | new | HumanActivity | 위성 거버넌스 정책 위협 |
| src-014 | Cerulean NRT 업그레이드 | new | HumanActivity | Sentinel-1 기반 준실시간 |
| src-023 | Earth Index 위성 검색엔진 | new | HumanActivity | 공개 도구, 낮은 중요도 |

## 제외 항목 (reported)

| 소스 | 제목 | 제외 근거 |
|------|------|----------|
| src-002 | 차세대중형위성 2호 뉴스핌 | src-001 중복 |
| src-003 | SpaceX CAS500-2 Space.com | src-001 중복 |
| src-010 | MethaneSAT ACP 논문 | src-009 중복 |
| src-012 | Kayapó 채굴 Mongabay | src-011 중복 |
| src-015~025 | 기타 reported | 이전 보고서 기보도 |

## 보고서 구성 방향

- **1순위:** 자연재해 (화산 4건 + 산불 1건) — 재해 우선 배치
- **한반도 GeoFocus:** CAS500-2/4 발사 성공 (한국 EO 역량 확대)
- **다중 위성 교차검증:** 금일 단일 이벤트 교차검증 신규 건은 없으나, MethaneSAT 독립 관측은 기존 TROPOMI/GOSAT 데이터와 교차 가능
- **미검증 의혹:** src-013 (DETER 금지 법안) — 위성 출처가 아닌 정책 이벤트이나, 위성 관측 인프라에 직접 영향하므로 본문 포함
- **KG 시각화:** 금일 신규 7 이벤트 + 관련 위성·기관·현상 노드 중심
