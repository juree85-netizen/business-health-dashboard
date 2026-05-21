# Content JSON schema

This is the shape `scripts/generate.js` expects.

## Top level

```jsonc
{
  "title": "기업 개요",
  "date": "'26. 4. 15 (水)",
  "toc": { /* TOC cover page — optional, only if user asks */ },
  "sections": [ /* Section */ ],
  "appendices": [ /* Appendix */ ]
}
```

Notes:

- Do not place source/citation text above the title. `titleAnnotation` is not a valid field and will be ignored.
- Title renders bold + underlined; section headings (`□ …`) render bold. Body text stays regular weight.
- `toc` is **optional** and triggers the formal 목차 cover page. **Include it only when the user explicitly requests** a 목차 / TOC / table of contents / 목차 장표. If omitted, the document starts directly with the title block as before.
- **When `toc` is present, the body's centered title block and right-aligned date are auto-skipped** (the TOC page already carries them). The body begins directly with the first section. Override with `"skipTitleBlock": false` on the top level if you explicitly want the title repeated.

## `toc` — formal 목차 cover page (optional)

```jsonc
{
  "toc": {
    "reportTitle": "2024년도 영업지원 상반기 보고",
    "items": [
      "미청구 현황",
      "요금조정 및 1회성 청구 현황",
      "매출채권 현황",
      "빌링시스템 구축 현황"
    ],
    "appendix": {
      "label": "[별첨]",
      "items": [
        "1-1) 조직별 미청구 현황",
        "1-2) 장기 미청구 리스트",
        "2-1) 조직별 요금조정 현황",
        "2-2) 금액별 요금조정 현황",
        "3) 1회성 청구 세부내역",
        "4) 법인별 매출채권 회전기일 현황",
        "5) 신규 발생 90일 초과 채권"
      ]
    },
    "date": "2024. 3. 30",
    "author": "XX팀"
  }
}
```

Rendering:

- 상단: 굵은 테두리 안에 `reportTitle` (22pt bold, 중앙정렬)
- 중앙: `- 목    차 -` 라벨 (18pt bold, 중앙정렬, 목·차 사이 4-space)
- 본문 박스: 얇은 테두리 안에 `items[]`가 `1. …`, `2. …` 형식으로 나열 (16pt bold).
  - 각 항목은 문자열 또는 `{ "text": "…", "number": 2 }` 형태. `number`를 주면 자동번호 대신 그대로 사용.
- `appendix` (선택): `[별첨]` 라벨과 함께 `1-1)`, `1-2)` 같은 세부 항목을 14pt로 들여써서 렌더.
- 하단: `date` (18pt, 중앙) → `author` (20pt bold, 중앙, 자간 넓힘)
- 이 장표 뒤에 자동으로 페이지 나눔이 들어가고 본문(제목/일자/섹션/이 상 -)은 다음 페이지에서 시작.

모든 필드는 선택적 — 누락된 필드는 그 슬롯만 비운 채 렌더.

## Section

```jsonc
{
  "heading": "회사 개요",
  "headingAnnotation": {
    "text": "공식 홈페이지 기준",
    "anchor": "회사 개요"
  },
  "bullets": [ /* Bullet */ ]
}
```

`headingAnnotation` is optional and remains allowed.

### Section heading levels (optional extra tiers)

The default section heading is `□ 제목` (14pt bold). For large reports that need extra hierarchy above `□`, you can optionally promote a section with `numeral` or `number`:

| Field | Renders as | Size | When to use |
|---|---|---|---|
| `numeral: "Ⅰ"` | `Ⅰ. 제목` (no `□`) | 16pt bold | Top-level chapter in a **very large** report (typically TOC-backed) |
| `number: 1` | `1. 제목` (no `□`) | 15pt bold | Sub-chapter under a Roman-numeral chapter, or mid-tier grouping in a long report |
| *(neither)* | `□ 제목` | 14pt bold | **Default** — ordinary section |

Full hierarchy (top → bottom), with indentation preserved:

```
Ⅰ. 대분류              ← numeral (optional, 매우 큰 범위의 보고서)
   1. 중분류           ← number  (optional)
      □ 소분류         ← default section
         - 본문        ← dash bullet
            · 세부     ← dot bullet
```

