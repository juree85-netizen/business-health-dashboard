---
name: sds-word-writer
description: Convert raw materials into a Word (.docx) document written in the Samsung SDS in-house report style (Python runtime). Use when the user asks for a report, SDS-style document, or a formal Korean Word document based on notes, URLs, articles, transcripts, or mixed raw material.
---

# sds-word-writer (Python edition)

Turns rough input into a report in Samsung SDS in-house Word style, with optional appendices and an optional formal **목차 (TOC) cover page**.

## What this skill owns end-to-end

1. **Research and compose**
   Read the source material, fill obvious fact gaps, infer the right section structure, and write the report itself. Do not just reformat thin input.
2. **Rewrite in SDS tone**
   Use compressed noun-ending phrasing, one fact per line, and blue 9pt annotations for citations or side-notes attached to the line they explain.
3. **Structure**
   Use the canonical layout: centered **bold + underlined** title, right-aligned date, **bold** `□` section headings, `-` bullets, `·` detail lines, `※` notes, `→` implications, and right-aligned `- 이 상 -`.
   - Full heading hierarchy (top → bottom): **Ⅰ. (Optional, 매우 큰 범위 보고서) → 1. (Optional) → □ → - (dash) → · (dot)**. `Ⅰ.` and `1.` are reserved for reports long enough to need extra tiers — ordinary briefs start at `□` and never introduce Roman/number chapters. Promote a section with `"numeral": "Ⅰ"` (16pt bold) or `"number": 1` (15pt bold); the generator drops the `□` prefix automatically for those levels.
   - `①②③` are an **optional accent at the dash/dot level**, not a separate hierarchy tier — use only when the content is genuinely an ordered list.
   - Key implication lines (`→`) and action items may use `"bold": true` for emphasis.
   - Section separators are bold empty paragraphs.
4. **Format**
   Drive `scripts/generate.py` with content JSON. Never open Word directly.
5. **Attach appendices**
   If the user gives clearly separate supporting material, promote it to `#별첨1. <제목>`, `#별첨2. <제목>`, etc. — the label appears top-left on its own page and the appendix body continues directly (no centered title, no date, no `- 이 상 -`).
