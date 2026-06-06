# 2026-06-06 보고서 기초 자료

## 요약
신규 3건, 주요 업데이트 16건, 추적 지속 7건. 캐나다 산불 급격 악화(65건→134건, 18,935→113,300 ha, 면적 6배 증가). NASA EO 호주 계획 소각(MODIS Aqua 5/28). DPRK 모내기 68.2%(Landsat NDVI, 전년 대비 -3.1%p). 시진핑 방북 6/8-9 확정(신화통신, 위성 예측 검증). El Nino Super 격상(ECMWF 100%). Sentinel-1 재구성 D-3(S-1C 6/9 중단). 한반도 GeoFocus 7건(신규 1건).

## 포함/제외 결정

### 포함 (Include) -- 22건

| # | 이벤트 | 신뢰도 | 포함 사유 |
|---|--------|--------|----------|
| 1 | evt-2603: 캐나다 산불 134건, 113,300 ha | 0.95 | **신규 1순위(재해 우선)**: 면적 6배 증가. 5위성 multiSat. 인명·인프라 위험. |
| 2 | evt-2601: 호주 NT 계획 소각 (NASA EO) | 0.90 | **신규**: NASA EO 공식. 화재 관리 전략 위성 관측. |
| 3 | evt-2602: DPRK 모내기 68.2% (Landsat NDVI) | 0.80 | **신규**: 한반도 GeoFocus. 농업 카테고리 충족. 식량 안보 지표. |
| 4 | temp-evt-2501: 시진핑 방북 6/8-9 확정 | 0.95 | **업데이트 핵심**: 위성 예측 → 공식 확인. 한반도 GeoFocus. |
| 5 | temp-evt-1902: El Nino Super 격상 (ECMWF 100%) | 0.92 | **기후 핵심**: Super El Nino 격상. 허리케인 억제 인과 강화. |
| 6 | temp-evt-2504: Sentinel-1 재구성 D-3 | 0.95 | **SatOps 긴급**: S-1C 6/9 취득 중단까지 3일. |
| 7 | evt-202: Kilauea ADVISORY/YELLOW, Ep48 기록 | 0.90 | 화산 시리즈: Ep48 기록 갱신. |
| 8 | evt-701: Bismarck Sea Day 29+, pumice rafts | 0.80 | 화산 시리즈: 감소 + pumice rafts 신규. |
| 9 | evt-082: Mayon Day 152+ AL3 | 0.90 | 화산 추적: SO2 변동 범위 갱신. |
| 10 | evt-203: Great Sitkin WATCH | 0.90 | 화산 추적. |
| 11 | evt-204: Shishaldin ADVISORY | 0.85 | 화산 추적. |
| 12 | temp-evt-1401: Kanlaon AL2 | 0.85 | 화산 추적. SO2 2,382 t/d. |
| 13 | evt-128: Dukono AL2, 3명 사망 | 0.85 | 화산 추적. 인명피해. |
| 14 | temp-evt-2203: Sangay/Reventador | 0.80 | 화산 추적. |
| 15 | evt-1201: Santa Rosa 97%, BAER 도착 | 0.90 | 산불 종결 임박. |
| 16 | temp-evt-2001: Jangmi 소멸 | 0.85 | 태풍 종결 기록. |
| 17 | temp-evt-2401: Gaza 40+ posts | 0.75 | 국방/인도주의 추적. |
| 18 | temp-evt-2002: Hami ICBM | 0.80 | 국방 추적. |
| 19 | evt-092: Antelope Reef | 0.85 | 인간활동 추적. |
| 20 | evt-2502: NISAR Maize Triangle | 0.95 | 농업 추적 지속. |
| 21 | evt-2505: 허리케인 시즌 below-normal | 0.90 | 기후 추적. |
| 22 | evt-2503: S-1D clock anomaly 해소 | 0.95 | SatOps 해소 기록. |

### 제외 (Exclude) -- 0건
- 금일 신규 미검증 이벤트 없음.

### 미검증 의혹 섹션 (별도 분리) -- 1건 유지
- **DPRK 서해 발사체 5/26 (temp-evt-1702):** 위성 미검증 상태 지속. 보고서 미검증 의혹 섹션 유지.

## Top 5
1. 캐나다 산불 134건, 113,300 ha -- 0.95 (신규 evt-2603, 면적 6배 증가, 5위성 multiSat)
2. 시진핑 방북 6/8-9 확정 -- 0.95 (위성 예측 → 공식 확인, 한반도 GeoFocus)
3. El Nino Super 격상, ECMWF 100% -- 0.92 (기후 핵심, 허리케인 억제 인과)
4. 호주 NT 계획 소각 (NASA EO) -- 0.90 (신규, 화재 관리 위성 관측)
5. DPRK 모내기 68.2% (Landsat NDVI) -- 0.80 (신규, 한반도 GeoFocus, 식량 안보)

