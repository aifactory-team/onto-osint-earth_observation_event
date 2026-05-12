# 2026-05-11 분석

## 신규 소스 중요도 평가

### 높음
1. **Florida Everglades Max Road Fire** (src-001): 미국 플로리다 에버글레이즈 대형 산불. 11,000ac(4,452ha) 연소, 50% 진화. GOES/VIIRS 위성 추적. 마이애미 메트로 인접으로 대기질·대피 영향. 플로리다 주 전체 61건 산불 활성.
2. **NASA EO Barents Sea 북극 해빙 기록** (src-003): ICESat-2 위성 확인, 2026년 3월 15일 해빙 최대면적 14.29M km² — 1979년 관측 이래 최저 타이 기록. 바렌츠해 얼음 완전 소실이 핵심 원인. 기후변화 핵심 신호.
3. **Ibu 화산 폭발적 분출** (src-004): 인도네시아 할마헤라. 2026년 641건 분출. Dukono(3명 사망)와 같은 섬(할마헤라)에서 동시 화산 활동 — 지역 화산 불안정 경고.

### 중간
4. **NASA EO Mid-Atlantic 해양색** (src-002): MODIS Aqua 관측 식물플랑크톤 블룸. 해양 생태계 모니터링 사례.
5. **NASA EO Ahuachapán** (src-005): 엘살바도르 지열·화산 지형 Landsat 8 피처. 관측 영상은 2024-11-25. 지열 에너지·화산 모니터링 사례. 현재 이벤트 아님.

## 업데이트 항목 변경사항
- **Mayon (ent-evt-082)**: Day 125→127, 스트롬볼리 활동(5/11 20:43 관측). ReliefWeb GLIDE 등록(5/10).
- **Kilauea (ent-evt-202)**: Ep47 예측 창 5/12~15로 수렴. 강한 분화구 발광·가스 화염 관측.
- **Great Sitkin (ent-evt-203)**: SAR 위성 레이더로 용암류 동쪽 성장 신규 확인. 구름 투과 관측의 SAR 이점 발휘.
- **Shishaldin (ent-evt-204)**: SO2·증기 위성 관측 지속. TROPOMI trace_gas 적합성.
- **Georgia Pineland (temp-evt-001)**: 70~87% 진화. 이탄층 지하화재 난항. 건조 예보로 화~목 진화 차질 우려.
- **Caloy/Hagupit (ent-evt-127)**: 잔여저기압 전환 완료. 이벤트 종결 단계.

## 도메인별 흐름 분석
- **자연재해**: 화산 분출 집중(Mayon 127일, Kilauea 임박, Great Sitkin SAR, Shishaldin SO2, Ibu 신규). 산불 2건(Florida 신규, Georgia 후속). 서태평양 열대저기압(Caloy) 종결.
- **인간활동**: 금일 신규 없음. Pemex 유출·Amazon 채굴·NISAR 삼림벌채 모두 이전 보도 유지.
- **기후·환경**: 북극 해빙 기록적 저점 NASA EO 분석 신규. Sentinel-2A/2C 정상 복구 확인.
- **농업·해양**: Mid-Atlantic 식물플랑크톤 MODIS 관측 신규. NLL 어선·CAS500-2 변동 없음.
- **국방·안보**: 금일 신규 없음. CSIS BP·스프래틀리·이란 모두 기존 보도 유지.
- **인도주의**: 금일 신규 없음. Mayon GLIDE 이미 5/10 등록.

## 온톨로지 변경
- 신규 위성: ICESat-2 (NASA, lidar, 해빙·빙하 고도 측정)
- 신규 국가: 엘살바도르(SV)
- 신규 이벤트: 5건(Florida 산불, Mid-Atlantic 블룸, 북극 해빙, Ibu 화산, Ahuachapán)
- 기존 이벤트 업데이트: 6건

## 추론 결과
- **multi_satellite_confirmation**: Florida 산불(GOES-18 + VIIRS), Georgia 산불(VIIRS + Landsat 8 + Landsat 9), Mayon(Himawari-9 + Sentinel-2A), Kilauea(Sentinel-2A + Landsat 9), Caloy(Himawari-9 + GOES-18)
- **sensor_capability_match_sar**: Great Sitkin SAR 용암류 관측 — 구름 투과 능력으로 광학 실패 시에도 관측 성공 (sarBoost +0.10)
- **sensor_capability_match_tracegas**: Shishaldin TROPOMI SO2 (tracegasBoost +0.15)
- **official_source_trust**: NASA EO(Barents Sea, Mid-Atlantic, Ahuachapán), USGS HVO/AVO(Kilauea, Great Sitkin, Shishaldin) — officialBoost +0.15
- **temporal_progression**: Mayon ent-evt-082 partOfSeries(125→127일), Kilauea ent-evt-202 partOfSeries(Ep46→Ep47), Georgia temp-evt-001 partOfSeries
