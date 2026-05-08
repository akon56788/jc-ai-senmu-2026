# PMO Reporting Workflow

**Date**: 2026-05-08
**Status**: Phase 1 operating draft

---

## Purpose

This workflow defines the lightweight reporting gate between Code, Cowork, Codex, and Codex PMO.

The goal is to keep the project observable without turning every task into a heavy approval ceremony.

---

## Default Rule

Every tool task should leave a short PMO handoff when it finishes or pauses.

Use the normal three-line PMO report unless the work changes coordination rules, automation, permissions, SSOT structure, or tool role definitions.

For small tasks that do not have a GitHub Issue or PR, the handoff can stay in the active chat thread. If the task affects shared operations or future reference, promote it to a GitHub Issue, PR, or Drive SSOT note.

```markdown
**PMO Handoff**
- Status: Done / Paused / Blocked
- Changed: [files, PR, Drive doc, Notion item, or N/A]
- Next: [owner and next action]
```

---

## Detailed PMO Check

Use detailed PMO mode when one or more are true:

- GitHub main, branch, PR, or Actions changed
- the work is submitted as a Pull Request, even if the underlying change is small
- Drive SSOT structure, Google Docs ownership, or core `.txt` context rules changed
- context file content changed in a way that affects tool roles, handoff rules, PMO rules, naming rules, or external review rules
- Notion / Sheets / Drive operational data changed
- tool responsibility, handoff, or naming rules changed
- permissions, CLI tools, automation, or workflow scripts changed
- the task was performed by Codex as a substitute for Code / Cowork / Chat

Small wording fixes, typo corrections, or low-risk content updates can stay in the three-line PMO report if the next owner and SSOT impact are clear.

```markdown
**Detailed PMO Check**
- GitHub: N/A / Updated / PR [#] / CI pass / CI fail
- Drive SSOT: N/A / Updated / Pending sync / Diff risk
- Notion or Sheets: N/A / Updated / Pending / Blocked
- External Review: Not needed / Requested / Completed / Blocked
- Risk: None / [specific risk]
- Next Owner: User / Codex / Code / Cowork / Chat
- Next Action: [specific next step]
```

---

## Engagement System Integration（エンゲージメント・テンプレート運用）

As of 2026-05-08, the PMO workflow is integrated with the engagement system (`docs/pmo_engagement_template.md`, `docs/kondo_core_roles.md`, `docs/llm_engagement_systemprompt.md`).

**When assigning tasks to 近藤さん（近藤）:**

1. Use the engagement template structure for task descriptions:
   - 【タスク】What is the work?
   - 【効果】What impact will this have (short/medium/long-term)?
   - 【あなたの役割】Which core role (Role 1–5) applies?
   - 【チーム/組織への影響】How does it ripple to the team/org?

2. Reference core roles from `docs/kondo_core_roles.md` (5 roles: complex information structuring, tool design, connector/bridge, iterative growth, empowering hero)

3. **For LLM usage:** Codex / Code can embed the LLM system prompt (`docs/llm_engagement_systemprompt.md`) in Claude API calls or chat context to provide consistent engagement support

4. **First operational phase:** Use this template as a candidate format for monthly/weekly task descriptions; lighten if operational load is too heavy

**Related files (GitHub SSoT + Drive Mirror):**
- GitHub SSoT: `docs/pmo_engagement_template.md`, `docs/kondo_core_roles.md`, `docs/llm_engagement_systemprompt.md`
- Drive Mirror: See `DRIVE_SYNC_STATUS.md` for mirror file IDs
- Memory: `memory/narrative_engagement_system.md`

---

## Gemini Review Trigger

Gemini review is recommended for important changes, not for every small task.

Run or request Gemini review when one or more are true:

- SSOT (Single Source of Truth / master reference) synchronization rules change
- GitHub Actions, scripts, CLI setup, or automation changes
- Drive / GitHub / Notion coordination changes
- tool roles, PMO rules, handoff rules, or permissions change
- a PR (Pull Request / change request) introduces meaningful operational risk
- the user asks for objective review, counterargument, or second opinion

Skip Gemini review for typo fixes, simple formatting, obvious file copies, or low-risk reporting updates.

Command:

```powershell
python scripts/external_review.py --target docs/PMO_REPORTING_WORKFLOW.md --question "Review PMO reporting gate risk" --run-gemini
```

---

## Tool-Specific Expectations

### Code

- Report GitHub PR / CI / merge state to Codex PMO.
- Mention whether Drive SSOT sync is needed.
- Request Gemini review before merging workflow, Actions, or role-rule changes.

### Cowork

- Report Notion / Sheets / Drive operation status to Codex PMO.
- Mention any pending user confirmation or schedule risk.
- Ask Codex PMO to generate or run Gemini review when operational rules change.

### Codex As Worker

- When Codex acts as a substitute for Code, Cowork, or Chat, leave the PMO handoff anyway.
- Clearly separate "work performed" from "PMO assessment."
- Use Gemini review for important changes before or immediately after PR creation.

### Codex PMO

- Triage incoming handoffs.
- Decide whether the three-line report is enough or detailed PMO mode is needed.
- Run Gemini review when trigger conditions are met.
- Reflect confirmed changes to GitHub and Drive SSOT.

---

## Acceptance Standard

A task is PMO-complete when:

- the changed artifact is named or linked,
- the current status is clear,
- the next owner is clear,
- SSOT / GitHub / Notion / Drive impact is either handled or marked N/A,
- sync confirmation is linked or named when Drive SSOT / GitHub sync was performed,
- external review is either completed or explicitly not needed.
