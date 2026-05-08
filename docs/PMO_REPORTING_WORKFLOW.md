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
