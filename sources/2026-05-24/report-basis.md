# 2026-05-24 보고서 기초 자료 (Phase 4)

## 1. 포함/제외 판정

### 포함 (Include) — 10건 업데이트

| src-ID | 이벤트 ID | 이벤트명 | 포함 근거 | 보고서 순위 |
|--------|-----------|---------|----------|------------|
| src-001 | evt-202 | Kilauea Ep48 D-1 | 예보 축소 5/25-26, 분출 24-48h 내 | **1** |
| src-003 | evt-1101 | Canada wildfire 연기 유럽 | CAMS 확인, 5위성 3기관, 인명피해 | **2** |
| src-005 | evt-701 | Bismarck Sea NASA EO | NASA 공식 기사, 부석 200km+, 신규 섬 가능 | **3** |
| src-002 | evt-1201 | Santa Rosa 87% | 72→87% 진압, mop-up phase | 4 |
| src-008 | evt-082 | Mayon AL3 Day139+ | PDC 발생, 장기 분출 | 5 |
| src-004 | evt-128 | Dukono VAAC#284 | 190폭발/일, FL070 | 6 |
| src-010 | evt-801 | Bezymianny KVERT Orange | 폭발적 분출, 열이상 | 7 |
| src-009 | temp-evt-1401 | Kanlaon AL2 SO2 | SO2 4081t/d 최고치 | 8 |
| src-006 | evt-203 | Great Sitkin WATCH | 용암돔 성장 | 9 |
| src-007 | evt-204 | Shishaldin ADVISORY | SO2 배출 | 10 |

### 제외 (Exclude) — 20건 기보고(reported, no change)

다음 항목은 금일 상태 변경 없음. 보고서에 포함하지 않음:
- Pemex Cantarell 유출 (evt-125)
- Kharg Island 유출 (기존)
- Amazon Xingu 금채굴 (evt-205)
- Antelope Reef (evt-120)
- Philippines Spratly (evt-305)
- CSIS DPRK 시설 (evt-115/116)
- Bellingcat Lebanon (evt-802/905)
- Hektoria Glacier (evt-118)
- Arctic sea ice (evt-503)
- Carbon Mapper (Tanager-1)
- UNEP MARS (evt-103)
- East Sea NLL fishing (evt-111)
- KOMPSAT-7 (evt-110)
- Odesa (evt-603)
- Iraq-Israel base (temp-evt-602)
- MizarVision (기존)
- Sentinel-1A recovery (temp-evt-1302)
- Everglades (evt-501)
- MethaneSAT (evt-122)
- Sentinel-2A extension (기존)

## 2. KG 시각화 범위

보고서에 포함할 Mermaid KG 다이어그램 범위:

### 핵심 노드 (10건 업데이트 이벤트)
```
evt-202 (Kilauea Ep48)
evt-1101 (Canada wildfire)
evt-701 (Bismarck Sea)
evt-1201 (Santa Rosa)
evt-082 (Mayon)
evt-128 (Dukono)
evt-801 (Bezymianny)
temp-evt-1401 (Kanlaon)
evt-203 (Great Sitkin)
evt-204 (Shishaldin)
```

### 관계 표시
- observedBy → 위성(최대 3개/이벤트)
- inCountry → 국가
- manifests → 현상
- inDomain → 도메인
- analyzedBy → 분석기관
- partOfSeries → 시리즈 연결 (Kilauea Ep47→Ep48)
- multiSatBoost → 교차검증 표시 (evt-1101, evt-701)

### 도메인별 클러스터
- **Disaster:** 화산(6) + 산불(2) = 8건
- **Climate/Env:** Bismarck Sea 부분 교차
- **Humanitarian:** Canada wildfire 부분 교차

## 3. 보고서 구조 가이던스

### 제목
`2026-05-24 위성영상 관측 이벤트 일일 다이제스트`

### 섹션 구성 (재해 우선순위 적용)

#### 1. 긴급 속보 (Breaking)
- **Kilauea Ep48 D-1:** 예보 5/25-26, 분수분출 임박. USGS HVO 공식. Landsat TIRS thermal.
- **Canada wildfire 연기 유럽 도달:** CAMS 공식 확인. 5위성 3기관 교차검증. 33,000+ 대피, 2명 사망.

#### 2. 주요 업데이트 (Major Updates)
- **Bismarck Sea NASA EO 공식:** 부석 200km+, 7km² thermal, 잠재적 신규 섬. NASA officialBoost.
- **Mayon AL3 Day139+ PDC:** PHIVOLCS 공식. PDC 위험 상승.
- **Santa Rosa 87%:** mop-up phase 심화. 진압 거의 완료.

#### 3. 화산 모니터링 (Volcano Watch)
- Dukono VAAC#284 (190 explosions/day)
- Bezymianny KVERT Orange (explosive)
- Kanlaon AL2 (SO2 4081t/d)
- Great Sitkin WATCH (lava dome)
- Shishaldin ADVISORY (SO2)

#### 4. 금일 신규 없음 명시 카테고리
- 인간활동(개발/군사/산업): 금일 신규 없음
- 농업/해양: 금일 신규 없음
- 기후/환경: 금일 신규 없음 (Bismarck Sea, Canada 연기는 Disaster 교차)

#### 5. 기추적 항목 요약
- 변경 없이 모니터링 지속 중인 20건 목록

#### 6. KG 시각화 (Mermaid)
- 금일 10건 업데이트 이벤트 중심 KG

#### 7. 내일 주시 항목
- Kilauea 분출 여부 (D-day)
- Canada 연기 유럽 대기질
- Kanlaon 경보 상향 여부
- Bismarck Sea 부석 이동
- Santa Rosa 진압 완료 여부

### 강조 포인트

1. **Kilauea Ep48 D-1** — 가장 중요. 예보 창 축소. 분출 시 Ep49가 아닌 Ep48 분수분출 단계 진입. USGS HVO 정량 데이터 인용.
2. **Canada wildfire 인도주의 차원** — 2명 사망, 33,000+ 대피, 군 투입, 연기 대서양 횡단. 다중 도메인 교차(Disaster + Humanitarian + Climate).
3. **Bismarck Sea NASA EO** — NASA 공식 기사 발행은 과학적 중요성 인증. 1972년 이후 최초 재활동. 잠재적 신규 섬 형성은 희소 지질 이벤트.

### 위성 출처 검증 상태

모든 10건 업데이트 이벤트가 최소 1개 위성/센서 출처 보유:
- evt-202: Landsat TIRS
- evt-1201: Landsat 9 OLI
- evt-1101: TROPOMI + OMPS + EarthCare + GOES-18 + VIIRS
- evt-128: Himawari-9 AHI
- evt-701: VIIRS + MODIS + Landsat 9 + Himawari-9 + PACE
- evt-203: Sentinel-1 SAR
- evt-204: Sentinel-5P TROPOMI
- evt-082: Himawari-9 AHI
- temp-evt-1401: Himawari-9 AHI
- evt-801: 위성 열이상(Himawari-9)

**미검증 의혹 항목: 0건** (금일 전체 업데이트가 위성 검증 완료)

### 보고서 언어
한국어 (report_language: ko). 원문 인용은 영문 보존.
