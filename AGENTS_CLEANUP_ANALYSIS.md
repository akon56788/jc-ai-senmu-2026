# AGENTS File Cleanup Analysis & Update Order Documentation

**Date**: 2026-05-06  
**Status**: Analysis Complete - Ready for Manual Deletion  
**Test Case**: AGENTS file family (before CODEX_WORKFLOW and SHARED_SOURCE cleanup)

---

## Executive Summary

The AGENTS file family on Google Drive contains **3 versions** due to format transition (`.md` → `.txt`) and incomplete cleanup. Analysis confirms which version is the authoritative SSOT (Single Source of Truth).

**Recommendation**: 
- ✅ **KEEP** (SSOT): `1B30FtpcK8od86dlwLQJ-4eqnCmnqeohA` (AGENTS.md.txt)
- ❌ **DELETE**: `1w76vJOjsZysuydWnIU5Yr5OvGhxPTo5g` (AGENTS.md.txt - older)
- ❌ **DELETE**: `1NhPivBe_V4GEeAhcS0_m3kGj_x5W16op` (AGENTS.md - old format)

---

## Detailed Analysis

### File Comparison Matrix

| Criterion | Keep (SSOT) | Delete #1 | Delete #2 |
|-----------|-------------|-----------|-----------|
| **File ID** | `1B30FtpcK8od86dlwLQJ-4eqnCmnqeohA` | `1w76vJOjsZysuydWnIU5Yr5OvGhxPTo5g` | `1NhPivBe_V4GEeAhcS0_m3kGj_x5W16op` |
| **Filename** | AGENTS.md.txt | AGENTS.md.txt | AGENTS.md |
| **Size** | 21,794 bytes | 20,930 bytes | 5,619 bytes |
| **Generated** | 2026-05-04T14:03:23.429Z | 2026-05-05T04:38:55.768Z | 2026-05-04T13:45:00.371Z |
| **Last Updated** | 2026-05-05T11:30:21.769Z | 2026-05-05T04:38:55.768Z | 2026-05-04T14:03:34.633Z |
| **Format** | Modern (`.txt`) | Modern (`.txt`) | Old (`.md`) |
| **Content Completeness** | 100% (21,794 B) | ~96% (20,930 B) | ~26% (5,619 B) |

### Decision Criteria Applied

1. **Format Priority**: `.txt` > `.md` (operational format changed mid-phase)
2. **Recency**: Last update timestamp (most recent wins)
3. **Completeness**: File size as proxy for content completeness

### Timeline of Updates

```
2026-05-04 13:45   → AGENTS.md (old format) created
2026-05-04 14:03   → AGENTS.md.txt (KEEP) created + AGENTS.md updated
2026-05-05 04:38   → AGENTS.md.txt (DELETE #1) created/updated
2026-05-05 05:59   → GitHub version synced (21,375 bytes)
2026-05-05 11:30   → AGENTS.md.txt (KEEP) updated to 21,794 bytes ✓ MOST RECENT
```

**Key Finding**: Drive SSOT (21,794 B) is **5.5 hours newer** than GitHub version (21,375 B), indicating post-sync updates on Drive.

---

## Update Order Operations & Implementation Plan

### Phase 1: AGENTS File Cleanup (Current)
**Status**: Ready for deletion  
**Files to Delete** (Google Drive):
1. File ID: `1w76vJOjsZysuydWnIU5Yr5OvGhxPTo5g`
   - Size: 20,930 bytes
   - Notes: Newer timestamp than old format file, but no updates after generation
   
2. File ID: `1NhPivBe_V4GEeAhcS0_m3kGj_x5W16op`
   - Size: 5,619 bytes (only 26% of full content)
   - Notes: Old `.md` format, obsolete since format migration

**How to Delete**:
- Open Google Drive: https://drive.google.com/drive/folders/11ryHnY2sXh9Ofio3vSsFHxOQhOr6Wcau
- Right-click each file ID above → Select "Remove" or "Delete"
- Confirm deletion in trash (files remain recoverable for 30 days)

### Phase 2: GitHub Sync Update (2026-05-06 Post-Deletion)
After deletion, sync the most current Drive version to GitHub:
```bash
cd /c/Users/User/jc-ai-senmu-2026

# Pull latest from GitHub
git pull origin main

# Download updated AGENTS.md.txt from Drive (ID: 1B30FtpcK8od86dlwLQJ-4eqnCmnqeohA)
# Place in: docs/AGENTS.md.txt

# Stage and commit
git add docs/AGENTS.md.txt
git commit -m "docs: Sync AGENTS.md.txt from Drive SSOT (2026-05-05T11:30 UTC) — Phase 1 cleanup"
git push origin main
```

### Phase 3: Apply to Other File Families (2026-05-07+)
Use same analysis methodology for:
1. **CODEX_WORKFLOW** file family (expected 3+ versions)
2. **SHARED_SOURCE** file family (expected 3+ versions)
3. **Other context files** in Drive SSOT folder

---

## Validation Checklist

- [x] Drive SSOT folder scanned for file metadata
- [x] Three versions of AGENTS identified (✓ matches previous findings)
- [x] File sizes compared and validated
- [x] Timestamps analyzed for recency
- [x] GitHub version compared against Drive version
- [x] Most current version confirmed: Drive version (21,794 B) > GitHub version (21,375 B)
- [ ] Deletion executed (awaiting user confirmation)
- [ ] GitHub synced with most current Drive version
- [ ] CODEX_WORKFLOW cleanup (pending)
- [ ] SHARED_SOURCE cleanup (pending)

---

## Rationale for Keeping AGENTS.md.txt (ID: 1B30FtpcK8od86dlwLQJ-4eqnCmnqeohA)

1. **Most Recent Update**: 2026-05-05T11:30:21.769Z (5.5 hours after GitHub sync)
2. **Modern Format**: `.txt` format (chosen during Phase 1 operational migration)
3. **Largest Size**: 21,794 bytes indicates full content inclusion
4. **No Degradation**: Consistent with 633-line structure verified in GitHub

This file becomes the **authoritative SSOT** for all future updates until replaced explicitly.

---

## Next Actions

1. **User Execution**: Delete the two marked files from Drive UI
2. **Verification**: Confirm both files appear in Drive Trash
3. **GitHub Sync**: Run Phase 2 commands to update GitHub with any Drive changes since 05:59 UTC
4. **Document Update**: Record successful cleanup in `DRIVE_SYNC_STATUS.md`
5. **Repeat Process**: Apply same methodology to CODEX_WORKFLOW and SHARED_SOURCE