## 다중 위성 교차검증 (5건, 변동 1건)
1. **캐나다 산불 evt-2603** -- 5위성 2기관 (VIIRS x2 + GOES-18 + Sentinel-2 + TROPOMI) **[규모 급변]**
2. Bismarck Sea -- 2위성 1기관 (Sentinel-2 + Landsat-9)
3. Hami ICBM -- 2위성 2기관 (WorldView-3 + PlanetScope)
4. Israel Gaza 40+ posts -- 2위성 2기관 (PlanetScope + WorldView-3)
5. DPRK 모내기 evt-2602 -- 2위성 1기관 (Landsat-8 + Landsat-9) **[신규]**

## 한반도 GeoFocus (7건, 신규 1건)
1. **DPRK 모내기 68.2% Landsat NDVI (evt-2602, KP)** -- 신규 추가
2. 시진핑 방북 6/8-9 확정 (temp-evt-2501, KP)
3. DPRK 최현급 구축함 서해 항해 + 남포 3번째 건조 (temp-evt-2003)
4. DPRK 구축함 2번함 Chongjin 건조 사고 (temp-evt-2102)
5. 압록강 신교량 세관시설 건설 (temp-evt-1601)
6. 두만강 북-러 교량 완공 임박 (temp-evt-1602)
7. DPRK 서해 발사체 5/26 (temp-evt-1702, 미검증)

## 카테고리 커버리지

| 카테고리 | 신규 | 업데이트 | 상태 |
|----------|------|---------|------|
| 자연재해 | 2 | 10+ | 충족 |
| 인간활동 | 0 | 1 | 충족 |
| 기후환경 | 0 | 1 | 충족 |
| 농업해양 | 1 | 1 | 충족 |

**4대 의무 카테고리 모두 충족.**

## 보고서 구조 제안

### 1순위: 신규 주요 이벤트 -- 재해 우선
- 캐나다 산불 급격 악화: 134건, 113,300 ha (면적 6배 증가, 5위성)
- 호주 NT 계획 소각 (NASA EO, MODIS Aqua)

### 2순위: 한반도/외교
- 시진핑 방북 6/8-9 확정 (위성 예측 → 공식 확인 검증 사례)
- DPRK 모내기 68.2% (Landsat NDVI, 식량 안보)

### 3순위: 기후/ENSO
- El Nino Super 격상 (ECMWF 100%, 허리케인 억제)

### 4순위: 위성 운영 (SatOps)
- Sentinel-1 재구성 D-3 (S-1C 6/9 취득 중단)
- S-1D clock anomaly 해소

### 5순위: 자연재해 추적
- Kilauea Ep48 기록 / Ep49 예보
- Bismarck Sea Day 29+ / pumice rafts
- Mayon Day 152+ / SO2 변동
- 기타 화산 (Great Sitkin, Shishaldin, Kanlaon, Dukono, Sangay/Reventador)
- Santa Rosa 97% (BAER 도착)
- Jangmi 소멸 (종결)

### 6순위: 국방/인도주의 추적
- Gaza 40+ military posts
- Hami ICBM
- Antelope Reef

### 미검증 의혹
- DPRK 서해 발사체 5/26

## Mermaid KG 시각화 포함 대상 노드

```
evt-2603 -- observedBy --> sat-snpp (VIIRS)
evt-2603 -- observedBy --> sat-noaa21 (VIIRS)
evt-2603 -- observedBy --> sat-goes18 (ABI)
evt-2603 -- observedBy --> sat-s2 (MSI)
evt-2603 -- observedBy --> sat-s5p (TROPOMI)
evt-2603 -- locatedIn --> loc-canada-fires
evt-2603 -- supersedes --> evt-1101
evt-2603 -- analyzedBy --> org-nesdis

evt-2601 -- observedBy --> sat-aqua (MODIS)
evt-2601 -- locatedIn --> loc-australia-nt
evt-2601 -- analyzedBy --> org-nasa

evt-2602 -- observedBy --> sat-l8 (OLI)
evt-2602 -- observedBy --> sat-l9 (OLI-2)
evt-2602 -- locatedIn --> loc-dprk-nationwide
evt-2602 -- analyzedBy --> org-dailynk
evt-2602 -- inDomain --> dom-agri-marine

temp-evt-2501 -- confirmedBy --> org-xinhua
temp-evt-2501 -- predictionValidated --> true

temp-evt-1902 -- causalLink --> evt-2505 (El Nino -> hurricane suppression)
temp-evt-1902 -- analyzedBy --> org-ecmwf

temp-evt-2504 -- affects --> sat-s1c (suspended 6/9-23)
temp-evt-2504 -- affects --> sat-s1a (terminated 6/29)
```
