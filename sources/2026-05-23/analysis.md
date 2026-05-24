# 2026-05-23 분석

## 신규 소스 중요도 평가

| 소스 | 중요도 | 근거 |
|------|--------|------|
| src-004 Canlaon VAAC #161 | 중간 | 필리핀 2번째 활화산 분출, 2024-2026 분출 시퀀스 일부, FL090 저고도, PHIVOLCS Alert Level 2. Himawari-9 AHI 관측. 에스컬레이션 가능성 모니터링 필요. |
| src-006 Sentinel-2A 연장 | 중간 | ESA 공식 -- 원래 2026-05 EOL이 12월까지 연장. MSI 다분광 관측 연속성 보장. 전 세계 EO 데이터 파이프라인(NDVI, burn scar, flood mapping 등)에 직접 영향. 좌표 없으므로 satops 사이드바 처리. |

## 기존 보도 추적 (UPDATE 항목)

| 소스 | 중요도 | 변경사항 | 분석 |
|------|--------|---------|------|
| src-001 Kilauea Ep48 | 높음 | 예보 창 5/22-26 -> 5/24-27 조정, tilt 10.5 -> 11.4urad 가속, both vents glowing(south brighter), SO2 1000-5000 tpd | 분출 임박 D-day(5/24). tilt 가속은 마그마 공급률 증가 시사. |
| src-002 Santa Rosa | 높음 | 59% -> 72% contained, mop-up phase 진입, 18,379ac, Torrey Pines 보존 확인, 저강도 잔불 정리 | 진압률 급개선(+13%p/일). 도서 생태계 위협 완화. 100% 진압까지 2-3일 예상. |
| src-003 Canada wildfire | 최고 | 첫 민간인 사망(2명, Lac du Bonnet), 대피 33,400+ 확대, Garden Hill FN 군대(CAF) 투입 | 인명피해 발생으로 재해 우선순위 최상위 격상. 원주민 커뮤니티 군사 지원은 인도주의 도메인 교차 확정. |
| src-005 Bezymianny | 중간 | VAAC #42, 23,000ft(7km) E 방향, 지속적 위성 관측 | VAAC advisory 시리즈 안정적 지속. FL230은 5/14 FL150 대비 상승이나 지속적 방출. |
| src-008 Mayon Day138+ | 중간-높음 | Day 138+ 지속 분출, 91,225명 영향, 스트롬볼리안 | 138일 연속 분출 장기화. 영향 인원 9만명 초과. |

## 도메인별 흐름 분석

- **자연재해**: 캐나다 산불이 인명피해(2사망)로 최고 우선순위. Kilauea Ep48 D-day(5/24) 임박. Santa Rosa 72% mop-up phase. Canlaon 신규 VAAC #161. Bezymianny VAAC#42 지속.
- **인간활동**: 변동 없음 (Pemex Cantarell, Kharg Island, Xingu 추적 유지)
- **기후·환경**: 변동 없음 (Hektoria/Arctic/Tanager-1/UNEP MARS 추적 유지)
- **농업·해양**: 변동 없음 (NLL 어선 추적 유지)
- **국방·안보**: 변동 없음 (SCS Antelope/Spratly, DPRK 추적 유지)
- **인도주의**: 캐나다 산불 인도주의 교차 진입 확정 (2명 사망, 33,400+ 대피, Garden Hill FN 군 투입). Mayon GLIDE 91,225명 지속.

## 온톨로지 변경 요약

- 스키마 구조적 변경 없음
- 인스턴스 추가: temp-evt-1401 (Canlaon), Sentinel-2A extension (satops), ent-loc-negros-island
- 인스턴스 업데이트: evt-202/1201/1101/801/082 (5건)
- 추론 12건 수행: multi_satellite_confirmation 2건, temporal_progression 3건, disaster_severity 1건, crossDomainLink 1건, sensor_capability_match 2건, official_source_trust 3건
