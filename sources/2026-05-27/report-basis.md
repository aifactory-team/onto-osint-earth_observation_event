# 2026-05-27 보고서 기초 자료

## 포함 항목

| 소스 ID | 제목 | 태그 | 도메인 | 포함 근거 |
|---------|------|------|--------|----------|
| src-003 | 캐나다 산불 지속 | update | Disaster→Humanitarian | 대피 확대, 5위성 교차검증, 재해 우선순위 1순위 |
| src-001 | Kilauea Ep48 5/27-29 window | update | Disaster | USGS HVO 공식 예보, 분출 임박, 창 확대 |
| src-004 | Bismarck Sea day19+ | update | Disaster | NASA EO 지속, 부석 확산, 항해 위험 |
| src-005 | Mayon Day141+ | update | Disaster | PHIVOLCS AL3, PDC 위험 지속 |
| src-006 | Kanlaon post-explosion | update | Disaster | 5/26 폭발 후속, PHIVOLCS AL2 |
| src-007 | Bezymianny FL100 | update | Disaster | VAAC KVERT, 완화 추세 기록 |
| src-008 | Great Sitkin SAR | update | Disaster | USGS AVO WATCH |
| src-009 | Shishaldin SO2 | update | Disaster | USGS AVO ADVISORY |
| src-010 | Dukono 190/일 | update | Disaster | VAAC Darwin |
| src-002 | Santa Rosa 97% | update | Disaster | 진압 거의 완료, 추적 종료 임박 |
| src-013 | 압록강 신교량 세관시설 건설 | new | HumanActivity | 38 North WV-3, koreaBoost, 전략적 함의 |
| src-014 | 두만강 교량 완공 임박 | new | HumanActivity | 38 North+RFA PlanetScope, koreaBoost |
| src-015 | 훙가통가 메탄 파괴 TROPOMI | new | ClimateEnvironment | Nature Communications, tracegasBoost+officialBoost |
| src-011 | Kharg Island 유출 | update | HumanActivity | Sentinel-1/2/3 3위성 교차검증 |
| src-012 | 남중국해 Antelope Reef | update | Defense | AMTI 분석, WorldView-3 |
| src-016 | Bellingcat 남레바논 | update | Humanitarian | PlanetScope before/after |

## 제외 항목

| 소스 ID | 제목 | 제외 근거 |
|---------|------|----------|
| — | 해당 없음 | 금일 수집 소스 모두 포함 기준 충족 |

## KG 시각화 범위

오늘 보고서 KG에 포함할 노드 및 엣지:
- **Events (15):** evt-1101(Canada), evt-202(Kilauea), evt-701(Bismarck), evt-082(Mayon), temp-evt-1401(Kanlaon), evt-801(Bezymianny), evt-203(Great Sitkin), evt-204(Shishaldin), evt-128(Dukono), evt-1201(Santa Rosa), temp-evt-1601(Yalu Bridge), temp-evt-1602(Tumen Bridge), temp-evt-1603(Hunga Tonga methane), ent-evt-kharg(Kharg), evt-092(Antelope)
- **Satellites (8):** GOES-18, VIIRS, Sentinel-5P, Landsat 9, Sentinel-2A, Himawari-9, WorldView-3, PlanetScope
- **Organizations (8):** USGS HVO/AVO, NASA EO, NOAA, ESA, PHIVOLCS, VAAC, 38 North, Bellingcat
- **Countries (8):** CA, US, PG, PH, RU, KP, IR, TO
- 총 노드 ~39개 → 도메인별 세부 그래프 분리 + 간략화된 전체 그래프

## 보고서 구성 방향

1. **재해 우선순위 규칙 적용**: 캐나다 산불(인명피해·대피·인프라) 1순위 배치
2. **다중 위성 교차검증 강조**: 2건 유지(Canada 5위성, Kharg 3위성)
3. **한반도 GeoFocus 복귀**: 2건 신규(압록강+두만강). 전일 0건에서 복귀. 38 North 위성영상 분석 기반 북한 인프라 이벤트. 대북 제재 회피 우려 관련 전략적 함의 기술.
4. **신규 기후 발견**: 훙가통가 메탄 파괴 메커니즘 — Nature Communications 동료 심사 논문, TROPOMI 데이터 기반. 보고서 기후·환경 섹션에 별도 항목.
5. **Kilauea Ep48 임박**: 예보 창 5/27-29. 분수분출 개시 가능성 높음. 다음 사이클 주시.
6. **Santa Rosa 97%**: 추적 종료 임박 플래그.
7. **미검증 의혹**: 금일 해당 없음 (모든 이벤트 위성 출처 확인됨)
8. **4종 카테고리 의무**: (a) 자연재해 11건, (b) 인간활동 3건, (c) 기후·환경 1건, (d) 농업·해양 0건 → 보고서에 "금일 신규 없음" 명시
