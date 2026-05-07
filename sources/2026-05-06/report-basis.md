# 2026-05-06 보고서 작성 근거 (report-basis)

## 1. 포함 이벤트 (final confidence ≥ 0.7) — 16건

| Rank | Event ID | 이벤트명 | Domain | 위성/센서 | 지역 | Final Conf | 비고 |
|------|----------|----------|--------|----------|------|-----------|------|
| 1 | ent-evt-082 | Mayon ashfall 87 barangays | Disaster | Sentinel-2A + Himawari-9 (multi) | Albay, PH | **0.97** | multiSatBoost+0.20, official+0.15, thermal+0.10, priority+0.20, ba+0.10, cascading→Guinobatan |
| 2 | ent-evt-093 | Pine Island Glacier 가속 10.6→12.7 m/day | Climate | Sentinel-1A C-SAR | West Antarctica | **0.97** | 10년 시계열, ESA 공식, sarBoost, priority, ba |
| 3 | ent-evt-083 | Cordoba flood EMSR865 | Disaster | Sentinel-1A + Sentinel-2A (multi) | Cordoba, CO | **0.97** | CEMS Rapid Mapping, multi-sensor, sar+priority |
| 4 | ent-evt-081 | Kilauea Episode 46 종료 (9h fountaining) | Disaster | Sentinel-2A (간접 USGS HVO) | Halemaʻumaʻu, US | **0.95** | partOfSeries(ent-evt-070), 650ft fountain, Hwy 11 tephra |
| 5 | ent-evt-092 | Antelope Reef 1,490 acres 인공섬 | Defense | WorldView-3 + PlanetScope (multi) | Paracel Islands, CN | **0.97** | AMTI Island Tracker, multi-sat, hi-res, ba |
| 6 | ent-evt-084 | ESA MARS methane + CAMS Hotspot Explorer | Climate | Sentinel-5P TROPOMI | INTL | **0.95** | tracegasBoost, official, multi-sensor |
| 7 | ent-evt-086 | 영변 UEP 4월 후속 (CSIS BP) | Defense | WorldView-3 0.31m | Yongbyon, KP | **0.95** | hi-res, analyst, **koreaBoost** |
| 8 | ent-evt-089 | Tehran 15 경찰서 PlanetScope (Bellingcat) | Defense | PlanetScope SkySat | Tehran, IR | **0.97** | hi-res, analyst, priority, ba |
| 9 | ent-evt-088 | Yelabuga UAV factory + DPRK 노동력 | Defense | WorldView-3 | Tatarstan, RU | **0.95** | DPRK-RU 협력 사슬, hi-res, analyst |
| 10 | ent-evt-095 | Sudan breadbasket NDVI (Al Jazeera) | AgriMarine | Sentinel-2A MSI | Gezira/Sennar/Khartoum, SD | **0.95** | 식량안보 priority, ba 전후 NDVI |
| 11 | ent-evt-091 | CAS500-1 국토위성 산불 복구 | Disaster | CAS500-1 | KR | **0.95** | KARI 정책브리핑, **koreaBoost** |
| 12 | ent-evt-097 | 미국 카리브해 Operation Southern Spear | Defense | (Wiki 종합) | Caribbean, VE | 0.70 | ent-evt-076 후속 |
| 13 | ent-evt-085 | Vantor 우크라이나 D2D 위성영상 시험 | Defense | WorldView-3 | UA | 0.80 | 보도자료성 cap, supersedes ent-evt-064 |
| 14 | ent-evt-087 | Panghyon airbase UAV (CSIS BP) | Defense | WorldView-3 | Panghyon, KP | 0.80 | **koreaBoost**, hi-res |
| 15 | ent-evt-094 | Planet Pelican-7/8/9 발사 (fleet 9기) | HumanActivity | (지상 발사) | US | 0.65 | 보도자료성 0.7 cap, 메타 |
| 16 | ent-evt-096 | NAU — Climate TRACE 도시 CO2 70% 과소 | Climate | (지상 측정 vs Climate TRACE) | US | 0.65 | 학술, 위성 직접관측 아님, 메타 |

## 2. 미검증 의혹 분리 (final confidence < 0.7) — 1건

