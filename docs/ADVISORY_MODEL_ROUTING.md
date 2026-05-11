# Advisory Model Routing

**Status**: Active draft  
**Owner**: Codex PMO  
**Created**: 2026-05-11  
**Related issues**: #36, #38, #39, #43

## Purpose

This document defines how to use the three interactive advisory lanes:

- Claude Chat
- Gemini Chat / Gems
- ChatGPT Business

The goal is to route work by role, purchased license, model/mode, token/capacity pressure, and source freshness risk.

## Current License Premises

These are operational assumptions based on user-provided context. Do not use this table as a procurement source of truth. Verify exact plan names, quotas, and billing terms only when making admin or purchasing decisions.

| Lane | Current license / access premise | Operational meaning |
| --- | --- | --- |
| ChatGPT Business | Business ChatGPT & Codex, 2 seats, Work Life Renovation workspace | Primary external advisory / PMO design lane. Second seat can be used as warm standby or controlled sub-account lane. |
| Claude Chat | Claude Pro | Human-context, wording, reflection, interpersonal nuance. Capacity can be shared with Claude Code / Cowork in practice, so Claude limits can affect the whole Claude lane. |
| Gemini Chat / Gems | Google Workspace paid / Plus-class premise and Gemini app access; Gemini 3 modes available | Long-context and token-relief lane. Especially useful when OpenAI / Claude capacity is tight. |
| Gemini CLI | Local Gemini CLI authenticated as user; observed Gemini Code Assist for individuals in CLI | Semi-automated review from repo root. Use read-first unless an action is explicitly scoped. |

## Core Routing Rule

```text
人にどう伝える？ -> Claude Chat
大量に読んで整理して -> Gemini Chat / Gems
構造としてどう設計する？ -> ChatGPT Business
実装・反映・Issue・Drive/GitHub -> Codex PMO
```

## Lane Definitions

### Claude Chat

Claude Chat is the human-context / wording / reflective PMO lane.

Use it for:

- interpersonal wording,
- relationship-sensitive messages,
- self-description and narrative reflection,
- motivation-aware PMO support,
- translating scattered feelings or concerns into practical next actions,
- drafting messages where tone matters.

Do not use it as:

- the main long-context intake lane,
- the main issue/SSOT updater,
- the main implementation lane,
- the primary tool during Claude capacity incidents.

### Gemini Chat / Gems

Gemini Chat / Gems is the long-context / broad-intake / token-relief lane.

Use it for:

- long documents,
- meeting notes,
- transcripts,
- field notes,
- Drive / GitHub / Notion export intake,
- broad consistency checks,
- first-pass task / issue / Notion candidate extraction,
- reducing context before sending work to Codex, Claude, or ChatGPT.

Do not use it as:

- a final write authority,
- a direct Drive / GitHub / Notion updater,
- the best lane for interpersonal tone polishing,
- a place to spend Pro capacity on trivial formatting.

### ChatGPT Business

ChatGPT Business is the external advisory / PMO design / structured judgment lane.

Use it for:

- PMO architecture,
- issue design,
- role-boundary review,
- postmortem synthesis,
- Token-aware Process Design,
- AI-BPaaS / deployment strategy abstraction,
- external advisor-style counterpoints,
- structured decision support.

Do not use it as:

- the direct source of truth,
- the primary Drive / GitHub / Notion updater,
- a substitute for source freshness checks,
- an execution lane when Codex PMO should apply the result.

## Model / Mode Routing

### Claude Chat

| Model / setting | Use | Capacity operation |
| --- | --- | --- |
| Opus 4.7 + adaptive thinking ON | High-stakes reflection, external-facing narrative, relationship-sensitive wording, human operating manual / motivation design updates | Reserve for important work. Claude Pro limits can block Claude Code / Chat / Cowork together. |
| Sonnet 4.6 + adaptive thinking ON | Default Claude Chat mode: day-to-day consultation, JC wording, PMO support, motivation-aware decomposition | Standard default. Best balance of quality and capacity. |
| Haiku 4.5 + adaptive thinking OFF | Lightweight rewriting, short summaries, LINE drafts, bullet cleanup, typo/wording fixes | Use to preserve higher-model capacity. |
| Haiku 4.5 or Sonnet 4.6 + adaptive thinking ON | Small tasks with some judgment | Use only when judgment matters; otherwise keep adaptive thinking OFF for transformations. |

Claude shortcut:

```text
Default: Sonnet 4.6 + adaptive thinking ON
Escalate: Opus 4.7 + adaptive thinking ON
Economize: Haiku 4.5 + adaptive thinking OFF
```

