# Postmortem: Issue #43 ChatGPT/Codex Business, Multi-Tool Context Refresh

**Date**: 2026-05-11  
**Primary issue**: #43  
**Status**: Completed / ready to close after user confirmation  
**Owner**: Codex PMO  

## Executive Summary

OpenAI/Codex usage exhaustion triggered a move to ChatGPT Business and a broader re-check of the AI PMO operating architecture.

The original #43 scope was "ChatGPT/Codex sub-account warm standby." In practice, the work expanded into a full multi-tool context refresh and tool-configuration audit covering:

- ChatGPT Business Project
- Google Drive source / connector behavior
- GitHub connector
- Claude Code
- Claude Chat
- Claude Cowork
- Gemini / Gems
- Gemini CLI
- Drive SSOT
- GitHub Mirror
- Tool Configuration Register

The end state is positive: the major AI tools now share a substantially aligned understanding of role boundaries, source-of-truth rules, SHIFT AI-BPaaS context, and the user's cognitive / motivation support model.

## What Was Completed

### ChatGPT Business

- New Business Project was set up.
- Project instructions were added.
- Drive source was connected.
- GitHub connector was verified in read-only use.
- Developer mode was kept off.
- Workspace settings were reviewed and recorded.
- Source resync risk was identified and added to operating rules.

Key rule:

```text
Drive source connected does not mean latest context is already indexed.
After Drive SSOT updates, ChatGPT Business may require manual source resync.
```

### Gemini / Gems

- Gemini Ops Lane was confirmed as a long-context / token-relief lane.
- Drive-based Knowledge Pack use was confirmed.
- SHIFT AI-BPaaS reference context was added as a knowledge source.
- Gemini was instructed to separate facts, inferences, and recommended actions.

### Gemini CLI

- Gemini CLI was tested locally.
- Initial wrong working directory was observed: `C:\Windows\System32`.
- Correct project entry point was established: repository root.
- Gemini CLI successfully read project context files and summarized its role.

Key rule:

```text
Start Gemini CLI from the repo root, not System32.
Treat no-sandbox mode as a caution state and prefer read-only review.
```

### Claude Code

- Claude Code initially failed to find three new context files.
- Root cause: files existed locally / Drive-side but had not yet been committed and pushed to GitHub Mirror.
- Context docs were committed and pushed to `main`.
- Claude Code then successfully read all four requested files.

Key rule:

```text
For repo-based tools, Drive SSOT updates are not enough.
Important context additions must also be mirrored to GitHub.
```

### Claude Chat

- Claude Chat successfully read Drive context files.
- It understood its role as dialogue / review / wording / second-opinion support.
- It correctly routed heavy reading to Gemini, issue/PMO work to Codex, and operational progress to Notion.

### Claude Cowork

- Cowork found relevant Drive files and imported local copies.
- It understood Notion-facing vs GitHub/Chat-facing work boundaries.
- It recognized Gemini Ops Lane as token-relief / long-context processing lane.

### Tool Configuration Register

`docs/TOOL_CONFIGURATION_REGISTER.md` became the core configuration register for:

- tool roles
- connector ownership
- source refresh rules
- workspace settings
- capacity-related behavior
- context refresh incidents
- read/write authority boundaries

## Important Incidents / Discoveries

### 1. ChatGPT Business Connector Ownership Incident

Observed message:

```text
Connector scope creator has left this project
```

Interpretation:

- Likely related to personal -> Business transition or connector owner/scope mismatch.
- Treat as a Project / Connector / Knowledge ownership issue, not a simple file upload failure.

Decision:

- Prefer new Project creation over repairing suspicious connector-scope state.
- Reconnect Drive under the current user identity.

### 2. ChatGPT Drive Source Resync Issue

Finding:

- ChatGPT Business can reference a Drive directory source.
- Updating files under that directory may still require a UI-level resync / re-index step.

Implication:

- "Drive source attached" and "latest context indexed" are different states.

### 3. GitHub Mirror Visibility Gap

Finding:

- Claude Code read from repo state.
- Untracked local files were invisible until committed and pushed.

Implication:

- Each AI tool's actual context source must be known:
  - Drive-linked
  - GitHub/repo
  - Project Knowledge
  - local snapshot
  - chat memory

### 4. Business Workspace Settings Are Architecture

Workspace settings reviewed included:

- Codex Local
- Codex Cloud
- Codex agent internet access
- Canvas code execution / network access
- memory / record
- web search
- deep research
- developer mode
- GitHub connector

Implication:

- Tool settings are not preferences. They are part of the AI PMO operating architecture.

### 5. SHIFT AI-BPaaS Misreading Guardrail

The following guardrail was added:

