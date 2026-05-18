# 2026-05-17 분석

## 신규 이벤트 (1건)

### ent-evt-1001: Stewart Trail Fire (Minnesota) — 중요도: 중간
- **위성:** GOES-19 (ABI true color loop)
- **현상:** wildfire, 375ac, 30% contained, 34 structures destroyed
- **지역:** Two Harbors, Lake County, MN (47.0°N, 91.67°W)
- **분석:** Lake Superior 북안에서 5/15 오후 발생한 산불. RH 21%의 극건조 조건과 돌풍(20mph+)으로 급속 확산. Hwy 61 폐쇄, Two Harbors~Castle Danger 대피명령. CIMSS 위성 블로그에서 GOES-19 true color loop로 연기 플룸 확인. 단일 위성 출처(GOES-19)로 multiSatBoost 미적용.

## 업데이트 항목 (3건)

### ent-evt-202: Kilauea Ep47 종료 + Ep48 예보 — 중요도: 높음
- Ep47 5/15 00:27 HST 종료 (9시간 연속 분수분출)
- ADVISORY/YELLOW로 하향
- HVO 모델: Ep48 예보 5/22-25
- 벤트 백열 지속, 화구 바닥 용암 냉각 중
- **multiSatBoost +0.20** (Sentinel-2A + Landsat 9 교차검증)
- **officialBoost +0.15** (USGS HVO)
- **partOfSeries** (Ep46→Ep47→Ep48 시계열)

### ent-evt-701: Bismarck Sea 해저화산 — 중요도: 높음
- VAAC #23 (5/17 05:00Z): FL120 (3,700m) NW
- 5/15 FL280 (8,500m) 정점 대비 현저히 하강
- 분출 지속이나 강도 약화 추세
- **multiSatBoost +0.20** (Himawari-9 + VIIRS)
- **partOfSeries** (5/8 onset → ongoing)

### ent-evt-501: Everglades Max Road Fire — 중요도: 중간
- 11,339ac 80% contained (전일 70% 대비 +10%p)
- 풍향 전환 우려이나 Florida Forest Service 1-2일 내 진압 자신
- 2차 화재: 172 Ave Fire (Florida City 인근 300ac 50%)
- **multiSatBoost +0.20** (GOES-18 + VIIRS)

## 도메인별 흐름

### 자연재해 (Disaster)
- **화산:** Kilauea Ep47 종료, Ep48 예보 5/22-25. Bismarck Sea FL120 하강 추세. Mayon Day132+ Alert Level 3 지속. Great Sitkin WATCH, Shishaldin ADVISORY, Bezymianny/Ibu 지속.
- **산불:** Minnesota Stewart Trail Fire 신규 발생 (GOES-19). Everglades 80% 진압 진행. Georgia Pineland 90%+ 마무리.
- **태풍/홍수:** 금일 신규 없음. Caloy 잔여저기압 종결 이후 서태평양 정온.

### 인간활동 (Human Activity)
- Pemex Cantarell 3개월+ SAR 관측 지속 (reported, 변동 없음)
- Amazon Xingu 금광 496k ha (reported, 변동 없음)

### 기후·환경 (Climate & Environment)
- UNEP MARS 메탄 석탄/폐기물 확대 (reported)
- NASA EO VIIRS 야간조명 Nature 표지 (reported)
- Harvard TROPOMI+GOSAT, MethaneSAT 글로벌 (reported, 변동 없음)
- 북극 해빙 14.29M km² 최저 타이, Hektoria 8km 후퇴 (reported)

### 농업·해양 (Agriculture & Maritime)
- 동해 NLL 중국 어선 (reported, 변동 없음)
- 금일 신규 없음

### 국방·안보 (Defense)
- 베트남 스프래틀리 216ha 확장 (reported)
- 필리핀 Thitu/Nanshan 건설 (reported)
- Antelope Reef 1,490ac 매립 (reported)
- 이라크 이스라엘 기지, CSIS Beyond Parallel (reported, 변동 없음)

### 인도주의 (Humanitarian)
- Bellingcat 남레바논 46/54 마을 파괴 (reported)
- 오데사 Grande Pettine (reported, 변동 없음)

## 온톨로지 변경
- **신규 Location 1건:** ent-loc-068 (Two Harbors, Minnesota)
- **신규 Event 1건:** ent-evt-1001 (Stewart Trail Fire)
- **스키마 변경:** 없음 (기존 클래스/관계로 충분)

## 추론 요약
- multiSatBoost 3건 (Kilauea, Bismarck Sea, Everglades)
- officialBoost 1건 (Kilauea)
- partOfSeries 2건 (Kilauea Ep series, Bismarck Sea)
- koreaBoost 0건 (직접 한국 이벤트 없음, NLL 어선은 reported)
