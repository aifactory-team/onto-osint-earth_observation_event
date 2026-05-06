# 온톨로지 추론 로그

이 파일은 온톨로지 추론 엔진이 생성한 추론 결과를 기록한다.
각 엔트리는 추론 규칙, 입력 트리플, 추론된 트리플, 신뢰도를 포함한다.

도메인: 위성영상 관측 이벤트 (Earth Observation Events).
초기화 일자: 2026-04-30.

---

> 첫 파이프라인 실행 시점부터 추론 결과가 누적된다.

## 2026-04-30 추론 결과

### multi_satellite_confirmation (다중 위성 교차검증) — 9건

- **추론 #1:** ent-evt-001 (영변 UEP) — observedBy WorldView-3 (Maxar) AND PlanetScope (Planet) → multiSatBoost +0.20 [confidence 0.92, 확정]
- **추론 #2:** ent-evt-002 (Sohae) — observedBy PlanetScope + WorldView-3 → multiSatBoost +0.20 [0.88, 확정]
- **추론 #3:** ent-evt-006 (Antelope Reef) — Sentinel-2A + Sentinel-2B + Vantor → multiSatBoost +0.20 [0.90, 확정]
- **추론 #4:** ent-evt-008 (가자 UNOSAT) — WorldView-3 + PlanetScope → multiSatBoost +0.20 [0.85, 확정]
- **추론 #5:** ent-evt-009 (Hektoria) — Sentinel-1A + Sentinel-2A + Landsat 9 → multiSatBoost +0.20 [0.92, 확정]
- **추론 #6:** ent-evt-011 (전지구 메탄) — Sentinel-5P TROPOMI + GOSAT → multiSatBoost +0.20 [0.93, 확정]
- **추론 #7:** ent-evt-012 (Sinlaku) — Himawari-9 + GOES-18 → multiSatBoost +0.20 [0.88, 확정]
- **추론 #8:** ent-evt-013 (Vaianu) — GOES-18 + Himawari-9 → multiSatBoost +0.20 [0.85, 확정]
- **추론 #9:** ent-evt-018 (CEMS GFM) — Sentinel-1A + Sentinel-1C → multiSatBoost +0.20 [0.80, 잠정]

### sensor_capability_match (센서-현상 적합성) — 12건

- **TIRS x volcano:** ent-evt-003 (Piton de la Fournaise) thermalBoost +0.10 [0.93]
- **SAR x volcano:** ent-evt-004 (Kilauea CSG InSAR) sarBoost +0.10 [0.90]
- **SAR x infra damage:** ent-evt-007 (Iran PWTT Sentinel-1) sarBoost +0.10 [0.88]
- **trace_gas x air pollution:** ent-evt-010 (Climate TRACE) tracegasBoost +0.15 [0.88]
- **trace_gas x methane:** ent-evt-011 (TROPOMI+GOSAT) tracegasBoost +0.15 [0.95]
- **SAR x flood:** ent-evt-017 (Sri Lanka ICEYE) sarBoost +0.10 [0.92]
- **SAR x flood:** ent-evt-018 (CEMS GFM) sarBoost +0.10 [0.93]
- **SAR x oilspill:** ent-evt-019 (Cerulean) sarBoost +0.10 [0.92]
- **hi-res x military:** ent-evt-001 (Yongbyon WV-3 0.31m) hiResBoost +0.15 [0.92]
- **hi-res x construction:** ent-evt-002 + ent-evt-006 hiResBoost +0.15 [0.85]
- **hi-res x infra damage:** ent-evt-008 (Gaza WV-3) hiResBoost +0.15 [0.85]

### official_source_trust — 7건

- ent-evt-001 (CSIS BP+IAEA) +0.15 [0.90], ent-evt-003 (NASA+USGS) +0.15 [0.95], ent-evt-004 (USGS HVO) +0.15 [0.95], ent-evt-008 (UNOSAT) +0.15 [0.95], ent-evt-012 (JMA+JAXA+NOAA) +0.15 [0.92], ent-evt-013 (NOAA) +0.15 [0.85], ent-evt-018 (CEMS) +0.15 [0.95].

### korea_geo_focus — 4건

