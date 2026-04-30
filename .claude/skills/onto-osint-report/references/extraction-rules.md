# 추출 & 태깅 규칙

## 태그 정의

| 태그 | 의미 | 조건 |
|------|------|------|
| `new` | 신규 | 이전 소스에 동일 URL·유사 제목 없음 |
| `reported` | 보고됨 | 이전에 이미 보고된 동일 내용 |
| `update` | 후속보도 | 기존 사건의 후속이지만 유의미한 새 정보 포함 |

## 중복 판단 기준

1. **URL 일치** → `reported` (가장 확실한 기준)
2. **제목 유사도** — 핵심 키워드(이벤트명, 지명, 위성명) 80%+ 일치 → `reported`
3. **후속 보도 판단** — 동일 이벤트 + 새로운 위성·관측일·피해규모 → `update`

## 비교 범위

- 이전 N일(`config.project.lookback_days`)의 `sources/*/index.json`만 읽는다
- 개별 items 파일은 읽지 않음 (토큰 효율성)
- N일 이전 소스는 무시한다

## 엔티티 추출 규칙

### 엔티티 유형 (config의 seed_classes 기반)
- **Event** (이벤트): name, event_type, observation_date, lat, lon, country, severity
- **Satellite** (위성): name, operator, sensor_types
- **Sensor** (센서): name, sensor_type
- **DataProduct** (데이터제품): name, level, provider
- **Location** (지역): name, country, region, lat, lon
- **Country** (국가): name, iso_code
- **Organization** (기관): name, org_type
- **Phenomenon** (관측현상): name, category
- **Domain** (도메인): name

### 추출 원칙
- 각 소스(기사·분석)에서 언급된 모든 엔티티를 추출한다
- 기존 `ontology/instances.json`과 매칭하여 알려진 엔티티는 기존 ID를 연결한다
  - 위성 이름은 표기 변형(Sentinel-2, S2, Sentinel 2A 등)을 정규화하여 시드 ID와 매칭한다
- 새로운 엔티티는 임시 ID를 부여한다 (`temp-XXXX`)
- 엔티티 간 관계도 기사 문맥에서 추출한다
- **Event 추출 시 좌표(lat, lon) 또는 admin level을 반드시 시도한다** — 본문/캡션/메타데이터에서 가능한 한 추출

### 관계 추출 원칙
- 명시적 관계: 기사 본문에 직접 언급된 관계 (예: "Sentinel-2가 X 지역의 산불을 관측했다" → Event observedBy Sentinel-2)
- 암시적 관계: 같은 문장/단락에 공출현(co-occurrence)하는 엔티티 간 잠재적 관계
- 관계 유형은 config의 `ontology.seed_relations`를 기준으로 분류
- **observedBy / usesSensor / locatedIn / inCountry / analyzedBy / manifests / inDomain** 6개 핵심 관계는 가능한 한 모든 Event에 부여

## 출력 스키마

### index.json (경량 인덱스)
```json
{
  "date": "YYYY-MM-DD",
  "total": 25,
  "new": 8,
  "reported": 15,
  "update": 2,
  "items": [
    {
      "id": "src-001",
      "title": "기사 제목",
      "url": "https://...",
      "tag": "new",
      "related_report": null,
      "entity_count": 5
    }
  ]
}
```

### items/src-XXX.json (개별 소스 상세)
```json
{
  "id": "src-001",
  "title": "기사 제목",
  "url": "https://...",
  "snippet": "기사 요약 또는 발췌",
  "source_name": "매체명",
  "language": "ko",
  "discovered_date": "YYYY-MM-DD",
  "tag": "new",
  "related_report": null,
  "related_item": null,
  "tag_reason": "이전 N일 소스에 동일/유사 항목 없음",
  "entities": [
    { "id": "temp-001", "type": "Event", "name": "캘리포니아 산불 2026-04", "properties": { "phenomenon": "wildfire", "lat": 38.5, "lon": -120.5, "country": "US" } }
  ],
  "relations": [
    { "subject": "temp-001", "predicate": "observedBy", "object": "sat-sentinel2a" },
    { "subject": "temp-001", "predicate": "manifests", "object": "phen-wildfire" }
  ]
}
```

### entities.json (일별 추출 엔티티 종합)
```json
{
  "date": "YYYY-MM-DD",
  "entities": [
    {
      "temp_id": "temp-001",
      "matched_id": null,
      "type": "Event",
      "name": "캘리포니아 산불 2026-04",
      "properties": { "phenomenon": "wildfire", "country": "US", "lat": 38.5, "lon": -120.5 },
      "source_ids": ["src-001", "src-003"],
      "mention_count": 3
    }
  ],
  "relations": [
    {
      "subject": "temp-001",
      "predicate": "observedBy",
      "object": "sat-sentinel2a",
      "source_ids": ["src-001"],
      "confidence": 0.9
    }
  ],
  "stats": {
    "total_entities": 15,
    "new_entities": 8,
    "matched_entities": 7,
    "total_relations": 12
  }
}
```

## 원칙
- `reported` 태그 소스도 index + items에 기록한다 (추적 가능성 보존)
- `tag_reason`은 개별 items 파일에 구체적으로 작성한다
- `related_report`/`related_item`은 `reported`/`update` 태그에만 기록한다
- 엔티티 추출 실패 시에도 태깅은 반드시 수행한다
- **위성 식별 불가능한 이벤트**는 별도 플래그(`satellite_unverified: true`)를 부여 — Reporter가 별도 섹션으로 분리할 수 있도록
