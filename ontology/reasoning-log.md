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

---

## 2026-05-06 추론 결과

### multi_satellite_confirmation (다중 위성 교차검증) — 4건

- **추론 #1:** ent-evt-082 (Mayon 5/6 ashfall 87 barangays) — observedBy Sentinel-2A (ESA, MSI 10m) AND Himawari-9 (JMA/JAXA, GEO IR) → multiSatBoost +0.20 [confidence 0.92, 확정]
  - Sentinel-2A: PhilSA NICA-DOST 8,544 ha ashfall 매핑
  - Himawari-9: VAAC Tokyo 1252Z eruption advisory
  - 운영자/궤도 독립: ESA SSO ≠ JAXA GEO → 강한 교차검증
- **추론 #2:** ent-evt-083 (Cordoba flood) — observedBy Sentinel-1A (SAR) AND Sentinel-2A (MSI) → multiSatBoost +0.20 [0.95, 확정]
  - Copernicus EMSR865 Rapid Mapping 표준 멀티센서 활용
  - SAR(야간/구름 투과 침수범위) + MSI(피해지 광학 검증) 상보적
- **추론 #3:** ent-evt-084 (ESA MARS methane system) — observedBy Sentinel-5P TROPOMI + CAMS multi-sensor (Sentinel-3 OLCI/SLSTR, GHGSat 융합) → multiSatBoost +0.20 [0.90, 확정]
  - MARS는 다중 데이터 소스 통합 detection 시스템
- **추론 #4:** ent-evt-092 (Antelope Reef 1,490 acres) — observedBy WorldView-3 (Vantor) AND PlanetScope (Planet) → multiSatBoost +0.20 [0.90, 확정]
  - 독립 운영자 교차검증 (Vantor ≠ Planet Labs)
  - AMTI Island Tracker — 시계열 매립 진전 추적

### temporal_progression (시계열 연속 관측) — 3건

- **추론 #5:** ent-evt-081 (Kilauea Ep46 종료, 9시간 lava fountaining) partOfSeries ent-evt-070 (Ep46 개시) → 직접 후속 [0.97, 확정]
  - 5/5 08:17 HST 개시 → 5/5 17:17 HST 종료 → 5/6 02:25 ADVISORY 강등
  - 동일 위치(Halemaʻumaʻu), 동일 episode 번호
- **추론 #6:** ent-evt-082 (Mayon 5/6 ashfall) partOfSeries ent-evt-071 (Mayon 5/5 VAAC) → 직접 후속 [0.96, 확정]
  - 5/3 phreatic eruption → 5/5 VAAC → 5/6 PhilSA satellite ashfall map (87 barangays)
- **추론 #7:** ent-evt-082 partOfSeries ent-evt-029 (Mayon 2026-01~ 분출 시리즈) → 장기 시리즈 시점 갱신 [0.92, 확정]

### cascading_disaster (재해 사슬) — 2건

- **추론 #8:** ent-evt-082 (Mayon ashfall) → src-009 (Guinobatan 호흡기 환자 증가) → triggeredBy 인과 [0.85, 확정]
  - 화산재 운(ash plume)이 Albay 87 barangays 덮음 → Guinobatan 보건소 호흡기 환자 logged
  - 자연재해 → 인도주의(보건) 사슬
- **추론 #9:** ent-evt-093 (Pine Island 가속) → ent-evt-042 (남극 30년 접지선 후퇴 종합) → triggeredBy [0.75, 잠정]
  - Pine Island 단일 빙하 가속이 광역 climate cascading의 일부
  - 신뢰도 0.75 — 동일 사슬이 아닌 종속 관측이라 잠정 처리

### sensor_capability_match — 8건

- **TIRS x volcano:** ent-evt-082 (Mayon Himawari-9 GEO IR) thermalBoost +0.10 [0.92, 확정]
  - IR8.6/IR10.4 채널이 화산재(ash plume) 탐지에 최적
- **SAR x flood:** ent-evt-083 (Cordoba S1A C-SAR) sarBoost +0.10 [0.95, 확정]
  - C-band SAR — 야간/구름 투과 침수범위 매핑 표준 (CEMS)
- **SAR x glacier_retreat:** ent-evt-093 (Pine Island S1A C-SAR offset tracking) sarBoost +0.10 [0.99, 확정]
  - Sentinel-1 offset tracking — 빙류 속도 측정 표준 기법 (10.6→12.7 m/day)
- **trace_gas x methane:** ent-evt-084 (Sentinel-5P TROPOMI 2.3 µm SWIR CH4 흡수밴드) tracegasBoost +0.15 [0.95, 확정]
- **hi-res x military:** ent-evt-086 (영변 UEP WV-3 0.31m) hiResBoost +0.15 [0.90]
- **hi-res x construction:** ent-evt-088 (Yelabuga UAV factory expansion WV-3) hiResBoost +0.15 [0.85]
- **hi-res x infra_damage:** ent-evt-089 (Tehran 15 경찰서 PlanetScope SkySat) hiResBoost +0.15 [0.92]
- **hi-res x construction:** ent-evt-092 (Antelope Reef WV-3 매립/구조물 식별) hiResBoost +0.15 [0.88]

### official_source_trust — 6건

- ent-evt-081 (USGS HVO) +0.15 [0.97]
- ent-evt-082 (PhilSA + VAAC Tokyo) +0.15 [0.95]
- ent-evt-083 (Copernicus EMS UN body) +0.15 [0.99]
- ent-evt-084 (ESA + CAMS) +0.15 [0.99]
- ent-evt-091 (KARI 정책브리핑) +0.15 [0.95]
- ent-evt-093 (ESA Sentinel-1 decade analysis) +0.15 [0.99]

### commercial_imagery_provider — 2건

- ent-evt-085 (Vantor D2D 시험) commercialBoost +0.10 [0.85]
- ent-evt-094 (Planet Pelican-7/8/9 발사) commercialBoost +0.10 [0.85, 보도자료성 0.7 cap 적용]

### analyst_org_trust — 5건

- ent-evt-086 (CSIS BP Yongbyon) +0.10 [0.92]
- ent-evt-088 (CSIS BP Yelabuga) +0.10 [0.92]
- ent-evt-089 (Bellingcat Tehran) +0.10 [0.95]
- ent-evt-092 (CSIS AMTI Antelope) +0.10 [0.92]
- ent-evt-095 (Al Jazeera Sudan NDVI) +0.10 [0.85]

### korea_geo_focus — 4건

- ent-evt-086 (KP — Yongbyon UEP) +0.10 [0.99]
- ent-evt-087 (KP — Panghyon UAV) +0.10 [0.99]
- ent-evt-090 (KP — DPRK 산불 보도, 위성 미검증) +0.10 [0.99, 의혹 분리]
- ent-evt-091 (KR — CAS500-1 산불 복구) +0.10 [0.99]

### disaster_severity_priority — 6건

- ent-evt-081 (Highway 11 tephra 인프라 영향) +0.20 [0.85]
- ent-evt-082 (87 barangays + 호흡기 환자) +0.20 [0.95]
- ent-evt-083 (CEMS 발동) +0.20 [0.92]
- ent-evt-089 (Tehran 15 경찰서 인프라 피해) +0.20 [0.90]
- ent-evt-093 (글로벌 해수면 영향) +0.20 [0.90]
- ent-evt-095 (Sudan 식량안보) +0.20 [0.90]

### before_after_credibility — 6건