`numeral` and `number` are **both optional** — use them only when the content is voluminous enough that `□` alone can't carry the structure. For ordinary briefs, keep the plain `□` style and do not introduce higher levels.

```jsonc
{
  "numeral": "Ⅰ",
  "heading": "Executive Summary",
  "bullets": [ /* … */ ]
}
```

```jsonc
{
  "number": 1,
  "heading": "시장 개요",
  "bullets": [ /* … */ ]
}
```

Rule: when `numeral` or `number` is set, the `□` prefix is **omitted** — these markers are higher-level than `□`, so never combine them. Use at most one of `numeral` / `number` on a single section.

## Bullet

```jsonc
{
  "kind": "dash",
  "text": "핵심 내용",
  "bold": true,
  "annotation": {
    "text": "출처 또는 보충설명",
    "anchor": "핵심"
  }
}
```

### Annotation forms

```jsonc
"annotation": "McKinsey 2025"
```

or

```jsonc
"annotation": {
  "text": "McKinsey 2025",
  "anchor": "78%"
}
```

#### Annotation rendering

Annotations render as a DrawingML 9pt blue **텍스트 상자** anchored under the target word. 배경 없음 / 테두리 없음 / 줄 바꿈 = 텍스트 앞 (`wp:wrapNone`, `behindDoc="0"`); 폭은 주석 길이에 맞춰 자동 계산. Do not set a `style` field — other annotation styles are not supported.

```jsonc
"annotation": {
  "text": "Bloomberg",
  "anchor": "AUM"
}
```

Rules:

- Prefer anchored annotations when the note explains a specific number, name, or term.
- Use whole-line string annotations only for umbrella citations.
- `anchor` must be an exact substring of the owning text.
- Section-level `headingAnnotation` follows the same rule.
- The textbox uses a DrawingML shape (`w:drawing` + `wps:wsp`) with `a:noFill` + `a:ln/a:noFill` for no background/border, and `wp:wrapNone` with `behindDoc="0"` for 텍스트 앞 wrap. Because the box sits in front of text, it does **not** reserve space — it can overlap the following bullet if the anchor is mid-paragraph of a multi-line bullet. Avoid that by choosing an anchor on the last wrapped line, or by omitting the annotation.
- **Never cite raw filenames** (`report.pdf`, `2024년_상반기.xlsx`, `meeting_notes.docx`, etc.) in annotations. The filename is a local artifact, not a citable source. Instead, cite the actual document title, publisher, organization, or source URL (e.g., `* 경영관리팀`, `* McKinsey Global Institute`, 기사 URL). If no meaningful citation is available, omit the annotation entirely.
- **Dates are conditionally allowed** — 사실적 의미를 지닐 때만 (이벤트 시점, 기준·관측 시점, 출처 발행월, 비교 시점). 장식적 꼬리표 날짜(기관명 뒤 발행월만 기계적으로 붙인 형태 `* Gartner, 2026.3` 등)는 우상단 `date`와 중복되므로 제거. 판단 기준: 그 날짜를 지우면 독자가 사실을 오독하는가? 자세한 규칙은 `references/tone.md` §7 참조.
- **URLs are allowed** when citing a 1차 소스 (기사·공식 발표·영상). URL 자체 또는 `URL (매체명, 발행월)` 형태로 기재.

## `kind` reference

| kind | renders as | use for |
|---|---|---|
| `dash` | `  - {text}` | main bullet |
| `dot` | `    ·{text}` | detail under a bullet |
| `wrap` | `      {text}` | continuation line |
| `note` | `  ※ {text}` | supplementary note |
| `arrow` | `    → {text}` | implication |
| `circled` | ` ① {text}` | ordered strategy item |
| `ordered` | ` 1) {text}` | numbered sub-section |
| `subhead` | `< {text} >` | mini-heading |
| `table` | table block | tabular content |

### `bold` (optional)

Set `"bold": true` on a bullet to render it in bold. Use this for key implications (`→`), summary takeaways, or action items that need emphasis. Do not overuse — limit to 1–3 critical lines per section.

### `scale` (optional)

Per-bullet character-width percentage. Default is 95 (inherited from the global 장체 95% rule). Lower it to 92 or 93 **only** when a long sentence wraps with a 1–2 character widow on the last line — tightening the letter-spacing pulls those characters up onto the previous line.

