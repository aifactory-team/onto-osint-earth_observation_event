# 2026-06-02 보고서 근거

## 포함 항목

| 소스 | 제목 | 태그 | 도메인 | 포함 근거 |
|------|------|------|--------|----------|
| src-001/002 | Kilauea Ep48 분수분출 개시 | update | Disaster | 기록적 48번째 에피소드 공식 시작. 최대 200m 분수. 공식 USGS 출처. |
| src-003/004/013 | 태풍 Jangmi 오키나와 접근 | update | Disaster | 필리핀→일본 진행. 400+ 항공편 취소. JMA 긴급경보. 인명 위험. |
| src-005/006 | El Niño Super El Niño 에스컬레이션 | update+new | Climate | CPC '가장 유력' 상향. ECMWF 100%. 역사적 수치. 첫 대기 응답 감지. |
| src-007 | 캐나다 산불 65건 | update | Disaster→Humanitarian | 33,400+ 대피 지속. 미국 AQI 영향. 6-8월 위험 예보. |
| src-008 | Bismarck Sea 해저 화산 | update | Disaster | Day 25+. 부석 70km². NASA PACE. 5위성 교차검증 유지. |
| src-009 | Mayon Day 147+ | update | Disaster | 287,000+ 이재민. 우기 라하르 위험. |
| src-010 | Great Sitkin WATCH | update | Disaster | 용암 돔 valley 진입. 2021 이후 지속. |
| src-011 | Shishaldin ADVISORY | update | Disaster | SO2 확산 위성 확인. |
| src-012 | Gaza 위성 피해 197,000건 | new | Humanitarian | UNOSAT Sentinel-1. 80% 파괴. before/after 가용. |
| src-021 | Sangay/Reventador 화산 | new | Disaster | 에콰도르 화산 지속. 위성 ash. 신규 이벤트. |
| src-022 | Kanlaon AL2 | update | Disaster | 분출 활동 지속. |

## 제외 항목

| 소스 | 제목 | 제외 근거 |
|------|------|----------|
| src-014 | DPRK 구축함 | reported — 전일 보도 동일 |
| src-015 | Antelope Reef | reported — 기존 보도 |
| src-016 | Kharg Island | reported — 기존 보도 |
| src-017 | Bellingcat Lebanon | reported — 기존 보도 |
| src-018 | Hami ICBM | reported — 기존 보도 |
| src-019 | FireSat | reported — 기존 보도 |
| src-020 | Spratly construction | reported — 기존 보도 |

## KG 시각화 범위

핵심 이벤트 노드: evt-202(Kilauea), temp-evt-2001(Jangmi), temp-evt-1902(El Niño), evt-1101(Canada), evt-701(Bismarck), evt-082(Mayon), temp-evt-2201(Gaza), temp-evt-2203(Ecuador)
위성 노드: Sentinel-2A, Landsat 9, Himawari-9, GOES-18, VIIRS, TROPOMI, Sentinel-1A
기관 노드: USGS HVO, NOAA, JMA, UNOSAT, PHIVOLCS
총 약 25개 노드 — 단일 전체 그래프 + 도메인별 세부.

## 보고서 구성 방향

1. **Top 1:** Kilauea Ep48 본격 분수분출 (200m, record)
2. **Top 2:** 태풍 Jangmi 오키나와 접근 (400+ 항공편, 162km/h)
3. **Top 3:** El Niño Super — CPC '가장 유력', ECMWF 100%
4. **Top 4:** Bismarck Sea day 25+ 부석 70km² (5위성 교차)
5. **Top 5:** 캐나다 산불 65건 (5위성 교차, 33,400+)
6. 한반도 GeoFocus: 추적 지속 5건 (변동 없음)
7. 다중 위성 교차검증: 4건 유지
8. 인도주의: Gaza UNOSAT 피해 신규
9. 미검증: temp-evt-2004(일본 군사 우주), DPRK 발사체 5/26
