# 2026-05-08 보고서 작성 근거 (Phase 4)

## 1. 보고서 포함 11건 (final confidence >= 0.7)

### 자연재해 (Disaster) — 7건 [보고서 1순위 섹션]
| Rank | Event ID | 이벤트명 | 위성/센서 | 지역 | Final Conf |
|------|----------|----------|----------|------|-----------|
| 1 | ent-evt-128 update | Dukono 화산 3명 사망 — ash 10km (severity HIGH) | Himawari-9 | Halmahera, ID | **0.97** |
| 2 | ent-evt-082 update | Mayon danger zone 8km — PDC + **lahar 위험 (Hagupit)** | Himawari-9 + Sentinel-2A (multi) | Albay, PH | **0.97** |
| 3 | ent-evt-127 update | TS Hagupit/Caloy PAR entry May 9 예상 | Himawari-9 + GOES-18 (multi) | W Pacific → PH | **0.97** |
| 4 | temp-evt-001 update | GA Pineland burn scar — CIRA before/after, 85% contained | S-NPP + Landsat 8/9 (3-sat multi) | Georgia, US | **0.97** |
| 5 | ent-evt-203 | Great Sitkin WATCH/ORANGE — lava dome growth | VIIRS (thermal) | Aleutian AK, US | **0.97** |
| 6 | ent-evt-202 | Kilauea Ep47 예보 May 12-17 (ADVISORY/YELLOW) | (USGS HVO in-situ, 위성 미관측) | Halemaʻumaʻu, US | **0.95** |
| 7 | ent-evt-204 | Shishaldin unrest ADVISORY/YELLOW — SO2 + seismicity | Sentinel-5P TROPOMI | Aleutian AK, US | **0.95** |

### 인간활동 (HumanActivity) — 1건
| Rank | Event ID | 이벤트명 | 위성/센서 | 지역 | Final Conf |
|------|----------|----------|----------|------|-----------|
| 8 | ent-evt-205 | Amazon Xingu gold mining 496k ha deforestation | PlanetScope + Sentinel-2A (multi) | Xingu, BR | **0.97** |

### 기후·환경 / SatOps — 1건
| Rank | Event ID | 이벤트명 | 위성/센서 | 지역 | Final Conf |
|------|----------|----------|----------|------|-----------|
| 9 | ent-evt-201 | Sentinel-2A/2C 데이터 장애 — NorthC datacenter fire | Sentinel-2A/2C (자체) | Almere, NL | **0.97** |

### 국방·안보 — 2건
| Rank | Event ID | 이벤트명 | 위성/센서 | 지역 | Final Conf |
|------|----------|----------|----------|------|-----------|
| 10 | ent-evt-126 update | Iran-US bases 228+ structures — Copernicus+Planet 교차검증 | Sentinel-2A + PlanetScope (multi) | Iran/Kuwait | **0.92** |
| 11 | ent-evt-206 | Balikatan 2026 + PLA Liaoning 14 vessels | PlanetScope | SCS | 0.75 |

## 2. 미포함 / 분리 — 0건

금일 사이클에서 confidence 0.7 미만 이벤트 없음. ent-evt-206은 0.75로 최저이나 포함 기준 충족.

## 3. 미검증 의혹 (carry from prior)

| Event ID | 이벤트명 | 상태 |
|----------|---------|------|
| ent-evt-090 | DPRK 조선중앙TV 산불 보도 | 위성 미검증 유지 — 금일 추가 정보 없음, carry |
| ent-evt-080 | 일본 Sanriku M7.7 | 위성 피해평가 미실시 — carry |

## 4. 한반도 GeoFocus — 금일 신규 없음

금일 한반도/DMZ/동해/남해 관련 위성 관측 이벤트 특이사항 없음. 보고서에 명시.

## 5. 보고서 구성 권고

### 제1섹션: 재해 경보 (최상위)
1. **Dukono 화산 인명피해** (3명 사망) — 인명피해 이벤트 최우선
2. **Mayon-Hagupit 연쇄 재해 경고 박스** — lahar 위험 잠정 추론 (cascading_disaster)
3. TS Hagupit/Caloy PAR entry
4. GA Pineland 산불 burn scar update

### 제2섹션: 화산 다발 현황
5. Great Sitkin WATCH/ORANGE
6. Kilauea Ep47 예보
7. Shishaldin SO2

### 제3섹션: 환경·인간활동
8. Amazon Xingu 496k ha gold mining
9. Sentinel-2 데이터 장애

### 제4섹션: 국방
10. Iran-US bases 교차검증
11. Balikatan + PLA Liaoning

### 부록
- 한반도 GeoFocus: "금일 신규 없음"
- 농업·해양: "금일 신규 없음"
- 미검증 의혹: carry 2건

## 6. Mermaid KG 시각화 권고 노드

```
ent-evt-127(Hagupit) --potentialTriggeredBy--> ent-evt-082(Mayon lahar)
ent-evt-082 --partOfSeries--> ent-evt-029(Mayon original)
ent-evt-202(Kilauea Ep47) --partOfSeries--> ent-evt-101(Ep46)
ent-evt-203(Great Sitkin) --partOfSeries--> ent-evt-050
ent-evt-128(Dukono) --partOfSeries--> ent-evt-128(May 7)
temp-evt-001(GA fires) --partOfSeries--> ent-evt-098
ent-evt-205(Xingu) --multiSat--> sat-planetscope + sat-sentinel2a
ent-evt-201(S2 장애) --observedBy--> sat-sentinel2c (NEW)
```

## 7. 전일 대비 변화 요약

| 항목 | 05-07 | 05-08 | 변화 |
|------|-------|-------|------|
| 신규 이벤트 | 26 | 6 | 감소 (업데이트 중심) |
| 다중 위성 교차검증 | 10 | 5 | 감소 |
| 한반도 GeoFocus | 5 | 0 | **없음** |
| 인명피해 이벤트 | 0 | 1 (Dukono 3명) | 신규 |
| cascading_disaster | 0 | 1 (잠정) | **Mayon-Hagupit** |
| 활성 화산 수 | 3 | 5 | 증가 |
| 신규 위성 | 3 | 1 (S2C) | — |
| 신규 기관 | 6 | 10 | 증가 |
