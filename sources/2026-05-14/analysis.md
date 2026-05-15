# 2026-05-14 분석

## 신규 이벤트 (3건)

### 1. Bezymianny 화산 폭발적 분출 (캄차카, 러시아)
- **분류:** dom-disaster / volcanic_eruption
- **위성:** Himawari-9 (AHI), VIIRS
- **위치:** 55.97°N, 160.59°E
- **분석:** VAAC Tokyo가 5/13 20:00Z에 advisory 발행. 화산재 FL150(4600m)까지 상승, SW 방향 25kts 이동. 캄차카 반도의 Klyuchevskoy 화산군(Bezymianny/Klyuchevskoy/Krasheninnikov)에서 동시다발 화산활동이 계속됨. Krasheninnikov(2025.8~ 분출 중)과 인접하여 cascading 가능성 있으나 별도 마그마 시스템으로 판단. KVERT 모니터링 중.
- **추론:** officialBoost +0.15 (VAAC Tokyo/KVERT)
- **신뢰도:** 0.85

### 2. Bellingcat 남레바논 IDF 철거·파괴 PlanetScope 공개
- **분류:** dom-humanitarian / infrastructure_damage
- **위성:** PlanetScope (Doves)
- **위치:** 33.12°N, 35.43°E (Qantara/Aadshit, 남레바논)
- **분석:** Bellingcat가 5/14 PlanetScope 위성영상(3/2 및 5/8)을 비교 공개. IDF "Yellow Line" 내 수십 개 마을에서 대규모 철거·파괴 확인. before/after 비교 영상 포함. 독립 분석기관의 위성 OSINT.
- **추론:** analystBoost +0.10 (Bellingcat), baCredibilityBoost +0.10 (before/after 영상)
- **민감 정보 처리:** 분쟁 지역이나 OSINT 공개 출처 — 좌표 일반화 불필요 (Bellingcat 자체가 공개)
- **신뢰도:** 0.88

### 3. Harvard TROPOMI+GOSAT 글로벌 메탄 2019-2024 증가 원인 분석
- **분류:** dom-climate / methane_plume
- **위성:** Sentinel-5P (TROPOMI) + GOSAT
- **위치:** 글로벌
- **분석:** Harvard 팀이 TROPOMI+GOSAT 융합 데이터로 2019-2024 글로벌 메탄 증가 원인 분석. 관성(momentum) 59%, 축산 +15%, 폐기물 +11%, 석유·가스 -9%, 벼 -17%. 위성 데이터 활용 글로벌 탄소 추적의 중요 이정표.
- **추론:** tracegasBoost +0.15 (TROPOMI 대기센서), officialBoost +0.15 (ESA Copernicus)
- **좌표 의무 면제:** 글로벌 스케일 연구 — admin "global"로 기록
- **신뢰도:** 0.85

## 주요 업데이트 (8건)

### Kilauea Ep47 (US) — 전조 오버플로우 개시 ★핵심
- WATCH/ORANGE 유지. 5/14 02:57 HST 남측 분출구에서 전조 오버플로우 시작. 6회 연속 20-30분 간격. 분수 분출이 5/14 중 시작될 가능성 높음. Uēkahuna 경사계 15.4μrad 인플레이션 기록.
- multiSatBoost +0.20 (Sentinel-2A + Landsat 9) · officialBoost +0.15 (USGS HVO)
- **신뢰도 업데이트:** 0.92 → 0.95

### Bismarck Sea 해저화산 (PG) — VAAC advisory #11
- 5/14 1020Z에 새 VA emission 관측. FL140 유지. 분출 1주일+ 지속 중. officialBoost +0.15.

### Mayon (PH) — Day 130
- VAAC advisory 594. 스트롬볼리안 지속. Alert Level 3 유지. multiSatBoost +0.20.

### Everglades (US) — 이탄층 화재 메커니즘
- 이탄층(peat) 지하 화재가 핵심 — 가뭄으로 수위 30-60cm 하강, 지하 연소 지속. GOES-18 + VIIRS 열점 모니터링.

### Pineland (US) — mop-up 단계
- 90%+ 진화. GFC가 mop-up 작전 단계 공식 진입. 158명 + 47자원 배치. 번밴 해제 상태.

### Great Sitkin (US) — SAR 관측 지속
- WATCH/ORANGE. 구름으로 광학 불가 — Sentinel-1A C-SAR 유일 관측. sarBoost +0.10.

### Shishaldin (US) — SO2 지속
- ADVISORY/YELLOW. 지진·인프라사운드 상승 지속. TROPOMI SO2 관측. tracegasBoost +0.15.

### Pemex 원유 유출 (MX) — 잔류 오염 업데이트
- SpillControl이 5/13 재보도. "persistent and dispersed residual contamination" — 표면 슬릭에서 잔류 오염 단계로 전이.

## 추론 결과

| 추론 규칙 | 대상 | 적용 | 신뢰도 변화 |
|----------|------|------|------------|
| multi_satellite_confirmation | evt-202 (Kilauea) | Sentinel-2A + Landsat 9 | +0.20 |
| multi_satellite_confirmation | evt-082 (Mayon) | Himawari-9 + Sentinel-2A | +0.20 |
| multi_satellite_confirmation | evt-501 (Everglades) | GOES-18 + VIIRS | +0.20 |
| multi_satellite_confirmation | temp-001 (Pineland) | VIIRS + Landsat 8 + 9 | +0.20 |
| official_source_trust | evt-202 | USGS HVO | +0.15 |
| official_source_trust | evt-801 | VAAC Tokyo/KVERT | +0.15 |
| official_source_trust | evt-701 | VAAC Darwin | +0.15 |
| sensor_capability_match_sar | evt-203 | Sentinel-1A C-SAR | +0.10 |
| sensor_capability_match_tracegas | evt-204 | TROPOMI SO2 | +0.15 |
| sensor_capability_match_tracegas | evt-803 | TROPOMI methane | +0.15 |
| before_after_credibility | evt-802 | PlanetScope 3/2 vs 5/8 | +0.10 |
| cascading_disaster | 해당 없음 | — | — |
| temporal_progression | evt-801 partOfSeries? | Krasheninnikov 인접 but 별도 화산 | 미적용 |
