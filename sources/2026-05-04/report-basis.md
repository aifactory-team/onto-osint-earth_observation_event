# 2026-05-04 보고서 근거

## 포함 항목

| 소스 ID | 제목 | 태그 | 도메인 | 포함 근거 |
|---------|------|------|--------|----------|
| src-001 | Kīlauea Episode 46 예보 May 4-7 | update | Disaster | USGS 공식 업데이트, 위성 열관측 지속 |
| src-003 | 조지아 산불 위성 피해 분석 (Newsweek) | update | Disaster | Landsat 8 OLI 위성영상 확인, containment 수치 업데이트 |
| src-005 | 가자 군사 시설 확장 (Al Jazeera/Planet/Sentinel) | new | Defense | PlanetScope+Sentinel-2A 다중위성 교차검증 |
| src-006 | 레바논 파괴 CNN/Airbus 분석 (523건 건물) | update | Humanitarian | Airbus 위성영상 정량분석 |
| src-007 | Mayon 화산 화쇄류 + 화산재 FL060 | update | Disaster | Himawari-9 VAAC 공식 자문 |
| src-009 | 중국 Lop Nur 군사기지 확장 | new | Defense | 위성영상 기반 분석, J-36 관측 |
| src-010 | 미국 이란 인근 군사 집결 (중국 위성) | new | Defense | GaoFen 위성 관측, 구체적 수량 |
| src-011 | Planet Labs 이란 영상 블랙아웃 | new | Defense | EO OSINT 투명성 구조적 변화 |
| src-013 | 영변 핵단지 활동 증가 (RFA) | update | Defense | 위성 관측 확인 (한반도 GeoFocus) |
| src-015 | MethaneSAT Permian 상원 조사 | new | Climate | MethaneSAT 위성 데이터 → 정책 전환 |
| src-020 | 그린란드 빙하 후퇴 2배 가속 | new | Climate | Landsat+Sentinel 다중위성 분석 |

## 제외 항목

| 소스 ID | 제목 | 제외 근거 |
|---------|------|----------|
| src-002 | Kīlauea BIVN 보도 | src-001과 동일 내용 reported |
| src-004 | NASA EO Georgia fires | src-003과 동일 이벤트 reported |
| src-008 | Mayon PDC YouTube | src-007과 동일 이벤트 reported |
| src-012 | Iran remote sensing Breaking Defense | src-011과 동일 이슈 reported |
| src-014 | 38North Sohae | 이전 보도 reported |
| src-016 | MethaneSAT EDF data | src-015와 동일 이벤트 reported |
| src-017 | AI 산불 탐지 Pano AI | 위성 출처 미확인 → 미검증 섹션 |
| src-018 | Sabancaya 5/3 | 이전 보도 reported |
| src-019 | CAS500-2 Korea Times | 이전 보도 reported |
| src-021 | NOAA Wildfire Portal | 위성 출처 미확인 (시스템 뉴스) |
| src-022 | Antarctica Nature Geoscience | 이전 보도 reported |

## KG 시각화 범위
- 이벤트 노드: 11개 (포함 항목 기반)
- 위성 노드: 8개 (Landsat 8, GOES-18, PlanetScope, Sentinel-2A, Himawari-9, GaoFen, MethaneSAT, Airbus Pléiades)
- 기관 노드: 6개 (USGS, NASA, Planet, EDF, RFA, CNN)
- 총 약 25개 노드 → 전체 그래프 + 도메인별 세부

## 보고서 구성 방향
- **1순위**: 자연재해 (Kīlauea, 조지아 산불, Mayon) — 인명·인프라 영향
- **한반도 GeoFocus**: 영변 핵단지 활동 증가
- **다중 위성 교차검증**: 가자 군사 시설 (PlanetScope+Sentinel-2), 그린란드 빙하 (Landsat+Sentinel-2)
- **미검증 의혹**: Pano AI 산불 탐지 (src-017) — 위성 출처 부재
- 인간활동 카테고리: 금일 신규 없음 명시
- 농업·해양 카테고리: 금일 신규 없음 명시
