# 2026-06-08 온톨로지 분석

## 스키마 변경

금일 스키마 구조적 변경 없음. 기존 클래스·관계로 충분.

## 인스턴스 추가

### 신규 Event (2건)
1. **evt-2801**: 북한 미림비행장 퍼레이드 준비 수송트럭 집결 (KP, dom-defense, PlanetScope)
2. **evt-2802**: NASA EO Typhoon Jangmi 공식 분석 (JP, dom-disaster, Himawari-9+GPM)

### 신규 Location (1건)
- **ent-loc-mirim**: Mirim Training Ground, Pyongyang (39.0°N, 125.85°E)

## 추론 결과

### multi_satellite_confirmation (다중 위성 교차검증)
| 이벤트 | 위성 수 | 독립 기관 | Boost |
|--------|---------|----------|-------|
| evt-1101 캐나다 산불 | 5 | NOAA, NASA, ESA | +0.20 |
| evt-701 비스마르크해 | 5 | USGS/NASA, NOAA, JMA/JAXA, ESA | +0.20 |
| temp-evt-2501 시진핑 방북 | 2 | Vantor, Planet | +0.20 |
| ent-evt-kharg 카르그 유출 | 3 | ESA (S-1/2/3) | +0.20 |
| evt-2802 Jangmi NASA EO | 2 | JMA/JAXA, NASA | +0.20 |

### korea_geo_focus (한반도 가산)
| 이벤트 | 가산 |
|--------|------|
| temp-evt-2501 시진핑 방북 D-Day | +0.10 |
| evt-2801 미림 퍼레이드 준비 | +0.10 |
| temp-evt-2003 구축함 배치 | +0.10 |
| temp-evt-2602 모내기 68.2% | +0.10 |
| temp-evt-1601 압록강 교량 | +0.10 |
| temp-evt-1602 두만강 교량 | +0.10 |
| ent-evt-001 영변 UEP | +0.10 |
| ent-evt-002 소해 발사장 | +0.10 |

### temporal_progression (시계열 시리즈)
- evt-2802 partOfSeries temp-evt-2001 (태풍 Jangmi 시리즈, NASA 공식 분석으로 종결)
- evt-202 시리즈 지속 (Kilauea Ep48→Ep49 예보 단축)
- evt-1101 시리즈 지속 (캐나다 산불 Day30+)

### sensor_capability_match
- evt-204 Shishaldin: TROPOMI trace_gas → tracegasBoost +0.15 (SO₂ 탐지)
- ent-evt-kharg: Sentinel-1 SAR → sarBoost +0.10 (해상 유막 탐지)
- temp-evt-2501: WorldView-3 0.31m → hiResBoost +0.15 (인공구조물 식별)

### official_source_trust
- evt-2802: NASA Earth Observatory 공식 → officialBoost +0.15
- evt-202: USGS HVO → officialBoost +0.15
- temp-evt-2504: ESA Copernicus 공식 → officialBoost +0.15

## 이전 보고서 연관

- **evt-2701** (Santa Rosa 100% 진화): 어제 종결 보고 완료. 추적 종료.
- **evt-2702** (Super El Niño): 어제 신규 보고. 금일 CPC 업데이트로 확인 강화.
- **temp-evt-2504** (Sentinel-1 재구성): D-1 → D-Day(내일 6/9 S-1C 중단)로 긴급도 격상.
- **temp-evt-2501** (시진핑 방북): D-1 → D-Day(오늘 도착)로 긴급도 최고.
