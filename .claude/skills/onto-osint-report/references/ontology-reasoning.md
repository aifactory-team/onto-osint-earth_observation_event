# 온톨로지 확장 & 추론 가이드

## 입력
- `sources/YYYY-MM-DD/entities.json` — 추출된 엔티티 및 관계
- `sources/YYYY-MM-DD/index.json` — 전체 태깅 현황
- `sources/YYYY-MM-DD/items/src-XXX.json` — `new`/`update` 항목만 개별 열람
- `ontology/schema.json` — 현재 온톨로지 스키마
- `ontology/instances.json` — 현재 엔티티 인스턴스
- `ontology/kg/cumulative.json` — 누적 지식그래프
- `reports/YYYY/MM/*.md` — 이전 N일 보고서

## Part 1: 온톨로지 확장

### 스키마 확장 판단 기준
기존 `schema.json`의 클래스/관계로 분류할 수 없는 엔티티/관계가 발견되면 스키마를 확장한다.

**새 클래스 추가 조건:**
- 기존 클래스의 하위 유형이 반복적으로 등장 (3건 이상)
- 기존 클래스로는 구별이 중요한 속성을 표현할 수 없음
- 하루 최대 `config.ontology.max_new_classes_per_day`개

**새 관계 유형 추가 조건:**
- 기존 관계 유형으로 표현할 수 없는 의미 있는 관계 발견
- 2건 이상의 소스에서 동일한 관계 패턴이 나타남
- 하루 최대 `config.ontology.max_new_relations_per_day`개

### 스키마 변경 기록
`schema.json`의 `changelog` 배열에 변경 사항을 기록한다:
```json
{
  "date": "YYYY-MM-DD",
  "action": "add_class|add_relation|modify_class",
  "target": "클래스/관계 ID",
  "reason": "변경 근거",
  "source_ids": ["근거가 된 소스 ID"]
}
```

### 인스턴스 업데이트
`instances.json`에 새 엔티티를 추가하거나 기존 엔티티 정보를 업데이트한다:
- `temp-XXXX` ID를 영구 ID(`ent-XXXX`)로 변환
- 기존 엔티티와 매칭되면 속성을 병합 (충돌 시 최신 정보 우선, 이전 정보 보존)
- `last_seen` 날짜를 업데이트
- `mention_count`를 누적

## Part 2: 지식그래프 구성

### 트리플 생성
엔티티와 관계를 (주어, 술어, 목적어) 트리플로 변환한다:

```json
{
  "subject": "ent-evt-001",
  "predicate": "observedBy",
  "object": "sat-sentinel2a",
  "source_id": "src-001",
  "date": "YYYY-MM-DD",
  "confidence": 0.9,
  "type": "explicit"
}
```

### 일별 KG 스냅샷: kg/YYYY-MM-DD.json
```json
{
  "date": "YYYY-MM-DD",
  "new_triples": [],
  "updated_triples": [],
  "inferred_triples": [],
  "stats": {
    "new_nodes": 5,
    "new_edges": 8,
    "inferred_edges": 3
  }
}
```

### 누적 KG 업데이트: kg/cumulative.json
- 새 트리플을 병합한다
- 기존 트리플과 충돌하면 출처와 함께 병기한다
- 삭제하지 않는다 (추적 가능성 보존)

## Part 3: 온톨로지 추론

### 추론 규칙 적용
`config.ontology.reasoning_rules`에 정의된 규칙을 적용한다.

EO 도메인 핵심 추론 규칙:
- `multi_satellite_confirmation` — 같은 이벤트가 2개 이상 독립 위성/센서로 관측되면 multiSatBoost +0.20
- `cascading_disaster` — 7일 내 동일 지역 재해 사슬(태풍→홍수, 지진→산사태)을 triggeredBy로 연결
- `temporal_progression` — 같은 위치·같은 현상의 시계열 관측을 partOfSeries로 연결
- `sensor_capability_match_*` — SAR/TIRS/trace_gas/hi-res 센서가 적합한 현상 관측 시 가산
- `official_source_trust` — 공식 우주기관·UN·재해기구 분석은 +0.15
- `korea_geo_focus` — 한반도 이벤트 +0.10
- `before_after_credibility` — 전후 비교 영상 보유 시 +0.10

### 추론 과정
1. 누적 KG의 모든 트리플을 대상으로 규칙을 매칭
2. 매칭된 패턴에서 새 트리플을 생성
3. 신뢰도 계산: `입력 트리플 신뢰도의 곱 × 규칙 가중치`
4. `config.ontology.confidence_threshold` 이상만 확정, 미만은 "잠정"
5. 추론 체인이 3단계 이상이면 신뢰도를 0.5배로 감쇠

### 추론 로그 (reasoning-log.md에 추가)
```markdown
## YYYY-MM-DD 추론 결과

### 추론 #1: multi_satellite_confirmation
- **입력:** (ent-evt-001, observedBy, sat-sentinel2a), (ent-evt-001, observedBy, sat-landsat9)
- **추론:** (ent-evt-001, multiSatBoost, +0.20)
- **신뢰도:** 0.95
- **상태:** 확정
```

## Part 4: 분석 산출물

### analysis.md
이전 보고서와 오늘의 새 정보를 교차 분석한다:
- 신규 소스별 중요도 평가 (높음/중간/낮음)
- 기존 보도 추적 (update 항목의 변경사항)
- 도메인별(Disaster/HumanActivity/Climate/AgriMarine/Defense/Humanitarian) 흐름 분석
- 온톨로지 변경 요약 (새 클래스/관계/엔티티)
- 추론 결과 요약 (다중 위성 교차검증, 재해 사슬, 센서-현상 적합성)

### report-basis.md
보고서에 포함/제외할 항목과 그 근거를 정리한다:
- 포함 항목: 소스 ID, 제목, 태그, 도메인, 포함 근거
- 제외 항목: 소스 ID, 제목, 제외 근거
- KG 시각화 범위: 오늘 보고서에 포함할 KG 노드/엣지 선정
- 보고서 구성 방향: 강조할 내용, 한반도 GeoFocus 항목, 다중 위성 검증 항목, 미검증 의혹 분리
