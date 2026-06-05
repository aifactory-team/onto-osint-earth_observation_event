# 2026-06-05 온톨로지 분석

## 1. 신규 엔티티 (New Entities) -- 5건

### temp-evt-2501: 시진핑 방북 준비 위성 관측 -- Kim Il Sung Square 건설 + Sunan Airport 정비
- **유형:** Event
- **도메인:** Defense (dom-defense)
- **현상:** construction (phen-construction) + military_buildup (phen-military, sub)
- **위치:** Kim Il Sung Square (39.02N, 125.75E) + Sunan Airport (39.22N, 125.67E), Pyongyang, KP
- **국가:** KP (co-kp)
- **위성:** WorldView-3 (Vantor, 0.31m 해상도, 5/30 촬영)
- **기관:** Vantor (org-vantor), Bloomberg/Seoul Economic Daily/Japan Times/NK Pro
- **전후비교:** true (before/after imagery available)
- **신뢰도 산정:**
  - 기본: 0.80 (다수 매체 교차보도)
  - hiResBoost: +0.15 (WorldView-3, 0.31m -- 리뷰스탠드+항공기 개별 식별)
  - koreaBoost: +0.10 (KP Pyongyang -- 한반도 GeoFocus)
  - baCredibilityBoost: +0.10 (Vantor before/after 가용)
  - **최종: 0.95 (cap)**
- **분석:** Vantor(구 Maxar Intelligence) 5/30 WorldView-3 위성영상으로 평양 김일성광장 리뷰스탠드 건설 및 수난국제공항 VIP 구역 항공기 8대 재배치 관측. Bloomberg, 서울경제, Japan Times, NK Pro 등 복수 매체 교차 보도. 6/11 시진핑 방북 추정 -- 2019년 이후 첫 방문. 군사적 함의(정상회담 의전 준비)와 건설 활동 동시 관측. 좌표 2개 사이트(광장+공항) 모두 기록. 민감 정보 처리: 군사적 함의 있으나 공개 OSINT 기반이며, 좌표는 행정구역 수준(평양직할시)으로 일반화.

### temp-evt-2502: NASA EO NISAR 남아프리카 옥수수 삼각지대 식생 변화
- **유형:** Event
- **도메인:** AgricultureMaritime (dom-agri-marine)
- **현상:** ndvi_change (phen-ndvi)
- **위치:** Maize Triangle, Free State, ZA (-28.5, 26.5)
- **국가:** ZA (co-za, 신규)
- **위성:** NISAR (sat-nisar, L-band SAR)
- **기관:** NASA EO (org-nasa)
- **신뢰도 산정:**
  - 기본: 0.75
  - officialBoost: +0.15 (NASA EO Image of the Day)
  - sarBoost: +0.10 (L-band SAR -- 작물 canopy penetration)
  - **최종: 0.90**
- **분석:** NASA EO Image of the Day 게재. NISAR L-band SAR로 남아프리카 Free State 옥수수 삼각지대 식생 구조 분석. L-band는 C-band/X-band 대비 작물 canopy 투과 능력 우수하여 농업 모니터링에 최적. 남아프리카공화국(ZA) 국가 인스턴스 신규 추가. 농업/해양 도메인 금일 유일 신규 이벤트로 카테고리 커버리지 충족.

### temp-evt-2503: Sentinel-1D SAR 데이터 품질 저하 -- internal clock corruption
- **유형:** Event (SatOps)
- **도메인:** SatOps
- **현상:** satellite_operations (phen-satops)
- **기간:** 2026-05-29 16:03 UTC ~ 2026-06-01 18:00 UTC
- **위성:** Sentinel-1D (sat-sentinel1d)
- **기관:** ESA (org-esa)
- **좌표:** 없음 (SatOps 이벤트)
- **신뢰도:** 0.90 (ESA 공식 공지)
- **분석:** Sentinel-1D 내부 클럭 손상으로 약 50시간 SAR 데이터 품질 저하. C-band SAR 데이터 시간 정밀도 영향. 글로벌 SAR 모니터링 역량에 일시적 공백. temp-evt-2504(콘스텔레이션 재구성)와 연계하여 Sentinel-1 운영 상태 종합 추적.

### temp-evt-2504: Sentinel-1 콘스텔레이션 재구성 -- S-1C 기동/S-1A 퇴역
- **유형:** Event (SatOps)
- **도메인:** SatOps
- **현상:** satellite_operations (phen-satops)
- **위성:** Sentinel-1A (sat-sentinel1a), Sentinel-1C (sat-sentinel1c), Sentinel-1D (sat-sentinel1d)
- **기관:** ESA (org-esa)
- **좌표:** 없음 (SatOps 이벤트)
- **신뢰도:** 0.92 (ESA 공식)
- **분석:** 6월 말 Sentinel-1C 2주간 궤도 기동 예정. 기동 완료 후 S-1A 퇴역, S-1C + S-1D 신규 2기 체제로 전환(2026년 7월). 전 세계 SAR 모니터링 역량에 단기 영향 가능. Sentinel-1A 장기 운용(2014년 발사, 12년 운용)에 따른 계획된 세대교체.