```jsonc
{ "kind": "dash", "text": "…long sentence that has only one widow character…", "scale": 92 }
```

Do **not** force every bullet onto a single line. Use `scale` surgically; most bullets should keep the default 95.

### Circled numbers (`①②③` — use at dash/dot level)

`kind: "circled"` with `index: 1/2/3…` renders `①②③…`. Circled numbers are a **formatting accent at the `-` (dash) or `·` (dot) level**, not a separate hierarchy tier. Use them when the content under a section is genuinely an ordered list — e.g., numbered strategy items, phased steps, ranked findings — and leave plain `dash` / `dot` for regular bullets. Mixing `dash` and `circled` within the same section is fine.

Do **not** use `①②③` to replace the Roman/number chapter levels (`numeral` / `number`) or the `□` section heading — those are structural; circled numbers are inline ordering only.

## Table

```jsonc
{
  "kind": "table",
  "columns": ["구분", "금액", "비중"],
  "rows": [
    ["A사업", "1,200억", "35%"],
    ["B사업", "800억",   "24%"]
  ],
  "fontSize": 12,
  "alignments": ["left", "right", "right"],
  "columnWidths": [3, 1, 1]
}
```

### `fontSize` (optional)

- **Default 12pt.** Accepts 9–14pt; values outside this range are clamped.
- Shrink (9–11pt) when the table has many columns or long text that would otherwise overflow.
- Grow (13–14pt) only for very short, visually prominent summary tables.

### `alignments` (optional)

Per-column array of `"left"` / `"right"` / `"center"`. Must have the same length as `columns`. When omitted, the generator auto-infers:

| Column content | Inferred alignment |
|---|---|
| Money / decimal / thousands-separator — 금액, 소수점, 자릿수 구분자 (e.g. `1,200억`, `258B$`, `45.0%`) | **right** (comma/decimal column alignment matters) |
| Short comparable numeric — 동일 기준 퍼센트·순위·소수량 (e.g. `81%`, `28%`, `8%`, `1`, `2`, `10`) | **center** |
| Fixed-length short strings — 모든 셀이 같은 길이, ≤8 chars (코드·등급·기호 등 `A`/`B`/`C`, `상`/`중`/`하`) | **center** |
| Mixed / longer text — 설명·명칭 | **left** |

Header row is **always centered**, regardless of body alignment.

Rule of thumb: **"돈·소수점·천단위 구분자가 보이면 오른쪽, 순위나 퍼센트처럼 짧은 비교 숫자면 가운데, 글은 왼쪽."** If a percentage column mixes short and long values (e.g., `8%` and `100%`) the auto-infer keeps it center as long as every cell is ≤5 chars with no decimal/currency marker. If you need a specific column right-aligned anyway, set `alignments` explicitly.

### `columnWidths` (optional)

Array of **relative weights** (same length as `columns`). `[3, 1, 1, 1]` gives the first column 3× the width of each of the other three; `[3000, 1000, 1000, 1000]` produces the same ratio — the numbers are rescaled to fit the page. Use this when the auto layout (see below) doesn't produce the proportions you want.

**Default (auto) behavior:** the generator no longer forces equal-width columns. It measures the natural content width of each column (max of header and body cells, in DXA, scaled by the table font size) and allocates width as follows:

- **Numeric or short-string columns** (≤6 chars) stay at their natural width — they don't need extra room and shouldn't wrap.
- **Long-text columns** absorb the remaining page width, proportional to their natural width. This is why a table like `[긴 설명 라벨, C-Suite, IC, Gap]` gives the label column ~65% of the row and the numeric columns ~10–12% each, instead of the old 25% × 4 where the label wrapped to two lines while numeric columns sat half-empty.
- Every column has a **minimum width floor** (~1.6 cm / 900 DXA) so even a 1-character numeric column isn't crushed.

Use `columnWidths` to override auto layout when you want a specific look — e.g., forcing equal width for a symmetric comparison table, or giving a mid-length column extra breathing room.

### `caption` (optional)

A short label rendered as a centered 14pt bold line **above** the table, wrapped in `< … >`. Use this for titled figure-style tables (e.g. `"장기간 대형 PJT 현황"` → `< 장기간 대형 PJT 현황 >`). Omit for unlabeled tables — most inline tables need no caption.

### `unit` (optional)

