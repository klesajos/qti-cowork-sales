> 🌍 Read this in: **English** | [Česky](02-brand.cs.md)

# 02 · Brand: voice and visual identity

Brand in Claude lives in three places. Know which one does what:

| Where | What it holds | Who sets it up | Used by |
|---|---|---|---|
| Skill `quanti-brand` (plugin) | Colours, type, logo rules, tone, claims policy, a final checklist | Sales lead, once; shipped in the plugin | Every file Claude writes in Cowork: PPTX, DOCX, XLSX, PDF |
| **Design system** (Settings → Capabilities → Design systems) | Visual styles extracted from your assets | Whoever owns the brand; *Published* makes it the org default | Claude Slides, Claude Design and HTML artifacts |
| Project or conversation files | Brand brief, logos, tone corpus | Anyone | Only that project or conversation |

The skill is the one rule set that travels with every task. The design system makes the
visual tools (Slides, artifacts) start on-brand. Keep both in sync from one source,
`sample-data/brand/tokens.json`.

## Tone of voice from real texts

`sample-data/tone-corpus/` holds 58 public quanti.cz texts (blog, references, services). That
is enough for Claude to describe how Quanti writes, with quotes as evidence, instead of
inventing a voice. The `brand-voice` plugin from Anthropic's catalogue (skills
`discover-brand`, `guideline-generation`, `brand-voice-enforcement`) automates this across
Notion, Drive or Confluence; with plain files, a prompt does the same.

What to look for in the result: concrete do / don't pairs, quotes from the corpus, and words to
avoid. Then compare with the tone section of `quanti-brand` and improve the skill.

## A design system from assets

Upload the brand manual PDF, `brand-brief.md`, `tokens.json`, both logos and the Montserrat
fonts. Claude extracts colours, type and components and shows a preview. Check the preview against the brief before
publishing: uppercase headings, rounded cards instead of the cut-corner panel, the logo not
bottom-right and a default font are typical first-run misses.

> Standalone Claude Design (claude.ai/design) closes on **14 Dec 2026**. Design systems stay
> under Settings → Capabilities → Design systems; on Enterprise plans an admin must enable
> them first (Organization settings → Artifacts).

## The claims rule

The biggest brand risk in sales is not a wrong colour; it is a number nobody can back. The skill
allows numbers, clients and certificates only from the task's inputs or
`approved-claims.md`, and writes `[DOPLNIT: …]` otherwise. Expect to see those markers; they are
the feature, not a bug.
