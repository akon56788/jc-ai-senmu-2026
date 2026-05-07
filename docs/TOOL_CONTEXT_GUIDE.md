# 各ツール向けコンテクストガイド

**Version**: 1.0  
**Date**: 2026-05-07  
**Updated by**: Code・Cowork  
**Status**: Phase 4 完了時点のプロジェクトスナップショット

---

## 📋 概要

あきる野青年会議所「2026年度専務理事対応（AI活用）」プロジェクトが Phase 4 を完了しました。GitHub ↔ Drive SSOT ワークフローが標準化され、全ツール間での連携仕様が統一されました。

このガイドは **各ツールが自分たちの役割を理解し、プロジェクトに効果的に関わるための** コンテクストをまとめています。

---

## 🎯 プロジェクト全体構造

### 3 つのカテゴリ

| カテゴリ | 定義 | 優先度 | 進捗管理 |
|---------|------|--------|---------|
| **1. 専務プロジェクト** | 専務理事対応・期限付き案件 | 🔴 最高 | Notion |
| **2. 専務タスク** | プロジェクト外の単発業務 | 🟡 高 | Notion |
| **3. 環境開発** | ツール・ワークフロー改善 | 🟢 ベストエフォート | GitHub Issues / Chat |

**Phase 4 の成果**: カテゴリ 3「環境開発」で GitHub ↔ Drive SSOT 同期を完全化

---

## 🏗️ SSOT アーキテクチャ

```
Drive Google Docs (SSOT: 正本)
       ↑↓
  同期スクリプト
       ↑↓
GitHub Docs/ (Mirror: 複製・版管理)
```

**原則:**
- **Drive が最新版の正本**（modifiedTime で版管理）
- **GitHub がバージョン管理**（commit log で履歴追跡）
- **更新フロー**: GitHub commit → Drive 同期スクリプト → Drive 反映

**ファイル管理:**
- 全 14 ファイル
- CODE 担当: 7 ファイル（AGENTS, SHARED_SOURCE, README, DRIVE_SYNC_* など）
- CODEX 担当: 6 ファイル（notion_poc_design, CLAUDE_enhanced, VISION, CODEX_* など）
- Cowork 進捗監視: 全ファイル（Read-only）

---

## 🔄 GitHub ↔ Drive 同期ワークフロー（標準化済み）

### 再利用可能スクリプト

**単一ファイル同期:**
```bash
python github_to_drive_sync.py --file [filename] --drive-id [id]
```

**複数ファイル一括同期:**
```bash
python github_to_drive_sync_batch.py --tool Code    # CODE 担当分全部
python github_to_drive_sync_batch.py --tool Codex   # CODEX 担当分全部
```

詳細: [`GITHUB_DRIVE_SYNC_WORKFLOW.md`](GITHUB_DRIVE_SYNC_WORKFLOW.md)

---

## 🛠️ ツール別ロール＆コンテクスト

### ✅ Code（Claude Code）

**責務:**
- GitHub リポジトリのリード・実装
- GitHub ↔ Drive SSOT 同期スクリプト管理
- CODE 担当 7 ファイルの更新・管理
- Notion への進捗 Push（種別 1・2）

**参照ドキュメント:**
- [`CLAUDE.md`](../.claude/projects/jc-ai-senmu-2026/CLAUDE.md) ← **最初に読む**
- [`GITHUB_BRANCH_RULESET_CONFIG.md`](GITHUB_BRANCH_RULESET_CONFIG.md)
- [`GITHUB_DRIVE_SYNC_WORKFLOW.md`](GITHUB_DRIVE_SYNC_WORKFLOW.md)

**特に重要:**
- GitHub branch protection 12 項目は **既に有効化済み**（Phase 3 完了）
- GitHub 更新 → Drive 同期は **スクリプト 2 種類で自動化可能**
- CODE 担当ファイル更新時は、必ず Drive 同期スクリプトを実行

**ファイル責務:**
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

---

### 🔍 Codex（Claude Codex）

**責務:**
- Code のサポート・分析・レビュー
- Codex 担当 6 ファイル（VISION, CODEX_*, notion_poc_design など）の更新
- GitHub 上のコード・ドキュメント分析
- Notion への Codex-specific 情報提供（種別 2 のサポート）

