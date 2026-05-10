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

**Related files (Drive SSoT + GitHub Mirror):**
- Drive SSoT: See `DRIVE_SYNC_STATUS.md` for SSoT file locations
- GitHub Mirror: `docs/pmo_engagement_template.md`, `docs/kondo_core_roles.md`, `docs/llm_engagement_systemprompt.md` (version control & diff tracking)
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

---

## Weekly AI PMO Reliability Check

As of 2026-05-11, Codex PMO runs a weekly reliability check in addition to Issue close checks.

Purpose:

- catch stale context before it causes tool disagreement,
- detect connector ownership drift before important work,
- keep capacity routing visible,
- ensure Drive SSOT and GitHub Mirror remain aligned,
- make role-boundary drift visible across AI lanes.

Minimum weekly checks:

1. **Role understanding**
   - Confirm each active AI lane still understands its current role and authority boundary:
     - Codex PMO
     - Claude Code
     - Claude Chat
     - Claude Cowork
     - ChatGPT Business
     - Gemini / Gems
     - Gemini CLI

2. **Source freshness**
   - Check whether each tool is reading the current source:
     - Drive SSOT
     - GitHub Mirror
     - Project Knowledge / uploaded files
     - local files
     - memory / record
   - Do not treat "file exists" as proof that the tool has the latest context.

3. **Connector state**
   - Review ownership and auth health for:
     - ChatGPT Business Project
     - Google Drive connector
     - GitHub connector
     - Gemini Gems Knowledge
     - Claude Chat / Cowork Drive connection
     - Notion Integration
     - GitHub PAT / gh CLI
     - Codex Local / Cloud

4. **Capacity state**
   - Check recent or current usage-limit incidents.
   - Route capacity / plan / fallback lessons to #38.
   - Route broader design lessons to #39.

5. **Drive / GitHub sync state**
   - Check whether Drive SSOT updates need GitHub commit/push.
   - Check whether GitHub doc updates need Drive SSOT copy.
   - Record any stale mirror risk.

6. **Follow-up routing**
   - Standardization / PMO process: #36
   - Capacity alert operation: #38
   - Token-aware process design: #39
   - Drive SSOT directory/source structure: #42

Automation:

- `AI PMO Reliability Weekly Check`
- Schedule: weekly, Monday morning JST
- Mode: read-first audit; produce recommended next actions unless a low-risk write action is explicitly in scope.

---

## Issue Close Tool Update Suggestions

When an Issue is closed, Codex PMO should suggest tool-side actions to keep each AI tool's context current.

Use this especially when the Issue changed shared context, tool roles, Knowledge Pack files, Notion/GitHub relationships, Drive SSOT, or operating rules.

### Issue Close Standard Check

As of 2026-05-11, every meaningful Issue close should include a lightweight closeout check for context freshness and tool-side follow-up.

Minimum checks:

1. **Tool-side update suggestions**
   - State which tools need user action, resync, pull, Project Knowledge update, or no action.
   - Include Codex, Claude Code, Claude Chat, Claude Cowork, ChatGPT, Gemini / Gems, Gemini CLI, Notion, Drive SSOT, and GitHub when the Issue affected shared context.

2. **Source refresh check**
   - Identify whether each affected tool reads from Drive, GitHub/repo, Project Knowledge, local files, or memory/record.
   - Do not assume a tool is current just because the source exists somewhere.

3. **Drive / GitHub / Project Knowledge / local distinction**
   - Drive source tools may need resync / re-index.
   - GitHub/repo tools need commit/push and pull/refresh.
   - Project Knowledge and uploaded attachments are snapshots unless Drive-linked.
   - Local files are invisible to other tools unless copied to Drive or committed to GitHub.

4. **Postmortem decision**
   - Create a postmortem when the Issue involved capacity limits, connector ownership, source freshness, role-boundary changes, multi-tool context propagation, Drive/GitHub/Notion coordination, or meaningful productivity / QCD learning.
   - For small Issues, a short close comment is enough.

5. **Follow-up routing**
   - If new standards emerge, link them to #36.
   - If capacity or plan limits were involved, link them to #38.
   - If Token/capacity design lessons emerged, link them to #39.
   - If Drive directory/source structure changed, link them to #42.

6. **Reliability check delta**
   - If the close changed any of the weekly reliability dimensions, note the delta:
     - role understanding
     - source freshness
     - connector state
     - capacity state
     - Drive / GitHub sync state

Template:

```markdown
Tool-side update suggestions:
- Codex: latest repo/context already reflected / N/A
- Claude Code: pull latest before next work
- Claude Chat: replace old project attachments if this context is needed
- Claude Cowork: update only if Notion/Drive task flow is affected
- ChatGPT: use latest context files or summary if wall-discussing this issue
- Gemini / Gems: update Drive Knowledge Pack or confirm Drive reference
- Gemini CLI: no extra action if `scripts/external_review.py` context list is updated
- Notion: [N/A / update project-task relation]
- Drive SSOT: [N/A / pending sync / updated]
- GitHub: [closed / follow-up issue created]
```

For small Issues, list only affected tools. For large Issues, list all tools.

General rule:

- AI project files, uploaded attachments, and Gem local uploads are snapshots unless explicitly Drive-linked.
- GitHub-based tools should pull latest before continuing.
- Drive SSOT remains the canonical source; GitHub Mirror is used for diff and review.
- Tool-side settings that affect safety, automation, capacity, context freshness, or notifications should be recorded in `docs/TOOL_CONFIGURATION_REGISTER.md`.
- If an Issue changes shared context, Codex PMO should ensure the relevant source path is refreshed: Drive resync, GitHub commit/push, Project Knowledge update, or local file copy as appropriate.
