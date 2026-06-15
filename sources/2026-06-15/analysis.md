# 분석 노트 — 2026-06-15

## 추론 적용 결과

### 1. multi_satellite_confirmation (다중 위성 교차검증)
- **evt-3201 (Mindanao M7.8)**: VIIRS 야간광 + Sentinel Asia + Disasters Charter Activation 1034 (17 acquisitions) → `multiSatBoost +0.20` 적용
- **evt-3502 (Amazon 삼림벌채 최저)**: Landsat 8 + Sentinel-2A (DETER 시스템 다중위성 융합) → `multiSatBoost +0.20` 적용
- **evt-3501 (China Hami)**: Reuters 분석에서 WorldView-3 + PlanetScope 독립 확인 → `multiSatBoost +0.20` 적용

### 2. official_source_trust (공식 기관 신뢰도)
- **evt-202 (Kilauea Ep49)**: USGS HVO 공식 발표 → `officialBoost +0.15`
- **temp-evt-1902 (El Niño)**: NOAA 공식 선언 → `officialBoost +0.15`
- **evt-3201 (Mindanao)**: PhilSA 정부기관 분석 → `officialBoost +0.15`

### 3. temporal_progression (시계열 연속)
- **evt-202**: Ep44→Ep45→Ep46→Ep47→Ep48→Ep49 시리즈 연속 (partOfSeries)
- **evt-701**: Bismarck Sea 5/8 분출 시작 → 5/13 FL280 → 6/11 Manus 차단 (시간 경과 따른 영향 확대)

### 4. cascading_disaster (연쇄 재해)
- **evt-701 → humanitarian impact**: 화산 분출 → 부석 뗏목 → 해상교통 차단 → 식량 위기 위협 (triggeredBy chain)

### 5. sensor_capability_match_hires (고해상도 광학 가산)
- **evt-3501 (Hami)**: WorldView-3 0.31m 해상도로 개별 발사대·차량·시설 식별 → `hiResBoost +0.15`
- **evt-3402 (Pyongsan)**: 고해상도 광학으로 화물열차·시설 확장 식별 → `hiResBoost +0.15`

### 6. korea_geo_focus (한반도 가산)
- **evt-3402 (Pyongsan KP)**: 북한 영토 → `koreaBoost +0.10`

## 최종 신뢰도 순위

| 순위 | Event | Base | Boosts | Final |
|------|-------|------|--------|-------|
| 1 | evt-3201 Mindanao M7.8 | 0.80 | +0.20 multi +0.15 official | 0.95 |
| 2 | evt-202 Kilauea Ep49 | 0.85 | +0.15 official | 0.95 |
| 3 | temp-evt-1902 El Niño | 0.85 | +0.15 official | 0.95 |
| 4 | evt-3501 China Hami | 0.70 | +0.20 multi +0.15 hiRes | 0.92 |
| 5 | evt-701 Bismarck Sea | 0.80 | +0.10 (Himawari official) | 0.90 |
| 6 | evt-3301 Vietnam Spratly | 0.80 | +0.10 (PlanetScope) | 0.90 |
| 7 | evt-3502 Amazon DETER | 0.70 | +0.20 multi | 0.88 |
| 8 | evt-3402 Pyongsan | 0.70 | +0.15 hiRes +0.10 korea | 0.85 |
| 9 | evt-1101 Canada wildfire | 0.75 | +0.10 (VIIRS/MODIS multi) | 0.85 |
| 10 | evt-082 Mayon | 0.80 | (지속 추적) | 0.80 |

## 도메인 커버리지 확인

- ✅ 자연재해: Kilauea, Bismarck Sea, Mindanao, Mayon, Great Sitkin, Canada wildfire (6건)
- ✅ 인간활동: Vietnam Spratly, Sentinel-1 constellation, Pyongsan (3건)
- ✅ 기후·환경: El Niño (1건)
- ✅ 농업·해양: Amazon deforestation (1건)
- ✅ 국방·안보: China Hami, Pyongsan (2건)
- (인도주의: Bismarck Sea 식량위기 요소로 cross-domain 커버)
