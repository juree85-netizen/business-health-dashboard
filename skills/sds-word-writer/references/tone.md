# SDS 임원 보고서 문체 규칙 (Tone rules)

The single thing that distinguishes this style from ordinary Korean prose is
**information density per line**. Every line is a standalone fact. Padding,
hedging, and narrative connective tissue all go away. Think: "a staff officer
briefing an executive in 3 minutes."

Read all of this before you start rewriting. These are the rules that give
the output its characteristic look.

---

## 1. Sentence ending — 명사형 / 축약형 우선

Rewrite verb endings to noun or compressed forms. This is the #1 signal.

| Avoid | Prefer |
|---|---|
| ~입니다 / ~습니다 | (삭제) |
| ~한다 / ~된다 | ~함 / ~됨 / (명사로 마침) |
| ~할 예정입니다 | ~예정 |
| ~진행 중입니다 | ~중 / ~진행 中 |
| ~필요합니다 | ~필요 |
| ~있습니다 | ~有 / (명사로 마침) |
| ~가능합니다 | ~가능 / ~可 |
| ~전망됩니다 | ~전망 |
| ~검토 중 | ~검토 中 |

**Before:** Microsoft가 M365 Copilot에 OpenClaw와 유사한 에이전트를 통합해서 개발하고 있는 것으로 알려졌습니다.
**After:**  Microsoft, M365 Copilot에 OpenClaw 유사 Agent 통합 개발 中

---

## 2. One information per line — 한 줄 = 한 정보

Each bullet carries exactly one fact. If a sentence naturally has two facts
("A이면서 동시에 B도 있음"), split into two bullets. If two facts are tightly
linked, use a `·` detail line under the parent bullet.

**Before:** 기업고객을 대상으로 하며 강화된 보안 기능과 접근 통제 기능이 탑재될 예정이고, 로컬 PC에서 실행되며 사용자 대신 작업을 수행하는 에이전트입니다.

**After:**
```
  - 기업고객 대상, 강화된 보안·접근 통제 기능 탑재 예정
  - Claw : 로컬 PC에서 실행되며 사용자 대신 작업 수행하는 Agent
```

---

## 3. Line length — 30~55 characters

Aim for 30~55 Korean characters per line. If a line runs over, break at a
clause boundary and wrap with **6-space indent** so the wrapped text aligns
with the content column (not with the bullet character).

**Example (line too long, wrapped):**
```
  - 핵심 기능은 'always-on' 상태로 장기간 다단계 작업을
    지속 수행하는 것
```

**Single-character widow rule**: if a bullet wraps with only 1–2 orphan characters
on the last line, first try to tighten the wording. If the text is already as
tight as it gets, set `"scale": 92` (or 93) on that bullet to condense the
letter-spacing just enough to pull the widow back up. Do **not** force every
line onto a single row — use `scale` surgically only for awkward widows.

---

## 4. Bullet hierarchy — 수동 들여쓰기

The hierarchy is **not** Word's list feature. It is literal spaces + symbols
in the text. The generator preserves them verbatim.

**Canonical order (top → bottom).** The top two tiers (`Ⅰ` / `1.`) are
**optional** and should be used only when the report is large enough to
need them — default briefs start at `□`.

| Level | Prefix | Size | Required? | When |
|---|---|---|---|---|
| Roman chapter | `Ⅰ. ` / `Ⅱ. ` / `Ⅲ. ` | 16pt bold | **Optional** — 매우 큰 범위의 보고서 | Top-level grouping in very large or TOC-backed reports |
| Number chapter | `1. ` / `2. ` / `3. ` | 15pt bold | **Optional** | Sub-chapter under a Roman-numeral chapter, or mid-tier grouping in a long report |
| Section | `□ ` | 14pt bold | Always | Each main section (default starting point for ordinary briefs) |
| L1 bullet | `  - ` (2sp + hyphen + space) | 14pt | Always | Facts under a section |
| L2 bullet | `    ·` (4sp + middle-dot) | 14pt | Always | Detail under L1 |
| Wrap | 6 spaces | 14pt | — | Continuation of previous line |
| Note | `  ※ ` | 14pt | — | Supplementary note at end of section |
| Implication | `    → ` | 14pt | — | "What this means" / follow-on |
| Subhead | `< … >` | 14pt bold | — | Inline mini-heading for a chart/table block |
| Bracket tag | `[위협]` / `[기회]` at section heading start | — | — | Threat/opportunity framing |

