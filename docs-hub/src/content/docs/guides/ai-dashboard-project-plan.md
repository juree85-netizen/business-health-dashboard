---
title: AI 대시보드 검증 프로젝트 추진계획서
description: 사업건전성 대시보드 웹기반 재구축(AI Use Case)의 배경·환경·아키텍처·GitHub 구성·AI 소통 방안·협업 R&R·과제별 추진 방향을 통합한 상세 추진계획서 (v1.0)
---

**작성일:** 2026-07-09 (v1.0)
**담당:** 솔루션사업부 기획팀
**참조:** [검증 프로젝트 구조서 v1.1](/guides/ai-dashboard-project-charter/) · [검증 계획서 v1.0](/guides/ai-dashboard-verification-plan/) · [기술 검토서](/guides/aipro-tech-review/) · [통합 구조도](/guides/ai-verify-architecture/)
**상태:** 계획 수립 중

> 본 문서는 흩어져 있던 배경·구조·계획·아키텍처를 **하나의 실행 기준**으로 통합한 마스터 추진계획서다. 상위 개념(가설·전환 조건)은 구조서를, 과제 순서·일정은 계획서를 따르며, 본 문서는 그 사이의 **"어떻게 실행하는가(환경·구성·소통·R&R)"** 를 상세화한다.

---

## 문서 열기 (도식 버전)

<p>
  <a href="../../html/ai_dashboard_project_plan.html" target="_blank" rel="noopener"
    style="display:inline-block;padding:0.6em 1.4em;background:#1428A0;color:#fff;border-radius:6px;font-weight:600;text-decoration:none;">
    📐 추진계획서 (다이어그램 버전) 열기 ↗
  </a>
</p>

> 아키텍처·AI 소통 루프·일정 간트·워크스페이스·CI/CD·Task 순서를 **도식으로 표현한 HTML 버전**입니다. 아래 본문은 동일 내용의 텍스트 버전입니다.

---

## 0. 한눈에 보기

| 항목 | 내용 |
|------|------|
| **과제명** | AI Use Case — 사업건전성 대시보드 웹기반 재구축 |
| **검증 가설** | 웹디자이너·Tableau 개발자·DB 전문가 없이, **기획자가 AI로** 대시보드를 구축·운영·유지보수할 수 있는가 |
| **핵심 방식** | Fence-First — 사내(AIPro/FabriX) ↔ 외부(Claude)를 **사내 Private GitHub 버스**로 연결. fence를 넘는 건 데이터가 아니라 **계약(Contract)** |
| **팀** | 3인 (PM·환경 / 화면·프론트 / 데이터·백엔드) + 공유 마스터 컨텍스트 |
| **과제 순서** | Phase 0(도구검증) → Task 3(시안·시뮬) → Task 2(데이터모델) → Task 1(웹) → Task 4(리포트) |
| **데드라인** | 2026년 10월 (차세대 전환 9월 병행) |
| **성공 시** | 실 운영서버(Web/WAS + 앱 + Impala + DevOps) 프로젝트로 전환 |

---

## 1. 추진 배경 및 목적 (~7/10)

### 1.1 배경
- 현행 사업건전성 대시보드는 **Tableau + Impala DB** 기반으로, 화면 변경·지표 추가 시 웹디자이너·Tableau 개발자·DB 전문가에게 각각 의존한다.
- 지표 정의부터 개발까지 리드타임이 길고, 기획 의도가 개발 단계에서 손실되며, 유지보수 비용이 지속 발생한다.
- 생성형 AI(사내 AIPro/FabriX, 외부 Claude)의 코드·SQL·문서 생성 역량이 실무 적용 수준에 도달했다.

### 1.2 문제 정의
> "기획자가 설계한 지표·화면을, 전문 개발 인력의 개입 없이 AI만으로 얼마나 완결할 수 있는가?"

### 1.3 목적
- **검증(Verify):** AI만으로 대시보드를 구축·운영·유지보수할 수 있는지 실제 과제로 입증.
- **전환(Transition):** 검증 성공 시 실 운영 프로젝트(Web/WAS + Impala + DevOps)로 전환하기 위한 기준·자산 확보.
- **역량 내재화:** 기획팀이 AI 기반 개발 사이클을 직접 주도하는 운영 모델 정립.

