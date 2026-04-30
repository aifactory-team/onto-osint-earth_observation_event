# Onto-OSINT-Earth-Observation-Event — 위성영상 관측 이벤트 일일 모니터

## Project Purpose
지구 어디에서든 **위성영상으로 관측 가능한 모든 이벤트**(자연재해·인간활동·기후·농업·해양·국방·환경)를 매일 자동으로 수집·구조화·요약한다.
`onto-osint`의 6단계 파이프라인(수집→추출→온톨로지→그래프→보고서→발행)을 그대로 사용하되, 도메인 특화 설정(`config/osint-config.json`)으로 위성영상 이벤트용 온톨로지를 시드한다.

## Domain Snapshot

| 항목 | 값 |
|------|-----|
| 도메인 정의 | **위성영상으로 관측 가능한 지구상 이벤트 전 영역** — 자연재해·인간활동·기후·농업·해양·국방·환경 |
| 1차 카테고리 (Disaster) | 산불, 홍수, 태풍·허리케인, 지진(피해), 화산 분출, 산사태, 가뭄, 폭설, 적조 |
| 2차 카테고리 (Human Activity) | 삼림벌채, 도시확장, 대형 건설, 광산 개발, 농경지 변화, 원유 유출, 군사 시설/배치, 해상 선박 활동, 산업사고 |
| 3차 카테고리 (Climate & Env) | 빙하 후퇴, 해수면 변화, 영구동토 융해, 메탄·CO₂ 플룸, 대기오염, 광공해, 지반 침하 |
| 4차 카테고리 (Cross-cutting) | 난민캠프, 인도주의 위기, 국경 활동, 고고학적 발견, NDVI/식생 변화 |
| 추적 대상 종류 | (a) Event(관측된 이벤트) (b) Satellite/Sensor(관측 플랫폼) (c) Organization(분석 주체) |
| 핵심 출처 | NASA Earth Observatory, ESA Copernicus, NOAA, USGS, KARI, JAXA, Planet Pulse, Maxar, Sentinel Hub, FIRMS, CEMS(Copernicus EMS), UNOSAT, GFW, Climate TRACE, SkyTruth, Bellingcat, AllSource Analysis, CSIS Beyond Parallel, The War Zone |
| 보고서 언어 | 한국어 (`report_language: ko`) — 단, 원문 인용은 영문 보존 |
| 룩백 기간 | 14일 (이전 보고서 대비 신규/후속 판별) |
| 글로벌 스코프 | 국가/지역 무관 — 단, 한국 영토·주변(동해·남중국해·DMZ·KOMPSAT 관측 우선) 가산점 |

## Pipeline Architecture

```
Phase 1        Phase 2         Phase 3          Phase 4        Phase 5          Phase 6
수집(Collect) → 추출(Extract) → 온톨로지(Onto) → 그래프(Graph) → 보고서(Report) → 발행(Publish)
    │              │               │                │              │                │
    ▼              ▼               ▼                ▼              ▼                ▼
search-        index.json      ontology/        kg/            YYYY-MM-DD.md    Git + Wiki
results.json   items/          schema.json      YYYY-MM-DD     (KG 시각화 포함)
                               instances.json   .json
```

## Directory Structure

```
config/
└── osint-config.json          # 위성영상 이벤트용 설정 (이 파일만 수정)

ontology/
├── schema.json                # 클래스(Event/Satellite/Sensor/Location/Organization/Phenomenon/Domain) + 관계
├── instances.json             # 알려진 위성·센서·기관·국가 인스턴스 누적
├── kg/
│   ├── YYYY-MM-DD.json        # 일별 KG 스냅샷
│   └── cumulative.json        # 누적 KG
└── reasoning-log.md           # 추론 로그

sources/YYYY-MM-DD/
├── search-results.json        # Phase 1
├── index.json                 # Phase 2
├── items/src-XXX.json         # Phase 2
├── entities.json              # Phase 2
├── analysis.md                # Phase 3
└── report-basis.md            # Phase 4

reports/YYYY/MM/
└── YYYY-MM-DD.md              # 최종 일일 위성영상 이벤트 다이제스트
```

## Agents & Skills

| 에이전트 | 참조 스킬 | Phase |
|----------|----------|-------|
| `.claude/agents/osint-collector.md` | `references/search-strategy.md` | 1 |
| `.claude/agents/osint-extractor.md` | `references/extraction-rules.md` | 2 |
| `.claude/agents/osint-reasoner.md` | `references/ontology-reasoning.md` | 3-4 |
| `.claude/agents/osint-reporter.md` | `references/report-format.md` | 5 |

오케스트레이터: `.claude/skills/onto-osint-report/skill.md`

## Domain Rules (이 프로젝트 특수 규칙)

