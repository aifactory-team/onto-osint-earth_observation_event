# 2026-05-11 보고서 근거

## 포함 항목

| 소스 ID | 제목 | 태그 | 도메인 | 포함 근거 |
|---------|------|------|--------|----------|
| src-001 | Florida Everglades Max Road Fire | new | Disaster | 신규 대형 산불, GOES/VIIRS 위성 추적, 도시 인접 |
| src-002 | NASA EO Mid-Atlantic Coast 블룸 | new | AgriMarine | MODIS 공식 관측, 해양 생태계 신호 |
| src-003 | NASA EO Barents Sea 북극 해빙 | new | Climate | ICESat-2 기록적 저점, 기후변화 핵심 |
| src-004 | Ibu 화산 분출 | new | Disaster | 신규 화산, Himawari-9 관측, 인도네시아 |
| src-006 | Mayon Day 127 Strombolian | update | Disaster | 127일 연속, PHIVOLCS 공식 |
| src-007 | Kilauea Ep47 예측 5/12~15 | update | Disaster | USGS HVO 공식, 임박 분출 |
| src-008 | Great Sitkin SAR 용암류 | update | Disaster | SAR 신규 관측, USGS AVO |
| src-009 | Shishaldin SO2 TROPOMI | update | Disaster | 위성 SO2 관측, USGS AVO |
| src-010 | Georgia Pineland 70~87% | update | Disaster | Landsat 8/9, 이탄 지하화재 |
| src-011 | Caloy/Hagupit 종결 | update | Disaster | 잔여저기압 전환, 이벤트 종결 |

## 제외 항목

| 소스 ID | 제목 | 제외 근거 |
|---------|------|----------|
| src-005 | NASA EO Ahuachapán | 관측 영상 2024-11-25. 현재 이벤트가 아닌 지형 피처 기사. 본문 포함 부적합, 참고용만 출처 목록에 기재 |
| src-012~029 | 기존 추적 reported | 금일 신규 정보 없음 — 추적 항목 테이블에만 표기 |

## KG 시각화 범위
- 핵심 노드: temp-evt-501(FL 산불), temp-evt-503(북극 해빙), temp-evt-504(Ibu), ent-evt-082(Mayon), ent-evt-202(Kilauea), ent-evt-203(Great Sitkin), ent-evt-204(Shishaldin), temp-evt-001(GA 산불)
- 위성 노드: sat-goes18, sat-viirs-jpss, sat-himawari9, sat-sentinel2a, sat-landsat9, sat-sentinel1a, sat-sentinel5p, sat-icesat2
- 센서 노드: sensor-c-sar, sensor-tropomi, sensor-msi
- 기관 노드: org-nasa, ent-org-hvo, ent-org-avo, ent-org-phivolcs
- 추론 엣지: SAR구름투과(Great Sitkin), tracegasBoost(Shishaldin), multiSatBoost(Florida, Georgia, Mayon, Kilauea)

## 보고서 구성 방향
- Top 5: Florida 산불(신규), Mayon 127일(지속), Kilauea Ep47 임박, 북극 해빙 기록, Great Sitkin SAR
- 다중 위성 교차검증: 5건(Florida, Georgia, Mayon, Kilauea, Caloy)
- 한반도 GeoFocus: 금일 신규 없음. NLL 어선·CAS500-2·영변 추적만 표기
- 미검증 의혹: Fuego 화산(GT, satellite_unverified) — 이전 보도 reported
- 인간활동/국방/인도주의: "금일 신규 없음" 명시