Visualized (only the two bottom tiers are mandatory):

```
Ⅰ. 대분류                 ← Optional — 매우 큰 범위의 보고서
   1. 중분류              ← Optional
      □ 소분류            ← default starting point
         - 본문
            · 세부
```

Set `"numeral": "Ⅰ"` or `"number": 1` on a section in the content JSON. The
generator drops the `□` prefix automatically for those levels — never combine
`Ⅰ`/`1.` with `□`, the markers are redundant.

### Circled numbers (`①②③`) — dash/dot 수준의 옵션 기호

`①②③` 번호는 **별도의 계층이 아니라 `-` (대시) / `·` (도트) 레벨에서 순서를
표시할 때 사용하는 선택적 기호**다. 전략 항목, 단계별 절차, 순위 있는 발견사항
처럼 순서 자체가 의미를 지닐 때만 사용하고, 나머지는 일반 `-` / `·`을 유지한다.
`Ⅰ`·`1.`·`□` 자리에는 절대 사용하지 않는다. (content JSON: `"kind": "circled"`)

**Bold is reserved for key takeaways and action items.** The primary visual
hierarchy comes from size (title 20pt vs body 14pt), the `□` symbol, and
indentation. However, in the SDS 시사점 section or equivalent, critical
implication lines (`→`) and action-item summaries may use `"bold": true` for
emphasis. Limit to 1–3 bold bullets per section to maintain contrast.

The `·` is **U+00B7 middle dot**, not a hyphen or bullet.

---

## 5. Symbols and shorthand

| Symbol | Meaning | Example |
|---|---|---|
| `→` | 시사점 / 귀결 / 파생 | `→ SDS 등 M365 기반 고객 대상 AI Agent 채택 가속화 예상` |
| `※` | 단락 끝의 보충·강조 | `※ 로컬 실행·보안 통제·상시 작동이 3대 키워드` |
| `↑` `↓` | 증가 / 감소 | `채택률 78%→88% ↑` |
| `∼` (U+223C) | 범위 | `10∼20%`, `3∼5명` |
| `·` (U+00B7) | 인라인 나열·하위 bullet | `보안·접근 통제` |
| `$` `B$` `₩` | 금액 | `258B$`, `100억원+` |
| `+` suffix | 초과 | `100+ 고객`, `연간 8%+` |

---

## 6. Hanja — 선택적으로만 (기본은 한글)

**Default to Hangul.** Hanja is sparing seasoning, not the main flavor. A
reader should encounter at most a handful of Hanja in a full-page brief — if
the page looks speckled with 漢字, you've overused it. Hanja appears in two
narrow cases, and nothing else:

### 6-1. Conventional single-character Hanja (whitelist)

Use a **single** Hanja character only in these conventional slots:

- **Degree / rank**: `高`·`中`·`低`, `上`·`中`·`下`, `大`·`小` — e.g., `비중高`, `ROI中`
- **Status / aspect** in predicate position: `有`·`無`, `可`·`不可`, `內`·`外`, `前`·`後`, `新`·`舊`, `未` (as in `未정`, `未사용`)
- **Time unit**: `年`·`月`·`週`·`日`·`時` — e.g., `'26年`, `3月`, `週 1회`
- **Ordinal marker**: `第N`, `N次`, `N回`
- **Company marker**: `社` right after a company name (e.g., `Anthropic社`)
- **Day of week** (date line only): `月`·`火`·`水`·`木`·`金`·`土`·`日`
- **Countries in comparison tables only**: `美`·`韓`·`中`·`印`·`英`·`日` when column width matters. In prose, always `미국`/`한국`/`중국`.

Keep to one Hanja character per compound. If you need more than one, the word is probably not on this list — write it in Hangul.

