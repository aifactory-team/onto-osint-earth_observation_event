# 2026-05-09 위성영상 관측 이벤트 분석

## 수집 통계
- 총 출처: 27건 (신규 7건, 업데이트 8건, 기보도 12건)
- 엔티티: 21건 (신규 12건, 기존 매칭 9건)
- 관계: 68건
- 위성 미확인: 1건 (Fuego GT)

## 이벤트 분석

### 신규 이벤트 (7건)

1. **PhilSA Mayon ashfall 작물피해 매핑** (ent-evt-207)
   - Sentinel-2A MSI 전후비교(before/after) 변화탐지
   - 1,039ha 벼 + 191ha 기타 작물, 총 8,544ha 화산재 피복
   - 교차 도메인: dom-agri-marine + dom-disaster
   - 신뢰도: 0.90 + officialBoost(0.15) + multispectralBoost(0.10) + baCredibilityBoost(0.10)
   - cascading_disaster 확정: Mayon eruption -> ashfall -> crop damage

2. **필리핀 스프래틀리 2개 섬 건설** (ent-evt-208)
   - Planet Labs PlanetScope 영상 확인
   - Thitu 활주로 1.5km 연장 + Nanshan 항만 건설 (10억 페소)
   - dom-defense, 좌표 admin-level 일반화
   - 신뢰도: 0.85 + commercialBoost(0.10)

3. **NISAR+Landsat 삼림벌채 조기탐지** (ent-evt-209)
   - NISAR L-band SAR + Landsat 9 OLI 융합
   - 아마존 파일럿: 기존 대비 100일 조기 탐지
   - Nature Communications 피어리뷰 논문
   - 신뢰도: 0.85 + officialBoost(0.15) + sarBoost(0.10)

4. **Shivelyuch 화산 눈녹음** (ent-evt-210)
   - Landsat 9 OLI, 캄차카 반도
   - 2022 분출 퇴적물에 의한 차별적 눈녹음
   - NASA Earth Observatory 공식
   - 신뢰도: 0.88 + officialBoost(0.15)

5. **Peter I Island 폰카르만 소용돌이** (ent-evt-211)
   - Landsat 8 OLI, 남극 벨링스하우젠 해
   - 대기 현상 -- 화산섬이 유발하는 카르만 와류
   - 신뢰도: 0.82 + officialBoost(0.15)

6. **Tracy Arm 산사태-쓰나미 후 지형 변화** (ent-evt-212)
   - Landsat 9 OLI, 알래스카 SE
   - Science 논문 기반 -- 빙하 피오르드 지형 변화
   - 신뢰도: 0.85 + officialBoost(0.15)

7. **Fuego 화산 분출 지속** (ent-evt-213) -- **위성 미확인**
   - INSIVUMEH 지상관측만, 위성 플랫폼 미명시
   - 화산재 937m, 다수 마을 ashfall
   - 신뢰도: 0.45 (satellite_unverified cap)

### 업데이트 이벤트 (6건)

1. **TS Caloy/Hagupit PAR 진입** (ent-evt-127): May 9 PAR 진입 확인, 65km/h, 870km east NE Mindanao
2. **Mayon VAAC 586** (ent-evt-082): SO2 2,785 t/d, 위험구역 8km 유지, 화쇄류 지속
3. **Dukono VAAC 226** (ent-evt-128): 수색 재개, 인니 여성 시신 수습, 싱가포르인 2명 수색 중
4. **GA Pineland** (temp-evt-001): 32,000+ ac, 70% containment, 이탄층 지하화재 난항
5. **Kilauea Ep47** (ent-evt-202): 예측 유지 May 12-17, summit inflation 6.9urad
6. **Sentinel-2A/2C 복구** (ent-evt-201): 19:00 UTC 이후 데이터 정상화, 데이터 손실 없음

## 추론 분석

### 다중 위성 교차검증 (4건)
1. TS Caloy -- Himawari-9 (JMA/JAXA) + GOES-18 (NOAA) -- 독립 GEO 교차검증
2. Mayon -- Himawari-9 (JMA) + Sentinel-2A (ESA) -- 독립 운영자/궤도 교차검증
3. GA Pineland -- S-NPP VIIRS (NOAA) + Landsat 8 (USGS) + Landsat 9 (USGS) -- 3위성
4. Kilauea -- Sentinel-2A (ESA) + Landsat 9 (USGS) -- 독립 운영자

### cascading_disaster (2건)
1. Caloy PAR entry -> Mayon lahar: PAR 진입 확인으로 신뢰도 0.70->0.75 상향
2. Mayon eruption -> ashfall crop damage: PhilSA Sentinel-2 변화탐지로 확정 사슬 (0.85)

### 센서 역량 매칭 (3건)
1. GA Pineland -- TIRS + VIIRS thermal -> wildfire/peat fire (thermalBoost +0.10)
2. NISAR -- L-band SAR -> deforestation canopy change (sarBoost +0.10)
3. PhilSA -- MSI NDVI/NBR -> ashfall vegetation mapping (multispectralBoost +0.10)

### 공식 기관 신뢰도 (11건)
PhilSA, NASA EO (x4), PAGASA+JMA+NOAA, PHIVOLCS+VAAC, CVGHM+VAAC Darwin, USGS HVO, NOAA+CIRA, ESA Copernicus

## 핵심 판단

1. **Mayon 복합재난 사슬 구체화**: Caloy PAR 진입 확인 + PhilSA ashfall crop damage 확정 -> 3중 도메인(disaster+agri+humanitarian) 수렴
2. **NASA EO 대거 발표**: Shivelyuch, Peter I, Tracy Arm, Forest Loss -- 4건 공식 feature article 동시 발표
3. **신규 위성 NISAR 첫 등장**: NASA-ISRO SAR 미션 첫 운영 데이터가 삼림벌채 탐지 논문에 사용
4. **Sentinel-2 인프라 복구 확인**: NorthC 데이터센터 화재 후 19:00 UTC 부분 복구 -- 데이터 손실 없음
