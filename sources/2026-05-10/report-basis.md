# 2026-05-10 보고서 작성 근거

## 포함 항목 (10건)

| src | 제목 | 태그 | 도메인 | 포함 근거 |
|-----|------|------|--------|----------|
| src-001 | 칼로이/하구핏 TD 약화 | update | Disaster | 열대폭풍→저압부 전환, 위성(Himawari-9/GOES-18) 추적 |
| src-002 | Mayon VAAC 589 125일째 | update | Disaster | 125일 연속 분출, Alert 3 유지, Himawari-9+S2A 관측 |
| src-003 | Mayon 작물피해 1,039ha | update | AgriMarine | PhilSA Sentinel-2 기반 작물 매핑, 농업 영향 정량화 |
| src-004 | Dukono 수색 완료 3명 사망 | update | Disaster | 사건 종결, 국제 인명피해(싱가포르 2명), Himawari-9 |
| src-005 | Kilauea Ep47 5/12~15 | update | Disaster | USGS HVO 공식, 팽창 10.7μrad, S2A+L9 |
| src-006 | Great Sitkin WATCH/ORANGE | update | Disaster | USGS AVO 공식, 용암돔 지속 분출, VIIRS |
| src-007 | Shishaldin ADVISORY/YELLOW | update | Disaster | USGS AVO 공식, SO2 위성 관측, TROPOMI |
| src-008 | GA Pineland 32,575ac 70% | update | Disaster | NASA Landsat 8/9 burn scar, 이탄 화재 지속 |
| src-009 | Sentinel-2A/2C 복구 | update | Climate | ESA 공식, 데이터 중단→정상화 |
| src-010 | Mayon 인도주의 GLIDE | new | Humanitarian | ReliefWeb 정식 등록, 인도주의 차원 첫 공식화 |

## 제외 항목 (15건 reported)

| src | 제목 | 제외 근거 |
|-----|------|----------|
| src-011~025 | 이란 기지/Spratly/Pemex/NISAR/Xingu/CSIS NK/MethaneSAT/Hektoria/NLL/CAS500/GFW/Antelope/Balikatan/Fuego/Krasheninnikov | 금일 신규 정보 없음 (reported). 출처 목록에만 유지. |

## KG 시각화 범위
- 금일 신규 노드: ent-evt-401 (Mayon humanitarian), org-ocha
- 주요 업데이트 노드: ent-evt-082, ent-evt-127, ent-evt-128, ent-evt-202, ent-evt-203, ent-evt-204, temp-evt-001, ent-evt-201
- 핵심 위성: sat-himawari9, sat-sentinel2a, sat-landsat8, sat-landsat9, sat-viirs-jpss, sat-sentinel5p, sat-goes18
- 노드 수 목표: 20개 이내 (단일 전체 그래프 + 주요 관계)

## 보고서 구성 방향
- **Top 5 핵심**: Mayon 125일(+GLIDE등록), Dukono 수색완료, Kilauea Ep47 예측, GA Pineland 이탄화재, Caloy TD약화
- **다중 위성 교차검증**: Mayon (Himawari-9+S2A), GA Pineland (S-NPP+L8+L9), Kilauea (S2A+L9), Caloy (Himawari-9+GOES-18)
- **한반도 GeoFocus**: 금일 신규 이벤트 없음. 기존 추적(NLL 어선, CAS500-2, NK Yongbyon) "금일 변동 없음" 명시
- **미검증 의혹**: Fuego GT (위성 미확인, reported)
- **인도주의 섹션 활성화**: Mayon GLIDE 등록 — 이전까지 0건이던 인도주의 카테고리 첫 이벤트