### 6-2. Multi-character Hanja compounds — almost never

Do **not** write two-or-more-character Hanja compounds for ordinary vocabulary
just because a Hanja form exists. Korean business readers parse these slower
than Hangul, and clusters of them make the doc look archaic.

| ❌ Don't write | ✅ Write |
|---|---|
| 業務, 使用, 作成, 時間, 構築, 導入, 管理, 原因, 報告, 持續, 確散, 成果 | 업무, 사용, 작성, 시간, 구축, 도입, 관리, 원인, 보고, 지속, 확산, 성과 |
| 創出, 生產性, 最大, 最下, 最低, 最高, 平均, 中心, 基本, 段階, 全社 | 창출, 생산성, 최대, 최하, 최저, 최고, 평균, 중심, 기본, 단계, 전사 |
| 不過, 未滿, 上位, 上승, 對比, 合算, 可視性, 現業, 明白, 引用, 本, 他 | 불과, 미만, 상위, 상승, 대비, 합산, 가시성, 현업, 명백, 인용, 본, 다른 |

The **only** time a 2+ character Hanja compound is acceptable is when removing
it would lose meaning a reader genuinely needs — e.g., a technical/legal term
whose Hangul homophone is ambiguous (`異議` vs `意義`, `公開` vs `公開` in a legal
brief). That situation is rare. Default to Hangul and only promote to Hanja
when you can articulate the ambiguity being resolved.

### 6-3. Don't mix Hanja into a Hangul word

Never stitch one Hanja character onto a Hangul stem (`近로자`, `生성`, `生산성`,
`基礎`, `上승`, `低조`, `高효율`). Either the whole word is on the 6-1 whitelist
or it stays fully Hangul.

---

## 7. 주석 (Annotations) — 파란 9pt 텍스트 상자, 단어 아래 배치

주석은 본문 한 줄을 읽다가 막히는 지점을 그 자리에서 짧게 풀어주는 장치.
실제 SDS 보고서에서 주석은 **세 가지 용도**로 쓰이며, 빈도 순은 다음과 같다:

1. **단문 맥락 보강** — 조건·범위·전제·비공개 사실을 한두 구절로 부연
2. **약어·도메인 용어 풀이** — 낯선 약어·기술·제품명의 정의
3. **출처 인용** — 출처 자체가 신호일 때만 (선택적)

출처 인용은 세 용도 중 가장 드문 쪽이며 **기본 동작이 아니다**. 모든
숫자에 기계적으로 출처를 다는 것은 오히려 정보 밀도를 떨어뜨린다.

**용도별 예시:**

| 용도 | 주석 내용 예시 | 앵커 |
|---|---|---|
| ① 단문 맥락 보강 (조건·범위·비공개) | `지분율 비공개` / `거래 종결시` / `규모 未공개` / `연결 기준, 비경상 항목 제외` | 해당 수치·명사 |
| ① 구체 예시·나열 | `예) Dose ID GPT` / `스페인, 이탈리아, 프랑스, 노르웨이` / `인사, 콜센터, 재무관리 등` | 상위 개념 |
| ② 도메인 약어 / 용어 | `MAU : 월간 활성 사용자 수` / `Wafer-Scale Engine` | 약어·용어 |
| ② 낯선 기술 / 제품명 | `Claw : 로컬 PC에서 사용자 대신 작업하는 Agent` | 제품 토큰 |
| ② 숫자가 의미하는 맥락 | `전년 동기 대비` / `전 세계 누적 기준` | 숫자 자체 |
| ② 인물·조직 1회 소개 | `Moderna CEO` / `공동창업자 겸 사장` | 인물명 |
| ③ 출처 인용 (선택) | `출처: Reuters ('25.11月)` / `McKinsey 2025` | 수치 또는 핵심 명사 |
| ③ 1차 소스 URL | `https://openai.com/index/stargate-community/` | 핵심 명사 |
| 특례: 인터뷰 질문 원문 | `(Q) AI 스케일링 법칙이 여전히 유효한가?` | 답변 요약 문장 |