### 1.4 목표 (측정 가능)
1. Task 3~4를 AI 산출물 중심으로 완료하고, 각 단계의 **AI 자력 완성도(%)** 를 기록.
2. 검증→운영 **전환 판단 기준** 을 데이터로 충족.
3. 재사용 가능한 **워크스페이스·문서포맷·소통 프로토콜** 을 표준화.

---

## 2. 추진 일정 및 마일스톤

### 2.1 준비(환경 구축) 단계 — 7월
| 완료목표 | 항목 | 산출물 |
|:---:|------|------|
| **~7/8** | GitHub Organization / Actions / Pages **SR 신청** | SR 티켓, Org 승인 |
| **~7/10** | 프로젝트 배경/목적 정리 | 본 문서 §1, 배경·목적 페이지 발행 |
| **~7/10** | 아키텍처(SW/HW) 설계 | 통합 구조도, 본 문서 §3 |
| **~7/16** | 프로젝트 환경 설정 완료 | Workspace·GitHub·CI/CD·Preview Hub·AI 환경 §4 |

### 2.2 검증 실행 단계 (계획서 기준)
| 기간 | Phase | 내용 |
|------|-------|------|
| Week 1~2 | **Phase 0** | AIPro/FabriX 도구 검증 스파이크 |
| Week 3~5 | **Task 3** | 시안 생성 + 데이터 시뮬레이션 |
| Week 5~8 | **Task 2** | 데이터 모델 개선 (사전 검증) |
| Week 8~12 | **Task 1** | 웹 대시보드 재구축 (Front/Back-end) |
| Week 12~14 | **Task 4** | 자동 분석 + 인사이트 리포트 발송 |

데드라인: **2026년 10월**

---

## 3. 프로젝트 아키텍처 — 재설계본 v2 (Fence-First)

> 베스트프랙티스 검증 결과를 반영한 재설계본. 기존 v1(데이터는 fence 안 · 버스/런타임은 fence 밖)의 보안 결함을 해소한다. **핵심 전환: fence를 넘는 것은 "데이터"가 아니라 "계약(Contract)"이다.**

### 3.1 재설계 5원칙 (Fence-First)
| 원칙 | 내용 |
|------|------|
| ① **Fence-First** | 기밀 DB·최종 런타임·반출 게이트를 **모두 fence(사내 보안망) 안**에. "기밀이라 VDI"라는 논리를 버스·런타임에도 일관 적용 |
| ② **사내 Private 버스** | Public이 아닌 **사내 Private 레포**를 버스로 → 비즈니스 로직·스키마·샘플이 공개망으로 유출되지 않음 |
| ③ **계약만 반출** | Claude는 물리 데이터가 아니라 **논리 데이터 계약**만으로 UI 제작 → fence를 넘는 건 계약·합성샘플뿐 |
| ④ **Build/Run 분리** | UI 제작(fence 밖)과 실데이터 연결·구동(fence 안) 분리. **검증 단계에 fence 내 실구동 1회 필수** |
| ⑤ **Pre-push 게이트** | 반출 검사를 push 이후(GitHub)가 아니라 **push 이전(VDI 내부)** 에 — 나가기 전 차단 |

### 3.2 TO-BE 토폴로지 — Fence-First
```
   [ fence 밖 · Build 레이어 ]                ╔══ SECURE FENCE (사내 보안망) ═══════╗
     Claude (개별 PC / 외부)                  ║ 🛡️ 반출 게이트 (pre-push 검사)      ║
     · UI·화면·리포트 생성      ── 계약만 ──▶  ║ ──────────────────────────────────  ║
     · Docs Preview Hub        ◀── Contract   ║  Impala(기밀 DB) · AIPro/FabriX     ║
     · 실데이터 접근 ✕            ·합성샘플     ║  최종 Web/WAS 런타임 ← 실데이터 연결  ║
                                              ║  사내 Private 버스 (Contract 저장)  ║
                                              ╚═════════════════════════════════════╝
```
> 데이터·최종 런타임·반출 게이트가 **모두 fence 안**. 밖에서는 실데이터 없이 계약으로 UI만 만든다.

