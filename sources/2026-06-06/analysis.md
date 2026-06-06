# 2026-06-06 온톨로지 분석

## 1. 신규 엔티티 (New Entities) -- 3건

### evt-2601: NASA EO 'Fighting Fire With Fire' -- 호주 노던 테리토리 계획 소각
- **유형:** Event
- **도메인:** Disaster (dom-disaster)
- **현상:** prescribed_burn (phen-prescribed-burn, phen-wildfire 하위)
- **위치:** Northern Territory, Australia (-13.0, 132.0)
- **국가:** AU (co-au)
- **위성:** MODIS (Aqua, 5/28 촬영), MODIS (Terra), VIIRS
- **기관:** NASA Earth Observatory (org-nasa)
- **신뢰도 산정:**
  - 기본: 0.75
  - officialBoost: +0.15 (NASA EO 공식 게시)
  - **최종: 0.90**
- **분석:** NASA EO 'Fighting Fire With Fire' 기사. 호주 노던 테리토리 건기 초기 계획 소각(prescribed burn)을 MODIS Aqua가 5/28 촬영. 원주민 전통 화재 관리(early dry season burning) 기법과 현대 위성 모니터링의 융합 사례. 열적외 센서(MODIS, VIIRS)로 화점 탐지. 위성영상 기반 화재 관리 전략의 효과성 평가에 활용. 자연재해 카테고리 내 '화재 관리' 서브카테고리 -- 일반 산불(wildfire)과 구분하여 phen-prescribed-burn 신규 하위 현상 생성.

### evt-2602: 북한 모내기 68.2% -- Landsat 8/9 NDVI 분석
- **유형:** Event
- **도메인:** AgricultureMaritime (dom-agri-marine)
- **현상:** ndvi_change (phen-ndvi)
- **위치:** DPRK nationwide, 8 sample sites (39.0, 126.0)
- **국가:** KP (co-kp)
- **위성:** Landsat-8 (OLI), Landsat-9 (OLI-2)
- **기관:** Daily NK (org-dailynk)
- **신뢰도 산정:**
  - 기본: 0.60
  - koreaBoost: +0.10 (KP 한반도 GeoFocus)
  - analystBoost: +0.10 (DailyNK 전문 분석기관)
  - baCredibilityBoost: +0.10 (NDVI 시계열 전후비교)
  - **최종: 0.80 (analyst cap 적용)**
- **분석:** DailyNK 보도. Landsat 8/9 위성영상 NDVI 시계열 분석으로 북한 전역 모내기 진척률 68.2% 추정. 8개 표본 지역(평안남도, 황해남도, 함경남도 등 곡창지대) 대상. 전년 동기(71.3%) 대비 3.1%p 지연 -- 5월 강수 부족과 비료 공급 제한이 원인. 위성 기반 식생지수로 북한 식량 안보 간접 평가. 농업/해양 의무 카테고리 충족. 한반도 GeoFocus 가산.

### evt-2603: 캐나다 산불 대폭 확대 -- 134건, 113,300 ha (evt-1101 후속)
- **유형:** Event
- **도메인:** Disaster (dom-disaster)
- **현상:** wildfire (phen-wildfire)
- **위치:** Canada, multiple provinces (55.0, -105.0)
- **국가:** CA (co-ca)
- **위성:** VIIRS (Suomi NPP, NOAA-21), MODIS (Terra/Aqua), GOES-18 (ABI), Sentinel-2 (MSI), Sentinel-5P (TROPOMI)
- **기관:** NOAA NESDIS (org-nesdis), SpaceQ (org-spaceq)
- **전후비교:** true (전일 65건 vs 금일 134건)
- **신뢰도 산정:**
  - 기본: 0.75
  - officialBoost: +0.15 (NOAA NESDIS 공식)
  - multiSatBoost: +0.20 (5위성 교차관측)
  - **최종: 0.95 (cap)**
- **분석:** evt-1101(캐나다 산불) 급격 악화. 전일 65건→134건(+106%), 소실 면적 18,935 ha→113,300 ha(약 6배 증가). 규모 변화가 너무 커 evt-2603으로 재분류(evt-1101 supersedes). NOAA NESDIS 위성 기반 연기 확산 모니터링. SpaceQ: WildfireSat 전용 산불 감시 위성 개발 가속 보도. 연기가 미국 북부까지 도달. 5위성 교차관측 유지(VIIRS 2기 + GOES-18 + Sentinel-2 + TROPOMI). 재해 우선순위 규칙에 따라 보고서 1순위 배치.

## 2. 주요 업데이트 엔티티 -- 16건

### temp-evt-2501: 시진핑 방북 6/8-9 확정 (신화통신 공식)
- 신화통신(Xinhua) 공식 발표: 시진핑 6월 8-9일 방북 확정.
- 이전 위성 관측(김일성광장 건설, 순안공항 재배치)에 의한 예측이 공식 확인됨.
- **위성 기반 예측 → 공식 확인 검증 사례(prediction_confirmed)**
- **최종 신뢰도: 0.95**

### evt-202: Kilauea -- ADVISORY/YELLOW, Ep48 기록, Ep49 10-15일
- ADVISORY/YELLOW 유지. Ep48 기록 갱신. Ep49 분출 10-15일 예보 지속.
- **최종 신뢰도: 0.90**

### evt-701: Bismarck Sea -- Day 29+, 감소 추세, pumice rafts
- Day 29+. 분출 감소 지속. 부석 뗏목(pumice rafts) 해상 표류 신규 관측.
- **최종 신뢰도: 0.80**