**관용 prefix — 내용이 실제로 해당할 때만 사용:**

- `출처:` — 기관·매체 인용
- `예)` — 구체 사례·상품명 나열
- `(참고)` — 본문에서 생략한 부연 정보
- `(추가)` — 뒤늦게 확인된 사실
- `(Q)` — 인터뷰 질문 원문 보존 (답변 요약 문장에 앵커)

prefix는 필수가 아니며, 기계적으로 붙이지 말 것. 단문 맥락 보강은 대개
prefix 없이 구절만 쓴다 (`지분율 비공개`).

**동일 출처의 반복 금지 — 한 섹션·보고서 내에서 같은 출처를 여러 주석에
중복 표기하지 않는다.** 섹션의 불릿이 모두 같은 보고서에서 왔다면:

- 섹션 헤딩에 `headingAnnotation`으로 한 번만 붙이거나,
- 그 섹션에서 가장 대표성 있는 단 한 줄에만 붙이고 나머지는 비워둔다.

같은 `* McKinsey 2025`가 한 장표에 4~5번 반복되는 순간, 주석은 해설
기능을 잃고 배경 소음이 된다. **반복되는 출처는 한 번만, 진짜 해설이
필요한 자리에만 주석을 남긴다**는 원칙을 지킨다.

---

렌더링 측면에서, 주석은 본문 흐름에서 분리된 **파란 9pt 떠 있는 텍스트
상자**로 `*` prefix와 함께, 설명 대상 단어 **바로 아래**에 배치된다.
`*`는 대상 단어의 첫 글자 아래에 정렬되며, 14pt 바탕체 장체 95%의 측정
문자폭을 기반으로 계산한다. 텍스트 상자는 배경·테두리 없이 본문 위에
떠 있으며, 본문을 아래로 밀어내지 않음.

Annotations render only as the textbox form — omit any `style` field; other annotation styles are not supported.

Annotations **must be anchored to a specific word** whenever possible. A
whole-line note (no anchor) is acceptable only when the citation is a
genuinely umbrella one — e.g., "기사 전체의 출처".

**Never cite raw filenames** (e.g., `report.pdf`, `2024년_상반기.xlsx`,
`meeting_notes.docx`). A filename is a local artifact, not a citable source —
in the final document the reader has no idea which file that was. Cite the
actual **document title, publisher, organization, or source URL** instead.

| ❌ Don't | ✅ Do |
|---|---|
| `* 2024년_상반기_실적.xlsx` | `* 경영관리팀` |
| `* CES2026_keynote.pdf` | `* CES Keynote` |
| `* mckinsey_report.docx` | `* McKinsey Global Institute` |

**URLs are allowed as annotation text** when citing a 1차 소스 — 기사·
공식 발표·영상 등. 긴 URL을 서술로 바꿔 쓰지 말고, URL 자체 또는
`URL (매체명, 발행월)` 형태로 기재한다. 예:

- `https://openai.com/index/stargate-community/`
- `https://biz.heraldcorp.com/article/10650555 (헤럴드경제, 1/7일 기사)`
- `https://www.youtube.com/watch?v=xRh2sVcNXQ8 (1h 20m)`

**Dates are conditionally allowed — 사실적 의미를 지닐 때만.** 날짜가
사건의 시점, 기준 시점, 출처 발행월처럼 본문 해석에 필요한 정보일 때는
그대로 둔다. 반면 우상단 `date`와 중복되는 **장식적 꼬리표 날짜**는
제거한다.

| ✅ 허용 (사실적 의미) | ❌ 금지 (장식적 꼬리표) |
|---|---|
| 이벤트 시점: `'25.12.10, 아마존 정상회의` | 기관명 뒤 발행월만: `* Gartner, 2026.3` |
| 기준·관측 시점: `'26.1月 기준`, `'25年 착공` | 본문 최신성만 암시: `* 78% (2025)` |
| 출처 발행월: `출처: Reuters ('25.11月)` | 우상단 `date`와 같은 달을 반복 표기 |
| 비교 시점: `전년 동기 대비` | 모든 출처에 기계적으로 붙인 발행일 |

