# 2026-06-05 보고서 기초 자료

## 요약
신규 5건, 주요 업데이트 6건, 추적 지속 8건. 시진핑 방북 준비 위성 관측(WorldView-3, Kim Il Sung Square 건설+Sunan Airport, 6/11 추정). NASA EO NISAR 남아프리카 옥수수 삼각지대 식생(ZA 신규국). Sentinel-1D clock corruption + Sentinel-1 콘스텔레이션 재구성(S-1C 기동/S-1A 퇴역). NOAA 허리케인 시즌 below-normal(El Nino 억제). 캐나다 산불 65 active 감소 추세. Kilauea Ep49 10-15d. Bismarck Sea day28+ 감소. 다중 위성 교차검증 5건 유지. 한반도 GeoFocus 6건(신규 1건).

## 포함/제외 결정

### 포함 (Include) -- 19건

| # | 이벤트 | 신뢰도 | 포함 사유 |
|---|--------|--------|----------|
| 1 | temp-evt-2501: 시진핑 방북 준비 위성 관측 | 0.95 | **신규 이벤트 1순위**: WorldView-3/Vantor hiRes+korea+ba. 6/11 방문 추정. 복수 매체 교차보도. |
| 2 | temp-evt-2502: NISAR 남아프리카 Maize Triangle | 0.90 | **신규 이벤트**: NASA EO 공식. 농업/해양 카테고리 충족. ZA 신규국. |
| 3 | temp-evt-2503: Sentinel-1D clock corruption | 0.90 | **SatOps**: 글로벌 SAR 역량 영향. ESA 공식. |
| 4 | temp-evt-2504: Sentinel-1 콘스텔레이션 재구성 | 0.85 | **SatOps**: S-1A 퇴역, 신규 체제 전환. 전 세계 SAR 영향. |
| 5 | temp-evt-2505: NOAA 허리케인 below-normal | 0.90 | **기후 핵심**: NOAA CPC 공식. El Nino 억제 인과. |
| 6 | evt-1101: 캐나다 산불 65 active | 0.95 | 산불 추적: 감소 추세이나 6 OOC 지속. 5위성 유지. |
| 7 | evt-202: Kilauea ADVISORY/YELLOW | 0.90 | 화산 시리즈: Ep49 10-15d 예보. |
| 8 | evt-701: Bismarck Sea Day 28+ | 0.95 | 화산 시리즈: 감소 추세. 5위성 유지. |
| 9 | evt-082: Mayon Day 150+ AL3 | 0.90 | 화산 추적: 287K+ 이재민. |
| 10 | temp-evt-1902: El Nino 82% | 0.90 | 기후 핵심: strong 2/3. 허리케인 억제 연계. |
| 11 | evt-203: Great Sitkin WATCH | 0.88 | 화산 추적. |
| 12 | evt-204: Shishaldin ADVISORY | 0.85 | 화산 추적. |
| 13 | temp-evt-1401: Kanlaon AL2 | 0.85 | 화산 추적. SO2 2382 t/d. |
| 14 | evt-128: Dukono AL2 | 0.85 | 화산 추적. |
| 15 | temp-evt-2203: Sangay/Reventador | 0.80 | 화산 추적. |
| 16 | evt-1201: Santa Rosa 97% | 0.85 | 산불 종결 임박. BAER 6/5. |
| 17 | temp-evt-2001: Jangmi dissipated | 0.85 | 태풍 종결 기록. |
| 18 | temp-evt-2401: Gaza 40+ posts | 0.95 | 국방/인도주의 추적. |
| 19 | temp-evt-2002: Hami ICBM | 0.95 | 국방 추적. |

### 제외 (Exclude) -- 0건
- 금일 신규 미검증 이벤트 없음.

### 미검증 의혹 섹션 (별도 분리) -- 1건 유지
- **DPRK 서해 발사체 5/26 (temp-evt-1702):** 위성 미검증 상태 지속. 보고서 미검증 의혹 섹션 유지.