- ent-evt-001 (영변, KP) +0.10 [0.95]
- ent-evt-002 (소해, KP) +0.10 [0.95]
- ent-evt-014 (한반도 산불, KR — 위성 미검증) +0.10 [0.60, 잠정 — 미검증 의혹 분리]
- ent-evt-015 (KOMPSAT-7, KR) +0.10 [0.90]

### disaster_severity_priority — 5건

- ent-evt-003 / 009 / 012 / 013 / 017 (high severity) → priorityBoost +0.20 each [0.85-0.90]

### before_after_credibility — 8건

- ent-evt-001 / 002 / 003 / 006 / 007 / 008 / 009 / 017 모두 전후 비교 또는 시계열 보유 → baCredibilityBoost +0.10 [0.85-0.90]

### 추론 통계

| 규칙 | 건수 | 평균 신뢰도 | 확정/잠정 |
|------|------|-------------|-----------|
| multi_satellite_confirmation | 9 | 0.88 | 8/1 |
| sensor_capability_match | 12 | 0.91 | 12/0 |
| official_source_trust | 7 | 0.92 | 7/0 |
| korea_geo_focus | 4 | 0.85 | 3/1 |
| disaster_severity_priority | 5 | 0.88 | 5/0 |
| before_after_credibility | 8 | 0.88 | 8/0 |
| **합계** | **45** | **0.89** | **43/2** |

### 미적용/제외 추론

- **cascading_disaster:** 동일 지역 7일 내 사슬 미발견.
- **temporal_progression:** 첫 사이클로 이전 보고서 없음.

### 온톨로지 변경

| 변경 유형 | 대상 | 근거 |
|-----------|------|------|
| 새 Phenomenon | phen-infra-damage | Bellingcat Iran SAR PWTT(src-008) + UNOSAT 가자(src-009) Humanitarian SAR 시그니처 |
| 새 Country | co-fr/ir/ps/aq/fm/to/lk/it (8건) | 시드 외 국가 확장 |
| 새 Satellite | sat-cosmoskymed-csg / sat-gosat / sat-kompsat7 / sat-kompsat6 (4건) | 추가 위성 인스턴스 |
| 새 Organization | org-38north / org-rfa (2건) | OSINT 매체 |
| 새 Event | ent-evt-001 ~ ent-evt-019 (19건) | 일별 이벤트 |
| 새 Location | ent-loc-001 ~ ent-loc-007 (7건) | 이벤트 발생 지역 |

config 한도(클래스 3건/일, 관계 5건/일) 내 — 새 클래스 0건, 새 Phenomenon 1건만 추가.

---

## 2026-04-30 추론 결과 (보충 — 2차 수집 사이클)

> 2차 수집 사이클에서 ent-evt-020~028 (9건) 추가, 신규 국가 2건(IS/LB), Sentinel-1D 위성, 신규 위치 6건 반영.

### multi_satellite_confirmation (다중 위성 교차검증) — 4건 추가

- **추론 #10:** ent-evt-020 (조지아 산불) — observedBy Landsat 8 (USGS/NASA) + VIIRS (NOAA/NASA) → multiSatBoost +0.20 [confidence 0.88, 확정] — 서로 다른 플랫폼(Landsat 8 vs Suomi-NPP/JPSS) 열적외+다분광 교차검증
- **추론 #11:** ent-evt-025 (Smith Glacier) — Sentinel-2A (ESA) + Landsat 9 (NASA/USGS) → multiSatBoost +0.20 [0.88, 확정]
- **추론 #12:** ent-evt-027 (Svartsengi) — Sentinel-1A (SAR) + Sentinel-2A (optical) → multiSatBoost +0.20 [0.85, 확정] — 센서 타입 다양성(SAR+광학)
- **추론 #13:** ent-evt-028 (레바논 인프라 파괴) — WorldView-3 (Maxar, optical) + Sentinel-1A (ESA, SAR) → multiSatBoost +0.20 [0.85, 확정]

### sensor_capability_match (센서-현상 적합성) — 8건 추가

