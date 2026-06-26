---
name: biz-type
description: 시장 데이터 수작업 업로드 시 biz_type 분류와 원천 데이터 분류 기준 간 매핑 — 확정본
metadata: 
  node_type: memory
  type: project
  originSessionId: f03b3e47-89b2-4970-918f-a6389c55d063
---

## 현황: 홀딩 (2026-06-16 재검토 필요)

**홀딩 사유:**
- `3분류 = 3 (라이선스)` → **자사 솔루션만** 해당 → Solution 매핑 가능
- `3분류 = 2 (HW)` → HW + **타사 솔루션 혼재** → SI/SM 단순 매핑 불가

타사 솔루션이 2번(HW)으로 분류되어 있어, 3분류만으로는 SI/SM과 Solution을 완전히 구분할 수 없음. 추가 기준 필드 또는 별도 식별 방법 확인 필요.

---

## 기존 검토 로직 (보류 중 — 적용 금지)

원천 데이터 필드: `5대`, `5대상세`, `3분류`

```
5대 / 5대상세 기준
├─ MSP    → biz_type = MSP
├─ SaaS   → biz_type = SaaS
└─ On-prem (SI/SM + Solution 혼재)
       └─ 3분류 적용
              ├─ 1 (용역)     → biz_type = SI/SM
              ├─ 2 (HW)       → biz_type = SI/SM  ← 타사 솔루션 혼재 문제 있음
              └─ 3 (라이선스) → biz_type = Solution (자사 솔루션만 해당)
```

**3분류 값 설명:**
- 1: 용역 (서비스 제공 형태)
- 2: HW (하드웨어 + 타사 솔루션 혼재)
- 3: 라이선스 (자사 솔루션만 해당)

**예외 처리:**
- 3분류 null/결측값 없음 (원천 데이터에서 확인됨)

**Why:** 5대/5대상세만으로는 On-prem 내 SI/SM과 Solution 구분 불가 → 3분류로 추가 분기 시도했으나 2번(HW) 내 타사 솔루션 혼재로 인해 로직 불완전
**How to apply:** 추가 기준 확정 후 재적용 예정
