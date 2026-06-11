# 2026-06-11 보고서 근거

## 포함 항목

| 소스 | 제목 | 태그 | 도메인 | 포함 근거 |
|------|------|------|--------|----------|
| src-001 | Russia Tank Reserve Depletion — Jompy 9개 기지 OSINT | new | Defense | 상업 위성 OSINT로 전략 자산 추적. 2,088 tanks / ~851 usable. T-80 12개월 소진. hiResBoost +0.15, analystBoost +0.10. |
| src-002 | Brazil DETER Satellite Ban Bill | new | HumanActivity | EO 모니터링 자체를 입법으로 무력화. evt-3003과 직접 모순. 위성 관측 메타-이벤트. |
| src-003 | GFM v4.1.1 Sentinel-1D Integration (TODAY rollout) | new/update | SatOps | CEMS 공식. 금일 S-1D 통합 롤아웃. Sentinel-1 풀 콘스텔레이션(A/C/D) GFM 가용. |
| src-004 | Kilauea Ep49 D-1 | update | Disaster | 재해 1순위. D-1. 6/12-15 예보, 6/13-14 최유력. USGS HVO 공식. |
| src-005 | Bismarck Sea 부석 69km2 역대 최대 | update | Disaster | 34일째 cascading. 5위성 교차검증. 정량화 완료. |
| src-006 | Canada wildfires 65건 18,935ha CIFFC L2 | update | Disaster | CIFFC Level 2 동원. BC 최고위험 지속. 4+ 위성 교차검증. |
| src-007 | Mayon AL3 Day157+ 287K displaced | update | Disaster | 장기 분출 위기 지속. 이재민 역대. |
| src-008 | Great Sitkin WATCH/ORANGE 6/6 lava flow | update | Disaster | SAR 위성 확인 용암류 전진. |
| src-009 | Shishaldin ADVISORY/YELLOW 75nm plume | update | Disaster | TROPOMI SO2 검출 지속. |
| src-010 | El Nino +0.9C 98% probability | update | Climate | Super El Nino 추적 강화. |
| src-011 | Arctic sea ice record low 11.439M km2 | update | Climate | 기록적 최저. 위성 기반 관측. |
| src-012 | Amazon deforestation lowest since 2014 | update | ClimateEnv | DETER 법안(src-002)과 교차 분석 강조. |
| src-013 | Antelope Reef 1,490 acres | update | Defense | SCS 최대 인공섬 가능성. 추적 지속. |

## 제외 항목

| 소스 | 제목 | 제외 근거 |
|------|------|----------|
| Vietnam Spratly 27 sites (evt-2901) | reported | 6/9 보도 완료. 금일 신규 정보 없음. |
| NK Mirim parade prep (evt-2801) | reported | 6/8 보도 완료. 금일 신규 정보 없음. |
| Xi DPRK visit concluded (evt-2902) | reported | 6/9 보도 완료. 금일 신규 정보 없음. |
| Artemis II moonlit Earth | excluded | 우주 관측 이벤트이지 지표면 EO 이벤트가 아님. scope.exclude 적용. |

## KG 시각화 범위

### 금일 주요 노드 (15건 이내)
- Events: temp-evt-3101(러시아 전차), temp-evt-3102(DETER 법안), temp-evt-3103(GFM v4.1.1 TODAY), evt-202(Kilauea D-1), evt-701/2903(Bismarck 69km2), evt-1101(캐나다), evt-082(Mayon), temp-evt-1902(El Nino), evt-203(Great Sitkin), evt-204(Shishaldin)
- Satellites: Sentinel-1A/C/D, WorldView-3, PlanetScope, Sentinel-2, Landsat-8/9, MODIS, VIIRS, Himawari-9, Sentinel-5P
- Organizations: USGS HVO, CEMS, Jompy, Mongabay, NOAA, INPE
- Countries: RU, BR, US, PG, CA, PH, INTL

### 금일 신규 관계 하이라이트
1. temp-evt-3101 --observedBy--> WorldView-3/PlanetScope (러시아 전차 OSINT)
2. temp-evt-3102 --manifests--> phen-defor + policy_impact_on_eo (DETER 금지)
3. temp-evt-3103 --partOfSeries--> temp-evt-2504 (S-1 재구성 시리즈)
4. evt-701 --cascading--> 69km2 largest ever pumice raft
5. temp-evt-3102 <--contradicts--> evt-3003 (DETER 금지 vs 삼림벌채 최저)

## 보고서 구성 방향

1. **재해 1순위**: Kilauea Ep49 **D-1** — 내일 분출 가능(6/12-15, 최유력 6/13-14). 비스마르크해 부석 69km2 역대 최대. Mayon 287K 이재민 Day157+.
2. **재해 2순위**: 캐나다 산불 CIFFC L2(65건), Great Sitkin 용암류 전진, Shishaldin 75nm 기둥.
3. **국방·안보**: 러시아 전차 예비 고갈 OSINT(9개 기지, T-80 12개월 소진). Antelope Reef 추적.
4. **인간활동**: 브라질 DETER 위성 금지 법안 — EO 메타-이벤트. 아마존 삼림벌채 최저와의 역설.
5. **기후·환경**: Super El Nino 98%. Arctic sea ice 기록 최저. 아마존 삼림벌채 추적.
6. **SatOps**: GFM v4.1.1 금일 S-1D 통합 — Sentinel-1 풀 콘스텔레이션 GFM 가용.
7. **농업·해양**: 금일 신규 없음 (보고서에 명시).
8. **미검증 의혹**: 러시아 전차(temp-evt-3101) — 위성 ID 추정이지 확인 아님. confidence 0.80.
9. **다중 위성 교차검증**: 3건 유지 (evt-1101 5위성, evt-701 5위성, temp-evt-3101 2+위성 추정)
10. **센서별 묶음**: SAR(S-1D GFM/Great Sitkin), 열적외(Mayon), 초분광(Shishaldin SO2), 고해상도 광학(러시아 전차)
