# 2026-05-12 분석

## 신규 소스 중요도 평가

| 소스 | 도메인 | 중요도 | 근거 |
|------|--------|--------|------|
| src-004 Mt Kupreanof ADVISORY/YELLOW | Disaster | 중간 | 신규 화산 불안 — TROPOMI SO2 위성 관측 8회. 아직 분출 아님이나 마그마 관입 확인 |
| src-009 이라크 이스라엘 비밀기지 | Defense | 높음 | 위성영상 OSINT 대표 사례 — 다중 위성(PlanetScope+WV-3) before/after. Al Jazeera 5/12 발행 |
| src-010 오데사 호텔 피격 Maxar | Humanitarian | 높음 | 5/12 당일 Maxar 위성영상 수집 — 인프라 파괴 고해상도 문서화 |
| src-011 Antelope Reef 1490ac 베트남 항의 | Defense | 높음 | 역대 최대 SCS 인공섬 접근 + 외교 격화. 다중 위성(Sentinel-2+WV-3) |

## 기존 추적 이벤트 업데이트

| 이벤트 | 변경사항 | 신뢰도 |
|--------|----------|--------|
| Everglades Max Road (evt-501) | 11,000→11,300ac, 50→70% 진화, 지하 이탄화재 상세 | 0.90 |
| Kilauea Ep47 (evt-202) | 예측 창 5/12-14, 남측 분출구 화염 강화 | 0.90 |
| Mayon (evt-082) | Day 128+, 21 화산지진(14 tremor), Alert 3 유지 | 0.92 |
| Great Sitkin (evt-203) | SAR 용암류 + 소지진·낙석, 구름으로 광학 불가 | 0.85 |
| Shishaldin (evt-204) | SO2·지진·인프라사운드 지속 | 0.78 |
| GA Pineland (temp-001) | ~90% 진화, 번 밴 해제, Day 24 | 0.85 |
| Ibu (evt-504) | VAAC 535 FL070 May 12 | 0.80 |
| Antelope Reef (evt-092) | 1490ac 상세 + 베트남 항의 | 0.92 |

## 도메인별 흐름

### Disaster (자연재해)
화산 활동 집중: 알래스카 3개 화산(Great Sitkin WATCH, Shishaldin ADVISORY, **Kupreanof 신규** ADVISORY), 하와이 Kilauea Ep47 임박, 필리핀 Mayon 128일, 인도네시아 Ibu 지속. 산불은 Everglades 진화 진행(70%) + GA Pineland 마무리(~90%).

### HumanActivity (인간활동)
금일 신규 없음. Pemex 원유 유출·Amazon 금광·GFW 추적 지속.

### ClimateEnvironment (기후·환경)
금일 신규 없음. 북극 해빙·Hektoria 빙하·MethaneSAT 추적 지속.

### AgricultureMaritime (농업·해양)
금일 신규 없음. 동해 NLL 어선 추적 지속.

### Defense (국방·안보)
**이라크 이스라엘 비밀 군사기지**(src-009)가 금일 최대 방위 OSINT 이벤트. 위성영상(PlanetScope/WV-3)으로 1.5km 활주로·헬기·차량 확인. Operation Roaring Lion 지원 시설. Antelope Reef(src-011)은 베트남 공식 항의라는 외교 격화 신호가 추가됨.

### Humanitarian (인도주의)
**오데사 Grande Pettine 호텔 피격**(src-010) — Maxar 5/12 위성영상 고해상도 피해 확인. Mayon GLIDE 인도주의 대응 지속.

## 온톨로지 변경 요약
- 신규 국가: 이라크(IQ), 이스라엘(IL)
- 신규 Location: 3건 (Mt Kupreanof AK, Al-Anbar IQ, Odesa UA)
- 신규 Event: 3건 (Kupreanof, 이라크 기지, 오데사 호텔)
- 업데이트 Event: 8건

## 추론 결과 요약
- 다중 위성 교차검증: **6건** (Everglades, Kilauea, Mayon, GA Pineland, 이라크 기지, Antelope Reef)
- SAR 전천후 관측: 1건 (Great Sitkin)
- TROPOMI 가스 탐지: 2건 (Kupreanof, Shishaldin)
- 고해상도 식별: 2건 (이라크 기지 WV-3, 오데사 WV-Legion)
- 공식 기관 신뢰: 2건 (Kupreanof USGS, Kilauea USGS)
- 전후 비교: 2건 (이라크 기지, 오데사 호텔)
