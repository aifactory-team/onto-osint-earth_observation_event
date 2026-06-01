# 2026-06-01 분석

## 신규 소스 중요도 평가

| 소스 | 중요도 | 근거 |
|------|--------|------|
| src-001 Kilauea Ep48 전조 오버플로우 | **높음** | WATCH/ORANGE 격상, 기록적 에피소드 임박 |
| src-002 캐나다 산불 65건 | **높음** | 33,400+ 대피, 미국 AQI 악화 직접 영향 |
| src-003 Bismarck Sea day 24+ | **높음** | 5위성 3기관 교차검증, 신규 섬 형성 가능 |
| src-004 태풍 Domeng PAR 이탈 | **높음** | 832,986명 피해, Mayon ashfall 지역 교차 영향 |
| src-005 Mayon Day 146+ | **높음** | 287,000+ 이재민, 우기 라하르 위험 |
| src-006 El Niño 96% | **높음** | WMO/CPC 거의 만장일치, Super El Niño 1/3 |
| src-007 Bezymianny Yellow 하향 | **중간** | 활동 감소 — 추적 유지하되 위험 하향 |
| src-008 Kanlaon AL2 | **중간** | SO2 변동, 지속 모니터링 |
| src-009 Great Sitkin WATCH | **중간** | 용암 돔 지속, 변동 없음 |
| src-010 Shishaldin ADVISORY | **낮음** | SO2 지속, 변동 미미 |
| src-011 FireSat 배치 ★신규 | **중간** | 위성운영 이벤트, 산불 관측 역량 확대 |
| src-012 DPRK 최현함 6월 배치 | **높음** | 한반도 GeoFocus, 6월 중순 공식 배치 확인 |
| src-017 DPRK 구축함 종합 분석 ★신규 | **중간** | 2번함 사고 포함, 전투준비태세 분석 |

## 도메인별 흐름

### 자연재해 (Disaster)
- **Kilauea**: Ep48 전조 오버플로우 시작(5/30 17:41 HST). ADVISORY→WATCH/ORANGE 격상. 기록적 에피소드 수.
- **캐나다 산불**: 65건 활성, 6건 통제 불능, 18,935 ha. 연기 미국 중서부 AQI 악화(June 1).
- **Bismarck Sea**: day 24+, 부석 70km², 해저 플랫폼 성장 지속.
- **태풍 Domeng**: PAR 이탈 June 1, 832,986명 피해. habagat 증강으로 Mayon 지역 홍수/산사태.
- **Mayon**: Day 146+, 287K+ 이재민, 우기 접근 라하르 위험.
- **Bezymianny**: Yellow로 하향 — 5/21 이후 폭발적 활동 감소.
- **Kanlaon**: AL2, SO2 변동 지속.
- **Great Sitkin/Shishaldin**: WATCH/ADVISORY 유지.

### 인간활동 (HumanActivity)
- 금일 신규 없음. Antelope Reef 1490ac 추적 지속.

### 기후·환경 (ClimateEnvironment)
- 금일 신규 없음. El Niño는 AgricultureMaritime + ClimateEnvironment 교차 도메인.

### 농업·해양 (AgricultureMaritime)
- **El Niño**: 96% through winter, Super El Niño 1/3. SST +0.9°C Niño 3.4.

### 국방·안보 (Defense)
- **DPRK 구축함**: 6월 중순 공식 배치 확인(뉴시스), 2번함 건조 사고(Daily NK). 한반도 GeoFocus.
- Hami ICBM, Antelope Reef 추적 지속.

### 인도주의 (Humanitarian)
- 캐나다 산불 33,400+ 대피 — 교차 도메인(Disaster→Humanitarian).
- Mayon 287K+ 이재민.
- Bellingcat Lebanon 46+ towns 추적 지속.

## 온톨로지 변경

- **신규 엔티티 2건**: temp-evt-2101 (FireSat 배치), temp-evt-2102 (DPRK 구축함 종합 분석)
- **스키마 구조적 변경: 없음** — 기존 클래스·관계·Phenomenon으로 모든 이벤트 분류 가능.

## 추론 결과

- **multiSatBoost**: evt-701 (Bismarck Sea, 5위성), evt-1101 (Canada, 5위성) — 유지
- **officialBoost**: evt-202 (USGS), evt-701 (NASA), evt-082 (PHIVOLCS), evt-801 (KVERT)
- **priorityBoost**: evt-1101 (2사망, 33K+대피), evt-082 (287K+이재민), temp-evt-2001 (832K+피해)
- **koreaBoost**: temp-evt-2003 (KP), temp-evt-2102 (KP)
- **hiResBoost**: temp-evt-2003 (WV-3 0.31m)
- **temporal_progression**: temp-evt-2102 → temp-evt-2003 (같은 구축함 프로그램)