| Event ID | 이벤트명 | 사유 |
|----------|---------|------|
| ent-evt-090 | DPRK 조선중앙TV 황해북도 사방야계·개성 산불감시·전국치수망 | 위성 영상 부재, 위성 출처 부재 → satellite_unverified, 본문 "미검증 의혹" 섹션 분리. koreaBoost는 적용했으나 final cap 0.55 |

## 3. 제외 이벤트 (sources/2026-05-06/index.json `excluded_for_scope` 참조)

22개 후보 URL 제외 — Earth Observatory IoTD 랜딩, FIRMS 홈페이지, 일반 SAR 방법론 논문, Bellingcat toolkit 인덱스, Disaster Charter 홈페이지, Sentinel-5P CH4 EE 카탈로그, NHC/Digital Typhoon hub, ICEYE 일반 서비스, Skylight Cerulean(이미 보고), 이전 Iran 사건 OSINT 중복, Bloomberg/RFE/RL/Anadolu/OPB Iran(older Feb-Apr), 농림위성 일반 보도자료, 북한 SLBM 신포(이미 5/5 보고), DPRK 425사업(이미 5/5 보고), 어업위성 일반론, 지진 위키 일반, Kilauea 540m 3월 보도(older), Climate TRACE about/data 인덱스, Sentinel-1 GFM/Nature 방법론 논문, MizarVision/Sohae/Yongbyon RFA 반복, InSAR 방법론 참조 등.

## 4. 보고서 KG 시각화 — 핵심 노드 30개 추출

### Events (17)
- ent-evt-081 Kilauea Ep46 종료
- ent-evt-082 Mayon ashfall 87 barangays
- ent-evt-083 Cordoba flood
- ent-evt-084 ESA MARS methane
- ent-evt-085 Vantor D2D
- ent-evt-086 영변 UEP 후속
- ent-evt-087 Panghyon UAV
- ent-evt-088 Yelabuga UAV
- ent-evt-089 Tehran 경찰서
- ent-evt-091 CAS500-1 산불 복구
- ent-evt-092 Antelope Reef 1,490 acres
- ent-evt-093 Pine Island
- ent-evt-095 Sudan breadbasket
- ent-evt-097 카리브해 Spear
- (ent-evt-070, ent-evt-071, ent-evt-029 — 시리즈 연결 표시)

### Satellites (6)
- sat-sentinel2a (S2A — 6 events)
- sat-worldview3 (WV-3/Vantor — 6 events)
- sat-sentinel1a (S1A — 2 events)
- sat-himawari9 (Himawari-9 — Mayon)
- sat-sentinel5p (S5P — methane)
- sat-cas500-1 (KARI 산불)

### Organizations (5)
- org-philsa (PhilSA — Mayon)
- org-cems (Copernicus EMS — Cordoba)
- org-csis-bp (CSIS BP — DPRK/Russia)
- org-amti (CSIS AMTI — Antelope Reef)
- org-bellingcat (Bellingcat — Tehran)

### Phenomena (5)
- phen-volcano, phen-flood, phen-methane, phen-glacier, phen-military

### Domains (5)
- dom-disaster, dom-defense, dom-climate, dom-agri-marine, dom-human

## 5. 보고서 구성 방향

### 5-1. 강조할 내용 (Top 5 본문)
1. **Mayon 화산 ashfall 87 barangays** — 다중위성+다중기관 교차검증, cascading→호흡기 환자
2. **Pine Island Glacier 10년 가속 (10.6→12.7 m/day)** — ESA Sentinel-1 decade
3. **Cordoba flood EMSR865** — CEMS Rapid Mapping SAR+MSI 멀티센서
4. **Kilauea Episode 46 종료 (9h, 650ft fountain)** — Hwy 11 tephra
5. **Antelope Reef 1,490 acres** — AMTI Island Tracker WV-3+PlanetScope 시계열

### 5-2. 다중 위성 교차검증 별도 섹션 (4건)
- Mayon S2A+Himawari-9 (다른 궤도/운영자)
- Cordoba S1A+S2A (SAR+MSI 상보)
- ESA MARS methane S5P+multi-sensor 융합
- Antelope Reef WV-3+PlanetScope (다른 운영자)

