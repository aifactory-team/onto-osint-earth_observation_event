# 2026-05-06 보고서 근거

## 포함 항목

| 소스 ID | 제목 | 태그 | 도메인 | 이벤트 ID | 포함 근거 |
|---------|------|------|--------|----------|----------|
| src-001 | Iran US bases 228 structures — WashPost Copernicus+Planet 교차검증 | new | Defense | temp-081 | 높음 — 다중위성(Sentinel-2A+PlanetScope) 교차검증, 전후비교 영상, multiSatBoost +0.20, baCredibilityBoost +0.10, hiResBoost +0.15 |
| src-002 | Kīlauea Episode 46 종료 — 650ft 용암 분수, 4.6M m³ (USGS HVO) | update | Disaster | ent-evt-021 | 중간 — USGS 공식 종료 보고, officialBoost +0.15, 9시간 분출 후 종료 |
| src-003 | Mayon VAAC 5/6 1252Z — Himawari-9 화산재 자문 | update | Disaster | ent-evt-029 | 중간 — VAAC Tokyo 공식 자문, 분출 지속 확인 |
| src-004 | PhilSA 마욘 화산재 위성 매핑 — 8,544ha 피복 | new | Disaster | temp-082 | 높음 — PhilSA+PHIVOLCS 우주기관 공식, officialBoost +0.15, 정량적 위성 산출물 |
| src-005 | Georgia 산불 — Hwy82 85%, Pineland 65% 봉쇄 | update | Disaster | ent-evt-041 | 중간 — 진화율 상승, Landsat 8 지속 모니터링, officialBoost +0.15 |
| src-007 | 아마존 금채굴 496,000ha 삼림벌채 — Sentinel-2+PlanetScope | new | Human | temp-083 | 높음 — 다중위성 교차검증, multiSatBoost +0.20, 시계열 비교(2018~2026), baCredibilityBoost +0.10 |
| src-008 | 이란 민간 피해 7,645동 — Bloomberg Sentinel-2+Planet | new | Humanitarian | temp-084 | 높음 — 다중위성 교차검증, multiSatBoost +0.20, 인도주의 피해 정량 평가, cascading_disaster(temp-081 연계) |
| src-011 | MethaneSAT Permian Basin — NM 1.2% vs TX 3.1% | update | Climate | ent-evt-053 | 중간 — MethaneSAT 전용 위성 데이터, 상원 조사 연계, 정량 비교 |
| src-018 | UNOSAT Gaza 198,273 구조물 81% 손상 | update | Humanitarian | ent-evt-028 | 중간 — UNOSAT 공식 위성 피해 평가, 누적 규모 확대 |
| src-021 | 이란 핵시설 부분 생존 — CNN 위성 조사 | new | Defense | temp-085 | 높음 — Sentinel-2A 피해 평가, 전략적 의미 |

## 제외 항목

| 소스 ID | 제목 | 제외 근거 |
|---------|------|----------|
| src-006 | Tuscany Monte Faeta wildfire 700ha — EMSR873 | 이전 보도 reported (2026-05-05/src-007에서 보고 완료, 5/3 진화 종료) |
| src-009 | CNN Iran nuclear — satellite images show some survived | src-021과 동일 이벤트 reported, 보충 출처로 본문 기재 |
| src-010 | Middle East Eye — far more US sites hit | src-001과 동일 이벤트 reported, 보충 출처로 본문 기재 |
| src-012 | Greenland glacier retreat Landsat+Sentinel-2 | 이전 보도 reported (2026-05-04/src-020에서 보고 완료) |
| src-013 | K-위성 스마트농업 CAS500 | 이전 보도 reported (2026-05-05/src-015에서 보고 완료) |
| src-014 | NK Sinpo-B submarine — 38 North | 이전 보도 reported (2026-05-05/src-012에서 보고 완료) |
| src-015 | China Type 004 carrier — SkyFi | 이전 보도 reported (2026-05-05/src-010에서 보고 완료) |
| src-016 | US Caribbean buildup — satellite tracking | 이전 보도 reported (2026-05-05/src-011에서 보고 완료) |
| src-017 | 425사업 정찰위성 5기 전력화 | 이전 보도 reported (2026-05-05/src-013에서 보고 완료) |
| src-019 | Mayon eruption continues — volcanodiscovery | src-003과 동일 이벤트 reported, 보충 출처로 본문 기재 |
| src-020 | USGS Photo Chronology May 5 Kīlauea | src-002와 동일 이벤트 reported, 보충 출처로 본문 기재 |
| src-022 | China Lop Nur J-36 — satellite | 이전 보도 reported (2026-05-04/src-009에서 보고 완료) |

