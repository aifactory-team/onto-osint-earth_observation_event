# 2026-05-29 온톨로지 분석

## 신규 엔티티

### 이벤트 (2건)
1. **temp-evt-1801**: 미국 토지교란 유형 변화 — Landsat 35년 분석 (Nature Geoscience)
   - 도메인: ClimateEnvironment
   - 현상: ndvi_change (토지 교란 유형 변화 — 산불·허리케인 증가 vs 벌목·농업확장 감소)
   - 위성: Landsat 8, Landsat 9 (+ Landsat 5/7 역사적 데이터)
   - 분석기관: NASA (EO Image of the Day 5/28), USGS (Landsat 운영)
   - 위치: Continental US (39.0°N, 98.0°W — 중심점)
   - 신뢰도: 0.92 (officialBoost +0.15 NASA/USGS, Nature Geoscience peer-reviewed)
   - before/after: true (35년 시계열)
   - 근거: NASA EO Image of the Day 5/28 발행. Zhe Zhu 주도, 40년 Landsat 데이터 + ML 알고리즘으로 50,000개 지점 분류. 75%+ 정확도.

2. **temp-evt-1802**: Sentinel-2 CDSE 카탈로그 발행 장애 (5/28)
   - 도메인: SatOps
   - 현상: satellite_operations
   - 위성: Sentinel-2A, 2B, 2C
   - 분석기관: ESA (Copernicus)
   - 좌표 없음 (글로벌 서비스 장애)
   - 신뢰도: 0.90 (ESA 공식 공지)
   - 근거: 05:45 CEST 시작, 10:45 CEST 복구. 약 5시간 중단. CLMS 제품 포함. 이전 5/8 NorthC datacenter fire(evt-201)와 별개.

## 기존 이벤트 업데이트 (13건)

| 이벤트 ID | 이름 | 변경사항 |
|-----------|------|----------|
| evt-202 | Kilauea Ep48 | 5/28-30 예보 유지, 편향 지연 가능. ADVISORY/YELLOW |
| evt-1101 | 캐나다 산불 | Manitoba "largest evacuation in living memory", Flin Flon 17K, 총 33K+, 2사망 |
| evt-701 | Bismarck Sea | day 21+, pumice 70km², The Watchers 5/28 신규 섬 가능 |
| evt-082 | Mayon | Day 143+, 287K+ 이재민, AL3, PDC 3.8km |
| temp-evt-1401 | Kanlaon | AL2, 화산재 800m, SO₂ 상승 |
| evt-801 | Bezymianny | 5/18 화산재 6km, 5/19 pyroclastic flow, KVERT Orange |
| evt-203 | Great Sitkin | WATCH/ORANGE, 용암돔 확장, SAR 관측 |
| evt-204 | Shishaldin | ADVISORY/YELLOW, SO₂, 지진 |
| evt-1201 | Santa Rosa Island | 97% 진압, mop-up 복구 |
| ent-evt-kharg | Kharg Island 유출 | Sentinel-1/2/3 모니터링, 45km² |
| evt-092 | Antelope Reef | 1490ac, 건물 50+, 활주로 기초 |
| evt-802 | 남레바논 파괴 | Bellingcat PlanetScope before/after (보고됨) |
| temp-evt-1702 | DPRK 발사체 | 미검증 (보고됨) |

## 스키마 변경
- 없음 (기존 클래스·관계로 충분)

## 추론 적용 (12건)

1. **multiSat_evt-1101**: 캐나다 산불 — GOES-18 + VIIRS + TROPOMI + OMPS + EarthCare = 5위성 3기관 → multiSatBoost +0.20 (유지)
2. **multiSat_kharg**: Kharg Island — Sentinel-1/2/3 = 3위성 3센서 → multiSatBoost +0.20 (유지)
3. **multiSat_evt-701**: Bismarck Sea — VIIRS + MODIS + Landsat 9 + Himawari-9 = 4위성 3기관 → multiSatBoost +0.20 (유지)
4. **multiSat_evt-1801**: NASA EO Landsat — Landsat 8 + Landsat 9 = 2위성 동일기관(USGS/NASA) → multiSatBoost 미적용 (동일 운영자)
5. **official_evt-202**: Kilauea — USGS HVO → officialBoost +0.15
6. **official_evt-1801**: Landsat 분석 — NASA EO → officialBoost +0.15
7. **official_evt-701**: Bismarck Sea — NASA EO → officialBoost +0.15 (유지)
8. **temporal_evt-202**: Kilauea Ep48 → partOfSeries Ep47/46/45/44
9. **temporal_evt-082**: Mayon Day 143+ → partOfSeries Day 142+
10. **severity_evt-1101**: 캐나다 산불 33K+ 대피 + 2사망 → priorityBoost +0.20
11. **severity_evt-082**: Mayon 287K+ 이재민 → priorityBoost +0.20
12. **sarBoost_kharg**: Kharg Island Sentinel-1 SAR → sarBoost +0.10
