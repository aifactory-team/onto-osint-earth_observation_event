# 2026-06-04 온톨로지 분석

## 1. 신규 엔티티 (New Entities)

### temp-evt-2401: Israel 40+ military posts Gaza (Al Jazeera 위성 분석)
- **유형:** Event
- **도메인:** Defense (dom-defense) + Humanitarian (dom-humanitarian, cross-domain)
- **현상:** military_buildup (phen-military) + infrastructure_damage (phen-infra-damage)
- **위치:** Gaza Strip (31.4N, 34.4E) -- ent-loc-006 재사용
- **국가:** PS (co-ps)
- **위성:** PlanetScope (Planet Labs), WorldView-3 (Maxar/Vantor)
- **기관:** Al Jazeera Open Source Unit (org-aljazeera)
- **전후비교:** true (before/after imagery)
- **신뢰도 산정:**
  - 기본: 0.80 (Al Jazeera OSINT -- 독립 분석 기관 수준)
  - hiResBoost: +0.15 (WorldView-3, 0.31m 해상도 -- 군사 시설 식별 최적)
  - multiSatBoost: +0.20 (PlanetScope + WorldView-3, Planet != Maxar/Vantor 독립 운영자)
  - baCredibilityBoost: +0.10 (before/after 위성영상 가용)
  - analystBoost: +0.10 (Al Jazeera Open Source Unit)
  - **최종: 0.95 (cap)**
- **분석:** Al Jazeera 위성영상 OSINT 분석으로 가자지구 내 이스라엘 군사 거점 40개 이상 확인. 이 중 8개는 2024년 1월 휴전 이후 신설. PlanetScope(3m)로 광역 거점 분포 파악, WorldView-3(0.31m)로 개별 구조물/차량 식별. 도메인 이중 분류: dom-defense(military_buildup 거점 건설) + dom-humanitarian(infrastructure_damage 교차 관점). 기존 temp-evt-2201(UNOSAT 가자 197,000건 피해 평가)과 공간적 중첩이나 분석 주체/관점 상이하여 별도 이벤트 유지.

## 2. 주요 업데이트 엔티티 -- 13건

### temp-evt-2001: TS Jangmi -> 일본 본토 상륙 확정 (MAJOR UPDATE)
- Wakayama 6/3 상륙. 23명 부상, 57가옥 파괴, 900편 항공편 취소.
- **Tokyo Level 4 대피경보 최초 발령** -- 도쿄 기상관측 역사상 전례 없는 경보 수준.
- cascading_disaster **확정** (이전 잠정 -> 확정): 홍수/산사태 실제 발생 확인. 신뢰도 0.70 -> 0.85.
- priorityBoost +0.20 (인명피해/인프라 파괴)
- officialBoost +0.15 (JMA 공식)
- thermalBoost +0.10 (Himawari-9 AHI)
- **최종 신뢰도: 0.90**

### evt-1101: 캐나다 산불 -> 400+ fires, AQ 악화 (MAJOR UPDATE)
- 400+ 화재 활성. AQ 'very unhealthy' Minnesota로 미국 대기질 악화 확산.
- 27,000+ 대피 3개 주. NOAA NESDIS 공식 보고 지속.
- 5위성 3기관 multiSat 유지 (GOES-18 + VIIRS + TROPOMI + OMPS + EarthCare).
- **최종 신뢰도: 0.95**

### evt-202: Kilauea -> ADVISORY/YELLOW (하향)
- WATCH/ORANGE -> ADVISORY/YELLOW 하향. 분출 활동 감소.
- Ep49 10-15일 후 예보 (6/14-19 window). 재팽창(reinflation) 지속.
- temporal_progression: Ep48 -> Ep49 시리즈 지속.
- officialBoost (USGS HVO).
- **최종 신뢰도: 0.90** (0.95에서 0.90으로 하향 -- paused/downgrade 상태)

### evt-701: Bismarck Sea -> Day 27+, 분출 감소
- 분출 감소 추세이나 지속. Rabaul Volcano Observatory 현장 보고.
- 5위성 multiSat 유지.
- **최종 신뢰도: 0.95**

### temp-evt-1902: El Nino -> WMO 80% Jun-Aug
- WMO 80% 확률 Jun-Aug El Nino. 허리케인 시즌 개막 시 활동 0건 -- 억제 신호.
- **최종 신뢰도: 0.90**

