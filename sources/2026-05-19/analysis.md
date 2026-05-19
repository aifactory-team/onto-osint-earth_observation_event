# 2026-05-19 온톨로지 분석

## 온톨로지 변경

### 새 인스턴스 추가 (5건)
1. **evt-20260519-flanders** (Event) — Flanders Fire, Crow Wing County, Minnesota
2. **evt-20260519-canada-fires** (Event) — Canadian Wildfires Manitoba/Ontario/Saskatchewan
3. **evt-20260519-kharg-oil** (Event) — Kharg Island Oil Spill, Persian Gulf
4. **co-ca** (Country) — 캐나다 (CA) — 첫 등장
5. **co-ir** (Country) — 이란 (IR) — 첫 등장

### 스키마 변경: 없음
- 기존 클래스·관계 유형으로 모든 신규 엔티티 표현 가능.

## 추론 결과 요약

| 규칙 | 대상 | 가산 | 비고 |
|------|------|------|------|
| multi_satellite_confirmation | Canada Fires | +0.20 | GOES-18 + VIIRS + Sentinel-5P (NOAA vs ESA) |
| multi_satellite_confirmation | Kharg Oil | +0.20 | Sentinel-1/2/3 (3 독립 센서/플랫폼) |
| sensor_capability_match_tracegas | Canada Fires | +0.15 | TROPOMI CO/smoke 300hPa 탐지 |
| sensor_capability_match_sar | Kharg Oil | +0.10 | SAR 유막 dampening 탐지 |
| official_source_trust | Canada Fires | +0.15 | NOAA + ESA/CAMS |
| official_source_trust | Kharg Oil | +0.15 | ESA Copernicus |
| temporal_progression | Flanders↔Stewart | series | 동일 지역+현상+조건 |
| temporal_progression | Canada→Flanders | series | 기상학적 연관 |

## 도메인 커버리지

| 도메인 | 신규 | 업데이트 | 합계 |
|--------|------|----------|------|
| 자연재해 (dom-disaster) | 2 | 5 | 7 |
| 인간활동 (dom-human) | 1 | 0 | 1 |
| 기후·환경 (dom-climate) | 0 | 0 | 0 (추적 중 7건) |
| 농업·해양 (dom-agri-marine) | 0 | 0 | 0 (추적 중 1건) |
| ���방·안보 (dom-defense) | 0 | 0 | 0 (추적 중 4건) |
| 인도주의 (dom-humanitarian) | 0 | 0 | 0 (추적 중 2건) |

## 의사결정 기록
- Kharg Island oil spill: 동일 기관(ESA)의 3개 위성이나, SAR/광학/해양색으로 **센서 모달리티가 독립**이므로 multiSatBoost 적용 판단. 반론: 엄격하게는 동일 기관이므로 운영 독립성 미충족. → 조건부 적용(multiSatBoost 부여하되 보고서에 "동일 ESA 플랫폼이나 센서 독립" 주석 기재).
- Canadian fires: 연기 유럽 도달은 기후·환경 도메인 파급이나, 원인 이벤트가 wildfire이므로 dom-disaster 주 분류 유지. 보고서 기후·환경 섹션에서 대기 수송 관련 언급만 추가.
