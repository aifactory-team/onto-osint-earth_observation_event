# 2026-05-07 보고서 작성 근거 (Phase 4)

## 1. 보고서 포함 24건 (final confidence ≥ 0.7)

### 자연재해 (Disaster) — 5건
| Rank | Event ID | 이벤트명 | 위성/센서 | 지역 | Final Conf |
|------|----------|----------|----------|------|-----------|
| 1 | ent-evt-098 | GA Pineland Road & Hwy 82 wildfires (50,000 ac) | Landsat 9 OLI/TIRS + VIIRS | Georgia, US | **0.97** |
| 2 | ent-evt-101 | Kilauea Episode 46 종료 후속 (in-situ HVO) | (USGS HVO in-situ + GOES-18 thermal) | Halemaʻumaʻu, US | **0.97** |
| 3 | ent-evt-102 | Mayon VAAC ash advisory 567 / 호흡기 경고 후속 | Himawari-9 + Sentinel-2A (multi) | Albay, PH | **0.97** |
| 4 | ent-evt-109 | Myanmar 몬순 사전 경보 (IFRC) | Sentinel-1 3기 (multi-SAR) | Yangon/Ayeyarwady, MM | **0.97** |
| 5 | ent-evt-099 | Krasheninnikov 화산 활동 (KVERT) | VIIRS + Himawari-9 (multi) | Kamchatka, RU | **0.95** |
| 6 | ent-evt-100 | 글로벌 화산 일일 요약 (보조) | (집계) | global | 0.78 |

### 한반도 GeoFocus — 5건
| Rank | Event ID | 이벤트명 | 위성/센서 | 지역 | Final Conf |
|------|----------|----------|----------|------|-----------|
| 7 | ent-evt-110 | KOMPSAT-7 발사 일정 (KARI) | KOMPSAT-7 (pre-launch) | KR | **0.97** |
| 8 | ent-evt-111 | NLL 中어선 100척 (동해) | VIIRS night light + Sentinel-1 (multi) | NLL/East Sea | **0.97** |
| 9 | ent-evt-113 | CAS500-2 첫 교신 (5/3 commissioning) | CAS500-2 | KR | **0.97** |
| 10 | ent-evt-115 | 영변 UEP 5/3 후속 (CSIS BP, supersedes evt-086) | WorldView-3 0.31m | Yongbyon, KP | **0.97** |
| 11 | ent-evt-116 | Sohae 엔진 시험 인프라 | WorldView-3 | Sohae, KP | **0.92** |

### 인간활동 (Human Activity) — 4건
| Rank | Event ID | 이벤트명 | 위성/센서 | 지역 | Final Conf |
|------|----------|----------|----------|------|-----------|
| 12 | ent-evt-106 | Amazon PIK 1.5°C 임계점 연구 | Sentinel-2A + Landsat 9 (multi) | Amazon, BR | **0.92** |
| 13 | ent-evt-119 | GFW 2026 보고서 발표 | Landsat 9 + Sentinel-2 + Sentinel-1 | global | **0.92** |
| 14 | ent-evt-123 | Brazil PRODES April update (partOfSeries evt-106) | Sentinel-2A + Landsat 9 | Amazon, BR | **0.95** |
| 15 | ent-evt-124 | Cerulean SkyTruth Brazil oil slick | Sentinel-1 C-SAR | offshore Brazil | **0.95** |

### 기후·환경 (Climate & Environment) — 5건
| Rank | Event ID | 이벤트명 | 위성/센서 | 지역 | Final Conf |
|------|----------|----------|----------|------|-----------|
| 16 | ent-evt-103 | UN MARS 메탄 알림 후속 (supersedes evt-084) | Sentinel-5P TROPOMI | global | **0.97** |
| 17 | ent-evt-112 | UCLA Silivri 매립지 메탄 (Carbon Mapper) | Tanager-1 + EMIT (multi-hyperspectral) | Silivri, TR | **0.97** |
| 18 | ent-evt-117 | Sentinel-1D 4-위성 콘스텔레이션 운용 (supersedes evt-026) | Sentinel-1A/B/C/D | global | **0.97** |
| 19 | ent-evt-118 | Hektoria Glacier 8 km / 2개월 후퇴 | Sentinel-1A + Sentinel-2A (multi) | Antarctica | **0.95** |
| 20 | ent-evt-122 | MethaneSAT 글로벌 평가 (EDF) | MethaneSAT | global | **0.85** |

