# 2026-05-30 온톨로지 분석

## 엔티티 매칭 요약

- 전체 추출 엔티티: 15건
- 기존 매칭: 12건 (위성·기관·국가·현상 대부분 기존 인스턴스에 매칭)
- 신규 엔티티: 3건 (temp-evt-1901, temp-evt-1902, temp-evt-1903)

## 온톨로지 확장 결정

### 스키마 변경: 없음
기존 클래스(Event, Satellite, Sensor, Organization, Location, Country, Phenomenon, Domain, DataProduct)와 관계 유형으로 금일 모든 이벤트를 표현 가능. 신규 클래스·관계 불필요.

### 신규 인스턴스
1. **temp-evt-1901** (Event) — Sentinel-3 L1/L2 프로덕션 지연. phenomenon: satellite_operations. domain: satops. 좌표 없음(글로벌 인프라).
2. **temp-evt-1902** (Event) — El Niño 2026 WMO 60% 예보. phenomenon: sea_level_change + crop_yield. domain: dom-agri-marine, dom-climate. lat 0.0, lon -170.0 (Niño 3.4).
3. **temp-evt-1903** (Event) — Sentinel-1A 데이터 유실 5/24. phenomenon: satellite_operations. domain: satops. temp-evt-1302(5/19 유실)와 partOfSeries 추론.

### 국가·위성·기관 추가: 없음
금일 신규 국가·위성·기관 없음. 모든 참조는 기존 인스턴스로 커버.

## 추론 규칙 적용

| 규칙 | 적용 대상 | 결과 |
|------|----------|------|
| multi_satellite_confirmation | evt-1101 (캐나다 산불) | multiSatBoost +0.20 유지 (5위성 3기관) |
| multi_satellite_confirmation | ent-evt-kharg (Kharg 유출) | multiSatBoost +0.20 유지 (3위성 3센서) |
| multi_satellite_confirmation | evt-701 (Bismarck Sea) | multiSatBoost +0.20 유지 (4위성 3기관) |
| temporal_progression | evt-202 (Kilauea) | Ep44→45→46→47→48 시리즈 |
| temporal_progression | evt-082 (Mayon) | Day 144+ 연속 |
| temporal_progression | evt-701 (Bismarck Sea) | day 22+ |
| temporal_progression | temp-evt-1903 → temp-evt-1302 | Sentinel-1A 데이터 유실 시리즈 (5/19, 5/24) |
| official_source_trust | evt-202, evt-701, evt-128 | USGS/NASA officialBoost +0.15 |
| sensor_capability_match_sar | evt-203 (Great Sitkin) | SAR 용암돔 구름 투과 관측 — sarBoost +0.10 |
| cascading_disaster | evt-1101 | 산불 → 33K+ 대피 → Humanitarian 교차 도메인 |
| before_after_credibility | evt-802 (Bellingcat Lebanon) | PlanetScope before/after 가용 — baCredibilityBoost +0.10 |

## 도메인별 커버리지

| 도메인 | 금일 건수 | 상태 |
|--------|----------|------|
| Disaster | 10 | 업데이트 10건 (화산 8, 산불 2) |
| HumanActivity | 1 | 업데이트 1건 (유출) |
| ClimateEnvironment | 0 | 전일 신규 보고됨 |
| AgricultureMaritime | 1 | 신규 1건 (El Niño) |
| Defense | 1 | 업데이트 1건 (Antelope Reef) |
| Humanitarian | 1 | 보고됨 (Lebanon) |

모든 4대 카테고리 커버됨 (Climate는 전일 신규, AgriMarine은 금일 신규).
