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
1. **Code のサポート・分析・レビュー**
   - GitHub 上のコード・ドキュメント分析
   - Code の実装案レビュー
   - Notion への Codex-specific 情報提供

2. **全体プロジェクト PMO 役（エージェント PM）**
   - **3 つのカテゴリ全体の進捗監視** → Code・Cowork・Chat の連携確認
   - **ツール間の連携リスク検出** → Code と Cowork の連動漏れ、Notion 更新遅延など
   - **SSOT 同期の健全性監視** → Drive ↔ GitHub 差分がないか定期チェック
   - **進捗ボトルネック検出** → どのタスク・ツールが止まっているか
   - **全体進捗レポート** → 週次・月次で Code・Cowork に報告

3. **Codex 担当 6 ファイルの更新・管理**

**参照ドキュメント:**
- [`CLAUDE.md`](../.claude/projects/jc-ai-senmu-2026/CLAUDE.md) ← **Code と共通**
- [`CODEX_WORKFLOW.md.txt`](CODEX_WORKFLOW.md.txt)
- [`VISION.md`](VISION.md)
- [`MANIFEST`](https://docs.google.com/document/d/1I1RDFgfo90ZqYIhPnTZukrl3D70gjFy2WOWC2MHpdb4) ← **PMO 役として全体監視**

**特に重要:**
- **PMO 視点**: 毎セッション、Code・Cowork の進捗・連携状況を整理・報告
- Code が GitHub → Drive 同期を実行する際、Codex も同時にスクリプト実行可能
- Codex 担当ファイルを更新したら `python github_to_drive_sync_batch.py --tool Codex` で自動同期
- **リスク検出時は即座に Code・Cowork に通知**（ボトルネック・遅延など）

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

**PMO チェックリスト（毎セッション）:**
- [ ] Code の GitHub 更新 → Drive 同期が実行されたか
- [ ] Cowork の Notion 更新は Code の作業と同期しているか
- [ ] Drive ↔ GitHub に差分がないか（SSOT 健全性）
- [ ] 各ツール間の競合・重複がないか
- [ ] ボトルネックはないか（タスク停止・進捗遅延）

---

### 📊 Cowork（Claude Cowork）

**責務:**
1. **Notion での進捗管理（種別 1・2 のみ）**
   - 専務プロジェクト（種別 1）の Notion 登録・更新・完了マーク
   - 専務タスク（種別 2）の Notion 登録・進捗追跡・完了マーク
   - Phase 進捗の可視化・ダッシュボード管理

2. **GitHub・Drive SSOT の整備サポート**
   - Code からの SSOT 同期実行のサポート（ドキュメント確認・確認依頼など）
   - GitHub ↔ Drive 同期後の動作確認
   - 新規ドキュメント追加時の Drive・GitHub への配置サポート

3. **チーム連携の調整**
   - Code・Codex の進捗状況を把握・調整
   - Codex の PMO レポートを受けて対応（ボトルネック解決など）
   - ツール間の情報連携の確認

**参照ドキュメント:**
- [`CLAUDE.md`](../.claude/projects/jc-ai-senmu-2026/CLAUDE.md) ← **種別 1・2 定義（最重要）**
- [`MANIFEST`](https://docs.google.com/document/d/1I1RDFgfo90ZqYIhPnTZukrl3D70gjFy2WOWC2MHpdb4) ← SSOT ファイル一覧・Drive ID
- [`GITHUB_DRIVE_SYNC_WORKFLOW.md`](GITHUB_DRIVE_SYNC_WORKFLOW.md) ← 同期ワークフロー

**特に重要:**
- **種別 3（環境開発）は Notion に登録しない** → GitHub Issues か Chat スレッド内で管理
- Code・Codex が同じファイルを同時編集しないよう監視（Codex の PMO 報告から）
- Codex の PMO レポートから「ボトルネック・リスク検出」を受けたら即座に対応

**権限:**
```
✅ Read: GitHub・Drive 全ファイル（監視用）
✅ Write: Notion プロジェクト・タスク管理
✅ Write: Notion リンク追加（ドキュメント参照用）
❌ Write: GitHub リポジトリ（Read-only）
❌ Write: Drive SSOT ファイル（直接編集禁止 ← スクリプト経由のみ）
```

**Notion 管理範囲:**
```
✅ 種別 1: 専務プロジェクト
  例) あきる野青年会議所「専務理事対応（AI活用）」
  
✅ 種別 2: 専務タスク（プロジェクト外）
  例) 月次レポート、委員会資料作成

❌ 種別 3: 環境開発・ツール改善
  例) GitHub Actions 整備、SSOT 標準化
  → これは GitHub Issues または Chat スレッド内で管理
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

## 📋 ツール間連携・共有ルール（Phase 4.5+）

### コンテクストファイル更新時の共通フロー

コンテクストファイル（CONTEXT_FOR_*.md など）を更新する際は、以下のルールを統一適用：

**優先順序:**
1. **Drive SSOT に先に作成・更新** → Drive ID・リンク確認
2. **ローカル docs/ に GitHub ファイル作成** → git commit/push
3. **各ツール向け依頼分にリンク張る** → 形式統一（番号 + 日本語説明）
4. **Drive 複製ファイル同期**（必要に応じて）

**リンク形式の統一:**
- 自動リンク化防止のため、「番号 + 日本語説明 + URL」形式
- 例：
  ```
  **1. TOOL_CONTEXT_GUIDE (メインコンテクスト)**
  https://docs.google.com/document/d/1mgnZq9d9__wi5GiUVGSaiFJw5GeBMwMa-plP1sXmr3k/edit?usp=drivesdk
  ```

**目的:**
- 各ツールが確実に Drive SSOT リンクにアクセス可能にする
- 並行作業時の SSOT 一貫性を保証
- ファイル名の自動リンク化による表示破損を防止

詳細: [`GITHUB_DRIVE_SYNC_WORKFLOW.md`](GITHUB_DRIVE_SYNC_WORKFLOW.md#-コンテクストファイル更新フロー)

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
