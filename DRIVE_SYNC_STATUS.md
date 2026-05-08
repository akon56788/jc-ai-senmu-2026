# DRIVE_SYNC_STATUS

**Last Updated:** 2026-05-08
**Status:** Phase 1 Complete + Engagement System Integration (ミラー配置)

## Source Of Truth

- Phase 0: Google Drive remains the SSOT for operational context files.
- Phase 1: **Google Drive is SSoT for context files & engagement system files; GitHub is Mirror for version control & diff tracking.**
- Repository: https://github.com/akon56788/jc-ai-senmu-2026

## Current Scope

### Context Files (GitHub SSoT → Drive Sync)
- `docs/SHARED_SOURCE.txt`
- `docs/AGENTS.md.txt`
- `docs/CODEX_WORKFLOW.md.txt`

### Engagement System Files (GitHub SSoT + Drive ミラー配置)
- **Narrative File**: `kondo_narrative_v1.16.md`
  - GitHub SSoT: `docs/narrative/kondo_narrative.md` (commit: ebeaa7f)
  - Drive Mirror: ID `1LsrD7u-Jd5Py1Qv2d3FkWe1oeUoFVwd-xhYaCM4y6TU`
  - Folder: 専務理事対応（AI活用）
  - Purpose: 全ツール（Code・Codex・Cowork）アクセス用
  - Sync Date: 2026-05-08

## Sync Rules

- Prefer `.txt` context files over `.gdoc` files.
- Do not use files under `old/` as active context.
- Commit verified Phase 1 updates to GitHub after local validation.
- Keep Drive as the operational reference until Phase 1 migration is explicitly completed.

## Next Checks

- Claude Code GitHub push permission.
- Codex GitHub read/workflow validation permission.
- GitHub MCP connectivity.
- Initial repository setup commit reflected on GitHub.