### Sat-Ops 인프라 / 메타 — 3건
| Rank | Event ID | 이벤트명 | 위성/센서 | 지역 | Final Conf |
|------|----------|----------|----------|------|-----------|
| 21 | ent-evt-104 | Sentinel-5P OCM Operational Cloud Mask 출시 (5/6) | Sentinel-5P | global | **0.95** |
| 22 | ent-evt-107 | ICEYE Polar 4 + Faroe 2 라이드쉐어 발사 | ICEYE | global | **0.85** |
| 23 | ent-evt-105 | WorldView Legion 6기 풀 운용 (PR cap) | WorldView Legion | global | **0.78** |
| 24 | ent-evt-108 | ICEYE deforestation service launch (PR cap) | ICEYE SAR | global | **0.72** |

### 국방·안보 — 1건 (한반도 외)
| Rank | Event ID | 이벤트명 | 위성/센서 | 지역 | Final Conf |
|------|----------|----------|----------|------|-----------|
| 25 | ent-evt-120 | Antelope Reef 5/4 후속 (supersedes evt-092) | WorldView-3 + Sentinel-2A (multi) | Paracel, CN | **0.97** |

## 2. 미포함 / 분리 — 2건
| Event ID | 이벤트명 | 사유 |
|----------|---------|------|
| ent-evt-121 | Cuarteron Reef 레이더 (단일 naturalnews) | low_confidence 0.65 — 본 사이클 부록 |
| ent-evt-114 | (skip — evt-105 중복 흡수) | duplicate |

## 3. 미검증 의혹 (carry from 2026-05-06)
| Event ID | 이벤트명 | 사유 |
|----------|---------|------|
| ent-evt-090 | DPRK 조선중앙TV 산불 보도 | satellite_unverified 유지 |

## 4. KG 시각화 핵심 노드 30개
### Events (19)
- evt-098 GA Pineland / evt-099 Krasheninnikov / evt-100 Volcano summary / evt-101 Kilauea Ep46 / evt-102 Mayon advisory
- evt-103 UN MARS / evt-104 S5P OCM / evt-106 PIK Amazon / evt-109 Myanmar flood / evt-110 KOMPSAT-7
- evt-111 NLL / evt-112 Silivri methane / evt-113 CAS500-2 / evt-115 영변 / evt-116 Sohae
- evt-117 S1D / evt-118 Hektoria / evt-119 GFW 2026 / evt-120 Antelope / evt-122 MethaneSAT / evt-123 Brazil PRODES

### Satellites (8)
- sat-sentinel1a (S1A) / sat-sentinel2a (S2A) / sat-landsat9 / sat-worldview3 (WV-3)
- sat-viirs-jpss / sat-himawari9 / sat-sentinel5p / sat-kompsat7 (신규)

### Organizations (5)
- org-csis-bp / org-kari / org-nasa / org-esa / org-philsa

### Phenomena (4)
- phen-volcano / phen-flood / phen-methane / phen-glacier

### 신규 (사이드 표기)
- 신규 Satellite 3: sat-wv-legion / sat-tanager1 / sat-emit
- 신규 Organization 6: KVERT / UNMARS / PIK / PAF / CarbonMapper / UCLA
- 신규 Country 2: co-mm (Myanmar) / co-tr (Türkiye)
- 신규 Phenomenon 1: phen-satops

## 5. 추론 통계 (본 사이클)
- 총 61건 / 0.92 평균 신뢰도
- multi-sat 10 / partOfSeries 3 / supersedes 4 / sensor capability 13 / official 12 / korea 5 / priority 4 / ba 6 / commercial 3 / analyst 5 / cascading 0

