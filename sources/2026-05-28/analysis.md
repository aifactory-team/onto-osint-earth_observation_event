# 2026-05-28 분석 (Phase 3)

## 온톨로지 변경 사항

### 스키마 변경
- 없음 (기존 스키마로 모든 이벤트 분류 가능)

### 인스턴스 변경
- **evt-128 (Dukono) 업데이트**: NASA EO 공식 기사 발행 — Landsat 9 OLI 2026-05-13 촬영, 52회/일 평균 폭발(5/9-16), 화산재 400-4,300m, AL2, 4km 배제구역. 인도네시아 5월 9개 화산 동시 분출 확인. officialBoost +0.15 (NASA EO 공식). `mention_count` 증가.
- **temp-evt-1702 (DPRK 서해 발사체)**: 신규 이벤트. 2026-05-26 서해 미상 발사체. 합동참모본부 확인, 한미 정밀분석 중. 위성영상 미확인 (satellite_unverified). koreaBoost +0.10 (KP). 신뢰도 0.60 (미검증).

### 이전 보고서 연관관계
- evt-202 (Kilauea) partOfSeries: Ep44→45→46→47→48 시퀀스 — 5/28-30 예보 창, 14.1μrad 확대(13.3→14.1), 수축→재팽창 전환. 오늘이 D-day.
- evt-1101 (캐나다 산불) partOfSeries: 33,000+ 대피 유지, Swan Hills SWF076 통제불능 지속. 연기 대서양 횡단 유럽 확인 유지.
- evt-082 (Mayon) partOfSeries: Day 142+, **287,000+ 이재민(102K→287K 급증)**, PDC 3.8km. AL3 유지.
- evt-701 (Bismarck Sea) partOfSeries: day 20+, 부석 70km², 신규 섬 형성 가능. 1972 이후 최대.
- ent-evt-kharg (Kharg Island) partOfSeries: Sentinel-1/2/3 45km² 유출 확산 지속. multiSatBoost +0.20 유지.

## 추론 적용 결과

| # | 규칙 | 대상 | 결과 | 비고 |
|---|------|------|------|------|
| 1 | multi_satellite_confirmation | 캐나다 산불 (evt-1101) | multiSatBoost +0.20 | GOES-18(NOAA) + VIIRS(NOAA/NASA) + TROPOMI(ESA) — 3위성 3기관 |
| 2 | multi_satellite_confirmation | Kharg Island (ent-evt-kharg) | multiSatBoost +0.20 | Sentinel-1/2/3 — 3위성 3센서 유형(SAR/optical/ocean) |
| 3 | multi_satellite_confirmation | Bismarck Sea (evt-701) | multiSatBoost +0.20 | VIIRS + MODIS + Landsat 9 + Himawari-9 — 4위성 3기관 |
| 4 | official_source_trust | Dukono NASA EO (evt-128) | officialBoost +0.15 | NASA EO Image of the Day 공식 분석 |
| 5 | official_source_trust | Kilauea (evt-202) | officialBoost +0.15 | USGS HVO 공식 업데이트 |
| 6 | sensor_capability_match_tirs | Kilauea (evt-202) | thermalBoost +0.10 | Landsat 9 TIRS 열적외 화산 관측 |
| 7 | sensor_capability_match_sar | Great Sitkin (evt-203) | sarBoost +0.10 | Sentinel-1 SAR 용암돔 관측 |
| 8 | sensor_capability_match_tracegas | Shishaldin (evt-204) | tracegasBoost +0.15 | TROPOMI SO₂ 모니터링 |
| 9 | sensor_capability_match_sar | Kharg Island | sarBoost +0.10 | Sentinel-1 SAR 유막 탐지 |
| 10 | temporal_progression | Kilauea Ep48 | partOfSeries evt-202 | Ep44→45→46→47→48 시퀀스 |
| 11 | temporal_progression | Mayon Day 142+ | partOfSeries evt-082 | 1월 이후 연속 분출 |
| 12 | temporal_progression | Dukono | partOfSeries evt-128 | 1933년 이후 근연속 분출 |
| 13 | korea_geo_focus | DPRK 발사체 | koreaBoost +0.10 | KP 국가 코드 |
| 14 | disaster_severity_priority | Mayon 287K 이재민 | priorityBoost +0.20 | 인명 영향 28.7만명 |
| 15 | disaster_severity_priority | Canada 산불 33K+ 대피 | priorityBoost +0.20 | 인명 대피 3.3만+ |
| 16 | hi-res boost | Antelope Reef | hiResBoost +0.15 | WorldView-3 0.31m 건설 식별 |

## 도메인별 커버리지

| 도메인 | 금일 건수 | 상태 |
|--------|----------|------|
| 자연재해 (Disaster) | 11 | ✅ |
| 인간활동 (HumanActivity) | 3 | ✅ |
| 기후·환경 (ClimateEnvironment) | 2 | ✅ |
| 농업·해양 (AgricultureMaritime) | 0 | ⚠️ 금일 신규 없음 |
| 국방·안보 (Defense) | 3 | ✅ |
| 인도주의 (Humanitarian) | 1 | ✅ |