### 3.3 fence를 넘는 것 — Data Contract
| 산출물 | 생산 | 반출 | 내용 |
|------|------|:---:|------|
| **Data Contract** (지표·필드 스펙) | AIPro → 합의 | ✅ | 지표 산식·필드(논리)·타입·단위·허용값·집계기준 |
| **검증된 SQL / ERD** | AIPro (VDI) | ✅ 마스킹 | 실행·검증 완료 로직. 물리 서버/테이블/컬럼명은 변환 |
| **합성 / 마스킹 샘플셋** | AIPro (VDI) | ✅ | 비식별 테스트 데이터 — UI·시뮬레이션 구동용 |
| **UI 컴포넌트 / 화면** | Claude (밖) | ↘ 안으로 | 계약 기준 프론트 → Run-time에 fence 안으로 배치 |
| **원천 실데이터 / 개인정보** | — | ⛔ 불가 | Impala 원본 레코드·실적치. fence 밖 이동 금지 |

### 3.4 Build-time vs Run-time 분리 *(검증 유효성 핵심)*
| 구분 | 위치 | 데이터 | 핵심 |
|------|------|------|------|
| **Build-time** (UI 제작) | fence 밖 · Claude | Contract + 합성 샘플셋 (실데이터 ✕) | 화면·차트·리포트 틀 생성 → 버스에 커밋 |
| **Run-time** (실데이터 통합·구동) | fence 안 · AIPro/실배포 | 실데이터 end-to-end | UI + 검증 SQL 결합 → Impala 연결. **최소 1회 성공 = "워킹" 입증** |

> **[v1 결함 해소]** 기존 설계는 웹이 fence 밖에서 합성데이터로만 돌아 "실데이터에 붙은 대시보드"를 한 번도 검증하지 못했다. 재설계는 Run-time을 fence 안에 두고 검증 범위에 포함시켜 실데이터 연결·정합·성능을 실제로 입증한다.

### 3.5 공유 버스(사내 Private GitHub) — 5-Layer
| Layer | 역할 | 정의 |
|:---:|------|------|
| **L1** | Ingress·접근제어 | VDI·개별PC 인증(PAT), main 브랜치 보호, 사내 Private 레포 |
| **L2** | Storage·저장 | `context/`·`plan/`·`work/`·`handoff/`·`verify/` — 폴더별 용도·포맷·쓰기오너·반출등급 고정 |
| **L3** | Message Queue | handoff 상태머신 `open→in_progress→done→confirmed` (§4.3) |
| **L4** | Automation | GitHub Actions — **2차 방어**(1차는 VDI pre-push): PII 스캔→Lint→Build→Deploy |
| **L5** | Egress·배포 | Pages 프리뷰 · Tags/Release 스냅샷 · 운영 레포 승격 |

### 3.6 버스 위치 — ✅ 실측 확정 (Scenario A 채택)
회사 PC의 외부 Claude CLI에서 사내 Private GitHub 접속을 **실측 검증**했다 (2026-07-09).

| 항목 | 결과 |
|------|------|
| DNS / HTTPS | ✅ `code.sdsdev.co.kr` → 70.220.98.33 · HTTP 302 |
| 읽기 (clone/pull) | ✅ 실측 성공 (main = 0358ad7) |
| **쓰기 (push ACL)** | ✅ 임시 브랜치 push(rc=0) → 삭제(rc=0) 확정 |
| 레포 | `Solution-Strategy-Group/biz_health_dashboard` |

**운영 조건(실측):** ① 프록시 우회 필수 — `NO_PROXY`에 `code.sdsdev.co.kr`(또는 `*`) ② 사내 CA — 루트 CA를 git에 등록(임시 `http.sslVerify=false`) ③ 자격증명 — Windows 자격증명 관리자에 `joori-yoo` + PAT.
→ **Plan B(fence 내 릴레이)는 A 확정으로 불필요, 대안 보관.**

### 3.7 SW 스택 (안)
| 계층 | 후보 | 비고 |
|------|------|------|
| 데이터 | **Impala** (`c_tableau` 스키마) | 기존 테이블 공존 → **검증용 테이블만** 생성/변경 |
| 백엔드 | Python(FastAPI 등) / SQL | AIPro 생성, Impala 커넥션 |
| 프론트 | HTML/CSS/JS, 차트 라이브러리 | Claude 생성, 와이어프레임 → 실구현 |
| 문서/뷰 | Astro Starlight (Docs Preview Hub) | 현 문서허브와 동일 스택 |
| CI/CD | GitHub Actions + Pages | 자동 빌드·프리뷰·배포 |

### 3.8 HW / 환경
| 환경 | 용도 | 제약 |
|------|------|------|
| **VDI (개인정보보호 PC)** | 데이터·SQL·모델링·**최종 런타임** | AIPro CLI만, Impala만 기본 통신, 타 서버는 방화벽 승인, 일반PC와는 사내웹메일만 |
| **개별 PC** | 웹개발·문서·리포트 (Build) | Claude + AIPro 모두 사용, 사내 GitHub/Nexus 접근 가능 |

