# 2026-06-13 분석

## 신규 이벤트 (3건)

### evt-3301: 베트남 스프래틀리 27개 사이트 군사·해양 인프라 건설 [높음]
- **출처:** RFA + CSIS AMTI (6/8 보도)
- **위성:** PlanetScope
- **분석:** 베트남이 스프래틀리 18개 암초에 27개 사이트에서 활주로·항만·군사시설·통신설비 건설. Barque Canada Reef에 4,000m 활주로 건설 중. DVOR 항법 비컨 완공. 항만 15개로 확장. 중국·필리핀 건설과 병행되는 남중국해 인프라 경쟁 격화 신호.
- **도메인:** Defense (construction cross-domain)
- **중요도:** 높음 — 남중국해 세력 균형 변화의 위성 증거

### evt-3302: Sentinel-1 콘스텔레이션 궤도 재구성 [중간]
- **출처:** Copernicus Data Space Ecosystem (5/28 발표)
- **분석:** 6/9-23 S1C 기동(운영 중단), S1A+S1D가 커버. 6/24 S1C 복귀, S1D 관측 시나리오 전환. 6/29 S1A 퇴역. 최종 구성: S1C+S1D 6일 재방문. 전환 기간 중 SAR 커버리지 일시 감소 — 홍수·유류 유출 등 SAR 의존 모니터링에 영향.
- **도메인:** HumanActivity (satellite_operations)
- **중요도:** 중간 — 전역 SAR 모니터링 인프라 변경

### evt-3303: 북한 2026 모내기 위성 관측 [중간]
- **출처:** DailyNK (6/5 보도)
- **위성:** Landsat 8 + Landsat 9 (NDWI 분석)
- **분석:** 8개 표본지 비교 결과 2026년 북한 모내기가 예년 대비 2.7% 빠르게 진행. NDWI(정규화 수체지수) 기법으로 논 물 채움 지역 식별. 한반도 GeoFocus + 농업 카테고리 커버.
- **도메인:** AgricultureMaritime
- **중요도:** 중간 — 한반도 GeoFocus, 농업 카테고리 유일 항목

## 업데이트 이벤트 (9건)

| 이벤트 | 변경사항 | 신뢰도 |
|--------|---------|--------|
| evt-202 Kilauea Ep49 | D-Day 진입(6/13), 최유력 6/13-14, 틸트 팽창 가속 | 0.95 |
| evt-082 Mayon Day159+ | AL3 지속, 용암 효출+PDC+스트롬볼리, 라하르 우기 경보 | 0.90 |
| evt-701 Bismarck Sea Day36+ | 부석 마누스주 해안 도달, 해상 접근 차단 지속 | 0.90 |
| evt-3201 민다나오 M7.8 | 45,556 가옥 손상 (8,865 파괴), 사망 19→47+명 | 0.95 |
| evt-1101 캐나다 산불 | 65건 활성, 6건 통제불능, CIFFC Level 2 | 0.85 |
| evt-203 Great Sitkin | WATCH/ORANGE 유지, 용암 돔 성장 | 0.85 |
| evt-204 Shishaldin | ADVISORY/YELLOW 유지, 증기/SO2 | 0.80 |
| temp-evt-1902 El Niño | +0.9°C, 98% 확률, 63% very strong 전망 | 0.95 |
| Scarborough Shoal | 구조물 출현→소멸 (Vantor 5/27-30→6/1 소실) | 0.70 |

## 도메인별 분석

- **자연재해:** Kilauea Ep49 D-Day 진입이 금일 최대 관심사. Mayon/Bismarck Sea/캐나다 산불 모두 장기 추적 중. 민다나오 지진 피해 규모 대폭 상향.
- **인간활동:** 베트남 스프래틀리 건설은 남중국해 군사화 경쟁의 새 국면. Sentinel-1 궤도 재구성은 전역 SAR 인프라 전환.
- **기후·환경:** El Niño 강화 추세 지속 — 하반기 글로벌 영향 예상.
- **농업·해양:** 북한 모내기 Landsat NDWI 분석이 유일한 커버. 한반도 GeoFocus.

## 온톨로지 변경
- 새 Country: co-vn (베트남)
- 새 Organization: org-dailynk (DailyNK)
- 새 Location: ent-loc-barque-canada (Barque Canada Reef)
- 새 Event: 3건 (evt-3301, evt-3302, evt-3303)
- 스키마 구조 변경 없음 — 기존 클래스·관계로 충분
