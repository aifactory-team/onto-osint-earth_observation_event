# 2026-05-16 보고서 근거

## 포함 항목 (new + update = 13건)

| ID | 제목 | 태그 | 도메인 | 포함 근거 |
|-----|------|------|--------|----------|
| src-001 | Bismarck Sea VAAC #17 FL140 | update | Disaster | 핵심 진행 중 이벤트, 다중위성 교차검증 |
| src-002 | Kilauea Ep47 종료·휴지 | update | Disaster | 주요 화산 상태 변동 |
| src-003 | Planet Pelican First Light 스웨덴 | new | SatOps | 신규 위성 운용 개시, 국방 의의 |
| src-004 | UNEP MARS 메탄 석탄·폐기물 확대 | new | Climate | 글로벌 메탄 모니터링 획기적 확대 |
| src-005 | 베트남 스프래틀리 216ha | new | Defense | 다중위성 교차검증, SCS 세력균형 |
| src-006 | 필리핀 Thitu/Nanshan | new | Defense | SCS 경쟁, Planet 확인 |
| src-007 | Florida Max Road Fire 25000ac | update | Disaster | 대형 산불 진압 추적 |
| src-008 | Pemex Cantarell 유출 3개월+ | update | Human | 장기 해양오염, SAR 확인 |
| src-009 | Bellingcat 레바논 May 8 영상 | update | Humanitarian | 인도주의 파괴 지속 문서화, before/after |
| src-010 | VIIRS 야간조명 Nature | new | Climate | NASA 공식, Nature 발표 |
| src-011 | Great Sitkin SAR 용암 | update | Disaster | SAR 관측 지속 |
| src-012 | Antelope Reef 1490ac | update | Defense | SCS 핵심 건설 추적 |
| src-025 | CAS500-2 + Pelican rideshare | update | AgriMarine | 한국 위성 관련, 한반도 관측 역량 |

## 제외 항목 (reported = 17건)

| ID | 제목 | 제외 근거 |
|-----|------|----------|
| src-013~030 | 이전 보고 항목 금일 변동 없음 | tag: reported — 보고서 포함 대상 아님 |

## KG 시각화 범위
- 핵심 이벤트 노드: 7건 (Bismarck Sea, UNEP MARS, Vietnam Spratly, Philippines Thitu, Pelican, Pemex, Bellingcat Lebanon)
- 위성/센서 노드: 8건 (Himawari-9, VIIRS, Sentinel-5P, MethaneSAT, PlanetScope, Sentinel-2A, Pelican, Sentinel-1A)
- 기관 노드: 5건 (Planet, UNEP IMEO, AMTI, Darwin VAAC, NASA)
- 현상 노드: 5건 (volcanic_eruption, methane_plume, construction, oil_spill, light_pollution)
- 총 노드: ~25개 (max_kg_nodes 30 이내)

## 보고서 구성 방향
1. **Top 5**: UNEP MARS 메탄 확대(multiSat+official+tracegas), 베트남 스프래틀리(multiSat+before/after), Bismarck Sea(multiSat), Pemex(multiSat+SAR), Bellingcat 레바논(before/after)
2. **다중 위성 교차검증**: 4건 강조
3. **한반도 GeoFocus**: CAS500-2 Pelican rideshare (간접), 동해 어선(reported이므로 추적 목록에만)
4. **미검증 의혹**: 0건 (금일 위성출처 미확인 이벤트 없음)
5. **before/after**: 베트남 스프래틀리, 필리핀 Thitu, Bellingcat 레바논
