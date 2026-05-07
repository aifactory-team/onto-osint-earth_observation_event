# 2026-05-06 분석

## 신규 소스별 중요도 평가

| 소스 ID | 제목 | 중요도 | 근거 |
|---------|------|--------|------|
| src-001 | 이란 미군기지 피해 위성 평가 (WashPost Copernicus+Planet) | **높음** | 다중위성 교차검증(Copernicus+Planet), 228개 구조물 파손 규모, 전후비교 영상 보유. 미국 정부 발표와 상충하는 독립 위성 분석으로 OSINT 가치 극대. |
| src-004 | PhilSA 마욘 화산재 8,544ha 위성 매핑 | **높음** | 필리핀 국가우주기관(PhilSA)의 공식 위성 분석, 정량적 피해 면적(8,544ha) 산출. officialBoost +0.15 적용. 국가급 위성 역량 활용 사례. |
| src-007 | 아마존 금 채굴 삼림벌채 496,000ha (AP/Amazon Conservation) | **높음** | 대규모 환경 파괴(496,000ha)의 위성 기반 정량 평가. Sentinel-2+PlanetScope 다중위성, 2018년 이후 시계열 분석. 연구기관(Oregon State) + NGO(Amazon Conservation) 교차분석. |
| src-008 | 이란 민간·군사 시설 7,645동 파괴 위성 분석 (Bloomberg) | **높음** | 전후비교(before/after) 위성영상 기반 정량 피해 평가(7,645동). Sentinel-2+Planet 교차. 민간 인프라 피해 규모의 독립적 위성 검증으로 인도주의적 의의. |
| src-021 | 이란 핵시설 생존 위성 평가 (CNN) | **높음** | 핵확산 관련 핵심 안보 이슈의 위성 증거. 미국 정부 주장(핵역량 완전 파괴) 대비 부분 생존 증거. 국제 안보 환경에 직접적 영향. |

## 기존 보도 추적

### Kilauea Episode 46 시리즈
- **이전**: ent-evt-004 (Ep44, 4/15) → ent-evt-021 (Ep45, 4/23) → ent-evt-070 (Ep46 시작, 5/5)
- **금일**: Episode 46 종료 보고. 9시간 분출, 650ft(~200m) 용암 분수, 총 4.6M m³ 용암 분출, 테프라가 Highway 11까지 도달. USGS HVO Photo Chronology 공식 게시.
- **추세**: 2024-12-23 이후 46회 에피소드 지속. 에피소드 간격 13일→12일로 유사한 주기성 유지. 분출 규모는 Ep45(270m)→Ep46(200m)로 소폭 감소했으나 총 용암량(4.6M m³)은 여전히 대규모.

### Mayon 시리즈
- **이전**: ent-evt-029 (2026-01~, SO2 2,466t/d) → ent-evt-071 (5/5 VAAC)
- **금일**: (1) VAAC Tokyo 5/6 1252Z 화산재 경보 (Himawari-9 관측), (2) 용암류 Basud 방향 3.8km 도달, (3) 화쇄류 3km 범위, (4) PhilSA 위성 매핑으로 화산재 피복 면적 8,544ha 산출.
- **추세**: 5개월 이상 장기 분출 지속. PhilSA의 공식 위성 매핑은 필리핀 자국 우주역량의 재해 대응 활용 측면에서 유의미.

### Georgia 산불 시리즈
- **이전**: ent-evt-020 (4/30 최초) → ent-evt-072 (5/5 85%/50%)
- **금일**: Hwy 82 화재 22,471ac 85% 봉쇄(변동 없음), Pineland Rd 32,575ac 65% 봉쇄(50%→65% 상승). Landsat 8 OLI 위성 추적 지속.
- **추세**: 양 화재 모두 봉쇄율 상승세 지속. Pineland이 15%p 진전으로 주목. 완전 진화까지 수일 소요 전망.