- **위성 출처 검증 의무 (최상위 규칙)**: 모든 Event 인스턴스는 최소 1개의 `Satellite` 또는 `DataProduct`(예: Sentinel-2 L2A, Landsat-9 OLI, Planet SkySat)를 출처로 명시한다. 위성 식별 불가능한 보도(예: 일반 뉴스만 인용)는 신뢰도 0.5 미만으로 분류하고 보고서 본문에서 별도 "미검증 의혹" 섹션으로 분리한다.
- **추적 대상 4종 의무 커버**: 매 사이클마다 (a) **자연재해**, (b) **인간활동**(개발/군사/산업), (c) **기후·환경**, (d) **농업·해양** — 네 카테고리 모두 검색·수집한다. 한 카테고리라도 0건이면 보고서에 "금일 신규 없음" 명시.
- **Sensor 타입 별 Confidence 가산**:
  - SAR(합성개구레이다 — Sentinel-1, ICEYE, Capella, KOMPSAT-5): 구름 투과·야간 관측 가능 → `sarBoost +0.1`
  - 광학 고해상도(Maxar WorldView, Planet SkySat, KOMPSAT-3A, ≤1m): 인공구조물·차량 식별 → `hiResBoost +0.15`
  - 다분광(Sentinel-2, Landsat, MODIS): NDVI·NBR·NDWI 산출 → 환경/농업/산불에 가산
  - 열적외(Landsat TIRS, MODIS, VIIRS, Himawari): 화재·열원 검출 → 산불·화산에 가산
  - 초분광/온실가스(Sentinel-5P, MethaneSAT, EMIT): 메탄·CO₂·NOx 플룸 → 환경 카테고리 의무 사용
- **다중 위성 교차검증 가산**: 동일 이벤트가 2개 이상의 독립 위성·센서로 확인되면 `multiSatBoost +0.2` 적용 — 단일 출처 의존도를 낮춘다.
- **공식 우주기관 신뢰도 가산**: NASA/ESA/NOAA/KARI/JAXA/USGS/CEMS/UNOSAT/Disaster Charter 발표는 `officialBoost +0.15` (정부·국제기구 공식 채널).
- **상업 OSINT 신뢰도**: Planet, Maxar, BlackSky, Capella, ICEYE 등 상업 위성 사업자가 직접 발표한 분석은 `commercialBoost +0.1`. 단, 보도자료성 콘텐츠는 신뢰도 0.7 cap.
- **분석가/싱크탱크 신뢰도**: Bellingcat, AllSource, CSIS Beyond Parallel, Skytruth, Climate TRACE 등 독립 분석기관은 `analystBoost +0.1`. 단, 군사·정치적 결론은 교차검증 필요.
- **이벤트 좌표 의무**: 모든 Event는 최소 (lat, lon) 또는 admin 단위(국가·시·도)를 기록해야 한다. 좌표 없는 이벤트는 보고서에 포함하지 않는다.
- **카테고리·서브카테고리 매핑**: 모든 Event는 (Domain → Phenomenon) 트리에 매핑된다. 분류 모호 시 보수적으로 처리하고 신뢰도 0.5 미만으로 표시.
- **민감 정보 처리 (defensive scope)**: 군사·국방 카테고리 이벤트는 *공개 출처(OSINT)*에 한해서만 수집한다. 좌표·시간 정밀도가 작전 보안에 영향을 줄 수 있는 항목은 보고서에서 정밀도를 낮추거나 (lat, lon 소수점 1자리) 행정구역 단위로 일반화한다.
- **재해 우선순위**: 인명피해·인프라파괴를 동반하는 자연재해는 보고서 1순위 섹션에 배치한다.
- **GeoFocus 가산점**: 한반도(특히 KOMPSAT 관측 우선 지역) 및 동해/서해/남해 해역 이벤트는 `koreaBoost +0.1`.
- **scope.exclude 엄격 적용**: 위성영상과 무관한 일반 정치 뉴스, 우주기술 기업 인사·재무 뉴스, 마케팅성 출시 발표는 자동 제외 (`config/osint-config.json` `scope.exclude` 참조).

## Commit Convention
- 보고서 커밋: `report: daily eo-event update (YYYY-MM-DD)`
- 온톨로지 변경: `ontology: expand schema/instances (YYYY-MM-DD)`
- 구조/설정 변경: `chore: 설명`
- `git add sources/ reports/ ontology/`

## Rules
- 출처 URL 없는 이벤트는 보고서에 포함하지 않는다 (위성기관 공식 페이지, 분석기관 리포트, 언론 기사 중 1개 이상 필수)
- 동일 이벤트가 여러 매체에서 보도된 경우 대표 1개를 본문에, 나머지는 출처 목록에 모두 기재한다
- 보고서가 비어있더라도 파일은 생성한다 ("금일 위성영상 관측 신규 이벤트 특이사항 없음")
- 파이프라인 중간 산출물은 항상 생성한다
- 온톨로지 변경은 반드시 근거(reasoning-log)를 남긴다
- 지식그래프 시각화는 Mermaid 다이어그램으로 보고서에 포함한다
- 위성영상의 시계열·전후비교(before/after) 정보가 있으면 본문에서 명시한다
