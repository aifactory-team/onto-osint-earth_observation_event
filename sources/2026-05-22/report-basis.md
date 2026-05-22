# 2026-05-22 보고서 근거

## 포함 항목

| 소스 | 제목 | 태그 | 도메인 | 포함 근거 |
|------|------|------|--------|----------|
| src-001 | NASA EO Bismarck Sea | new | Disaster | NASA 공식 3위성 분석, 최고 신뢰도 0.97 |
| src-002 | Sentinel-1A 데이터 유실 | new | SatOps | SAR 모니터링 영향 — 센서·플랫폼 묶음 섹션 |
| src-003 | Santa Rosa 44% | update | Disaster | 유의미한 진압 진전 |
| src-004 | Kilauea Ep48 D-day | update | Disaster | 예보 창 개시 — 긴급 |
| src-005 | Canada 33K 대피 | update | Disaster→Humanitarian | 규모 확대, 인도주의 전환 |
| src-006 | Bismarck VAAC #33 | update | Disaster | 화산재 방출 지속 |

## 제외 항목

| 소스 | 제외 근거 |
|------|----------|
| src-007~029 (reported) | 전일 보고 동일 내용, 유의미한 변동 없음 |

## KG 시각화 범위

- 핵심 노드: ent-evt-701 (Bismarck Sea), ent-evt-202 (Kilauea), ent-evt-1201 (Santa Rosa), ent-evt-1101 (Canada)
- 위성 노드: Landsat 9, MODIS, VIIRS, Himawari-9, GOES-18, TROPOMI, Sentinel-2A
- 기관 노드: NASA, USGS, NOAA, CAMS
- 현상 노드: volcanic_eruption, wildfire, air_pollution
- 추론 엣지: multiSatBoost x2, officialBoost x2, crossDomainLink x1

## 보고서 구성 방향

- **Top 5:** Kilauea D-day(긴급) > Bismarck Sea NASA EO(신뢰도 최고) > Canada 33K(규모) > Santa Rosa 44%(진전) > Mayon Day137(지속)
- **다중 위성 교차검증:** Bismarck Sea (4위성/3기관), Canada smoke (3위성/2기관)
- **한반도 GeoFocus:** 직접 신규 없음. KOMPSAT-7/NLL/CSIS BP 추적 유지.
- **미검증 의혹:** MizarVision (변동 없음)
- **전후 비교:** Bismarck Sea (NASA EO Landsat 9), Santa Rosa (Landsat 9 SWIR)