### MethaneSAT 시리즈
- **이전**: ent-evt-053 (2/6 글로벌 평가) → ent-evt-066 (3/19 Permian Basin 상원 조사)
- **금일**: NM 주 1.2% vs TX 주 3.1% 메탄 강도 비교 데이터 공개. 동일 유전지대 내 규제 효과 차이의 위성 증거. 미 상원 조사 지속.
- **추세**: MethaneSAT 데이터가 정책 결정(상원 조사)에 직접 활용되는 사례로, 위성 관측→정책 피드백 루프의 대표적 성공 사례.

## 도메인별 흐름 분석

### 자연재해 (Disaster) — 4건

- **Kilauea Episode 46 종료** (업데이트, temp-086): 5/5 시작된 분출이 9시간 만에 종료. 650ft 용암 분수는 Ep45(270m≈886ft) 대비 감소했으나, 총 용암량 4.6M m³는 단일 에피소드 기준 대규모. 테프라가 Highway 11까지 도달해 교통 영향. GOES-18 열적외 + USGS 지상 관측 교차.
- **Mayon 화산 분출 지속** (업데이트, temp-087): VAAC Tokyo 화산재 자문 발표(5/6 1252Z). Himawari-9 정지궤도 위성 실시간 관측. 용암 3.8km, 화쇄류 3km — 위험 반경 확대 추세.
- **Mayon 화산재 위성 매핑** (신규, temp-082): PhilSA가 자국 위성 데이터로 화산재 피복 면적 8,544ha(케손시 절반 규모) 산출. 필리핀 국가우주기관의 재해 대응 위성 역량 입증. officialBoost +0.15 적용.
- **조지아 산불** (업데이트, temp-088): Pineland Rd 50%→65% 봉쇄 상승. Landsat 8 OLI 시계열 추적 지속.

### 국방·안보 (Defense) — 2건

- **이란 미군기지 피해 위성 평가** (신규, temp-081): WashPost 탐사보도 — Copernicus(ESA) + Planet Labs 위성영상으로 이란 미사일 공격에 의한 미군기지(UAE Al Dhafra 등) 피해 228개 구조물 파손 확인. 미국 정부 공식 발표보다 실질 피해 규모 큼. **multiSatBoost +0.20** (Copernicus+Planet 독립 교차검증).
- **이란 핵시설 생존 평가** (신규, temp-085): CNN 탐사보도 — 미국-이스라엘 공습 후 이란 일부 핵시설이 파괴를 면한 것으로 위성영상 확인. 미국 정부의 "핵역량 완전 무력화" 주장과 상충. confidence 0.80(위성 소스 특정 불명확).

### 인간활동 (HumanActivity) — 1건

- **아마존 금 채굴 삼림벌채** (신규, temp-083): AP/Amazon Conservation 공동 연구 — 2018년 이후 브라질 아마존 금 채굴로 인한 삼림벌채 면적 496,000ha. Sentinel-2 + PlanetScope 시계열 분석. 단일 원인 삼림 손실 중 최대 규모. Oregon State Conflict Ecology Lab 연구 협력. **multiSatBoost +0.20** (Sentinel-2+PlanetScope).

### 기후·환경 (ClimateEnvironment) — 1건

- **MethaneSAT Permian Basin 메탄 격차** (업데이트, temp-089): 뉴멕시코 1.2% vs 텍사스 3.1% 메탄 강도. 동일 유전지대 내 규제 정책 효과 차이를 위성으로 정량 증명. 미 상원 환경위 조사 근거자료로 활용. EDF 분석. officialBoost 비적용(NGO 분석), analystBoost +0.10.

### 인도주의 (Humanitarian) — 2건

- **이란 민간 시설 피해** (신규, temp-084): Bloomberg 시각화 보도 — Sentinel-2+Planet 전후비교 영상으로 7,645동 민간·군사 건물 피해 확인. 이란 이스파한 일대. temp-081(미군기지 피해)의 cascading 이벤트(동일 분쟁의 상대측 피해). **multiSatBoost +0.20**.
- **UNOSAT 가자 피해** (업데이트, temp-090): 198,273 구조물 중 81% 파손. UNOSAT 공식. officialBoost +0.15.

### 농업·해양 (AgricultureMaritime) — 0건 (신규)

- 금일 신규 농업·해양 이벤트 없음. 이전 CAS500-2 스마트농업(ent-evt-079) 관련 src-013 재보도 존재하나 내용 업데이트 없음.

