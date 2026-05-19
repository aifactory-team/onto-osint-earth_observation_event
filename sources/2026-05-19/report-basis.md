# 2026-05-19 보고서 작성 근거

## 오늘의 핵심 이벤트 (신뢰도 순)

1. **캐나다 Manitoba/Ontario 대형 산불** — conf 0.92 + multiSatBoost + tracegasBoost + officialBoost → 최종 1.0 (cap)
   - GOES-18 + VIIRS + Sentinel-5P/TROPOMI
   - 160+건, 33,000명 대피, pyrocumulonimbus, 연기 유럽 도달
   - 공식 출처: NOAA NESDIS, Copernicus CAMS

2. **이란 Kharg Island 원유 유출** — conf 0.88 + multiSatBoost(조건부) + sarBoost + officialBoost → 최종 1.0 (cap)
   - Sentinel-1(SAR) + Sentinel-2(광학) + Sentinel-3(해양색)
   - ~45,000km² 유막, ���란 최대 원유 수출 허브
   - 전후 비교 가용

3. **Kilauea Ep48 예보 유지** — conf 0.95 + officialBoost(USGS) → 최종 1.0 (cap)
   - Sentinel-2A + Landsat 9
   - ADVISORY/YELLOW, 재팽창 진행, Ep48 5/22-25 예보 유지
   - 연속 시리즈 추적 (Ep47 → Ep48)

4. **Flanders Fire 미네소타** — conf 0.88
   - GOES-18 + VIIRS
   - 1,700ac, 20% contained, National Guard 동원, 비상선포
   - Stewart Trail Fire와 partOfSeries

5. **Bismarck Sea 해저화산** — conf 0.90 + multiSatBoost(이전 적용)
   - Himawari-9 + VIIRS
   - 분출 지속, FL120 하강 추세. 1972년 이후 54년 만.

## 다중 위성 교차검증 대상 (2건 신규)
- Canadian Wildfires: NOAA(GOES-18, VIIRS) vs ESA(Sentinel-5P)
- Kharg Island Oil Spill: Sentinel-1(SAR) + Sentinel-2(광학) + Sentinel-3(해양색)

## 한반도 GeoFocus
- 직접 신규/업데이트 이벤트 없음.
- 추적 중: 동해 NLL 어선 + CSIS Beyond Parallel 영변/신포/판교 + KOMPSAT-7 커미셔닝

## 보고서 섹션별 배정

| 섹션 | 내용 |
|------|------|
| 핵심 Top 5 | Canada Fires, Kharg Oil, Kilauea, Flanders Fire, Bismarck Sea |
| 다중위성 교차검증 | Canada Fires, Kharg Oil (+ 기존 추적: Kilauea, Bismarck) |
| 한반도 GeoFocus | 직접 이벤트 없음 / 추적 항목 유지 |
| 자연재해 | Flanders★신규, Canada★신규, Stewart update, Kilauea update, Bismarck update, Everglades update |
| 인간활동 | Kharg Oil★신규, Pemex Cantarell(추적), Amazon Xingu(추적) |
| 기후·환경 | Canada smoke TROPOMI 유럽 도달(재해 파급), 기존 추적 7건 |
| 농업·해양 | 금일 신규 없음 / 동해 어선 추적 |
| 국방·안보 | 금일 신규 없음 / CSIS BP + 남중국해 추적 |
| 인도주의 | 금일 신규 없음 / Bellingcat 남레바논, 우크라이나 추적 |
| 센서별 묶음 | GOES/VIIRS(산불), Sentinel-1/2/3(유출), TROPOMI(연기) |
| 전후 비교 | Kharg Island(Sentinel-2 May 6 vs 8) |
| 미검증 의혹 | MizarVision 중국기업 미군 위성영상(출처 불명) |
