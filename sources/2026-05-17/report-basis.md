# 2026-05-17 보고서 포함/제외 결정

## 포함 항목 (new + update = 4건)

| src-ID | 제목 | 태그 | 도메인 | 포함 근거 |
|--------|------|------|--------|-----------|
| src-001 | Stewart Trail Fire MN GOES-19 | new | dom-disaster | 신규 산불. 375ac, 34건물 파괴, 대피명령. GOES-19 위성 관측. |
| src-002 | Kilauea Ep47 종료 + Ep48 예보 | update | dom-disaster | Ep47 종료 확정 + Ep48 예보 5/22-25 = 핵심 업데이트. multiSatBoost. |
| src-003 | Bismarck Sea VAAC #23 FL120 | update | dom-disaster | FL280→FL120 현저한 하강 = 분출 강도 약화 신호. multiSatBoost. |
| src-004 | Everglades 80% contained | update | dom-disaster | 진압률 70%→80% 상승 + 풍향 전환 우려. multiSatBoost. |

## 제외 항목 (reported = 26건)

| src-ID | 제목 | 제외 근거 |
|--------|------|-----------|
| src-005~030 | (전일과 동일한 26건) | tag: reported — 유의미한 새 정보 없음. 추적 항목으로 목록 유지. |

## KG 시각화 범위
- 중심 노드: 4개 이벤트 (ent-evt-1001, ent-evt-202, ent-evt-701, ent-evt-501)
- 연관 위성: GOES-18/19, Sentinel-2A, Landsat 9, Himawari-9, VIIRS
- 연관 기관: USGS HVO, VAAC Darwin, CIMSS
- 연관 현상: wildfire, volcanic_eruption
- 총 노드: ~15개 (단일 그래프 적합)

## 보고서 구성 방향
- **자연재해 중심:** 금일 포함 4건 모두 dom-disaster
- **한반도 GeoFocus:** 직접 신규/업데이트 없음. 추적 항목(NLL 어선, CSIS BP 영변/소해/신포)만 추적 테이블에 언급.
- **다중 위성 교차검증:** Kilauea (S2A+L9), Bismarck Sea (Himawari+VIIRS), Everglades (GOES+VIIRS) — 3건
- **미검증 의혹:** 없음 (모든 new/update에 위성 출처 있음)
- **전후 비교:** 금일 신규/업데이트 중 해당 없음
- **4카테고리 의무:** 인간활동·기후환경·농업해양 — 금일 신규 없음 명시
