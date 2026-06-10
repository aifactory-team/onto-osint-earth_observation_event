# 2026-06-10 분석

## 신규 소스 중요도 평가

| 소스 | 제목 | 도메인 | 중요도 | 근거 |
|------|------|--------|--------|------|
| src-011 | Copernicus GFM v4.1.1 Sentinel-1D 통합 | SatOps | **중간** | CEMS 공식. S-1C 중단 기간 SAR 홍수 모니터링 연속성 확보. temp-evt-2504 시리즈. officialBoost +0.15. |
| src-012 | Vantor 위성 함대 확장 (Pulse 40cm) | SatOps | **낮음** | 상업 위성 PR. confidence cap 0.70. 직접적 관측 이벤트 아님. |
| src-013 | 아마존 삼림벌채 역대 최저 (INPE) | ClimateEnv | **높음** | INPE 공식 위성 데이터. Landsat 시계열 기반. 삼림벌채↓ vs 황폐화↑ 이중 발견. officialBoost +0.15, multiSatBoost +0.20. |
| src-014 | GFW 글로벌 식생 교란 경보 서비스 | ClimateEnv | **중간** | 기존 산림 경보→비산림 식생 교란까지 확대. Sentinel-2/Landsat/Planet 3기관 교차검증. analystBoost +0.10. |

## 업데이트 항목 변경사항

| 이벤트 | 전일 상태 | 금일 변경 |
|--------|----------|----------|
| Kilauea (evt-202) | Ep49 예보 6/12-15 | 가장 유력한 시기 6/13-14로 특정. tilt 15.2μrad 재팽창 가속. **3일 후 분출 가능.** |
| Bismarck Sea (evt-701/2903) | 부석 마누스섬 도달 | 3km x 5km, 5m 깊이 확대 + Discover Magazine 신규 섬 형성 가능성 분석 추가. 33일째 cascading. |
| 캐나다 산불 (evt-1101) | BC 최고 위험 | 142건 활성 화재. BC 최고 위험 지속. 6월 건조·고온 전망 악화 우려. |
| Mayon (evt-082) | AL3 Day154+ | Day156+. 6/9 Tokyo VAAC FL090 화산재 분출 통보(신규). 우기 라하르 위험 증가. |
| Super El Niño (temp-evt-1902) | Nino 3.4 +0.9°C | IRI Quick Look + Weather.com 추가 교차 확인(3출처). CPC 82%, ECMWF 100%. |
| Sentinel-1C (temp-evt-2504) | D-Day 중단 시작 | Day2. S-1A+S-1D 단독 운영. GFM v4.1.1이 S-1D 6/11 통합 예정(src-011 연계). |
| Great Sitkin (evt-203) | WATCH/ORANGE | 용암돔 확장 지속. SAR 모니터링. |
| Shishaldin (evt-204) | ADVISORY/YELLOW | 6/9 17:57 UTC 신규 AVO 통보. TROPOMI SO₂ 검출 지속. |
| Antelope Reef (evt-092) | 1,490 에이커 | 추적 지속. 신규 변동 없음. |
| 미림 퍼레이드 (evt-2801) | 수백 대 트럭 집결 | 추적 지속. 시진핑 방북 종결 후 10월 열병식 준비 가능성. |
| 베트남 스프래틀리 (evt-2901) | 27사이트 건설 | 추적 지속. 신규 변동 없음. |

## 도메인별 흐름

### Disaster (자연재해)
Kilauea Ep49 분출 가장 유력한 시기 6/13-14로 **3일 후 분출 가능** — 보고서 1순위. 비스마르크해 부석 피해 확대(3x5km) + 신규 섬 형성 가능성. Mayon FL090 화산재 분출(6/9 신규). 캐나다 산불 142건 BC 최고 위험 지속. Great Sitkin/Shishaldin/Kanlaon/Dukono 지속.

### HumanActivity (인간활동)
카르그섬 유출 추적 지속(기보도, 신규 없음). 시진핑 방북 종결(6/9) 후속 반응 추적.

### ClimateEnvironment (기후·환경)
Super El Niño +0.9°C threshold — 3출처 교차 확인으로 확실성 강화. **아마존 삼림벌채 역대 최저**(신규) — INPE 공식 데이터, 삼림벌채↓와 황폐화↑의 역설적 발견. GFW 식생 교란 경보 서비스 개시(신규).

### AgricultureMaritime (농업·해양)
북한 모내기 68.2% 추적 지속(기보도). 금일 신규 이벤트 없음.

### Defense (국방·안보)
베트남 스프래틀리 추적 지속(변동 없음). Antelope Reef 추적 지속(변동 없음). 미림 퍼레이드 준비 지속. 하미 핵 사일로(기보도).

### SatOps (위성 운영)
S-1C Day2 중단 + GFM v4.1.1 S-1D 통합(6/11). Vantor Pulse 함대 확장(PR, 낮은 우선도).

## 추론 결과 요약

1. **multi_satellite_confirmation**: 캐나다 산불(5위성), 비스마르크해(5위성), 카르그 유출(3위성), 아마존(Landsat+INPE), GFW(3기관) — 5건
2. **temporal_progression**: Kilauea Ep48→Ep49 예보 단축, GFM v4.1.1→temp-evt-2504 시리즈 — 2건
3. **cascading_disaster**: Bismarck Sea 해저 분출→부석 마누스 해안 피해 확대(33일째) — 1건
4. **sensor_capability**: Mayon 열적외(thermalBoost), Shishaldin TROPOMI SO₂(tracegasBoost), Great Sitkin SAR(sarBoost), evt-3003 다분광(hiResBoost) — 4건
5. **official_source_trust**: Kilauea USGS, CEMS GFM, 아마존 INPE — 3건
6. **commercial_imagery_trust**: Vantor PR cap 0.70 — 1건
7. **korea_geo_focus**: 미림 퍼레이드(evt-2801) — 1건

## 교차 분석 특기사항

- **Sentinel-1 체제 전환 연쇄 영향**: S-1C Day2 중단(temp-evt-2504) → GFM v4.1.1 S-1D 통합(evt-3001) → 6/29 S-1A 퇴역 예정. SAR 기반 모니터링(홍수·유출·빙하) 전체에 영향. 과도기 3주.
- **비스마르크해 최장 cascading**: 33일째 5단계 연쇄. 파이프라인 전체 역대 최장 기간.
- **삼림벌채 역설**: INPE 공식 삼림벌채↓ vs 독립 연구 황폐화↑. 단일 지표만으로는 삼림 건강성 평가 불충분 — 보고서에 양면 제시.
- **Kilauea 긴급도**: 6/13-14 분출 가장 유력 — 보고서 작성 시점 3일 후. 재해 우선순위 규칙에 따라 1순위 배치.