## 이벤트 포함/분류

### 본문 포함 이벤트 (confidence >= 0.50, 위성 출처 확인)

- temp-081: 이란 미군기지 위성 피해 확인 (Sentinel-2A+PlanetScope, WashPost) — **1순위 국방·인도주의 (최고 영향)**
- temp-082: 마욘 화산재 PhilSA 위성 매핑 8,544ha (Himawari-9, PhilSA+PHIVOLCS) — 자연재해
- temp-083: 아마존 금채굴 삼림벌채 496,000ha (Sentinel-2A+PlanetScope) — 인간활동
- temp-084: 이란 민간 피해 7,645동 (Sentinel-2A+PlanetScope, Bloomberg) — 인도주의
- temp-085: 이란 핵시설 부분 생존 (Sentinel-2A, CNN) — 국방
- ent-evt-021: Kīlauea Episode 46 종료 (USGS HVO) — 자연재해 업데이트
- ent-evt-029: Mayon 분출 지속 (Himawari-9, VAAC) — 자연재해 업데이트
- ent-evt-041: Georgia 산불 진화 진전 (Landsat 8) — 자연재해 업데이트
- ent-evt-053: MethaneSAT Permian 메탄 비교 — 기후·환경 업데이트
- ent-evt-028: UNOSAT Gaza 피해 누적 — 인도주의 업데이트

### 미검증 의혹 섹션

- 해당 없음 (금일 신규 미검증 이벤트 없음)

## KG 시각화 범위

### 이벤트 노드 (10개)
- temp-081 (이란 미군기지 피해)
- temp-082 (마욘 화산재 매핑)
- temp-083 (아마존 금채굴)
- temp-084 (이란 민간 피해)
- temp-085 (이란 핵시설)
- ent-evt-021 (킬라우에아 Ep46 종료)
- ent-evt-029 (마욘 분출 지속)
- ent-evt-041 (조지아 산불)
- ent-evt-053 (MethaneSAT 퍼미안)
- ent-evt-028 (가자 UNOSAT)

### 위성 노드 (5개)
- Sentinel-2A, PlanetScope, Himawari-9, Landsat 8, MethaneSAT

### 기관 노드 (7개)
- Washington Post, PhilSA, PHIVOLCS, Amazon Conservation, Oregon State Univ, USGS HVO, UNOSAT

### 국가/지역 노드 (5개)
- US/Iran, PH, BR, US(Georgia), PS(Gaza)

### 인과 관계 (특수 엣지)
- temp-081 → triggeredBy → temp-084 (군사 공격 → 민간 피해 인과)

### 총 약 27개 노드, 40개 엣지 → Mermaid 그래프 + 도메인별 세부

## 보고서 구성 방향

### 1순위: 이란 위성 피해 평가 (최고 영향 — 국방+인도주의 복합)
- temp-081: 미군기지 228개 구조물 피해 — Copernicus+Planet 다중위성, WashPost 탐사보도
- temp-084: 민간 7,645동 피해 — Bloomberg 위성 분석, Oregon State 연구팀
- temp-085: 핵시설 부분 생존 — CNN 위성 조사, 전략적 의미
- **인과 관계 명시**: temp-081(공격 피해) → temp-084(민간 인프라 2차 피해), cascading_disaster 규칙

### 2순위: 자연재해 — 화산 (Disaster-Volcano)
- temp-082: PhilSA 마욘 화산재 위성 매핑 8,544ha (신규 정량 데이터)
- ent-evt-029: Mayon 5/6 VAAC 분출 지속 (업데이트)
- ent-evt-021: Kīlauea Episode 46 종료 (업데이트 — 9시간 분출 후 정지)

