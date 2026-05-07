# 2026-05-06 위성영상 관측 이벤트 — 온톨로지·추론 분석

## 1. 도메인별 흐름 분석

### 1-1. Disaster (자연재해) — 9건 (최다 도메인)

**활화산 클러스터 (4건)**:
- **Kilauea Episode 46** (US, 하와이) — 5/5 08:17 HST 개시 → **9시간 lava fountaining** → 5/5 17:17 종료 → 5/6 ADVISORY/YELLOW로 강등(src-001~004). 650ft 용암 분수, 20,000ft plume, Highway 11까지 tephra 도달. **ent-evt-070(5/5 개시)에서 ent-evt-081(5/6 종료)로 partOfSeries**.
- **Mayon Volcano** (PH, Albay) — **5/3 phreatic eruption + 5/5~5/6 VAAC Tokyo Himawari-9 ash advisory + PhilSA Sentinel-2 ashfall map (87 barangays, 8,544 ha)**(src-005~008). ent-evt-082는 ent-evt-071/029의 후속이며, **다중위성(S2A+Himawari-9)·다중기관(PhilSA+VAAC Tokyo) 교차검증**으로 신뢰도 0.97. Guinobatan 호흡기 환자(src-009) → **cascading_disaster** 트리거.
- 누적 분출 시리즈: ent-evt-029(2026-01~) → ent-evt-071(5/5) → ent-evt-082(5/6) — 6일 연속 추적

**홍수 (1건)**:
- **Cordoba 홍수** (CO) — Copernicus EMSR865 Rapid Mapping 발동(src-010). **Sentinel-1A C-SAR + Sentinel-2A MSI 멀티센서**, 다중위성 교차검증 +0.20.

**산불 보도 (2건)**:
- DPRK 조선중앙TV 황해북도/개성 산불감시·치수망(src-021) — **위성 영상 부재 → satellite_unverified**, 미검증 의혹 분리 처리.
- KR CAS500-1 산불 피해지역 영상 지원(src-022) — KARI 정책브리핑, **한반도 GeoFocus +0.10**.

### 1-2. Defense (국방·안보) — 11건 (최다 도메인 동률)

**한반도 클러스터**:
- **영변 UEP 완공 후속** (CSIS BP, 2026-04, src-018) — ent-evt-001 업데이트, WV-3 0.31m hi-res 식별
- **Panghyon UAV airbase 변경** (CSIS BP, src-018)
- **Yelabuga UAV 제조시설 확장 + DPRK 노동력** (CSIS BP, src-019) — **DPRK-RU 협력 사슬**, WV-3 hi-res

**남중국해 클러스터**:
- **Antelope Reef 1,490 acres** (CN, AMTI Island Tracker, src-025/026) — ent-evt-006 업데이트, **WV-3 + PlanetScope 다중위성**, 시계열 매립 진전 ba+0.10

**중동·남미 클러스터**:
- **Tehran 15개 경찰서 표적 타격** (Bellingcat PlanetScope, src-020) — 2026-03-03 사건 위성 retro-analysis
- **Vantor 우크라이나 D2D 시험** (src-015~017) — Maxar Intelligence 리브랜드, ent-evt-064(Planet Iran 배포 중단)에 대응
- **카리브해 미군 집결 Operation Southern Spear** (Wiki 종합, src-033) — ent-evt-076 업데이트

### 1-3. Climate (기후·환경) — 5건

- **ESA MARS 메탄 탐지 시스템 + CAMS Methane Hotspot Explorer** (src-013/014) — **Sentinel-5P TROPOMI 2.3 µm CH4 흡수밴드**, tracegasBoost +0.15
- **Pine Island Glacier 가속 10.6→12.7 m/day** (ESA Sentinel-1 decade, src-027) — **C-SAR offset tracking**, sarBoost +0.10, **2016→2026 10년 시계열** ba+0.10
- **NAU Climate TRACE 도시 CO2 ~70% 과소 산정** (src-031) — 학술 발견, 위성 직접 관측 아님
- **Climate TRACE Release 5.6.0** (src-032)

### 1-4. AgriMarine (농업·해양) — 3건