## 6. 보고서 구성 가이드
1. **오늘의 핵심 (Top 5)**: evt-098 GA Pineland → evt-115 영변 → evt-118 Hektoria → evt-117 S1D → evt-112 Silivri
2. **다중 위성 교차검증** (8건 강): Mayon / Krasheninnikov / Amazon / Myanmar 3xS1 / NLL / Silivri / Hektoria / Antelope
3. **한반도 GeoFocus** (5건): KOMPSAT-7 / NLL / CAS500-2 / 영변 / Sohae
4. **재해 사슬**: 본 사이클 0건 (시계열 후속 위주)
5. **시계열·전후 비교** (6건 강): Kilauea Ep46 / Mayon / 영변 / Sohae / Hektoria / Antelope
6. **메탄 트리오 별도 묶음**: UN MARS / Silivri / MethaneSAT
7. **Amazon 트리오 별도 묶음**: PIK / PRODES / Cerulean
8. **Sat-Ops 인프라** (5건 메타): S1D / WV-Legion / ICEYE rideshare / CAS500-2 / KOMPSAT-7 / S5P OCM
9. **미검증 의혹**: evt-090 carry, evt-100 보조, evt-121 부록 단일출처
10. **Mermaid 4-cluster KG 시각화**: Disaster / Defense+Korea / Climate+Methane+Hektoria / HumanActivity+Amazon

## 7. 위성 출처 검증 매트릭스 (요약)
- **다중 검증** 8건: Mayon / Krasheninnikov / Amazon / Myanmar / NLL / Silivri / Hektoria / Antelope
- **단일 위성 검증** 12건
- **위성 미검증 / 메타 (in-situ·발표·연구)** 4건: Kilauea evt-101(in-situ), KOMPSAT-7 evt-110(pre-launch), MethaneSAT evt-122(연구), CAS500-2 evt-113(commissioning), 글로벌 화산 evt-100(집계)
- **PR cap** 2건: evt-105, evt-108
- **low confidence 부록** 1건: evt-121
- **carry 미검증** 1건: evt-090

## 8. 사이클 통계
- 신규 이벤트: 26 (포함 24, 부록 1, skip 1)
- 신규 Satellite: 3 (WV-Legion, Tanager-1, EMIT)
- 신규 Organization: 6 (KVERT, UNMARS, PIK, PAF, CarbonMapper, UCLA)
- 신규 Country: 2 (MM, TR)
- 신규 Location: 7 (ent-loc-039 ~ 045)
- 신규 Phenomenon: 1 (phen-satops)
- 새 Class: 0 / 새 Relation: 0 (config 한도 내)
- 다중 위성 교차검증: 8 강 + 2 약 = 10건
- 한반도 이벤트: 5건
- supersedes 체인: 4건
- 누적 KG: 790 트리플 (579 explicit + 211 inferred)

---

## Cycle 2 보고서 작성 근거 (src-029 ~ src-036)

### C2-1. 보고서 포함 7건 + 업데이트 1건

#### 자연재해 (Disaster) — 3건
| Rank | Event ID | 이벤트명 | 위성/센서 | 지역 | Final Conf |
|------|----------|----------|----------|------|-----------|
| C2-1 | ent-evt-127 | Tropical Storm Hagupit (서태평양) | Himawari-9 + GOES-18 (multi-GEO) | 7.7N/142.2E, Yap/W. Pacific | **0.95** |
| C2-2 | ent-evt-128 | Dukono 화산 분출 (인도네시아) | Himawari-9 thermal IR | 1.69N/127.88E, Halmahera, ID | **0.90** |
| C2-3 | ent-evt-131 | Kanlaon 화산 Alert Level 2 (필리핀) | (PHIVOLCS in-situ + 위성 보조) | 10.41N/123.13E, Negros, PH | **0.85** |

