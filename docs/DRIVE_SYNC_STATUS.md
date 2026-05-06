# Drive ↔ GitHub 同期ステータス

**バージョン**: v1.1
**最終更新**: 2026-05-06
**作成者**: Mr. Coro (a.kondo@work-life-renovation.com)

---

## 📌 SSoT 定義

| フェーズ | SSoT | 状態 |
|---------|------|------|
| Phase 0（現在） | Google Drive | ✅ 運用中 |
| Phase 1（移行中） | GitHub (`jc-ai-senmu-2026`) | 🔵 段階的移行中 |

**方針**: Drive が常にマスター。GitHub は Drive から同期する形で段階的に移行。

---

## 🔵 GitHub 同期スコープ（現在）

### 同期済み（`docs/` 配下）

| Drive ファイル | GitHub path | 同期日 |
|--------------|-------------|-------|
| SHARED_SOURCE.txt | `docs/SHARED_SOURCE.txt` | 2026-05-05 |
| CLAUDE_enhanced.md | `docs/CLAUDE_enhanced.md` | 2026-05-05 |
| AGENTS.md.txt | `docs/AGENTS.md` | 2026-05-05 |

### 未同期（Drive のみ）

| ファイル | 理由 |
|---------|------|
| MANIFEST | Google Doc形式のため要変換 |
| CODEX_WORKFLOW.md.txt | Phase 1 対象予定 |
| CODEX_PROJECT_SETUP.txt | Phase 1 対象予定 |
| codex_context_latest.txt | Phase 1 対象予定 |
| README.md | Phase 1 対象予定 |
| VISION.md | Phase 1 対象予定 |
| notion_poc_design.md | Phase 1 対象予定 |

---

## 📋 同期ルール

1. **Drive → GitHub**: Code または Codex が手動 or GitHub Actions で同期
2. **GitHub → Drive**: 行わない（Drive が SSOT）
3. **競合解決**: Drive 側を優先。GitHub の変更は PR経由でレビュー後に Drive に反映

---

## ✅ 次回チェック項目

- [ ] MANIFEST v1.2 の GitHub path カラム埋め（全16ファイル）
- [ ] GitHub Actions の Drive→GitHub 自動同期ワークフロー設計
- [ ] `docs/` 配下の未同期ファイルの段階的追加

---

## 📋 更新履歴

| バージョン | 日付 | 変更内容 | 担当 |
|-----------|------|----------|------|
| v1.1 | 2026-05-06 | Cowork ローカル同期。更新履歴テーブル追加。GitHub同期スコープ表を整理 | Cowork |
| v1.0 | 2026-05-05 | 初版作成（Phase 0/1 定義・同期スコープ） | Code |
