# Onto-OSINT-Earth-Observation-Event

> 위성영상으로 관측 가능한 **지구상 모든 이벤트**(자연재해·인간활동·기후·농업·해양·국방·환경)를 매일 자동으로 수집·구조화·요약하는 OSINT 시스템.
> [`onto-osint`](https://github.com/tykimos/onto-osint) 시스템을 포크하여 위성·EO(Earth Observation) 도메인에 맞게 설정한 인스턴스다.

---

## 1. 무엇을 해주는가

매일 아침, 다음 한 장의 보고서가 자동으로 갱신된다 — `reports/YYYY/MM/YYYY-MM-DD.md`.

| 섹션 | 내용 |
|------|------|
| 오늘의 핵심 (Top 5) | 영향규모·검증강도·재해도 종합 상위 5건 |
| 자연재해 | 산불·홍수·태풍·지진·화산·산사태 등 위성으로 확인된 재해 |
| 인간활동 | 삼림벌채·도시확장·광산·원유유출·산업사고·군사시설 등 |
| 기후·환경 | 빙하·해수면·메탄플룸·대기오염·NDVI 변화 |
| 농업·해양 | 작물 작황, 어업, 적조, 해상 선박 활동 |
| 위성·센서별 묶음 | Sentinel/Landsat/MODIS/Planet/Maxar/KOMPSAT 등 플랫폼별 |
| 다중 위성 교차검증 | 2개 이상 위성으로 확인된 고신뢰 이벤트 |
| 한반도 GeoFocus | 한국 영토·주변 해역 관측 이벤트 별도 정리 |
| 미검증 의혹 | 위성 출처 미확인 — 후속 검증 대기 |
| 지식그래프 시각화 | 이벤트–위성–센서–기관–지역의 관계망 (Mermaid) |
| 출처 목록 | 모든 이벤트의 원문 URL |

---

## 2. 모니터링 범위

### 1차 카테고리 — 자연재해 (Disaster)

산불, 홍수, 태풍·허리케인, 지진(피해 분석), 화산 분출, 산사태, 가뭄, 폭설, 한파, 적조

### 2차 카테고리 — 인간활동 (Human Activity)

삼림벌채, 도시확장, 대형 건설사업, 광산 개발, 농경지 변화, 원유 유출, 군사 시설/배치, 해상 선박 활동, 산업사고, 댐·저수지 변화

### 3차 카테고리 — 기후·환경 (Climate & Environment)

빙하 후퇴, 해수면 변화, 영구동토 융해, 메탄·CO₂ 플룸, 대기오염(NO₂·SO₂·미세먼지), 광공해, 지반 침하

### 4차 카테고리 — 농업·해양 (Agriculture & Maritime)

NDVI/식생지수 변화, 작황, 가뭄성 작물 피해, 어선 활동, 양식장 변화, 해양 쓰레기, 해류 이상

### Cross-cutting — 인도주의·고고학·국경

난민캠프 확장, 인도주의 위기, 국경 이상 활동, 고고학적 발견, 야간 광원(경제활동) 변화

### 핵심 출처 (custom_sites)

| 출처 | 다루는 내용 |
|------|------------|
| NASA Earth Observatory | 일별 영상·해설 (글로벌 모든 카테고리) |
| ESA Copernicus | Sentinel 시리즈 EO 결과·CEMS(긴급재해) |
| NOAA / NESDIS | 기상·해양·기후 위성 분석 |
| USGS (Landsat / Hazards) | 토지 변화·산불·화산 |
| KARI (한국항공우주연구원) | KOMPSAT/CAS500 한반도 관측 |
| JAXA EORC | ALOS-2(SAR)·GCOM 데이터 |
| FIRMS (NASA Fire) | 전 지구 화재 활성 (MODIS/VIIRS) |
| Planet Pulse | 상업 EO 분석 콘텐츠 |
| Maxar News | 고해상도 영상 분석 (재해·국방) |
| Sentinel Hub Stories | Copernicus 활용 사례 |
| UNOSAT | UN 위성영상 인도주의·재해 분석 |
| Disaster Charter | 국제 재해 위성영상 협조 |
| GFW (Global Forest Watch) | 삼림 손실 모니터링 |
| Climate TRACE | 위성·AI 기반 온실가스 배출 추적 |
| SkyTruth | 환경·해양 오염 OSINT |
| Bellingcat | 분쟁·국방 OSINT (위성영상 활용) |
| CSIS Beyond Parallel | 한반도 군사·인프라 위성 분석 |
| AllSource Analysis | 상업 OSINT 분석 리포트 |
| The War Zone (TWZ) | 군사 OSINT (위성·SAR 활용) |

---

## 3. 도메인 온톨로지 시드

`config/osint-config.json` → `ontology.seed_classes`에 다음이 정의되어 있다.

```
Entity
├── Event         — name, event_type, observation_date, lat, lon, severity, source_url, confidence, satellites_used, sensors_used, area_km2, ...
├── Satellite     — name, operator, orbit_type, revisit_days, resolution_m, sensor_types, mission_status
├── Sensor        — name, sensor_type (optical/SAR/thermal/multispectral/hyperspectral), bands, resolution_m
├── DataProduct   — name, level (L1/L2/L3), provider
├── Location      — name, country, region, admin_level, lat, lon
├── Country       — name, iso_code, region
├── Organization  — name, org_type (space_agency/commercial/defense/ngo/research/media)
├── Phenomenon    — name, category, observable_signature
└── Domain        — name (Disaster/HumanActivity/Climate/Agriculture/Maritime/Defense/Humanitarian)
```

핵심 관계:

```
Event   --observedBy-->     Satellite
Event   --usesSensor-->     Sensor
Event   --locatedIn-->      Location
Event   --inCountry-->      Country
Event   --analyzedBy-->     Organization
Event   --inDomain-->       Domain
Event   --manifests-->      Phenomenon
Event   --triggeredBy-->    Event   (예: 홍수 ← 태풍)
Event   --partOfSeries-->   Event   (시계열 모니터링)
Satellite --carriesSensor--> Sensor
Satellite --operatedBy-->   Organization
```

도메인 추론 규칙(`reasoning_rules`):

- `multi_satellite_confirmation` — 2개 이상 독립 위성/센서로 확인된 이벤트는 신뢰도 가산
- `cascading_disaster` — 같은 지역에서 시간차로 발생한 재해는 triggeredBy 추정 (태풍→홍수, 지진→산사태)
- `temporal_progression` — 같은 위치 시계열 관측은 partOfSeries
- `sensor_capability_match` — 센서 종류와 현상의 적합성 검증 (예: SAR=구름투과, TIRS=열원, S5P=가스플룸)
- `official_source_trust` — 정부 우주기관 발표는 신뢰도 가산
- `korea_geo_focus` — 한반도·주변 해역 이벤트는 우선순위 가산

---

## 4. 실행 방법

### 로컬 (Claude Code CLI)

```bash
cd onto-osint-earth_observation_event
claude "오늘 날짜로 위성영상 관측 이벤트 OSINT 보고서를 생성해줘"
```

Claude Code가 `CLAUDE.md`를 읽고, `.claude/skills/onto-osint-report/skill.md` 오케스트레이터를 따라 6단계 파이프라인을 실행한다.

### GitHub Actions (자동)

`.github/workflows/daily-osint-report.yml`이 매일 KST 08:00에 실행된다.

1. 이 리포지토리를 Fork (또는 aifactory-team 조직 내에서 직접 사용)
2. Settings → Secrets에 `CLAUDE_CODE_OAUTH_TOKEN` 추가
3. Actions → "Daily OSINT Report" → Run workflow (수동 테스트)

---

## 5. 디렉토리 구조

```
onto-osint-earth_observation_event/
├── config/
│   └── osint-config.json          # 위성영상 EO 도메인 설정 (이것만 수정하면 다른 도메인으로 포팅 가능)
├── ontology/
│   ├── schema.json                # 자동 진화하는 스키마
│   ├── instances.json             # 누적되는 위성·센서·기관·국가 인스턴스
│   ├── kg/
│   │   ├── YYYY-MM-DD.json        # 일별 KG 스냅샷
│   │   └── cumulative.json        # 누적 KG
│   └── reasoning-log.md
├── sources/YYYY-MM-DD/            # 파이프라인 중간 산출물
│   ├── search-results.json
│   ├── index.json
│   ├── items/src-XXX.json
│   ├── entities.json
│   ├── analysis.md
│   └── report-basis.md
├── reports/YYYY/MM/
│   └── YYYY-MM-DD.md              # 일일 EO 이벤트 다이제스트 (최종 산출물)
├── .claude/
│   ├── agents/                    # 4개 osint 에이전트 + 3개 docs 에이전트
│   └── skills/onto-osint-report/  # 오케스트레이터
├── .github/workflows/
│   └── daily-osint-report.yml
├── CLAUDE.md
└── README.md
```

---

## 6. 베이스 시스템에 대한 설명

이 프로젝트의 파이프라인·에이전트·추론 엔진 구조는 [`onto-osint`](https://github.com/tykimos/onto-osint) 본가에서 그대로 가져왔다.
온톨로지 진화·지식그래프 추론·에이전트 분리 등 일반 메커니즘에 대한 자세한 설명은 본가 README를 참고하라.

이 포크에서 손댄 것은 단 두 파일이다:

- `config/osint-config.json` — 도메인 시드(주제/카테고리/위성/센서/기관/온톨로지)
- `CLAUDE.md` — 도메인 규칙(위성 출처 검증, Sensor 가산, 다중위성 교차검증, 한반도 GeoFocus)

---

## License

MIT
