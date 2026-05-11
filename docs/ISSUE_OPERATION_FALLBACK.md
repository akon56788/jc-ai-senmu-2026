# Issue Operation Fallback

**Status**: Active draft  
**Owner**: Codex PMO  
**Created**: 2026-05-11  
**Related issues**: #38, #45

## Purpose

Codex PMO が capacity / token / usage limit で一時的に動けない場合でも、GitHub Issue の確認、コメント、作成、更新を止めないための代替運用を定義する。

この文書は「全ツールが自由に Issue を書き換える」ための許可ではない。目的は、ユーザーの明示スコープと軽量確認に基づき、急ぎの記録だけを安全に残し、Codex PMO 復旧後にレビューできる状態を作ること。

## Core Principle

原則は staged authority（段階権限）とする。

| Level | 権限 | English label | 許可される行為 |
| --- | --- | --- | --- |
| Level 0 | Read-only | Observe | Issue / PR / docs / Drive / Notion を読む。要約、論点整理、次アクション提案まで。書き込みなし。 |
| Level 1 | Draft-only | Prepare | Issue コメント、Issue 本文、更新案、close コメントを下書きする。ユーザーまたは Codex PMO が投稿する。 |
| Level 2 | 明示スコープ内・軽量確認付きIssue書き込み | Scoped write | ユーザーが Issue 番号、目的、投稿範囲を明示した場合に、軽量確認後、コメント追加や限定的な本文更新を行う。 |
| Level 3 | ユーザー事前確認付き・代替PMO暫定更新権限 | Acting PMO | Codex PMO 不在時の urgent / blocking work に限り、ユーザー事前確認後、Issue 作成、ラベル提案、状態更新、暫定 PMO コメントを行う。 |

Level 2 以上では、書き込み前に「どの Issue に、何を、どの目的で書くか」を明示する。Level 3 は恒久権限ではなく、Codex PMO 復旧までの暫定代理である。

## Acting-manager Model

Codex PMO を manager とし、代替ツールを acting lead として扱う。

Codex PMO が不在または capacity-limited のとき、acting lead は次を行う。

1. 緊急性と範囲を確認する。
2. 既存 Issue への追記で足りるか判断する。
3. 明示スコープ内で最小限の書き込みを行う。
4. Fallback PMO Handoff を残す。
5. Codex PMO 復旧後レビューのため、URL と判断理由を記録する。

Acting lead は、恒久的な優先順位変更、Issue close、広範なラベル再設計、運用ルール変更を単独で確定しない。必要な場合は Level 1 の下書きに留めるか、ユーザー確認を取って Level 3 として扱う。

## Capacity Incident Routing

Capacity / Token / usage limit の記録は、まず #38 のコメントへ集約する。

新規 Issue を作るのは、次のいずれかに該当する場合に限る。

- distinct incident: #38 の通常ログでは追跡しにくい、別系統の障害や権限問題
- recovery task: 復旧手順、設定変更、再接続、検証など独立した作業が必要
- permanent countermeasure: 恒久対策、運用ルール、設計変更として残す必要がある

迷う場合は、Level 1 で「#38 追記案」と「新規 Issue 案」を両方作り、ユーザーまたは Codex PMO に選ばせる。

## Tool Matrix

| Tool | Default level | Level 2 可否 | Level 3 可否 | 主な使い方 |
| --- | --- | --- | --- | --- |
| Codex PMO | Level 3 | 可 | 可 | 通常の Issue triage、コメント、作成、更新、close 補助、復旧レビュー。 |
| ChatGPT Business | Level 1 | 条件付き | 原則不可 | GitHub / Drive 文脈の整理、Issue 文案、判断補助。Connector 書き込みは Codex PMO またはユーザー確認を優先。 |
| Claude Code | Level 1 | 条件付き | 条件付き | repo / docs / PR 文脈に基づく Issue コメント案、実装修正との対応整理。書き込みは明示 Issue 番号と投稿文確認後。 |
| Claude Chat | Level 1 | 原則不可 | 原則不可 | 人間文脈、表現調整、PMO コメント案、ユーザー向け説明の作成。 |
| Claude Cowork | Level 1 | 条件付き | 条件付き | Notion / Drive 実務タスクと Issue の接続整理。Issue 書き込みはユーザー確認付きの限定用途。 |
| Gemini Chat / Gems | Level 1 | 原則不可 | 原則不可 | 長文整理、監査、代替案比較、#38 追記案や新規 Issue 案の作成。 |
| Gemini CLI | Level 0 | 条件付き | 条件付き | repo 監査、外部レビュー、差分確認。no sandbox / local auth の扱いに注意し、書き込みは明示スコープ時のみ。 |
| User manual | Level 3 | 可 | 可 | 最終権限者として GitHub UI / CLI で投稿、編集、close、ラベル変更を実行する。 |

「条件付き」は、そのツールが実際に GitHub 書き込み権限を持ち、ユーザーが Issue 番号、操作内容、投稿文または更新範囲を確認した場合のみ許可する。

## Write Pre-checks

Level 2 以上の Issue 書き込み前に、acting lead は次を確認する。

