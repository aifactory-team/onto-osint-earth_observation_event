# 2026-05-04 분석

## 도메인별 흐름 분석

### 자연재해 (Disaster)
- **Kīlauea Episode 46 예보** (업데이트): USGS HVO가 5/4-7 분출 창을 공식 확인. 팽창 틸트 급속 복귀, 양 화구에서 강한 글로우·가스 방출 관측. 2024-12-23 이후 45회 에피소드 경과. GOES-18 열적외로 실시간 모니터링 중.
- **조지아 산불** (업데이트): Landsat 8 OLI 위성 허위색 영상으로 피해 범위 확인. Hwy 82 75%, Pineland Rd 44% 진화. 총 55,000에이커 이상. NASA Earth Observatory 공식 분석 게시.
- **Mayon 화산** (업데이트): 5/2 화쇄류(PDC) 발생, Himawari-9 VAAC 화산재 자문 FL060. 지속적 분출 중.

### 인간활동 (HumanActivity)
- 금일 신규 보도 없음. 이전 아마존 불법 채굴(ent-evt-054), 브라질 DETER 금지 법안(ent-evt-055) 추적 지속.

### 기후·환경 (ClimateEnvironment)
- **MethaneSAT Permian Basin 상원 조사** (신규): Senator Whitehouse가 EPA 추정치 vs MethaneSAT 실측치 4배 격차 공식 조사 착수. 위성 데이터가 정책적 행동으로 전환된 첫 사례.
- **그린란드 빙하 후퇴** (신규): 주변 빙하 후퇴율 20년간 2배 가속. Landsat+Sentinel-2 다중위성 분석. 해수면 상승 기여 14%.

### 농업·해양 (AgricultureMaritime)
- 금일 신규 없음. CAS500-4 광대역 센서가 향후 농업/산림 모니터링에 기여 예정.

### 국방·안보 (Defense)
- **가자 군사 시설 확장** (신규): Planet+Sentinel 다중위성 교차 확인. 48개 군사 시설 중 13개가 휴전 이후 건설. Rafah 중심.
- **레바논 파괴** (업데이트): CNN/Airbus 위성으로 523건 건물 파괴 정량 분석. 3월 공세 10일간.
- **Lop Nur 확장** (신규): 60,000 sq ft 격납고, J-36 스텔스기 시험. 상업 위성영상 분석.
- **미국 이란 인근 집결** (신규): 중국 위성이 사우디 Prince Sultan AB에서 E-3/KC-135 대규모 배치 포착. 150대+ 항공기, 12척 군함.
- **영변 핵단지** (업데이트): RFA — 2026년 연중 5MW 원자로 가동 지속, 재처리연구소 간헐적 활동 확인.
- **Planet Labs 이란 블랙아웃** (신규): 미 정부 요청으로 이란/중동 위성영상 무기한 배포 중단. Vantor/BlackSky도 유사 조치. 상업 EO OSINT 투명성 구조적 제약.

### 인도주의 (Humanitarian)
- **레바논 파괴** (업데이트): CNN 분석이 인도주의 측면에서도 중요 — 모스크, 약국, 주거지 파괴 확인.

## 온톨로지 변경 요약
- 새 국가: 사우디아라비아(SA), 그린란드(GL)
- 새 위치: Lop Nur Test Base, Bint Jbeil
- 새 이벤트: 7건 (ent-evt-059~068)
- 스키마 변경: 없음 (기존 클래스/관계로 충분히 표현)

## 추론 결과 요약
1. **multi_satellite_confirmation**: 가자 군사 시설 확장(PlanetScope+Sentinel-2A) → +0.20
2. **multi_satellite_confirmation**: 그린란드 빙하 후퇴(Landsat 8+Sentinel-2A) → +0.20
3. **official_source_trust**: Kīlauea(USGS) → +0.15, 조지아 산불(NASA) → +0.15
4. **korea_geo_focus**: 영변 핵단지(KP) → +0.10
5. **sensor_capability_match_tracegas**: MethaneSAT Permian(trace_gas 센서) → +0.15
6. **before_after_credibility**: 조지아 산불, 레바논 파괴, Lop Nur → 각 +0.10
7. **temporal_progression**: Kīlauea ep46 partOfSeries ep45, Mayon 5/2 partOfSeries 이전
