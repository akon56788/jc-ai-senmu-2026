# PMO Fallback Environment

**Status**: Active draft  
**Owner**: Codex PMO  
**Created**: 2026-05-11  
**Related issues**: #38, #44, #45, #36, #39

## Purpose

Codex PMO can become temporarily unavailable because of usage limits, 5-hour limits, message limits, app errors, connector errors, or local environment issues.

This document defines how PMO work continues when Codex PMO is unavailable.

The model is an acting-manager model:

```text
Codex PMO = regular PMO manager
Fallback tool = acting PMO delegate
User = final approver
Fallback PMO Handoff = handover memo
Codex recovery check = manager review after return
```

The acting delegate can handle urgent scoped work, but must leave evidence, open questions, and recovery notes for Codex PMO.

## Core Principle

```text
Fallback write is not autonomous write.
Fallback write = user-confirmed provisional operation + audit trail + Codex recovery check.
```

## Default Fallback Rule

```text
Codex PMO down = ChatGPT Business drafts + Gemini reads + User decides + Codex reconciles after recovery
```

If another tool performs a write action during fallback operation, it must:

1. show the target and update content to the user first,
2. receive explicit user confirmation,
3. record that the action was performed under fallback PMO operation,
4. leave a `Fallback PMO Handoff`,
5. tell Codex PMO what to check after recovery.

## Fallback Triggers

Use this workflow when any of the following occurs:

- Codex usage limit / 5-hour limit / message limit is reached.
- Codex automation stops before completing a PMO task.
- Codex cannot access GitHub, Drive, Notion, or local workspace.
- Codex cannot respond but another AI lane is available.
- User explicitly asks another AI to continue PMO work.
- A weekly/daily automation cannot complete because the main PMO lane is unavailable.

## First Response During Codex PMO Down

The fallback tool should first produce a short triage:

```markdown
## Fallback PMO Triage

Codex state:
- unavailable / degraded / unknown

User request:
- ...

Likely parent issue:
- #38 / #36 / #39 / #42 / #45 / other

Recommended action:
- comment existing issue / create incident issue / create countermeasure issue / draft only

Write authority:
- Level 0 / Level 1 / Level 2 / Level 3

Need user confirmation before write:
- yes / no
```

## Issue Routing Rule

Capacity / Token / usage limit context should route to #38 first.

```text
Token死 / 使用上限 / 5時間制限 / usage limit / Codex limit / Claude limit / Gemini capacity
=> Prefer #38 comment first.
```

Create a new Issue only when:

- there is a distinct incident record,
- there is a recovery task,
- there is permanent countermeasure work,
- there is implementation work,
- the user explicitly asks for a new Issue.

## Tool Roles During Fallback

| Tool | Fallback role | Write stance |
| --- | --- | --- |
| ChatGPT Business | PMO design, issue draft, handoff draft, external advisory review | Draft by default. Scoped write only with user confirmation. |
| ChatGPT Business second seat | Warm standby PMO continuation | Same as ChatGPT Business. Avoid double-writing without handoff. |
| Gemini Chat / Gems | Long-context reading, messy note intake, broad audit, status compression | Draft only. No direct production update. |
| Gemini CLI | Repo-root read-first audit, issue routing recommendation, docs update proposal | Draft/read-first unless explicitly scoped. |
| Claude Chat | Human-context wording, user-facing explanation, soft handoff, light triage | Draft by default. |
| Claude Code | Repo/docs implementation fallback if Claude capacity is available | Scoped technical write with user confirmation. |
| Claude Cowork | Notion/Sheets/Drive operational fallback | Scoped operational write with user confirmation. |
| User manual | Final authority during fallback | Can execute emergency writes manually. |

## Write Authority Levels

### Level 0: Read-only

Allowed:

- Read Issue body, comments, labels, and state.
- Read Drive/GitHub/Notion context where connected.
- Identify likely parent Issue.
- Recommend comment vs new Issue.

Not allowed:

- Write comments.
- Create Issues.
- Close/reopen Issues.
- Change labels, projects, milestones, or docs.

### Level 1: Draft-only

Allowed:

- Draft a comment.
- Draft a new Issue.
- Draft a close/reopen note.
- Draft a Codex recovery handoff.

Not allowed:

- Execute the update.

### Level 2: 明示スコープ内・軽量確認付きIssue書き込み

Use for:

- Single comment to a clearly specified Issue.
- Small update where the target and purpose are obvious.
- Capacity Alert comment to #38.

Before write:

1. State target Issue.
2. Show summary of the update.
3. Ask for / receive user confirmation.

After write:

1. Return the GitHub URL.
2. Note fallback operation if relevant.
3. Mark whether Codex recovery check is needed.

Suggested note:

```markdown
Note: This comment was added during fallback PMO operation while Codex capacity was constrained. Codex PMO should review this entry after recovery.
```

### Level 3: ユーザー事前確認付き・代替PMO暫定更新権限

Use for:

- New Issue creation.
- Cross-Issue comments.
- Issue close / reopen.
- Label / project / milestone changes.
- Docs update plus Issue reflection.
- Drive/GitHub/Notion-crossing PMO decisions.

Before write:

1. List all targets.
2. Show the exact or summarized update.
3. State this is fallback PMO operation.
4. State risks and unknowns.
5. Get explicit user confirmation.

After write:

1. Return all URLs.
2. Leave a `Fallback PMO Handoff`.
3. Identify first checks for Codex PMO after recovery.

## Codex Recovery Check

When Codex PMO recovers, it should not immediately resume normal work. First it should:

1. Read #38, #45, and the latest fallback handoff.
2. Review fallback comments, new Issues, closes, labels, and docs changes.
3. Check for duplicate Issues, wrong parent Issues, missing links, or stale source use.
4. Reconcile Drive SSOT, GitHub Mirror, Notion, and local files.
5. Add correction comments if needed.
6. Report the fallback handoff review result to the user.

## Required Fallback Handoff

Any Level 2 or Level 3 write should leave or link a handoff using:

- `docs/PMO_FALLBACK_HANDOFF_TEMPLATE.md`

Minimum handoff fields:

- Reason
- Actions performed
- User confirmation
- Sources read
- Pending review for Codex recovery
- Risks / possible gaps
- Next owner

## Implementation Targets

Primary docs:

- `docs/PMO_FALLBACK_ENVIRONMENT.md`
- `docs/PMO_FALLBACK_HANDOFF_TEMPLATE.md`
- `docs/ISSUE_OPERATION_FALLBACK.md`

Related docs to keep aligned:

- `docs/PMO_REPORTING_WORKFLOW.md`
- `docs/TOOL_CONFIGURATION_REGISTER.md`
- `docs/PROJECT_OWNERSHIP_REGISTER.md`
- `docs/ADVISORY_MODEL_ROUTING.md`
- `docs/GEMINI_OPS_KNOWLEDGE_PACK.md`

Related Issues:

- #38 Capacity Alert operation
- #44 Codex limit incident
- #45 PMO fallback environment
- #36 PMO standardization
- #39 Token-aware Process Design
