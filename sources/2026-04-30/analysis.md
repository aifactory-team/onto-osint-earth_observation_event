# Analysis — 2026-04-30 위성영상 관측 이벤트 분석

## 신규 소스별 중요도

| 소스 | 제목 | 도메인 | 중요도 | 근거 |
|------|------|--------|--------|------|
| src-001 | Yongbyon UEP 완공 (CSIS BP) | Defense | 높음 | 한반도 GeoFocus + IAEA Grossi 검증 + WV-3 hi-res |
| src-002 | RFA Yongbyon 4월 후속 | Defense | 높음 | src-001 update — 4월 15일 차량 관측 |
| src-003 | Sohae 마을 철거 (38 North) | Defense | 높음 | KP 발사장 확장 |
| src-004 | Piton de la Fournaise (NASA) | Disaster | 높음 | TIRS + 화산 high severity + before/after |
| src-005 | Kilauea Episode 44 InSAR | Disaster | 높음 | InSAR 12.5cm + 분출 |
| src-006 | GFW Tropical Forest Loss 2025 | HumanActivity | 높음 | 글로벌 GFW/UMD 4월 29일 발표 |
| src-007 | Antelope Reef (FDD) | Defense | 높음 | 인공섬 6.11 km² + Sentinel-2 다중 |
| src-008 | Bellingcat Iran PWTT | Humanitarian | 높음 | SAR PWTT 도구 |
| src-009 | UNOSAT 가자 평가 | Humanitarian | 높음 | 1500+ 건축물 파괴 |
| src-010 | Hektoria 빙하 붕괴 | Climate | 높음 | 역대 최단기 후퇴 |
| src-011 | Climate TRACE v5.5.0 | Climate | 중간 | 글로벌 배출 추적 |
| src-012 | TROPOMI 메탄 추세 | Climate | 높음 | TROPOMI+GOSAT 다중 |
| src-013 | Sinlaku 슈퍼태풍 | Disaster | 높음 | 4월 슈퍼태풍 |
| src-014 | Vaianu Cat 3 | Disaster | 높음 | 남태평양 |
| src-015 | 한반도 산불 4/26 | Disaster | 낮음 | **위성 미검증** — 미검증 의혹 분리 |
| src-016 | KOMPSAT-7 운용 시작 | AgriMarine | 중간 | 한반도 GeoFocus |
| src-017 | Maxar 우크라이나 GEGD 재개 | Defense | 중간 | 보도자료성 cap 0.7 |
| src-018 | ICEYE Sri Lanka Ditwah | Disaster | 높음 | SAR 홍수 매핑 |
| src-019 | Sentinel-1 GFM (CEMS) | Disaster | 중간 | 운영 인프라 |
| src-020 | SkyTruth Cerulean | HumanActivity | 중간 | 글로벌 오일 슬릭 |

## 도메인별 흐름 분석

### Disaster (자연재해) — 7건
- 화산 2건 (Piton de la Fournaise, Kilauea) — Landsat 9 TIRS + COSMO-SkyMed CSG.
- 태풍/사이클론 3건 (Sinlaku, Vaianu, Ditwah) — Himawari-9 + GOES-18 + ICEYE SAR.
- 홍수 2건 (Sri Lanka, CEMS GFM) — Sentinel-1 SAR.

### HumanActivity — 2건
- 글로벌 열대 원시림 손실 (4.3M ha 2025).
- 해상 오일 슬릭 자동 탐지 (Cerulean).

### ClimateEnvironment — 3건
- Hektoria 빙하 다중 위성 시계열.
- TROPOMI 메탄 (TROPOMI+GOSAT).
- Climate TRACE v5.5.0.

### AgricultureMaritime — 1건
- KOMPSAT-7 한반도 정밀 관측 운용.

### Defense — 5건
- 영변 UEP, Sohae, Antelope Reef, Maxar Ukraine, Bellingcat Iran.

### Humanitarian — 2건
- UNOSAT Gaza, Bellingcat Iran PWTT.

## 온톨로지 변경 요약

- 새 Phenomenon 1건 (phen-infra-damage), 새 Country 8건, 새 Satellite 4건, 새 Organization 2건, 새 Event 19건, 새 Location 7건.
- config 한도 준수 (클래스 0/3, Phenomenon 1, 관계 0/5).

## 추론 결과 요약

- 다중 위성 교차검증 9건 / 센서-현상 적합성 12건 / 공식 출처 7건 / 한반도 GeoFocus 4건 / 재해 우선순위 5건 / 전후 비교 8건.
- 평균 신뢰도 0.89, 확정 43건 / 잠정 2건.

## 한반도 GeoFocus 특이사항

- KP: 영변 UEP 완공 + Sohae 마을 철거 — 다중 상업 위성 교차검증.
- KR: KOMPSAT-7 운용 시작 (2025-12-02 발사, 2026 상반기 영상). KR 산불 4/26은 위성 미검증 → 미검증 의혹.
