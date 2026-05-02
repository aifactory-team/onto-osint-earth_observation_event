# 2026-05-01 보고서 근거 (Report Basis)

## 포함 항목

| 소스 | 제목 | 태그 | 도메인 | 포함 근거 |
|------|------|------|--------|----------|
| src-001 | Mayon 화산 Landsat 8 | new | Disaster | NASA 공식 발표, Landsat 8 OLI+TIRS 위성 확인, 좌표·관측일 보유 |
| src-003 | Shiveluch 48,000ft 화산재 | new | Disaster | VAAC 공식 경보, Himawari-9 위성 관측 확인, 좌표 보유 |
| src-005 | Kilauea 위성 변화 (Apr 30) | update | Disaster | USGS HVO 공식 발표, 위성영상 변화 확인, Episode 46 예보 |
| src-008 | Georgia 산불 NASA EO | update | Disaster | NASA 공식 발표, Landsat 8 + VIIRS 다중 검증, 120+ 주택 파괴 |
| src-011 | MizarVision AI 군사 추적 | new | Defense | 상업 위성 군사 OSINT, 다수 매체 보도, Vantor/Maxar 위성 출처 확인 |
| src-014 | 이란전쟁 상업위성 시사점 | new | Defense | Breaking Defense 분석, 상업 원격탐사 군사 시사점 |
| src-015 | CAS500-2/4 발사 예정 | new | AgriMarine | KARI 공식, 한국 EO 위성 확장 |
| src-017 | NK 최현급 IMO 등록 | update | Defense | 위성영상 기반 분석 후속, NLL 전략 시사점 |
| src-018 | GFW DIST-ALERT | new | Human | GFW 공식 발표, Landsat+Sentinel-2 데이터 |
| src-021 | 베네수엘라 원유 유출 | new | Human | Global Witness, Sentinel-1 SAR 504건 탐지 |
| src-024 | Copernicus InSAR 코히런스 | new | AgriMarine | ESA 공식 서비스 출시 |
| src-027 | 매립지 메탄 Nature | new | Climate | Nature 논문, Sentinel-5P TROPOMI |

## 제외 항목

| 소스 | 제목 | 제외 근거 |
|------|------|----------|
| src-002 | Mayon space photo | src-001과 중복 (reported) |
| src-004 | Shiveluch Apr 29 | src-003과 중복 (reported) |
| src-006 | Kilauea Ep 45 recap | src-005와 중복 (reported) |
| src-009 | Georgia 파괴 Newsweek | src-008과 중복 (reported) |
| src-010 | Georgia GEMA | src-008과 중복 (reported) |
| src-012 | MizarVision DefensePost | src-011과 중복 (reported) |
| src-013 | Iran MizarVision ArmyRecog | src-011과 중복 (reported) |
| src-016 | NanoAvionics CAS500 | src-015와 중복 (reported) |
| src-019 | GFW drivers | src-018과 보조 (reported) |
| src-022 | UNDP-UNITAR framework | 위성 출처 미확인, 일반 역량 소개 |
| src-023 | UNOSAT Gaza update | 어제 보고 (reported) |
| src-025 | 10년 SAR 홍수 논문 | 연구 논문 — 특정 이벤트 아님 |
| src-026 | NOAA 산불 포털 | 일반 역량 소개 |
| src-028 | ASU SMAGNet | 연구 도구 소개 |
| src-029 | Svartsengi 계속 | 어제 보고 (reported) |
| src-030 | NK 저수지 Sentinel | 구체적 이벤트 아님, 일반 분석 |

## 미검증 의혹 항목
- ent-evt-014 (한반도 전국 산불 2026-04-26) — 어제 보고, 위성 출처 미확인 상태 지속

## KG 시각화 범위
오늘 보고서에 포함할 KG 노드 (30개 이내):
- 이벤트: ent-evt-029(Mayon), ent-evt-030(Shiveluch), ent-evt-020(Georgia), ent-evt-021(Kilauea), ent-evt-031(MizarVision), ent-evt-032(CAS500), ent-evt-034(Venezuela oil), ent-evt-035(methane), ent-evt-022(NK 최현급)
- 위성: sat-landsat8, sat-himawari9, sat-viirs-jpss, sat-sentinel1a, sat-sentinel5p, sat-worldview3, sat-cas500-2, sat-cas500-4
- 센서: sensor-oli, sensor-tirs, sensor-viirs, sensor-c-sar, sensor-tropomi
- 기관: org-nasa, org-noaa, org-kari, org-mizarvision, org-gfw, org-skytruth
- 국가: co-ph, co-ru, co-us, co-kr, co-kp, co-ve

## 보고서 구성 방향
1. **Top 5**: Georgia 산불(인명피해 최우선), Mayon 화산, MizarVision 군사OSINT, Kilauea Ep46 예보, 베네수엘라 원유
2. **다중 위성 교차검증**: Georgia(Landsat 8 + VIIRS), 어제 보고 11건 추적
3. **한반도 GeoFocus**: CAS500-2/4 발사(May 3), NK 최현급 IMO 등록, NK 드론·영변·소해 추적
4. **재해 1순위**: Georgia 산불 → Mayon → Shiveluch → Kilauea
5. **미검증**: 한반도 산불(Apr 26)