### 5-3. 한반도 GeoFocus 별도 섹션 (4건)
- KP 영변 UEP 후속 (CSIS BP, WV-3)
- KP Panghyon airbase UAV (CSIS BP)
- KR CAS500-1 산불 피해지 영상 지원 (KARI)
- KP 조선중앙TV 산불 보도 (위성 미검증, 의혹 분리)

### 5-4. 재해 사슬 (cascading) 섹션
- Mayon 분출 → ashfall(87 barangays/8,544 ha) → 호흡기 환자(Guinobatan) — 자연재해 → 인도주의 사슬

### 5-5. 시계열·전후 비교 강조 (6건)
- Kilauea Ep45→Ep46 직접 후속
- Mayon 2026-01~ 분출 시리즈의 5/6 시점 갱신
- Pine Island 2016→2026 10년 시계열
- Antelope Reef AMTI Island Tracker 매립 시계열
- Sudan Gezira/Sennar/Khartoum 전쟁 전후 NDVI
- Tehran 경찰서 PlanetScope 전후 영상

### 5-6. 미검증 의혹 분리 섹션
- ent-evt-090 DPRK 조선중앙TV 산불 보도

### 5-7. 인프라·메타 (분석가용)
- Vantor 우크라이나 D2D 시험 (Maxar 리브랜드 보도자료)
- Planet Pelican-7/8/9 fleet 9기 (보도자료성)
- ESA MARS methane + CAMS Hotspot Explorer (시스템 출시)
- NAU Climate TRACE 도시 CO2 ~70% 과소 (학술 비판)

## 6. 위성 출처 검증 매트릭스

| 이벤트 | 위성/DataProduct 1차 출처 | 위성/DataProduct 2차 | 검증 상태 |
|-------|------------|------------|----------|
| ent-evt-081 Kilauea | USGS HVO photo (Sentinel-2A 간접) | GOES-18 thermal | 검증 |
| ent-evt-082 Mayon | Sentinel-2A MSI (PhilSA) | Himawari-9 (VAAC Tokyo) | **다중 검증** |
| ent-evt-083 Cordoba | Sentinel-1A C-SAR (CEMS) | Sentinel-2A MSI | **다중 검증** |
| ent-evt-084 MARS | Sentinel-5P TROPOMI (ESA) | CAMS multi-sensor | **다중 검증** |
| ent-evt-085 Vantor D2D | WorldView-3 (Vantor) | — | 검증 |
| ent-evt-086 영변 | WorldView-3 (CSIS BP) | — | 검증 |
| ent-evt-087 Panghyon | WorldView-3 (CSIS BP) | — | 검증 |
| ent-evt-088 Yelabuga | WorldView-3 (CSIS BP) | — | 검증 |
| ent-evt-089 Tehran | PlanetScope (Bellingcat) | — | 검증 |
| ent-evt-090 DPRK 조선중앙TV | (없음) | — | **미검증** |
| ent-evt-091 CAS500-1 | CAS500-1 (KARI) | — | 검증 |
| ent-evt-092 Antelope Reef | WorldView-3 (AMTI) | PlanetScope | **다중 검증** |
| ent-evt-093 Pine Island | Sentinel-1A C-SAR (ESA) | — | 검증 |
| ent-evt-094 Pelican | (지상 발사 보도) | — | 메타 |
| ent-evt-095 Sudan | Sentinel-2A MSI (Al Jazeera) | — | 검증 |
| ent-evt-096 Climate TRACE | (학술 데이터) | — | 메타 |
| ent-evt-097 카리브해 | (Wiki 종합) | — | 메타 |

## 7. 사이클 통계

- 신규 이벤트: 17 (final conf ≥ 0.7: 16건, 미검증 1건)
- 신규 Country: 1 (SD)
- 신규 Location: 9
- 신규 Satellite: 1 (Pelican)
- 신규 Organization: 6
- 새 Class: 0 / 새 Relation: 0 (config 한도 내)
- 다중 위성 교차검증 이벤트: **4건**
- 한반도 이벤트: **4건**
- 재해 사슬 추론: 2건
- 시계열 후속 추론: 3건
- 누적 KG: ~600 트리플 (425 explicit + 175 inferred)
