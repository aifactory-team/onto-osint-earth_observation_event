# 2026-06-13 보고서 작성 근거

## 포함 항목

| 소스 ID | 제목 | 태그 | 도메인 | 포함 근거 |
|---------|------|------|--------|----------|
| src-001 | Kilauea Ep49 D-Day | update | Disaster | 예보 창 D-Day 진입, 금일 분출 가능 |
| src-002 | Mayon Day159+ | update | Disaster | AL3 장기 분출, 라하르 우기 경보 |
| src-003 | Bismarck Sea Day36+ | update | Disaster+Humanitarian | 해상 접근 차단, 인도주의 위기 |
| src-004 | 민다나오 M7.8 | update | Disaster | 피해 규모 상향 (45,556 가옥) |
| src-005 | 캐나다 산불 65건 | update | Disaster | CIFFC Level 2 유지 |
| src-006 | Great Sitkin WATCH | update | Disaster | 용암 돔 성장 지속 |
| src-007 | Shishaldin ADVISORY | update | Disaster | 증기/SO2 지속 |
| src-008 | El Niño +0.9°C | update | Climate | 강화 추세, 글로벌 영향 |
| src-009 | 베트남 스프래틀리 건설 | new | Defense | 27개 사이트 위성 확인, 남중국해 정세 |
| src-010 | Sentinel-1 궤도 재구성 | new | HumanActivity | 전역 SAR 인프라 전환, 모니터링 영향 |
| src-011 | 북한 모내기 위성 분석 | new | AgricultureMaritime | 한반도 GeoFocus, 농업 카테고리 |
| src-012 | Scarborough Shoal | update | Defense | 구조물 출현→소멸, 남중국해 긴장 |

## 제외 항목

없음. 모든 수집 항목이 위성영상 관련 이벤트로 보고서에 포함.

## KG 시각화 범위

금일 보고서 KG 시각화에 포함할 노드/엣지:
- 핵심 이벤트: evt-202, evt-082, evt-701, evt-3201, evt-3301, evt-3302, evt-3303, evt-1101, temp-evt-1902
- 위성: sat-landsat9, sat-sentinel2a, sat-viirs-jpss, sat-planetscope, sat-landsat8, sat-himawari9, sat-sentinel1c, sat-sentinel1a, sat-sentinel1d
- 기관: org-usgs, org-esa, org-rfa, org-dailynk, org-noaa
- 국가: co-us, co-ph, co-pg, co-vn, co-kp
- 현상: phen-volcano, phen-earthquake, phen-wildfire, phen-construction, phen-ndvi, phen-satops
- 도메인: dom-disaster, dom-defense, dom-agri-marine, dom-climate, dom-human

## 보고서 구성 방향

1. **오늘의 핵심 Top 5:** Kilauea D-Day, 민다나오 피해 상향, Bismarck Sea 인도주의, 베트남 스프래틀리, El Niño
2. **다중 위성 교차검증:** evt-701 (5위성), evt-1101 (5위성) 유지
3. **한반도 GeoFocus:** evt-3303 북한 모내기 Landsat NDWI (신규!)
4. **센서·플랫폼 특기사항:** Sentinel-1C 기동으로 SAR 커버리지 일시 감소 경고
5. **미검증 의혹:** Scarborough Shoal 구조물 (0.70, 출현→소멸)
