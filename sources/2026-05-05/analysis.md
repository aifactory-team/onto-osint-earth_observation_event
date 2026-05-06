# 2026-05-05 분석

## 도메인별 흐름 분석

### 자연재해 (Disaster) — 5건

- **Kilauea Episode 46 분출** (업데이트, ent-evt-070): USGS HVO 공식 보고 — 5/4 밤 용암 범람 시작, 5/5 북쪽 분출구에서 650ft(~200m) 용암 분수 확인. Episode 45(4/23, 270m) 이후 13일 만에 재분출. GOES-18 열적외 실시간 모니터링. 경보 수준 advisory→watch 상향. 2024-12-23 이후 46번째 에피소드 — Halema'uma'u 칼데라 시리즈 지속.
- **Mayon 화산 5월 5일 분출** (업데이트, ent-evt-071): VAAC Tokyo 0544Z 화산재 자문 발표, Himawari-9 관측. 필리핀 PHIVOLCS 경보 유지. 5/2 화쇄류 이후 지속 분출, 주변 도시 화산재 강하로 암흑 상태 보도(SCMP). 2026년 1월 이후 장기 분출 시리즈.
- **조지아 산불 진화 진전** (업데이트, ent-evt-072): GA Forestry 공식 — Hwy 82 화재 22,471ac 85% 봉쇄, Pineland Rd 32,575ac 50% 봉쇄. 5/4 대비 Hwy82 75→85%, Pineland 44→50% 진화율 상승. Landsat 8 OLI 위성 허위색 영상으로 피해 범위 계속 추적.
- **이탈리아 Monte Faeta 산불** (신규, ent-evt-073): 토스카나 피사/루카 경계 Monte Faeta에서 4/28 발생, 700ha 소실, 3,500명 대피, 5/3 진화. Copernicus Sentinel-2A 영상 확인(Euronews). 유럽 5월 초 이례적 대형 산불.
- **네덜란드 't Harde 산불** (신규, ent-evt-074): 겔더란트주 군사사격장 't Harde에서 4/29 발생. Sentinel-2A + PlanetScope 위성영상으로 다중위성 교차확인(Misbar). 연기가 영국까지 도달. Ruisdael 관측소 대기 영향 분석. **multiSatBoost +0.20** 적용.

### 국방·안보 (Defense) — 4건

- **중국 Type 004 핵추진 항공모함** (신규, ent-evt-075): Dalian 조선소에서 Type 004 건조 중 — SkyFi 위성영상으로 원자로 구획(reactor compartments) 구조 확인. 핵추진 항공모함 건조의 위성 증거로는 최초 수준의 공개 분석. lat 38.9, lon 121.6.
- **미국 카리브해 군사력 집결** (신규, ent-evt-076): 3개 항모전단, F-35, AC-130 등 대규모 전력이 베네수엘라 인근 해역에 집결. PlanetScope 위성으로 주요 자산 추적(The Conversation). lat 12.0, lon -68.0.
- **북한 신포 SLBM 발사 준비** (신규, ent-evt-077): SI Analytics 위성영상 분석에서 신포 남조선소 활동 증가 포착. 신형 미사일 잠수함 발사 가능성 제기(NASDAQ/싱크탱크). **koreaBoost +0.10** 적용. lat 39.8, lon 128.1(정밀도 하향 — 국방 민감정보 처리).
- **한국 425사업 정찰위성 5기 전력화** (업데이트, ent-evt-078): MBC 보도 — 425사업 정찰위성 5기 전력화 완료, 2시간마다 북한 전역 감시 가능 체계 구축. SAR+EO+IR 복합 관측. **koreaBoost +0.10** 적용. ent-evt-024 업데이트.

### 농업·해양 (AgricultureMaritime) — 1건

- **CAS500-2 스마트농업 활용** (신규, ent-evt-079): 한국인터넷진흥원 보도 — CAS500-2 위성의 농업 활용 전망. 작물 생육 모니터링, 병해충 탐지, 토양수분 분석 등 5가지 변화 예측. CAS500-4 광대역(120km) 센서와 연계한 농업·산림 모니터링 체계. **koreaBoost +0.10** 적용.

### 기후·환경 (ClimateEnvironment) — 0건 (신규)

- 금일 신규 기후·환경 이벤트 없음. 이전 보고서의 MethaneSAT Permian Basin 상원 조사(ent-evt-066), 그린란드 빙하 후퇴(ent-evt-068) 추적 지속.

### 인도주의 (Humanitarian) — 0건 (신규)

- 금일 신규 인도주의 이벤트 없음. 이전 보고서의 레바논 파괴(ent-evt-028), 가자 인프라 파괴(ent-evt-008) 추적 지속.

## 미검증 섹션