- **TIRS x wildfire:** ent-evt-020 (조지아 산불 Landsat 8 TIRS) thermalBoost +0.10 [0.90]
- **SAR x flood:** ent-evt-026 (하와이 홍수 Sentinel-1D SAR) sarBoost +0.10 [0.90]
- **SAR x volcano:** ent-evt-027 (Svartsengi Sentinel-1 InSAR) sarBoost +0.10 [0.90]
- **thermal x volcano:** ent-evt-027 (Svartsengi 열이상) thermalBoost +0.10 [0.85]
- **SAR x infra_damage:** ent-evt-028 (레바논 Sentinel-1 변화탐지) sarBoost +0.10 [0.85]
- **hi-res x naval:** ent-evt-022 (북한 호위함 WV-3 0.31m) hiResBoost +0.15 [0.85]
- **hi-res x infra_damage:** ent-evt-028 (레바논 WV-3) hiResBoost +0.15 [0.85]

### official_source_trust — 1건 추가

- ent-evt-021 (Kilauea Episode 45, USGS HVO) +0.15 [0.95, 확정]

### korea_geo_focus — 3건 추가

- ent-evt-022 (북한 최현급 호위함, KP) +0.10 [0.95, 확정]
- ent-evt-023 (북한 구성 드론, KP) +0.10 [0.95, 확정]
- ent-evt-024 (한국 정찰위성, KR) +0.10 [0.95, 확정]

### disaster_severity_priority — 4건 추가

- ent-evt-020 (조지아 산불, high) → priorityBoost +0.20 [0.85]
- ent-evt-021 (Kilauea Ep.45, high) → priorityBoost +0.20 [0.90]
- ent-evt-026 (하와이 홍수, high) → priorityBoost +0.20 [0.85]
- ent-evt-027 (Svartsengi, high) → priorityBoost +0.20 [0.90]

### before_after_credibility — 5건 추가

- ent-evt-021 (Kilauea Ep.44→45 시계열) +0.10 [0.90]
- ent-evt-022 (호위함 건조 전후) +0.10 [0.85]
- ent-evt-025 (Smith Glacier 42km 후퇴 시계열) +0.10 [0.90]
- ent-evt-026 (하와이 홍수 SAR 전후 비교) +0.10 [0.85]
- ent-evt-027 (Svartsengi 용암류 + InSAR 전후) +0.10 [0.90]
- ent-evt-028 (레바논 파괴 전후 위성 비교) +0.10 [0.85]

### 추론 통계 (보충 사이클)

| 규칙 | 추가 건수 | 누적 건수 | 평균 신뢰도 |
|------|-----------|-----------|-------------|
| multi_satellite_confirmation | 4 | 13 | 0.87 |
| sensor_capability_match | 8 | 20 | 0.88 |
| official_source_trust | 1 | 8 | 0.92 |
| korea_geo_focus | 3 | 7 | 0.90 |
| disaster_severity_priority | 4 | 9 | 0.87 |
| before_after_credibility | 6 | 14 | 0.88 |
| **합계** | **25** | **72** | **0.89** |

### 온톨로지 변경 (보충)

| 변경 유형 | 대상 | 근거 |
|-----------|------|------|
| 새 Country | co-is (아이슬란드), co-lb (레바논) (2건) | Svartsengi 화산 + 레바논 인프라 파괴 이벤트 |
| 새 Satellite | sat-sentinel1d (1건) | ESA Sentinel-1D, SAR, 2025-11 발사, 2026-04-17 운영 개시 — ent-evt-026 하와이 홍수 SAR 매핑 사용 |
| 새 Event | ent-evt-020 ~ ent-evt-028 (9건) | 2차 수집 사이클 이벤트 |
| 새 Location | ent-loc-008 ~ ent-loc-013 (6건) | 이벤트 발생 지역 |
| phen-naval 첫 사용 | ent-evt-022 | 북한 최현급 호위함 건조 — naval_movement Phenomenon 첫 이벤트 참조 |

config 한도 내 — 새 클래스 0건, 기존 Phenomenon (phen-naval) 첫 이벤트 매핑 1건.

---

## 2026-05-01 추론 결과

### multi_satellite_confirmation (다중 위성 교차검증) — 1건 추가

- **추론 #14:** ent-evt-020 (Georgia 산불) — 이전 Landsat 8 (USGS/NASA) + VIIRS/NOAA-21 (NOAA) 교차 검증 확인 강화. NASA Earth Observatory 공식 분석 발표(src-008)로 multiSatBoost 재확인 [confidence 0.95, 확정]

### sensor_capability_match (센서-현상 적합성) — 5건 추가

