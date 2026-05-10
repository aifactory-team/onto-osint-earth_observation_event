# 2026-05-09 보고서 기초 자료

## 보고서 구성 순서

### 1순위: 인명피해 동반 자연재해
- Dukono 화산 수색 재개 (3 dead, 2 missing) -- UPDATE, 0.95
- Mayon 화산 VAAC 586 + 작물피해 (8km zone, 1,039ha rice) -- UPDATE+NEW, 0.92/0.90

### 2순위: 다중 위성 교차검증 이벤트
- TS Caloy PAR 진입 (Himawari-9 + GOES-18) -- UPDATE, 0.88
- GA Pineland 70% (S-NPP + Landsat 8/9) -- UPDATE, 0.88
- Kilauea Ep47 (Sentinel-2A + Landsat 9) -- UPDATE, 0.88

### 3순위: 신규 글로벌 이벤트
- NISAR+Landsat 삼림벌채 (dom-human) -- NEW, 0.85
- 필리핀 스프래틀리 건설 (dom-defense) -- NEW, 0.85
- Shivelyuch 화산 눈녹음 (dom-disaster) -- NEW, 0.88
- Tracy Arm 산사태-쓰나미 (dom-disaster) -- NEW, 0.85
- Peter I Island 폰카르만 소용돌이 (dom-climate) -- NEW, 0.82

### 4순위: 인프라/운영
- Sentinel-2A/2C 부분 복구 (dom-climate/sat-ops) -- UPDATE, 0.92

### 미검증 분리
- Fuego 화산 (dom-disaster) -- NEW, 0.45, satellite_unverified

## 도메인별 커버리지

| 도메인 | 이벤트 수 | 상태 |
|--------|----------|------|
| 자연재해 (dom-disaster) | 7+1미검증 | 커버 |
| 인간활동 (dom-human) | 1 | 커버 |
| 기후/환경 (dom-climate) | 2 | 커버 |
| 농업/해양 (dom-agri-marine) | 1 | 커버 |
| 국방/안보 (dom-defense) | 1 | 커버 |
| 인도주의 (dom-humanitarian) | 0 | 금일 신규 없음 |

## KG 시각화 노드 (30개 이내)

### 이벤트 노드 (13)
EVT01~EVT13: Dukono, Mayon, PhilSA ashfall, Caloy, GA Pineland, Kilauea, Sentinel-2 복구, 스프래틀리, NISAR 삼림벌채, Shivelyuch, Peter I, Tracy Arm, Fuego(미검증)

### 위성 노드 (8)
Himawari-9, GOES-18, S-NPP VIIRS, Landsat 8, Landsat 9, Sentinel-2A, NISAR, PlanetScope

### 기관 노드 (5)
PHIVOLCS/VAAC, NASA EO, PhilSA, USGS HVO, ESA Copernicus

## 전후비교 이벤트
- PhilSA Mayon ashfall 작물피해 -- Sentinel-2A MSI 전후비교 변화탐지 (Apr 28 vs May 3)

## cascading_disaster 상세
- Primary: TS Caloy PAR entry (confirmed May 9)
- Secondary: Mayon lahar risk (elevated -- PAR confirmed)
- Tertiary: PhilSA ashfall crop damage (confirmed chain)
- Confidence: 0.75 (Caloy->Mayon), 0.85 (Mayon->crop)

## 출처 URL 확인
- 신규 7건: 모두 URL 보유
- 업데이트 8건: 모두 URL 보유
- 미검증 1건: URL 보유 (VolcanoDiscovery)
- 기보도 12건: 본문 미포함 (출처 목록 기재)
