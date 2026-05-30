# 2026-05-30 보고서 기반

## 포함 결정

### 본문 포함 (16건)

| 소스 | 이벤트 | 도메인 | 판정 |
|------|--------|--------|------|
| src-001 | Sentinel-3 L1/L2 프로덕션 지연 | SatOps | **신규** — SatOps 섹션 |
| src-002 | El Nino 2026 WMO 예보 | AgriMarine+Climate | **신규** — 본문 포함, dom-agri-marine 커버 |
| src-003 | Sentinel-1A 데이터 유실 5/24 | SatOps | **신규** — SatOps 섹션, 5/19 시리즈 |
| src-004 | Kilauea Ep48 5/29-31 | Disaster | **업데이트** — Top 5 |
| src-005 | Mayon 287K+ AL3 Day144+ | Disaster | **업데이트** — Top 5 |
| src-006 | 캐나다 산불 33K+ 대피 | Disaster→Humanitarian | **업데이트** — Top 5 |
| src-007 | Bismarck Sea day22+ | Disaster | **업데이트** — Top 5 |
| src-008 | Kanlaon AL2 ash 800m | Disaster | **업데이트** |
| src-009 | Bezymianny Orange | Disaster | **업데이트** |
| src-010 | Great Sitkin WATCH SAR | Disaster | **업데이트** |
| src-011 | Shishaldin ADVISORY SO₂ | Disaster | **업데이트** |
| src-012 | Dukono 52/day Landsat 9 | Disaster | **업데이트** |
| src-013 | Santa Rosa 97% closed 6/6 | Disaster | **업데이트** |
| src-014 | Kharg Island 45km² | HumanActivity | **업데이트** |
| src-015 | Antelope Reef 1490ac | Defense | **업데이트** |
| src-016 | Bellingcat Lebanon 46+ | Humanitarian | **업데이트** — before/after |

### 미검증 의혹 섹션 (0건)
- 금일 새로운 미검증 이벤트 없음.
- 기존 DPRK 발사체 5/26(temp-evt-1702)은 전일 보고 완료.

### SatOps 섹션 (4건)
| 소스 | 이벤트 | 판정 |
|------|--------|------|
| src-001 | Sentinel-3 L1/L2 지연 | **신규** |
| src-003 | Sentinel-1A 유실 5/24 | **신규** |
| — | Sentinel-1D 4위성 | **보고됨** (이전) |
| — | KOMPSAT-7 0.3m | **보고됨** (이전) |

### 본문 제외 (0건)
- 금일 중복 제외 대상 없음.

## Top 5 선정 (신뢰도 + 영향규모 기준)

1. **Kilauea Ep48** — 0.95 + officialBoost. 5/29-31 예보 창 도래, 15.8μrad, spatter.
2. **Mayon 287K+** — 0.92 + priorityBoost. Day 144+ AL3, 이재민 최고치.
3. **캐나다 산불** — 0.95 + multiSatBoost + priorityBoost + cascading. 33K+ 대피, 2사망.
4. **Bismarck Sea** — 0.97 + multiSatBoost. day 22+, pumice 70km².
5. **El Nino 2026 WMO** — 0.82 + officialBoost. 60% 여름 발생, Super El Nino 가능.

## 도메인별 커버리지

- 자연재해: 9건 (Kilauea, Mayon, Canada, Bismarck, Kanlaon, Bezymianny, Great Sitkin, Shishaldin, Dukono, Santa Rosa)
- 인간활동: 2건 (Kharg Island, Antelope Reef)
- 기후·환경: 1건 (El Nino WMO 예보)
- 농업·해양: 1건 (El Nino WMO 예보 — 작황 영향)
- 국방·안보: 1건 (Antelope Reef 군사시설)
- 인도주의: 2건 (캐나다 산불 교차, 남레바논)
- SatOps: 2건 (Sentinel-3 지연, Sentinel-1A 유실)

4대 카테고리 의무 커버 충족:
- (a) 자연재해: 9건
- (b) 인간활동(개발/군사/산업): 2건
- (c) 기후·환경: 1건
- (d) 농업·해양: 1건

## 한반도 GeoFocus
- 금일 한반도 신규 이벤트 0건.
- 기존 추적: 압록강 교량(보고됨), 두만강 교량(보고됨), KOMPSAT-7(보고됨), DPRK 발사체(보고됨)
- 보고서에 "한반도 금일 신규 없음" 명시.

## 다중 위성 교차검증 현황

| 이벤트 | 위성 수 | 기관 수 | 위성 목록 |
|--------|---------|---------|----------|
| evt-1101 캐나다 산불 | 5 | 3 | GOES-18, VIIRS, Sentinel-5P, OMPS, EarthCare |
| evt-701 Bismarck Sea | 4 | 3 | VIIRS, MODIS, Landsat 9, Himawari-9 |
| ent-evt-kharg Kharg | 3 | 1(ESA) | Sentinel-1, Sentinel-2, Sentinel-3 (3센서) |

## 보고서 구성 권고

1. **재해 섹션 (1순위):** Kilauea → Mayon → 캐나다 산불 → Bismarck Sea → 화산 일람 (Kanlaon, Bezymianny, Great Sitkin, Shishaldin, Dukono) → Santa Rosa
2. **인간활동 섹션:** Kharg Island 유출 → Antelope Reef 군사 매립
3. **기후·환경 섹션:** El Nino 2026 WMO 예보
4. **인도주의 섹션:** 캐나다 산불 교차 → 남레바논 Bellingcat
5. **SatOps 섹션:** Sentinel-3 지연 → Sentinel-1A 유실
6. **미검증 의혹:** 해당 없음 (전일 보고 완료)
7. **한반도 GeoFocus 노트:** 금일 신규 없음
8. **농업·해양 노트:** El Nino 예보로 커버