### temp-evt-2002: Hami ICBM -> Reuters/NBC 상세 보도
- 80+ pads, 2개 팔각형 시설, C3 인프라, 광섬유 네트워크 상세.
- multiSatBoost 유지 (WorldView-3 + PlanetScope).
- hiResBoost +0.15.
- **최종 신뢰도: 0.95**

### evt-082: Mayon -- 지속 분출
### evt-801: Bezymianny -- 추적 지속
### evt-203/204: Great Sitkin/Shishaldin -- 변동 없음
### temp-evt-1401: Kanlaon -- AL2 지속
### temp-evt-2203: Sangay/Reventador -- 분출 지속
### evt-1201: Santa Rosa -- 추적 지속 (97%, 6/6 종결 예정)

## 3. 추론 결과 요약

| 추론 규칙 | 건수 | 대상 |
|-----------|------|------|
| multi_satellite_confirmation | 5건 (신규 1 + 유지 4) | temp-evt-2401(신규), evt-701, evt-1101, temp-evt-2002, ent-evt-kharg |
| official_source_trust | 4건 | evt-202(USGS), temp-evt-2001(JMA), evt-1101(NOAA), evt-202(HVO) |
| temporal_progression | 3건 | evt-202(Ep49), evt-701(day27+), temp-evt-2001(경로 완료) |
| cascading_disaster | 1건 확정 | temp-evt-2001 -> flooding/landslides JP 확정(0.85) |
| sensor_capability_match | 4건 | temp-evt-2401(hiRes), temp-evt-2001(thermal), temp-evt-2002(hiRes), evt-202(thermal) |
| disaster_severity_priority | 2건 | temp-evt-2001(23 injuries), evt-1101(27K evacuated) |
| before_after_credibility | 1건 신규 | temp-evt-2401(Gaza before/after) |
| analyst_org_trust | 1건 신규 | temp-evt-2401(Al Jazeera OSU) |
| korea_geo_focus | 0건 신규 | 기존 5건 유지 |

## 4. 도메인 트렌드 분석

### 4.1 자연재해 -- 고밀도 동시 다발
- **태풍 Jangmi 완료:** 일본 본토 상륙 후 열대저기압 약화. Tokyo Level 4 최초 발령은 기후 변화 시대 극한기상의 신호. cascading_disaster 확정.
- **화산 7건 동시 추적:** Kilauea(US), Bismarck Sea(PG), Mayon(PH), Bezymianny(RU), Great Sitkin(US), Shishaldin(US), Kanlaon(PH), Sangay/Reventador(EC). 역대 최다 동시 추적 상태.
- **캐나다 산불 에스컬레이션:** 400+ fires로 수 주간 증가 추세. 미국 대기질까지 영향. 5위성 교차검증 유지.

### 4.2 인간활동/국방 -- 신규 이벤트 주목
- **Gaza 군사거점 40+:** 금일 유일한 신규 이벤트. 도메인 이중 분류(Defense + Humanitarian).
- **Hami ICBM 상세화:** Reuters/NBC 보도로 80+ pads, C3 인프라 구체화. 기존 multiSat 유지.

### 4.3 기후환경 -- El Nino 확정 국면
- WMO 80% Jun-Aug. 허리케인 시즌 억제 신호. Super El Nino 가능성 지속.

### 4.4 농업해양 -- 금일 신규 없음
- El Nino 교차 도메인으로 간접 커버. 보고서에 "금일 신규 없음" 명시.

### 4.5 한반도 GeoFocus -- 5건 유지
- DPRK 구축함(2건), 압록강 교량, 두만강 교량, DPRK 발사체(미검증) -- 변동 없음.

## 5. 스키마 변경: 없음

기존 클래스, 관계, Phenomenon으로 금일 모든 이벤트 커버 가능. 신규 클래스/관계 불필요.

## 6. 인스턴스 변경: 없음

- Al Jazeera Open Source Unit은 기존 org-aljazeera(Al Jazeera Digital Investigations)와 동일 기관으로 취급. 별도 인스턴스 추가 불필요.
- Gaza Strip은 ent-loc-006으로 기존 추적 중.
- 모든 위성(PlanetScope, WorldView-3), 국가(PS), 현상(military_buildup, infrastructure_damage)은 기존 인스턴스로 매핑.
