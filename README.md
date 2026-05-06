# jc-ai-senmu-2026

【専務理事対応（AI活用）】GitHub 統合プロジェクト

---

## 📌 プロジェクト概要

あきる野青年会議所 **2026年度専務理事対応**を、Claude（AI）で支援・効率化するプロジェクトです。  
GitHub リポジトリは **Phase 1 実装体制の基盤** として構築されています。

---

## 📁 フォルダ構成（30秒ガイド）

| フォルダ | 内容 | 用途 |
|---------|------|------|
| **`docs/`** | AI共通コンテキストファイル（SSOT） | Code・Codex・Cowork が参照する統一ルール・ガイド |
| **`LOM_2026_docs/`** | 月次発送資料・引継ぎ書 | 実務ファイル管理（Google Drive 正本） |
| **`.github/`** | GitHub設定（branch protection等） | リポジトリガバナンス |
| **`old/`** | アーカイブ（参照禁止） | 旧ドキュメント格納 |

---

## 📄 主要ファイル説明

### 📚 Phase 0 → Phase 1 コンテキストファイル（`docs/`）

- **`SHARED_SOURCE.txt`** ← **最初に読む**  
  ツール間の読み取りルール・ファイル構成方針

- **`CLAUDE_enhanced.md.txt`**  
  プロジェクト全体方針・ロードマップ・ツール分担

- **`AGENTS.md.txt`**  
  AI運用ルール・LOM発送手順・スレッド命名規則

- **`CODEX_WORKFLOW.md.txt`**  
  Codex標準ワークフロー・ファイル命名規則

- **`GITHUB_BRANCH_RULESET_CONFIG.md`**  
  GitHub branch protection 12項目の設定方針・Phase別ロードマップ

---

## 🔗 重要リンク

- **Google Drive SSOT**（コンテキスト正本）:  
  https://drive.google.com/drive/folders/11ryHnY2sXh9Ofio3vSsFHxOQhOr6Wcau

- **GitHub Branch Ruleset 詳細**:  
  [`docs/GITHUB_BRANCH_RULESET_CONFIG.md`](docs/GITHUB_BRANCH_RULESET_CONFIG.md)

---

## 🛠️ ツール別アクセス権限

| ツール | GitHub MCP | 権限 | 用途 |
|--------|-----------|------|------|
| **Claude Code** | ✅ | Push・Merge | 実装・テンプレート生成 |
| **Codex** | ✅ | Read | 分析・レビュー・カスタマイズ |
| **Cowork** | — | — | Google Drive・Notion 連携 |

---

## 🔄 GitHub ↔ Drive SSOT 同期ワークフロー（Phase 4 実装）

**基本原則:**
- 🎯 **Drive が SSOT（Single Source of Truth）** ← 最新版の正本
- 🪞 **GitHub が Mirror** ← Drive の複製・バージョン管理用

**運用フロー:**
```
GitHub でファイル編集 → git commit/push → 同期スクリプト実行 → Drive に自動反映
```

**再利用可能スクリプト:**

単一ファイル同期:
```bash
python github_to_drive_sync.py --file AGENTS.md.txt --drive-id 1B30FtpcK8od86dlwLQJ-4eqnCmnqeohA
```

複数ファイル一括同期（CODE担当分）:
```bash
python github_to_drive_sync_batch.py --tool Code
```

複数ファイル一括同期（CODEX担当分）:
```bash
python github_to_drive_sync_batch.py --tool Codex
```

詳細・トラブルシューティング: [`docs/GITHUB_DRIVE_SYNC_WORKFLOW.md`](docs/GITHUB_DRIVE_SYNC_WORKFLOW.md)

---

## 🎯 Phase 進捗

```
✅ リポジトリ基本構成
✅ Google Drive SSOT ファイル同期
✅ Code・Codex アクセス権限確認
✅ GitHub Branch Ruleset 設定・有効化（Phase 3）
✅ GitHub ↔ Drive SSOT ワークフロー標準化（Phase 4）
✅ 同期スクリプト・ドキュメント整備（Phase 4.5）
🚀 Phase 1 本格運用開始
```

---

## 📖 初めての方へ

1. **このリポジトリの目的を理解する**  
   → `docs/SHARED_SOURCE.txt` を読んでください（5分）

2. **プロジェクト方針を確認**  
   → `docs/CLAUDE_enhanced.md.txt` を確認（10分）

3. **実務ルールを確認**  
   → `docs/AGENTS.md.txt` で運用ルール確認（10分）

4. **Code・Codex のローカルプロジェクト設定**  
   → このリポジトリと Google Drive SSOT を参照先に登録

---

**Last Updated**: 2026-05-06  
**Repository Status**: Phase 4 完了・Phase 1 本格運用開始 ✅  
**Workflow**: GitHub ↔ Drive SSOT 同期ワークフロー実装済み