> **방화벽 승인 현황:** VDI·개별 PC 모두 사내 GitHub(code.sdsdev.co.kr)·Nexus(nexus.sdsdev.co.kr) 허용 완료. 외부 Claude CLI ↔ 사내 Private GitHub 읽기·쓰기 실측 확인(§3.6).

---

## 4. 프로젝트 환경 설정 (~7/16)

### 4.1 GitHub 구성 방안

**연결 실측 확인 (2026-07-09)** — §3.6 참조
| 항목 | 결과 |
|------|------|
| 레포 | `Solution-Strategy-Group/biz_health_dashboard` (code.sdsdev.co.kr) |
| 읽기(clone/pull) | ✅ 실측 성공 |
| 쓰기(push ACL) | ✅ 임시 브랜치 push→삭제로 확정 |
| 운영 조건 | 프록시 우회(`NO_PROXY`) · 사내 CA(루트 CA 등록/`http.sslVerify`) · 자격증명(PAT) |

**구성 검토안**
- **Repo 전략:** 검증 단계는 단일 사내 Private 레포로 시작(3인 컨텍스트 공유·충돌 최소화). 운영 전환 시 앱/데이터/문서 분리 검토.
- **공개 범위:** **사내 Private 레포 우선**(§3.6 Scenario A). Public 지양 — 어느 경우든 **원천 데이터·서버/테이블/컬럼 실명 절대 미포함**(§4.7 PII 스캔).
- **Actions / Pages:** CI/CD·문서 프리뷰·배포 자동화용 (SR).
- **브랜치/PR:** `main` 보호 + 과제별 브랜치, PR 리뷰로 3인 변경 가시화.

### 4.2 Workspace / 프로젝트 구조화 (폴더·파일·문서포맷)

**로컬 스캐폴드:** `C:\Users\SDS\Desktop\biz-health-verify` (git init 완료)

```
biz-health-verify/
├── CLAUDE.md          # Claude 작업 기준·역할·규칙
├── AIPRO.md           # AIPro 작업 기준·Impala 규칙·정보보호 규칙
├── INDEX.md           # 전체 인덱스 (사람·기계 모두 읽기용)
├── context/           # 공유 마스터 컨텍스트 (프로젝트 상태·결정사항)
├── plan/              # 과제별 계획
├── work/              # 진행 산출물 (과제별)
├── handoff/           # Claude ↔ AIPro 인계 파일 (요청/응답)
└── verify/            # 검증 결과·로그
```

**문서포맷 원칙**
- **Human + Machine readable 병행:** 서술은 Markdown, 구조화 데이터·인계·상태는 **JSON/YAML**, 실행 로직은 **Python**.
- 각 폴더 최상단 `INDEX.md` 로 탐색성 확보, 파일명 규칙 통일(과제-일자-주제).
- CLI 대화 지속성: `CLAUDE.md`/agent/skill 기준 문서 + 스냅샷으로 **로그인 시 이어서 작업** 가능하게.

### 4.3 AI 소통 방안 (핵심)

**GitHub를 Claude ↔ AIPro 비동기 메시지 버스로 사용한다.** (두 AI는 서로 다른 보안망에 있어 직접 통신 불가)

```
① Claude(외부): 계획·화면설계·SQL 요청서를 handoff/ 에 커밋·push
        │
        ▼
② AIPro(VDI): handoff/ pull → Impala에서 구현·검증 → 결과(변환된 스키마 정보 포함)를 handoff/ 에 커밋·push
        │
        ▼
③ Claude(외부): 결과 pull → 확인·다음 작업 반영 → 반복
```

**인계(handoff) 파일 규약 (안)**
| 필드 | 내용 |
|------|------|
| `id` | 요청 고유번호 (task-seq) |
| `from` / `to` | claude / aipro |
| `type` | request / response |
| `task` | 대상 과제 (T1~T4) |
| `ask` | 요청 내용 (SQL 생성, 모델 검증 등) |
| `constraints` | 정보보호·스키마 규칙 |
| `result` / `status` | 응답·완료여부 |
| `masked` | 서버/테이블/컬럼 **변환(마스킹)** 여부 |

