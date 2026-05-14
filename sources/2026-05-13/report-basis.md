# 2026-05-13 보고서 근거

## 포함 항목

| 소스 | 제목 | 태그 | 도메인 | 포함 근거 |
|------|------|------|--------|----------|
| src-001 | Bismarck Sea 해저 화산 분출 | new | Disaster | 1972년 이후 최초 분출, Himawari-9 위성 확인 |
| src-008 | Bismarck Sea VolcanoDiscovery 상세 | new | Disaster | src-001 보조 출처 |
| src-002 | Kilauea Ep47 WATCH/ORANGE | update | Disaster | 경보 수준 상향, 분출 임박 |
| src-003 | Mayon Day 129 | update | Disaster | 장기 분출 지속 추적 |
| src-004 | Everglades 11,339ac | update | Disaster | 이탄층 지하화재 지속 |
| src-005 | Pineland 32,575ac 90% | update | Disaster | 번밴 해제, 마무리 단계 |
| src-006 | Great Sitkin SAR | update | Disaster | SAR 전천후 관측 지속 |
| src-007 | Shishaldin SO2 | update | Disaster | TROPOMI 추적 |

## 제외 항목

| 소스 | 제목 | 제외 근거 |
|------|------|----------|
| src-009~028 | reported 항목 19건 | 금일 신규 정보 없음, 기존 추적만 유지 |
| src-012 | Fuego 화산 | satellite_unverified, 미검증 유지 |

## KG 시각화 범위
- 핵심 노드: ent-evt-701(Bismarck Sea), ent-evt-202(Kilauea), ent-evt-082(Mayon), ent-evt-501(Everglades), temp-evt-001(Pineland), ent-evt-203(Great Sitkin), ent-evt-204(Shishaldin)
- 위성 노드: sat-himawari9, sat-sentinel2a, sat-landsat9, sat-goes18, sat-viirs-jpss, sat-sentinel1a, sat-sentinel5p, sat-landsat8
- 기관 노드: org-vaac-darwin, org-hvo, org-avo
- 총 노드 ~22개 (max_kg_nodes 30 이내)

## 보고서 구성 방향
- **1순위**: Bismarck Sea 신규 해저 화산 — 54년 만의 분출
- **2순위**: Kilauea WATCH 상향 — Ep47 임박
- **강조**: 전 세계 7+ 화산 동시 위성 모니터링
- **한반도 GeoFocus**: 금일 신규 없음 (기존 추적 NLL 어선, CAS500-2, CSIS BP)
- **다중 위성 교차검증**: Kilauea(S2A+L9), Mayon(H9+S2A), Everglades(GOES+VIIRS), Pineland(VIIRS+L8+L9) — 4건
- **미검증 의혹**: Fuego 화산 (위성 미확인 지속)
