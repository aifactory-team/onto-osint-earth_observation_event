# Analysis — 2026-04-30 위성영상 관측 이벤트 분석

## 신규 소스별 중요도

| 소스 | 제목 | 도메인 | 중요도 | 근거 |
|------|------|--------|--------|------|
| src-001 | Yongbyon UEP 완공 (CSIS BP) | Defense | 높음 | 한반도 GeoFocus + IAEA Grossi 검증 + WV-3 hi-res |
| src-002 | RFA Yongbyon 4월 후속 | Defense | 높음 | src-001 update — 4월 15일 차량 관측 |
| src-003 | Sohae 마을 철거 (38 North) | Defense | 높음 | KP 발사장 확장 |
| src-004 | Piton de la Fournaise (NASA) | Disaster | 높음 | TIRS + 화산 high severity + before/after |
| src-005 | Kilauea Episode 44 InSAR | Disaster | 높음 | InSAR 12.5cm + 분출 |
| src-006 | GFW Tropical Forest Loss 2025 | HumanActivity | 높음 | 글로벌 GFW/UMD 4월 29일 발표 |
| src-007 | Antelope Reef (FDD) | Defense | 높음 | 인공섬 6.11 km² + Sentinel-2 다중 |
| src-008 | Bellingcat Iran PWTT | Humanitarian | 높음 | SAR PWTT 도구 |
| src-009 | UNOSAT 가자 평가 | Humanitarian | 높음 | 1500+ 건축물 파괴 |
| src-010 | Hektoria 빙하 붕괴 | Climate | 높음 | 역대 최단기 후퇴 |
| src-011 | Climate TRACE v5.5.0 | Climate | 중간 | 글로벌 배출 추적 |
| src-012 | TROPOMI 메탄 추세 | Climate | 높음 | TROPOMI+GOSAT 다중 |
| src-013 | Sinlaku 슈퍼태풍 | Disaster | 높음 | 4월 슈퍼태풍 |
| src-014 | Vaianu Cat 3 | Disaster | 높음 | 남태평양 |
| src-015 | 한반도 산불 4/26 | Disaster | 낮음 | **위성 미검증** — 미검증 의혹 분리 |
| src-016 | KOMPSAT-7 운용 시작 | AgriMarine | 중간 | 한반도 GeoFocus |
| src-017 | Maxar 우크라이나 GEGD 재개 | Defense | 중간 | 보도자료성 cap 0.7 |
| src-018 | ICEYE Sri Lanka Ditwah | Disaster | 높음 | SAR 홍수 매핑 |
| src-019 | Sentinel-1 GFM (CEMS) | Disaster | 중간 | 운영 인프라 |
| src-020 | SkyTruth Cerulean | HumanActivity | 중간 | 글로벌 오일 슬릭 |
| **src-021** | **Georgia 산불 (Landsat 8 + VIIRS)** | **Disaster** | **높음** | **50,000+ 에이커, 다중 위성 검증** |
| **src-022** | **Kilauea Episode 45 (Apr 23)** | **Disaster** | **높음** | **src-005 update, 270m 분수** |
| **src-023** | **NK 최현급 구축함 건조** | **Defense** | **높음** | **위성영상 확인, 한반도 GeoFocus** |
| **src-024** | **NK 군용 드론 생산 확대 (구성)** | **Defense** | **높음** | **위성영상 확인, KP 시설** |
| **src-025** | **한국 5기 정찰위성 체계** | **Defense** | **중간** | **한반도 GeoFocus, kill chain** |
| **src-026** | **Smith Glacier 42km 후퇴 (남극)** | **Climate** | **높음** | **다중 위성, 서남극** |
| **src-027** | **Hawaii 홍수 March 2026 (SAR)** | **Disaster** | **높음** | **NASA DAS 활성화, SAR 검증** |
| **src-028** | **Svartsengi 아이슬란드 마그마 (InSAR)** | **Disaster** | **중간** | **InSAR 위성 관측** |
| **src-029** | **레바논 위성 파괴 분석 (CNN)** | **Humanitarian** | **높음** | **위성영상 피해 분석** |
| **src-030** | **Antelope Reef AMTI 상세 (1,490 acres)** | **Defense** | **높음** | **src-007 update, 최대 인공섬** |
| **src-031** | **Sentinel-1D 데이터 개방 (Apr 17)** | **인프라** | **중간** | **3위성 SAR 성좌** |
| **src-032** | **나라스페이스 메탄 위성 발사 예정** | **AgriMarine** | **낮음** | **한반도 GeoFocus, 향후 자산** |