#### 인간활동 (Human Activity) — 2건
| Rank | Event ID | 이벤트명 | 위성/센서 | 지역 | Final Conf |
|------|----------|----------|----------|------|-----------|
| C2-4 | ent-evt-125 | Pemex Cantarell 원유 유출 3개월 지속 | Sentinel-1A (SAR) + Sentinel-2A (MSI) | 19.8N/92.4W, Campeche Bay, MX | **0.90** |
| C2-5 | ent-evt-126 | Iran-US 기지 피해 228+ 구조물 | Copernicus 위성 검증 (WaPo) | 29.3N/47.7E, Camp Arifjan, KW/BH | **0.85** |

#### 기후·환경 (Climate & Environment) — 1건
| Rank | Event ID | 이벤트명 | 위성/센서 | 지역 | Final Conf |
|------|----------|----------|----------|------|-----------|
| C2-6 | ent-evt-129 | UNEP IMEO MARS coal/waste 확장 (supersedes evt-106) | Sentinel-5P TROPOMI | global | **0.95** |

#### 국방 (Defense) — 1건
| Rank | Event ID | 이벤트명 | 위성/센서 | 지역 | Final Conf |
|------|----------|----------|----------|------|-----------|
| C2-7 | ent-evt-130 | Sweden 첫 군사위성 발사 | Planet Labs 제작, 광학 LEO | SE | **0.80** |

#### 업데이트 (시계열 진전) — 1건
| Event ID | 이벤트명 | 변경사항 | Final Conf |
|----------|---------|---------|-----------|
| ent-evt-082 | Mayon 화산 lava flow 진전 | Basud 방향 3.8km, SO2 2,184 t/d | **0.97** (기존 유지) |

### C2-2. supersedes / partOfSeries
- ent-evt-129 :supersedes ent-evt-106 (UN MARS oil&gas only → coal+waste sectors 확장)
- ent-evt-082 :partOfSeries ent-evt-029 (Mayon 2026-01~ 시리즈 — lava flow 3.8km 업데이트)

### C2-3. 신규 엔티티 (instances.json 반영 대상)
- Country 2: co-mx (Mexico), co-kw (Kuwait)
- Organization 5: CEMDA (NGO, MX), Pemex (industry, MX), Washington Post (media, US), CVGHM/PVMBG (space_agency, ID), Swedish Armed Forces (defense_intel, SE)
- Location 5: Cantarell (MX), Camp Arifjan/5th Fleet (KW), Western Pacific/Yap, Mount Dukono (ID), Mount Kanlaon (PH)
- Satellite 1: Sweden Military Recon 1 (Swedish AF, LEO, optical)

### C2-4. 보고서 구성 가이드 (Cycle 2 추가분)
1. **자연재해 섹션 추가**: TS Hagupit → Dukono → Kanlaon (재해 우선순위 순)
2. **인간활동 섹션 추가**: Pemex Cantarell (3개월 SAR 시계열) → Iran-US 기지 피해 (Copernicus 검증)
3. **기후 섹션 추가**: UNEP MARS coal/waste 확장 (supersedes 기존 oil&gas 항목)
4. **국방 섹션 추가**: Sweden 첫 군사위성 (sat-ops 메타이벤트)
5. **Mayon 업데이트**: 기존 Mayon 항목에 lava flow 3.8km + SO2 수치 추가
6. **다중 위성 교차검증 2건 추가**: Cantarell (SAR+MSI cross-modal) + Hagupit (GEO 독립 운영자)

### C2-5. 사이클 통계 (C1+C2 합산)
- 총 이벤트: 26 (C1) + 7 (C2) + 1 update = 34건
- 총 신규 Satellite: 3 (C1) + 1 (C2) = 4건
- 총 신규 Organization: 6 (C1) + 5 (C2) = 11건
- 총 신규 Country: 2 (C1) + 2 (C2) = 4건
- 총 신규 Location: 7 (C1) + 5 (C2) = 12건
- 총 추론 발동: 61 (C1) + 10 (C2) = 71건
- 누적 KG 추정: ~830 트리플