## Top 5
1. 시진핑 방북 준비 위성 관측 -- 0.95 (신규, 한반도 GeoFocus)
2. 캐나다 산불 65 active -- 0.95 (5위성 multiSat)
3. NOAA 허리케인 below-normal -- 0.90 (신규, NOAA CPC 공식)
4. NASA EO NISAR 남아프리카 -- 0.90 (신규, 농업 카테고리)
5. Sentinel-1 콘스텔레이션 재구성 -- 0.85~0.92 (SatOps, 글로벌 SAR 영향)

## 다중 위성 교차검증 (5건 유지, 변동 없음)
1. Bismarck Sea -- 5위성 3기관 (VIIRS+MODIS+Landsat9+Himawari-9+Sentinel-2A)
2. 캐나다 산불 -- 5위성 3기관 (GOES-18+VIIRS+TROPOMI+OMPS+EarthCare)
3. Kharg Island -- 3위성 3센서 (Sentinel-1+Sentinel-2+Sentinel-3)
4. Hami ICBM -- 2위성 2기관 (WorldView-3+PlanetScope)
5. Israel Gaza 40+ posts -- 2위성 2기관 (PlanetScope+WorldView-3)

## 한반도 GeoFocus (6건, 신규 1건)
1. **시진핑 방북 준비 위성 관측 (temp-evt-2501, KP)** -- 신규 추가
2. DPRK 최현급 구축함 서해 항해 + 남포 3번째 건조 (temp-evt-2003)
3. DPRK 구축함 2번함 Chongjin 건조 사고 (temp-evt-2102)
4. 압록강 신교량 세관시설 건설 (temp-evt-1601)
5. 두만강 북-러 교량 완공 임박 (temp-evt-1602)
6. DPRK 서해 발사체 5/26 (temp-evt-1702, 미검증)

## 카테고리 커버리지

| 카테고리 | 신규 | 업데이트 | 상태 |
|----------|------|---------|------|
| 자연재해 | 0 | 10+ | 충족 |
| 인간활동 | 1 | 0 | 충족 |
| 기후환경 | 1 | 1 | 충족 |
| 농업해양 | 1 | 0 | 충족 |

**4대 의무 카테고리 모두 충족.**

## 보고서 구조 제안

### 1순위: 신규 주요 이벤트
- 시진핑 방북 준비 위성 관측 (국방/인간활동)
- NASA EO NISAR 남아프리카 옥수수 삼각지대 (농업)
- NOAA 허리케인 시즌 below-normal (기후)

### 2순위: 위성 운영 (SatOps)
- Sentinel-1D clock corruption
- Sentinel-1 콘스텔레이션 재구성

### 3순위: 자연재해 추적
- 캐나다 산불 (감소 추세)
- Kilauea Ep49 예보
- Bismarck Sea (감소 추세)
- Mayon Day 150+ (장기)
- 기타 화산 (Great Sitkin, Shishaldin, Kanlaon, Dukono, Sangay/Reventador)
- Santa Rosa 97% (종결 임박)
- Jangmi 소멸

### 4순위: 국방/인도주의 추적
- Gaza 40+ military posts
- Hami ICBM

### 5순위: 기후
- El Nino 82% May-Jul

### 미검증 의혹
- DPRK 서해 발사체 5/26

## Mermaid KG 시각화 포함 대상 노드

```
temp-evt-2501 -- observedBy --> sat-worldview3
temp-evt-2501 -- locatedIn --> ent-loc-075 (Kim Il Sung Square)
temp-evt-2501 -- locatedIn --> ent-loc-076 (Sunan Airport)
temp-evt-2501 -- inCountry --> co-kp
temp-evt-2501 -- inDomain --> dom-defense
temp-evt-2501 -- analyzedBy --> org-vantor
temp-evt-2502 -- observedBy --> sat-nisar
temp-evt-2502 -- locatedIn --> ent-loc-077 (Maize Triangle)
temp-evt-2502 -- inCountry --> co-za
temp-evt-2502 -- inDomain --> dom-agri-marine
temp-evt-2502 -- analyzedBy --> org-nasa
temp-evt-2505 -- inDomain --> dom-climate
temp-evt-2505 -- analyzedBy --> org-noaa
temp-evt-1902 -- triggeredBy_causal --> temp-evt-2505 (El Nino -> hurricane suppression)
```
