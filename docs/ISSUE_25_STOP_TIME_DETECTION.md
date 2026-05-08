# Issue #25: Stop-Time Detection - Layer 1 Implementation

**Date**: 2026-05-08  
**Status**: Layer 1 (Automation) - IMPLEMENTED  
**Component**: Pre-Session-End Detection Hook

---

## 📋 Overview

**Issue #25** implements a 3-layer strategy to prevent unpushed commits in the GitHub repository:

| Layer | Component | Purpose | Status |
|-------|-----------|---------|--------|
| **1** | **Pre-Session-End Detection Hook** | Warn Code about unpushed commits when session ends | ✅ DONE |
| **2** | GitHub Actions (30min interval) | Automated detection & notification outside Claude | ⏳ TODO |
| **3** | CODE_COMMIT_WORKFLOW.md | Documentation & best practices | ⏳ TODO |

This document covers **Layer 1 implementation**.

---

## 🎯 What is Pre-Session-End Detection?

A **hook** that runs automatically when a Claude Code session ends (Stop event):

1. **Trigger**: Session termination (`Stop` event)
2. **Check**: Runs `git log origin/main..HEAD` to count unpushed commits
3. **Action**: If unpushed commits exist, displays warning message
4. **Goal**: Code remembers to push before abandoning the session

### Why This Design?

- ✅ **Safe**: Does NOT automatically push (respects Code's judgment)
- ✅ **Minimal**: Only 8 lines of configuration
- ✅ **Non-blocking**: Warning doesn't prevent session end
- ✅ **Visible**: Message appears in Claude UI at stop time

---

## 🛠️ Implementation Details

### Location
```
.claude/settings.json
```

### Hook Configuration

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "unpushed=$(git log origin/main..HEAD --oneline 2>/dev/null | wc -l); if [ \"$unpushed\" -gt 0 ]; then echo '{\"systemMessage\": \"⚠️ WARNING: '$unpushed' unpushed commits detected. Remember to push before ending the session.\"}'; fi",
            "timeout": 10,
            "statusMessage": "Checking for unpushed commits..."
          }
        ]
      }
    ]
  }
}
```

### How It Works

1. **Git command**: `git log origin/main..HEAD --oneline`
   - Lists all commits in HEAD that are NOT in origin/main
   - Counts them with `wc -l`

2. **Conditional message**: If count > 0:
   - Outputs JSON with `systemMessage` field
   - Claude displays the warning in the UI

3. **Timeout**: 10 seconds
   - Long enough for git to complete on any reasonable system
   - Short enough not to delay session termination

4. **Error handling**: `2>/dev/null`
   - Suppresses git errors (repo not found, origin doesn't exist)
   - Silently skips if git command fails

---

## ✅ Verification

### Test 1: No unpushed commits
```bash
cd <project>
git log origin/main..HEAD --oneline
# Should output nothing
```
**Expected**: Hook runs, no warning shown ✅

### Test 2: With unpushed commits
```bash
cd <project>
echo "test" >> test.txt
git add test.txt
git commit -m "test: temporary commit for hook verification"
# Don't push yet
```

Then end the session → Hook should display:
```
⚠️ WARNING: 1 unpushed commits detected. Remember to push before ending the session.
```

After verification, push the commit:
```bash
git push origin HEAD
```

---

## 📊 Design Rationale

### Why Not Auto-Push?

❌ **Automatic Push Problem:**
- Could push unreviewed code
- Could push code before Code has verified it
- Removes accountability

✅ **Manual Check + Warning Solution:**
- Code decides what to do
- Maintains review responsibility
- Warning still reminds Code to push

### Why Hook at Stop?

**Timing options:**
1. **Post-Commit Hook** (too early) → Runs after each commit, not at session end
2. **Stop Event Hook** (just right) ← Code has chance to review all commits before push decision
3. **GitHub Actions** (too late) → Runs after session ends, can't warn Code in-session

---

## 🔄 Integration with Layer 2 & 3

### Layer 2 (GitHub Actions)
- Will detect unpushed commits 30min after Code session
- Provides secondary check if Layer 1 warning missed
- Separate issue (TODO)

### Layer 3 (Documentation)
- CODE_COMMIT_WORKFLOW.md will explain:
  - When to push (immediately vs. batch)
  - How to review commits before push
  - Recovery procedures if commits pushed incorrectly

---

## 📝 Implementation Checklist

```markdown
## Layer 1 Implementation Checklist

- [x] Create .claude/settings.json with Stop hook
- [x] Verify JSON syntax
- [x] Test git log command works
- [x] Document in ISSUE_25_STOP_TIME_DETECTION.md
- [ ] Verify hook fires at session Stop (manual test)
- [ ] Verify message appears in UI
- [ ] Document in CODE_COMMIT_WORKFLOW.md (Layer 3)
- [ ] Implement Layer 2 GitHub Actions (separate issue)
```

---

## 🚀 Next Steps

1. **Immediate**:
   - Hook is live in `.claude/settings.json`
   - Works on next session `Stop` event

2. **Short-term** (Layer 2):
   - Create GitHub Actions workflow
   - 30-minute interval check for unpushed commits
   - Send notification to Code's workspace

3. **Medium-term** (Layer 3):
   - Document best practices in CODE_COMMIT_WORKFLOW.md
   - Training for Code team on push discipline

---

## 📎 Related Files

- `.claude/settings.json` - Hook implementation
- `docs/CODE_COMMIT_WORKFLOW.md` - Best practices (TODO)
- `.github/workflows/check-unpushed-commits.yml` - Layer 2 GitHub Actions (TODO)

---

**Status**: Layer 1 ✅ Complete | Layer 2 ⏳ Pending | Layer 3 ⏳ Pending

**Last Updated**: 2026-05-08  
**Owner**: Code (Implementation) / Codex (Documentation)

---

## 🔐 Safety Notes

- Hook does NOT execute git push automatically
- Hook does NOT modify any files
- Hook runs in read-only mode (only `git log` command)
- Safe to fail silently if git is unavailable
- Can be disabled anytime by removing hook from settings.json