- ent-evt-081 (Kilauea USGS photo chronology) +0.10 [0.92]
- ent-evt-082 (Mayon ashfall 분출 전후) +0.10 [0.92]
- ent-evt-089 (Tehran PlanetScope 전후) +0.10 [0.92]
- ent-evt-092 (Antelope Reef AMTI 시계열) +0.10 [0.92]
- ent-evt-093 (Pine Island 2016→2026 10년 시계열) +0.10 [0.95]
- ent-evt-095 (Sudan 전쟁 전후 NDVI) +0.10 [0.90]

### supersedes — 1건

- **추론 #지타:** ent-evt-085 supersedes ent-evt-064 (Planet Iran 무기한 배포 중단 → Vantor가 우크라이나 D2D로 대체 모델) [0.85]
  - 단, Vantor는 Maxar 출신, Planet과 다른 사업자 — 동일 시장의 대체이지 동일 조직 supersede 아님

### 종합 신뢰도 산정

| 이벤트 ID | 이벤트명 | 기본 | 가산 | 최종 | 비고 |
|-----------|---------|------|------|------|------|
| ent-evt-081 | Kilauea Ep46 종료 | 0.78 | official+0.15, priority+0.20, ba+0.10 | 0.95 (cap) | USGS 공식, 시계열 |
| ent-evt-082 | Mayon ashfall 87 barangays | 0.78 | multiSat+0.20, official+0.15, thermal+0.10, priority+0.20, ba+0.10 | 0.97 (cap) | 다중위성 + PhilSA 공식 |
| ent-evt-083 | Cordoba flood EMSR865 | 0.85 | multiSat+0.20, official+0.15, sar+0.10, priority+0.20, analyst+0.00 | 0.97 (cap) | CEMS 멀티센서 |
| ent-evt-084 | ESA MARS methane | 0.85 | multiSat+0.20, official+0.15, tracegas+0.15 | 0.97 (cap) | ESA + CAMS |
| ent-evt-085 | Vantor D2D 우크라이나 | 0.78 | commercial+0.10 | 0.80 | 보도자료성 cap |
| ent-evt-086 | 영변 UEP 후속 | 0.85 | hiRes+0.15, analyst+0.10, korea+0.10 | 0.95 (cap) | CSIS BP |
| ent-evt-087 | Panghyon UAV | 0.75 | korea+0.10 | 0.80 | CSIS BP |
| ent-evt-088 | Yelabuga UAV expansion | 0.78 | hiRes+0.15, analyst+0.10 | 0.95 | CSIS BP |
| ent-evt-089 | Tehran 15 경찰서 | 0.85 | hiRes+0.15, analyst+0.10, priority+0.20, ba+0.10 | 0.97 (cap) | Bellingcat |
| ent-evt-090 | DPRK 조선중앙TV 산불 | 0.50 | korea+0.10 | 0.55 | 위성 미검증 (의혹) |
| ent-evt-091 | CAS500-1 산불 복구 | 0.75 | official+0.15, korea+0.10 | 0.95 (cap) | KARI |
| ent-evt-092 | Antelope Reef 1490 acres | 0.85 | multiSat+0.20, hiRes+0.15, analyst+0.10, ba+0.10 | 0.97 (cap) | AMTI |
| ent-evt-093 | Pine Island 가속 | 0.85 | official+0.15, sar+0.10, priority+0.20, ba+0.10 | 0.97 (cap) | ESA |
| ent-evt-094 | Planet Pelican 7-9 | 0.55 | commercial+0.10 | 0.65 | 보도자료성 cap (0.7) |
| ent-evt-095 | Sudan breadbasket | 0.78 | analyst+0.10, priority+0.20, ba+0.10 | 0.95 | Al Jazeera |
| ent-evt-096 | Climate TRACE 오차 | 0.65 | — | 0.65 | 학술 발견, 위성 직접 관측 아님 |
| ent-evt-097 | 카리브해 군사 집결 | 0.70 | — | 0.70 | Wiki 종합, 단일 출처 |

### 추론 통계 요약

| 규칙 | 금일 발동 | 누적 (~05-06) | 평균 신뢰도 |
|------|----------|------|-----------|
| multi_satellite_confirmation | 4 | 16 | 0.92 |
| temporal_progression | 3 | 12 | 0.95 |
| cascading_disaster | 2 | 2 | 0.80 |
| sensor_capability_match | 8 | 24 | 0.93 |
| official_source_trust | 6 | 19 | 0.97 |
| commercial_imagery_provider | 2 | 4 | 0.85 |
| analyst_org_trust | 5 | 7 | 0.91 |
| korea_geo_focus | 4 | 18 | 0.99 |
| disaster_severity_priority | 6 | 17 | 0.91 |
| before_after_credibility | 6 | 20 | 0.92 |
| supersedes | 1 | 1 | 0.85 |
| **합계** | **47** | **140** | **0.92** |

### 온톨로지 변경

| 변경 유형 | 대상 | 근거 |
|----------|------|------|
| 새 Country | co-sd (수단) (1건) | Sudan breadbasket NDVI Al Jazeera |
| 새 Location | ent-loc-030~038 (9건) | Halemaʻumaʻu, Cordoba, Panghyon, Yelabuga, Tehran, 황해북도/개성, Antelope Reef, Pine Island, Sudan agricultural belt |
| 새 Satellite | sat-pelican (1건) | Planet Pelican-7/8/9 fleet 9기 |
| 새 Organization | org-philsa, org-vaac-tokyo, org-amti, org-aljazeera, org-cams, org-nau (6건) | 각 기관 첫 참조 |
| 새 Event | ent-evt-081~097 (17건) | 신규 17건 |
| 이벤트 업데이트 | ent-evt-070→081(Kilauea), ent-evt-071→082(Mayon), ent-evt-001→086(영변), ent-evt-006→092(Antelope), ent-evt-076→097(Caribbean) (5건) | 후속 보도 반영 |

config 한도 내 — 새 클래스 0건 (max_new_classes_per_day=3), 새 관계 유형 0건 (max_new_relations_per_day=5).

### 미적용/제외 추론

- **3+ 단계 추론:** 발견되지 않음 (모든 추론 1단계 직접)
- **공간적 근접 (nearby):** 기존 location 간 nearby 관계 신규 미발견
- **DPRK 조선중앙TV (ent-evt-090):** 위성 영상 부재 → satellite_unverified, 보고서 본문에서 "미검증 의혹" 섹션으로 분리, koreaBoost는 적용했으나 final confidence cap 0.5 미만 유지

---

## 2026-05-07 (Phase 3-4)

입력: sources/2026-05-07/entities.json (80 entities, 105 explicit relations, 13 신규 + 67 매칭). 이벤트 26건.

### 다중 위성 교차검증 (multi_satellite_confirmation, +0.20)

- **추론 #1:** ent-evt-098 (GA Pineland) — Landsat 8 + Landsat 9 (USGS/NASA 동일 사업자) → 약가산 [0.92, 약가산 시계열]
- **추론 #2:** ent-evt-100 (글로벌 화산) — VIIRS(NOAA/NASA) + Himawari-9(JMA/JAXA) → multiSatBoost +0.20 [0.85, 확정]
- **추론 #3:** ent-evt-106 (Amazon 임계점 PIK) — Sentinel-2A(ESA) + Landsat 9(USGS/NASA) → multiSatBoost +0.20 [0.90, 확정]
- **추론 #4:** ent-evt-109 (Myanmar 홍수) — Sentinel-1A/C/D 3기 동일사업자(ESA)지만 cross-platform → 약가산 [0.85]
- **추론 #5:** ent-evt-111 (NLL 어선) — VIIRS(NOAA) + Sentinel-1A(ESA), 광학+SAR cross-modal → multiSatBoost +0.20 [0.88, 확정]
- **추론 #6:** ent-evt-112 (Silivri 매립지) — Tanager-1(Planet/CarbonMapper) + EMIT(NASA) → multiSatBoost +0.20 [0.95, 확정]
- **추론 #7:** ent-evt-118 (Hektoria) — Sentinel-1A + Sentinel-2A 동일사업자지만 SAR+MSI cross-modal → 약가산 [0.92]
- **추론 #8:** ent-evt-119 (GFW) — Landsat 9 + Sentinel-2A + Sentinel-1A → multiSatBoost +0.20 [0.95, 확정]
- **추론 #9:** ent-evt-120 (Antelope Reef) — Sentinel-2(ESA) + WV-3(Maxar) → multiSatBoost +0.20 [0.95, 확정]
- **추론 #10:** ent-evt-123 (Brazil Apr) — Sentinel-2A + Landsat 9 → multiSatBoost +0.20 [0.92, 확정]

