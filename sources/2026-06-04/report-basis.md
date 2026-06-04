# 2026-06-04 보고서 기초 자료

## 요약
신규 1건, 주요 업데이트 6건, 추적 지속 7건. Gaza 40+ 군사거점 Al Jazeera 위성분석(신규). TS Jangmi 일본 본토 상륙 완료 -- 23명 부상 57가옥 파괴 900편 취소 Tokyo Level 4 최초. 캐나다 산불 400+ fires, Minnesota AQ very unhealthy. Kilauea ADVISORY/YELLOW 하향 Ep49 10-15일 예보. Bismarck Sea Day 27+ 감소 추세. El Nino WMO 80% Jun-Aug. 다중 위성 교차검증 5건(신규 1건: Gaza). 한반도 GeoFocus 5건 유지.

## 포함/제외 결정

### 포함 (Include) -- 14건

| # | 이벤트 | 신뢰도 | 포함 사유 |
|---|--------|--------|----------|
| 1 | temp-evt-2001: TS Jangmi 일본 본토 상륙 | 0.90 | **1순위 배치**: 인명피해(23명 부상, 57가옥), cascading_disaster 확정, Tokyo Level 4 최초. Himawari-9 위성 확인. |
| 2 | evt-1101: 캐나다 산불 400+ fires | 0.95 | **1순위 배치**: 27,000+ 대피, AQ very unhealthy 미국 확산, 5위성 3기관 multiSat. |
| 3 | temp-evt-2401: Israel 40+ military posts Gaza | 0.95 | **신규 이벤트**: PlanetScope+WV-3 multiSat, before/after, Al Jazeera OSINT. cross-domain(Defense+Humanitarian). |
| 4 | evt-202: Kilauea ADVISORY/YELLOW | 0.90 | 시리즈 핵심 업데이트: WATCH -> ADVISORY 하향, Ep49 10-15일 예보. USGS HVO. |
| 5 | evt-701: Bismarck Sea Day 27+ | 0.95 | 시리즈 핵심 업데이트: 분출 감소, 5위성 유지. |
| 6 | temp-evt-1902: El Nino WMO 80% | 0.90 | 기후 핵심: WMO 공식 80%, 허리케인 억제 신호. |
| 7 | temp-evt-2002: Hami ICBM 80+ pads | 0.95 | 국방 핵심 업데이트: Reuters/NBC 상세 보도, C3 인프라. |
| 8 | evt-082: Mayon ongoing | 0.90 | 화산 추적. |
| 9 | evt-203: Great Sitkin WATCH | 0.88 | 화산 추적. |
| 10 | evt-204: Shishaldin ADVISORY | 0.85 | 화산 추적. |
| 11 | temp-evt-1401: Kanlaon AL2 | 0.85 | 화산 추적. |
| 12 | evt-801: Bezymianny | 0.80 | 화산 추적. |
| 13 | temp-evt-2203: Sangay/Reventador | 0.80 | 화산 추적. |
| 14 | evt-1201: Santa Rosa | 0.85 | 산불 종결 임박(97%, 6/6). |

### 제외 (Exclude) -- 0건
- 금일 신규 미검증 이벤트 없음.

### 미검증 의혹 섹션 (별도 분리) -- 1건 유지
- **DPRK 서해 발사체 5/26 (temp-evt-1702):** 위성 미검증 상태 지속. 보고서 미검증 의혹 섹션 유지.

## Top 5
1. TS Jangmi 일본 본토 -- 0.90 (인명피해 우선)
2. 캐나다 산불 400+ fires -- 0.95
3. Israel Gaza 40+ posts -- 0.95 (신규)
4. Bismarck Sea Day 27+ -- 0.95
5. El Nino WMO 80% -- 0.90

## 다중 위성 교차검증 (5건, 신규 1건)
1. Bismarck Sea -- 5위성 3기관 (VIIRS+MODIS+Landsat9+Himawari-9+Sentinel-2A)
2. 캐나다 산불 -- 5위성 3기관 (GOES-18+VIIRS+TROPOMI+OMPS+EarthCare)
3. Kharg Island -- 3위성 3센서 (Sentinel-1+Sentinel-2+Sentinel-3)
4. Hami ICBM -- 2위성 2기관 (WorldView-3+PlanetScope)
5. **Israel Gaza 40+ posts -- 2위성 2기관 (PlanetScope+WorldView-3)** (신규)

## 한반도 GeoFocus (5건 유지, 변동 없음)
1. DPRK 최현급 구축함 서해 항해 + 남포 3번째 건조
2. DPRK 구축함 2번함 Chongjin 건조 사고
3. 압록강 신교량 세관시설 건설
4. 두만강 북-러 교량 완공 임박
5. DPRK 서해 발사체 5/26 (미검증)

## 카테고리별
- 자연재해: 10건 (Jangmi, Canada, Kilauea, Bismarck Sea, Mayon, Great Sitkin, Shishaldin, Kanlaon, Bezymianny, Sangay/Reventador, Santa Rosa)
- 인간활동: 1건 (Gaza military posts -- Defense/Humanitarian cross-domain)
- 기후환경: 1건 (El Nino WMO)
- 농업해양: 0건 (금일 신규 없음 -- El Nino 교차 도메인으로 간접 커버)
- 국방안보: 2건 (Gaza military posts, Hami ICBM)
- 인도주의: 1건 (Gaza cross-domain)

## KG 시각화 범위 (Mermaid)
- 핵심 노드: temp-evt-2401(신규), temp-evt-2001, evt-1101, evt-202, evt-701, temp-evt-1902, temp-evt-2002
- 위성 노드: PlanetScope, WorldView-3, Himawari-9, GOES-18, VIIRS, TROPOMI
- 관계: observedBy, manifests, inDomain, triggeredBy, partOfSeries, multiSatBoost
- cascading_disaster 확정 화살표: temp-evt-2001 -> flooding/landslides JP

## 보고서 섹션 배치 순서
1. **재해 우선 섹션:** TS Jangmi(cascading 확정) + 캐나다 산불(400+ fires)
2. **신규 이벤트 섹션:** Gaza 40+ military posts
3. **화산 동시 추적:** Kilauea, Bismarck Sea, Mayon, + 5건 요약
4. **국방안보:** Hami ICBM 상세
5. **기후환경:** El Nino WMO 80%
6. **한반도 GeoFocus:** 5건 요약 (변동 없음)
7. **미검증 의혹:** DPRK 발사체
8. **농업해양:** 금일 신규 없음