A unit label rendered as a right-aligned 10pt line between the caption (or directly above the table if no caption). The generator wraps it in parentheses automatically — pass `"건, 백만원"` and it renders `(건, 백만원)`. Use this **only when every numeric column shares the same unit(s)**; if columns have different units, omit `unit` and put the unit inside the header text instead (`금액(억원)`).

Both `caption` and `unit` are optional — a plain numeric table should not carry either.

### Complex merged tables — `cells` (optional)

For tables that need merged cells (stacked period headers, hierarchical row labels), use `cells` instead of `columns + rows`. This is an escape hatch — **do not reach for `cells` for ordinary tables**. Most tables are flat grids; `columns + rows` is the right default and results in cleaner JSON.

```jsonc
{
  "kind": "table",
  "caption": "분기 실적",
  "unit": "건, 억원",
  "headerRowCount": 2,
  "cells": [
    [ {"text":"구분","rowspan":2,"colspan":2}, {"text":"'25.1Q","colspan":2}, {"text":"'25.2Q","colspan":2} ],
    [ null, null, "건수", "금액", "건수", "금액" ],
    [ {"text":"합계","colspan":2}, "24", "62", "109", "392", null, null ],
    [ "국내", "A사업", "7", "14", "28", "226" ],
    [ null,   "B사업", "2", "3",  "16", "10"  ]
  ],
  "columnWidths": [1, 1, 1, 1, 1, 1]
}
```

Cell item forms (each slot in a row):

- **string** — single 1×1 cell (text only). Equivalent to `{"text": "…"}`.
- **object** `{ "text", "rowspan", "colspan", "align", "bold" }` — explicit descriptor.
  - `rowspan` / `colspan` default to 1. Use them to merge down/right.
  - `align` (optional): `"left" | "center" | "right"` — overrides per-cell inference.
  - `bold` (optional): force bold on a body cell (headers are already bold).
- **`null`** — marker for a slot **already covered** by a prior merge (rowspan from above, or colspan from the left). You must include `null` for every covered slot so the row still has the right column count; `cells` is a full 2D grid, not a sparse list.

### `headerRowCount` (optional, cells-mode only)

Number of top rows that should render as header (bold + centered). Default `1`. For stacked headers (period group + sub-label like 건수/금액), set `2` or `3` so all header tiers get header styling.

### `columnWidths` in cells-mode

With `cells` the generator cannot auto-infer column widths the way it does for flat tables (merges blur the natural-width signal). If you want specific proportions, pass `columnWidths` as an array of relative weights matching the full logical column count (same length as the longest row after expanding merges). If omitted, columns are split equally.

### Per-cell alignment in cells-mode

Header rows (top `headerRowCount` rows): centered, bold. Body cells: alignment is inferred **per cell** — numeric cells right- or center-align, text cells left-align. Override any cell with `"align": "..."`.

### Page-break behavior

Every table is rendered with two protections so the whole table stays on one page when it fits:

- `w:cantSplit` on every row — prevents a single row from splitting mid-cell across pages.
- `w:keepNext` on every paragraph in every row **except the last row** — forces Word to keep each row attached to the next one, so the entire table moves to the next page together rather than breaking between rows.

Caption/unit paragraphs also carry `w:keepNext` so they stay attached to the start of the table. Tables taller than a single page will still have to split between rows — there is no way around that.

This applies automatically; you do not need to configure anything.

Side effect: because `keepNext` is set on cell paragraphs, Word's editing view draws a ■ indicator in the left gutter next to every non-last row. This is visual only — it does not print, export to PDF, or otherwise affect the document. It is the cost of guaranteeing the table does not split mid-way across a page boundary.

Layout: the table is auto-indented so the first column starts at the same x-position as the surrounding `  - ` bullet text (not flush-left). Do not add manual indent — the generator handles it.

## Appendix

```jsonc
{
  "title": "별첨 제목",
  "sections": [ /* Section */ ]
}
```

Rendered as `#별첨N. <title>` at the top-left of a new page, then sections follow directly. Appendices do **not** render a centered title, a date, or `- 이 상 -`.

## Notes for authors

- Keep lines within roughly 30 to 55 Korean characters.
- Put citations in `annotation`, not in `text`.
- Keep section notes / implications after the main bullets in that section.
- The closing `- 이 상 -` is automatic.
