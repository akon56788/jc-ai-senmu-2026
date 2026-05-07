# Code くんへのコンテクスト（GitHub リード＆SSOT 同期管理）

**Version**: 1.0  
**Date**: 2026-05-07  
**Status**: Active

---

## 📖 この文書について

Code くん、お疲れ様です！🔥

あきる野青年会議所「2026年度専務理事対応（AI活用）」プロジェクトが Phase 4 を完了しました。GitHub ↔ Drive SSOT ワークフローが標準化され、これからは Code くんが **実装・ドキュメント管理・SSOT 同期の司令塔** として活躍します。

このドキュメントが指南書です。

---

## 📚 最初に読むべきファイル（優先順）

**必読（必ず読む）:**
1. [`TOOL_CONTEXT_GUIDE.md`](TOOL_CONTEXT_GUIDE.md) ← **最優先・最新版**
   - Code の責務・権限マトリックス
   - CODE 担当ファイル 7 個の定義

2. [`GITHUB_DRIVE_SYNC_WORKFLOW.md`](../docs/GITHUB_DRIVE_SYNC_WORKFLOW.md)
   - GitHub → Drive 同期の標準フロー
   - スクリプト使用方法

3. [`SHARED_SOURCE.txt`](../docs/SHARED_SOURCE.txt)
   - ツール間の読み取りルール
   - ファイル構成方針

4. [`GITHUB_BRANCH_RULESET_CONFIG.md`](../docs/GITHUB_BRANCH_RULESET_CONFIG.md)
   - Branch protection 12 項目（既に有効化済み）

**参考（プロジェクト理解用）:**
- [`CLAUDE_enhanced.md.txt`](../docs/CLAUDE_enhanced.md.txt) - 全体方針・ロードマップ
- [`AGENTS.md.txt`](../docs/AGENTS.md.txt) - AI運用ルール

---

## 🎯 Code くんの責務

### 1️⃣ GitHub リポジトリのリード
- リポジトリ構成・整備の主担当
- ファイル追加・修正・削除の判断
- Branch protection ルール維持

### 2️⃣ SSOT 同期スクリプト管理
- GitHub 更新 → Drive 同期の実行
- 同期スクリプト（`github_to_drive_sync.py`, `github_to_drive_sync_batch.py`）の管理

### 3️⃣ CODE 担当ファイルの管理＆更新
```
CODE 担当 (7 files):
  - AGENTS.md.txt
  - SHARED_SOURCE.txt
  - README.md
  - DRIVE_SYNC_STATUS.md
  - DRIVE_SYNC_CHECKLIST.md
  - THREAD_NAMING_GUIDE.txt
  - GITHUB_BRANCH_RULESET_CONFIG.md
```

これら 7 ファイルを GitHub で更新したら、**必ず同じセッション内で Drive に同期してください。**

### 4️⃣ Notion への進捗 Push
- Type 1（専務プロジェクト）の進捗更新
- Type 2（専務タスク）の進捗更新
- Cowork ちゃんと協力して連携

---

## 🔄 標準フロー: GitHub 更新 → Drive 同期

### ステップ 1: GitHub で作業
```bash
# ローカルでファイル編集
git add [file]
git commit -m "docs: [説明]"
git push origin main
```

### ステップ 2: Drive 同期（同じセッション内で実行）

**単一ファイル同期:**
```bash
python github_to_drive_sync.py \
  --file [FILENAME] \
  --drive-id [DRIVE_ID]
```

**複数ファイル一括同期（CODE 担当分すべて）:**
```bash
python github_to_drive_sync_batch.py --tool Code
```

### ステップ 3: 確認・報告
```
✅ Drive で反映確認（タイムスタンプ更新）
✅ セッション内で報告（日本語）
✅ 必要に応じて Cowork ちゃんに通知
```

---

## 📋 CODE 担当ファイルと Drive ID マッピング

