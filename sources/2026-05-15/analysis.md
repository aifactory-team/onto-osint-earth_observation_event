# 2026-05-15 분석

## 신규 소스 중요도 평가

| ID | 제목 | 태그 | 도메인 | 중요도 | 근거 |
|----|------|------|--------|--------|------|
| src-001 | Kilauea Ep47 분수 분출 9h → 종료, WATCH→ADVISORY | update | Disaster | **높음** | Ep47 완결. 분수 분출 → 종료 → 경계수준 2단계 하향. 전일 "전조 오버플로우"에서 극적 전환. |
| src-002 | Bismarck Sea FL280 (8500m) VAAC #15 | update | Disaster | **높음** | FL140→FL280 하루 만에 2배 상승. 분출 강도 급격 증가. 항공 위험 확대. |
| src-003 | NASA EO Aniak 얼음 해빙·홍수 Landsat 9 | new | Disaster | **중간** | NASA EO Image of the Day. before/after 제공. 아이스잼 → 홍수 메커니즘. |
| src-004 | Sentinel-2A Extension 2026년 말 연장 | new | SatOps | **중간** | ESA 공식 발표. Sentinel-2 콘스텔레이션 운영 연속성 확보. |
| src-011/029 | Bellingcat 남레바논 인터랙티브 맵 | new | Humanitarian | **높음** | 전일 기사 + 금일 인터랙티브 맵 공개. before/after PlanetScope 시계열. 인도주의 OSINT 핵심. |

## 기존 추적 항목 업데이트

| 이벤트 | 변화 | 영향 |
|--------|------|------|
| Kilauea Ep47 | 전조 오버플로우 → 분수 분출 9h → **종료**. WATCH→ADVISORY | 분출 사이클 완료. 향후 Ep48 가능성 모니터링 |
| Bismarck Sea 해저화산 | FL140→**FL280** | 분출 강도 급격 증가. 1주+ 지속. 해저화산으로는 이례적 고도 |
| Everglades Max Road | 70%→**80%** contained | 10% 개선. 이탄층 지하화재 지속 |
| Georgia Pineland | 90% contained, **번밴 해제** | 주 전역 번밴 해제. mop-up 단계 |
| Bezymianny | VAAC advisory #3 FL150 지속 | 안정적 분출 지속 |
| Great Sitkin | WATCH/ORANGE 지속, SAR 유일 | 변동 없음 |
| Shishaldin | ADVISORY/YELLOW SO2 지속 | 변동 없음 |
| Mayon | Day 131 스트롬볼리안 | 변동 없음 |

## 도메인별 흐름

### Disaster (14건)
화산 동시 모니터링 **8+개** 지속 (역대급). Kilauea Ep47 완결은 단기적 정점 이후 하강. Bismarck Sea 급격 상승은 가장 우려되는 변화. 미국 남부 산불(Everglades/Pineland) 모두 진화 진전.

### Human Activity (4건)
Pemex 잔류오염 지속. Amazon/GFW 추적 항목 변동 없음.

### Climate & Environment (4건)
Harvard TROPOMI+GOSAT 메탄 연구, 북극 해빙, Hektoria 빙하 — 모두 추적 지속, 금일 신규 없음.

### Agriculture & Maritime (2건)
동해 NLL 어선, CAS500-2 커미셔닝 — 금일 신규 없음.

### Defense (3건)
이라크 기지, Antelope Reef, DPRK — 금일 신규 없음.

### Humanitarian (2건)
Bellingcat 인터랙티브 맵은 중요한 추가. 오데사 추적 지속.

## 온톨로지 변경

### 신규 엔티티
- **ent-loc-067**: Aniak, Alaska (US, 61.58°N, 159.53°W)
- **ent-evt-903**: Aniak 얼음 해빙·홍수 (NASA EO)
- **ent-evt-905**: 남레바논 Bellingcat 인터랙티브 맵 (PlanetScope before/after)

### 스키마 변경
- 없음 (기존 클래스/관계로 충분)

## 추론 요약
- **multi_satellite_confirmation**: 5건 유지 (Kilauea, Mayon, Everglades, Pineland, Bezymianny) + Bismarck Sea 신규 추가 → **6건**
- **temporal_progression**: Kilauea Ep47→종료, Bismarck Sea FL 상승, Everglades/Pineland 진화율 개선
- **officialBoost**: NASA EO Aniak(+0.15), USGS HVO Kilauea(+0.15), VAAC Darwin Bismarck(+0.15)
- **baCredibilityBoost**: Aniak before/after(+0.10), Bellingcat Lebanon before/after(+0.10)
