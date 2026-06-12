# Phase 3 분석 — 2026-06-12

## 입력 요약

- index.json: 12 items (1 new, 8 update, 3 reported)
- 4대 카테고리 커버: disaster(O), human_activity(O), climate_env(O), agriculture_ocean(O)

## 신규 이벤트 분석

### evt-3201: Mindanao M7.8 지진 위성 피해 평가 [NEW, HIGH PRIORITY]

**온톨로지 의의**: 이 파이프라인 역사상 최초의 실제 위성 검증 지진 피해 이벤트. `phen-earthquake`는 2026-04-30 스키마 초기화 시 정의되었으나 `mention_count=0`으로 한 번도 실제 이벤트에 매핑된 적이 없었다. evt-3201이 첫 번째 매핑이 된다.

**이벤트 상세**:
- 규모: M7.8 (USGS)
- 위치: 사랑가니, 민다나오, 필리핀 (5.9N, 125.3E)
- 피해: 47+ 사망, 12,600+ 가옥 손상/파괴
- 위성 관측: PhilSA VIIRS 야간 조명 데이터 (before/after)
- 국제 대응: Sentinel Asia 발동 (EQ-2026-000083-PHL)
- 신규 기관: PhilSA (Philippine Space Agency) -- 필리핀 국가 우주기관
- 신규 위치: Sarangani, Mindanao

**추론 적용**:
1. `first_event_reference`: phen-earthquake mention_count 0 -> 1 (마일스톤)
2. `official_source_trust`: PhilSA = space_agency (+0.15), Sentinel Asia = intl_body (+0.15)
3. `disaster_severity_priority`: 47+ 사망, 인프라 대규모 파괴 (+0.20)
4. `before_after_credibility`: VIIRS 야간 조명 전후 비교 (+0.10)
5. `sensor_capability_match_sar`: Sentinel-1 InSAR 후속 분석 예상 -- 아직 미수신이나 M7.8 규모로 공동변위(coseismic deformation) 분석이 표준 절차

**신뢰도 산정**: 기본 0.85 + officialBoost 0.15 + priorityBoost 0.20 + baCredibility 0.10 = 0.97 (cap)

**보고서 배치**: 1순위 -- 인명피해 동반 자연재해 최우선 규칙 적용

## 업데이트 이벤트 분석

### evt-202: Kilauea Ep49 D-Day (예보 창 6/12 개시)
- 시계열 연속: Ep44 -> Ep45 -> Ep46 -> Ep47 -> Ep48 -> Ep49
- 금일이 예보 창 시작일(D-Day). 가장 유력한 분출 시점 6/13-14.
- USGS HVO officialBoost +0.15 유지
- temporal_progression 확정 (partOfSeries)

### evt-701/evt-2903: Bismarck Sea 부석 해상 접근 차단
- Day35+ cascading chain (파이프라인 최장)
- 마누스주 해상 접근 차단 -- 인도주의 영향 격상
- 5위성 교차검증 유지 (multiSatBoost +0.20)
- cascading_disaster 규칙 지속 적용

### evt-082: Mayon Day158+ PDC 4km
- AL3 장기 분출 위기 지속
- 금일 4km PDC(화쇄류) 보고 -- 위험도 격상
- 287K 이재민 유지
- thermalBoost +0.10 (Himawari-9 AHI)
- temporal_progression 확정

### evt-2802: Typhoon Jangmi 피해 평가
- 피해 평가 완료 단계
- Tokyo 홍수 동일 기상 시스템 -- cascading_disaster 적용
- Himawari-9 + GPM multiSatBoost +0.20

### evt-1101: Canada Wildfire 65 Active
- CIFFC Level 2 유지
- 5위성 4기관 교차검증 유지
- multiSatBoost +0.20

### evt-203: Great Sitkin WATCH/ORANGE
- SAR 용암돔 성장 모니터링
- sarBoost +0.10 (Sentinel-1)

### evt-204: Shishaldin ADVISORY/YELLOW
- 75nm 수증기 플룸
- tracegasBoost +0.15 (TROPOMI SO2)

### temp-evt-1902: El Nino +0.9C 강화
- 98% 확률, 강화 추세
- 기후-환경 카테고리 의무 커버

## 보고서 제외 이벤트 (reported 태그)

- evt-3101 (러시아 전차 OSINT) -- 6/11 보고 완료
- evt-3102 (브라질 DETER 법안) -- 6/11 보고 완료
- evt-3001 (GFM v4.1.1) -- 6/11 보고 완료

## 온톨로지 변경 요약

| 변경 유형 | 대상 | 근거 |
|----------|------|------|
| first_event_reference | phen-earthquake mention_count 0->1 | evt-3201: 파이프라인 최초 위성 검증 지진 피해 |
| 새 Location | ent-loc-sarangani (5.9N, 125.3E) | Sarangani, Mindanao, PH |
| Organization 업데이트 | org-philsa (PhilSA) last_seen 갱신 | 기존 기관 업데이트 |
| co-ph last_seen 갱신 | 2026-06-12 | evt-3201 필리핀 이벤트 |
| 이벤트 업데이트 | 8건 | 후속 정보 반영 |

## 추론 통계

| 규칙 | 금일 발동 | 평균 신뢰도 |
|------|----------|-----------|
| first_event_reference | 1 | 0.99 |
| official_source_trust | 2 | 0.95 |
| disaster_severity_priority | 1 | 0.95 |
| before_after_credibility | 1 | 0.90 |
| sensor_capability_match | 3 | 0.87 |
| multi_satellite_confirmation | 2 | 0.93 |
| temporal_progression | 2 | 0.93 |
| cascading_disaster | 2 | 0.87 |
| **합계** | **14** | **0.92** |

## 한반도 GeoFocus

금일 한반도 신규 이벤트 없음. `korea_geo_focus` 규칙 미적용.