### Gemini Chat / Gems

| Mode | Use | Capacity operation |
| --- | --- | --- |
| 高速モード | Quick summaries, bullet conversion, first-pass classification, light reformatting | Use when quality risk is low. |
| 思考モード | Standard Gemini mode: issue candidate extraction, multi-file reading, moderate audit, fact/inference/action separation | Default Gemini Ops Lane mode. |
| Pro | Important cross-document audit, agenda AX, ontology/context extraction, AI-BPaaS / Token-aware synthesis, PMO handoff quality checks | Reserve for work that prevents PMO mistakes or large downstream rework. |

Gemini shortcut:

```text
Default: 思考モード
Escalate: Pro
Economize: 高速モード
```

### ChatGPT Business

| Model / setting | Use | Capacity operation |
| --- | --- | --- |
| Latest 5.5 Auto | Lightweight dialogue, quick question, ambiguous task where effort can be auto-adjusted | Useful for ordinary conversation. Not the authoritative review mode. |
| Latest 5.5 Thinking | Medium-weight comparison, policy review, trade-off analysis | Use when deliberate reasoning is needed but research-level depth is not. |
| Latest 5.5 Pro + effort Standard | Default ChatGPT Business Project setting: external advisory review, PMO design, issue design, role-boundary checks, postmortem synthesis | Primary ChatGPT advisory setting. |
| Latest 5.5 Pro + effort Extended | #39-class research, major architecture decisions, important postmortems, AI-BPaaS / Token-aware abstraction, external explanation drafts | Use selectively because it is heavier and slower. |

ChatGPT shortcut:

```text
Default: Latest 5.5 Pro + effort Standard
Escalate: Pro + effort Extended
Economize: Auto or Thinking
```

## Token / Capacity Operating Rules

1. Do not treat any paid plan as unlimited.
2. Track capacity by operational signals:
   - usage limit warnings,
   - degraded UI,
   - hard blocks,
   - reset times,
   - response latency,
   - answer quality,
   - rework rate,
   - whether a lower or higher mode should have been used.
3. Log capacity events in #38.
4. Route broader design lessons to #39.
5. Capacity incidents should record:
   - product / lane,
   - model / mode,
   - license / seat context,
   - limit type if visible,
   - reset time if visible,
   - work interrupted,
   - fallback lane used,
   - mitigation: wait / reroute / upgrade / add credits / seat switch,
   - source refresh needed after fallback.
6. A stronger model reading stale context is unsafe. Confirm source freshness before increasing reasoning effort.

## Source Freshness Rules

| Lane | Primary source risk | Required check |
| --- | --- | --- |
| Claude Chat | Project files / uploads may be stale; Drive connection must be explicit | Ask it to read the relevant Drive files or confirm current source. |
| Gemini Gems | Local initial attachments are stale snapshots unless Drive-linked | Prefer Drive-linked Knowledge Pack files under `50_Gemini_Knowledge_Pack`. |
| ChatGPT Business | Drive source may require manual resync / re-index after SSOT updates | Confirm source resync before important decisions. |
| Gemini CLI | Wrong cwd can cause wrong context; no sandbox state matters | Start from repo root and read `GEMINI.md` / docs. |

## Escalation / Fallback Patterns

### Claude capacity constrained

Use:

- Gemini for long-context intake and first-pass structure,
- ChatGPT Business for PMO design and issue architecture,
- Codex PMO for GitHub / Drive / issue reflection.

Avoid:

- starting new Claude Code / Chat / Cowork heavy tasks until reset.

### ChatGPT / Codex capacity constrained

Use:

- Gemini for heavy reading,
- Claude Chat for wording / human nuance if Claude capacity is available,
- manual handoff notes until Codex PMO recovers.

Avoid:

- assuming ChatGPT Business second seat can write to the same sources without role conflict.

### Gemini capacity or quality constrained

Use:

- ChatGPT Business for structured review if context size is manageable,
- Claude Chat for human-context review,
- Codex PMO to split files / reduce input / create smaller handoff packets.

Avoid:

- repeatedly retrying Pro on low-quality prompts without reducing scope.

## PMO Closeout Note

When an Issue changes this routing, update:

- `docs/TOOL_CONFIGURATION_REGISTER.md`
- `docs/PROJECT_OWNERSHIP_REGISTER.md`
- `docs/ADVISORY_MODEL_ROUTING.md`
- #36 for standard operation changes
- #38 for capacity alert changes
- #39 for Token-aware Process Design lessons