- **일본 산리쿠 M7.7 지진** (신규, ent-evt-080): 4/20 발생, 쓰나미 경보 발령. 그러나 위성 기반 피해 평가 미실시 상태. Disaster Charter 미발동, InSAR 지반변위 분석 미공개. 위성 출처 미확인으로 **confidence 0.50 미만** — 미검증 의혹 섹션으로 분류. lat 39.5, lon 143.5.

## 다중위성 교차검증

- **ent-evt-074 (네덜란드 't Harde 산불)**: Sentinel-2A (ESA, 10m 광학) + PlanetScope (Planet, 3m 광학) — 두 독립 사업자의 위성으로 동일 산불 이벤트 확인. multiSatBoost +0.20 적용. 금일 유일한 다중위성 교차검증 사례.

## 시간적 시리즈 분석

| 시리즈 | 현재 이벤트 | 이전 이벤트 | 최초 이벤트 | 경과 |
|--------|------------|------------|------------|------|
| Kilauea 분출 시리즈 | ent-evt-070 (Ep46, 5/5) | ent-evt-021 (Ep45, 4/23) | ent-evt-004 (Ep44, 4/15) | 46회 에피소드, 2024-12-23 이후 |
| Mayon 분출 시리즈 | ent-evt-071 (5/5 VAAC) | ent-evt-029 (5/2 PDC) | ent-evt-029 (2026-01~) | 5개월 이상 지속 |
| Georgia 산불 시리즈 | ent-evt-072 (5/5 85%) | ent-evt-020 (5/4 75%) | ent-evt-020 (4/30 최초) | 진화율 점진적 상승 |

## 한반도 GeoFocus 분석

금일 한반도 관련 3건:
1. **ent-evt-077 (NK 신포 SLBM)**: 신포 남조선소 활동 증가, SI Analytics 위성 분석. SLBM 잠수함 발사 가능성. 군사 민감 — 좌표 정밀도 하향(소수점 1자리).
2. **ent-evt-078 (425사업 전력화)**: 한국 독자 위성 감시체계 완성. SAR(KOMPSAT-5계열)+EO(KOMPSAT-3A계열)+IR 복합. 2시간 재방문.
3. **ent-evt-079 (CAS500-2 농업)**: CAS500-2/4 발사 성공(5/3) 이후 농업 응용 전망. 한국 위성 역량의 민수 확대.

## 온톨로지 변경 요약

### 새 인스턴스
- **국가**: co-nl (네덜란드, NL, 서유럽) — 't Harde 산불 이벤트에서 추가 필요
- **위치 5건**:
  - ent-loc-025: Monte Faeta, Tuscany (IT, 43.78/10.45)
  - ent-loc-026: 't Harde, Gelderland (NL, 52.37/5.77)
  - ent-loc-027: Dalian Shipyard, Liaoning (CN, 38.9/121.6)
  - ent-loc-028: Sinpo South Shipyard (KP, 39.8/128.1)
  - ent-loc-029: Sanriku offshore, Iwate (JP, 39.5/143.5)
- **기관 2건**:
  - org-skyfi: SkyFi (commercial_imagery, US) — 위성영상 태스킹 플랫폼
  - org-sianalytics: SI Analytics (commercial_imagery, KR) — 위성영상 AI 분석 기업
- **위성 1건**:
  - sat-skyfi: SkyFi tasking platform (commercial, multi-provider, 다양한 해상도)
- **이벤트 11건**: ent-evt-070~080

### 스키마 변경
- 없음 (기존 클래스/관계/현상으로 충분히 표현)
- phen-earthquake (earthquake_damage)가 ent-evt-080에서 첫 이벤트 참조 — mention_count 0→1

## 추론 결과 요약

1. **multi_satellite_confirmation**: 't Harde 산불(Sentinel-2A + PlanetScope) → +0.20
2. **temporal_progression**: Kilauea Ep46 partOfSeries Ep45, Mayon 5/5 partOfSeries 5/2, Georgia 5/5 partOfSeries 5/4
3. **official_source_trust**: Kilauea(USGS) → +0.15, Georgia(NASA) → +0.15
4. **korea_geo_focus**: NK 신포 SLBM(KP) → +0.10, 425사업(KR) → +0.10, CAS500 농업(KR) → +0.10
5. **commercial_imagery_provider**: Type 004(SkyFi) → +0.10
6. **analyst_org_trust**: 신포 SLBM(SI Analytics) → +0.10
7. **before_after_credibility**: Georgia 산불(Landsat 8) → +0.10
8. **satellite_unverified_cap**: 산리쿠 지진(ent-evt-080) → confidence 0.50 미만 cap

## 통계
- 총 이벤트: 11건 (신규 7 + 업데이트 4)
- 도메인별: Disaster 5, Defense 4, AgriMarine 1, Climate 0(신규), Humanitarian 0(신규)
- 다중위성 확인: 1건
- 한반도 GeoFocus: 3건
- 미검증: 1건 (산리쿠 지진)
