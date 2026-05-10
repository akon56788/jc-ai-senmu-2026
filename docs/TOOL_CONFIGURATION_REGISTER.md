# Tool Configuration Register

**Status**: Active draft  
**Owner**: Codex PMO  
**Purpose**: Track user-facing AI tool settings that affect safety, context freshness, automation, capacity, and handoff reliability.

## Why This Exists

AI tool settings are part of the operating architecture.

Small UI settings can affect:

- whether a tool can edit files without confirmation
- whether the user notices blocked or waiting sessions
- whether local/project attachments become stale
- whether PRs are created or modified automatically
- whether Drive SSOT / GitHub Mirror boundaries are respected
- whether capacity limits stop work unexpectedly

Therefore, important tool-side settings should be captured as configuration, not only as personal preferences.

## Current Rules

- Prefer safe defaults over automation until the workflow is proven.
- Keep bypass / auto-write / auto-merge / auto-fix features off unless a specific Issue approves them.
- Treat uploaded files and project attachments as snapshots unless explicitly Drive-linked.
- Record capacity-related settings and warnings in #38.
- Record context / Knowledge Pack settings in #36 / #37 / #42 as appropriate.

## Claude Code / Claude Desktop

Last reviewed: 2026-05-10  
Context: Claude usage limit reached; settings reviewed from Code settings screen.

| Setting | Current / Recommended | Reason |
| --- | --- | --- |
| バイパス権限モードを許可 | OFF | Prevents uncontrolled command/file operations. Keep confirmation gates for Drive SSOT / GitHub Mirror safety. |
| 通知を目立たせる | ON | Helps user notice blocked/waiting sessions, confirmations, and capacity issues. Recommended for ADHD/supportive PMO operation. |
| ワークツリーの場所 | Inside project (`.claude/worktrees`) | Keeps Code worktrees scoped to project. Do not change without repo/Drive path review. |
| ブランチプレフィックス | `claude` | Acceptable. Keeps Claude-created branches identifiable. |
| プレビュー | ON | Useful for frontend/browser validation. Safe enough with current workflow. |
| プレビューセッションを保持 | OFF | Avoids persistent cookies/local storage unless specifically needed. Safer for JC/SSOT work. |
| PRを自動的に作成する | OFF | PR creation should remain PMO/user-reviewed for now. |
| PRを自動修正 | OFF | Avoid unattended CI/review response loops. PMO should triage. |
| PRマージまたはクローズ後に自動アーカイブ | OFF | Keep manual/PMO visibility until workflow stabilizes. |

### Claude Code Context Refresh Incident

Last reviewed: 2026-05-11  
Incident: Claude Code refreshed repo but could not find:

- `docs/HUMAN_OPERATING_MANUAL_FOR_AI_PMO.md`
- `docs/PMO_MOTIVATION_DESIGN.md`
- `docs/reference/shift_ai_bpaas_q2_2026_context.md`

Cause:

- These files existed locally and/or in Drive SSOT but had not yet been committed and pushed to GitHub Mirror.
- Claude Code was reading repository state after GitHub refresh, so untracked local files were invisible.

Resolution:

- Committed and pushed context/tool docs to `main`.
- Commit: `ca88dcb` (`Add AI PMO context and tool configuration docs`)
- Follow-up verification succeeded after repo refresh. Claude Code read all four requested files:
  - `docs/HUMAN_OPERATING_MANUAL_FOR_AI_PMO.md`
  - `docs/PMO_MOTIVATION_DESIGN.md`
  - `docs/reference/shift_ai_bpaas_q2_2026_context.md`
  - `docs/TOOL_CONFIGURATION_REGISTER.md`

Rule:

- If a tool reads from GitHub/repo context, Drive SSOT updates are not enough.
- Important context additions must be mirrored to GitHub before asking Claude Code or other repo-based tools to read them.
- At Issue close or tool-side update time, check whether the target tool reads Drive, GitHub, Project Knowledge, or local files.

## Gemini / Gems

Last reviewed: 2026-05-10

| Setting / Area | Current / Recommended | Reason |
| --- | --- | --- |
| Gem name | `専務理事AI補佐｜Gemini Ops Lane` | Distinguishes it from other Gems and anchors the JC executive secretary context. |
| Custom instructions | Japanese instructions in `docs/GEMINI_OPS_LANE_SETUP.md` | Operational language should be Japanese. |
| Knowledge sources | Drive files under `50_Gemini_Knowledge_Pack/00_Common` | Avoid stale local uploads. |
| Local initial attachments | Remove / ignore | Treat as stale snapshots. |
| Source set | 9 Drive files | Acceptable for initial phase; split later if too heavy. |
| Mode routing | Flash / Thinking / Pro by QCD | See `docs/GEMINI_OPS_LANE_SETUP.md`. |

