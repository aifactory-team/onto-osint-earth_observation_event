# 2026-05-20 분석

## 중요도 평가

### 높음
- **Stewart Trail Fire 100% 진압** (src-001): 최종 소멸 — 추적 종료 대상. 면적 356ac 확정, 34건물 파괴. 원인 전력선.
- **Bismarck Sea 부석 뗏목 70km²** (src-004): 기존 FL120 화산재 하강 추세에서 신규 열수분출 단계로 전환. 부석이 해면 도달 = 분출구 상승. "10년래 최대 심해 해저분출" 평가. 항해 위험.

### 중간
- **Flanders Fire 대피 해제** (src-002): 진압 진전. 기상 호전(냉각·습도 상승)으로 소방인력 철수 시작. 면적 유지 ~1,700ac.
- **Kilauea Ep48 예보 창 확대** (src-003): 5/22-25→5/22-26 (1일 연장). 재팽창 감속. 모니터링 일부 오프라인.

### 낮음 (보고됨 — 변동 없음)
- 캐나다 MB/ON 산불 160+건, Kharg Island 유출, Great Sitkin, Mayon, Bezymianny, Shishaldin, Ibu 등 22건 기존 보도 반복.

## 도메인별 흐름

| 도메인 | 신규 | 업데이트 | 보고됨 | 주요 동향 |
|--------|------|----------|--------|----------|
| Disaster | 0 | 4 | 8 | Stewart 100% 진압 종료, Flanders 대피 해제, Kilauea Ep48 임박, Bismarck 부석 신국면 |
| HumanActivity | 0 | 0 | 3 | Kharg/Pemex/Xingu 변동 없음 |
| Climate | 0 | 0 | 4 | 북극해빙/Hektoria/MARS/Tanager 변동 없음 |
| AgriMarine | 0 | 0 | 1 | 동해 NLL 어선 변동 없음 |
| Defense | 0 | 0 | 5 | 남중국해/DPRK/MizarVision 변동 없음 |
| Humanitarian | 0 | 0 | 2 | 레바논/우크라이나 변동 없음 |

## 온톨로지 변경

금일 스키마 변경 없음. 인스턴스 업데이트만 수행:
- ent-evt-1001 containment 62→100%
- ent-evt-1101 evacuation_lifted true 추가
- ent-evt-202 ep48_forecast 범위 확대
- ent-evt-701 eruption_phase hydrothermal_pumice로 전환

## 추론 결과 요약

- **multi_satellite_confirmation**: Bismarck Sea (Himawari-9 + VIIRS + Sentinel-2A, 3개 독립 위성) → +0.20
- **multi_satellite_confirmation**: Kilauea (Sentinel-2A + Landsat 9) → +0.20 (기존 유지)
- **official_source_trust**: Kilauea (USGS HVO) → +0.15
- **thermalBoost**: Kilauea (TIRS) → +0.10
- **partOfSeries**: Flanders Fire → Stewart Trail Fire (동일 Minnesota 산불 기상 패턴)
