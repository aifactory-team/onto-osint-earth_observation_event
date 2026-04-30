# Report Basis — 2026-04-30 보고서 작성 근거

## 포함 항목 (19건)

| 소스 | Event ID | 도메인 | 태그 | 포함 근거 |
|------|----------|--------|------|-----------|
| src-001 | ent-evt-001 | Defense | new | WV-3 + 좌표 + 다중관측 |
| src-002 | ent-evt-001 | Defense | update | src-001 후속 |
| src-003 | ent-evt-002 | Defense | new | KP Sohae + 다중 위성 |
| src-004 | ent-evt-003 | Disaster | new | NASA + Landsat 9 TIRS + before/after |
| src-005 | ent-evt-004 | Disaster | new | USGS + CSG InSAR |
| src-006 | ent-evt-005 | HumanActivity | new | GFW/UMD 공식 |
| src-007 | ent-evt-006 | Defense | new | Sentinel-2 다중 + before/after |
| src-008 | ent-evt-007 | Humanitarian | new | Sentinel-1 SAR PWTT |
| src-009 | ent-evt-008 | Humanitarian | new | UNOSAT 공식 |
| src-010 | ent-evt-009 | Climate | new | 다중 위성 시계열 |
| src-011 | ent-evt-010 | Climate | new | Climate TRACE 정기 |
| src-012 | ent-evt-011 | Climate | new | TROPOMI+GOSAT |
| src-013 | ent-evt-012 | Disaster | new | 정지궤도 다중 + 슈퍼태풍 |
| src-014 | ent-evt-013 | Disaster | new | Cat 3 + 정지궤도 |
| src-016 | ent-evt-015 | AgriMarine | new | KOMPSAT-7 한반도 |
| src-017 | ent-evt-016 | Defense | new | Maxar GEGD cap 0.7 |
| src-018 | ent-evt-017 | Disaster | new | ICEYE SAR + 좌표 |
| src-019 | ent-evt-018 | Disaster | new | CEMS 공식 |
| src-020 | ent-evt-019 | HumanActivity | new | SkyTruth Cerulean |

## 미검증 의혹 분리

| 소스 | Event ID | 사유 |
|------|----------|------|
| src-015 | ent-evt-014 | 한반도 4/26 산불 — 보도만 인용, 위성 출처 미확인 |

## 제외 항목
없음 — 모든 포함 소스가 좌표 또는 admin level + 출처 URL 보유.

## KG 시각화 범위 (30 노드 한도)

- Events 10: 001/002/003/004/006/008/009/011/012/015
- Satellites 10: WV-3, PlanetScope, Landsat 9, Sentinel-1A, Sentinel-2A, Sentinel-5P, Himawari-9, GOES-18, ICEYE, KOMPSAT-7
- Sensors 3: TIRS, C-SAR, TROPOMI
- Organizations 4: CSIS-BP, NASA, UNOSAT, KARI
- Countries 3: KP, KR, CN

## 보고서 구성 방향

- 한반도 GeoFocus 섹션 본문 상단 (Yongbyon / Sohae / KOMPSAT-7).
- Top 5 — 다중 위성 교차검증 우선.
- before/after 보유 8건 별도 표.
- 미검증 의혹 1건 본문 분리.
- 국방·안보 섹션 좌표 일반화 (소수점 1자리, CLAUDE.md 정책).