총 10건 multi_satellite_confirmation 후보 중 8건 강가산, 2건 약가산(동일사업자 cross-modal).

### 시계열 진행 / 시리즈 (temporal_progression, partOfSeries)

- **추론 #11:** ent-evt-101 (Kilauea Ep46) :partOfSeries ent-evt-081 (Kilauea Ep46 직전 사이클) → 동일 위치 동일 phenomenon 시계열 [0.95, 확정]
- **추론 #12:** ent-evt-102 (Mayon Advisory 567) :partOfSeries ent-evt-082 (Mayon ashfall 87 barangays) → 05-03 ash → 05-05 advisory [0.95, 확정]
- **추론 #13:** ent-evt-123 (Brazil Apr -67.9%) :partOfSeries ent-evt-106 (PIK 임계점 study) → 동일 위치 동일 deforestation [0.92, 확정]
- **추론 #14:** ent-evt-119 (GFW 2026 보고) :partOfSeries 사이클간 GFW deforestation 시리즈 → 약신뢰 [0.85]

### Supersedes (이전 사이클 이벤트 대체)

- **추론 #15:** ent-evt-115 (영변 UEP 후속) :supersedes ent-evt-086 (직전 사이클 영변 follow-up) — CSIS BP 새 imagery [0.85]
- **추론 #16:** ent-evt-103 (UN MARS 운영) :supersedes ent-evt-084 (직전 ESA MARS preview) — preview→공식 운영 시작 [0.85]
- **추론 #17:** ent-evt-117 (Sentinel-1D commissioning 완료) :supersedes ent-evt-026 (2026-04-17 commissioning 시작 분) — 4-sat live entry [0.85]
- **추론 #18:** ent-evt-120 (Antelope airbase) :supersedes ent-evt-092 (1490 acres expansion) — 매립→비행장 단계 [0.85]

### Cascading Disaster (시간차 인과)

- **본 사이클:** 동일 위치·시간차 disaster 패턴 미발견. Mayon→Guinobatan ashfall 류 cascading은 전 사이클에서 이미 추론됨. 이번 Krasheninnikov(RU)·Mayon(PH)·Kilauea(US)·Myanmar 홍수(MM)는 각기 독립 위치이며, 단일 phenomenon만 활성화.

### Sensor Capability Match

- **TIRS×wildfire:** ent-evt-098 (GA Pineland Landsat TIRS) → thermalBoost +0.10 [0.95]
- **VIIRS thermal×volcano:** ent-evt-099 (Krasheninnikov 1MW thermal flux) → thermalBoost +0.10 [0.92]
- **C-SAR×cloudy(Asia monsoon):** ent-evt-109 (Myanmar) sarBoost +0.10 [0.92]
- **C-SAR×ship detect:** ent-evt-111 (NLL VIIRS+S1A) sarBoost +0.10 [0.90]
- **X-SAR×tropics:** ent-evt-108 (ICEYE deforestation) sarBoost +0.10 [0.92]
- **C-SAR×polar:** ent-evt-118 (Hektoria) sarBoost +0.10 [0.92]
- **C-SAR×oilspill:** ent-evt-124 (Cerulean SkyTruth) sarBoost +0.10 [0.92]
- **trace_gas×methane:** ent-evt-103 (TROPOMI), ent-evt-112 (Tanager+EMIT), ent-evt-122 (MethaneSAT) → tracegasBoost +0.15 each [0.97, 0.97, 0.99]
- **hi-res×military_buildup/construction:** ent-evt-115 (영변 WV-3), ent-evt-116 (Sohae WV-3), ent-evt-120 (Antelope WV-3) → hiResBoost +0.15 each [0.95]

총 13건 sensor_capability 발동.

### 공식 출처 신뢰 (official_source_trust, +0.15)

- ent-evt-098 (NASA EO) [0.97], ent-evt-101 (USGS HVO) [0.99], ent-evt-102 (VAAC Tokyo+PHIVOLCS) [0.95], ent-evt-103 (ESA+UN MARS) [0.97], ent-evt-104 (ESA Copernicus dataspace) [0.99], ent-evt-106 (PIK 학술 — Nature) [0.95], ent-evt-109 (CEMS) [0.92], ent-evt-110 (KARI) [0.99], ent-evt-113 (KARI) [0.99], ent-evt-117 (ESA) [0.99], ent-evt-118 (NASA EO) [0.99], ent-evt-119 (GFW analyst) [0.92]
- 총 12건 officialBoost 적용.

### 상업 위성 신뢰 (commercial_imagery_trust, +0.10, PR cap)

- ent-evt-105 (WorldView Legion fully op, Maxar/Vantor 발표) — is_press_release=true → final cap 0.78
- ent-evt-107 (ICEYE rideshare 발사) — ICEYE 직접 분석 [0.85]
- ent-evt-108 (ICEYE deforestation 서비스 launch) — is_press_release=true → cap 0.72

### 한반도 GeoFocus (korea_geo_focus, +0.10)

- ent-evt-110 (KOMPSAT-7 운영, KR) [0.99, 확정]
- ent-evt-111 (NLL 어선 100척, KR) [0.99]
- ent-evt-113 (CAS500-2 첫 교신, KR) [0.99]
- ent-evt-115 (영변 UEP, KP) [0.99]
- ent-evt-116 (Sohae 엔진, KP) [0.99]

총 5건 koreaBoost 적용.

### 재해 우선순위 (disaster_severity_priority, +0.20)

- ent-evt-098 (GA Pineland 50000 acres) [0.95]
- ent-evt-101 (Kilauea Ep46 lava fountaining) [0.95]
- ent-evt-102 (Mayon eruption ongoing high) [0.95]
- ent-evt-109 (Myanmar 홍수경보 high) [0.85]

### Before/After 신뢰 (before_after_credibility, +0.10)

- ent-evt-098 (GA NBR 시계열) [0.92]
- ent-evt-101 (Kilauea Ep46 9-hour fountaining 시계열) [0.92]
- ent-evt-115 (영변 04-2026 vs 이전) [0.92]
- ent-evt-116 (Sohae 09-2025 imagery vs 이전) [0.90]
- ent-evt-118 (Hektoria 8 km/2 month 시계열) [0.95, 확정]
- ent-evt-120 (Antelope airbase before/after) [0.95]

총 6건 baCredibilityBoost 적용.

### 종합 신뢰도 산정 (최종 confidence cap 0.97)