## 온톨로지 변경 요약

### 새 인스턴스

- **기관 5건**:
  - org-philsa: PhilSA (Philippine Space Agency), space_agency, PH — 마욘 화산재 매핑 주체
  - org-washpost: Washington Post, media, US — 이란 미군기지 위성 탐사보도
  - org-bloomberg: Bloomberg, media, US — 이란 민간 피해 위성 시각화
  - org-amazon-conservation: Amazon Conservation, ngo, US — 아마존 금 채굴 위성 연구
  - org-oregon-state: Oregon State Conflict Ecology Lab, research, US — 아마존 연구 협력기관

- **국가 1건**:
  - co-ae: 아랍에미리트 (UAE, AE, 서아시아) — Al Dhafra 공군기지 소재국

- **위치 3건**:
  - ent-loc-030: Al Dhafra Air Base, Abu Dhabi, UAE (lat 24.0, lon 54.0)
  - ent-loc-031: Isfahan Nuclear Complex, Iran (lat 32.65, lon 51.68)
  - ent-loc-032: Amazon Basin gold mining zone, Para/Mato Grosso, Brazil (lat -5.0, lon -53.0)

- **이벤트 5건 (신규)**: temp-081~085 → ent-evt-081~085

### 기존 인스턴스 업데이트

- co-ir (이란): mention_count 증가 (1→4) — 금일 핵심 관련국
- co-ph (필리핀): mention_count 증가 (2→4) — Mayon 지속 분출
- co-br (브라질): mention_count 증가 (0→1) — 아마존 금 채굴
- ent-evt-021 (Kilauea): 시리즈 연장, Ep46 종료 기록
- ent-evt-029 (Mayon): 시리즈 연장, 용암/화쇄류 범위 갱신
- ent-evt-020 (Georgia wildfires): Pineland 65% 봉쇄 기록
- ent-evt-053 (MethaneSAT): Permian Basin NM/TX 비교 데이터 추가
- ent-evt-028 (UNOSAT Gaza): 198,273 구조물 81% 파손 갱신

### 스키마 변경

- 없음. 기존 관계 유형(`observedBy`, `manifests`, `inDomain`, `inCountry`, `locatedIn`, `analyzedBy`, `partOfSeries`, `usesSensor`, `cascadedFrom`)으로 충분히 표현 가능.

## 추론 결과

### 1. 다중위성 교차검증 (multiSatBoost +0.20)

| 이벤트 | 위성 1 | 위성 2 | 부스트 |
|--------|--------|--------|--------|
| temp-081 (이란 미군기지) | Copernicus Sentinel-2 (ESA, 10m) | PlanetScope (Planet, 3m) | +0.20 |
| temp-082 (마욘 화산재) | Himawari-9 (JMA, 정지궤도) | PhilSA 위성 (광학) | +0.20 |
| temp-083 (아마존 금 채굴) | Sentinel-2 (ESA, 10m) | PlanetScope (Planet, 3m) | +0.20 |
| temp-084 (이란 민간 피해) | Sentinel-2 (ESA, 10m) | PlanetScope (Planet, 3m) | +0.20 |

금일 4건 다중위성 교차검증 — 전일(1건) 대비 대폭 증가. Sentinel-2+PlanetScope 조합이 3회 사용되어 ESA 공개 데이터 + Planet 상업 고해상도의 보완적 교차검증 패턴이 확립됨.

### 2. Cascading Event (연쇄 이벤트) 분석

```
temp-081 (이란의 미군기지 공격 피해)
  └─ cascadedFrom → [이란-이스라엘/미국 분쟁 시리즈]
      ├─ temp-084 (이란 민간·군사 시설 보복 피해 7,645동)
      └─ temp-085 (이란 핵시설 생존 평가)
```

동일 분쟁의 양측 피해를 독립적 위성 분석으로 확인하는 구도:
- src-001 (WashPost): 미군 측 피해 → Copernicus+Planet 교차 (confidence 0.90)
- src-008 (Bloomberg): 이란 측 피해 → Sentinel-2+Planet 교차 (confidence 0.85)
- src-021 (CNN): 이란 핵시설 잔존 → 위성 소스 불명확 (confidence 0.80)

