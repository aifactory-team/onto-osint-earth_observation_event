# 2026-05-31 온톨로지 분석

## 신규 이벤트 (4건)

### temp-evt-2001: 태풍 장미(Domeng) 태풍 격상
- **도메인:** Disaster (typhoon)
- **위치:** Philippine Sea (16.5°N, 130.0°E)
- **위성:** Himawari-9 (AHI)
- **분석:** 5/27 열대폭풍→5/29 강한 열대폭풍→5/30 태풍(120 kph). PAGASA 현지명 Domeng. PAR 6/1 이탈 예보. 필리핀 상륙 가능성 낮음. Himawari-9 정지궤도 위성 추적. 2026년 서태평양 4번째 열대저기압.
- **신뢰도:** 0.80 (officialBoost +0.15 PAGASA/JMA 공동 예보)

### temp-evt-2002: 중국 Hami ICBM 사일로 방어 네트워크 80+ 패드
- **도메인:** Defense (military_buildup)
- **위치:** Hami, Xinjiang, CN (42.8°N, 93.5°E — 정밀도 소수점 1자리)
- **위성:** WorldView-3 (0.31m), PlanetScope (3m) — Reuters 분석
- **분석:** 80+ 발사 패드, 장갑 벙커, 통신 노드, 비행장, 철도. 2개 팔각형 설치물 (140km, 230km from Hami silos). 이동식 미사일 발사대, 방공체계, 전자전 체계 지원. "unprecedented among nuclear-armed states." 4-5월 군사 훈련 확인. multiSatBoost +0.20 (WorldView-3 + PlanetScope 2위성). hiResBoost +0.15 (WorldView-3 ≤0.31m).
- **신뢰도:** 0.90

### temp-evt-2003: DPRK 최현급 구축함 서해 항해 + 남포 3번째 건조
- **도메인:** Defense (naval_movement)
- **위치:** West Coast, DPRK (38.7°N, 125.0°E — 정밀도 소수점 1자리)
- **위성:** WorldView-3 / Vantor 영상
- **분석:** NK Pro 5/31 위성영상 분석. 최대 현대 구축함 서해 항해 포착. 남포 조선소 3번째 최현급 건조 중. 미사일 발사 시험 연관 가능성. koreaBoost +0.10. hiResBoost +0.15.
- **신뢰도:** 0.80

### temp-evt-2004: 일본 군사 우주 확장 (미검증)
- **도메인:** Defense (military_buildup)
- **위치:** Tokyo, JP (35.7°N, 139.7°E)
- **위성:** 없음 (정책 발표 — 위성영상 직접 출처 아님)
- **분석:** satellite_unverified. MoD 브리핑: SOG 880인, FY2026 $1B 예산, Synspective SAR 콘스텔레이션 계약. 위성영상 자체를 사용하지 않은 정책 뉴스이므로 미검증 섹션 배치.
- **신뢰도:** 0.50 (satellite_unverified)

## 업데이트 이벤트 (13건)

1. **evt-202 Kilauea Ep48** — 5/29-31 예보 유지, spatter 북측 분출구, glow 양측, ADVISORY/YELLOW
2. **evt-1101 Canada wildfire** — 33,400+ 대피 유지, Norway House Cree Nation SOE, 군 투입, 연기 US/Europe
3. **evt-701 Bismarck Sea** — day 23+, Sentinel-2 5/22 활동 감소 vs 5/15, 부석 70km², 해저 플랫폼 성장
4. **evt-082 Mayon** — Day 145+, 287K+ 이재민, AL3, 우기 라하르 위험
5. **temp-evt-1401 Kanlaon** — AL2, 6-31 VQ/일, SO₂ 410-4,081 t/d
6. **evt-801 Bezymianny** — Orange, explosive continues
7. **evt-203 Great Sitkin** — WATCH/ORANGE, SAR lava dome east
8. **evt-204 Shishaldin** — ADVISORY/YELLOW, SO₂ elevated
9. **ent-evt-kharg Kharg Island** — 45km² oil spill, S1/S2/S3 three-sensor
10. **evt-092 Antelope Reef** — 1,490ac, approaching Mischief Reef
11. **temp-evt-1902 El Niño** — 82-98% WMO/IRI/ECMWF, SST +0.9°C Niño 3.4
12. **temp-evt-1901 Sentinel-3** — S3A manoeuvre #156 on 5/28
13. **temp-evt-1802 Sentinel-2** — CDSE catalogue delay 5/28

## 추론 결과

1. **multiSatBoost** — temp-evt-2002 (WorldView-3 + PlanetScope, 2기관) → +0.20
2. **multiSatBoost 유지** — evt-1101 (5위성 3기관), ent-evt-kharg (3위성 3센서), evt-701 (4위성 3기관)
3. **hiResBoost** — temp-evt-2002 (WV-3 0.31m), temp-evt-2003 (WV-3 0.31m) → +0.15 each
4. **koreaBoost** — temp-evt-2003 (DPRK KP) → +0.10
5. **officialBoost** — evt-202 (USGS), evt-701 (NASA EO), temp-evt-2001 (PAGASA/JMA) → +0.15 each
6. **thermalBoost** — evt-801 Bezymianny VIIRS thermal → +0.10
7. **tracegasBoost** — evt-204 Shishaldin TROPOMI SO₂ → +0.15
8. **temporal_progression** — temp-evt-2003 partOfSeries evt-022 (Choe Hyon-class 최초 관측 → 3번째 건조)
9. **cascading_disaster (잠정)** — Mayon eruption + 우기 → lahar risk (evt-082 triggeredBy 예상)
10. **severity_priority** — evt-1101 (2명 사망, 33K+ 대피), evt-082 (287K+ 이재민) → priorityBoost +0.20

## 스키마 변경
- 구조적 변경 없음 — 기존 클래스·관계·Phenomenon으로 충분
