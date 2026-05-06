# Drive 同期チェックリスト

**バージョン**: v2.1
**最終更新**: 2026-05-06
**作成者**: Mr. Coro (a.kondo@work-life-renovation.com)

---

## 🎯 同期対象ファイル

### ✅ Markdown ドキュメント

| ファイル名 | 更新内容 | 優先度 | 同期状態 |
|-----------|--------|--------|---------|
| **CLAUDE_enhanced.md** | Facebook 投稿コンテンツ統合・ユースケース・設計思想追加 | 🔴 高 | ✅ 同期完了 |
| **VISION.md（新規）** | 実現技術・ユースケース・設計思想・DB層・AI ツール使い分け詳細版 | 🔴 高 | ✅ 同期完了 |
| **ARCHITECTURE.md** | システム全体像・Chat 壁打ちガイド | 🟡 中 | ✅ 同期済み |
| **classification_rules.md** | 定常業務 vs. プロジェクト分類ルール | 🟢 低 | ✅ 同期済み |
| **lom_process.md** | LOM 発送プロセス・チェックリスト | 🟢 低 | ✅ 同期済み |
| **SHARED_SOURCE.txt** | ツール別役割・分担表 | 🟡 中 | ✅ 同期済み |
| **AGENTS.md.txt** | Codex 作業ルール | 🟡 中 | ✅ 同期済み |

---

## 📌 同期完了の詳細

### 2026-05-05 アップロード完了

| ファイル | Google Drive ID | 形式 | 備考 |
|---------|-----------------|-----|------|
| VISION.md | 1lEvLQw8QR1vpjszkzS6YeNH9C-lnTT0W | text/markdown | 新規作成・314行 |
| CLAUDE_enhanced.md | 1xsMRpiILSugU511ujNtIuk4fQPaIPlKb | text/markdown | v2.0・418行 |

### 2026-05-06 ローカル同期（Cowork）

| ファイル | 処理内容 |
|---------|---------|
| SHARED_SOURCE.txt | 更新履歴テーブル追加・v1.1 |
| CLAUDE_enhanced.md | 更新履歴テーブル整形・v2.1 |
| AGENTS.md.txt | 更新履歴テーブル追加・v1.1 |
| VISION.md | 更新履歴テーブル追加・v1.1 |
| CODEX_WORKFLOW.md.txt | 要点整理・更新履歴追加・v1.1 |
| CODEX_PROJECT_SETUP.txt | 要点整理・更新履歴追加・v1.1 |
| codex_context_latest.txt | 要点整理・更新履歴追加・v1.1 |
| README.md | 更新履歴テーブル追加・v1.1 |
| DRIVE_SYNC_STATUS.md | 更新履歴テーブル追加・v1.1 |
| DRIVE_SYNC_CHECKLIST.md | 更新履歴テーブル追加・v2.1（このファイル） |
| THREAD_NAMING_GUIDE.txt | 更新履歴テーブル追加・v1.1 |
| notion_poc_design.md | 更新履歴テーブル追加・v1.1 |
| MANIFEST | v1.2 作成・Google Docs API で Drive 反映済み |

---

## 📚 ドキュメント構成（推奨読み取り順序）

### 第 1 段階：コア（運用・操作）
1. **CLAUDE_enhanced.md** ← 全体設計・プロジェクト目的・ツール分担（**最初に読む**）
2. **ARCHITECTURE.md** ← Chat での壁打ちガイド・アーキテクチャ詳細
3. **classification_rules.md** ← タスク分類ルール（Cowork が参照）

### 第 2 段階：詳細参考資料
4. **VISION.md** ← 実現技術・ユースケース・設計思想（**全体文脈を深掘る**）
5. **SHARED_SOURCE.txt** ← 各ツール別役割（Chat・Cowork・Code・Codex・ChatGPT）
6. **AGENTS.md.txt** ← Codex 専用ルール

### 第 3 段階：定常業務・運用ハウツー
7. **lom_process.md** ← LOM 発送プロセス（Cowork が定期実行）

---

## 📋 更新履歴

| バージョン | 日付 | 変更内容 | 担当 |
|-----------|------|----------|------|
| v2.1 | 2026-05-06 | Cowork ローカル同期。2026-05-06 ローカル同期分の記録追加・更新履歴テーブル追加 | Cowork |
| v2.0 | 2026-05-05 | VISION.md 追加・CLAUDE_enhanced.md 統合・コンテキスト読み取り順序明記 | Code |
| v1.0 | 2026-05-04 | 初版作成（LOM 発送ドキュメント同期チェック） | Code |