- Target: Issue 番号、repo、URL が明確か。
- Intent: コメント、本文更新、新規作成、ラベル提案、close 提案のどれか。
- Scope: 変更範囲がユーザー依頼または明示スコープ内か。
- Source: 参照した docs / Drive / Notion / PR / chat の出所を説明できるか。
- Duplication: 既存 Issue、特に capacity 系は #38 コメントで足りないか。
- Risk: 誤投稿、個人情報、未確定方針、他者作業の上書きリスクがないか。
- Confirmation: 投稿文または更新要約をユーザーに見せ、軽量確認を取ったか。
- Recovery: Codex PMO が後で追跡できる handoff を残せるか。

軽量確認の例:

```text
Issue #38 に capacity incident として以下をコメントします。
目的: Codex PMO capacity limit の発生ログ
範囲: 事象、影響、暫定対応、次回確認のみ
投稿してよいですか？
```

## Post-write URL Logging

書き込み後は、必ず投稿先 URL を記録する。

最低限のログ:

```markdown
**Issue write log**
- Tool: [acting lead tool]
- Level: Level 2 / Level 3
- Target: [Issue URL or new Issue URL]
- Action: comment / body update / create / label proposal / close proposal
- Scope confirmed by: user / Codex PMO / prior explicit instruction
- Follow-up owner: Codex PMO
```

URL が取得できない場合は、Issue 番号、投稿時刻、投稿冒頭 1 行、実行ツールを残す。後続の Codex PMO が GitHub 上で確認できる粒度にする。

## Fallback PMO Handoff

Level 2 以上の代替書き込みでは、以下の handoff を残す。Issue コメント、作業チャット、または PMO ログのいずれかに記録する。

```markdown
**Fallback PMO Handoff**
- Acting lead: [tool / person]
- Authority level: Level 2 / Level 3
- Trigger: [Codex PMO capacity limit / urgent blocker / user request]
- Target issue: [# / URL]
- Action taken: [what was written or changed]
- User confirmation: [yes/no + short basis]
- Source consulted: [docs / PR / Drive / Notion / chat]
- Why not #38 only: [N/A or distinct incident / recovery task / permanent countermeasure]
- Remaining risk: [N/A or concise risk]
- Required Codex PMO review: [what to verify after recovery]
- Post-write URL: [URL]
```

Level 1 の場合も、重要な下書きには `Acting lead`、`Target issue`、`Draft purpose`、`Required reviewer` を残す。

## Allowed Operations By Level

| Operation | Level 0 | Level 1 | Level 2 | Level 3 |
| --- | --- | --- | --- | --- |
| Issue 読み取り | 可 | 可 | 可 | 可 |
| Issue 要約 | 可 | 可 | 可 | 可 |
| コメント下書き | 不可 | 可 | 可 | 可 |
| 既存 Issue へのコメント投稿 | 不可 | 不可 | 可 | 可 |
| Issue 本文の軽微な補足 | 不可 | 不可 | 可 | 可 |
| 新規 Issue 作成 | 不可 | 下書きのみ | 原則不可 | 可 |
| ラベル変更 | 不可 | 提案のみ | 原則不可 | ユーザー確認後のみ |
| Issue close / reopen | 不可 | 提案のみ | 原則不可 | 原則 Codex PMO またはユーザー実行 |
| 優先順位・運用ルール変更 | 不可 | 提案のみ | 原則不可 | ユーザー確認後の暫定コメントまで |

## Codex Recovery Checklist

Codex PMO が capacity / token / usage limit から復旧したら、次を確認する。

1. #38 の最新コメントを確認し、capacity incident が集約されているか見る。
2. Fallback PMO Handoff を検索し、Level 2 / Level 3 書き込みを一覧化する。
3. 各 post-write URL を開き、投稿内容、Issue 番号、スコープ、重複を確認する。
4. 新規 Issue が作成されていた場合、#38 コメントで足りなかった理由を確認する。
5. 暫定更新が恒久方針に見えていないか確認し、必要なら Codex PMO コメントで補正する。
6. ラベル、assignee、milestone、project relation が必要なら通常 PMO 手順で整理する。
7. Drive SSOT、GitHub Mirror、Notion、Project Knowledge の更新要否を判断する。
8. 復旧レビューコメントを該当 Issue または #38 に残す。

復旧レビューコメントの最小形:

```markdown
**Codex PMO Recovery Review**
- Reviewed fallback action: [URL]
- Scope check: OK / needs correction
- Routing check: #38 comment was enough / separate Issue justified
- Follow-up: N/A / [next action]
```

## Guardrails

- 代替ツールは「PMOの席に一時的に座る」が、「PMOの権限を恒久的に持つ」わけではない。
- 書き込みは、観測された事実、ユーザー確認済みの判断、明示された次アクションに限定する。
- 未確定の戦略判断は、Issue 本文へ断定的に反映せず、コメントまたは draft として残す。
- 他ツールや他者が作業中の Issue は、上書きではなく追記を基本にする。
- Capacity 系のログは #38 優先。新規 Issue は、別事故、復旧作業、恒久対策に限る。
- Codex PMO 復旧後にレビューできない書き方、URL が残らない書き方、判断理由が追えない書き方は禁止する。

