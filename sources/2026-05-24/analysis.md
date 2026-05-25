# 2026-05-24 교차 분석 (Phase 3)

## 1. 개요

금일 사이클은 **업데이트 전용(10건)** — 신규 이벤트 0건. 모든 항목이 기존 추적 이벤트의 상태 변경이다.

### 주요 변동

| 순위 | 이벤트 ID | 이벤트명 | 변동 요약 | 중요도 |
|------|-----------|---------|----------|--------|
| 1 | evt-202 | Kilauea Ep48 | 예보 5/25-26 축소, D-1 | **최고** |
| 2 | evt-1101 | Canada wildfire | 연기 유럽 도달 CAMS 확인 | **최고** |
| 3 | evt-701 | Bismarck Sea | NASA EO 공식 기사 | **높음** |
| 4 | evt-1201 | Santa Rosa | 87% 진압 (72→87%) | 중간 |
| 5 | evt-128 | Dukono | VAAC#284 190폭발/일 | 중간 |
| 6 | evt-082 | Mayon | AL3 Day139+ PDC | 중간 |
| 7 | evt-801 | Bezymianny | KVERT Orange explosive | 중간 |
| 8 | temp-evt-1401 | Kanlaon | AL2 SO2 4081t/d | 중간 |
| 9 | evt-203 | Great Sitkin | WATCH lava dome | 낮음(안정) |
| 10 | evt-204 | Shishaldin | ADVISORY SO2 | 낮음(안정) |

## 2. 출처별 중요도 평가

### src-001: Kilauea Ep48 USGS HVO
- **중요도:** 최고 (D-1 임박, 분수분출 24-48h 내)
- **공식 기관:** USGS HVO (officialBoost +0.15)
- **위성:** Landsat TIRS thermal (thermalBoost +0.10)
- **판단:** 예보 창 축소는 분출 확실성 증가 의미. 다음 사이클에서 분출 발생 시 WARNING/RED 상향 및 대규모 보도 예상.

### src-002: Santa Rosa Island Fire
- **중요도:** 중간 (87% 진압, 하향 추세)
- **위성:** Landsat 9 OLI burn scar (baCredibilityBoost +0.10)
- **판단:** 진압 거의 완료. 잔불 정리 단계. 100% 도달 시 추적 종료 예정.

### src-003: Canada Manitoba Wildfire
- **중요도:** 최고 (연기 유럽 도달, 인명피해)
- **위성:** TROPOMI + OMPS + EarthCare + GOES-18 + VIIRS (multiSatBoost +0.20)
- **기관:** CAMS/NOAA (officialBoost +0.15)
- **판단:** 대륙간 환경 영향. 5위성 3기관 교차검증은 본 파이프라인 최고 수준. 인도주의 도메인 교차 지속.

### src-004: Dukono VAAC#284
- **중요도:** 중간
- **위성:** Himawari-9 (officialBoost +0.15)
- **판단:** 190 explosions/day 높은 빈도이나 FL070 저고도. 항공 위험 제한적.

### src-005: Bismarck Sea NASA EO
- **중요도:** 높음 (NASA EO 공식 분석 기사)
- **위성:** VIIRS + MODIS + Landsat 9 + Himawari-9 + PACE (multiSatBoost +0.20, officialBoost +0.15, thermalBoost +0.10)
- **판단:** NASA EO 공식 기사 발행은 과학적 중요성 확인. 부석 200km+ 이동, 잠재적 신규 섬 형성은 희소 이벤트.

### src-006: Great Sitkin
- **중요도:** 낮음(안정)
- **위성:** Sentinel-1 SAR (sarBoost +0.10, officialBoost +0.15)
- **판단:** WATCH 경보 유지. 용암돔 성장 지속적이나 급변 없음.

### src-007: Shishaldin
- **중요도:** 낮음(안정)
- **위성:** Sentinel-5P TROPOMI (officialBoost +0.15)
- **판단:** ADVISORY 경보. SO2 배출 탐지. 에스컬레이션 모니터링.

### src-008: Mayon
- **중요도:** 중간
- **위성:** Himawari-9 (officialBoost +0.15)
- **판단:** Day 139+ 장기 분출. PDC 발생은 위험도 상승 신호이나 AL3 유지.

### src-009: Kanlaon
- **중요도:** 중간
- **위성:** Himawari-9 (officialBoost +0.15)
- **판단:** SO2 4081 t/d 최고치. AL2→AL3 상향 가능성.

### src-010: Bezymianny
- **중요도:** 중간
- **위성:** Himawari-9 (officialBoost +0.15)
- **판단:** KVERT Orange. 폭발적 분출 지속. 열적외 이상 위성 확인.

## 3. 도메인 흐름 분석

### Disaster (자연재해) — 8건
- 화산 6건: Kilauea (D-1), Dukono, Bismarck Sea, Mayon, Kanlaon, Bezymianny
- 산불 2건: Santa Rosa (87%), Canada wildfire (유럽 연기)
- **추세:** 글로벌 화산 활동 동시 다발 (6기). 산불 시즌 진행 중.

### Climate & Environment — 2건 (부분 교차)
- Bismarck Sea (해양 화산 → 환경 영향: 부석 뗏목, 해수 변색)
- Canada wildfire (연기 대륙간 이동 → 대기 환경)

### Human Activity — 0건 (금일 신규 없음)
- 기존 추적 유지: Pemex, Xingu, Antelope Reef, CSIS DPRK 등

### AgriMarine — 0건 (금일 신규 없음)
- 기존 추적 유지: NLL 어선, Mayon 작물 피해 등

**4대 카테고리 의무 커버 점검:** Human Activity 및 AgriMarine 금일 신규 없음 → 보고서에 "금일 신규 없음" 명시 필요.

## 4. 온톨로지 변경

금일 스키마 구조적 변경 **없음**. 모든 이벤트가 기존 클래스/관계에 매핑됨.
- 신규 클래스: 0건
- 신규 관계: 0건
- 신규 Phenomenon: 0건
- 신규 Location: 0건
- 신규 Country: 0건
- 신규 Satellite/Sensor: 0건
- 신규 Organization: 0건

## 5. 추론 결과 요약

총 18건 추론 발동:
- multi_satellite_confirmation: 2건 (evt-1101 5위성, evt-701 5위성)
- temporal_progression: 3건 (Kilauea, Santa Rosa, Canada)
- official_source_trust: 7건 (화산 기관 7곳)
- sensor_capability_match: 3건 (thermal x2, SAR x1)
- disaster_severity_priority: 2건 (Canada 인명, Kilauea D-1)
- before_after_credibility: 1건 (Santa Rosa burn scar)

### 미적용 추론
- korea_geo_focus: 0건 (한반도 이벤트 없음)
- cascading_disaster: 0건 (신규 재해 사슬 없음)
- analyst_org_trust: 0건 (독립 분석 없음)
- supersedes: 0건 (대체 관계 없음)
- commercial_imagery_trust: 0건 (상업 위성 분석 없음)

## 6. 내일(5/25) 주시 항목

1. **Kilauea Ep48 분출 여부** — D-day. 예보 5/25-26. WARNING/RED 상향 가능.
2. **Canada wildfire 연기 유럽 영향** — 대기질 악화 보고 가능.
3. **Kanlaon AL2→AL3 상향 여부** — SO2 4081t/d 최고치.
4. **Bismarck Sea 부석 뗏목 이동** — 선박 항로 영향 + 신규 섬 형성 모니터링.
5. **Santa Rosa 100% 진압 여부** — 87%→100% 달성 시 추적 종료.
