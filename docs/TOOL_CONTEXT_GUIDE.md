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
- 全 14 ファイル（SSOT management）
- CODE 担当: 7 ファイル（AGENTS, SHARED_SOURCE, README, DRIVE_SYNC_* など）
- CODEX 担当: 6 ファイル（notion_poc_design, CLAUDE_enhanced, VISION, CODEX_* など）
- Cowork 進捗監視: 全ファイル（Read-only）

**Engagement System Files** (Issue #21・Phase 5):
- Drive SSoT: 近藤さんの narrative file（Google Drive で保存・全ツールアクセス用）
- GitHub Mirror: `docs/pmo_engagement_template.md`, `docs/kondo_core_roles.md`, `docs/llm_engagement_systemprompt.md`
- 用途: タスク説明時に「意味・効果」を示唆し、モチベーション・活力を引き出す

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

4. **Code / Cowork / Chat の補完・代替・保管**
   - Code の Token 不足・並行業務時に、GitHub 差分確認、PR / Actions 確認、軽微な docs 修正、検証結果整理を補完
   - Cowork の作業が詰まる場合に、Notion / Drive / Sheets 連携状況の確認、進捗報告文、未登録・遅延タスク整理を補完
   - Chat に渡す前の論点整理、リスク整理、スレッド命名案の下書きを補助
   - 代替実行時は、実施内容・結果・未決事項・主担当への戻し先を必ず残す

5. **ChatGPT / Gemini への外部レビュー依頼（半自動）**
   - 重要な方針変更、SSOT 変更、GitHub / Drive / Notion 連携変更では、必要に応じて外部レビューを依頼
   - ChatGPT / Gemini は客観レビュー、反対意見、抜け漏れ確認、リスク指摘を担当
   - Codex は `scripts/external_review.py` でレビュー依頼文を生成し、Gemini CLI が利用可能な場合は半自動で実行
   - 外部レビュー結果は助言扱いとし、最終判断・反映・SSOT 更新は Codex / Code / Cowork / Chat とユーザー判断で行う

**参照ドキュメント:**
- [`CLAUDE.md`](../.claude/projects/jc-ai-senmu-2026/CLAUDE.md) ← **Code と共通**
- [`CODEX_WORKFLOW.md.txt`](CODEX_WORKFLOW.md.txt)
- [`VISION.md`](VISION.md)
- [`MANIFEST`](https://docs.google.com/document/d/1I1RDFgfo90ZqYIhPnTZukrl3D70gjFy2WOWC2MHpdb4) ← **PMO 役として全体監視**

**特に重要:**
- **Agent PMO 視点**: 毎セッション、Code・Cowork の進捗・連携状況を整理・報告
- **補完視点**: Token 不足・並行業務・一時離脱で主担当が止まる場合は、Codex が一時的にサブ担当として代替確認・保管・引き継ぎを行う
- **外部レビュー視点**: 重要変更では ChatGPT / Gemini に客観レビューを依頼し、Codex が結果を要約・分類して PMO 報告に反映
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
- 手動・対話型の外部顧問レビュー
- Codex PMO またはユーザーから共有された文脈に基づく客観レビュー、反対意見、リスク確認
- 技術相談、運用設計、ツール分担、責務境界に関する助言
- Code / Codex / Cowork / Gemini CLI へ渡す依頼文案の作成支援
- 最終判断、GitHub / Drive / Notion 反映、SSOT 更新は行わない

**参照:**
- 詳細な役割定義は [`CONTEXT_FOR_CHATGPT.md`](CONTEXT_FOR_CHATGPT.md) を正とする
- 当面は Codex がレビュー依頼文に必要な SSOT 要約・差分・判断対象を含めて渡す

**権限:**
```
❌ Access: GitHub・Drive（アクセス不可）
✅ Reference: Cowork・Code・Codex から提供された情報のみ
```

---

### ♊ Gemini（外部レビュー・半自動レビュアー）

**責務:**
- Codex PMO が生成したレビュー依頼文に対する客観レビュー
- 方針・設計・SSOT・自動化変更のリスク、抜け漏れ、矛盾の指摘
- GitHub / Drive / Notion 連携変更に対する第三者視点の確認
- ChatGPT が手動・対話型の外部顧問であるのに対し、Gemini CLI は Codex がコマンドで呼び出す半自動レビュー実行役

**利用方法:**
```powershell
python scripts/external_review.py --target docs/TOOL_CONTEXT_GUIDE.md --question "PMO role update risk check"
python scripts/external_review.py --target docs/TOOL_CONTEXT_GUIDE.md --question "PMO role update risk check" --run-gemini
```

**権限:**
```
✅ Review: Codex が渡した文脈への客観レビュー
✅ Output: Blocker / Risk / Suggestion / No issue の分類
❌ Write: GitHub・Drive・Notion の直接更新
❌ Decision: 最終意思決定
```

詳細: [`EXTERNAL_REVIEW_WORKFLOW.md`](EXTERNAL_REVIEW_WORKFLOW.md)

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

## 🔁 補完・代替実行時の引き継ぎルール

Code / Cowork / Chat へ人を介して依頼・引き継ぎする場合は、以下の出力構造を使います。

```markdown
【依頼先】Code / Cowork / Chat
【目的】何を完了・確認してほしいか
【背景】Codex が確認した事実・差分・リスク
【対象】ファイル名、PR、Drive URL、Notion項目など
【依頼内容】番号付きで具体化
【Codex実施済み】実行済み作業・検証結果
【未決事項】判断待ち・確認待ち
```

補完・代替実行は、主担当の権限を奪うものではありません。Codex はプロジェクトを止めないための一時的なサブ担当として動き、完了後は主担当へ戻します。

---

## 🔎 外部レビュー連携ルール（ChatGPT / Gemini）

Codex PMO は、重要変更時に ChatGPT / Gemini CLI を外部レビュー役として使えます。ChatGPT は手動・対話型、Gemini CLI は半自動・コマンド駆動のレビュー層です。通常は Gemini CLI の半自動フローから開始し、対話的な確認や文案調整が必要な場合は ChatGPT へ手動共有します。

```text
1. Codex が変更対象・論点・差分を整理
2. scripts/external_review.py で reviews/ に依頼文を生成
3. Gemini CLI がある場合は --run-gemini で実行
4. 対話的な追加確認が必要な場合、または Gemini CLI がない場合は ChatGPT に手動共有
5. Codex が結果を Blocker / Risk / Suggestion / No issue に分類
6. ユーザー確認後、必要なら GitHub PR、PMO レポート、SSOT 更新案に反映
```

外部レビューは助言です。レビュー結果を採用するかどうか、また GitHub / Drive / Notion へ反映するかは、Codex PMO と主担当ツール、最終的にはユーザー判断で決めます。

---

## 📌 次ステップ（Phase 5+）

- [ ] GitHub Actions による自動同期の検討（現在はスクリプト手動実行）
- [ ] Drive 監査ログの Spreadsheet 記録（Sync 履歴追跡）
- [ ] 競合解決の自動マージ戦略定義
- [ ] ツール間の定期同期スケジュール化
- [ ] Gemini CLI / ChatGPT を使った外部レビューの自動化範囲を段階的に拡張

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
- Code / Cowork / Chat の補完・代替・保管が必要な場合は、サブ担当として検証・整理・引き継ぎを実行
- 重要変更では ChatGPT / Gemini 外部レビューを半自動で依頼し、結果を PMO 観点で要約
- `github_to_drive_sync_batch.py --tool Codex` で自動同期

**Claude Chat:**
- プロジェクト質問時はこのドキュメント + CLAUDE.md を参照
- 回答は各ツールの責務の枠内で提供

**ChatGPT:**
- 手動・対話型の外部顧問レビュー役として、共有された文脈に基づき助言・リスク指摘・依頼文案作成を行う

---

**このガイドは全ツール間で統一されます。定期的に更新してください。**
