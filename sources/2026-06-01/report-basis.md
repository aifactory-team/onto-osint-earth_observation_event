# 2026-06-01 보고서 근거

## 포함 항목

| 소스 ID | 제목 | 태그 | 도메인 | 포함 근거 |
|---------|------|------|--------|----------|
| src-001 | Kilauea Ep48 전조 오버플로우 | update | Disaster | WATCH/ORANGE 격상, 기록 에피소드 임박 |
| src-002 | 캐나다 산불 65건 | update | Disaster→Humanitarian | 33,400+ 대피, AQI 미국 악화 |
| src-003 | Bismarck Sea day 24+ | update | Disaster | 5위성 교차검증, 신규 섬 가능 |
| src-004 | 태풍 Domeng PAR 이탈 | update | Disaster | 832,986명 피해, habagat 증강 |
| src-005 | Mayon Day 146+ | update | Disaster | 287K+ 이재민, 라하르 위험 |
| src-006 | El Niño 96% | update | AgriMarine+Climate | Super El Niño 1/3, 글로벌 영향 |
| src-007 | Bezymianny Yellow 하향 | update | Disaster | 활동 감소 기록 |
| src-008 | Kanlaon AL2 | update | Disaster | SO2 변동 |
| src-009 | Great Sitkin WATCH | update | Disaster | 용암 돔 지속 |
| src-010 | Shishaldin ADVISORY | update | Disaster | SO2 지속 |
| src-011 | FireSat 배치 ★신규 | new | SatOps | 위성운영 신규 이벤트 |
| src-012 | DPRK 최현함 6월 배치 | update | Defense | GeoFocus, 배치 일정 확인 |
| src-017 | DPRK 구축함 종합 분석 ★신규 | new | Defense | 2번함 사고 상세 |

## 제외 항목

| 소스 ID | 제목 | 제외 근거 |
|---------|------|----------|
| src-013 | Antelope Reef 1490ac | reported — 전일 보고 동일 내용 |
| src-014 | Kharg Island 45km² | reported — 전일 보고 동일 내용 |
| src-015 | Bellingcat Lebanon 46+ | reported — 전일 보고 동일 내용 |
| src-016 | Hami ICBM 80+ | reported — 전일 보고 동일 내용 |
| src-018 | Dukono AL2 | reported — 전일 보고 동일 내용 |
| src-019 | Canada wildfire season outlook | reported — src-002에 흡수 |
| src-020 | Super El Niño | reported — src-006에 흡수 |

## KG 시각화 범위

오늘 보고서에 포함할 KG 노드 (20개):
- Events: evt-202, evt-1101, evt-701, temp-evt-2001, evt-082, temp-evt-1902, evt-801, temp-evt-2003, temp-evt-2101, temp-evt-2102
- Satellites: sat-sentinel2a, sat-goes18, sat-viirs-jpss, sat-himawari9, sat-landsat9, sat-worldview3
- Organizations: org-usgs, org-noaa, org-nasa, org-phivolcs

## 보고서 구성 방향

- **Top 5**: Kilauea Ep48 WATCH(가장 긴급), Canada 33K+, Bismarck Sea day24+, Mayon 287K+, 태풍 Domeng 832K
- **다중 위성 교차검증**: 4건 유지 (Bismarck Sea 5위성, Canada 5위성, Kharg Island 3위성, Hami 2위성)
- **한반도 GeoFocus**: DPRK 구축함 6월 배치 확인 + 2번함 사고 분석 + 추적 4건
- **미검증 의혹**: DPRK 서해 발사체 5/26, 일본 군사 우주 확장 지속
- **교차 도메인**: Domeng → Mayon ashfall 지역 홍수 (cascading_disaster 잠정)
