# 2026-05-08 위성영상 관측 이벤트 — 도메인 분석 (Phase 3)

## 0. 개요
- 입력: 25 sources (11 new, 6 update, 8 reported)
- 신규 이벤트: 6건 (ent-evt-201~206)
- 업데이트 이벤트: 5건 (ent-evt-082, 126, 127, 128, temp-evt-001)
- 도메인 분포: Disaster 7, HumanActivity 1, Climate 1, Defense 1, AgriMarine 0 (SatOps 1건 포함)
- 한반도 GeoFocus: 0건 (금일 한반도 관련 이벤트 없음)
- 다중 위성 교차검증: 5건 (모두 강가산 — 독립 운영자)
- partOfSeries: 6건, cascading_disaster 잠정 1건
- 금일 핵심: **Dukono 인명피해**, **Mayon-Hagupit lahar 연쇄 위험**, **Sentinel-2 데이터 장애**

## 1. 도메인별 분석

### 1-1. Disaster (자연재해) — 7건 (신규 3 + 업데이트 4)

**화산 클러스터 — 5건 동시 활성**

금일 사이클의 핵심은 전 세계 5개 화산이 동시에 활성 상태라는 점이다:

- **ent-evt-128 update (Dukono, Indonesia)** — VAAC Darwin advisory에서 severity HIGH로 업그레이드. 3명 사망(등산객), ash plume 10km. Himawari-9 열적외 검증. CVGHM/PVMBG + BNPB 공식. **금일 최고 우선순위** (인명피해).
  - confidence: 0.97 (cap) — official+0.15, priority+0.20
  
- **ent-evt-082 update (Mayon, Philippines)** — Danger zone 6km→8km 확대. PDC(pyroclastic density current) 지속. **Hagupit/Caloy 접근으로 lahar 위험 잠정 추론.** Himawari-9 + Sentinel-2A 다중위성 확인.
  - confidence: 0.97 (cap) — multiSat+0.20, priority+0.20, partOfSeries(evt-029)
  - **cascading_disaster 잠정**: Hagupit PAR entry May 9 → 강우 시 Mayon 화산재 퇴적 위 lahar 발생 가능

- **ent-evt-202 (Kilauea Ep47 forecast)** — USGS HVO 예보 May 12-17 분출. ADVISORY/YELLOW. 위성 직접 관측 없음(예보 단계).
  - confidence: 0.95 — official+0.15, partOfSeries(evt-101 Ep46→Ep47)

- **ent-evt-203 (Great Sitkin WATCH/ORANGE)** — AVO alert 상향. Lava dome growth 지속. VIIRS thermal 확인.
  - confidence: 0.97 (cap) — official+0.15, thermal+0.10, partOfSeries(evt-050)

- **ent-evt-204 (Shishaldin ADVISORY/YELLOW)** — AVO 경보. **Sentinel-5P TROPOMI SO2 탐지** — 금일 유일한 trace gas 위성 검증 건.
  - confidence: 0.95 — official+0.15, tracegas+0.15

**열대성 폭풍**

- **ent-evt-127 update (TS Hagupit/Caloy)** — Yap 통과 후 서진, May 9 PAR entry 예상. Himawari-9 + GOES-18 다중 GEO 교차검증. PAGASA가 local name "Caloy" 부여.
  - confidence: 0.97 (cap) — multiSat+0.20, official+0.15
  - **Mayon lahar 연쇄 재해 위험의 트리거**

**산불 (업데이트)**

- **temp-evt-001 update (GA Pineland/Hwy 82)** — CIRA S-NPP VIIRS before/after burn scar + Landsat 8/9 + NASA EO article. 50,000+ acres, 85% contained.
  - confidence: 0.97 (cap) — multiSat+0.20(3위성), thermal+0.10, official+0.15, ba+0.10

### 1-2. HumanActivity (인간활동) — 1건

