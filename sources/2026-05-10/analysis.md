# 2026-05-10 분석

## 요약
금일은 대규모 신규 이벤트 없이 기존 추적 이벤트들의 후속 업데이트가 주를 이루는 날. 9건 업데이트 + 1건 신규(Mayon 인도주의 등록). 화산 활동이 가장 활발한 도메인이며, 필리핀(Mayon 125일 분출 + Dukono 수색 완료 + Caloy 약화)이 금일 가장 많은 이벤트 집중 지역.

## 도메인별 흐름

### 자연재해 (Disaster) — 8건 업데이트
- **Mayon 화산**: 125일 연속 분출. VAAC 589 발행 (FL090 WSW). Alert Level 3 유지. PhilSA Sentinel-2로 작물피해 1,039ha 벼 확인. 인도주의 차원으로 확대 (ReliefWeb GLIDE 등록).
- **Dukono 화산**: 수색 완료. 싱가포르인 2명 시신 5/10 수습, 총 사망 3명. 사건 종결.
- **Caloy/Hagupit**: TS→TD 약화 (55km/h). 잔여저기압 전환 예상. 필리핀 직접 영향 미미.
- **Kilauea**: Ep46 종료 후 팽창 10.7μrad. Ep47 예측 창 5/12~15.
- **Great Sitkin**: WATCH/ORANGE. 용암돔 지속 분출, 낙석 지진 검출. 구름으로 위성 관측 제한.
- **Shishaldin**: ADVISORY/YELLOW. SO2·증기 위성 관측 지속.
- **Georgia Pineland Road**: 32,575ac 70% 진화. 이탄층 지하화재 난항.

### 인간활동 (Human Activity) — 신규 없음
Pemex Cantarell 유출, Amazon Xingu 금광, Philippines Spratly 건설 등 기존 추적 이벤트 금일 신규 보도 없음.

### 기후·환경 (Climate & Environment) — 1건 업데이트
- **Sentinel-2A/2C**: NorthC 화재 후 5/7 19:00 UTC 정상 복구 완료.

### 농업·해양 (Agriculture & Maritime) — 1건 업데이트
- **Mayon ashfall 작물피해**: Manila Times 1,039ha 벼 + 191ha 기타 확인 보도 (PhilSA Sentinel-2 데이터 기반).

### 국방·안보 (Defense) — 신규 없음
이란-미국 기지, CSIS Beyond Parallel NK, SCS 등 금일 신규 위성 분석 없음.

### 인도주의 (Humanitarian) — 1건 신규
- **Mayon ReliefWeb GLIDE VO-2026-000065-PHL**: 화산 분출→작물피해→건강피해 인과 사슬로 인도주의 차원 공식화.

## 온톨로지 변경
- 신규 Organization 1건: org-ocha (UN OCHA / ReliefWeb, un_body)
- 신규 Event 1건: ent-evt-401 (Mayon 인도주의 등록)
- 스키마 변경: 없음 (기존 클래스/관계 유형으로 충분)

## 추론 결과
- multi_satellite_confirmation 1건: ent-evt-401 (Sentinel-2A + Himawari-9)
- cascading_disaster 1건: ent-evt-082 (Mayon eruption) → ent-evt-401 (humanitarian)
- official_source_trust 1건: ent-evt-401 (UN OCHA)
- tracegasBoost 1건: ent-evt-204 (Shishaldin SO2, TROPOMI)
- partOfSeries 5건: Mayon/Caloy/Dukono/Kilauea/GA Pineland 시계열 지속