## ChatGPT

Last reviewed: 2026-05-10

| Setting / Area | Current / Recommended | Reason |
| --- | --- | --- |
| Project files / uploads | Snapshot unless manually replaced | Do not assume latest Drive/GitHub context. |
| Role | Manual interactive external advisory reviewer | See `docs/CONTEXT_FOR_CHATGPT.md`. |
| Context refresh | Use latest summary or context files when needed | Avoid stale project context. |
| Direct updates | No direct GitHub / Drive / Notion claims | Advisory only. |

### ChatGPT Business Workspace Settings

Last reviewed: 2026-05-10  
Workspace: Work Life Renovation  
Context: Browser workspace settings screen, `権限とロール`.

| Area | Setting | Current / Recommended | Reason |
| --- | --- | --- | --- |
| Local Codex | メンバーに Codex Local の使用を許可する | ON / OK | Needed for Codex Local / CLI / IDE / app usage. Acceptable because this is the user's own AI PMO workspace. |
| Local Codex | Codex CLI のデバイスコード認証を有効化 | OFF / OK | Keep OFF unless needed. Device-code auth can be useful in headless environments but increases phishing/credential-flow risk. |
| Record | メンバーが ChatGPT の記録を使用することを許可 | ON / OK with caution | Useful for transcription/long audio notes. Avoid feeding confidential client or JC sensitive material without intent. |
| Record | ChatGPT が過去のメモや文字起こしを参照することを許可 | ON / OK with caution | Helpful for continuity, but can create stale-context/over-personalization risk. Use explicit context files for authoritative PMO facts. |
| Skills | スキルを有効にする | ON / OK | Useful for future skill standardization. Skills should still respect Drive SSOT / GitHub Mirror / Notion Task boundaries. |

Additional enterprise / agent settings reviewed:

| Area | Setting | Current / Recommended | Reason |
| --- | --- | --- | --- |
| Agents | エージェントを有効にする | ON / OK | Enables workspace agents. Acceptable for AI PMO experimentation; keep responsibility boundaries explicit. |
| Sharing | Workspace chat/canvas/project sharing | Workspace members only / OK | Good default. Avoid public or broad external sharing while SSOT/JC/client context is present. |
| Memory | メンバーにメモリの使用を許可 | ON / OK with caution | Useful continuity, but memory is not SSOT. Do not rely on memory for authoritative facts. |
| Retention | チャットの保持ポリシー | Unlimited / OK with caution | Useful for audit/postmortem. Reassess if client-confidential data enters workspace. |
| Canvas | Canvas コードの実行 | ON / OK with caution | Useful for analysis/prototyping. Avoid running untrusted code or sensitive data processing casually. |
| Canvas | Canvas コードのネットワークアクセス | ON / Caution | Enables outbound access from Canvas code. Keep only if needed; avoid secrets/client data in network-enabled runs. |
| Search | ウェブ検索 | ON / OK | Useful for current/public research. Treat web results as non-SSOT and cite/verify. |
| Search | Deep research | Available / OK | Useful for research. Use for external/public investigation, not Drive SSOT mutation. |
| Voice | 音声中の画面/動画共有 | ON / OK with caution | Useful for meeting/debug support. Avoid screen sharing confidential materials unless intentional. |
| Codex | メンバーに Codex の管理を許可 | OFF / OK | Good least-privilege default. Only owner/admin should manage Codex environment settings. |
| Codex Cloud | メンバーに Codex Cloud の使用を許可 | ON / OK with caution | Useful for cloud agent work. Requires GitHub/app boundaries and data handling discipline. |
| Codex Slack | Task complete answer posting | OFF / OK | Avoids unsolicited full responses to Slack. Keep manual/controlled. |
| Codex Security | メンバーに Codex セキュリティの使用を許可 | ON / OK | Useful for scans/security review. |
| Codex Security | メンバーに Codex セキュリティの管理を許可 | OFF / OK | Keep security management restricted to owner/admin. |
| Codex Agent | Internet access for Codex agents | ON / Caution | Useful for cloud tasks requiring network. Use explicit task scope; avoid exposing secrets or SSOT data unnecessarily. |
| macOS coding | macOS code editing | ON / Mostly irrelevant | Workspace-level setting; current main environment is Windows. Keep unless a macOS workflow creates risk. |
| Apple Intelligence | Link with Apple Intelligence | ON / Mostly irrelevant | Workspace-level option; not central to current PMO workflow. Reassess if Apple-side data paths matter. |

### ChatGPT Business Project Initialization

