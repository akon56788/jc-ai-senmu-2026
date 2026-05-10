# Gemini Ops Lane Prompt Pack

**Status**: Initial prompt pack for Issue #37  
**Use with**: `Gemini Ops Lane` Gem or a normal Gemini chat with project context loaded.

## Field Intake

```text
mode: field-intake

Organize the following field notes, meeting notes, transcript, or rough memo.

Output:
1. Executive summary
2. Decisions already made
3. Open questions
4. Tasks with owner, due date, and source evidence when available
5. Risks / blockers
6. Notion Project DB / Task DB candidates
7. GitHub Issue candidates
8. Recommended handoff to Codex

Separate observed facts from your inferences.
```

## Notion Extraction

```text
mode: notion-extract

Convert the following material into Notion-ready project and task candidates.

For each project candidate, provide:
- Project Name
- Status
- Category
- Start Date
- End Date / deadline
- Description
- Related Projects
- Risks / Issues

For each task candidate, provide:
- Task Name
- Related Project
- Owner if known
- Due Date
- Status
- Notes

Do not claim that you updated Notion. Produce a handoff for Codex or Cowork.
```

## PMO Integrity Audit

```text
mode: audit

Review the provided context for operational consistency.

Focus on:
- contradictions between GitHub Mirror, Drive SSOT, Notion, and PMO rules
- unclear ownership across Codex, ChatGPT, Claude, Gemini, Gemini CLI, Code, and Cowork
- missing handoff or stop rules
- token-pressure risks and fallback gaps
- wording that could confuse a non-technical operator

Output:
1. Overall result: Blocker / Risk / Suggestion / No issue
2. Findings
3. Missing context
4. Recommended next action
```

## GitHub Issue Draft

```text
mode: github-issue

Draft a GitHub Issue from the following context.

Output:
- Title
- Background
- Purpose
- Scope
- Out of scope
- Acceptance criteria
- Related Notion / Drive / GitHub links
- Priority suggestion

Do not create the issue. Codex will decide and create it if needed.
```

## Token Relief Handoff

```text
mode: token-relief

Compress the following context for handoff to another AI tool.

Output:
1. Current goal
2. Important facts
3. Decisions made
4. Open questions
5. Next recommended actions
6. Files / links / references that matter
7. What the receiving AI should not redo

Keep it compact enough to paste into ChatGPT, Claude, or Codex.
```
