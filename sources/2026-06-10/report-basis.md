# 2026-06-10 보고서 근거

## 포함 항목

| 소스 | 제목 | 태그 | 도메인 | 포함 근거 |
|------|------|------|--------|----------|
| src-001 | Kilauea Ep49 예보 6/12-15, 최유력 6/13-14 | update | Disaster | 3일 후 분출 가능. 재해 우선순위 1순위. |
| src-002 | 비스마르크해 부석 마누스섬 3x5km 피해 확대 | update | Disaster | 33일째 cascading. 신규 섬 형성 가능성. |
| src-003 | 캐나다 산불 142건 BC 최고 위험 | update | Disaster | 5위성 교차검증. 시즌 피크 접근. |
| src-004 | Mayon AL3 Day156+ VAAC FL090 | update | Disaster | 6/9 신규 VAAC 통보. 우기 라하르 위험. |
| src-005 | 전세계 화산활동 주간 요약 | update | Disaster | 추적 중 다수 화산 포함. |
| src-006 | Great Sitkin WATCH/ORANGE | update | Disaster | SAR 모니터링 용암돔 지속. |
| src-007 | Shishaldin ADVISORY SO₂ TROPOMI | update | Disaster | 6/9 신규 AVO 통보. |
| src-008 | 베트남 스프래틀리 27사이트 | update | Defense | 추적 지속. |
| src-009 | 시진핑 방북 종결 후속 | update | HumanActivity | 방북 종결 후속 반응. |
| src-010 | Sentinel-1C Day2 중단 | update | SatOps | S-1C 중단 기간. SAR 과도기. |
| src-011 | GFM v4.1.1 Sentinel-1D 통합 | new | SatOps | CEMS 공식. S-1D 데이터 6/11 통합. temp-evt-2504 연계. |
| src-013 | 아마존 삼림벌채 역대 최저 | new | ClimateEnv | INPE 공식. 삼림벌채↓ vs 황폐화↑ 이중 발견. |
| src-014 | GFW 글로벌 식생 교란 경보 | new | ClimateEnv | 3기관 교차검증. 모니터링 범위 확대. |
| src-015 | Super El Niño +0.9°C 3출처 | update | Climate | IRI+Weather.com 추가 확인. |
| src-016 | Antelope Reef 1,490에이커 | update | Defense | 추적 지속. |
| src-017 | 미림비행장 퍼레이드 준비 | update | Defense | koreaBoost. 추적 지속. |
| src-018 | Kanlaon AL2 7회 분출 | update | Disaster | 추적 지속. |
| src-019 | Dukono AL2 화산재 | update | Disaster | 추적 지속. |

## 제외 항목

| 소스 | 제목 | 제외 근거 |
|------|------|----------|
| src-012 | Vantor Pulse 함대 확장 | PR cap 0.70. 상업 위성 확장 발표. 위성영상 관측 이벤트 아닌 인프라 뉴스. SatOps 섹션에서 1줄 언급만. |
| src-020 | 카르그섬 유출 (기보도) | reported — 신규 정보 없음. |
| src-021 | 북한 모내기 (기보도) | reported — 신규 정보 없음. |
| src-022 | 하미 핵 사일로 (기보도) | reported — 6/7 이후 신규 없음. |

## KG 시각화 범위

### 금일 주요 노드 (15건 이내)
- Events: evt-202(Kilauea), evt-701/2903(Bismarck Sea), evt-1101(캐나다 산불), evt-082(Mayon), temp-evt-1902(El Niño), temp-evt-2504(S-1C), evt-3001(GFM), evt-3003(아마존), evt-3004(GFW), evt-2801(미림)
- Satellites: Sentinel-1D, Sentinel-2, Landsat-9, VIIRS, MODIS, Himawari-9, GOES-18, Sentinel-5P
- Organizations: USGS, CEMS, INPE, GFW, NASA FIRMS
- Countries: US, PG, CA, PH, BR, KP

## 보고서 구성 방향

1. **재해 1순위**: Kilauea Ep49 6/13-14 분출 가능(3일 후), 비스마르크해 부석 피해 확대(3x5km), 캐나다 산불 142건
2. **기후·환경**: Super El Niño +0.9°C 확정 임박, 아마존 삼림벌채 역대 최저(+황폐화 역설), GFW 식생 경보 확대
3. **SatOps**: S-1C Day2 + GFM v4.1.1 S-1D 통합(6/11) — SAR 과도기 연쇄 보도
4. **한반도 GeoFocus**: 미림 퍼레이드 준비(시진핑 방북 종결 후속)
5. **국방·안보**: 베트남 스프래틀리/Antelope Reef 추적, 미림 퍼레이드
6. **미검증 의혹**: 해당 없음 (모든 이벤트가 위성 출처 확인됨)
7. **다중 위성 교차검증**: 5건 (evt-1101 5위성, evt-701 5위성, ent-evt-kharg 3위성, evt-3003 2위성, evt-3004 3기관)
8. **센서별 묶음**: SAR(S-1C/D/GFM), 열적외(Mayon/FIRMS), 초분광(Shishaldin SO₂), 다분광(아마존 NDVI/GFW)