Last reviewed: 2026-05-11  
Status: Initial Project setup confirmed by ChatGPT Business / GPT-5.5 Pro response.

Confirmed behavior:

- ChatGPT Business identifies itself as external advisory / review / thinking partner.
- It does not claim authority to directly update Drive SSOT, GitHub Issues, or Notion.
- It recognizes Drive = SSOT, GitHub = Mirror / Version Layer, Notion = Task / Operational Layer.
- It recognizes Codex PMO as the execution / sync / GitHub reflection lead.
- It recognizes Gemini Ops Lane as long-context intake / structure / audit lane.
- It recognizes Claude as review / dialogue / implementation support after capacity recovery.
- It correctly preserves the SHIFT AI-BPaaS misreading guardrail.

Required refresh rule:

- Drive source connected does not mean latest context is already indexed.
- After Drive SSOT context updates, ChatGPT Business Project may require manual source resync.
- For important decisions, confirm whether the latest Drive SSOT context has been resynced / re-indexed.

Information reliability order:

1. Latest Drive SSOT original
2. Project Context explicitly resynced / re-indexed from Drive SSOT
3. Latest information explicitly provided by the user in the current conversation
4. Past chat / existing Project Knowledge
5. General model knowledge

Developer mode:

- Keep OFF for now.
- Use checked / official apps and connectors only.
- Do not add unverified connectors during the AI PMO foundation phase.

Current ChatGPT Business next-use checklist:

- Use for advisory review, wall-clock thinking, Codex PMO handoff drafts, issue/Notion candidate extraction, and misreading-risk checks.
- Before relying on Drive context, ask whether Drive source resync has been performed after the latest context update.
- Do not use ChatGPT Business as the primary writer for Drive SSOT / GitHub / Notion.

### ChatGPT Business GitHub Connector Verification

Last reviewed: 2026-05-11  
Status: Read-only verification passed.

Verified:

- GitHub connector is available from ChatGPT Business Project.
- Repository `akon56788/jc-ai-senmu-2026` can be referenced.
- Default branch observed: `main`.
- Visibility observed: `public`.
- Archived status observed: `false`.
- Issue list search succeeded.
- Read-only operation discipline was preserved.

Observed issue counts via connector:

- Total issues: 29
- Open issues: 23
- Closed issues: 6

Important guardrail:

- Connector may expose broader permissions such as triage / push / maintain / admin.
- ChatGPT Business must still operate as external advisory / review / context organizer.
- GitHub Issue creation, comments, updates, labels, close, code changes, or PR actions remain Codex PMO / user execution responsibilities unless explicitly authorized and intentionally scoped.

Known caveat:

- Issue `state` may not always be returned directly by the connector search result; classify via search filters such as `is:open` / `is:closed` when needed.
- GitHub Mirror visibility does not prove latest Drive SSOT context is reflected in ChatGPT Project Knowledge.

Operational note:

- Workspace memory/record features are convenience context, not SSOT.
- Authoritative operational context remains Drive SSOT and GitHub issue/context files.
- If client-confidential or JC-sensitive data is involved, decide explicitly whether it should enter ChatGPT Record / transcription flows.
- Network-enabled code execution / agent internet access should be treated as an explicit data-boundary setting.
- For public research and open-source/code tasks, web/network access is useful. For confidential customer/JC data, avoid unnecessary outbound access.
- Record this page again if Workspace owner, seat type, connector settings, app permissions, or Codex Local settings change.

### ChatGPT Business Project / Connector Ownership Incident

Last reviewed: 2026-05-10  
Observed message: `Connector scope creator has left this project`

Interpretation:

- The Google Drive Connector scope previously attached to the ChatGPT Business Project may have been created by an identity that is no longer in the Project.
- Drive connector authority, Project Knowledge access, and Project-level source visibility may be inconsistent.
- This is not merely a file upload problem. Treat it as a Project ownership / connector scope integrity issue.

Refined diagnosis:

1. ChatGPT source refresh operation issue
   - The Project was not necessarily referencing individual files only.
   - It may have been referencing the broader Drive SSOT directory as a source.
   - When context files are updated under the Drive source directory, ChatGPT Business may require the user to press a UI-level resync button.
   - Therefore, "Drive source attached" does not automatically guarantee "latest context already indexed."

2. Personal-to-Business migration / Drive connector issue
   - The `Connector scope creator has left this project` message is likely related to the personal -> Business workspace transition or connector ownership migration.
   - Treat this as a separate incident from ordinary context refresh.

Recommended handling:

