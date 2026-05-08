# External Review Workflow

**Date**: 2026-05-08
**Status**: Phase 1 adjunct draft

---

## Purpose

Codex PMO can request an external, objective review from ChatGPT or Gemini when a change affects project policy, SSOT operations, GitHub / Drive / Notion coordination, or cross-tool role definitions.

The first implementation is **semi-automatic**:

1. Codex collects the change target, context, and review questions.
2. Codex generates a Markdown review request under `reviews/`.
3. If Gemini CLI is installed, Codex can send the request to Gemini and save the response.
4. Codex summarizes the result in the PMO report and decides whether follow-up changes are needed.

---

## Roles

| Role | Responsibility | Decision Authority |
|------|----------------|--------------------|
| Codex | PMO owner, request generation, result triage, GitHub / Drive follow-up | Yes |
| ChatGPT | Manual external review and second opinion | No |
| Gemini | Semi-automatic external review through CLI | No |
| Code | Implementation owner for GitHub-heavy changes | Yes, within scope |
| Cowork | Notion / Drive operations owner | Yes, within scope |
| Claude Chat | Policy discussion and final wording support | Yes, with user approval |

External reviewers are advisory. They do not directly update GitHub, Drive, Notion, or SSOT documents.

---

## When To Request Review

Use external review when one or more are true:

- A change updates tool roles, PMO rules, or handoff rules.
- A change affects GitHub ↔ Drive SSOT synchronization.
- A change introduces automation, GitHub Actions, CLI tooling, or scripts.
- The user asks for objective review, third-party review, counterargument, or risk check.
- Codex detects a meaningful risk, ambiguity, or cross-tool ownership issue.

Skip external review for small typo fixes, obvious file moves, or low-risk formatting.

---

## Semi-Automatic Command

Generate only:

```powershell
python scripts/external_review.py --target docs/TOOL_CONTEXT_GUIDE.md --question "PMO role update risk check"
```

Generate and run Gemini CLI:

```powershell
python scripts/external_review.py --target docs/TOOL_CONTEXT_GUIDE.md --question "PMO role update risk check" --run-gemini
```

On Windows, if `gemini` is installed but not on the current PowerShell `PATH`, pass the command path explicitly:

```powershell
python scripts/external_review.py --target docs/TOOL_CONTEXT_GUIDE.md --question "PMO role update risk check" --run-gemini --gemini-command "$env:APPDATA\npm\gemini.cmd"
```

When `--run-gemini` is used, the script runs Gemini CLI in headless review mode with `--prompt ""`, `--approval-mode plan`, `--skip-trust`, and `--output-format text`. Gemini is used as a review-only advisor; Codex remains responsible for triage and any GitHub / Drive / Notion follow-up.

By default, the review request includes compact project context from:

- `GEMINI.md`
- `docs/TOOL_CONTEXT_GUIDE.md`
- `docs/CONTEXT_FOR_CODEX.md`
- `docs/AGENTS.md.txt`
- `docs/EXTERNAL_REVIEW_WORKFLOW.md`
- `docs/PMO_REPORTING_WORKFLOW.md`

Add more context when needed:

```powershell
python scripts/external_review.py --target docs/AGENTS.md.txt --context docs/DRIVE_SYNC_STATUS.md --question "Check SSOT sync risk" --run-gemini
```

Use `--no-default-context` only for very small reviews where the PMO / SSOT background is unnecessary.

The script writes:

- `reviews/YYYY-MM-DD_external_review_request.md`
- `reviews/YYYY-MM-DD_external_review_gemini_result.md` when `--run-gemini` succeeds

If Gemini CLI is unavailable, the generated request can be pasted manually into ChatGPT or Gemini.

---

## Review Prompt Requirements

Every request should include:

- Objective of the change
- Target files or PR
- Relevant project context
- Expected reviewer stance: objective, critical, concise
- Questions to answer
- Output format

Reviewer output should classify issues as:

- `Blocker`: must fix before merge / SSOT reflection
- `Risk`: should consider or mitigate
- `Suggestion`: optional improvement
- `No issue`: explicitly safe enough

---

## PMO Handling

Codex should report external review status in detailed PMO mode:

```markdown
**External Review:**
- Reviewer: Gemini / ChatGPT / N/A
- Status: Not needed / Requested / Completed / Blocked
- Result: Blocker / Risk / Suggestion / No issue
- Follow-up: [action or none]
```

Normal three-line PMO reports do not need this block unless an external review was requested.

---

## Installation Note

Gemini CLI is optional. Use only the official Gemini CLI source and verify the package name before installation. The semi-automatic workflow still works without Gemini because it can generate a manual review request.