판단 기준: **그 날짜를 지우면 독자가 사실을 오독할 가능성이 있는가?**
그렇다면 유지, 아니라면 제거.

If no meaningful citation is available, omit the annotation entirely —
better no annotation than a filename.

The textbox renderer emits a DrawingML shape (`w:drawing` +
`wps:wsp`) with no fill, no border, and `wp:wrapNone` + `behindDoc="0"`
(줄 바꿈 = 텍스트 앞) — the box floats in front of text and does **not**
push body content. Because it doesn't reserve space, it can overlap the
next body line when the anchor sits in the middle of a multi-line bullet;
avoid that by anchoring on the bullet's last wrapped line, or by omitting
the annotation.

**Rendering target:**
```
  - 기업의 AI 채택률은 증가(78%→88%) 했으나, 이익 창출 기업은 6%에 불과
                          * McKinsey 2025
```
(the `*` lines up under the `7` of `78%→88%`)

**In content JSON — use the object form with `anchor`:**
```json
{
  "text": "기업의 AI 채택률은 증가(78%→88%) 했으나, 이익 창출 기업은 6%에 불과",
  "annotation": { "text": "McKinsey 2025", "anchor": "78%→88%" }
}
```

**The `anchor` must be an exact substring of `text`** — the first occurrence
is used to compute indent. If the anchor isn't found, the generator falls
back to a whole-line note (no indent) instead of failing.

**Whole-line (legacy) form — still allowed, use sparingly:**
```json
{
  "text": "…",
  "annotation": "TechCrunch 전체 기사 참고"
}
```

### Picking the anchor

Choose the shortest, most specific substring that the note is really about:

| Note content | Pick anchor on… |
|---|---|
| 약어 / 도메인 용어 해설 | 약어/용어 그 자체 (`MAU`, `TCO`, `SMR`) |
| 제품·기능 개념 설명 | 제품 토큰 (`Claw`, `Copilot Cowork`) |
| 숫자의 맥락·기준 | 해당 수치 (`78%→88%`, `7,440억 달러`) |
| 인물·조직 부연 | 인명·조직명 (`스테판 반셀`, `Global Atlantic`) |
| (선택) 출처 인용 | 인용 대상이 되는 숫자 또는 핵심 명사 |

Do **not** anchor on very short tokens that appear multiple times in the
bullet (`AI`, `M365`) — pick a longer substring that is unique within `text`.

**주석을 달 자리 — 해설이 실제로 필요한 곳에만:**

- 본문 한 줄에 조건·범위·비공개 사실을 짧게 덧붙일 필요 → 해당 수치·명사에 앵커, 한두 구절로 부연 (`지분율 비공개`)
- 낯선 약어·용어가 본문에 처음 등장 → 해당 토큰에 앵커, 짧은 풀이
- 숫자가 맥락 없이는 오독될 위험 → 그 숫자에 앵커, 기준·범위 보충
- 제품/기능명이 독자에게 생소 → 1회에 한해 개념 한 줄 해설
- 출처가 **그 자체로 신호**이고 섹션에 아직 표기 안 됨 → 대표 1줄에만
- 1차 소스(기사·발표·영상) URL이 인용 근거 → 해당 URL을 주석 본문으로 기재
- 인터뷰 아키타입에서 질문 원문을 보존 → 답변 요약 문장에 `(Q) …` 주석

**주석을 달지 말아야 할 자리:**

- 이미 같은 출처를 다른 주석·헤딩에서 표기함 (중복 금지)
- 숫자·사실이 본문만으로 충분히 이해됨 (불필요한 소음)
- 파일명밖에 댈 것이 없음 (§7 서두 규칙)
- 출처 기관명에 의미 없는 발행월만 꼬리표로 붙임 (장식 날짜 금지)

If the user explicitly asks for an annotation ("여기에 McKinsey 출처 넣어줘"),
honor it verbatim — anchor to the most natural term if you can infer it,
otherwise use the whole-line form.

---

## 8. Section heading framing