- **ent-evt-205 (Amazon Xingu gold mining 496k ha)** — PlanetScope + Sentinel-2A 다중위성. Amazon Conservation + ISA 분석. 불법 금 채굴로 인한 삼림벌채 496,000 ha. **phen-mining + phen-defor 이중 매핑.**
  - confidence: 0.97 (cap) — multiSat+0.20, analyst+0.10, ba+0.10

### 1-3. ClimateEnvironment (기후·환경) — 1건

- **ent-evt-201 (Sentinel-2 datacenter fire 장애)** — NorthC datacenter fire in Almere NL. ESA/Copernicus 공식 발표. phen-satops 분류.
  - confidence: 0.97 (cap) — official+0.15
  - **운영적 영향**: Sentinel-2 데이터에 의존하는 다수 이벤트의 후속 관측에 잠정 영향

### 1-4. Defense (국방·안보) — 1건 + 1건 업데이트

- **ent-evt-206 (Balikatan 2026 + PLA Liaoning 14 vessels)** — 남중국해 PLA 항모전단 위성 촬영.
  - confidence: 0.75 — 단일 위성 출처

- **ent-evt-126 update (Iran-US bases 228+)** — Copernicus + Planet 교차검증 상세.
  - confidence: 0.92 — multiSat+0.20

### 1-5. AgriMaritime (농업·해양) — 0건

금일 농업·해양 카테고리 이벤트 없음. 보고서에 "금일 농업·해양 신규 없음" 명시.

## 2. 주요 교차 분석

### 2-1. Mayon-Hagupit 연쇄 재해 위험

| 1차 이벤트 | 2차 위험 | 조건 | 시기 | 신뢰도 |
|-----------|---------|------|------|--------|
| ent-evt-127 (TS Hagupit/Caloy) | ent-evt-082 (Mayon lahar) | PAR entry May 9 → Albay 강우 | 5/9~5/12 | 0.70 (잠정) |

### 2-2. Sentinel-2 데이터 장애의 하류 영향

Sentinel-2A/2C 데이터 장애는 Mayon ashfall, Amazon, GFW 등의 후속 관측에 영향.

### 2-3. 화산 동시 활성 — 5개 위치

| 화산 | 국가 | Alert | 위성 | 센서 유형 |
|-----|------|-------|------|----------|
| Dukono | ID | HIGH (3 deaths) | Himawari-9 | thermal_infrared |
| Mayon | PH | 8km danger zone | Himawari-9 + S2A | thermal + multispectral |
| Kilauea | US | ADVISORY/YELLOW | (예보) | — |
| Great Sitkin | US | WATCH/ORANGE | VIIRS | thermal_infrared |
| Shishaldin | US | ADVISORY/YELLOW | Sentinel-5P | trace_gas (SO2) |

## 3. 위성 활용도 Top

| 위성 | 본 사이클 활용 | 핵심 도메인 |
|------|----------|------------|
| **Himawari-9** (GEO) | 3건 | Dukono/Mayon/Hagupit |
| **Sentinel-2A** (MSI) | 3건 | Mayon/Xingu/Iran |
| **PlanetScope** (Doves) | 3건 | Xingu/Iran/Liaoning |
| **S-NPP VIIRS** | 2건 | GA Pineland/Great Sitkin |
| **Landsat 8/9** | 2건 | GA Pineland burn scar |
| **GOES-18** (GEO) | 1건 | Hagupit 교차검증 |
| **Sentinel-5P TROPOMI** | 1건 | Shishaldin SO2 |
| **Sentinel-2C** (NEW) | 1건 | datacenter fire 장애 |

## 4. 4개 카테고리 커버리지 확인

| 카테고리 | 건수 | 상태 |
|---------|------|------|
| 자연재해 (Disaster) | 7 | ACTIVE |
| 인간활동 (HumanActivity) | 1 | ACTIVE |
| 기후·환경 (Climate/Env) | 1 | ACTIVE |
| 농업·해양 (AgriMarine) | 0 | **금일 신규 없음** |
