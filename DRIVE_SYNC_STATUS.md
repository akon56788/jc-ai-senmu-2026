# DRIVE_SYNC_STATUS

**Last Updated:** 2026-05-05
**Status:** Phase 1 GitHub integration preparation

## Source Of Truth

- Phase 0: Google Drive remains the SSOT for operational context files.
- Phase 1: GitHub mirrors the context files for version control and workflow preparation.
- Repository: https://github.com/akon56788/jc-ai-senmu-2026

## Current Scope

- `docs/SHARED_SOURCE.txt`
- `docs/AGENTS.md.txt`
- `docs/CODEX_WORKFLOW.md.txt`

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