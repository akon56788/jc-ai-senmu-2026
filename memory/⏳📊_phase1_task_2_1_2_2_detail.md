---
name: Phase 1 Task 2-1・2-2 詳細状態
description: Task 2-1（引継ぎ書確認）と Task 2-2（リポジトリ整理）の詳細・ファイルID・期限管理
type: project
originSessionId: 3fc0d7ec-517f-4e89-961f-308b49b468d4
---
# Phase 1 Task 2-1・2-2 詳細

**更新日**: 2026-05-05  
**期限**: 2026-05-08  
**進捗**: 40%（Google Drive 同期・GitHub Push 待ち）

## Task 2-1: 引継ぎ書類の最新性確認

**担当**: ユーザー  
**確認対象ファイル**:
1. LOM発送_専務理事対応_引き継ぎ書.docx
2. LOM発送_スレッド運用ガイド.docx
3. LOM発送_確認チェックリスト.xlsx

**確認項目**:
- 更新日時が 2026-04 以降
- 実務で使用されている項目がすべて反映
- Codex・Cowork が参照する際に齟齬がない

---

## Task 2-2: リポジトリ構成の整理（Priority 1-A・1-B）

### Phase 1-A: Google Drive SSOT ファイルダウンロード（期限: 2026-05-06）

**対象ファイル** (前セッション 2026-05-05 で更新済み)：

| ファイル | Google Drive ID | 配置先 |
|---------|-----------------|--------|
| SHARED_SOURCE.txt | 1lDDTOjBUMqOb1EORVfv1RJjGuBL8H0fS | docs/ |
| AGENTS.md.txt | 1B30FtpcK8od86dlwLQJ-4eqnCmnqeohA | docs/ |
| CODEX_WORKFLOW.md.txt | 11og38-q5gJ6DugZuqXxMcVjIErFHqA77 | docs/ |

**実行内容**:
1. Google Drive API または手動ダウンロード
2. ファイルを `docs/` に配置
3. ファイルサイズ・エンコーディング確認（UTF-8）
4. DRIVE_SYNC_STATUS.md に同期日時記録

### Phase 1-B: GitHub Push・権限確認（期限: 2026-05-06）

**実行内容**:
```bash
cd /c/Users/User/jc-ai-senmu-2026
git add .
git commit -m "Initial repository setup: Phase 0 → Phase 1 準備"
git branch -M main
git push -u origin main
```

**確認項目**:
- [ ] コミットが GitHub に反映
- [ ] README.md がリポジトリトップに表示
- [ ] docs/ フォルダが見える
- [ ] .gitignore が機能
- [ ] Claude Code: Push 権限あり
- [ ] Codex: Read 権限あり

### Phase 2: LOM 資料同期（期限: 2026-05-07）

**配置先**: `LOM_2026_docs/`

対象ファイル：
- LOM発送_専務理事対応_引き継ぎ書.docx
- LOM発送_スレッド運用ガイド.docx
- LOM発送_確認チェックリスト.xlsx
- 各月の発送資料（1, 2, 3, 5, 6, 7 回分）

---

## GitHub Repository 基本構成

**リポジトリ**: https://github.com/akon56788/jc-ai-senmu-2026

```
jc-ai-senmu-2026/
├── README.md              ✅ 完成
├── .gitignore             ✅ 完成
├── DRIVE_SYNC_STATUS.md   ✅ 完成
├── docs/
│   └── [SHARED_SOURCE.txt, AGENTS.md.txt, CODEX_WORKFLOW.md.txt] ⏳
├── LOM_2026_docs/
│   └── [月次資料・引継ぎ書] ⏳
└── old/
    └── README.md          ✅ 完成
```

---

## Google Drive SSOT

**正本フォルダ**: https://drive.google.com/drive/folders/11ryHnY2sXh9Ofio3vSsFHxOQhOr6Wcau

---

## 次セッション向け

別スレッドで Phase 1 実装フェーズ開始予定（Google Drive 同期・GitHub Push）