| 이벤트 ID | 이벤트명 | 기본 | 가산 | 최종 | 비고 |
|-----------|---------|------|------|------|------|
| ent-evt-098 | GA Pineland 산불 | 0.90 | thermal+0.10, official+0.15, priority+0.20, ba+0.10 | 0.97 (cap) | NASA EO + Landsat TIRS |
| ent-evt-099 | Krasheninnikov 화산 | 0.85 | thermal+0.10 | 0.95 | VIIRS thermal flux |
| ent-evt-100 | 글로벌 화산 일일 | 0.78 | multiSat+0.20 | 0.97 (cap) | VIIRS+Himawari |
| ent-evt-101 | Kilauea Ep46 종료 | 0.85 | official+0.15, priority+0.20, ba+0.10, partOfSeries | 0.97 (cap) | USGS HVO 시리즈 |
| ent-evt-102 | Mayon Advisory 567 | 0.85 | official+0.15, priority+0.20, partOfSeries | 0.97 (cap) | VAAC+PHIVOLCS |
| ent-evt-103 | UN MARS 운영 | 0.90 | tracegas+0.15, official+0.15, supersedes | 0.97 (cap) | ESA+UN |
| ent-evt-104 | S5P OCM | 0.92 | official+0.15 | 0.97 (cap) | ESA Copernicus |
| ent-evt-105 | WV-Legion fully op | 0.78 | commercial+0.10 | 0.78 (PR cap 0.7) | Maxar/Vantor PR |
| ent-evt-106 | Amazon 임계점 PIK | 0.85 | multiSat+0.20, official+0.15 | 0.97 (cap) | PIK Nature |
| ent-evt-107 | ICEYE rideshare | 0.78 | commercial+0.10 | 0.85 | ICEYE direct |
| ent-evt-108 | ICEYE deforestation 서비스 | 0.72 | sar+0.10, commercial+0.10 | 0.72 (PR cap) | press release |
| ent-evt-109 | Myanmar 홍수경보 | 0.72 | multiSat+0.20, sar+0.10, official+0.15, priority+0.20 | 0.97 (cap) | Sentinel-1A/C/D + CEMS |
| ent-evt-110 | KOMPSAT-7 운영 | 0.82 | official+0.15, korea+0.10 | 0.97 (cap) | KARI |
| ent-evt-111 | NLL 어선 100척 | 0.70 | multiSat+0.20, sar+0.10, korea+0.10 | 0.97 (cap) | VIIRS+S1A |
| ent-evt-112 | Silivri 매립지 | 0.85 | multiSat+0.20, tracegas+0.15 | 0.97 (cap) | Tanager+EMIT |
| ent-evt-113 | CAS500-2 첫 교신 | 0.85 | official+0.15, korea+0.10 | 0.97 (cap) | KARI |
| ent-evt-115 | 영변 UEP 후속 | 0.90 | hiRes+0.15, korea+0.10, ba+0.10 | 0.97 (cap) | CSIS BP supersedes |
| ent-evt-116 | Sohae 엔진 | 0.92 | hiRes+0.15, korea+0.10, ba+0.10 | 0.97 (cap) | CSIS BP |
| ent-evt-117 | S1D 4-sat live | 0.92 | official+0.15 | 0.97 (cap) | ESA supersedes |
| ent-evt-118 | Hektoria 8km/2mo | 0.90 | multiSat+0.20, official+0.15, sar+0.10, ba+0.10 | 0.97 (cap) | NASA EO 시계열 |
| ent-evt-119 | GFW 2026 보고 | 0.88 | multiSat+0.20, official+0.15 | 0.97 (cap) | GFW analyst |
| ent-evt-120 | Antelope airbase | 0.90 | multiSat+0.20, hiRes+0.15, ba+0.10 | 0.97 (cap) | AMTI supersedes |
| ent-evt-121 | Cuarteron 레이더 | 0.65 | — | 0.65 | naturalnews 단일출처 low-conf |
| ent-evt-122 | MethaneSAT global | 0.88 | tracegas+0.15 | 0.97 (cap) | EDF |
| ent-evt-123 | Brazil Apr -67.9% | 0.82 | multiSat+0.20, partOfSeries | 0.97 (cap) | INPE |
| ent-evt-124 | Cerulean SkyTruth | 0.85 | sar+0.10 | 0.95 | SkyTruth 운영중 |

### 추론 통계 요약

| 규칙 | 금일 발동 | 누적 (~05-07) | 평균 신뢰도 |
|------|----------|------|-----------|
| multi_satellite_confirmation | 10 | 26 | 0.92 |
| temporal_progression / partOfSeries | 4 | 16 | 0.92 |
| supersedes | 4 | 9 | 0.85 |
| cascading_disaster | 0 | 5 | — |
| sensor_capability_match (전체) | 13 | 37 | 0.94 |
| official_source_trust | 12 | 31 | 0.96 |
| commercial_imagery_trust | 3 | 7 | 0.81 |
| korea_geo_focus | 5 | 23 | 0.99 |
| disaster_severity_priority | 4 | 21 | 0.93 |
| before_after_credibility | 6 | 26 | 0.93 |
| **합계** | **61** | **201** | **0.92** |

### 온톨로지 변경

| 변경 유형 | 대상 | 근거 |
|----------|------|------|
| 새 Country | co-mm (미얀마), co-tr (튀르키예) (2건) | Myanmar SW monsoon 홍수경보 / Silivri 매립지 8.4 t/h |
| 새 Phenomenon | phen-satops (1건) | 위성 자체 활동(launch/commissioning/OCM/first-contact) 메타-이벤트 — 6건 즉시 매핑 |
| 새 Satellite | sat-wv-legion, sat-tanager1, sat-emit (3건) | WorldView Legion fully op, Tanager-1 hyperspectral, EMIT ISS imaging |
| 새 Organization | org-kvert, org-unmars, org-pik, org-paf, org-carbonmapper, org-ucla (6건) | KVERT/UN MARS/PIK/Portuguese AF/Carbon Mapper/UCLA — 각 기관 첫 참조 |
| 새 Location | ent-loc-039~045 (7건) | Pineland GA, Krasheninnikov, NLL Goseong, Silivri Istanbul, Hektoria Glacier, Cuarteron Reef, Permian Basin |
| 새 Event | ent-evt-098~124 (26건, evt-114 skip) | 신규 26건 |
| 이벤트 supersedes | evt-115→086(영변), evt-103→084(MARS), evt-117→026(S1D), evt-120→092(Antelope) (4건) | CSIS BP/UN MARS/ESA/AMTI 후속 |
| 이벤트 partOfSeries | evt-101→081, evt-102→082, evt-123→106 (3건) | Kilauea/Mayon/Brazil Amazon 시리즈 |

config 한도 내 — 새 클래스 0건 (max=3), 새 관계 유형 0건 (max=5). 새 Phenomenon(satops)은 Phenomenon 클래스 인스턴스로 추가 (클래스 추가 아님).

### 미적용/제외 추론

- **3+ 단계 추론:** 발견되지 않음 (모든 추론 1단계 직접)
- **공간적 근접 (nearby):** 기존 location 간 nearby 관계 신규 미발견
- **cascading_disaster:** 본 사이클 동일위치 7일내 시간차 재해 패턴 0건 (Krasheninnikov/Mayon/Kilauea/Myanmar 각기 독립)
- **DPRK 조선중앙TV (ent-evt-090, prior carry):** 이번 사이클 신규 보도 없음, 위성 미검증 상태 유지
- **ent-evt-114:** WV-Legion src-009 SpaceNews 후속 보도는 src-008과 중복 — 별도 이벤트 ID 미부여
- **ent-evt-100, ent-evt-121:** 단일출처 low-conf 분류 — 보고서 본문 미포함, 부록만 기재

---

## 2026-05-07 Cycle 2 추론

