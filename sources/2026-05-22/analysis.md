# 2026-05-22 분석

## 신규 소스 중요도 평가

| 소스 | 중요도 | 근거 |
|------|--------|------|
| src-001 (NASA EO Bismarck Sea) | 높음 | NASA 공식 위성 분석 + 3위성 교차검증 + before/after |
| src-002 (Sentinel-1A 데이터 유실) | 중간 | SAR 의존 모니터링 영향, 단일 날짜 데이터 공백 |

## 업데이트 소스 변경사항

| 소스 | 핵심 변경 |
|------|----------|
| src-003 (Santa Rosa) | 26% → 44% 진압, 야간 활동 현저 감소 |
| src-004 (Kilauea) | Ep48 예보 창 개시(D-day), 10.5μrad, 단기 수축 후 재팽창 |
| src-005 (Canada) | 33K+ 대피, Manitoba 비상사태, 2차 연기 대서양 진입 |
| src-006 (Bismarck VAAC) | Advisory #33, FL190 지속 |

## 도메인별 흐름 분석

- **Disaster:** 화산 활동이 지배적. Kilauea Ep48 D-day 진입이 최고 긴급. Bismarck Sea에 NASA 공식 분석 추가로 신뢰도 최고치 달성. 산불은 Santa Rosa 진압 개선, 캐나다 확대.
- **Human Activity:** 신규 없음. Kharg/Pemex/Xingu 추적 지속.
- **Climate/Environment:** Canadian smoke 2차 플룸 + 33K 대피. 기후 영향 확대 추세.
- **Agriculture/Maritime:** 신규 없음. NLL 어선 모니터링 지속.
- **Defense:** 신규 없음. 남중국해 + NK 시설 추적 지속.
- **Humanitarian:** Canadian wildfire 33K 대피로 crossDomain 진입. Bellingcat 레바논 지속.

## 온톨로지 변경 요약

- 스키마 구조 변경: 없음
- 신규 인스턴스: temp-evt-1302 (Sentinel-1A 데이터 유실)
- 기존 업데이트: ent-evt-701 (NASA officialBoost 추가), ent-evt-1201 (44% 진압), ent-evt-202 (D-day), ent-evt-1101 (33K 대피)

## 추론 결과 요약

- multiSatBoost 2건: Bismarck Sea (4위성/3기관), Canadian smoke (3위성/2기관)
- officialBoost 2건: Bismarck Sea (NASA EO), Kilauea (USGS HVO)
- tracegasBoost 1건: Canadian smoke (TROPOMI CO)
- crossDomainLink 1건: Canada wildfires → Humanitarian
- baCredibilityBoost 1건: Bismarck Sea (Landsat 9 before/after)
- priorityBoost 1건: Santa Rosa (17,554ac severity high)
