# GitHub ⇔ Drive SSOT 標準化ワークフロー

**Version**: 1.0  
**Status**: Active (2026-05-06)  
**Applies to**: Code, Codex, Cowork  
**Last Updated**: 2026-05-06

---

## 📋 概要

CODE・CODEX・Cowork の 3 ツール間で GitHub リポジトリと Drive SSOT（Single Source of Truth）を同期するための標準化されたプロセスです。

**目的:**
- ツール間での連携仕様の統一化
- GitHub commit と Drive SSOT の同期タイミングを明確化
- 複数ツール間での重複・競合を防止

---

## 🎯 基本原則

| 原則 | 説明 |
|------|------|
| **Drive が SSOT** | Drive SSOT がソース・オブ・トゥルース。GitHub は Mirror |
| **Commit → Sync** | GitHub へ commit したら、同じセッションで Drive に反映 |
| **タイムスタンプ管理** | Drive 側のタイムスタンプで version を記録 |
| **ツール間非競合** | CODE・CODEX が同じファイルを同時編集しない（Cowork が調整） |

---

## 🔄 標準フロー: Git 更新 → Drive 反映

### ステップ 1: GitHub での作業
```
1.1 ローカルでファイル編集
1.2 git add / git commit
1.3 git push origin [branch]
```

### ステップ 2: Drive への同期（同じセッション内で実行）

```
2.1 Drive ファイル ID を確認（スクリプト内で管理）
2.2 GitHub から最新ファイルを読み込み
2.3 Drive API で該当ファイルを update
2.4 タイムスタンプを確認（Drive で自動更新）
```

### ステップ 3: 確認・報告
```
3.1 Drive での反映を確認
3.2 セッション内で報告（日本語）
```

---

## 📄 ファイル管理マトリックス

| ファイル | Drive ID | GitHub Path | 管理者 | Sync Priority |
|---------|----------|-------------|-------|-------------|
| AGENTS.md.txt | 1B30FtpcK8od86dlwLQJ-4eqnCmnqeohA | docs/ | Code | ⭐⭐⭐ |
| SHARED_SOURCE.txt | 1lDDTOjBUMqOb1EORVfv1RJjGuBL8H0fS | docs/ | Code | ⭐⭐⭐ |
| README.md | 1f6QajaCNq_3lwooBLoARCToj54QcPsTI | docs/ | Code | ⭐⭐ |
| DRIVE_SYNC_STATUS.md | 1hA1qWXRvDpYuVXkwrkCoZu_N1Kjd_KvI | docs/ | Code | ⭐⭐ |
| DRIVE_SYNC_CHECKLIST.md | 1-c0JxteOPAgnhiLIEeG_oQs8w0l8-MyT | docs/ | Code | ⭐⭐ |
| THREAD_NAMING_GUIDE.txt | 1SR7WsbduNB1KpKZVlP1CNnKrG59obXpx | docs/ | Code | ⭐ |
| notion_poc_design.md | 1fuwHgDuwm7bZNA5c06j-kkQt8EeIWFtT | docs/ | Codex | ⭐⭐ |
| CLAUDE_enhanced.md | 1xsMRpiILSugU511ujNtIuk4fQPaIPlKb | docs/ | Codex | ⭐⭐ |
| VISION.md | 1lEvLQw8QR1vpjszkzS6YeNH9C-lnTT0W | docs/ | Codex | ⭐⭐ |
| CODEX_WORKFLOW.md.txt | 11og38-q5gJ6DugZuqXxMcVjIErFHqA77 | docs/ | Codex | ⭐⭐⭐ |
| CODEX_PROJECT_SETUP.txt | 1BLwDyhlhsNJe2HR1Vd1MlKlgj-AumHII | docs/ | Codex | ⭐⭐ |
| codex_context_latest.txt | 1EzHoVlebl3bGCPDTQa8OMFXSxSuSQKSw | docs/ | Codex | ⭐⭐⭐ |
| GITHUB_BRANCH_RULESET_CONFIG.md | 1_KtJ_1WLcYMB7NMZHJP6OHzks5_jBmSC | docs/ | Code | ⭐ |

---

## 🛠️ スクリプト使用方法

### 単一ファイル同期テンプレート

```bash
python github_to_drive_sync.py \
  --file AGENTS.md.txt \
  --drive-id 1B30FtpcK8od86dlwLQJ-4eqnCmnqeohA
```

### 複数ファイル同期（CODE 担当分）

```bash
python github_to_drive_sync_batch.py \
  --tool Code \
  --files AGENTS.md.txt,SHARED_SOURCE.txt,README.md
```

### 複数ファイル同期（CODEX 担当分）

```bash
python github_to_drive_sync_batch.py \
  --tool Codex \
  --files notion_poc_design.md,CLAUDE_enhanced.md,CODEX_WORKFLOW.md.txt
```

---

## 📋 チェックリスト: Git 更新後の Drive 同期

```
[ ] ファイルを GitHub に commit
[ ] git push で GitHub リモートに反映
[ ] Drive ファイル ID を確認（上表参照）
[ ] 汎用スクリプトで Drive に sync
  → python github_to_drive_sync.py --file [filename] --drive-id [id]
[ ] Drive での反映を確認（タイムスタンプ更新）
[ ] セッション内で報告
```

---

## ⚠️ 競合回避ルール

### CODE と CODEX の分担

| 担当ツール | 主管ファイル | 権限 |
|-----------|-------------|------|
| **CODE** | AGENTS.md.txt, SHARED_SOURCE.txt, README.md, DRIVE_SYNC_* | Full |
| **CODEX** | notion_poc_design.md, CLAUDE_enhanced.md, VISION.md, CODEX_* | Full |
| **Cowork** | すべてのファイル | Read-only (進捗レポーティング) |

### 競合時の対応

1. **同時編集の防止**: Cowork が進捗管理（Lock/Unlock 的役割）
2. **変更権限の制限**: 担当ツール以外は Read-only
3. **マージ前の確認**: Cowork が差分確認後に Drive 反映許可

---

## 📊 Sync ログ・監査

### Drive タイムスタンプ

Drive API の `modifiedTime` フィールドで最終更新日時を記録：
```
2026-05-06T12:30:00.000Z (UTC)
```

### セッション内報告フォーマット

```
## GitHub → Drive Sync 完了

**ファイル**: [filename]  
**Drive ID**: [id]  
**Updated**: 2026-05-06 12:30:00 UTC  
**Status**: ✅ Synced  
```

---

## 🔧 トラブルシューティング

| 問題 | 原因 | 解決 |
|------|------|------|
| Drive ファイルが見つからない | File ID が incorrect | 上記表で確認し直す |
| Sync スクリプトが失敗 | 認証情報なし | `~/.claude/token.pickle` を確認 |
| GitHub と Drive で内容が異なる | 競合編集 | Cowork に報告・調整 |

---

## 📝 次のステップ

1. **自動化**: GitHub Actions で自動 sync を検討（Phase 2）
2. **監査ログ**: Sync 履歴を Drive Spreadsheet に記録（Phase 2）
3. **Conflict Resolution**: 自動マージ戦略を定義（Phase 2+）

---

**このワークフローはすべてのツール（CODE・CODEX・Cowork）で統一して適用してください。**