```text
Kondo belongs to the AI-BPaaS business unit, but that does not mean he exclusively owns or solely works on the AI-BPaaS new service shown in the earnings material.
His main role context is existing BPaaS, especially information-systems outsourcing / staffing-substitution, while that business area transitions toward AI-BPaaS and he supports customer expansion.
```

This is especially important for lower-capability models that may over-read organization names.

## Why It Mattered

The session exposed that a multi-AI PMO architecture is not only about prompts and files.

It also requires configuration management for:

- connector ownership
- source refresh state
- model/tool capacity
- read/write authority
- source-of-truth hierarchy
- workspace permissions
- project knowledge freshness
- handoff formats

This is directly aligned with Token-aware Process Design and AI-BPaaS deployment thinking.

## So What

This session converted a usage-limit incident into durable operating architecture.

Key outcomes:

- ChatGPT Business became a usable external advisory / review lane.
- Gemini / Gemini CLI became a practical long-context and token-relief lane.
- Claude Code / Chat / Cowork were refreshed after capacity recovery.
- The Tool Configuration Register became the standard place to track tool-side state.
- The architecture now explicitly distinguishes Drive SSOT, GitHub Mirror, Notion task layer, and tool-local knowledge.

The project is now less dependent on one AI product's token capacity and less vulnerable to silent stale-context failures.

## So How

New standard operations:

1. After major context updates, identify each target tool's actual context source.
2. If the target reads Drive, confirm Drive source and resync/index status.
3. If the target reads GitHub/repo, commit and push GitHub Mirror before asking it to refresh.
4. If the target reads Project Knowledge, treat uploaded files as snapshots unless Drive-linked.
5. Record tool settings and connector incidents in `TOOL_CONFIGURATION_REGISTER.md`.
6. At issue close, include tool-side update suggestions and source-refresh needs.
7. Keep advisory tools advisory unless a write action is explicitly scoped.

## Productivity / Effort View

Manual-only baseline would have required substantially more effort because the work spanned:

- Business workspace setup
- connector troubleshooting
- GitHub and Drive source handling
- multi-tool context propagation
- issue comments
- docs updates
- role-boundary design
- postmortem logging

AI-assisted execution kept the user mostly in decision / verification mode while Codex PMO handled:

- GitHub issue logging
- docs updates
- Drive copy updates
- commit / push
- tool register updates
- synthesis and handoff text

The largest remaining human effort was interactive UI work that AI could not directly perform safely:

- Business Project setup
- connector authorization
- UI resync checks
- app settings review
- external tool confirmation prompts

## What Went Well

- User quickly surfaced tool errors and screenshots.
- Codex PMO converted each finding into a durable log.
- Gemini and ChatGPT Business were configured before the next token crisis.
- Claude recovery was used to confirm multi-tool context propagation.
- Misreading guardrails were added before wider AI reuse.
- Configuration drift was treated as architecture, not annoyance.

## What Was Hard

- Personal -> Business migration introduced connector ownership ambiguity.
- Some UI settings were not obvious.
- Drive source freshness and Project indexing are not transparent.
- GitHub Mirror and Drive SSOT can diverge if local docs are not committed.
- Some local files displayed encoding issues in shell output.
- Model/product naming and capacity states changed during work.

## Risks Remaining

- ChatGPT Business Drive source may still require manual resync after future updates.
- Workspace connector permissions may drift.
- Untracked local files can still cause repo-based tools to miss context.
- Memory/Record features may create non-SSOT convenience context.
- Network-enabled code / agent access needs task-specific data-boundary awareness.
- The Tool Configuration Register itself must be kept current.

## Recommended Follow-Up

- Close #43 after user confirms this postmortem.
- Add issue-close checklist item: "Tool-side update suggestions + source refresh instructions."
- Continue #36 for PMO / Notion / Issue standardization.
- Continue #38 for capacity alerts.
- Continue #39 for Token-aware Process Design.
- Consider a small `Project Ownership Register` or section in `TOOL_CONFIGURATION_REGISTER.md`.
- Periodically ask each major AI lane to summarize its role and source freshness.

## Close Criteria Check

- Sub account / Business Project purpose and boundaries documented: yes.
- Required context files identified: yes.
- Tool configuration register updated: yes.
- Capacity / backup lane linked to #38/#39 context: yes.
- Test prompts confirmed role and handoff behavior: yes.
- User knows when to use main vs backup / advisory lanes: yes.
- Gemini, ChatGPT Business, Claude Code, Claude Chat, Claude Cowork, Gemini CLI refreshed: yes.

## Closing Note

#43 started as a warm-standby setup, but it produced a broader operating pattern:

```text
AI PMO reliability = context freshness + connector ownership + role boundary + capacity routing + postmortem logging.
```

This is now a reusable pattern for future AI PMO / AI-BPaaS deployment work.
