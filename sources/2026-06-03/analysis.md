# 2026-06-03 온톨로지 분석

## 1. 신규 엔티티 (New Entities)

### temp-evt-2301: 북극 해빙 최대면적 역대 최저 타이
- **유형:** Event
- **도메인:** ClimateEnvironment (dom-climate)
- **현상:** sea_level_change (phen-sealevel)
- **위치:** Arctic Ocean (76.0N, 40.0E)
- **위성:** ICESat-2 (ATLAS lidar), AMSR-2
- **기관:** NASA (officialBoost +0.15)
- **신뢰도:** 0.92
- **분석:** 2026년 3월 15일 겨울 최대면적 5.52M sq miles -- 1979년 위성 관측 개시 이래 역대 최저 타이 기록. 바렌츠해 해빙 감소가 주요 원인.

## 2. 업데이트 엔티티 -- 11건

### evt-202: Kilauea Ep48 -> 종료/일시정지
- Ep48 6/1 04:40~13:37 HST(9시간) 분출 후 갑작 종료. Ep49 1-3주 예보.
- temporal_progression, official_source_trust (USGS HVO)

### temp-evt-2001: TS Jangmi -> 일본 본토 상륙
- 태풍->열대폭풍 약화. 6/2 16+ 부상, 48K 정전. 6/3 본토 접근. 300+ 항공편 취소.
- cascading_disaster 잠정, priorityBoost

### temp-evt-1902: El Nino -> SST NINO3.4 +0.9C
- SST +0.9C(5/13주). 모델 +3C 2026 하반기. 6/11 차기 ENSO Discussion.

### evt-701: Bismarck Sea -> day 26+, NASA PACE 확인
- NASA PACE 해수변색 공식 확인. 신규 섬 가능성. 5위성 3기관 유지.

### evt-1101: 캐나다 산불 -> NOAA NESDIS 공식 보고
- NOAA NESDIS 공식 위성 모니터링 보고서 발행.

### evt-082: Mayon Day 148+ -- 라하르 위험 증가
### evt-203/204: Great Sitkin/Shishaldin -- 변동 없음
### temp-evt-1401: Kanlaon -- AL2 지속
### temp-evt-2203: Sangay/Reventador -- 분출 지속
### evt-1201: Santa Rosa -- 97%, 6/6 종결

## 3. 추론 결과 요약

| 추론 규칙 | 건수 | 대상 |
|-----------|------|------|
| multi_satellite_confirmation | 2건 유지 | evt-701, evt-1101 |
| official_source_trust | 4건 | evt-202, temp-evt-1902, evt-701, evt-1101 |
| temporal_progression | 2건 | evt-202, temp-evt-2001 |
| priorityBoost | 2건 | temp-evt-2001, evt-1101 |
| cascading_disaster | 1건 잠정 | temp-evt-2001 |
| sensor_capability_match | 2건 | evt-202, evt-701 |
| korea_geo_focus | 0건 신규 | 기존 5건 유지 |

## 4. 카테고리 커버리지

| 카테고리 | 건수 | 상태 |
|----------|------|------|
| 자연재해 | 11건 | 충분 |
| 인간활동 | 2건 (reported) | 추적 지속 |
| 기후환경 | 3건 | 충분 |
| 농업해양 | 0건 | 금일 신규 없음 |
| 국방안보 | 2건 (reported) | 추적 지속 |
| 인도주의 | 2건 (reported) | 추적 지속 |

## 5. 스키마 변경: 없음
