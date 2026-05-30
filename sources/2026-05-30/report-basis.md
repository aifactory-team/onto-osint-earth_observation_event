# 2026-05-30 보고서 작성 근거

## 포함 결정

### 신규 (3건) — 본문 포함
| ID | 제목 | 도메인 | 신뢰도 | 결정 | 근거 |
|----|------|--------|--------|------|------|
| src-001 | Sentinel-3 L1/L2 프로덕션 지연 | satops | 0.85 | 포함 (SatOps 섹션) | ESA 공식 공지, 위성 운영 이슈 |
| src-002 | El Niño 2026 WMO 60% | dom-agri-marine | 0.80 | 포함 (농업·해양 섹션) | WMO 공식 발표, SST 위성관측 기반, 아시아 작물 영향 |
| src-003 | Sentinel-1A 데이터 유실 5/24 | satops | 0.85 | 포함 (SatOps 섹션) | 5/19에 이어 반복 장애, SAR 연속성 영향 |

### 업데이트 (13건) — 본문 포함
| ID | 제목 | 도메인 | 신뢰도 | 결정 | 근거 |
|----|------|--------|--------|------|------|
| src-004 | Kilauea Ep48 5/29-31 | dom-disaster | 0.95 | 포함 | 예보 창 갱신, 15.8μrad |
| src-005 | Mayon Day 144+ | dom-disaster | 0.92 | 포함 | 287K+ 이재민, priorityBoost |
| src-006 | 캐나다 산불 33K+ | dom-disaster | 0.95 | 포함 | 5위성 multiSatBoost, 인명피해 |
| src-007 | Bismarck Sea day 22+ | dom-disaster | 0.97 | 포함 | 4위성 최고신뢰, 과학적 가치 |
| src-008 | Kanlaon AL2 | dom-disaster | 0.88 | 포함 | 화산재 800m, SO₂ 상승 |
| src-009 | Bezymianny Orange | dom-disaster | 0.85 | 포함 | 폭발적 분출, KVERT |
| src-010 | Great Sitkin WATCH | dom-disaster | 0.85 | 포함 | SAR 용암돔 동측 확장 확인 |
| src-011 | Shishaldin ADVISORY | dom-disaster | 0.78 | 포함 | SO₂ 지속, TROPOMI |
| src-012 | Dukono NASA EO | dom-disaster | 0.95 | 포함 | 52/일, Landsat 9 공식 |
| src-013 | Santa Rosa 97% | dom-disaster | 0.90 | 포함 | NASA Earthdata, 6/6 폐쇄 |
| src-014 | Kharg Island 45km² | dom-human | 0.90 | 포함 | 3위성 multiSatBoost |
| src-015 | Antelope Reef 1490ac | dom-defense | 0.92 | 포함 | CSIS AMTI, 군사 인프라 |
| src-016 | Bellingcat Lebanon | dom-humanitarian | 0.90 | 포함 (추적/reported) | before/after, 인도주의 |

### 보고됨 (7건) — 본문 제외, 추적 목록에 기재
| ID | 제목 | 결정 | 근거 |
|----|------|------|------|
| src-017 | 38 North DPRK | 추적 목록 | 변동 없음 |
| src-018 | KOMPSAT-7 | 추적 목록 | 변동 없음 |
| src-019 | CAS500-2 | 추적 목록 | 변동 없음 |
| src-020 | DPRK 발사체 | 미검증 의혹 섹션 | satellite_unverified |
| src-021 | Sentinel-1D | 추적 목록 | 보고됨 |
| src-022 | Hunga Tonga TROPOMI | 추적 목록 | 보고됨 |
| src-023 | NASA EO Dukono | 추적 목록 | 전일 신규 보고 |

## 배치 순서

1. 오늘의 핵심 (Top 5): Kilauea > 캐나다 산불 > Bismarck Sea > Mayon > El Niño
2. 다중 위성 교차검증: 3건 유지
3. 한반도 GeoFocus: 추적 4건, 신규 0건
4. 자연재해: 10건 (화산 8 + 산불 2)
5. 인간활동: 1건 (Kharg + 교량 추적)
6. 기후·환경: 0건 신규 (전일 보고)
7. 농업·해양: 1건 신규 (El Niño)
8. 국방: 1건 (Antelope Reef)
9. 인도주의: 1건 (Bellingcat Lebanon 추적)
10. 센서·플랫폼별 묶음
11. 전후 비교
12. 미검증 의혹: 1건 (DPRK 발사체)
13. SatOps: 2건 신규 + 추적
14. KG 시각화
15. 추론·분석·출처