## 도메인별 흐름 분석

### Disaster (자연재해) — 10건
- 화산 3건 (Piton de la Fournaise, Kilauea Ep44/45, Svartsengi Iceland InSAR)
- 태풍/사이클론 3건 (Sinlaku, Vaianu, Ditwah)
- 홍수 3건 (Sri Lanka, CEMS GFM, Hawaii March 2026)
- 산불 1건 (Georgia — Landsat 8 + VIIRS 다중 위성 검증)

### HumanActivity — 2건
- 글로벌 열대 원시림 손실 (4.3M ha 2025)
- 해상 오일 슬릭 자동 탐지 (Cerulean)

### ClimateEnvironment — 4건
- Hektoria 빙하 다중 위성 시계열
- Smith Glacier 42km 후퇴 (서남극, 다중 위성)
- TROPOMI 메탄 (TROPOMI+GOSAT)
- Climate TRACE v5.5.0

### AgricultureMaritime — 1건
- KOMPSAT-7 한반도 정밀 관측 운용

### Defense — 8건
- 영변 UEP, Sohae, Antelope Reef (+AMTI update), Maxar Ukraine
- **신규: NK 최현급 구축함 건조, NK 드론 생산 구성, SK 5기 정찰위성 체계**

### Humanitarian — 3건
- UNOSAT Gaza, Bellingcat Iran PWTT, **레바논 파괴 위성 분석**

## 2차 수집 사이클 주요 발견

1. **Georgia 산불**: Landsat 8 burn scar + VIIRS/NOAA-21 연기 플룸으로 다중 위성 교차검증. 50,000+ 에이커는 2026 미국 최대 산불 중 하나.
2. **Kilauea Episode 45**: Episode 44에 이은 후속 분출(4월 23일), 최대 270m 분수. USGS HVO 지속 모니터링.
3. **NK 해군/군사 확장**: 최현급 구축함 3호 건조(10월 진수 목표) + 구성 드론 생산 시설 확장 — 위성영상 확인.
4. **Smith Glacier**: Hektoria에 이어 서남극 42km 접지선 후퇴 — 빙상 불안정성 확대 신호.
5. **Antelope Reef AMTI 업데이트**: 1,490 에이커(~6.03 km²)로 남중국해 최대 인공섬 가능성, 11,000 ft 활주로 추정 구간 식별.

## 온톨로지 변경 요약

- 새 Phenomenon 0건 (기존 스키마 충분)
- 새 Country 2건 (IS/Iceland, LB/Lebanon)
- 새 Satellite 1건 (Sentinel-1D)
- 새 Event 9건 (ent-evt-020 ~ 028)
- 새 Location 5건
- config 한도 준수 (클래스 0/3, 관계 0/5)

## 추론 결과 요약 (보충 포함)

- 다중 위성 교차검증 11건 (+2: Georgia, CEMS 3위성)
- 센서-현상 적합성 15건 (+3: VIIRS/TIRS wildfire, SAR flood Hawaii)
- 공식 출처 9건 (+2: USGS, NASA DAS)
- 한반도 GeoFocus 7건 (+3: NK 구축함, NK 드론, SK 정찰위성)
- 재해 우선순위 7건 (+2: Georgia wildfire, Hawaii floods)
- 전후 비교 9건 (+1: Hawaii)
- 평균 신뢰도 0.88, 확정 51건 / 잠정 3건

## 한반도 GeoFocus 특이사항

- KP: 영변 UEP + Sohae + **최현급 구축함 3호 건조 + 구성 드론 생산 확대** — 4건 모두 다중 상업 위성 교차검증.
- KR: KOMPSAT-7 운용 시작 + **한국 5기 정찰위성 체계 구축 완료** + 산불 4/26 미검증 — 정찰위성 체계가 한반도 EO 역량을 근본적으로 변화시키는 이정표.
