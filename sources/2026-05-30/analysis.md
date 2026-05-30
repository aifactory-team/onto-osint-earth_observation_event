# 2026-05-30 온톨로지 분석

## 신규 엔티티

### 이벤트 (3건)
1. **temp-evt-1901**: Sentinel-3 L1/L2 프로덕션 지연
   - 도메인: SatOps
   - 현상: satellite_operations
   - 위성: Sentinel-3A, Sentinel-3B (NRT/STC L1/L2 프로덕트)
   - 분석기관: ESA (Copernicus)
   - 좌표 없음 (지상 세그먼트 글로벌 서비스 이슈)
   - 신뢰도: 0.95 (ESA 공식 공지, officialBoost +0.15)
   - 근거: 5/21~ 지상 세그먼트 이슈로 NRT(Near-Real-Time)/STC(Short-Time-Critical) 프로덕트 지연. 해양(OLCI/SLSTR)·대기 관측 데이터 영향.
   - URL: https://dataspace.copernicus.eu/news/2026-5-26-sentinel-3-l1l2-production-delay

2. **temp-evt-1902**: El Nino 2026 WMO 예보
   - 도메인: AgricultureMaritime + ClimateEnvironment (교차)
   - 현상: ndvi_change (작황 영향) + sea_level_change (SST anomaly)
   - 위성: 위성 SST 데이터 기반 (특정 위성 명시 없음 — 일반 참조)
   - 분석기관: WMO (UN 전문기구)
   - 위치: 0.0°N, 170.0°W (적도 태평양 Nino 3.4 지역)
   - 신뢰도: 0.82 (WMO officialBoost +0.15, 확률적 예보 특성 감안)
   - before/after: false
   - 근거: WMO 예보 60% 확률 여름 2026 El Nino 발생. Super El Nino 가능성. 인도 몬순 92% 평균 예상. 동남아 쌀·설탕·팜유 작황 영향. 위성 SST anomaly 데이터에 기반한 예보이나 직접 위성영상 이벤트는 아님.
   - URL: https://www.rappler.com/environment/explainer-el-nino-potential-impact-world-weather-2026-2027/
   - 비고: 농업·해양 도메인 의무 커버(전일 0건) 확보 목적 포함.

3. **temp-evt-1903**: Sentinel-1A 데이터 유실 5/24
   - 도메인: SatOps
   - 현상: satellite_operations
   - 위성: Sentinel-1A (SAR C-band)
   - 분석기관: ESA (Copernicus)
   - 좌표 없음 (글로벌 SAR 데이터 영향)
   - 신뢰도: 0.95 (ESA 공식 공지, officialBoost +0.15)
   - 근거: 5/24 두 번째 unrecoverable 데이터 유실 (5/19에 이어 월 2회째). temp-evt-1302(5/19 유실)와 시리즈 관계. Sentinel-1A 노후화 패턴 관찰. 4기 콘스텔레이션(A/C/D) 중 A 위성 안정성 우려.
   - URL: https://dataspace.copernicus.eu/news/2026-5-26-copernicus-sentinel-1a-data-unavailability-24-may-2026

## 기존 이벤트 업데이트 (13건)

| 이벤트 ID | 이름 | 변경사항 |
|-----------|------|----------|
| evt-202 | Kilauea Ep48 | 5/29-31 예보, 15.8μrad 팽창, spatter 활동. US |
| evt-082 | Mayon | Day 144+, 287K+ 이재민, AL3 지속. PH |
| evt-1101 | 캐나다 산불 | 33K+ 대피, 2명 사망, Manitoba 지속. CA |
| evt-701 | Bismarck Sea | day 22+, pumice 70km² 유지. PG |
| temp-evt-1401 | Kanlaon | AL2, 화산재 800m. PH |
| evt-801 | Bezymianny | KVERT Orange, explosive 지속. RU |
| evt-203 | Great Sitkin | WATCH/ORANGE, SAR lava dome 동측 확장. US |
| evt-204 | Shishaldin | ADVISORY/YELLOW, SO₂ 관측. US |
| evt-128 | Dukono | 52회/일 폭발, Landsat 9 OLI. ID |
| evt-1201 | Santa Rosa Island | 97% 진압, 18,379ac, 6/6 공식 폐쇄 예정. US |
| ent-evt-kharg | Kharg Island 유출 | 45km², Sentinel-1/2/3 모니터링 지속. IR |
| evt-092 | Antelope Reef | 1,490ac, 군사시설 확인. CN |
| evt-802 | 남레바논 파괴 | Bellingcat 46+ towns, before/after 인터랙티브 맵. LB |

## 엔티티 매칭