Each `□` section heading states a **topic**, not a sentence. Typical patterns:

- Descriptive: `□ 기사 개요`, `□ OpenClaw 개요`, `□ 신규 Claw 차별점 및 핵심 기능`
- Tagged: `□ [위협] Agentic IT 개발 도구의 급속한 확산`, `□ [기회] AI 시장확대`
- Action-oriented: `□ 향후 일정 및 SDS 시사점`, `□ 실행방안`

Keep them short. 5~25 characters is typical.

### Higher-level headings (Ⅰ·Ⅱ·Ⅲ, 1·2·3) — Optional tiers above `□`

For reports big enough that `□` sections alone can't carry the structure, promote headings with:

- `"numeral": "Ⅰ"` → renders as `Ⅰ. 제목` (16pt bold, no `□`) — Roman-numeral top-level chapter, typically in TOC-backed reports.
- `"number": 1` → renders as `1. 제목` (15pt bold, no `□`) — numeric sub-chapter, one level under a Roman-numeral chapter or as a mid-tier grouping in long reports.

Both are **optional**. The hierarchy is: Ⅰ → 1. → □ → - → ·. Use only as many top tiers as the content actually needs; for ordinary briefs, start at `□`.

Never combine the markers (`□ Ⅰ. …`, `Ⅰ. □ …`, `1. □ …` are all wrong) — the generator drops `□` automatically whenever `numeral` or `number` is set.

---

## 9. Document opening and closing

- **Opening**: `Title (centered, 20pt, not bold)` → `Date (right-aligned, 14pt)`
- **Closing (main body and each 별첨)**: `- 이  상 -` **right-aligned** at the
  bottom of the block. Note the **two spaces** between `이` and `상` (Korean
  public-document convention). The generator inserts this automatically —
  don't include it in the content JSON.

---

## 9-1. No meta / self-referential content — 주제로 바로 진입

보고서의 독자는 **주제에 대한 사실·시사점**을 보러 온다. "이 보고서가
어떻게 작성되었는가"는 독자 관심사가 아니다. 따라서 보고서 작성자·
조사자 관점의 메타 서술은 전부 빼고, 첫 섹션부터 주제 본문으로 바로
진입한다.

**금지 — 섹션 자체**

| 금지 헤딩 예시 | 대체 |
|---|---|
| `□ 검토 범위` | 삭제. 바로 `□ 개요` / `□ 주요 변화` / `□ 현황` 등으로 시작 |
| `□ 작성 기준` | 삭제 |
| `□ 조사 범위` / `□ 분석 방법` | 삭제 |
| `□ 본 보고서 개요` | `□ 개요`로 축약 (주제 개요이지 보고서 소개가 아님) |

**금지 — 메타 문장**

| Don't | Do |
|---|---|
| "본 보고서는 OpenAI 공개자료 기준으로 Images 2.0을 비교 정리" | (삭제) — 내용 자체로 바로 진입 |
| "핵심 관찰 포인트는 품질 향상보다 실무형 산출물에 있음" | "실무형 산출물 제작 범위 전면 확대"처럼 사실로 전환 |
| "~ 관점에서 해석" / "~ 기준으로 정리" | 해석·기준 프레이밍 삭제, 결론만 남김 |
| "이번 리뷰에서는 ~를 다룸" | (삭제) |

**예외 — 굳이 공개해야 하는 scope 단서**

공개 자료 限, 특정 기간 限 등 독자 판단에 실제로 영향을 주는 제약은
별도 섹션이 아니라 관련 섹션 하단에 **`※` 주 한 줄로** 붙인다.

예:
```
  ※ OpenAI 공개 자료 기준, 내부 수치는 非공개
```

**Rule of thumb** — 문장 앞에 "본 보고서는", "이번 분석은", "작성자는"을
붙일 수 있으면 그 문장은 메타 서술이다. 전부 삭제하거나 주제 사실로
전환한다.

---

## 10. 표 (Tables) — 폰트 크기와 정렬