6. **(Optional) 목차 cover page**
   Only when the user **explicitly asks** for a 목차 / TOC / table of contents / 목차 장표, prepend a formal cover page in front of the body: boxed report title at top, centered `- 목    차 -` heading, a bordered box listing the main sections (and optional `[별첨]` sub-entries), then 발행일과 작성자/부서. If the user does not ask for one, do **not** add a TOC page — keep the current default layout.
   - **When `toc` is present, the body automatically skips the centered title block and the right-aligned date** — the TOC page already carries them, so the body starts directly with the first section. (This is the generator default; you don't need to set anything.)
   - **Roman-numeral chapter headings (Ⅰ, Ⅱ, Ⅲ …) are reserved for formal reports that include a TOC**. In the body JSON, set `"numeral": "Ⅰ"` on a section to render it as `Ⅰ. 제목` at 16pt bold. The generator will **omit the `□` prefix** for numeral-marked sections, because the Roman numeral is a higher-level marker than `□` — **never combine both**. For ordinary reports (no TOC), keep the plain `□ 제목` style; do not introduce Roman numerals.

## Non-negotiable rules

- The title must never carry a source annotation. Source/citation annotations belong only to section headings or body bullets.
- Titles render bold + underlined; section headings (`□ …`) render bold. Body bullets and details stay regular weight.
- Appendices have **no** centered title block, **no** date, and **no** `- 이 상 -` closing. Only the main body has those.
- **Annotations have three use cases, in rough frequency order**: (a) **단문 맥락 보강** — 조건·범위·전제·비공개 사실을 한두 구절로 부연 (`지분율 비공개`, `규모 未공개`, `연결 기준`, `거래 종결시`); (b) **약어·도메인 용어 풀이** (`MAU : 월간 활성 사용자 수`, `Wafer-Scale Engine`); (c) **출처 인용** — 출처 자체가 신호일 때만 (`McKinsey`, `Gartner`, `Reuters` 등). 출처는 세 용도 중 가장 드문 쪽이지 기본 동작이 아님.
- **Allowed prefix patterns**: `출처:`, `예)`, `(참고)`, `(추가)`, `(Q)` (인터뷰 질문 원문 보존). 내용이 실제로 prefix에 해당할 때만 사용.
- **URLs are allowed as annotation text** when citing a 1차 소스 (기사·공식 발표·영상). URL 자체 또는 `URL (매체명, 발행월)` 형식으로 기재 — 서술로 재작성하지 않는다.
- **Dates are conditionally allowed — 사실적 의미를 지닐 때만.** 허용: 이벤트 시점 (`'25.12.10, 아마존 정상회의`), 기준·관측 시점 (`'26.1月 기준`, `'25年 착공`), 출처 발행월 (`출처: Reuters ('25.11月)`), 비교 시점 (`전년 동기 대비`). 금지: 장식적 꼬리표 날짜 — 기관명 뒤에 의미 없이 붙은 발행일 (`* Gartner, 2026.3`), 본문 최신성만 암시하는 날짜. 우상단 `date`와 중복되는 날짜는 제거.
- **Never repeat the same source across multiple annotations in one report.** If every bullet in a section is from McKinsey 2025, do **not** tag `* McKinsey 2025` on each line. Attach the source once (e.g., on the section heading via `headingAnnotation`, or on the single most representative bullet) and leave the rest clean.
- **Never cite raw filenames in annotations** (e.g., `report.pdf`, `2024_상반기.xlsx`). A filename is a local artifact, not a citable source. Cite the actual document title, publisher, organization, or source URL instead (e.g., `경영관리팀`, `McKinsey Global Institute`, 기사 URL). If no meaningful citation exists, omit the annotation.
- **No meta / self-referential content.** The reader wants facts about the subject, not a description of how the report was produced. Do **not** create sections like `검토 범위` / `작성 기준` / `분석 방법` / `조사 범위`, and do **not** open bullets with phrases like "본 보고서는 …", "핵심 관찰 포인트는 …에 있음", "~ 기준으로 비교 정리", "~ 관점에서 해석". The first section must step straight into the subject matter (개요 / 동향 / 현황 / 주요 변화 등). If scope genuinely needs disclosure (e.g., "분석 대상은 공개 자료 限"), fold it into a single `※` note under the relevant section — never a standalone opening section.
- Heading hierarchy order is fixed: `Ⅰ. → 1. → □ → - → ·`. `Ⅰ.` and `1.` are optional top tiers; never reverse the order, and never combine `Ⅰ.` / `1.` with the `□` prefix on the same heading.

## When to use

Use this skill when the user:

- asks for a report / 보고서 / 브리프 / 제언 / Word 문서 / docx
- asks for SDS style or a Korean business brief
- gives raw material and expects a polished Korean corporate document
- asks to rewrite existing content into SDS in-house report tone

## Procedure

### Step 0. Plan the structure (ideation)

Before writing, read `references/report-archetypes.md` and use it to
**ideate the section skeleton**. The catalog lists 8 recurring archetypes
(기업개요 / 이벤트요약 / 시장분석 / 기술개요 / SDS 제언 / 주간보고 /
업무계획 / 현안보고) and one common-DNA set shared across all of them.

The archetype catalog is an **ideation palette, not a template**:

- Real reports are almost always **hybrids** — e.g., an investment-impact
  analysis that ends with a company-overview trailer, or a weekly status
  that folds a mini-issue report inside. Draw blocks from multiple
  archetypes as needed.
- **Drop any section the input doesn't actually support.** If the raw
  material has no revenue data, do not invent a `경영실적` section. If
  there's no clear SDS action item, do not tack on a fake `제언` block.
  An empty or invented section is worse than no section.
- Reorder, merge, rename, or omit freely so the **reader** can scan the
  brief quickly. Comprehension is the goal; conformance to a pattern
  never is.

Once you have a skeleton composed from *what the input actually supports*
(not from a template), move to Step 1.

### Step 1. Read, classify, and research

Figure out:

- **Main topic**: the subject of the one-page body
- **Date**: use `'YY. M.D (曜)` with the correct single-character weekday in Asia/Seoul unless the user provides a date
- **Appendices**: separate material that deserves its own mini-document
- **Sources / citations**: URLs, publication names, dates, or quote attributions to place in blue 9pt annotations

Fill gaps actively. If the user gives only a few facts, research adjacent facts and produce a complete brief.

### Step 2. Rewrite in SDS tone

Read `references/tone.md` before writing.

Key rules:

- strip narrative padding
- one fact per line
- target 30 to 55 Korean characters per line
- prefer noun endings / compressed endings over conversational prose
- use Hanja sparingly — default to Hangul; reserve Hanja for conventional single characters (`高`·`中`·`低`, `年`·`月`·`週`·`日`, `社`, `有`·`無`, `內`·`外`, `前`·`後`, 요일 Hanja 등). Avoid 2+ character Hanja compounds (業務·使用·時間·構築·導入·創出 → 업무·사용·시간·구축·도입·창출) and never splice a Hanja character onto a Hangul stem (近로자·生산성 → 근로자·생산성). See `references/tone.md` §6 for the full rule.
- keep citations and tangential context in blue 9pt annotations, ideally anchored to the exact word or number they explain

### Step 3. Build the content JSON

Write JSON matching `references/content-schema.md` (schema is identical to the Node edition).

Minimum shape:

```json
{
  "title": "기업 개요",
  "date": "'26. 4. 15 (水)",
  "sections": [
    {
      "heading": "회사 개요",
      "bullets": [
        {
          "kind": "dash",
          "text": "핵심 내용",
          "annotation": { "text": "출처", "anchor": "핵심" }
        }
      ]
    }
  ],
  "appendices": []
}
```

Notes:

- Do **not** add any source/citation field above the title. `titleAnnotation` is no longer supported.
- `annotation` on bullets can be either a plain string or `{ "text": "...", "anchor": "..." }`. Annotations always render as the textbox style — a DrawingML 텍스트 상자 (배경 없음 / 테두리 없음 / 줄 바꿈 = 텍스트 앞), anchored 9pt blue 배지 below the anchor word. Do not set a `style` field; other annotation styles are not supported.
- `headingAnnotation` is still allowed for section headings (textbox only).
- `bold`: set `true` on bullets that need emphasis (key takeaways, `→` implications).
- `scale`: optional per-bullet character-width override (default 95). When set manually, the value is applied uniformly to **both** the bullet mark (prefix) and the sentence body, and disables auto widow fix (below). Use a manual override only when you want a specific uniform compression.
- **Auto widow fix** (automatic, no config): when a bullet wraps to ≥2 lines and the **last wrapped line has only 1–2 words**, the generator tries tightening the sentence body's 장평 in steps `94 → 93 → 92 → 91 → 90` and picks the first value that eliminates the short tail. The bullet mark (prefix — `-`, `·`, `→`, 원문자 등) stays at 95% — only the sentence body is compressed. If 90% still cannot resolve the widow, the generator reverts to the original wrap and keeps 95% scale everywhere (no side effects). Disabled whenever the bullet has a manual `scale` field.
- `numeral` / `number` on a section: optional higher-level heading (`Ⅰ.` 16pt / `1.` 15pt). Use only when the report needs a tier above `□`; the generator drops the `□` prefix automatically. Never combine with `□`.
- Circled numbers (`kind: "circled"`): optional dash/dot-level accent for genuinely ordered lists. Not a hierarchy tier — do not use in place of `numeral` / `number` / `□`.
- Tables: default 12pt. Set `fontSize` to adjust within 9–14pt when columns are many or text is long. Columns auto-align by content: money/decimal/thousands-separator values → right; short comparable numeric (`%`, 순위 등 ≤5 chars, no decimal/currency marker) → center; fixed-length codes/grades → center; else left. Override with per-column `alignments: ["left","right","center"]` when needed. Header row is always centered. Column widths are content-aware by default (long-text columns absorb extra page width, numeric columns stay narrow at their natural width, ~1.6 cm minimum floor); override with relative weights `columnWidths: [3,1,1,1]` when a specific ratio is needed.
- **Tables — default = 단순 표.** Keep `columns + rows` as the default. Only reach for the extra table features below when the **content actually requires** them — do not bolt them onto every table.
  - `caption` (optional): 표 위 중앙정렬 14pt 굵은 `< 제목 >`. 재무 집계 표처럼 명시적 표 제목이 있을 때만 사용. 본문 흐름 속 단순 비교 표엔 불필요.
  - `unit` (optional): 표 위 우측정렬 10pt `(단위)`. 표 **모든 수치 열이 같은 단위를 공유**할 때만 사용 (`"건, 백만원"`, `"억원"` 등). 열마다 단위가 다르면 `unit`을 쓰지 말고 헤더에 단위 병기(`금액(억원)`).
  - `cells` (optional, 복합 병합): `columns + rows`로 표현 못 하는 표 — 기간 그룹 헤더, 계층 행 라벨, 2차원 계층 등 — 에만 사용. 단순 격자 표는 절대 `cells`로 쓰지 말 것. 스키마: [content-schema.md](references/content-schema.md) 참고.
  - 페이지 분리 방지는 **자동** — 모든 표에 기본 적용. 표와 캡션·단위가 페이지 끝에 걸치면 통째로 다음 페이지로 이동. 설정 불필요.
- Annotations: never put a raw filename (`*.pdf`, `*.xlsx`, `*.docx`) in the annotation `text`. Cite the document title / organization instead, or omit the annotation. Also never include date tokens (`2026.4.21`, `'25.3`, `Q1`, `2024년` 등) — the top-right report date already covers recency.
- Appendix entries in `appendices[]` only need `title` and `sections`; `date` is ignored.
- **Optional** top-level `toc` triggers the formal 목차 cover page (see `references/content-schema.md`). Add it **only when the user explicitly requests** a 목차/TOC; otherwise omit the field and fall back to the default layout.

### Step 4. Generate the .docx

```bash
python scripts/generate.py <content.json> <output.docx>
```

If `python-docx` is not yet installed, the script auto-installs it on first run (via `pip install -r requirements.txt`). Python 3.9+ recommended.

Generator behavior:

- A4, 2cm margins
- body 14pt, title 20pt, annotations 9pt
- `autoSpaceDE="0"` / `autoSpaceDN="0"` on every paragraph (prevents CJK/Latin auto-spacing)
- body line spacing 240 auto; wrapped lines within the **same** bullet use after=180 (9pt) between rows, while the last wrapped line keeps the normal 12pt gap to the next bullet
- annotation line spacing 200 exact (9pt)
- title: bold + underline, after=240; date: right-aligned, after=240
- section heading (`□ …`): bold; everything else regular weight unless `bold: true`
- section separators: bold empty paragraph with after=240
- annotations — **textbox only**: DrawingML 텍스트 상자 (`w:drawing` + `wps:wsp`) anchored under the target word. 배경 없음 (`a:noFill`), 테두리 없음 (`a:ln/a:noFill`), 줄 바꿈 = 텍스트 앞 (`wp:wrapNone`, `behindDoc="0"`). 바탕체 9pt #0000FF, 장체 95%. 프레임 폭은 주석 길이에 맞춰 자동 계산. 텍스트 앞 배치라 본문을 밀어내지 않음 — 멀티라인 bullet 중간 앵커가 다음 라인과 겹칠 위험이 있으면 앵커 단어를 조정하거나 주석을 생략한다.
- wrapped lines use a hanging indent so continuation starts under the text, not the bullet mark
- colon-based hanging indent: when a bullet contains `" : "`, wrapped continuation starts at the character after the colon, aligning the value column (e.g., `설립 : 1976년 미국 뉴욕` wraps under `1976…`)
- tables are indented to start at the same x-position as the bullet text above them (not flush-left)
- tables default to 12pt; `fontSize` clamps to 9–14pt for dense or long-text tables
- table column widths: content-aware by default — each column gets `max(header, body) DXA` as its natural width; numeric/short-string columns stay at natural width, long-text columns absorb the remaining page width, 900 DXA floor applies. Override with `columnWidths: [weights]` (relative).
- table cell alignment: header row always centered; body cells auto-inferred (money/decimal/thousands → right, short comparable numeric ≤5 chars → center, fixed-length short strings → center, else left) or explicitly set via `alignments`
- table borders: single black line; header row centered, no shading
- `- 이 상 -` is right-aligned with after=180; inserted automatically in the main body only
- appendix label renders as `#별첨N. <title>` at the top-left of a new page, then the sections follow directly
- page numbers render as `- N -` centered in the footer (12pt 바탕체, 바닥글 0.9cm)

Do **not** place citations above the title.

### Step 5. Validate and return

Validate the resulting `.docx` if possible, then return the output path and a one-line summary.

## Edge cases

- English input: translate to Korean, then apply SDS tone
- Existing doc input: extract text first, then rewrite
- Very long input: split into body + appendices
- Tables: use `"kind": "table"` when the content is inherently tabular
- No date given: default to today in Asia/Seoul

## Files in this skill

- `SKILL.md`
- `references/tone.md`
- `references/content-schema.md`
- `references/report-archetypes.md`
- `scripts/generate.py`
- `assets/example.json`
- `assets/example.docx`
- `requirements.txt` (runtime dep: `python-docx` — auto-installed on first run if missing)