- **TIRS x volcano:** ent-evt-029 (Mayon 화산 Landsat 8 TIRS) thermalBoost +0.10 [0.93] — 용암 열적외 시그니처 감지
- **thermal x wildfire:** ent-evt-020 (Georgia 산불 VIIRS thermal) thermalBoost +0.10 [0.92] — 활성 화재 전선 열감지
- **SAR x oilspill:** ent-evt-034 (Venezuela Sentinel-1 SAR) sarBoost +0.10 [0.85] — 해수면 SAR 후방산란 감소로 유막 탐지
- **trace_gas x methane:** ent-evt-035 (매립지 메탄 TROPOMI) tracegasBoost +0.15 [0.88] — Sentinel-5P XCH4 컬럼 측정
- **hi-res x military:** ent-evt-031 (MizarVision WorldView-3/Vantor 0.31m) hiResBoost +0.15 [0.80] — 군사 장비·차량 AI 자동 식별

### official_source_trust — 3건 추가

- ent-evt-029 (Mayon, NASA EO 공식 발표) +0.15 [0.93, 확정]
- ent-evt-030 (Shiveluch, VAAC Tokyo/JMA 공식 경보) +0.15 [0.85, 확정]
- ent-evt-020 (Georgia 산불, NASA EO 공식 update 발표) +0.15 [0.95, 확정]

### korea_geo_focus — 2건 추가

- ent-evt-032 (CAS500-2/4 발사, KR 위성) +0.10 [0.95, 확정] — KARI 차세대중형위성
- ent-evt-022 (북한 최현급 IMO 등록 update, KP) +0.10 [0.90, 확정]

### disaster_severity_priority — 1건 추가

- ent-evt-020 (Georgia 산불, 120+ 주택 파괴 — 조지아주 역대 최다) → priorityBoost +0.20 [0.95, 확정]

### before_after_credibility — 2건 추가

- ent-evt-029 (Mayon 화산 Landsat 8 적외선 전후 비교) +0.10 [0.90]
- ent-evt-020 (Georgia 산불 Landsat 8 false-color 전후 burn scar) +0.10 [0.90]

### temporal_progression — 1건 추가

- **추론 #15:** ent-evt-021 (Kilauea Ep45) → partOfSeries ent-evt-004 (Ep44) — 같은 위치(Halemaʻumaʻu), 같은 현상(volcanic_eruption), 시계열 진행. Episode 46 예보(May 5-9)로 시리즈 지속 확인 [confidence 0.92, 확정]

### 추론 통계 (2026-05-01)

| 규칙 | 추가 건수 | 누적 건수 | 평균 신뢰도 |
|------|-----------|-----------|-------------|
| multi_satellite_confirmation | 1 | 14 | 0.88 |
| sensor_capability_match | 5 | 25 | 0.88 |
| official_source_trust | 3 | 11 | 0.92 |
| korea_geo_focus | 2 | 9 | 0.91 |
| disaster_severity_priority | 1 | 10 | 0.88 |
| before_after_credibility | 2 | 16 | 0.88 |
| temporal_progression | 1 | 1 | 0.92 |
| **합계** | **15** | **86** | **0.89** |

### 온톨로지 변경 (2026-05-01)

| 변경 유형 | 대상 | 근거 |
|-----------|------|------|
| 새 Country | co-ph (필리핀), co-ve (베네수엘라) (2건) | Mayon 화산 + Lake Maracaibo 원유 유출 |
| 새 Satellite | sat-cas500-2, sat-cas500-4 (2건) | KARI 차세대중형위성 May 3 발사 예정 |
| 새 Organization | org-mizarvision, org-vantor, org-phivolcs, org-globalwitness (4건) | AI 군사 OSINT + 화산 + 환경 NGO |
| 새 Event | ent-evt-029 ~ ent-evt-036 (8건) | 신규 이벤트 |
| 이벤트 업데이트 | ent-evt-019/020/021/022 (4건) | 후속 보도 반영 |
| 새 Location | ent-loc-014 ~ ent-loc-016 (3건) | Mayon, Shiveluch, Lake Maracaibo |

config 한도 내 — 새 클래스 0건, 새 관계 유형 0건.

## 2026-05-03 추론 결과

### sensor_capability_match (센서-현상 적합성) — 1건