- **Sudan breadbasket 농경지 황폐화** (Gezira/Sennar/Khartoum, Al Jazeera Sentinel-2 NDVI, src-030) — **전쟁 전후 NDVI 비교**, 식량안보 priority+0.20
- **CAS500-2 commissioning** 한반도 첫 교신 (src-023/024) — 4-개월 commissioning 단계, 한반도 GeoFocus

### 1-5. HumanActivity — 2건

- **GFW DIST-ALERT** (Landsat+Sentinel-2 통합, src-011/012) — ent-evt-033 후속
- **Planet Pelican-7/8/9 발사** (src-029) — fleet 9기, 보도자료성 0.7 cap

### 1-6. Humanitarian — 2건

- **Guinobatan 호흡기 환자** (src-009) — Mayon ashfall 인과 사슬
- **UNOSAT Gaza 종합 피해** (src-028) — ent-evt-008 후속 (198,273명 영향, 81% 손상)

## 2. 위성·센서별 활용 분석

| 위성 | 본 사이클 활용 | 핵심 도메인 |
|------|----------|------------|
| **Sentinel-2A** (ESA, MSI) | 6건 (Mayon/Cordoba/Sudan/GFW/Kilauea/...) | 화산재·홍수·NDVI·산불 |
| **WorldView-3** (Vantor) | 6건 (Yongbyon/Yelabuga/Antelope/Vantor D2D/Gaza) | 군사 hi-res 0.31m |
| **PlanetScope** (Planet) | 3건 (Tehran/Antelope/Gaza) | hi-res 변화탐지 |
| **Sentinel-1A** (ESA, C-SAR) | 2건 (Cordoba/Pine Island) | SAR 홍수·빙류 |
| **Himawari-9** (JAXA, GEO IR) | 2건 (Mayon VAAC ash advisory) | 화산재 추적 |
| **Sentinel-5P** (ESA, TROPOMI) | 2건 (MARS+CAMS) | 메탄·트레이스가스 |
| **Landsat 9** (USGS/NASA, OLI/TIRS) | 1건 (GFW DIST-ALERT) | 광역 식생 교란 |
| **CAS500-1** (KARI) | 1건 (산불 피해 복구) | 한반도 재해 대응 |

## 3. 지역별 분포

| 지역/국가 | 이벤트 수 | 주요 사례 |
|----------|----------|----------|
| 한반도 (KR/KP) | 4 | 영변/Panghyon/CAS500-1 산불/DPRK 보도 |
| 동아시아 (CN/PH/JP) | 3 | Antelope Reef/Mayon/(Himawari-9 운용) |
| 북미 (US) | 3 | Kilauea/Climate TRACE/Pelican |
| 동유럽 (RU/UA) | 2 | Yelabuga/Vantor D2D Ukraine |
| 중동·서아 (IR) | 1 | Tehran 경찰서 |
| 남미 (CO/VE) | 2 | Cordoba flood/카리브해 군사 |
| 동아프리카 (SD) | 1 | Sudan breadbasket |
| 남극 (AQ) | 1 | Pine Island Glacier |
| 글로벌 | 2 | ESA MARS methane / GFW DIST-ALERT |

**한반도 GeoFocus**: 4건(KP 3 + KR 1) — koreaBoost +0.10 자동 적용.

## 4. 이전 보고서 (2026-04-30 ~ 2026-05-05) 대비 추적

| 이전 이벤트 | 본 사이클 후속 | 변경 사항 |
|------------|--------------|----------|
| ent-evt-070 (Kilauea Ep46 개시 5/5) | ent-evt-081 (Ep46 종료 5/6) | 9시간 fountaining 종료, ADVISORY/YELLOW 강등 |
| ent-evt-071 (Mayon 5/5 VAAC) | ent-evt-082 (5/6 ashfall 87 barangays) | PhilSA satellite map, 8,544 ha 광역 ashfall |
| ent-evt-029 (Mayon 2026-01~ 시리즈) | ent-evt-082 (시점 갱신) | 장기 분출 활성화 지속 |
| ent-evt-001 (영변 UEP 완공) | ent-evt-086 (4월 후속 관측) | CSIS BP 추가 분석 |
| ent-evt-006 (Antelope Reef 확장) | ent-evt-092 (1,490 acres 1+km^2 추가) | AMTI 매립 시계열 갱신 |
| ent-evt-076 (US Caribbean buildup) | ent-evt-097 (Operation Southern Spear 종합) | Wiki 종합 출처 추가 |
| ent-evt-064 (Planet Iran 배포 중단) | ent-evt-085 (Vantor D2D Ukraine) | 시장 supersede 신호 |
| ent-evt-042 (남극 30년 접지선 후퇴) | ent-evt-093 (Pine Island 단일 가속) | 종합→단일 빙하 사례 cascading |