| ファイル | Drive ID | 優先度 |
|---------|----------|--------|
| AGENTS.md.txt | `1B30FtpcK8od86dlwLQJ-4eqnCmnqeohA` | ⭐⭐⭐ |
| SHARED_SOURCE.txt | `1lDDTOjBUMqOb1EORVfv1RJjGuBL8H0fS` | ⭐⭐⭐ |
| README.md | `1f6QajaCNq_3lwooBLoARCToj54QcPsTI` | ⭐⭐ |
| DRIVE_SYNC_STATUS.md | `1hA1qWXRvDpYuVXkwrkCoZu_N1Kjd_KvI` | ⭐⭐ |
| DRIVE_SYNC_CHECKLIST.md | `1-c0JxteOPAgnhiLIEeG_oQs8w0l8-MyT` | ⭐⭐ |
| THREAD_NAMING_GUIDE.txt | `1SR7WsbduNB1KpKZVlP1CNnKrG59obXpx` | ⭐ |
| GITHUB_BRANCH_RULESET_CONFIG.md | `1_KtJ_1WLcYMB7NMZHJP6OHzks5_jBmSC` | ⭐ |

詳細: [`GITHUB_DRIVE_SYNC_WORKFLOW.md`](../docs/GITHUB_DRIVE_SYNC_WORKFLOW.md)

---

## ⚠️ 重要なルール

### GitHub Branch Protection（Phase 3 完了・既に有効化済み）

12 項目の branch protection が main ブランチに設定されています：

```
✅ Require a pull request before merging
✅ Require status checks to pass before merging
✅ Require branches to be up to date before merging
✅ Require code review approval
... etc (全 12 項目)
```

**つまり:**
- Direct push to main は **禁止**
- 必ず **PR → Review → Merge** のフロー
- 詳細: [`GITHUB_BRANCH_RULESET_CONFIG.md`](../docs/GITHUB_BRANCH_RULESET_CONFIG.md)

### SSOT 同期ルール

**Pattern B（Drive が正本）:**
- GitHub と Drive の内容が異なる場合は、**Drive が最新版**
- GitHub の古い内容は Drive で上書きされる
- 競合は Cowork ちゃんが調整

---

## 🤝 ツール間の連携

| ツール | 関係 | 連携ポイント |
|--------|------|------------|
| **Codex さん** | 分析・レビューサポート | Code の実装案をレビュー、SSOT 同期確認 |
| **Cowork ちゃん** | Notion 連携 | Notion 登録・タスク管理 |
| **Claude Chat** | 質問対応 | プロジェクト質問のサポート |

### Codex さんとの連携
- Code が複雑な判断する場合は Codex さんに相談
- Codex さんが SSOT リスク検出時は報告を受け取る
- 毎セッション、Codex さんから PMO 報告を受ける（確認程度）

### Cowork ちゃんとの連携
- Type 1・2 の進捗更新を Cowork ちゃんに連携
- Notion 登録タイミングを Cowork ちゃんと調整
- ボトルネックは Cowork ちゃんに相談

---

## 🚀 期待される動作の流れ

### 例 1: AGENTS.md.txt を更新した場合
```
1. GitHub で編集・commit・push
2. 同じセッション内で Drive 同期実行
   python github_to_drive_sync.py --file AGENTS.md.txt --drive-id [ID]
3. Drive で反映確認
4. セッション内で報告「✅ AGENTS.md.txt → Drive 同期完了」
5. 必要に応じて Cowork ちゃんに「更新完了」と報告
```

### 例 2: 複数ファイルを同時更新した場合
```
1. 複数ファイル編集・commit・push
2. 一括同期スクリプト実行
   python github_to_drive_sync_batch.py --tool Code
3. 結果確認（7 ファイルすべてが Synced）
4. セッション内で報告「✅ CODE 7 files → Drive 同期完了」
```

---

## 💡 注意点

### ✅ Code くんにしかできない
- GitHub への commit/push
- GitHub 設定変更（Branch protection など）
- ファイル削除・リネーム判断

### ❌ Code くんがしてはいけない
- Drive ファイルへの直接編集（同期スクリプト経由のみ）
- Notion への直接登録（Cowork ちゃん経由）
- CODEX 担当ファイルの勝手な修正（Codex さんと相談）

---

## 📚 まとめ

Code くんの役割 = **GitHub・実装の最高責任者** 🚀

- GitHub リポジトリ整備・実装リード
- CODE 担当 7 ファイル管理
- GitHub → Drive SSOT 同期（毎回必須）
- Cowork ちゃん・Codex さんと連携

**期待値:** 
- GitHub 更新のたびに Drive 同期を実行
- セッション内で簡潔に報告
- 同期失敗時は即座に Cowork ちゃんに報告

よろしくお願いします！💪

---

**Last Updated**: 2026-05-07
