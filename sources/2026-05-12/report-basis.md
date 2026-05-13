# 2026-05-12 보고서 근거

## 포함 항목

| 소스 ID | 제목 | 태그 | 도메인 | 포함 근거 |
|---------|------|------|--------|----------|
| src-001 | Everglades Max Road 11,300ac 70% | update | Disaster | 면적·진화율 변동, 지하화재 상세 |
| src-002 | Kilauea Ep47 5/12-14 | update | Disaster | 예측 창 좁혀짐, 화염 강화 |
| src-003 | Mayon Day 128+ | update | Disaster | 지진 횟수 상세, Alert 3 지속 |
| src-004 | Mt Kupreanof ADVISORY/YELLOW | new | Disaster | 신규 화산 — TROPOMI SO2 8회 |
| src-005 | Great Sitkin SAR lava | update | Disaster | SAR 전천후 관측 |
| src-006 | Shishaldin SO2 | update | Disaster | TROPOMI 지속 관측 |
| src-007 | GA Pineland ~90% | update | Disaster | 번 밴 해제, 마무리 단계 |
| src-008 | Ibu VAAC 535 | update | Disaster | 5/12 최신 화산재 advisory |
| src-009 | 이라크 이스라엘 비밀기지 | new | Defense | 다중 위성 before/after, 주요 OSINT |
| src-010 | 오데사 호텔 Maxar | new | Humanitarian | 5/12 당일 고해상도 피해 영상 |
| src-011 | Antelope Reef 1490ac | new | Defense | 베트남 항의, 상세 구조물 분석 |

## 제외 항목

| 소스 ID | 제목 | 제외 근거 |
|---------|------|----------|
| src-012~030 | reported 태그 전체 | 금일 유의미한 신규 정보 없음 |

## KG 시각화 범위
- 오늘 보고서 포함 이벤트 11건 중심
- 노드 수 ~25개 (max 30 미초과)
- 신규 이벤트(evt-601/602/603) 강조
- 추론 관계(multiSatBoost, sarBoost, tracegasBoost, hiResBoost) 점선 표시

## 보고서 구성 방향
1. **오늘의 핵심 Top 5**: Kilauea Ep47 임박(1순위), 이라크 비밀기지(2), Antelope Reef(3), Mayon 128일(4), Everglades 지하화재(5)
2. **다중 위성 교차검증**: 6건 (역대 최다 수준)
3. **한반도 GeoFocus**: 금일 신규 없음 (동해 NLL·CSIS DPRK·CAS500-2 추적만)
4. **자연재해 우선**: 화산 5건 + 산불 2건 = 7건
5. **국방·안보**: 이라크 기지 + Antelope Reef (좌표 정밀도 일반화)
6. **인도주의**: 오데사 호텔 + Mayon GLIDE
7. **미검증 의혹**: Fuego 화산(GT, 위성 미확인)