### evt-082: Mayon -- Day 152+, AL3, SO2 1,083-2,747 t/d, 3,975명 대피소
- Day 152+ 장기 분출. AL3 유지. SO2 범위 1,083-2,747 t/d (변동성 증가).
- 대피소 수용 3,975명(이전 287K 이재민 규모 대비 대피소 인원 구체화).
- **최종 신뢰도: 0.90**

### temp-evt-1902: El Nino -- Super El Nino 'single most likely outcome', ECMWF 100%
- NOAA CPC 82% May-Jul 유지. Super El Nino가 '가장 가능성 높은 단일 결과'로 격상.
- ECMWF 모델 100% 엘니뇨 예측. 인과 연계: Super El Nino → 허리케인 억제 강화.
- **최종 신뢰도: 0.92**

### evt-203/204: Great Sitkin WATCH / Shishaldin ADVISORY
- 변동 없음. 추적 지속.

### temp-evt-1401: Kanlaon -- AL2, SO2 2,382 t/d
- AL2 유지. SO2 2,382 t/d. 변동 없음.

### evt-128: Dukono -- AL2, 3명 사망
- AL2 유지. 3명 사망 확인 지속.

### temp-evt-2203: Sangay/Reventador -- 분출 지속
- 에콰도르 화산 분출 지속.

### evt-1201: Santa Rosa -- 97%, BAER 팀 도착
- 97% 진화 유지. BAER 팀 6/5 현장 도착 확인. 종결 임박.

### temp-evt-2001: Jangmi -- 소멸, 일본 복구
- 소멸 확인. 일본 피해 복구 진행 중. 종결.

### temp-evt-2504: Sentinel-1 재구성 일정 확정
- S-1C 6/9-23 취득 중단(궤도 기동). S-1A 6/29 임무 종료.
- 구체 일정 확정. 글로벌 SAR 역량 영향 D-3 임박.

### evt-2503: Sentinel-1D clock anomaly 해소
- S-1D 클럭 이상 해소 확인. 정상 운용 복귀.

## 3. 추론 결과 요약

| 추론 규칙 | 건수 | 대상 |
|-----------|------|------|
| official_source_trust | 2건 | evt-2601(NASA), evt-2603(NOAA NESDIS) |
| korea_geo_focus | 1건 신규 | evt-2602(KP 전역) |
| analyst_credibility | 1건 | evt-2602(DailyNK) |
| multi_satellite_confirmation | 1건 신규 | evt-2603(5위성) |
| temporal_escalation | 1건 신규 | evt-2603(면적 6배 증가) |
| before_after_credibility | 1건 | evt-2602(NDVI 시계열) |
| enso_hurricane_suppression | 1건 강화 | temp-evt-1902→evt-2505 인과 |
| satellite_prediction_validation | 1건 신규 | temp-evt-2501(위성 예측 → 공식 확인) |
| temporal_progression | 2건 | evt-202(Kilauea Ep48), evt-701(Day 29+) |
| infrastructure_impact | 1건 | temp-evt-2504(글로벌 SAR 역량) |

## 4. 온톨로지 변경 요약

| 변경 유형 | 대상 | 근거 |
|----------|------|------|
| 새 Phenomenon | phen-prescribed-burn (1건) | wildfire 하위: 계획 소각 구분 |
| 새 Location | loc-australia-nt, loc-dprk-nationwide (2건) | 호주 NT, 북한 전역 |
| 새 Organization | org-spaceq, org-xinhua, org-ecmwf (3건) | SpaceQ, 신화통신, ECMWF |
| 새 Event | evt-2601~2603 (3건) | 신규 이벤트 |
| 이벤트 업데이트 | 16건 | 후속 보도/공식 확인 반영 |
| 이벤트 계승 | evt-2603 supersedes evt-1101 | 규모 급변으로 재분류 |

## 5. 카테고리 커버리지

| 카테고리 | 신규 | 업데이트 | 상태 |
|----------|------|---------|------|
| 자연재해 (Disaster) | 2 (호주 계획 소각, 캐나다 산불 확대) | 10+ (화산 7, 산불 1, 태풍 1) | 충족 |
| 인간활동 (HumanActivity) | 0 | 1 (시진핑 방북 확정) | 충족 |
| 기후환경 (ClimateEnvironment) | 0 | 1 (El Nino Super 격상) | 충족 |
| 농업해양 (AgricultureMaritime) | 1 (DPRK 모내기 68.2%) | 1 (NISAR Maize Triangle) | 충족 |

4대 의무 카테고리 모두 커버 완료.

## 6. 특이사항

### 위성 기반 예측 검증 (Satellite Prediction Validation)
temp-evt-2501(시진핑 방북): 위성영상 기반 예측(김일성광장 건설, 순안공항 재배치)이 신화통신 공식 발표로 확인된 사례. 위성 OSINT의 예측력 검증 -- 온톨로지에 prediction_confirmed 추론 규칙 신규 추가.

### 캐나다 산불 급격 악화
evt-1101 → evt-2603: 24시간 내 화재 건수 106% 증가, 소실 면적 498% 증가. 급속 악화 패턴은 temporal_escalation 추론 규칙으로 포착. 재해 우선순위 규칙(인명피해·인프라파괴 동반) 적용.

### Sentinel-1 재구성 D-3
S-1C 취득 중단까지 3일(6/9). 글로벌 SAR 모니터링 역량에 2주간 공백 예상. 산불/홍수/해빙 등 SAR 의존 모니터링 항목에 영향.
