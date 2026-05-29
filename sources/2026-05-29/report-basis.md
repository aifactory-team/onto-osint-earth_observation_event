# 2026-05-29 보고서 기반

## 포함 결정

### 본문 포함 (15건)

| 소스 | 이벤트 | 도메인 | 판정 |
|------|--------|--------|------|
| src-001 | NASA EO Landsat 35년 토지교란 | Climate | **신규** — 본문 포함 |
| src-003 | Kilauea Ep48 5/28-30 | Disaster | **업데이트** — Top 5 |
| src-004 | 캐나다 산불 33K+ 대피 | Disaster→Humanitarian | **업데이트** — Top 5 |
| src-005 | Bismarck Sea day21+ | Disaster | **업데이트** — Top 5 |
| src-006 | Mayon 287K+ | Disaster | **업데이트** — Top 5 |
| src-007 | Kanlaon AL2 | Disaster | **업데이트** |
| src-008 | Bezymianny Orange | Disaster | **업데이트** |
| src-009 | Great Sitkin WATCH | Disaster | **업데이트** |
| src-010 | Shishaldin ADVISORY | Disaster | **업데이트** |
| src-011 | Santa Rosa 97% | Disaster | **업데이트** |
| src-012 | Kharg Island 45km² | HumanActivity | **업데이트** |
| src-013 | Antelope Reef 1490ac | Defense | **업데이트** |
| src-014 | 남레바논 46+ 마을 | Humanitarian | **보고됨** — 지속 추적 |
| src-015 | 압록강 교량 | HumanActivity | **보고됨** — KP GeoFocus |
| src-016 | 두만강 교량 | HumanActivity | **보고됨** — KP GeoFocus |

### 미검증 의혹 섹션 (2건)
| src-017 | DPRK 발사체 5/26 | Defense | 위성영상 미검증 |
| src-021 | AEI 한반도 종합 | Defense | 위성영상 미검증 |

### SatOps 섹션 (3건)
| src-002 | Sentinel-2 장애 5/28 | SatOps | **신규** |
| src-018 | Sentinel-1D 4위성 | SatOps | **보고됨** |
| src-019 | KOMPSAT-7 0.3m | SatOps | **보고됨** |

### 본문 제외 (1건)
| src-020 | NASA EO Dukono | Disaster | 전일 신규로 보고됨 — 중복 제외 |

## Top 5 선정 (신뢰도·영향규모 기준)

1. **Kilauea Ep48** — 0.95 + officialBoost. 분출 D-day 5/28-30 임박.
2. **Mayon 287K+** — 0.92 + priorityBoost. 이재민 급증 2.8x.
3. **캐나다 산불** — 0.95 + multiSatBoost + priorityBoost. 33K+ 대피.
4. **Bismarck Sea** — 0.97 + multiSatBoost. 신규 섬 형성 가능.
5. **NASA EO Landsat 35년** — 0.92 + officialBoost. 신규 Nature Geoscience 논문.

## 도메인별 커버리지

- 자연재해: 10건 ✓
- 인간활동: 3건 ✓
- 기후·환경: 1건 ✓
- 농업·해양: 0건 → 보고서에 "금일 신규 없음" 명시 ✓
- 국방·안보: 3건 ✓
- 인도주의: 1건 ✓

## 한반도 GeoFocus
- 압록강 교량 (보고됨)
- 두만강 교량 (보고됨)
- KOMPSAT-7 (보고됨)
- DPRK 발사체 5/26 (미검증)