- Prefer creating a new Business Project over trying to repair a suspicious connector-scope state.
- Keep the old Project as reference-only if needed.
- Reconnect Google Drive from the current user identity that owns / operates the Business Workspace.
- Re-add the core context files and Project Instructions after reconnection.
- Do not assume old Project Knowledge is complete or fresh.
- After any Drive SSOT context update, perform ChatGPT Business source resync manually if the Project uses a Drive directory source.

Required core files for the rebuilt Project:

- `docs/HUMAN_OPERATING_MANUAL_FOR_AI_PMO.md`
- `docs/PMO_MOTIVATION_DESIGN.md`
- `docs/TOOL_CONFIGURATION_REGISTER.md`
- `docs/reference/shift_ai_bpaas_q2_2026_context.md`

Recommended Project Instructions:

```text
Drive = SSOT.
GitHub = Mirror / Version Layer.
Notion = Task / Operational Layer.
ChatGPT Business = external advisory / review / thinking partner.
Do not claim direct authority to update Drive SSOT, GitHub Issues, or Notion unless explicitly instructed.
When context is uncertain, say what is missing instead of guessing.
Prefer responsibility boundaries, ownership clarity, and context freshness over convenience.
```

Project Ownership Register seed:

| Target | Owner / Authority | Note |
| --- | --- | --- |
| ChatGPT Business Project | User | Rebuild under current user identity. |
| Google Drive Connector | User | Must be connected by the current workspace/project owner. |
| Drive SSOT | User / Codex PMO-assisted | Drive is the source of truth. |
| GitHub Mirror | Codex PMO / User | Version and issue layer, not primary Drive truth. |
| Notion Integration | Cowork / User, PMO-scoped | Operational task layer. |
| Gemini / Gems Knowledge | User-managed Drive sources | Prefer Drive-linked files over local uploads. |
| Gemini CLI | Codex PMO / local repo context | Review/advisory output only unless explicitly scoped. |
| Claude Code / Chat / Cowork | User-managed, capacity-dependent | Refresh after usage limit recovery. |

### ChatGPT / Codex Sub Account

Last reviewed: 2026-05-10  
Related issue: #43

| Setting / Area | Current / Recommended | Reason |
| --- | --- | --- |
| Purpose | Warm standby / backup PMO lane | Avoid full stop when main account hits usage limits. |
| Suggested name | `専務理事AI PMO Standby` | Distinguishes from main PMO account. |
| Authority | Advisory / handoff only | Prevent double writes to GitHub / Drive / Notion / SSOT. |
| Primary use | emergency PMO continuation, long-context drafting, agenda AX validation, Business feature testing | Use the second Business seat deliberately. |
| Required handoff | `Main PMO Handoff` format | Main account/Codex should triage and execute after recovery. |
| Context set | See #43 | Keep minimal but sufficient. |

## Gemini CLI

Last reviewed: 2026-05-10

| Setting / Area | Current / Recommended | Reason |
| --- | --- | --- |
| Entry point | Repo root + `GEMINI.md` | Keeps CLI review grounded in repository context. |
| Default context | `scripts/external_review.py` | Standard PMO/SSOT context bundle. |
| Model routing | `auto` default; `pro` for audit; `flash` for lightweight review | See `docs/GEMINI_OPS_LANE_SETUP.md`. |
| Write authority | None by default | Review output only; Codex/user execute. |

## Claude Chat

Last reviewed: 2026-05-10

| Setting / Area | Current / Recommended | Reason |
| --- | --- | --- |
| Project files / uploads | Snapshot unless manually replaced | Same stale-context risk as ChatGPT. |
| Capacity state | Degraded when shared Claude limit reached | See #38 capacity alert logs. |
| Role | Dialogue / reflection / wording / advisory review | Avoid treating as SSOT updater. |

## Claude Cowork

Last reviewed: 2026-05-10

| Setting / Area | Current / Recommended | Reason |
| --- | --- | --- |
| Capacity state | Degraded when shared Claude limit reached | UI may appear usable while shared limit blocks work. |
| Role | Notion/Sheets/Drive operational support | Coordinate through Codex PMO for SSOT-sensitive updates. |
| Direct updates | Only when explicitly scoped and PMO-approved | Avoid hidden divergence between Notion/Drive/GitHub. |

## Update Triggers

Update this register when:

- a tool setting changes,
- a tool hits a capacity or usage limit,
- a new Gem / Project / workspace is created,
- context source files are replaced,
- automation / bypass / auto-PR settings change,
- a security or data boundary changes,
- a tool-side update suggestion is made at Issue close.

## Related Issues

- #36: PMO / Notion / Issue standardization
- #37: Gemini Ops Lane setup
- #38: AI Capacity Alert operation
- #42: Drive SSOT directory reorganization