**参照ドキュメント:**
- [`CLAUDE.md`](../.claude/projects/jc-ai-senmu-2026/CLAUDE.md) ← **Code と共通**
- [`CODEX_WORKFLOW.md.txt`](CODEX_WORKFLOW.md.txt)
- [`VISION.md`](VISION.md)

**特に重要:**
- Code が GitHub → Drive 同期を実行する際、Codex も同時にスクリプト実行可能
- Codex 担当ファイルを更新したら `python github_to_drive_sync_batch.py --tool Codex` で自動同期

**ファイル責務:**
```
CODEX 担当 (6 files):
  - notion_poc_design.md
  - CLAUDE_enhanced.md
  - VISION.md
  - CODEX_WORKFLOW.md.txt
  - CODEX_PROJECT_SETUP.txt
  - codex_context_latest.txt
```

---

### 📊 Cowork（Claude Cowork）

**責務:**
- Notion での進捗管理（種別 1・2）
- GitHub・Drive SSOT の進捗監視（Read-only）
- ツール間の競合検出・調整
- 進捗レポーティング

**参照ドキュメント:**
- [`CLAUDE.md`](../.claude/projects/jc-ai-senmu-2026/CLAUDE.md) ← 種別 1・2 定義
- [`GITHUB_DRIVE_SYNC_WORKFLOW.md`](GITHUB_DRIVE_SYNC_WORKFLOW.md) ← 競合回避ルール

**特に重要:**
- Code・Codex が同じファイルを同時編集しないよう監視
- GitHub・Drive の差分を定期的に確認
- Notion に Phase 進捗を記録

**権限:**
```
✅ Read: GitHub・Drive 全ファイル
✅ Write: Notion プロジェクト管理
❌ Write: GitHub リポジトリ
❌ Write: Drive SSOT ファイル（直接編集禁止）
```

---

### 💬 Claude Chat

**責務:**
- プロジェクト全体の質問サポート
- ドキュメント検索・要約サポート
- Notion 情報の参照・報告アシスト

**参照ドキュメント:**
- [`CLAUDE.md`](../.claude/projects/jc-ai-senmu-2026/CLAUDE.md)
- [`MANIFEST`](https://docs.google.com/document/d/1I1RDFgfo90ZqYIhPnTZukrl3D70gjFy2WOWC2MHpdb4) (Drive)
- すべてのドキュメント（Read-only）

**権限:**
```
✅ Read: 全ドキュメント（GitHub・Drive）
❌ Write: すべて（参照のみ）
```

---

### 🤖 ChatGPT

**責務:**
- 外部参考ツール
- Code・Codex の補助検討

**参照:**
- 必要に応じて、Code または Codex から情報を口頭で提供

**権限:**
```
❌ Access: GitHub・Drive（アクセス不可）
✅ Reference: Cowork・Code・Codex から提供された情報のみ
```

---

## 📌 次ステップ（Phase 5+）

- [ ] GitHub Actions による自動同期の検討（現在はスクリプト手動実行）
- [ ] Drive 監査ログの Spreadsheet 記録（Sync 履歴追跡）
- [ ] 競合解決の自動マージ戦略定義
- [ ] ツール間の定期同期スケジュール化

---

## 🆘 トラブルシューティング

| 問題 | 対応 |
|------|------|
| GitHub と Drive でファイル内容が異なる | Pattern B（Drive 正本）で上書き同期 |
| 同期スクリプトが失敗する | `~/.claude/token.pickle` 認証を確認 |
| Code と Codex が同じファイル編集中 | Cowork が調整・Lock する |

詳細: [`GITHUB_DRIVE_SYNC_WORKFLOW.md`](GITHUB_DRIVE_SYNC_WORKFLOW.md#-トラブルシューティング)

---

## 📞 各ツールへの指示

**Code くん:**
- このドキュメント中の「Code」セクションを参照
- GitHub 更新時は自動同期スクリプトで Drive に反映
- CODE 担当ファイル 7 つの管理リード

**Codex さん:**
- このドキュメント中の「Codex」セクションを参照
- Code のサポート・分析・Codex ファイル管理
- `github_to_drive_sync_batch.py --tool Codex` で自動同期

**Claude Chat:**
- プロジェクト質問時はこのドキュメント + CLAUDE.md を参照
- 回答は各ツールの責務の枠内で提供

**ChatGPT:**
- Code・Codex から相談を受けた際にサポート（参考用）

---

**このガイドは全ツール間で統一されます。定期的に更新してください。**