> **정보보호:** AIPro는 서버·테이블·컬럼 실명을 **변환하여 공유**한다. 원천 데이터·개인정보는 GitHub에 절대 올리지 않는다.
> **개선 과제:** GitHub 비동기 방식보다 나은 소통 방법(구조화 메시지 스키마, 자동 폴링 등)은 **별도 검토 과제**로 병행.

### 4.4 스냅샷 · 버전관리
- **버전 태그:** 의미 있는 완료 시점마다 `git tag`(예: `verify-v0.1`) + **GitHub push 필수**.
- **스냅샷:** 프로젝트 상태·결정사항·미결건을 `context/` 에 스냅샷으로 기록 → 컨텍스트 과다 방지 + 세션 이어받기.
- **커밋 규약:** 과제·유형 프리픽스(`[T2] 데이터모델 검증 결과`), PR 기반 리뷰.

### 4.5 DevOps (CI/CD)
| 파이프라인 | 트리거 | 동작 |
|------|------|------|
| **Docs Build** | 문서/guides push | Astro 빌드 → Pages 배포 (Preview Hub 갱신) |
| **Web Preview** | 대시보드 코드 push | 빌드 → 프리뷰 환경 배포 |
| **Lint/Check** | PR | 포맷·PII 스캔·기본 검증 |

- GitHub Actions로 **문서·웹 프리뷰 자동 배포**, 수동 배포 최소화.
- 운영 전환 시 사내 DevOps(CI/CD) 파이프라인으로 승격.

### 4.6 Docs Preview Hub
- **현행:** Astro Starlight 기반 문서허브(PLAN HUB) — 본 계획서를 포함한 검증 문서를 GitHub Pages로 서빙.
- **역할:** 3인·이해관계자가 **최신 산출물을 실시간 프리뷰**하는 단일 창구. 와이어프레임·리포트·계획서를 링크로 공유.
- 사이드바 그룹 **'사업건전성 대시보드 웹 구축'** 에 문서 통합 관리.

### 4.7 PII / 정보보호 스캔
- PR·push 시 **원천 데이터·개인정보·서버/테이블/컬럼 실명** 유입 여부 자동 점검(스캔 프로토콜).
- Impala 규칙 위반(기존 테이블 변경/삭제, `c_tableau` 외 스키마 접근) 감지 체크리스트.

### 4.8 AI Pro · Claude 환경 설정
| 도구 | 위치 | 설정 |
|------|------|------|
| **AIPro / FabriX** | VDI | CLI 설정, Impala 커넥션, `AIPRO.md` 기준·Impala/정보보호 규칙 |
| **Claude Enterprise** | 개별 PC/외부 | `CLAUDE.md`·agent·skill 기준, 문서허브·리포트 워크플로우 |
| **공유 컨텍스트** | GitHub | `context/` 마스터 컨텍스트 — 양측이 동일 기준 참조 |

### 4.9 프로젝트 정보 · 스냅샷 · 컨텍스트 관리
- **마스터 컨텍스트(단일 소스):** 프로젝트 상태·결정·미결건·규칙을 `context/` 한 곳에 유지, 3인·양 AI 공유.
- **컨텍스트 과다 방지:** 장기 대화는 스냅샷으로 요약·이관, 세션 재개 시 스냅샷+기준문서로 복원.
- **3인 충돌·누락 방지:** INDEX·PR·컨텍스트 스냅샷으로 상태 가시화.

### 4.10 FabriX 연결 관련 Follow-Up
| 항목 | 내용 | 상태 |
|------|------|:---:|
| 활용 범위 | 대시보드 AI 고도화(사내 AI)로서 AIPro와의 역할 구분 | 검토 |
| 기술 확인 | DB 직접 접근·코드 실행 환경·스케줄링·사내 메일 연동 가능 여부 | 개발자 미팅 확인 대상 |
| 공식 문의 | `fabrix.cs@samsung.com` | F/Up |

---

## 5. 협업 방식 및 AI (AIPro · Claude) R&R

### 5.1 AI 도구 역할 분담
| 환경 | 도구 | 역할 |
|------|------|------|
| 사내 보안망 (VDI) | **AIPro / FabriX** | SQL 생성·검증, 데이터 모델 설계, KPI 산출 로직 확인, Impala 실행 |
| 외부망 (개별 PC/서버) | **Claude Enterprise** | 웹 대시보드 개발, 와이어프레임, 기획 문서, 인사이트 리포트 |

> 두 도구는 **대체재가 아니라 역할 분리 설계**다. 경계는 보안이 정한다.

