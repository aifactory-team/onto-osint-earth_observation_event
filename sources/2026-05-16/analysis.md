# 2026-05-16 분석

## 신규 소스 중요도 평가

| ID | 제목 | 도메인 | 중요도 | 근거 |
|-----|------|--------|--------|------|
| src-003 | Planet Pelican First Light + 스웨덴 주권위성 | SatOps | 높음 | 50cm급 AI 위성 9기 운용 개시, 유럽 최초 주권 군사 EO 위성 |
| src-004 | UNEP MARS 메탄 석탄·폐기물 확대 | 기후·환경 | 높음 | 전 지구 메탄 모니터링 범위 확대, 23000+ 관측 축적, 석탄 부문 최초 체계적 DB |
| src-005 | 베트남 스프래틀리 216ha 확장 | 국방·안보 | 높음 | SCS 세력균형 변동 신호, PlanetScope+Sentinel-2 다중위성 교차검증, DVOR 비콘 설치 |
| src-006 | 필리핀 Thitu/Nanshan 건설 | 국방·안보 | 중간 | SCS 경쟁적 인프라 확장의 일환, Planet Labs 확인 |
| src-010 | VIIRS 야간조명 Nature 표지 | 기후·환경 | 중간 | 글로벌 광공해 변화 분석, Nature 수준 과학적 검증 |

## 업데이트 항목 변경사항

| ID | 변경 내용 | 의의 |
|-----|----------|------|
| src-001 | Bismarck Sea VAAC #15→#17, FL280→FL140 | 분출 고도 감소 — 약화 추세? 그러나 여전히 지속 |
| src-002 | Kilauea Ep47 종료, WATCH→ADVISORY | 분출 일시정지, 팽창 지속으로 재개 가능성 |
| src-007 | Max Road Fire 25,000ac 이상 확대 | 최종 억제 단계 진입 |
| src-008 | Pemex Cantarell 5월 초 SAR 여전히 유막 | 3개월+ 장기 오염, 해양 환경 심각 |
| src-009 | Bellingcat 레바논 5월 8일 영상 추가 | 지속적 파괴 문서화 |
| src-011 | Great Sitkin SAR 관측 용암 동쪽 이동 | 완만한 용암류 지속 |
| src-012 | Antelope Reef 1490ac 규모 유지 | 건설 지속 확인 |
| src-025 | CAS500-2 Pelican 3기 탑재 확인 | 한국 위성 탑재 상업 위성 최초 운용 |

## 도메인별 흐름 분석

### 자연재해 (Disaster)
- 화산: Bismarck Sea 해저화산이 핵심 — 약화 추세이나 계속. Kilauea 휴지기 진입. Great Sitkin SAR 관측 지속.
- 산불: Florida Everglades 사실상 진압 완료 직전. Georgia 완료.
- 홍수/기상: 금일 신규 없음.

### 인간활동 (Human Activity)
- Pemex 원유 유출 장기화가 핵심 — 3개월째 SAR 관측.
- 아마존 광산/삼림벌채 별도 변동 없음.

### 기후·환경 (Climate & Environment)
- **UNEP MARS 확대가 핵심 신규** — 석탄·폐기물 메탄 모니터링 체계화.
- VIIRS 야간조명 Nature 분석 신규.
- 빙하/해빙/MethaneSAT 별도 변동 없음.

### 농업·해양 (AgriMarine)
- CAS500-2 + Pelican rideshare로 한반도 해양관측 역량 간접 강화.
- 동해 어선 모니터링 별도 변동 없음.

### 국방·안보 (Defense)
- **남중국해 3중 경쟁**: 베트남 216ha 확장(신규) + 필리핀 Thitu/Nanshan(신규) + 중국 Antelope Reef(지속).
- 북한 영변/소해/신포 변동 없음.

### 인도주의 (Humanitarian)
- Bellingcat 레바논 파괴 계속 업데이트.
- 우크라이나 오데사 변동 없음.

## 온톨로지 변경 요약
- 새 클래스: 없음
- 새 관계 유형: 없음
- 새 엔티티: Pelican 위성, CAS500-2, SwAF, UNEP IMEO, AMTI, Darwin VAAC, 파푸아뉴기니, 스웨덴, 베트남, 필리핀, light_pollution 현상 (11건)

## 추론 결과 요약
- multiSatBoost: 4건 (UNEP/메탄, 베트남/스프래틀리, Bismarck Sea, Pemex)
- tracegasBoost: 1건 (UNEP TROPOMI 메탄)
- officialBoost: 2건 (UNEP IMEO, NASA)
- sarBoost: 1건 (Pemex Cantarell SAR 유막)
- partOfSeries: 2건 (SCS 건설 시리즈)
