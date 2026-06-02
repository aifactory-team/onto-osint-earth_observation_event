# 2026-06-02 분석

## 신규 소스 중요도 평가

| 소스 | 중요도 | 근거 |
|------|--------|------|
| src-001/002 Kilauea Ep48 분수분출 개시 | **높음** | 기록적 48번째 에피소드 공식 시작. 200m 분수, 24,000ft plume. USGS 공식. |
| src-003/004/013 태풍 Jangmi 오키나와 | **높음** | 필리핀 이후 일본 영향. 400+ 항공편 취소. 162km/h. JMA 긴급경보. |
| src-005/006 El Niño Super El Niño | **높음** | CPC '단일 가장 유력 결과' 상향. ECMWF 100%. Kelvin wave 1997-98 초과. 역사적 에스컬레이션. |
| src-012 Gaza 위성 피해 평가 | **높음** | UNOSAT Sentinel-1 포괄적 분석 — 197,000건(80%). 인도주의 도메인 핵심. |
| src-021 Sangay/Reventador | **중간** | 에콰도르 화산 지속 활동. 위성 ash 모니터링 확인. 신규 국가 추가 필요(EC). |
| src-006 First El Niño impacts | **중간** | 6월 미국/캐나다 대기 응답 첫 감지. 기후 도메인 신규 이벤트. |

## 기존 추적 항목 변경사항

1. **Kilauea (evt-202):** 전조 오버플로우 → **본격 분수분출 시작**. ADVISORY→WATCH 유지. 200m 분수(record). 상태 대폭 변경.
2. **태풍 Jangmi (temp-evt-2001):** 필리핀 PAR 이탈 → **일본 오키나와 접근**. 영향 국가 변경(PH→JP). 400+ 항공편 취소. 새로운 위험 지역.
3. **El Niño (temp-evt-1902):** 96% → **CPC Super El Niño '가장 유력'**, ECMWF 100%. Kelvin wave +8°C(역사적). 6월 대기 응답 첫 감지.
4. **캐나다 산불 (evt-1101):** 65건/33,400+ 대피 지속. 변동 없음.
5. **Bismarck Sea (evt-701):** Day 25+. 부석 70km². 신규 섬 가능성 과학자 주시. 변동 미미.
6. **Mayon (evt-082):** Day 147+. 287,000+ 이재민. 우기 접근 라하르 위험. 변동 미미.

## 도메인별 흐름

- **자연재해:** Kilauea Ep48 본격 시작(금일 핵심), 태풍 Jangmi 오키나와 접근, 화산 5건 추적 지속, Sangay/Reventador 신규
- **인간활동:** 금일 신규 없음 (추적 지속: Antelope Reef, 스프래틀리, DPRK 교량)
- **기후·환경:** El Niño Super 에스컬레이션(금일 핵심), 첫 대기 응답 감지
- **농업·해양:** 금일 신규 없음 (El Niño가 농업·해양에도 교차 영향)
- **국방·안보:** 금일 신규 없음 (추적 지속: DPRK 구축함, Hami ICBM)
- **인도주의:** Gaza 위성 피해 평가 신규, 캐나다 산불 인도주의 교차 지속

## 온톨로지 변경 요약

- 신규 국가: 에콰도르(EC) — Sangay/Reventador 화산
- 신규 Location: 오키나와(JP) — 태풍 Jangmi 영향 지역
- 기존 인스턴스 업데이트: evt-202 상태 대폭 변경, temp-evt-2001 영향 국가 추가(JP), temp-evt-1902 에스컬레이션

## 추론 결과 요약

1. **temporal_progression:** Kilauea Ep48(evt-202) partOfSeries Ep47 — 같은 위치·같은 현상의 시계열 연속
2. **official_source_trust:** Kilauea(USGS HVO) +0.15, El Niño(NOAA CPC) +0.15, Gaza(UNOSAT) +0.15
3. **sensor_capability_match_sar:** Gaza UNOSAT Sentinel-1 SAR 피해 평가 — sarBoost +0.10
4. **before_after_credibility:** Gaza before/after +0.10
5. **multiSatBoost:** 기존 4건 유지 (Bismarck 5위성, 캐나다 5위성, Kharg 3위성, Hami 2위성)
6. **cascading_disaster:** 태풍 Jangmi → 오키나와 산사태/홍수 잠정 (6/2-3)
7. **severity_priority:** Kilauea +0.20, 태풍 Jangmi +0.20, 캐나다 산불 +0.20