### 5.2 3인 팀 R&R
| 역할 | 담당 | 주요 업무 |
|------|------|------|
| ① **기획·환경 (PM)** | — | 배경/목적/목표, 환경설정, 시스템 구조, DevOps/CI/CD, 보안 |
| ② **사용자·화면 (프론트)** | — | 사용자 정의·Customer Journey·Empathy Map, 지표 정의, Frontend |
| ③ **데이터 (백엔드)** | — | Backend, 분석, 연계, 데이터 모델링 |

### 5.3 협업 원칙
- **단일 소스:** 모든 상태·결정은 GitHub(`context/`)에 기록, 구두 결정 금지.
- **비동기 인계:** Claude↔AIPro는 handoff 규약(§4.3)으로만 주고받음.
- **가시성:** PR·태그·스냅샷으로 3인이 서로의 진행을 실시간 확인.

---

## 6. 본 과제 추진 방향 (Task 상세)

과제는 **리스크 낮은 순**으로 추진한다 (계획서 §Task 순서).

### 6.1 Task 3 — 시안 생성 + 데이터 시뮬레이션 *(1st)*
- DB 접근 없이 **가상 데이터**로 시작 → 리스크 최저.
- Claude가 화면 시안(와이어프레임) 생성, 산출 로직을 시뮬레이션해 정합성(집계 기준·예외 케이스) 사전 확인.

### 6.2 Task 2 — 데이터 모델 개선 (사전 검증) *(2nd)*
- AIPro가 SQL 생성·모델 개선안 도출, **개발 착수 전** 지표 산식·ERD·정합성을 Impala(`c_tableau`)에서 검증.
- 검증용 테이블만 사용, 기존 Tableau 테이블 불변.

### 6.3 Task 1 — 웹 대시보드 재구축 (Front/Back-end) *(3rd)*
- Task 3 시안 + Task 2 SQL/모델을 결합해 **AI 기반 화면 설계 및 실구현**.
- 프론트(Claude) + 백엔드/데이터(AIPro) 결합, 코드 실행 환경·컨텍스트 유지·DB 연결이 핵심 검증 포인트.

### 6.4 Task 4 — 사업건전성 인사이트 리포트 자동 생성 + 메일 푸시 *(4th, 방향 검토)*
- 환경 구축 후 **자동/반자동** 검증.
- **검토 필요:** ① 데이터 수집 방식(DB 직접 read vs 대시보드 read) ② 스케줄링 자동화 지원 ③ 사내 메일 시스템 연동 가능 여부.
- 사업부장 보고용 월별 리포트(Tableau 자동화 홀딩건)와 연계 방향 검토.

---

## 7. 리스크 및 미결정 사항

| # | 항목 | 상태 |
|---|------|:---:|
| 1 | 사내 Private 버스 연결(읽기·쓰기) | ✅ 실측 확정 (§3.6) |
| 2 | AIPro/FabriX 기술 확인(DB 직접접근·코드실행·스케줄링·메일연동) | 개발자 미팅 |
| 3 | Claude↔AIPro 소통 방법 고도화 | 별도 과제 |
| 4 | 시장 데이터 biz_type 매핑(수작업 업로드) | 담당자 문의 후 재논의 |
| 5 | Task 4 데이터 수집 방식·리포트 자동화 범위 | 검토 |

---

## 8. 성공 기준 및 전환 조건

- Task 3~4를 AI 산출물 중심으로 완료하고 각 단계 **AI 자력 완성도**를 기록·평가.
- 검증 성공 판정 시 → **실 운영서버 프로젝트**(Web/WAS + 추가 애플리케이션 + Impala + DevOps/CI/CD)로 전환.
- 차세대 전환('26.9월)과 병행, **데드라인 2026년 10월**.
- 재사용 자산(워크스페이스·문서포맷·소통 프로토콜·CI/CD)을 운영 단계로 승계.

---

## 관련 문서
[추진 배경 및 목적](/guides/ai-verify-background-purpose/) · [검증 프로젝트 구조서 v1.1](/guides/ai-dashboard-project-charter/) · [검증 계획서 v1.0](/guides/ai-dashboard-verification-plan/) · [AIPro/FabriX 기술 검토서](/guides/aipro-tech-review/) · [AI Use Case PoC 슬라이드](/guides/ai-usecase/) · [통합 구조도](/guides/ai-verify-architecture/)