### temp-evt-2505: NOAA 2026 대서양 허리케인 시즌 below-normal 전망
- **유형:** Event
- **도메인:** ClimateEnvironment (dom-climate)
- **현상:** typhoon (phen-typhoon, 허리케인 시즌 전망)
- **위치:** Atlantic basin (0.0, -60.0)
- **기관:** NOAA CPC (org-noaa)
- **신뢰도 산정:**
  - 기본: 0.78
  - officialBoost: +0.15 (NOAA CPC 공식 계절 전망)
  - **최종: 0.90**
- **분석:** NOAA CPC 2026 대서양 허리케인 시즌 공식 전망. 55% 확률 below-normal, 8-14 named storms 예상. El Nino 발달에 의한 열대 대류 억제 메커니즘. temp-evt-1902(El Nino 82% May-Jul)와 직접 연계 -- El Nino -> 허리케인 억제 인과 구조. 2025년 record-breaking 시즌 대비 극적 감소 전망.

## 2. 주요 업데이트 엔티티 -- 14건

### evt-202: Kilauea -- ADVISORY/YELLOW 유지, Ep49 10-15일 예보
- ADVISORY/YELLOW 유지 (전일과 동일). Ep49 10-15일 예보 지속.
- 재팽창(reinflation) 지속. no material change.
- **최종 신뢰도: 0.90**

### evt-1101: 캐나다 산불 -- 65 active, 18,935 ha, 6 OOC
- 65건 활성 화재, 18,935 ha, 6건 통제 불능(OOC).
- 이전 400+ fires에서 규모 감소 추세.
- 5위성 3기관 multiSat 유지.
- **최종 신뢰도: 0.95**

### evt-701: Bismarck Sea -- Day 28+, 분출 감소 지속
- 분출 감소 추세 지속. Day 28+.
- 5위성 multiSat 유지.
- **최종 신뢰도: 0.95**

### evt-082: Mayon -- Day 150+, AL3, 287K+
- Day 150+ 장기 분출. AL3 유지. 287K+ 이재민 지속.
- **최종 신뢰도: 0.90**

### temp-evt-1902: El Nino -- 82% May-Jul, strong 2/3
- El Nino 82% May-Jul. Strong El Nino 확률 2/3.
- temp-evt-2505(허리케인 below-normal)와 직접 연계.
- **최종 신뢰도: 0.90**

### evt-203/204: Great Sitkin WATCH / Shishaldin ADVISORY
- 변동 없음. 추적 지속.

### temp-evt-1401: Kanlaon -- AL2, SO2 2382 t/d
- AL2 유지. SO2 2382 t/d.

### evt-128: Dukono -- AL2 유지
- AL2 유지. 추적 지속.

### temp-evt-2203: Sangay/Reventador -- 분출 지속
- 에콰도르 화산 분출 지속.

### evt-1201: Santa Rosa -- 97% contained, BAER June 5
- 97% contained. Burned Area Emergency Response(BAER) 평가 6/5 시행.
- 종결 임박.

### temp-evt-2001: Jangmi -- dissipated (소멸)
- 태평양 열린 해상에서 소멸 확인.
- cascading_disaster 이전 확정 상태 유지(종결).

### temp-evt-2401: Gaza 40+ military posts -- 보도 지속
- Al Jazeera 위성 분석 지속 보도.

### temp-evt-2002: Hami ICBM -- 보도 지속
- Reuters/NBC 보도 지속.

## 3. 추론 결과 요약

| 추론 규칙 | 건수 | 대상 |
|-----------|------|------|
| sensor_capability_match | 2건 | temp-evt-2501(hiRes), temp-evt-2502(sar) |
| official_source_trust | 2건 | temp-evt-2502(NASA), temp-evt-2505(NOAA) |
| korea_geo_focus | 1건 신규 | temp-evt-2501(KP Pyongyang) |
| before_after_credibility | 1건 신규 | temp-evt-2501(Vantor b/a) |
| temporal_progression | 4건 | evt-202(Kilauea), evt-701(Bismarck), evt-1101(Canada), evt-082(Mayon) |
| multi_satellite_confirmation | 5건 유지 | Bismarck/Canada/Kharg/Hami/Gaza |

## 4. 온톨로지 변경 요약

| 변경 유형 | 대상 | 근거 |
|----------|------|------|
| 새 Country | co-za (남아프리카공화국) (1건) | NISAR Maize Triangle |
| 새 Location | ent-loc-075~077 (3건) | Kim Il Sung Square, Sunan Airport, Maize Triangle |
| 새 Event | temp-evt-2501~2505 (5건) | 신규 이벤트 |
| 이벤트 업데이트 | 14건 | 후속 보도 반영 |

## 5. 카테고리 커버리지

| 카테고리 | 신규 | 업데이트 | 상태 |
|----------|------|---------|------|
| 자연재해 (Disaster) | 0 | 10+ (화산 7, 산불 2, 태풍 1 소멸) | 충족 |
| 인간활동 (HumanActivity) | 1 (시진핑 방북 건설) | 0 | 충족 |
| 기후환경 (ClimateEnvironment) | 1 (허리케인 전망) | 1 (El Nino) | 충족 |
| 농업해양 (AgricultureMaritime) | 1 (NISAR Maize Triangle) | 0 | 충족 |
| 국방안보 (Defense) | 1 (시진핑 방북) | 2 (Gaza, Hami) | 충족 |
| 인도주의 (Humanitarian) | 0 | 1 (Gaza) | 충족 |

4대 의무 카테고리 모두 커버 완료.
