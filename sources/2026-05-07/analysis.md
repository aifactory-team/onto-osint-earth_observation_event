# 2026-05-07 위성영상 관측 이벤트 — 도메인 분석 (Phase 3)

## 0. 개요
- 입력: entities.json (80 entities, 105 relations, 13 신규 + 67 매칭, 26 이벤트)
- 도메인 분포: Defense 8, Disaster 6, Climate 6, HumanActivity 5, Agri-Marine 3 — 4개 카테고리 모두 활성
- 한반도 GeoFocus: 5건 (KOMPSAT-7, NLL 어선, CAS500-2, 영변 UEP, Sohae)
- 다중 위성 교차검증 후보: 10건 (강가산 8건 + 약가산 2건)
- supersedes 4건, partOfSeries 3건

## 1. 도메인별 분석

### 1-1. Disaster (자연재해) — 6건
- **GA Pineland Road & Hwy 82 wildfires** (evt-098) — 미국 조지아 50,000 acres 광역 산불, Landsat TIRS 열적외 검증, 0.97
- **Krasheninnikov volcano** (evt-099) — 러시아 캄차카 활화산 KVERT 모니터링, VIIRS+Himawari-9 다중위성, 0.95
- **글로벌 화산 일일 요약** (evt-100) — wordpress 단일 출처 보조, 0.78
- **Kilauea Episode 46 종료** (evt-101) — partOfSeries(evt-081), USGS HVO in-situ 측정 (위성영상 직접 검증 없음), 0.97
- **Mayon VAAC ash advisory 567** (evt-102) — partOfSeries(evt-082), Himawari-9+S2A, 87 barangay 호흡기 경고 후속, 0.97
- **Myanmar 몬순 사전경보** (evt-109) — Sentinel-1 3기 SAR 흐름 모델, IFRC 발동, 0.97

### 1-2. HumanActivity (인간활동) — 5건
- **Amazon PIK 1.5°C 임계점** (evt-106) — Potsdam 연구, S2A+Landsat 9, 0.92
- **ICEYE deforestation service** (evt-108 PR cap) — 상용 서비스 출시, 0.72
- **GFW 2026 보고서 발표** (evt-119) — Landsat+S2+S1 통합, 분석가 가산, 0.92
- **Brazil PRODES April update** (evt-123) — partOfSeries(evt-106), INPE 시계열, 0.95
- **Cerulean SkyTruth Brazil oil slick** (evt-124) — Sentinel-1 SAR sea surface dampening, 0.95

### 1-3. ClimateEnvironment (기후·환경) — 6건
- **UN MARS 메탄 알림 후속** (evt-103) — supersedes(evt-084), TROPOMI plume detect, 0.97
- **Sentinel-5P OCM Operational Cloud Mask 출시 (5/6)** (evt-104) — ESA 운영 도입, 0.95
- **UCLA Silivri 매립지 메탄** (evt-112) — Tanager-1 + EMIT 다중 hyperspectral 검증, 0.97
- **Sentinel-1D 4-위성 콘스텔레이션 운용 진입** (evt-117) — supersedes(evt-026), 재방문 6일→1.5일, 0.97
- **Hektoria Glacier 8km/2개월 후퇴** (evt-118) — S1A+S2A 다중위성, 극야 SAR, 0.95
- **MethaneSAT 글로벌 평가** (evt-122) — EDF, 학술 발표, 0.85

### 1-4. AgriMaritime (농업·해양) — 3건
- **NLL 中어선 100척** (evt-111) — VIIRS night light + Sentinel-1 ship detect, 한반도 GeoFocus, 0.97
- **CAS500-2 첫 교신 (5/3)** (evt-113) — KARI 스발바르 commissioning, 0.97
- **Pelican carry** — 메타 (evt-094 carry-over)

### 1-5. Defense (국방·안보) — 8건
- **WorldView Legion 6기 풀 운용** (evt-105 PR cap) — Maxar/Vantor 발표, 0.78
- **ICEYE Polar 4 + Faroe 2 라이드쉐어** (evt-107) — SAR 콘스텔레이션 확장, 0.85
- **KOMPSAT-7 발사 일정** (evt-110) — KARI, 한반도 GeoFocus, 0.95
- **영변 UEP 후속 관측 (5/3)** (evt-115) — supersedes(evt-086), CSIS BP WV-3 0.31m, 0.97
- **Sohae 엔진 시험 인프라** (evt-116) — 한반도 GeoFocus, WV-3 hi-res, 0.92
- **Antelope Reef 후속 (5/4)** (evt-120) — supersedes(evt-092), AMTI WV-3+S2A, 0.97
- **Cuarteron Reef 레이더 단일 출처** (evt-121) — naturalnews 단일, 미포함, 0.65
- **GFW 일반 deforestation analysis 통합** (보조)

