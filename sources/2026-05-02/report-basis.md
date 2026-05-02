# 2026-05-02 보고서 근거

## 포함 항목

| 소스 ID | 제목 | 태그 | 도메인 | 포함 근거 |
|---------|------|------|--------|----------|
| src-001 | PNG 바이닝산맥 산사태 (TC Maila, Landsat 9) | new | Disaster | 인명피해 25명, Disaster Charter 발동, Landsat 9 전후비교 |
| src-004 | 조지아 산불 (NASA EO Landsat 8) | update | Disaster | 120+ 가옥 파괴, 50,000+ acres, 위성영상 상세 확인 |
| src-006 | Kilauea Ep.46 예측 (USGS HVO) | update | Disaster | USGS 공식, Episode 46 예측창 신규정보 |
| src-007 | 전 세계 활화산 종합 (Sabancaya/Fuego/Merapi) | new | Disaster | 3개 화산 위성 열이상/화산재 관측 |
| src-008 | CAS500-2/4 발사 확정 (May 3) | update | AgriMarine | 한반도 관측 위성 발사 확정, GeoFocus |
| src-011 | 남극 30년 접지선 후퇴 (ESA Sentinel-1) | new | Climate | 12,800km² 빙하 손실, SAR 교차검증 |
| src-013 | 상업 위성 군사 전략 변화 (Glass Battlefield) | new | Defense | Planet+Maxar 다중위성 참조, MizarVision 후속 |
| src-015 | Niscemi 산사태 VHR 전후비교 | new | Disaster | VHR 위성영상 전후비교, 1,500명 대피 |
| src-016 | NASA 다중위성 조기 산림벌채 탐지 | new | HumanActivity | 3개 위성 결합 기술 혁신 |
| src-018 | ESA Sentinel 3종 메탄 매핑 | new | Climate | 다중위성 tiered 메탄 탐지 |
| src-023 | Mayon 화산 업데이트 (PHIVOLCS) | update | Disaster | 공식 기관 상태보고 |
| src-024 | Sheveluch 화산 업데이트 (KVERT) | update | Disaster | 위성 열이상 관측 |

## 제외 항목

| 소스 ID | 제목 | 제외 근거 |
|---------|------|----------|
| src-002 | TC Maila 관련 The Watchers 기사 | src-001과 중복 (reported) |
| src-003 | Disaster Charter PNG | src-001에 Disaster Charter 정보 포함됨 |
| src-005 | Wikipedia Georgia wildfires | src-004 대표 출처에 포함 |
| src-009~010 | CAS500 중복 보도 | src-008 대표 |
| src-012 | UC Irvine 남극 연구 | src-011에 포함 |
| src-014 | MizarVision 중복 | src-013에 포함 |
| src-017~022 | 기존 보도 중복 | reported 태그 |
| src-019~020 | UNOSAT/메탄 중복 | 기존 보도 |
| src-025 | Sohae 중복 | 2026-04-30 기보도 |

## KG 시각화 범위
- **포함 노드 (25개):** ent-evt-037, 038, 039, 040, 041, 042, 043, 044, 045, 046, ent-evt-020(u), 021(u), 029(u), 030(u), 032(u), sat-landsat9, sat-sentinel1a, sat-sentinel5p, sat-sentinel2a, sat-worldview3, sat-planetscope, org-nasa, org-esa, org-charter, phen-landslide
- **전체 그래프:** 노드 15~30 범위 → 전체 + 도메인별 세부 적합

## 보고서 구성 방향
1. **Top 5:** PNG 산사태(Landsat 9), 남극 접지선(Sentinel-1), 조지아 산불(Landsat 8), Niscemi 산사태(VHR), ESA 메탄 매핑(Sentinel 3종)
2. **다중 위성 교차검증:** ent-evt-042(Sentinel-1 A/C), ent-evt-045(Landsat 9+Sentinel-2+MODIS), ent-evt-046(Sentinel-5P+2A+3), ent-evt-043(Planet+Maxar)
3. **한반도 GeoFocus:** CAS500-2/4 발사 확정(D-1), KOMPSAT 관측 현황 기존 추적
4. **미검증 의혹:** 금일 해당 없음 (모든 신규 이벤트에 위성 출처 확인됨)
5. **전후 비교:** PNG 산사태, Niscemi 산사태, 남극 접지선