### 다중 위성 교차검증
- **ent-evt-125 (Pemex Cantarell)**: Sentinel-1A(SAR) + Sentinel-2A(MSI) — ESA 단일 운영자이나 SAR+광학 cross-modal → multiSatBoost +0.20 (약가산)
- **ent-evt-127 (TS Hagupit)**: Himawari-9(JMA/JAXA) + GOES-18(NOAA) — 독립 운영자 GEO 교차검증 → multiSatBoost +0.20

### 센서 능력 매칭
- ent-evt-125: SAR(C-band) oil slick dampening signature → sarBoost +0.10
- ent-evt-128 (Dukono): Himawari-9 thermal IR → thermalBoost +0.10
- ent-evt-129 (UNEP MARS coal/waste): TROPOMI trace_gas → tracegasBoost +0.15

### supersedes 추론
- ent-evt-129 supersedes ent-evt-106 (UN MARS oil&gas only → coal+waste 확장)

### 공식 출처 가산
- ent-evt-128: CVGHM/PVMBG officialBoost +0.15
- ent-evt-129: UNEP officialBoost +0.15
- ent-evt-127: JMA/NOAA officialBoost +0.15

### 시계열 partOfSeries
- ent-evt-082 (Mayon) partOfSeries(ent-evt-029 original) — lava flow 3.8km 진전 업데이트

### 신규 Country
- co-mx (멕시코), co-kw (쿠웨이트)

---

## 2026-05-08 추론 결과

입력: sources/2026-05-08/entities.json — 25 sources (11 new, 6 update, 8 reported). 신규 이벤트 6건(ent-evt-201~206), 업데이트 5건(evt-082/126/127/128/temp-001).

### 다중 위성 교차검증 (multi_satellite_confirmation, +0.20) — 5건

- **추론 #1:** ent-evt-127 (TS Hagupit) — Himawari-9(JMA/JAXA, GEO) + GOES-18(NOAA, GEO) → multiSatBoost +0.20 [confidence 0.92, 확정]
  - 독립 운영자 GEO 교차검증: JMA ≠ NOAA
- **추론 #2:** ent-evt-082 (Mayon danger zone 8km) — Himawari-9(JMA, GEO) + Sentinel-2A(ESA, SSO) → multiSatBoost +0.20 [0.92, 확정]
  - 독립 운영자/궤도: JMA GEO ≠ ESA SSO
- **추론 #3:** ent-evt-205 (Amazon Xingu gold mining) — PlanetScope(Planet) + Sentinel-2A(ESA) → multiSatBoost +0.20 [0.92, 확정]
  - 독립 운영자: Planet ≠ ESA
- **추론 #4:** temp-evt-001 (GA Pineland burn scar) — S-NPP VIIRS(NOAA) + Landsat 8(USGS) + Landsat 9(USGS) → multiSatBoost +0.20 [0.95, 확정]
  - 3위성 교차검증, NOAA ≠ USGS 독립
- **추론 #5:** ent-evt-126 (Iran-US bases 228+) — PlanetScope(Planet) + Sentinel-2A(ESA) → multiSatBoost +0.20 [0.88, 확정]
  - Copernicus + Planet 교차검증 Orbital Today 후속

### 시계열 진행 / 시리즈 (temporal_progression, partOfSeries) — 6건

- **추론 #6:** ent-evt-082 (Mayon danger zone 8km) :partOfSeries ent-evt-029 (Mayon original 2026-01~) → 장기 시리즈 [0.97, 확정]
  - 2026-01 분출 시작 → 05-03 phreatic → 05-05 VAAC 567 → 05-06 87 barangays → 05-08 8km danger zone + lahar risk
- **추론 #7:** ent-evt-127 (TS Hagupit) :partOfSeries 이전 사이클 (May 7→8) → track 업데이트 [0.95, 확정]
  - Yap 통과 → PAR entry 예상 May 9 as Caloy
- **추론 #8:** ent-evt-128 (Dukono) :partOfSeries 이전 사이클 (May 7 VAAC advisory→May 8 deaths) → severity upgrade [0.95, 확정]
  - VAAC Darwin advisory → 3 hikers killed, ash 10km
- **추론 #9:** ent-evt-202 (Kilauea Ep47 예보) :partOfSeries ent-evt-101 (Ep46 종료) → 에피소드 시리즈 [0.92, 확정]
  - 동일 위치(Halemaʻumaʻu), Ep46 05-05 종료 → Ep47 05-12~17 예보
- **추론 #10:** temp-evt-001 (GA Pineland) :partOfSeries ent-evt-098 (GA fires) → burn scar 시계열 [0.95, 확정]
  - May 5→7→8 CIRA before/after 추가, 50,000+ ac, 85% contained
- **추론 #11:** ent-evt-203 (Great Sitkin WATCH) :partOfSeries ent-evt-050 (Great Sitkin 2026-05-03) → alert upgrade [0.85, 확정]
  - medium→WATCH/ORANGE lava dome growth

### 연쇄 재해 (cascading_disaster) — 1건 잠정

- **추론 #12:** ent-evt-082 (Mayon) :potentialTriggeredBy ent-evt-127 (TS Hagupit/Caloy)
  - **조건:** Hagupit이 5월 9일 PAR 진입 시 Albay 지역 강우 → Mayon ashfall 퇴적 위 lahar(화산이류) 발생 우려
  - **근거:** PHIVOLCS 8km danger zone 확대 사유에 "approaching typhoon lahar risk" 명시
  - **신뢰도:** 0.70 [잠정 — Hagupit 경로 확정 시 재평가]
  - **유형:** Disaster(typhoon) → Disaster(volcanic lahar) 사슬

### 센서 능력 매칭 (sensor_capability_match) — 3건

- **trace_gas × volcanic SO2:** ent-evt-204 (Shishaldin, Sentinel-5P TROPOMI SO2) → tracegasBoost +0.15 [0.88, 확정]
- **VIIRS thermal × volcanic:** ent-evt-203 (Great Sitkin, VIIRS thermal) → thermalBoost +0.10 [0.90, 확정]
- **TIRS+VIIRS thermal × wildfire:** temp-evt-001 (GA Pineland, Landsat TIRS + S-NPP VIIRS) → thermalBoost +0.10 [0.92, 확정]

### 공식 출처 신뢰 (official_source_trust, +0.15) — 7건

- ent-evt-201 (ESA Copernicus 공식) [0.99, 확정]
- ent-evt-202 (USGS HVO 공식 예보) [0.99, 확정]
- ent-evt-203 (USGS AVO 공식) [0.99, 확정]
- ent-evt-204 (USGS AVO 공식) [0.99, 확정]
- ent-evt-128 (CVGHM/PVMBG + VAAC Darwin) [0.95, 확정]
- ent-evt-127 (JMA + NOAA + PAGASA) [0.95, 확정]
- temp-evt-001 (NASA EO + CIRA/RAMMB) [0.95, 확정]

### 재해 우선순위 (disaster_severity_priority, +0.20) — 2건

- ent-evt-128 (Dukono 3 deaths, HIGH severity) [0.95, 확정]
- ent-evt-082 (Mayon 8km danger zone, evacuations, lahar risk) [0.97, 확정]

### 전후 비교 신뢰 (before_after_credibility, +0.10) — 2건

- temp-evt-001 (GA Pineland CIRA S-NPP before/after burn scar) [0.95, 확정]
- ent-evt-205 (Amazon Xingu mining PlanetScope+S2A 전후) [0.90, 확정]

### 분석가 신뢰 (analyst_org_trust, +0.10) — 1건

- ent-evt-205 (Amazon Conservation + ISA 독립 NGO 분석) [0.90, 확정]

### 종합 신뢰도 산정 (최종 confidence cap 0.97)