- **추론 #1:** ent-evt-053 (MethaneSAT 글로벌 메탄 평가) — usesSensor trace_gas + phenomenon methane_plume → tracegasBoost +0.15 [confidence 0.90, 확정]

### official_source_trust (공식 기관 신뢰���) — 2건

- **추론 #2:** ent-evt-052 (조지아 산불) — analyzedBy USGS (space_agency) → officialBoost +0.15 [0.90, 확정]
- **추론 #3:** ent-evt-050 (Great Sitkin) — analyzedBy USGS (space_agency) → officialBoost +0.15 [0.85, 확정]

### temporal_progression (시계열 진행) — 2건

- **추론 #4:** ent-evt-048 (Kilauea Ep.46 예보) — locatedIn Halemaʻumaʻu + phenomenon volcanic_eruption + observation_date > ent-evt-021 → partOfSeries ent-evt-021 [0.92, 확정]
- **추론 #5:** ent-evt-049 (Mayon 5/2 분출) — locatedIn Mayon + phenomenon volcanic_eruption + observation_date > ent-evt-029 → partOfSeries ent-evt-029 [0.92, 확정]

### korea_geo_focus (한반도 가산) — 1건

- **추론 #6:** ent-evt-047 (CAS500-2/4 발사) — inCountry KR → koreaBoost +0.10 [0.95, 확정]

### 금일 미적용 규칙

- `multi_satellite_confirmation`: 금일 신규 이벤트 중 2개 이상 독립 위성 교차검증 건 없음. MethaneSAT 단독 관측이나, 기존 TROPOMI/GOSAT 데이터(ent-evt-035)와 교차 가능 — 직접 동일 이벤트가 아니므로 미적용.
- `cascading_disaster`: 금��� 신규 재해 사슬 없음.
- `before_after_credibility`: 금일 ���규 before/after 영상 보유 이벤트 없음.

### 온톨로지 변경 요약

| 변경 | 대상 | 근거 |
|------|------|------|
| 위성 상태 갱신 | sat-cas500-2/4: pre-launch → operational | 발사 성공 + 첫 교신 확인 |
| 새 Organization | org-edf, org-inpe, org-amw (3건) | MethaneSAT 운영(EDF), DETER 운영(INPE), 아마존 채굴 탐지(AMW) |
| phen-mining 첫 매핑 | mention 0→1 (1건) | 아마존 불법 금 채굴 |
| 새 Event | ent-evt-050 ~ ent-evt-056 (7건) | 신규 이벤트 |
| 새 Location | ent-loc-019 (Great Sitkin), ent-loc-020 (Krasheninnikov) (2���) | 신규 위치 |

config 한도 내 — 새 클래스 0건, 새 관계 유형 0건.

## 2026-05-02 추론 결과

### multi_satellite_confirmation (다중 위성 교차검증) — 4건

- **추론 #1:** ent-evt-042 (남극 접지선 30년 연구) — observedBy Sentinel-1A (ESA) + Sentinel-1C (ESA) → multiSatBoost +0.20 [confidence 0.93, 확정]
- **추론 #2:** ent-evt-045 (NASA 조기 산림벌채 탐지) — observedBy Landsat 9 (USGS/NASA) + Sentinel-2A (ESA) + MODIS (NASA) → multiSatBoost +0.20 [0.88, 확정]
- **추론 #3:** ent-evt-046 (ESA 메탄 3종 매핑) — observedBy Sentinel-5P + Sentinel-2A + Sentinel-3 → multiSatBoost +0.20 [0.90, 확정]
- **추�� #4:** ent-evt-043 (상업 위성 군사 전략) — observedBy PlanetScope (Planet) + WorldView-3 (Maxar) → multiSatBoost +0.20 [0.82, 잠정]

### sensor_capability_match (센서-현상 적합성) — 3건

- **SAR × glacier:** ent-evt-042 (남극 접지선) — C-band SAR로 30년 빙하 접지선 관측 → sarBoost +0.10 [0.93, 확정]
- **trace_gas × methane:** ent-evt-046 (메탄 매핑) — TROPOMI로 메탄 초대량 배출원 탐지 → tracegasBoost +0.15 [0.95, 확정]
- **hiRes × military:** ent-evt-043 (군사 전략) — WorldView-3 (0.31m)로 군사 자산 식별 → hiResBoost +0.15 [0.80, 잠정]

