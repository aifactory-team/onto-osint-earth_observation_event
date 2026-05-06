# 2026-05-05 보고서 근거

## 포함 항목

| 소스 ID | 제목 | 태그 | 도메인 | 이벤트 ID | 포함 근거 |
|---------|------|------|--------|----------|----------|
| src-001 | Kilauea Ep46 — 650ft lava fountains (USGS HVO) | update | Disaster | ent-evt-070 | USGS 공식 업데이트, GOES-18 열관측, officialBoost +0.15 |
| src-004 | Mayon Ash Advisory May 5 — VAAC Tokyo 0544Z (Himawari-9) | update | Disaster | ent-evt-071 | Himawari-9 VAAC 공식 자문, PHIVOLCS 경보 |
| src-006 | Georgia wildfires — Hwy82 85%, Pineland 50% contained | update | Disaster | ent-evt-072 | Landsat 8 OLI 위성영상, NASA 분석, officialBoost +0.15 |
| src-007 | Tuscany Monte Faeta wildfire — 700ha, 3,500 evacuated | new | Disaster | ent-evt-073 | Sentinel-2A Copernicus 영상 확인 |
| src-008 | Netherlands 't Harde wildfire — Sentinel-2/Planet multi-sat | new | Disaster | ent-evt-074 | Sentinel-2A + PlanetScope 다중위성, multiSatBoost +0.20 |
| src-010 | China Type 004 carrier — SkyFi sat reactor compartments | new | Defense | ent-evt-075 | SkyFi 위성영상 직접 분석, commercialBoost +0.10 |
| src-011 | US Caribbean military buildup — PlanetScope tracking | new | Defense | ent-evt-076 | PlanetScope 위성 추적, 구체적 자산 식별 |
| src-012 | NK Sinpo SLBM — SI Analytics satellite imagery | new | Defense | ent-evt-077 | SI Analytics 위성영상 AI, koreaBoost +0.10 |
| src-013 | 한국 425사업 정찰위성 5기 전력화 | update | Defense | ent-evt-078 | 한반도 GeoFocus, koreaBoost +0.10 |
| src-015 | CAS500-2 스마트농업 활용 전망 | new | AgriMarine | ent-evt-079 | CAS500-2 위성 농업 응용, koreaBoost +0.10 |
| src-016 | Japan Sanriku M7.7 earthquake — satellite unverified | new | Disaster | ent-evt-080 | 미검증 섹션 배치 (위성 피해평가 미실시, conf<0.5) |

## 제외 항목

| 소스 ID | 제목 | 제외 근거 |
|---------|------|----------|
| src-002 | Kilauea alert level escalates (BIVN) | src-001과 동일 이벤트 reported |
| src-003 | Lava fountains 650ft (Star-Advertiser) | src-001과 동일 이벤트 reported |
| src-005 | Mayon ashfall blankets towns (SCMP) | src-004와 동일 이벤트 reported |
| src-009 | Netherlands wildfire smoke (Ruisdael) | src-008과 동일 이벤트 reported, 보충 출처로 본문 기재 |
| src-014 | CAS500-2 '4년 지연' 끝 우주로 (뉴스페이스) | 이전 보도 reported (5/3 발사 이미 보고) |
| src-017 | US warships Middle East (Military Times) | 이전 보도 reported (5/4 src-010과 유사) |
| src-018 | 04 May global volcano summary | 이전 보도 reported (종합 뉴스) |
| src-019 | China carrier nuclear evidence (The War Zone) | src-010과 동일 이벤트 reported, 보충 출처로 본문 기재 |
| src-020 | US buildup Venezuela (Capital Post) | src-011과 동일 이벤트 reported |

## 이벤트 포함/분류

### 본문 포함 이벤트 (confidence >= 0.50, 위성 출처 확인)
- ent-evt-070: Kilauea Episode 46 (GOES-18, USGS) — **1순위 자연재해**
- ent-evt-071: Mayon May 5 eruption (Himawari-9, PHIVOLCS) — **1순위 자연재해**
- ent-evt-072: Georgia wildfire containment (Landsat 8, NASA) — **1순위 자연재해**
- ent-evt-073: Monte Faeta wildfire (Sentinel-2A) — 자연재해
- ent-evt-074: 't Harde wildfire (Sentinel-2A + PlanetScope) — 자연재해, multiSat 강조
- ent-evt-075: China Type 004 carrier (SkyFi) — 국방
- ent-evt-076: US Caribbean buildup (PlanetScope) — 국방
- ent-evt-077: NK Sinpo SLBM (SI Analytics) — 국방, 한반도 GeoFocus
- ent-evt-078: 425 recon satellites (KARI) — 국방, 한반도 GeoFocus
- ent-evt-079: CAS500-2 agriculture (KARI) — 농업, 한반도 GeoFocus

### 미검증 의혹 섹션
- ent-evt-080: Japan Sanriku M7.7 earthquake — 위성 피해평가 미실시, satellite_unverified, conf 0.50

## KG 시각화 범위

### 이벤트 노드 (10개 본문 + 1개 미검증)
- ent-evt-070 ~ ent-evt-079 (본문)
- ent-evt-080 (미검증, 점선 표시)

### 위성 노드 (7개)
- GOES-18, Himawari-9, Landsat 8, Sentinel-2A, PlanetScope, SkyFi, CAS500-2

### 기관 노드 (7개)
- USGS, PHIVOLCS, NASA, SkyFi, SI Analytics, KARI, Planet Labs

### 국가 노드 (8개)
- US, PH, IT, NL, CN, KP, KR, JP

### 총 약 33개 노드 → Mermaid 그래프 + 도메인별 세부

## 보고서 구성 방향

### 1순위: 자연재해 (Disaster)
- Kilauea Ep46 (인명 위험 — 용암 분수 200m, 하와이 화산국립공원)
- Mayon 5/5 분출 (인명 위험 — 화산재 강하, 대피)
- Georgia 산불 (인프라 — 55,000ac, 진화 진전)
- Monte Faeta 산불 (3,500 대피, 700ha)
- 't Harde 산불 (군사사격장, 연기 국경 통과, 다중위성)

### 2순위: 국방·안보 (Defense)
- 한반도 GeoFocus: NK 신포 SLBM + 425사업 (대비 분석)
- 중국 Type 004 핵항모 (전략적 의미)
- 미국 카리브해 집결 (지역 긴장)

### 3순위: 농업·해양 (AgricultureMaritime)
- CAS500-2 스마트농업 (한반도 GeoFocus)

### 4순위: 기후·환경 (ClimateEnvironment)
- 금일 신규 없음 명시

### 5순위: 인도주의 (Humanitarian)
- 금일 신규 없음 명시

### 미검증 의혹
- 산리쿠 M7.7 지진 — 위성 출처 부재

### 카테고리 커버리지 체크
- [x] 자연재해: 5건
- [x] 인간활동(개발/군사/산업): 국방 4건으로 커버
- [x] 기후·환경: 0건 신규 → "금일 신규 없음" 명시
- [x] 농업·해양: 1건