### 기존 매칭 (업데이트)
- evt-202: Kilauea 시리즈 Ep48→Ep47→Ep46→Ep45→Ep44 (temporal_progression 확정)
- evt-082: Mayon 2026-01~ 연속 분출 시리즈 (temporal_progression 확정)
- evt-701: Bismarck Sea 2026-05-09~ 시리즈 (temporal_progression 확정)
- temp-evt-1903: → temp-evt-1302 (5/19 유실)와 시리즈. Sentinel-1A 노후화 패턴.
- temp-evt-1901: 기존 Sentinel 운영 이벤트(evt-201 NorthC, temp-evt-1802 CDSE)와 별개 인시던트이나 ESA 인프라 이슈 카테고리 공유.

### 신규 매칭 없음
- 모든 이벤트가 기존 인스턴스로 분류 가능.
- 신규 국가/위성/기관 추가 불필요.

## 스키마 변경
- 없음 (기존 클래스·관계로 충분)

## 추론 적용 (15건)

1. **multiSat_evt-1101**: 캐나다 산불 — GOES-18 + VIIRS + TROPOMI + OMPS + EarthCare = 5위성 3기관 → multiSatBoost +0.20 (유지)
2. **multiSat_kharg**: Kharg Island — Sentinel-1/2/3 = 3위성 3센서 → multiSatBoost +0.20 (유지)
3. **multiSat_evt-701**: Bismarck Sea — VIIRS + MODIS + Landsat 9 + Himawari-9 = 4위성 3기관 → multiSatBoost +0.20 (유지)
4. **official_evt-202**: Kilauea — USGS HVO → officialBoost +0.15
5. **official_evt-128**: Dukono — NASA EO → officialBoost +0.15
6. **official_evt-1901**: Sentinel-3 — ESA → officialBoost +0.15
7. **official_evt-1903**: Sentinel-1A — ESA → officialBoost +0.15
8. **temporal_evt-202**: Kilauea Ep48 → partOfSeries
9. **temporal_evt-082**: Mayon Day 144+ → partOfSeries
10. **temporal_evt-701**: Bismarck Sea day 22+ → partOfSeries
11. **severity_evt-1101**: 캐나다 산불 33K+ 대피 + 2사망 → priorityBoost +0.20
12. **severity_evt-082**: Mayon 287K+ 이재민 → priorityBoost +0.20
13. **sar_evt-203**: Great Sitkin SAR lava dome → sarBoost +0.10
14. **cascading_evt-1101**: 캐나다 산불 → dom-disaster→dom-humanitarian crossDomainLink
15. **ba_evt-802**: 남레바논 Bellingcat before/after → baCredibilityBoost +0.10

## 도메인별 분석

### 자연재해 (Disaster) — 9건
- Kilauea Ep48: 분출 임박, 예보 창 5/29-31
- Mayon: 287K+ 이재민 최고치
- 캐나다 산불: Manitoba 역대급 대피 지속
- Bismarck Sea: 해저화산 day22+
- Kanlaon: AL2 재분출
- Bezymianny: Orange 등급 폭발
- Great Sitkin: WATCH 용암돔
- Shishaldin: ADVISORY SO₂
- Dukono: 52/일 폭발

### 인간활동 (HumanActivity) — 2건
- Kharg Island: 이란 유출 45km²
- Antelope Reef: 중국 군사 매립 1,490ac

### 기후·환경 (ClimateEnvironment) — 1건
- El Nino WMO 예보 (dom-climate 교차)

### 농업·해양 (AgricultureMaritime) — 1건
- El Nino WMO 예보 (dom-agri-marine 교차) — 인도 몬순, 동남아 작황

### 인도주의 (Humanitarian) — 2건
- 캐나다 산불 → 인도주의 교차 (33K+ 대피)
- 남레바논 파괴 (46+ towns)

### SatOps — 2건
- Sentinel-3 L1/L2 지연
- Sentinel-1A 유실 5/24

## 신뢰도 종합

| 이벤트 | 최종 신뢰도 | 핵심 가산 |
|--------|-----------|----------|
| 캐나다 산불 | 0.95 | multiSat+priority+cascading |
| Bismarck Sea | 0.97 | multiSat+official |
| Kilauea Ep48 | 0.95 | official+temporal |
| Mayon | 0.92 | priority+temporal |
| Kharg Island | 0.90 | multiSat+SAR |
| Sentinel-3 지연 | 0.95 | official |
| Sentinel-1A 유실 | 0.95 | official |
| El Nino WMO | 0.82 | official (확률적) |
| Dukono | 0.92 | official (NASA EO) |
| Great Sitkin | 0.90 | SAR |
| 남레바논 | 0.92 | before/after |
| Santa Rosa | 0.88 | — |
| Kanlaon | 0.85 | — |
| Bezymianny | 0.85 | — |
| Shishaldin | 0.80 | — |
| Antelope Reef | 0.90 | — |