### 3순위: 자연재해 — 산불 (Disaster-Wildfire)
- ent-evt-041: Georgia 산불 봉쇄율 상승 (Hwy82 85%, Pineland 65%)

### 4순위: 인간활동 — 삼림벌채·광업 (Human Activity)
- temp-083: 아마존 금채굴 496,000ha — 2018 이후 위성 시계열 모니터링

### 5순위: 기후·환경 (Climate & Environment)
- ent-evt-053: MethaneSAT Permian Basin NM vs TX 메탄 강도 비교

### 6순위: 인도주의 (Humanitarian)
- ent-evt-028: UNOSAT Gaza 198,273 구조물 81% 손상 — 누적 규모 업데이트

### 카테고리 커버리지 체크
- [x] 자연재해: 4건 (화산 3, 산불 1)
- [x] 인간활동(개발/군사/산업): 4건 (이란 국방 3, 아마존 광업 1)
- [x] 기후·환경: 1건 (MethaneSAT 업데이트)
- [x] 농업·해양: 0건 신규 → "금일 신규 없음" 명시 (이전 CAS500-2 보고 완료)

## 다중위성 교차검증

| 이벤트 | 위성 1 | 위성 2 | 부스트 | 비고 |
|--------|--------|--------|--------|------|
| temp-081 | Sentinel-2A (ESA, 10m) | PlanetScope (Planet, 3m) | multiSatBoost +0.20 | 미군기지 피해 독립 교차검증 |
| temp-083 | Sentinel-2A (ESA, 10m) | PlanetScope (Planet, 3m) | multiSatBoost +0.20 | 아마존 삼림벌채 장기 모니터링 |
| temp-084 | Sentinel-2A (ESA, 10m) | PlanetScope (Planet, 3m) | multiSatBoost +0.20 | 이란 민간 피해 정량 평가 |

금일 3건 다중위성 교차검증 — 모두 Sentinel-2A + PlanetScope 조합. Copernicus(공공) + Planet(상업) 독립 사업자 교차검증으로 높은 신뢰도.

## 시간적 시리즈 분석

| 시리즈 | 현재 이벤트 | 이전 이벤트 | 상태 |
|--------|------------|------------|------|
| Kīlauea 분출 시리즈 | ent-evt-021 (Ep46 종료, 5/6) | ent-evt-070 (Ep46 시작, 5/5) | **종료** — 9시간 지속 후 정지 |
| Mayon 분출 시리즈 | ent-evt-029 + temp-082 (5/6 VAAC+PhilSA) | ent-evt-071 (5/5 VAAC) | **지속** — 장기 분출 계속 |
| Georgia 산불 시리즈 | ent-evt-041 (5/6 85%/65%) | ent-evt-072 (5/5 85%/50%) | **진화 진전** — Pineland 50→65% |
| MethaneSAT Permian | ent-evt-053 (5/6 NM vs TX) | 2026-05-04/src-015 | **지속** — 상원 조사 연계 |
| Gaza 피해 시리즈 | ent-evt-028 (5/6 198K 구조물) | 2026-05-02/src-020 | **지속** — 피해 규모 누적 확대 |
| 이란 공습 시리즈 | temp-081/084/085 (신규 진입) | — | **신규** — 위성 피해 평가 첫 보고 |

## 인과 관계 (Cascading Disaster)

```
temp-081 (이란 미군기지 공습 피해)
    │
    ├─── triggeredBy ───→ temp-084 (민간 인프라 피해 7,645동)
    │                      동일 지역, 동일 시간대
    │                      군사 공격의 민간 부수적 피해
    │
    └─── relatedTo ────→ temp-085 (핵시설 부분 생존)
                          동일 작전의 다른 표적
                          위성으로 생존 여부 평가
```

## 민감 정보 처리

- temp-081, temp-084, temp-085: 이란 내 미군기지·핵시설 좌표는 행정구역 단위(Isfahan/Bushehr 등)로 일반화
- 정밀 좌표 미기재 — 국방 민감정보 처리 규칙 적용
- 공개 출처(WashPost, Bloomberg, CNN)의 OSINT 분석만 활용