표의 기본 폰트는 **12pt**다. 컬럼이 많거나 셀 텍스트가 길어서 한 줄에 담기
어려우면 `fontSize`로 9~14pt 범위 내에서 조정한다 (권장 범위).

| 상황 | 폰트 크기 |
|---|---|
| 기본 | 12pt |
| 컬럼 4개 이하, 텍스트 짧음 | 12~13pt |
| 컬럼 5개 이상 또는 셀 텍스트가 긺 | 10~11pt |
| 컬럼이 매우 많거나 페이지 폭 꽉 차는 긴 텍스트 | 9pt |
| 요약표·핵심 KPI 한 줄 | 13~14pt |

**셀 정렬 규칙:**

| 셀 종류 | 정렬 |
|---|---|
| **헤더(타이틀)** | 가운데 — 항상 |
| 일반 텍스트 (설명·명칭) | 좌측 (default) |
| **금액·소수점·천단위 구분자** (1,200억, 258B$, 45.0%) | 우측 — 자릿수·소수점을 맞춰 읽어야 함 |
| **동일 기준의 짧은 비교 숫자** (81%, 28%, 8%, 순위 1·2·10 등 ≤5자) | 가운데 — 비교 사다리처럼 읽힘 |
| **고정 길이 데이터** (코드·등급·기호 — 모든 셀 같은 길이, ≤8자) | 가운데 |

Rule of thumb: **"돈·소수점·쉼표가 보이면 우측, 순위·퍼센트처럼 짧은 비교 숫자면 가운데, 글은 좌측."**

생성기는 자동으로 판정한다. 직접 지정이 필요하면 `alignments: ["left","right","center"]`처럼 컬럼별 배열을 준다. (상세: `references/content-schema.md`)

**컬럼 너비:** 이제 기본이 **내용 기반 자동 산정**이다. 짧은 숫자·짧은 문자열 컬럼은 자신의 자연 폭을 유지하고, 긴 텍스트 컬럼이 나머지 페이지 폭을 흡수한다. `[긴 라벨, C-Suite, IC, Gap]` 같은 표에서 과거 `25% × 4`로 라벨이 2줄로 접히던 문제가 해소된다. 특정 비율을 강제하려면 `columnWidths: [3,1,1,1]` 같은 상대 가중치 배열로 override 할 수 있다.

---

## 11. 별첨 (Appendices)

Each 별첨 is a self-contained mini-document. It has:
- its own title
- its own date
- `□` sections like the main body
- its own `- 이  상 -`

Use 별첨 when the supporting material is substantive enough to deserve its
own title and would distract from the main topic if inlined. Rule of thumb:
if the material has its own headline, its own source, or its own date, it's
probably a 별첨.

Label: `별첨 1`, `별첨 2`, … (the generator handles the label).

---

## Quick self-check before generating

- [ ] Every bullet starts with `- ` or `·` or `□ ` (no freeform sentences)
- [ ] No `-습니다` / `-합니다` endings left
- [ ] No line over 55 Korean characters without a 6-space wrap
- [ ] 주석은 세 용도(**① 단문 맥락 보강 / ② 약어·용어 풀이 / ③ 출처 인용**) 중 하나에 해당하며, 같은 출처가 여러 주석에 반복 표기되지 않음 (중복 출처는 섹션 헤딩 1회 또는 대표 불릿 1회로 통합). 주석 속 날짜는 **이벤트·기준·발행 시점** 등 사실적 의미가 있을 때만 유지, 장식적 꼬리표 날짜(`* Gartner, 2026.3` 류)는 제거
- [ ] Each section heading is a topic, not a sentence
- [ ] Hanja limited to the §6-1 whitelist (single chars like 高·中·低, 年·月·週, 社, 有·無) — no 2+ character Hanja compounds (業務·使用·構築 등), no Hanja-Hangul splices (近로자, 生산성)
- [ ] 별첨 have been separated from main body where appropriate
- [ ] **No meta / self-referential content** — 검토 범위 / 작성 기준 등의 섹션 없음, "본 보고서는 ~" / "핵심 관찰 포인트는 ~" 같은 문장 없음, 첫 섹션부터 주제 본문으로 진입