| 이벤트 ID | 이벤트명 | 기본 | 가산 | 최종 | 비고 |
|-----------|---------|------|------|------|------|
| ent-evt-201 | Sentinel-2 datacenter fire 장애 | 0.85 | official+0.15 | 0.97 (cap) | ESA 공식 |
| ent-evt-202 | Kilauea Ep47 예보 | 0.80 | official+0.15, partOfSeries | 0.95 | HVO 공식, 위성 직접 관측 없음 |
| ent-evt-203 | Great Sitkin WATCH/ORANGE | 0.78 | official+0.15, thermal+0.10, partOfSeries | 0.97 (cap) | AVO + VIIRS |
| ent-evt-204 | Shishaldin ADVISORY/YELLOW | 0.75 | official+0.15, tracegas+0.15 | 0.95 | AVO + TROPOMI SO2 |
| ent-evt-205 | Amazon Xingu 496k ha | 0.82 | multiSat+0.20, analyst+0.10, ba+0.10 | 0.97 (cap) | PlanetScope+S2A + Amazon Conservation |
| ent-evt-206 | Balikatan + PLA Liaoning | 0.75 | — | 0.75 | 단일 위성 출처, defense |
| ent-evt-128 update | Dukono 3 deaths | 0.78 | official+0.15, priority+0.20 | 0.97 (cap) | CVGHM + VAAC Darwin |
| ent-evt-127 update | Hagupit/Caloy PAR | 0.80 | multiSat+0.20, official+0.15 | 0.97 (cap) | Himawari-9 + GOES-18 |
| ent-evt-082 update | Mayon 8km PDC | 0.85 | multiSat+0.20, priority+0.20, partOfSeries | 0.97 (cap) | Himawari-9 + S2A + lahar risk |
| temp-evt-001 update | GA Pineland burn scar | 0.85 | multiSat+0.20, thermal+0.10, official+0.15, ba+0.10 | 0.97 (cap) | S-NPP + L8/9 + NASA EO |
| ent-evt-126 update | Iran bases 228+ | 0.78 | multiSat+0.20 | 0.92 | Copernicus + Planet 교차 |

### 추론 통계 요약

| 규칙 | 금일 발동 | 누적 (~05-08) | 평균 신뢰도 |
|------|----------|------|-----------|
| multi_satellite_confirmation | 5 | 31 | 0.92 |
| temporal_progression / partOfSeries | 6 | 22 | 0.93 |
| cascading_disaster | 1 (잠정) | 6 | 0.70 |
| sensor_capability_match | 3 | 40 | 0.90 |
| official_source_trust | 7 | 38 | 0.97 |
| analyst_org_trust | 1 | 8 | 0.90 |
| disaster_severity_priority | 2 | 23 | 0.96 |
| before_after_credibility | 2 | 28 | 0.92 |
| **합계** | **27** | **196** | **0.92** |

### 금일 한반도 GeoFocus — 0건

금일 사이클에서 한반도/DMZ/동해/남해 관련 위성 관측 이벤트 없음. 보고서에 "금일 한반도 GeoFocus 신규 이벤트 특이사항 없음" 명시.

### 금일 미적용/제외 추론

- **korea_geo_focus:** 한반도 관련 이벤트 0건 — 미적용
- **commercial_imagery_trust:** PR cap 해당 이벤트 0건
- **supersedes:** 금일 supersede 관계 없음 (모두 partOfSeries 또는 update)
- **3+ 단계 추론:** cascading_disaster(Hagupit→Mayon lahar)가 잠정 2단계 추론 — Hagupit 경로 확정 필요

### 온톨로지 변경

| 변경 유형 | 대상 | 근거 |
|----------|------|------|
| 새 Country | co-kw (쿠웨이트) (1건) | Iran-US bases Copernicus+Planet 교차검증 상세 지역 |
| 새 Satellite | sat-sentinel2c (1건) | Sentinel-2C — NorthC datacenter fire 데이터 장애 |
| 새 Organization | ent-org-hvo/avo/cvghm/vaac-darwin/pagasa/bnpb/amazon-conservation/isa/cira/pla (10건) | 각 기관 첫 참조 |
| 새 Location | ent-loc-046~050 (5건) | Almere, Dukono, Great Sitkin, Shishaldin, Xingu |
| 새 Event | ent-evt-201~206 (6건) | 신규 이벤트 |
| 이벤트 업데이트 | ent-evt-082/126/127/128/temp-001 (5건) | 후속 보도·severity 업그레이드 반영 |

config 한도 내 — 새 클래스 0건 (max=3), 새 관계 유형 0건 (max=5).


---

## 2026-05-09 추론 결과

입력: sources/2026-05-09/entities.json — 27 sources (7 new, 8 update, 12 reported). 신규 이벤트 7건(ent-evt-207~213), 업데이트 6건(evt-082/127/128/temp-001/202/201).

### 다중 위성 교차검증 (multi_satellite_confirmation, +0.20) — 4건

- **추론 #1:** ent-evt-127 (TS Caloy/Hagupit) — Himawari-9(JMA/JAXA, GEO) + GOES-18(NOAA, GEO) → multiSatBoost +0.20 [confidence 0.92, 확정]
  - 독립 운영자 GEO 교차검증: JMA ≠ NOAA (연속 확인 3일차)
- **추론 #2:** ent-evt-082 (Mayon VAAC 586) — Himawari-9(JMA, GEO) + Sentinel-2A(ESA, SSO) → multiSatBoost +0.20 [0.92, 확정]
  - 독립 운영자/궤도: JMA GEO ≠ ESA SSO (연속 확인)
- **추론 #3:** temp-evt-001 (GA Pineland 70% contained) — S-NPP VIIRS(NOAA) + Landsat 8(USGS) + Landsat 9(USGS) → multiSatBoost +0.20 [0.95, 확정]
  - 3위성 교차검증: NOAA ≠ USGS (연속 확인)
- **추론 #4:** ent-evt-202 (Kilauea Ep47 예보) — Sentinel-2A(ESA) + Landsat 9(USGS) → multiSatBoost +0.20 [0.88, 확정]
  - 독립 운영자: ESA ≠ USGS

### 시계열 진행 / 시리즈 (temporal_progression, partOfSeries) — 5건

- **추론 #5:** ent-evt-082 (Mayon VAAC 586) :partOfSeries ent-evt-029 (Mayon original 2026-01~) → 장기 시리즈 [0.97, 확정]
  - 2026-01 분출 시작 → ... → 05-08 8km PDC → 05-09 VAAC 586 SO2 2785 t/d
- **추론 #6:** ent-evt-127 (TS Caloy PAR entry) :partOfSeries 이전 사이클 → PAR 진입 확인 [0.95, 확정]
  - May 7 Yap → May 8 PAR entry 예상 → May 9 PAR entry 확인 65km/h
- **추론 #7:** ent-evt-128 (Dukono 수색 재개) :partOfSeries 이전 사이클 → body recovery 후속 [0.95, 확정]
  - May 7 VAAC → May 8 3 deaths → May 9 search resumed, 1 body recovered, 2 Singaporeans missing
- **추론 #8:** temp-evt-001 (GA Pineland 70%) :partOfSeries ent-evt-098 → containment 하향 [0.95, 확정]
  - May 5 발화 → May 8 85% → May 9 **70%** (이탄층 지하연소 반영)
- **추론 #9:** ent-evt-202 (Kilauea Ep47) :partOfSeries ent-evt-101 (Ep46) → 예보 유지 [0.92, 확정]
  - Ep46 May 5 종료 → Ep47 예보 유지 May 12-17, 6.9μrad 팽창

### 연쇄 재해 (cascading_disaster) — 2건 (1건 상향, 1건 확정)