### official_source_trust (공식 출처 신���도) — 3건

- ent-evt-037 (PNG 산사태) — analyzedBy NASA + reportedBy Disaster Charter → officialBoost +0.15 [0.95, 확정]
- ent-evt-042 (남극 접지선) — analyzedBy ESA → officialBoost +0.15 [0.95, 확정]
- ent-evt-046 (메탄 매핑) — analyzedBy ESA → officialBoost +0.15 [0.95, 확정]

### before_after_credibility (전후 비교 신뢰도) — 3건

- ent-evt-037 (PNG 산사태) — Landsat 9 before (Sep 2025) / after (Apr 2026) → baCredibilityBoost +0.10 [0.95, 확정]
- ent-evt-044 (Niscemi 산사태) — VHR before (Sep 2025) / after (Feb 2026) → baCredibilityBoost +0.10 [0.90, 확정]
- ent-evt-042 (남극 접지선) — 30년 시계열 → baCredibilityBoost +0.10 [0.93, 확정]

### cascading_disaster (연쇄 재해) — 1건

- **입력:** (ent-evt-037, locatedIn, PNG) AND (ent-evt-038, locatedIn, PNG) AND (TC Maila → landslide → flood, 같은 주)
- **추론:** (ent-evt-038, triggeredBy, ent-evt-037) — TC Maila 강우 → 산사태 → 2차 홍수
- **신뢰도:** 0.85 [확정]

### temporal_progression (시계열 연결) — 1건

- ent-evt-042 (ESA 30년 연구) partOfSeries ent-evt-025 (Smith Glacier 42km 후퇴) → 동일 지역 빙하 후퇴 시계열 [0.85, 확정]

### disaster_severity_priority (재해 우선순위) — 1건

- ent-evt-020 (조지아 산불) — 120+ 가옥 파괴, 고위험 → priorityBoost +0.20 [0.92, 확정]

### 온톨로지 변경

| 변경 유형 | 대상 | 근거 |
|----------|------|------|
| 새 Country | co-pg (파푸아뉴기니), co-pe (페루), co-gt (과테말라) (3건) | TC Maila + Sabancaya + Fuego |
| phen-landslide 첫 매핑 | mention 0→2 (2건) | PNG 산사태 + Niscemi 산사태 |
| 새 Event | ent-evt-037 ~ ent-evt-046 (10건) | 신규 이벤트 |
| 이벤트 업데이트 | ent-evt-020/021/029/030/032 (5건) | 후속 보도 반영 |
| 새 Location | ent-loc-017 (Baining Mts), ent-loc-018 (Niscemi) (2건) | 신규 위치 |

config 한도 내 — �� 클래스 0건, 새 관��� 유형 0건.

---

## 2026-05-04 추론 결과

### multi_satellite_confirmation (다중 위성 교차검증) — 2건

- **추론 #1:** ent-evt-059 (가자 군사 시설 확장) — observedBy PlanetScope (Planet) AND Sentinel-2A (ESA) → multiSatBoost +0.20 [confidence 0.90, 확정] — 독립 운영자 2개(Planet/ESA) 광학 교차검증
- **추론 #2:** ent-evt-068 (그린란드 빙하 후퇴) — observedBy Landsat 8 (USGS/NASA) AND Sentinel-2A (ESA) → multiSatBoost +0.20 [0.82, 확정] — 100년 역사적 사진 + 현대 위성 비교

### sensor_capability_match (센서-현상 적합성) — 1건

- **trace_gas × methane:** ent-evt-066 (MethaneSAT Permian Basin) — usesSensor trace_gas + phenomenon methane_plume → tracegasBoost +0.15 [0.95, 확정] — MethaneSAT 전용 메탄 관측 100m 해상도

### official_source_trust (공식 기관 신뢰도) — 2건

- ent-evt-004 (Kīlauea Ep.46 예보) — analyzedBy USGS HVO (space_agency) → officialBoost +0.15 [0.99, 확정]
- ent-evt-020 (조지아 산불) — analyzedBy NASA EO (space_agency) → officialBoost +0.15 [0.95, 확정]

### korea_geo_focus (한반도 가산) — 1건

