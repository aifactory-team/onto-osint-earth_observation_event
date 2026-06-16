# 보고서 기반 — 2026-06-16

## 핵심 5건 (신뢰도·영향규모 기준)

1. **Kilauea Episode 49 분출·종료** — 6/14 09:36 HST 분출, 17:05 종료 (7.5시간). 분수 213m(700ft), 플룸 5500m(18,000ft). 역대 최다 49회 에피소딕 분수분출 기록 (Pu'u'O'o 47회 초과). WATCH→ADVISORY 하향.
2. **Bismarck Sea 부석 Admiralty Islands 침입** — NASA EO Image of Day. Titan Ridge 부석이 해안 도달, 해초/산호 광합성 차단, 어류 폐사, Manus Province 식량 위기 우려 심화.
3. **Mindanao M7.8 Sentinel-2 산사태 영상** — 6/14 Sentinel-2 영상으로 66건 산사태 확인, >500m 대형 다수. NDRRMC 공식 집계.
4. **Canada 2026 산불 시즌 급증** — 1,747 fires YTD (전일 1,495), 95 active (전일 65+), 44 out of control, 166,400 ha (전일 78,800 ha). 면적 2배 이상 증가.
5. **Copernicus GFM v4.1.1 Sentinel-1D 통합** — SAR 기반 자동 홍수 매핑에 Sentinel-1D 정식 투입. 5시간 내 NRT 홍수 지도 생성.

## 다중 위성 교차검증 이벤트
- evt-701: Landsat 9 + Sentinel-2A + Himawari-9 + VIIRS (4 satellites)
- evt-1101: MODIS (Terra) + VIIRS (JPSS)
- evt-3501: WorldView-3 + PlanetScope (3 independent analysts)
- evt-3601: Sentinel-2A + Landsat 9 (NDVI)

## 한반도 GeoFocus
- evt-3601: 북한 제2차 조림 10개년 계획 위성 NDVI 관측 (DailyNK). koreaBoost +0.10.
- 금일 KOMPSAT/CAS500 직접 관측 신규 이벤트: 없음

## 전후 비교 보유 이벤트
- evt-3201: Sentinel-2 6/8(지진 전) vs 6/14(산사태 후) before/after
- evt-3601: DPRK NDVI 다년간 시계열 비교
- evt-3501: Hami 시계열 6년간 인프라 구축 (유지)

## 미검증 의혹 (위성 출처 미확인)
- evt-3601 (DPRK reforestation): DailyNK 단독 보도. 위성영상 기반이나 구체적 위성명 불명확. Sentinel-2/Landsat 추정. 신뢰도 0.75 (analystBoost 미적용, 잠정).

## 포함/제외 판단

### 포함 (12건)
| Event | 포함 사유 |
|-------|----------|
| evt-202 Kilauea Ep49 | 공식 기관(USGS) + 다중 출처(HVO + Watchers + Star-Advertiser). 역사적 기록 갱신. |
| evt-701 Bismarck Sea | NASA EO 공식. 다중 위성. 생태·인도주의 영향 확대. |
| evt-3303 GFM v4.1.1 | Copernicus EMS 공식 출시. SAR 홍수 모니터링 역량 확대. |
| evt-3401 AI4CH4 | ESA 공식. 메탄 탐지 역량 확대. Climate 카테고리 커버. |
| evt-1101 Canada wildfire | 정부 공식 발표. 다중 위성. 규모 급증. |
| evt-3201 Mindanao | Sentinel-2 영상 확인. 전후 비교. 66건 산사태. |
| evt-3601 DPRK reforestation | 한반도 GeoFocus. 위성 NDVI. Human Activity 카테고리. |
| evt-082 Mayon | PHIVOLCS 공식. Day162+. 287K+ 이재민. |
| evt-203 Great Sitkin | USGS AVO 공식. WATCH/ORANGE 유지. |
| evt-204 Shishaldin | USGS AVO 공식. ADVISORY/YELLOW 유지. |
| evt-3501 China Hami | 다중 위성. 고해상도 확인. Defense 카테고리. |

### 제외
- 없음. 금일 전체 수집 항목 보고서 포함 판단.