- **추론 #10:** ent-evt-082 (Mayon lahar) :potentialTriggeredBy ent-evt-127 (TS Caloy)
  - **조건:** Caloy PAR entry May 9 확인됨 → Albay 강우 시 lahar 발생 위험
  - **변경:** 신뢰도 0.70 → **0.75 상향** (PAR entry 확인됨, 경로 Albay 접근 확인 필요)
  - **유형:** Disaster(typhoon) → Disaster(volcanic lahar)
  - **상태:** elevated — PAR entry 확인, 경로·강우량에 따라 재평가

- **추론 #11:** ent-evt-207 (ashfall crop damage) :potentialTriggeredBy ent-evt-082 (Mayon eruption)
  - **조건:** Mayon 화산재 퇴적 → 벼 1,039ha + 기타 191ha 작물 피해 — PhilSA Sentinel-2 변화탐지
  - **신뢰도:** 0.85 [**확정** — 위성 before/after 검증]
  - **유형:** Disaster(volcanic eruption) → AgriMarine(crop damage)
  - **상태:** confirmed — PhilSA 공식 Sentinel-2 NDVI 변화탐지 근거

### 센서 능력 매칭 (sensor_capability_match) — 3건

- **SAR × deforestation:** ent-evt-209 (NISAR L-band SAR 수관 관통 → 삼림벌채 canopy change) sarBoost +0.10 [0.85, 확정]
- **TIRS+VIIRS × wildfire:** temp-evt-001 (GA Pineland Landsat TIRS + S-NPP VIIRS thermal) thermalBoost +0.10 [0.92, 확정 — 연속]
- **multispectral × NDVI:** ent-evt-207 (Sentinel-2 MSI NDVI/NBR ashfall crop damage mapping) multispectralBoost +0.10 [0.90, 확정]

### 공식 출처 신뢰 (official_source_trust, +0.15) — 11건

- ent-evt-207 (PhilSA 공식 우주기관 + Sentinel-2) [0.95, 확정]
- ent-evt-209 (NASA EO + Nature Communications 피어리뷰) [0.92, 확정]
- ent-evt-210 (NASA Earth Observatory 공식) [0.92, 확정]
- ent-evt-211 (NASA Earth Observatory 공식) [0.90, 확정]
- ent-evt-212 (NASA EO + Science 학술지) [0.90, 확정]
- ent-evt-127 (PAGASA + JMA + NOAA 공식) [0.95, 확정]
- ent-evt-082 (PHIVOLCS + VAAC 공식) [0.95, 확정]
- ent-evt-128 (CVGHM/PVMBG + VAAC Darwin 공식) [0.95, 확정]
- ent-evt-202 (USGS HVO 공식 예보) [0.95, 확정]
- temp-evt-001 (NASA EO + CIRA/RAMMB 계승) [0.90, 확정]
- ent-evt-201 (ESA Copernicus 공식 복구 발표) [0.95, 확정]

### 재해 우선순위 (disaster_severity_priority) — 3건

- ent-evt-128 (Dukono 인명피해 지속, body recovery) +0.20 [0.95, 확정]
- ent-evt-082 (Mayon 8km + PDC + lahar risk from Caloy) +0.20 [0.97, 확정]
- ent-evt-207 (1,039ha rice loss — 식량안보 moderate) +0.10 [0.88, 확정]

### 전후 비교 신뢰 (before_after_credibility, +0.10) — 1건

- ent-evt-207 (PhilSA Sentinel-2 ashfall before/after NDVI change detection) [0.92, 확정]

### 상업 위성 신뢰 (commercial_imagery_trust, +0.10) — 1건

- ent-evt-208 (Planet Labs PlanetScope Thitu/Nanshan 건설 확인) [0.82, 확정]

### 종합 신뢰도 산정 (최종 confidence cap 0.97)

| 이벤트 ID | 이벤트명 | 기본 | 가산 | 최종 | 비고 |
|-----------|---------|------|------|------|------|
| ent-evt-207 | PhilSA ashfall crop damage | 0.90 | official+0.15, ba+0.10, multispectral+0.10, priority+0.10 | 0.97 (cap) | PhilSA 공식, cross-domain |
| ent-evt-208 | Thitu/Nanshan construction | 0.85 | commercial+0.10 | 0.85 | Planet Labs 단일 출처 |
| ent-evt-209 | NISAR deforestation 100d early | 0.85 | official+0.15, sar+0.10 | 0.97 (cap) | NASA + Nature Comms |
| ent-evt-210 | Shivelyuch snowmelt | 0.88 | official+0.15 | 0.97 (cap) | NASA EO + Landsat 9 |
| ent-evt-211 | Peter I Island vortex | 0.82 | official+0.15 | 0.92 | NASA EO + Landsat 8 |
| ent-evt-212 | Tracy Arm landslide-tsunami | 0.85 | official+0.15 | 0.97 (cap) | NASA EO + Science |
| ent-evt-213 | Fuego eruption | 0.45 | — | 0.45 | satellite_unverified |
| ent-evt-082 update | Mayon VAAC 586 | 0.85 | multiSat+0.20, priority+0.20, partOfSeries | 0.97 (cap) | cascading 0.75 |
| ent-evt-127 update | Caloy PAR entry | 0.80 | multiSat+0.20, official+0.15 | 0.97 (cap) | cascading trigger |
| ent-evt-128 update | Dukono body recovery | 0.78 | official+0.15, priority+0.20 | 0.97 (cap) | severity HIGH |
| temp-evt-001 update | GA Pineland 70% | 0.85 | multiSat+0.20, thermal+0.10, official+0.15 | 0.97 (cap) | peat underground |
| ent-evt-202 update | Kilauea Ep47 forecast | 0.80 | multiSat+0.20, official+0.15, partOfSeries | 0.95 | 위성 직접 관측 한정 |
| ent-evt-201 update | S2 데이터 복구 | 0.85 | official+0.15 | 0.97 (cap) | ESA 공식 |

### 추론 통계 요약

| 규칙 | 금일 발동 | 누적 (~05-09) | 평균 신뢰도 |
|------|----------|------|-----------|
| multi_satellite_confirmation | 4 | 35 | 0.92 |
| temporal_progression / partOfSeries | 5 | 27 | 0.95 |
| cascading_disaster | 2 (1 상향, 1 확정) | 8 | 0.80 |
| sensor_capability_match | 3 | 43 | 0.89 |
| official_source_trust | 11 | 49 | 0.94 |
| commercial_imagery_trust | 1 | 8 | 0.82 |
| analyst_org_trust | 0 | 8 | — |
| disaster_severity_priority | 3 | 26 | 0.93 |
| before_after_credibility | 1 | 29 | 0.92 |
| **합계** | **30** | **233** | **0.91** |

### 금일 한반도 GeoFocus — 0건

금일 사이클에서 한반도/DMZ/동해/남해 관련 위성 관측 이벤트 없음. 보고서에 "금일 한반도 GeoFocus 신규 이벤트 특이사항 없음" 명시.

### 금일 미적용/제외 추론

- **korea_geo_focus:** 한반도 관련 이벤트 0건 — 미적용
- **analyst_org_trust:** 독립 분석기관 신규 분석 없음 (Bellingcat/CSIS/Skytruth 금일 미참조)
- **supersedes:** 금일 supersede 관계 없음 (모두 partOfSeries 또는 update)
- **satellite_unverified:** ent-evt-213 (Fuego) — INSIVUMEH 지상 관측만, 위성 검증 불가, conf <0.50 cap 적용
- **3+ 단계 추론:** cascading_disaster(Mayon→ashfall crop damage→Caloy lahar)가 최대 3단계 — 확정+잠정 혼합

### 온톨로지 변경