- ent-evt-001 (영변 핵단지 활동 증가) — inCountry KP → koreaBoost +0.10 [0.99, 확정]

### temporal_progression (시계열 연결) — 2건

- **추론 #3:** ent-evt-004 update (Kīlauea Ep.46) → partOfSeries ent-evt-021 (Ep.45) — 동일 위치(Halemaʻumaʻu), 동일 현상(volcanic_eruption), 에피소드 연속 [0.95, 확정]
- **추론 #4:** ent-evt-029 update (Mayon 5/2 PDC) → partOfSeries ent-evt-029 — 2026-01 이후 지속 분출 시계열 [0.90, 확정]

### before_after_credibility (전후 비교 신뢰도) — 3건

- ent-evt-020 (조지아 산불) — Landsat 8 false-color burned area 전후 비교 → baCredibilityBoost +0.10 [0.95, 확정]
- ent-evt-028 (레바논 파괴) — Airbus 위성 전후 비교 (523건 건물 파괴 정량) → baCredibilityBoost +0.10 [0.95, 확정]
- ent-evt-068 (그린란드 빙하) — 100년 사진 + 현대 위성 전후 비교 → baCredibilityBoost +0.10 [0.85, 확정]

### 금일 미적용 규칙

- `cascading_disaster`: 금일 신규 재해 사슬 없음.
- `disaster_severity_priority`: 신규 고위험 재해 이벤트 없음 (Kīlauea/조지아/Mayon 모두 이전 이벤트 업데이트).

### 추론 통계 (2026-05-04)

| 규칙 | 추가 건수 | 누적 건수 | 평균 신뢰도 |
|------|-----------|-----------|-------------|
| multi_satellite_confirmation | 2 | 20 | 0.87 |
| sensor_capability_match | 1 | 27 | 0.89 |
| official_source_trust | 2 | 15 | 0.93 |
| korea_geo_focus | 1 | 11 | 0.91 |
| temporal_progression | 2 | 6 | 0.92 |
| before_after_credibility | 3 | 22 | 0.89 |
| **합계** | **11** | **101+** | **0.90** |

### 온톨로지 변경

| 변경 유형 | 대상 | 근거 |
|----------|------|------|
| 새 Country | co-sa (사우디아라비아), co-gl (그린란드) (2건) | 미군 집결 + 빙하 후퇴 |
| 새 Location | ent-loc-021~024 (4건) | Lop Nur, Bint Jbeil, Prince Sultan AB, Permian Basin |
| 새 Event | ent-evt-059/062/063/064/066/068 (6건) | 신규 이벤트 |
| 이벤트 업데이트 | ent-evt-001/004/020/028/029 (5건) | 후속 보도 반영 |

config 한도 내 — 새 클래스 0건, 새 관계 유형 0건.

---

## 2026-05-05 추론 결과

### multi_satellite_confirmation (다중 위성 교차검증) — 1건

- **추론 #1:** ent-evt-074 (네덜란드 't Harde 산불) — observedBy Sentinel-2A (ESA) AND PlanetScope (Planet Labs) → multiSatBoost +0.20 [confidence 0.90, 확정]
  - Sentinel-2A: 2026-04-29 화재 연기 플룸 관측
  - PlanetScope: 2026-04-29 연기 확산 영상 (smoke reached England)
  - 운영자 독립: ESA ≠ Planet Labs → 교차검증 성립

### temporal_progression (시계열 연속 관측) — 3건

- **추론 #2:** ent-evt-070 (Kilauea Ep46) partOfSeries ent-evt-021 (Ep45) [confidence 0.95, 확정]
  - 동일 위치(19.421, -155.287), 동일 현상(volcanic_eruption), Ep45(4/23)→Ep46(5/5)
- **추론 #3:** ent-evt-071 (Mayon 5/5) partOfSeries ent-evt-029 (Mayon ongoing) [confidence 0.95, 확정]
  - 동일 위치(13.257, 123.685), 연속 분출, VAAC 경보 시리즈
- **추론 #4:** ent-evt-072 (Georgia wildfire 5/5) partOfSeries ent-evt-020 (Georgia wildfire 4/30) [confidence 0.95, 확정]
  - 동일 위치(31.2, -82.3), 봉쇄율 진전(64%→85%)

