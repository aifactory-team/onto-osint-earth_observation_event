# 2026-05-01 분석 (Phase 3-4)

## 신규 소스 중요도 평가

| 소스 | 제목 | 도메인 | 중요도 | 근거 |
|------|------|--------|--------|------|
| src-001 | Mayon 화산 Landsat 8 관측 | Disaster | 높음 | NASA EO 공식 발표, Landsat 8 OLI+TIRS 확인, 대피 6km 반경 |
| src-003 | Shiveluch 48,000ft 화산재 | Disaster | 높음 | VAAC Tokyo 공식 경보, 항공 안전 위협 |
| src-008 | Georgia 산불 NASA EO (update) | Disaster | 높음 | 120+ 주택 파괴 — 조지아주 역대 최악, Landsat 8 + VIIRS 다중 검증 |
| src-011 | MizarVision AI 군사 위성 추적 | Defense | 높음 | 상업 위성영상의 군사 OSINT 활용 패러다임 변화, 이란 IRGC 활용 의혹 |
| src-015 | CAS500-2/4 발사 예정 | AgriMarine | 중간 | 한국 KARI 차세대중형위성, 농업 관측 전용 CAS500-4 |
| src-017 | 북한 최현급 IMO 등록 (update) | Defense | 중간 | NLL 방어 전략 변경 시사 |
| src-018 | GFW DIST-ALERT 가동 | Human | 중간 | 삼림 넘어 전 지구 식생 교란 감시 |
| src-021 | 베네수엘라 원유 유출 504건 | Human | 높음 | Sentinel-1 SAR 기반, 만성 해양 오염 |
| src-027 | 매립지 메탄 Nature 논문 | Climate | 중간 | Sentinel-5P TROPOMI 활용, 전 지구 규모 |

## 기존 보도 추적 (update 항목)

| 이벤트 | 이전 보고 | 변경사항 |
|--------|----------|----------|
| ent-evt-020 Georgia 산불 | 2026-04-30 (50,000+ acres) | NASA EO 정식 발표, 120+ 주택 파괴 확인 — 조지아주 역대 최다 |
| ent-evt-021 Kilauea Ep 45 | 2026-04-30 (270m 분수) | Apr 30 위성영상 변화 관측, Episode 46 예보 (May 5-9) |
| ent-evt-022 NK 최현급 | 2026-04-30 (3호함 건조) | IMO 공식 등록, NLL 위협 분석 심화 |
| ent-evt-019 Cerulean 오일 | 2026-04-30 (시스템 소개) | 근-실시간(NRT) 탐지 역량 업데이트 |

## 도메인별 흐름 분석

### 자연재해 (Disaster)
- 화산 활동 집중: Mayon(PH 신규), Shiveluch(RU 신규), Kilauea(US 계속), Svartsengi(IS 계속) — 4개 화산 동시 모니터링
- Georgia 산불은 인명·재산 피해 규모로 인해 1순위 배치
- Episode 46 예보(May 5-9)는 조기 경보 성격

### 인간활동 (HumanActivity)
- 베네수엘라 원유 유출: Sentinel-1 SAR로 504건 슬릭 탐지 — 만성적 해양 오염
- GFW DIST-ALERT: 삼림벌채를 넘어 전 지구 식생 교란으로 확장

### 기후·환경 (ClimateEnvironment)
- 매립지 메탄 위성 조사: Nature 논문, TROPOMI 활용, 기존 배출량 추정치에 불확실성 제기

### 농업·해양 (AgricultureMaritime)
- CAS500-4 발사(May 3): 120km 광역 관측 — 작황/수자원/산림 모니터링 전용 위성
- Copernicus InSAR 코히런스 서비스: openEO 기반 변화탐지 역량 확장

### 국방·안보 (Defense)
- MizarVision 사태: 상업 위성영상의 AI 자동 분석이 군사 OSINT를 민주화/위험화
- 북한 최현급 IMO 등록: 국제 규범 편입 시도 vs NLL 위협 증가

### 인도주의 (Humanitarian)
- 금일 신규 없음 — 어제 보고된 레바논/가자 상황 추적 지속

## 온톨로지 변경 요약
- 새 국가: PH(필리핀), VE(베네수엘라) — 2건
- 새 위성: CAS500-2, CAS500-4 — 2건
- 새 기관: MizarVision, Vantor, PHIVOLCS, Global Witness — 4건
- 새 위치: Mayon, Shiveluch, Lake Maracaibo — 3건
- 새 이벤트: 8건 (ent-evt-029~036)
- 업데이트: 4건 (ent-evt-019/020/021/022)

## 추론 결과 요약
- multi_satellite_confirmation: 1건 (Georgia 산불 Landsat 8 + VIIRS)
- sensor_capability_match: 5건 (Mayon TIRS, Georgia VIIRS thermal, Venezuela SAR, methane TROPOMI, MizarVision hi-res)
- official_source_trust: 3건 (Mayon NASA, Shiveluch VAAC, Georgia NASA)
- korea_geo_focus: 2건 (CAS500 발사, 북한 최현급)
- before_after_credibility: 2건 (Mayon, Georgia)
- temporal_progression: 1건 (Kilauea Ep44→45→46)
- disaster_severity_priority: 1건 (Georgia 인명·재산 피해)