## 5. 추론 결과 요약

- **multi_satellite_confirmation 4건** (Mayon S2A+Himawari, Cordoba S1A+S2A, MARS S5P+CAMS multi, Antelope WV-3+PlanetScope) — 본 사이클 핵심
- **temporal_progression 3건** (Kilauea Ep46 종료, Mayon ashfall, Mayon long-running)
- **cascading_disaster 2건** (Mayon→호흡기 환자, Pine Island→남극 종합)
- **sensor_capability_match 8건** (TIRS×volcano 1, SAR×flood 1, SAR×glacier 1, trace_gas×methane 1, hi-res×military/construction/infra 4)
- **official_source_trust 6건** (USGS/PhilSA/CEMS/ESA/KARI/ESA-S1)
- **korea_geo_focus 4건** — KP 3 + KR 1
- **disaster_severity_priority 6건** + **before_after_credibility 6건** + **analyst_org_trust 5건** + **commercial_imagery_provider 2건** + **supersedes 1건**

총 47건 추론, 평균 신뢰도 0.92.

## 6. 온톨로지 확장 요약

| 유형 | 추가 | 누적 |
|------|------|------|
| 새 Class | 0 | 9 |
| 새 Relation | 0 | 16 |
| 새 Country | 1 (co-sd) | 23 |
| 새 Location | 9 (ent-loc-030~038) | 38 |
| 새 Satellite | 1 (sat-pelican) | 17 |
| 새 Organization | 6 (PhilSA/VAAC Tokyo/AMTI/Al Jazeera/CAMS/NAU) | 30+ |
| 새 Event | 17 (ent-evt-081~097) | 97 |
| Event 업데이트 | 5 (Kilauea/Mayon/영변/Antelope/Caribbean) | 누적 ~25 |

config 한도 내 — `max_new_classes_per_day=3`, `max_new_relations_per_day=5` 모두 0건으로 안전.

## 7. 신뢰도 분포

- **0.95 이상 (확정 최상급)**: 8건 (Kilauea Ep46/Mayon ashfall/Cordoba/MARS methane/영변/Yelabuga/Tehran/CAS500-1/Antelope Reef/Pine Island)
- **0.80~0.94 (확정)**: 4건 (Vantor/Panghyon/Sudan/카리브해)
- **0.65~0.79 (포함 가능)**: 2건 (Pelican/Climate TRACE 오차)
- **0.50~0.64 (잠정/의혹)**: 1건 (DPRK 조선중앙TV — 미검증 의혹 분리)

## 8. 미적용 신호 / 제외 사유

- ent-evt-090 (DPRK 산불 보도): 위성 영상 부재 → 보고서 "미검증 의혹" 섹션 분리
- src-024 CAS500-2 칼럼 (한국 민간 우주시대 종합): ent-evt-079에 흡수, 별도 이벤트 미생성
- ent-evt-094 Pelican 발사: 보도자료성, 0.65 final → 보고서 인프라 메타 섹션 후보
- ent-evt-096 Climate TRACE 오차: 학술 발견, 위성 직접 관측 아님 — 메타 섹션 후보

## 9. 보고서 작성 가이드라인

1. **Top 5** 후보: ent-evt-082(Mayon multi-sat) > ent-evt-083(Cordoba CEMS) > ent-evt-093(Pine Island 10년 가속) > ent-evt-081(Kilauea Ep46) > ent-evt-092(Antelope Reef 1,490 acres)
2. **다중 위성 교차검증** 별도 섹션: 4건 모두 강조
3. **한반도 GeoFocus** 별도 섹션: 영변/Panghyon/CAS500-1 산불/DPRK(미검증)
4. **재해 사슬**: Mayon 분출→ashfall→호흡기 cascading
5. **시계열·전후 비교** 강조: Kilauea Ep45→Ep46, Mayon 시리즈, Pine Island 10년, Antelope Reef AMTI 시계열, Sudan 전쟁 전후 NDVI
6. **미검증 의혹** 분리: DPRK 산불 보도
