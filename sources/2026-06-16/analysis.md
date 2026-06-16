# 분석 노트 — 2026-06-16

## 추론 적용 결과

### 1. multi_satellite_confirmation (다중 위성 교차검증)
- **evt-701 (Bismarck Sea)**: Landsat 9 + Sentinel-2A + Himawari-9 + VIIRS = 4위성 3기관 → `multiSatBoost +0.20` 적용 [유지]
- **evt-1101 (Canada wildfire)**: MODIS (Terra) + VIIRS (JPSS) 독립 열적외 교차검증 → `multiSatBoost +0.20` 적용 [유지]
- **evt-3501 (China Hami)**: WorldView-3 + PlanetScope 독립 확인 → `multiSatBoost +0.20` 적용 [유지]
- **evt-3601 (DPRK reforestation)**: Sentinel-2A + Landsat 9 다분광 NDVI 교차검증 → `multiSatBoost +0.20` 적용 [신규, 잠정 — DailyNK 단독 보도]

### 2. official_source_trust (공식 기관 신뢰도)
- **evt-202 (Kilauea Ep49)**: USGS HVO 공식 화산 정보 통지 → `officialBoost +0.15`
- **evt-701 (Bismarck Sea)**: NASA Earth Observatory Image of Day 공식 기사 → `officialBoost +0.15`
- **evt-3303 (GFM v4.1.1)**: Copernicus EMS 공식 제품 출시 공지 → `officialBoost +0.15`

### 3. temporal_progression (시계열 연속)
- **evt-202**: Ep44→Ep45→Ep46→Ep47→Ep48→Ep49 시리즈. Ep49 분출·종료 확인. 역대 최다 49회 기록 달성 (Pu'u'O'o 47회 초과). partOfSeries 확정.
- **evt-701**: 5/8 분출 → 5/13 FL280 → 6/11 Manus 차단 → 6/16 Admiralty Islands 침입. 영향 범위 지속 확대.
- **evt-082**: Day160→Day161→Day162+. AL3 유지. SO2 범위 1088-3096 t/d.

### 4. cascading_disaster (연쇄 재해)
- **evt-701 → ecological → humanitarian**: 화산 분출 → 부석 뗏목 → Admiralty Islands 침입 → 해초/산호 광합성 차단 → 어류 폐사 → 어업 마비 → 식량 위기 (triggeredBy chain 확대)

### 5. sensor_capability_match (센서-현상 적합성)
- **SAR x flood**: evt-3303 (GFM v4.1.1) — Sentinel-1C/1D C-band SAR 기반 자동 홍수 매핑 → `sarBoost +0.10`
- **hiRes x military**: evt-3501 (Hami) — WorldView-3 0.31m 해상도 → `hiResBoost +0.15` [유지]
- **trace_gas x SO2**: evt-082 (Mayon) — Sentinel-5P TROPOMI SO2 1088-3096 t/d → `tracegasBoost +0.15`

### 6. korea_geo_focus (한반도 가산)
- **evt-3601 (DPRK reforestation KP)**: 북한 iso_code KP → `koreaBoost +0.10`

### 7. before_after_credibility (전후 비교 신뢰도)
- **evt-3201 (Mindanao)**: Sentinel-2 June 14 전후 비교 산사태 영상 → `baCredibilityBoost +0.10`
- **evt-3601 (DPRK reforestation)**: 다년간 NDVI 시계열 비교 → `baCredibilityBoost +0.10`

### 8. disaster_severity_priority (재해 우선순위)
- **evt-082 (Mayon)**: 287K+ 이재민, AL3 Day162+ → `priorityBoost +0.20`
- **evt-1101 (Canada wildfire)**: 1,747 fires, 95 active, 44 OOC, 166,400 ha → `priorityBoost +0.20`

## 최종 신뢰도 순위

| 순위 | Event | Base | Boosts | Final |
|------|-------|------|--------|-------|
| 1 | evt-202 Kilauea Ep49 | 0.85 | +0.15 official | 0.95 |
| 2 | evt-701 Bismarck Sea | 0.80 | +0.20 multi +0.15 official | 0.95 |
| 3 | evt-3201 Mindanao M7.8 | 0.80 | +0.10 baCredibility | 0.95 |
| 4 | evt-3501 China Hami | 0.70 | +0.20 multi +0.15 hiRes | 0.92 |
| 5 | evt-1101 Canada wildfire | 0.75 | +0.20 multi +0.20 priority | 0.90 |
| 6 | evt-082 Mayon Day162+ | 0.80 | +0.20 priority +0.15 tracegas | 0.90 |
| 7 | evt-3303 GFM v4.1.1 | 0.75 | +0.15 official +0.10 sar | 0.90 |
| 8 | evt-3401 AI4CH4 methane | 0.75 | +0.15 official (prev) | 0.90 |
| 9 | evt-203 Great Sitkin | 0.75 | +0.10 (USGS) | 0.85 |
| 10 | evt-204 Shishaldin | 0.70 | +0.10 (USGS) | 0.80 |
| 11 | evt-3601 DPRK reforestation | 0.60 | +0.20 multi +0.10 korea | 0.75 |

## 도메인 커버리지 확인

- Disaster: Kilauea Ep49, Bismarck Sea pumice, Mindanao landslides, Canada wildfire, Mayon, Great Sitkin, Shishaldin, GFM v4.1.1 (8건)
- Human Activity: DPRK reforestation/NDVI, China Hami nuclear silo (2건)
- Climate/Environment: ESA AI4CH4 methane framework (1건)
- Agriculture/Ocean: Bismarck Sea fishery impact / Manus food shortage (cross-domain from Disaster, 1건)

4대 카테고리 모두 커버 확인.

## 전일 대비 주요 변화

1. **Kilauea Ep49 분출·종료**: 전일 예보(June 14-15 most likely)가 정확히 적중. 6/14 09:36 HST 분출, 17:05 종료. 역대 49회로 Pu'u'O'o 47회 기록 초과.
2. **Bismarck Sea 생태 확대**: NASA EO Image of Day 선정. 부석이 Admiralty Islands 해안까지 도달, 해초/산호/어업 피해 확인.
3. **Mindanao 산사태 영상**: Sentinel-2 광학 영상으로 66건 산사태 확인, >500m 대형 산사태 복수.
4. **Canada 산불 급증**: 1,495→1,747 fires, 65+→95 active, 78,800→166,400 ha. 면적 2배 이상 증가.
5. **DPRK 조림 신규**: 북한 제2차 10개년 조림 계획 위성 NDVI 확인 (DailyNK). 한반도 GeoFocus.
