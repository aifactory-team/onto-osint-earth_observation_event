# 2026-05-26 보고서 기초 자료

## 포함 항목

| 소스 ID | 제목 | 태그 | 도메인 | 포함 근거 |
|---------|------|------|--------|----------|
| src-001 | 캐나다 산불 Swan Hills 에스컬레이션 | update | Disaster→Humanitarian | 인명피해+대피 확대, 5위성 교차검증, 재해 우선순위 1순위 |
| src-003 | Kilauea Ep48 예보 창 5/25-26 | update | Disaster | USGS HVO 공식 예보, 분출 임박 |
| src-004 | Bismarck Sea 부석 70km² 200km+ | update | Disaster | NASA EO 공식, 5위성 교차검증, 해상 위험 |
| src-006 | Kanlaon 폭발적 분출 5/26 | new | Disaster | 신규 폭발적 에피소드, PHIVOLCS 공식, PDC |
| src-005 | Mayon AL3 Day 140+ PDC | update | Disaster | 장기 시리즈, PDC 위험도 |
| src-007 | Bezymianny VAAC#45 FL100 | update | Disaster | VAAC 공식, 완화 추세 기록 |
| src-008 | Great Sitkin SAR 용암돔 | update | Disaster | USGS AVO 공식, SAR 모니터링 |
| src-009 | Shishaldin SO₂ | update | Disaster | USGS AVO 공식 |
| src-010 | Dukono 190회/일 | update | Disaster | VAAC Darwin 공식 |
| src-002 | Santa Rosa 87% | update | Disaster | 진압 추적 완료 임박 |
| src-011 | Kharg Island 유출 Sentinel-1/2/3 | update | HumanActivity | 3위성 교차검증, 전쟁 중 환경피해 |
| src-012 | 남중국해 Antelope+Spratly | update | Defense | CSIS AMTI 분석, WorldView-3+Planet |
| src-016 | Sentinel-1D 4위성 완성 | new | SatOps | ESA 공식, SAR 역량 구조적 강화 |

## 제외 항목

| 소스 ID | 제목 | 제외 근거 |
|---------|------|----------|
| src-013 | MizarVision 중국 AI | reported(기존), satellite_unverified(구체적 위성 출처 불명확) |
| src-014 | 북한 영변/소해 | reported(기존 추적 항목, 변동 없음) |
| src-015 | 캐나다 연기 대서양 횡단 | reported(src-001에서 교차 참조로 커버) |
| src-017 | Amazon 삼림벌채 | reported(기존 추적, 2026-02 기사) |
| src-018 | 엘니뇨 전망 | reported, satellite_unverified(위성 관측 데이터 미포함) |
| src-019 | KOMPSAT-7 영상 공개 | reported(기존 추적, 변동 없음) |

## KG 시각화 범위

오늘 보고서 KG에 포함할 노드 및 엣지:
- **Events (12):** evt-1101(Canada), evt-202(Kilauea), evt-701(Bismarck), temp-evt-1501(Kanlaon explosive), evt-082(Mayon), evt-801(Bezymianny), evt-203(Great Sitkin), evt-204(Shishaldin), evt-128(Dukono), evt-1201(Santa Rosa), ent-evt-kharg(Kharg), evt-092(Antelope)
- **Satellites (9):** GOES-18, VIIRS, Sentinel-5P, Landsat 9, Sentinel-2A, Himawari-9, MODIS, PACE, Sentinel-1A
- **Organizations (6):** USGS HVO/AVO, NASA EO, NOAA, ESA/CAMS, PHIVOLCS, VAAC
- **Countries (7):** CA, US, PG, PH, RU, ID, IR
- 총 노드 ~34개 → 도메인별 세부 그래프 분리 + 간략화된 전체 그래프

## 보고서 구성 방향

1. **재해 우선순위 규칙 적용**: 캐나다 산불(인명피해·대피·인프라) 1순위 배치
2. **다중 위성 교차검증 강조**: 3건(Canada 5위성, Bismarck 5위성, Kharg 3위성)
3. **한반도 GeoFocus**: 금일 직접 이벤트 없음 — 추적 항목 현황 기재
4. **미검증 의혹**: MizarVision(satellite_unverified), 엘니뇨(satellite_unverified) — 본문 제외, 미검증 섹션 분리
5. **Kanlaon 신규 폭발적 분출**: 기존 temp-evt-1401(VAAC/SO₂ 수준)에서 격상. 별도 이벤트로 보고
6. **Sentinel-1D 4위성 완성**: 센서·플랫폼 섹션에서 기술적 의의 기술 (좌표 없어 본문 이벤트 불포함, 부록/SatOps 처리)