### sensor_capability_match (센서-현상 적합성) — 2건

- **추론 #5:** ent-evt-071 (Mayon 5/5) — observedBy Himawari-9 (GEO, thermal_infrared) + volcanic_eruption → thermalBoost +0.10 [confidence 0.90, 확정]
- **추론 #6:** ent-evt-072 (Georgia wildfire) — observedBy Landsat 8 (OLI+TIRS) + wildfire → thermalBoost +0.10 [confidence 0.90, 확정]

### official_source_trust (공식 기관 신뢰도 가산) — 2건

- **추론 #7:** ent-evt-070 (Kilauea Ep46) — analyzedBy USGS (space_agency) → officialBoost +0.15 [confidence 0.95, 확정]
- **추론 #8:** ent-evt-071 (Mayon 5/5) — analyzedBy PHIVOLCS (space_agency) → officialBoost +0.15 [confidence 0.90, 확정]

### korea_geo_focus (한반도 가산) — 3건

- **추론 #9:** ent-evt-077 (NK Sinpo SLBM) — inCountry KP → koreaBoost +0.10 [confidence 1.0, 확정]
- **추론 #10:** ent-evt-078 (425 정찰위성) — inCountry KR → koreaBoost +0.10 [confidence 1.0, 확정]
- **추론 #11:** ent-evt-079 (CAS500-2 농업) — inCountry KR → koreaBoost +0.10 [confidence 1.0, 확정]

### 종합 신뢰도 산정

| 이벤트 ID | 이벤트명 | 기본 신뢰도 | 가산 | 최종 신뢰도 | 비고 |
|-----------|---------|-----------|------|-----------|------|
| ent-evt-070 | Kilauea Ep46 | 0.80 | officialBoost +0.15 | 0.95 | USGS 공식, 시계열 |
| ent-evt-071 | Mayon 5/5 | 0.75 | officialBoost +0.15, thermalBoost +0.10 | 0.95 | PHIVOLCS+Himawari |
| ent-evt-072 | Georgia wildfire | 0.80 | thermalBoost +0.10 | 0.90 | Landsat 8 TIRS |
| ent-evt-073 | Monte Faeta | 0.65 | — | 0.65 | 위성 출처 간접 |
| ent-evt-074 | Netherlands 't Harde | 0.75 | multiSatBoost +0.20 | 0.95 | Sentinel-2+Planet 교차 |
| ent-evt-075 | Type 004 carrier | 0.85 | hiResBoost +0.15 | 0.95 | SkyFi hi-res tasking |
| ent-evt-076 | US Caribbean | 0.80 | — | 0.80 | Planet imagery 확인 |
| ent-evt-077 | NK Sinpo SLBM | 0.80 | koreaBoost +0.10 | 0.90 | SI Analytics 위성 |
| ent-evt-078 | 425 정찰위성 | 0.85 | koreaBoost +0.10 | 0.95 | 공식 발표 |
| ent-evt-079 | CAS500-2 농업 | 0.70 | koreaBoost +0.10 | 0.80 | 활용 전망 |
| ent-evt-080 | Sanriku M7.7 | 0.50 | — | 0.50 | 위성 미검증 |

### 추론 통계 요약

| 규칙 | 금일 발동 | 누적 | 평균 신뢰도 |
|------|----------|------|-----------|
| multi_satellite_confirmation | 1 | 12 | 0.90 |
| temporal_progression | 3 | 9 | 0.95 |
| sensor_capability_match | 2 | 16 | 0.90 |
| official_source_trust | 2 | 13 | 0.93 |
| korea_geo_focus | 3 | 14 | 1.00 |
| **합계** | **11** | **64** | **0.93** |

### 온톨로지 변경

| 변경 유형 | 대상 | 근거 |
|----------|------|------|
| 새 Country | co-nl (네덜란드) (1건) | 't Harde 산불 위성 관측 |
| 새 Location | ent-loc-025~029 (5건) | Monte Faeta, 't Harde, Dalian, Sinpo, Sanriku |
| 새 Event | ent-evt-070~080 (11건) | 신규 7건 + 업데이트 4건 |
| Organization | org-si-analytics (1건) | SI Analytics — 한국 위성영상 AI 기업 |

config 한도 내 — 새 클래스 0건, 새 관계 유형 0건.