## 2. 위성 활용도 Top
| 위성 | 본 사이클 활용 | 핵심 도메인 |
|------|----------|------------|
| **Sentinel-1A** (C-SAR) | 6건 | Myanmar/Brazil 오일/Hektoria/NLL/S1D 콘스텔레이션 |
| **Sentinel-2A** (MSI) | 5건 | Mayon/Amazon/Antelope/GFW/Hektoria |
| **Landsat 9** (OLI/TIRS) | 4건 | GA Pineland TIRS/Amazon/GFW/Brazil |
| **WorldView-3** | 4건 | 영변/Sohae/Antelope/Cuarteron |
| **VIIRS (JPSS)** | 3건 | Krasheninnikov/NLL/GA |
| **Himawari-9** | 2건 | Krasheninnikov/Mayon |
| **Sentinel-5P TROPOMI** | 2건 | UN MARS/MethaneSAT |
| **Tanager-1 + EMIT** (신규) | 1건 | UCLA Silivri 메탄 |
| **WorldView Legion** (신규) | — | 운용 진입 |

## 3. 지역 클러스터
- **한반도 5건**: KOMPSAT-7 발사 일정 / NLL 中어선 / CAS500-2 commissioning / 영변 UEP / Sohae 엔진시험
- **남중국해 2건**: Antelope Reef supersedes / Cuarteron Reef 단일출처
- **메탄 트리오 3건**: UN MARS / Silivri / MethaneSAT
- **Amazon 트리오 3건**: PIK 1.5°C 임계점 / Brazil PRODES / Cerulean oil slick

## 4. 추론 결과 요약
| 규칙 | 적용 건수 |
|------|---------|
| multi_satellite_confirmation | 10 (강 8 + 약 2) |
| temporal_progression / partOfSeries | 3 |
| supersedes | 4 |
| sensor_capability_match (SAR 5 + TIRS 2 + tracegas 3 + hires 3) | 13 |
| official_source_trust | 12 |
| commercial_imagery_trust | 3 (PR cap 2) |
| analyst_org_trust | 5 |
| korea_geo_focus | 5 |
| disaster_severity_priority | 4 |
| before_after_credibility | 6 |
| cascading_disaster | 0 |
| **합계** | **61건** |

평균 신뢰도 0.92, 본 사이클 일별 trippe 154 explicit + 36 inferred = 190 (누적 790).

## 5. 직전 보고서 follow-up 9건
- supersedes 4건: evt-115(영변), evt-117(S1D), evt-120(Antelope), evt-103(UN MARS)
- partOfSeries 3건: evt-101(Kilauea Ep46), evt-102(Mayon), evt-123(Brazil Amazon)
- 약결합 2건: evt-111(NLL/이전 동해 어업 보고), evt-104(S5P OCM/이전 메탄)

## 6. 데이터 품질
- 모든 이벤트 26/26 PASS — phenomenon, domain, satellite_or_unverified, location_info 모두 충족
- press release cap 2건 (evt-105, evt-108)
- low confidence 2건 (evt-100 wordpress, evt-121 naturalnews 단일)
- supersedes chain consistency PASS

## 7. 결론
본 사이클의 4개 핵심 축:
1. **위성 capacity 자체 확장** — Sentinel-1D 운용진입(evt-117), WorldView Legion 6기 풀 운용(evt-105), ICEYE 라이드쉐어(evt-107), Tanager-1+EMIT 본격 적용(evt-112), CAS500-2 commissioning(evt-113), KOMPSAT-7 발사 일정(evt-110), S5P OCM(evt-104) → 7건
2. **한반도/남중국해 / 메탄 / Amazon 4축** 균형
3. **9건 follow-up 시계열 진전** — supersedes 4 + partOfSeries 3 + 약결합 2
4. **Mayon 호흡기 사슬 연속**, Amazon 1.5°C 임계점 강도 진전 (학술→정책 신호)