| 변경 유형 | 대상 | 근거 |
|----------|------|------|
| 새 Satellite | sat-nisar (NASA/ISRO, SSO, L-band SAR, 10m, 12-day, July 2025) (1건) | NISAR+Landsat 삼림벌채 조기탐지 Nature Communications |
| 새 Location | ent-loc-051 (Mayon ashfall zone PH), ent-loc-052 (Thitu PH), ent-loc-053 (Nanshan PH), ent-loc-054 (Shivelyuch RU), ent-loc-055 (Peter I AQ), ent-loc-056 (Tracy Arm US), ent-loc-057 (Fuego GT) (7건) | 각 신규 이벤트 발생 지역 |
| 새 Organization | org-insivumeh (Guatemala volcano/seismology institute) (1건) | Fuego 화산 분출 지상 관측 |
| 새 Phenomenon | phen-atmo (atmospheric dynamics — von Karman vortex) (1건) | Peter I Island Landsat 8 폰카르만 소용돌이 — 기존 phen-air_pollution과 구분되는 대기 유체역학 현상 |
| 새 Event | ent-evt-207~213 (7건) | 신규 이벤트 |
| 이벤트 업데이트 | ent-evt-082/127/128/temp-001/202/201 (6건) | 후속 보도·수색·containment·예보·복구 반영 |

config 한도 내 — 새 클래스 0건 (max=3), 새 관계 유형 0건 (max=5). 새 Phenomenon(phen-atmo)은 Phenomenon 클래스 인스턴스로 추가 (클래스 추가 아님).

## 2026-05-10 추론 결과

### multi_satellite_confirmation (다중 위성 교차검증) — 1건

- **추론 #1:** ent-evt-401 (Mayon humanitarian GLIDE) — observedBy Sentinel-2A (ESA) AND Himawari-9 (JMA) → multiSatBoost +0.20 [confidence 0.85, 확정]

### sensor_capability_match (센서-현상 적합성) — 1건

- **tracegasBoost:** ent-evt-204 (Shishaldin SO2) — usesSensor TROPOMI (trace_gas) AND phenomenon volcanic_eruption → tracegasBoost +0.15 [confidence 0.78, 확정]

### cascading_disaster (인과 사슬) — 1건

- **추론 #1:** ent-evt-082 (Mayon 화산 분출, Disaster) → ent-evt-401 (Mayon humanitarian GLIDE 등록) — 같은 위치(Albay PH), 화산 분출이 직접 인과로 작물피해·건강피해·인도주의 위기 초래. triggeredBy 관계 확정. [confidence 0.90, 확정]

### official_source_trust (공식 기관 신뢰도) — 1건

- **추론 #1:** ent-evt-401 — analyzedBy org-ocha (UN OCHA, un_body) → officialBoost +0.15 [confidence 0.85, 확정]

### temporal_progression (시계열 추적) — 5건

- ent-evt-082 (Mayon 125일 연속 분출) — partOfSeries 유지 [0.92]
- ent-evt-127 (Caloy TS→TD→remnant low) — partOfSeries 유지 [0.85]
- ent-evt-128 (Dukono rescue 1→3 시신 수습, 완료) — partOfSeries 유지 [0.95]
- ent-evt-202 (Kilauea Ep46→pause→Ep47 5/12~15) — partOfSeries 유지 [0.88]
- temp-evt-001 (GA Pineland 4/19→5/10, 32575ac 70%) — partOfSeries 유지 [0.88]

### 금일 추론 요약

| 규칙 | 적용 | 트리플 수 | 비고 |
|------|------|----------|------|
| multi_satellite_confirmation | 1건 | 1 | Mayon humanitarian S2A+Himawari |
| sensor_capability_match_tracegas | 1건 | 1 | Shishaldin TROPOMI SO2 |
| cascading_disaster | 1건 | 1 | Mayon eruption→humanitarian |
| official_source_trust | 1건 | 1 | OCHA un_body |
| temporal_progression | 5건 | 5 | 기존 이벤트 시계열 유지 |
| **합계** | **9건** | **9 inferred** | |

### 온톨로지 변경 요약

| 변경 유형 | 대상 | 근거 |
|----------|------|------|
| 새 Organization | org-ocha (UN OCHA / ReliefWeb, un_body, INTL) (1건) | Mayon GLIDE 등록, 인도주의 도메인 첫 참조 |
| 새 Event | ent-evt-401 (Mayon humanitarian GLIDE VO-2026-000065-PHL) (1건) | ReliefWeb 정식 재해 등록 |
| 이벤트 업데이트 | ent-evt-082/127/128/202/203/204/temp-001/201/303 (9건) | 후속 보도·수색완료·TD약화·예보·containment·복구·작물 확인 반영 |

config 한도 내 — 새 클래스 0건 (max=3), 새 관계 유형 0건 (max=5).

## 2026-05-11 추론 결과

### 추론 #1: multi_satellite_confirmation (5건)
- **Florida Everglades Fire (ent-evt-501):** GOES-18(NOAA) + VIIRS(NOAA/NASA) — 정지궤도·극궤도 독립 관측 → multiSatBoost +0.20 | 신뢰도 0.85
- **Georgia Pineland (temp-evt-001):** VIIRS + Landsat 8 + Landsat 9 — 3중 위성 검증 → multiSatBoost +0.20 | 신뢰도 0.88
- **Mayon (ent-evt-082):** Himawari-9(JMA) + Sentinel-2A(ESA) — 독립 운영기관 교차 → multiSatBoost +0.20 | 신뢰도 0.92
- **Kilauea (ent-evt-202):** Sentinel-2A(ESA) + Landsat 9(USGS/NASA) → multiSatBoost +0.20 | 신뢰도 0.88
- **Caloy/Hagupit (ent-evt-127):** Himawari-9(JMA) + GOES-18(NOAA) — 독립 정지궤도 2기 → multiSatBoost +0.20 | 신뢰도 0.82
- **상태:** 모두 확정

### 추론 #2: sensor_capability_match_sar
- **Great Sitkin (ent-evt-203):** C-band SAR(Sentinel-1A) 구름 투과 용암류 성장 관측 — 광학 위성 구름 차단 시 SAR이 유일 관측 수단 → sarBoost +0.10 | 신뢰도 0.88
- **상태:** 확정

### 추론 #3: sensor_capability_match_tracegas
- **Shishaldin (ent-evt-204):** TROPOMI(Sentinel-5P) SO2 원격 감지 — 화산 가스 배출 정량 → tracegasBoost +0.15 | 신뢰도 0.85
- **상태:** 확정

### 추론 #4: official_source_trust (3건)
- **Barents Sea (ent-evt-503):** NASA EO 공식 분석 → officialBoost +0.15 | 신뢰도 0.95
- **Mid-Atlantic (ent-evt-502):** NASA EO 공식 분석 → officialBoost +0.15 | 신뢰도 0.95
- **Kilauea/Great Sitkin/Shishaldin:** USGS HVO/AVO 공식 → officialBoost +0.15 | 기존 적용 유지
- **상태:** 모두 확정

### 추론 #5: temporal_progression (3건)
- **Mayon:** Day 125→127, 동일 위치·동일 현상(volcanic_eruption) 시계열 관측 → partOfSeries
- **Kilauea:** Ep46 종료→Ep47 임박, 동일 분화구 에피소드 시퀀스 → partOfSeries
- **Georgia Pineland:** 22일 연속 화재, 동일 위치·동일 현상(wildfire) → partOfSeries
- **상태:** 모두 확정

### 금일 한반도 GeoFocus
- 한반도 관련 신규 이벤트 없음. korea_geo_focus 가산 0건.
