# Project Ownership Register

**Status**: Active draft  
**Owner**: Codex PMO  
**Created**: 2026-05-11  
**Related issues**: #36, #38, #39, #43

## Purpose

AI PMO運用では、どのツールが何を読めるかだけでなく、誰の認証、どのWorkspace、どのConnector権限で接続されているかが重要になる。

この台帳は、ChatGPT Business移行時に発生した `Connector scope creator has left this project` を教訓として、Project / Connector / Knowledge / CLI / Integration の所有権と権限主体を明示するために作成する。

## Core Principle

```text
Context freshness depends on source ownership.
```

ファイルが存在していても、以下が曖昧だとAI PMOは不安定になる。

- どのアカウントで接続しているか
- どのWorkspace / Projectに紐づいているか
- Drive / GitHub / Project Knowledge / local / memory のどれを読んでいるか
- 書き込み権限を持つのか、読み取り専用なのか
- ConnectorやPATの所有者が退場、切替、移行した場合にどうなるか

## Ownership Table

| Target | Owner / Auth Principal | Current Use | Authority Boundary | Refresh / Maintenance |
| --- | --- | --- | --- | --- |
| ChatGPT Business Project | User / Work Life Renovation workspace owner | 外部顧問レビュー、壁打ち、文脈整理 | Direct update主体ではない。Drive/GitHub/Notion更新はCodex PMOまたはUser判断 | Drive source更新後にProject resync / re-index確認 |
| Google Drive Connector for ChatGPT Business | User Google auth under current Business Project | Drive SSOT参照 | DriveをSSOTとして読む。Connector ownership driftに注意 | Project再作成・Workspace変更時は再接続 |
| GitHub Connector for ChatGPT Business | User GitHub auth | GitHub Mirror / Issue参照 | 読み取り・レビュー中心。Issue更新/PR/コード変更はCodex PMO/User | 権限範囲をrepo単位に絞る。読み取り確認を定期実施 |
| Gemini Gems Knowledge | User-managed Drive files | Gemini Ops Lane Knowledge | Geminiは助言・整理・監査。Drive/GitHub/Notion直接更新なし | Drive上のKnowledge Packを更新。必要に応じてGem側source確認 |
| Gemini CLI | Local user auth / repo root context | 外部レビュー、長文処理、監査、Token relief | no sandbox時は原則read-only review。実行・更新は明示スコープ時のみ | repo rootから起動。`GEMINI.md` とdocsを読む |
| Claude Code | User Claude account / GitHub repo context | repo / code / docs読解、実装補助 | GitHub Mirrorへpush済みの内容を読む。untracked local filesは不可視 | 重要docs追加時はcommit/push後にrefresh |
| Claude Chat Drive connection | User Claude account / Google Drive connector | 対話、レビュー、文章化、Drive文脈確認 | Direct update主体ではない | Drive SSOTの対象ファイルを明示して読む |
| Claude Cowork Drive connection | User Claude account / Google Drive / Notion support | Notion/Sheets/Drive実務支援 | Notion/Drive操作はCodex PMO/Userでスコープ確認 | Drive source / Notion task flow変更時に更新 |
| Notion Integration | User / Cowork-scoped operational use | Task / Operational Layer | Notionは進捗・実務運用レイヤー。SSOTではない | Project/Task DB schema変更時に確認 |
| GitHub PAT / gh CLI | User local credentials / `tools/gh/gh.exe` | Issue comment, close, repo inspection | Codex PMOが実行補助。破壊的操作は明示許可 | 権限・期限・repo scopeを定期確認 |
| Codex Local | User / local workspace | PMO実行、docs更新、GitHub反映 | Drive/GitHub/Notion本番反映はユーザー依頼または明示スコープ内 | repo status、untracked files、push stateを確認 |
| Codex Cloud | ChatGPT Business workspace setting | Cloud agent / future work | Internet accessやGitHub App境界に注意 | Workspace設定変更時に台帳更新 |
| Drive SSOT root | User-managed Google Drive | 正本 | 最終的な運用文脈の正本 | コピー/移動/命名変更時はManifest/links/source更新 |
| GitHub Mirror | User / Codex PMO-assisted | Version Layer / Issue Layer | 正本ではないが差分・履歴・Issue管理に使う | Drive更新後に必要docsをcommit/push |

## Incident Reference

### ChatGPT Business Connector Ownership

Observed:

```text
Connector scope creator has left this project
```

Interpretation:

- Personal -> Business transition or connector owner/scope mismatch likely caused the issue.
- A Project can appear valid while its connector authority is stale or ambiguous.

Decision:

- Prefer rebuilding a clean Project with current user authentication over repairing ambiguous connector state.
- Treat old Project as reference-only if connector ownership is unclear.

## Standard Checks

Run this checklist when:

- a new Project / Gem / Claude Project / connector is created,
- an account moves from Personal to Business / Team / Enterprise,
- Drive source or GitHub connector is reconnected,
- a tool cannot find an expected context file,
- a major Issue closes and context changed,
- a capacity incident forces fallback tooling,
- the weekly AI PMO reliability check runs.

Checklist:

1. Who owns the Workspace / Project?
2. Which account authorized the connector?
3. Is the connector Drive-linked, GitHub-linked, Project Knowledge, local, or memory-based?
4. Does it have read-only, triage, write, maintain, or admin authority?
5. Does the tool claim write authority it should not have?
6. Does source refresh require manual resync / re-index / pull?
7. Is the relevant context mirrored to the source this tool actually reads?
8. Is the ownership state recorded in this register and `TOOL_CONFIGURATION_REGISTER.md`?

## Weekly Review Scope

At least once per week, Codex PMO should check whether the following ownership-sensitive sources are still healthy:

- ChatGPT Business Project and Drive/GitHub connectors
- Gemini Gems Knowledge and source files
- Gemini CLI local auth and repo-root startup path
- Claude Code GitHub/repo visibility
- Claude Chat / Cowork Drive connection
- Notion Integration
- GitHub PAT / gh CLI
- Codex Local / Cloud settings

The weekly review should be treated as a read-first audit. It should produce recommended next actions unless an explicitly scoped low-risk update is available.

## Closeout Rule

When closing an issue that changed tool configuration or context files, Codex PMO should suggest tool-side update actions for:

- Codex
- Claude Code
- Claude Chat
- Claude Cowork
- ChatGPT
- Gemini / Gems
- Gemini CLI
- Notion
- Drive SSOT
- GitHub

The suggestion should distinguish:

- source refresh,
- connector ownership,
- knowledge upload/re-index,
- local pull/commit/push,
- read-only vs write authority.
