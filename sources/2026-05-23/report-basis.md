# 2026-05-23 보고서 근거

## 포함 항목

| 소스 | 제목 | 태그 | 도메인 | 포함 근거 | 신뢰도 |
|------|------|------|--------|----------|--------|
| src-003 | 캐나다 산불 2명 사망 33,400+ 대피 | update | Disaster -> Humanitarian | 첫 민간인 사망, 대규모 대피 확대, Garden Hill FN 군 투입. 재해 우선순위 규칙에 따라 1순위. multiSatBoost(GOES+VIIRS+TROPOMI). | 0.97 (cap) |
| src-001 | Kilauea Ep48 예보 5/24-27 | update | Disaster | 분출 임박 D-day(5/24). 예보 창 5/22-26 -> 5/24-27 이동. tilt 11.4urad 가속. officialBoost(USGS HVO). | 0.95 |
| src-002 | Santa Rosa Island 72% contained | update | Disaster | 진압률 59% -> 72% mop-up phase. Torrey Pines 보존 확인. | 0.95 |
| src-004 | Canlaon VAAC #161 FL090 | new | Disaster | 필리핀 화산 신규 VAAC advisory. Himawari-9 AHI 관측. 2024-2026 시퀀스. | 0.82 |
| src-005 | Bezymianny VAAC #42 23,000ft | update | Disaster | VAAC advisory 시리즈 지속. 23,000ft E. thermalBoost(Himawari-9). | 0.93 |
| src-008 | Mayon Day138+ 91,225명 | update | Disaster | 138일 연속 분출. 91,225명 영향. multiSatBoost(Himawari+S2A). | 0.95 |
| src-006 | Sentinel-2A 연장 2026말 | new | SatOps | ESA 공식 -- EO 데이터 연속성 확보. **좌표 없음 -- satops sidebar note로 처리, 메인 이벤트 아님.** | 0.95 |

## 제외 항목

| 소스 | 제목 | 제외 근거 |
|------|------|----------|
| src-007~src-030 | 기보고 항목 23건 | 이전 보고서에서 이미 보고됨 (reported 태그). 금일 significant update 없음. |
| src-028 | MizarVision 위성 분석 | satellite_unverified flag 유지. reported 태그. 미검증 의혹 섹션 해당이나 기보고로 제외. |

## KG 시각화 범위

- 금일 보고서 KG: 재해 + 업데이트 이벤트 중심
  - **중심 노드:** Canada wildfire(evt-1101), Kilauea(evt-202), Santa Rosa(evt-1201)
  - **신규 노드:** Canlaon(temp-evt-1401)
  - **위성/센서:** GOES-18, VIIRS, TROPOMI, Himawari-9, Landsat 9, Sentinel-2A
  - **관계:** observedBy, multiSatBoost, partOfSeries, crossDomainLink
- 노드 약 15-18개: 적정 -- 단일 전체 그래프
- Bezymianny, Mayon은 보조 노드(연결 간선 표시)

## 보고서 구성 방향

1. **캐나다 산불** -- 인명피해(2명 사망) + 33,400+ 대피 + 군 투입으로 1순위 (재해 우선순위 규칙: 인명피해-인프라파괴 동반 시 1순위 배치)
2. **Kilauea Ep48** -- 분출 임박 D-day(5/24). tilt 가속(11.4urad). 위성 관측 집중 예상.
3. **Santa Rosa** -- 72% mop-up phase. 급격한 진압률 개선.
4. **Canlaon** -- 신규 VAAC #161. 필리핀 2개 화산 동시 활동(Mayon + Canlaon).
5. **Bezymianny** -- VAAC#42 23,000ft. 항공 위험 안정적.
6. **Mayon** -- Day138+ 91,225명 영향. 스트롬볼리안 지속.
7. **Sentinel-2A 연장** -- satops sidebar (EO 데이터 연속성 보장)

## 한반도 GeoFocus

- 금일 한반도 직접 이벤트: **0건**
- 기존 추적 항목 (reported, 본문 미포함):
  - KOMPSAT-7 커미셔닝 진행 중 (7월 정식운용 예정)
  - NLL 어선 활동 추적 유지
  - CSIS Beyond Parallel NK 시설 모니터링 유지
- 보고서 내 "금일 한반도 GeoFocus 신규 이벤트 특이사항 없음" 명시

## 미검증 의혹 (Unverified)

- src-028 (MizarVision) -- satellite_unverified flag. 기보고(reported) 상태 유지. 금일 추가 검증 정보 없음.
- Fuego GT -- satellite_unverified 지속(INSIVUMEH 지상 관측만). 기보고.

## 신뢰도 요약

| 이벤트 | 최종 신뢰도 | 가산 요인 |
|--------|-----------|----------|
| Canada wildfire (evt-1101) | 0.97 (cap) | multiSat+0.20, tracegas+0.15, official+0.15, priority+0.20 |
| Kilauea Ep48 (evt-202) | 0.95 | official+0.15, partOfSeries |
| Santa Rosa (evt-1201) | 0.95 | official+0.15, ba+0.10, priority+0.20 |
| Mayon Day138+ (evt-082) | 0.95 | multiSat+0.20, partOfSeries |
| Bezymianny (evt-801) | 0.93 | thermal+0.10, official+0.15 |
| Canlaon (temp-evt-1401) | 0.82 | Himawari-9 단독, 가산 없음 |
| Sentinel-2A ext | 0.95 | ESA 공식 (좌표 없음, satops) |