### 3. Sensor Capability Match (센서-현상 적합성)

| 이벤트 유형 | 사용 센서 | 적합성 | 가산 |
|------------|-----------|--------|------|
| 군사 구조물 피해 (temp-081, 084) | MSI 10m + PlanetScope 3m 광학 | 고해상도 광학 → 건물 피해 식별 최적 | hiResBoost +0.15 |
| 화산재 범위 (temp-082) | Himawari-9 AHI 정지궤도 | 광역 열적외 → 화산재 구름 추적 최적 | 열적외 가산 |
| 삼림 손실 (temp-083) | MSI 10m 다분광 + PlanetScope | NDVI/NBR 산출 → 삼림벌채 탐지 최적 | 다분광 가산 |
| 메탄 배출 (temp-089) | MethaneSAT XCH4 | 초분광/온실가스 → 메탄 플룸 탐지 전용 | 초분광 가산 |
| 산불 진화 (temp-088) | Landsat 8 OLI+TIRS | 열적외+NBR → 활성 화재+소실 면적 | 열적외 가산 |

### 4. 공식 기관 신뢰도 (officialBoost +0.15)

- temp-082: PhilSA 공식 분석 → +0.15
- temp-086: USGS HVO 공식 보고 → +0.15
- temp-090: UNOSAT 공식 평가 → +0.15
- temp-089: EDF/MethaneSAT → analystBoost +0.10 (NGO이므로 officialBoost 비적용)

### 5. Before/After 전후비교 가용성

금일 전후비교 영상 보유 이벤트:
- temp-081 (이란 미군기지): 공격 전후 위성영상 명시적 대비 (WashPost)
- temp-083 (아마존 금 채굴): 2018년 기준 vs 2026년 현재 시계열 비교
- temp-084 (이란 민간 피해): Bloomberg 인터랙티브 전후비교
- temp-086 (Kilauea): 분출 전후 칼데라 형상 변화
- temp-088 (Georgia): 화재 진행 시계열

## Key Insight (핵심 인사이트)

오늘의 핵심은 세 가지이다:

### 1. WashPost 이란 미군기지 피해 위성 교차검증 (Copernicus+Planet)

미국 정부 공식 발표와 상충하는 독립 위성 분석의 대표적 사례. Copernicus(ESA 공개 데이터)와 Planet(상업 고해상도)의 교차검증으로 228개 구조물 파손을 정량 확인. OSINT 위성영상이 정부 발표의 사실관계를 검증하는 기능을 입증. 이는 2026년 이란 분쟁에서 상업 위성영상의 전략적 가치가 극대화되는 시점과 일치한다(cf. ent-evt-064 Planet 배포 중단과 대비).

### 2. PhilSA 마욘 화산재 위성 매핑

동남아시아 개발도상국의 국가우주기관이 자연재해 대응에 자국 위성 역량을 활용한 사례. 8,544ha라는 정량적 피해 면적 산출은 재해 대응 자원 배분의 근거로 활용 가능. Himawari-9(일본 기상위성)와의 교차로 관측 시간대 보완(정지궤도 실시간 + 저궤도 고해상도).

### 3. 아마존 금 채굴 대규모 위성 모니터링 연구

496,000ha(서울 면적의 8배)라는 단일 원인 삼림 손실의 위성 정량 평가. Sentinel-2+PlanetScope 8년간 시계열 분석으로 불법 채굴의 시공간적 확산 패턴 규명. 학술(Oregon State) + NGO(Amazon Conservation) + 언론(AP) 삼각 협력 모델이 위성 기반 환경 감시의 모범 사례.

## 통계
- 총 이벤트: 10건 (신규 5 + 업데이트 5)
- 도메인별: Disaster 4, Defense 2, HumanActivity 1, ClimateEnvironment 1, Humanitarian 2, AgriMarine 0(신규)
- 다중위성 확인: 4건 (전일 대비 +3)
- 전후비교(before/after): 5건
- Cascading event: 1개 체인 (3건 연결)
- 한반도 GeoFocus: 0건
