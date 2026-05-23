# 2026-05-23 분석

## 신규 소스 분석
| 소스 | 중요도 | 근거 |
|------|--------|------|
| src-004 Canlaon VAAC #161 | 중간 | 필리핀 2번째 활화산 분출, 기존 2024-2026 시퀀스 일부, FL090 저고도 |
| src-006 Sentinel-2A 연장 | 중간 | ESA 공식 — 원래 2026-05 EOL이 12월까지 연장. EO 데이터 연속성 보장 |

## 업데이트 분석
| 소스 | 중요도 | 변경사항 |
|------|--------|---------|
| src-001 Kilauea Ep48 | 높음 | 예보 창 5/22-26→5/24-27 조정, tilt 10.5→11.4μrad, 분출 임박 D-1~D+4 |
| src-002 Santa Rosa | 높음 | 44%→59% 진압률 대폭 개선, Torrey Pines 보존 확인, 저강도 잔불 |
| src-003 Canada wildfire | 최고 | 첫 민간인 사망(2명, Lac du Bonnet), 33,400+→확대, Garden Hill FN 군대 투입 |
| src-005 Bezymianny | 중간 | VAAC #42, 23,000ft(7km) E 방향, 지속적 위성 관측 |

## 도메인별 흐름
- **자연재해**: 캐나다 산불이 인명피해로 최고 우선순위. Kilauea Ep48 D-day 임박. Canlaon 신규 VAAC.
- **인간활동**: 변동 없음 (Pemex Cantarell, Kharg Island, Xingu 추적 유지)
- **기후·환경**: 변동 없음 (Hektoria/Arctic/Tanager-1/UNEP MARS 추적 유지)
- **농업·해양**: 변동 없음 (NLL 어선 추적 유지)
- **국방·안보**: 변동 없음 (SCS Antelope/Spratly, DPRK 추적 유지)
- **인도주의**: 캐나다 산불 인도주의 교차 진입 (33,400+ 대피, 2명 사망)

## 온톨로지 변경
- 스키마 구조적 변경 없음
- 인스턴스 추가: temp-evt-1401 (Canlaon), co-ca (Canada) 추가 필요
- 추론 6건 수행 (multi_satellite_confirmation 1건, temporal_progression 4건, disaster_severity 1건)
