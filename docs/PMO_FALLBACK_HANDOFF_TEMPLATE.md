# PMO Fallback Handoff Template

**Status**: Active draft  
**Owner**: Codex PMO  
**Created**: 2026-05-11  
**Related issues**: #38, #45

Use this template when any tool performs PMO work while Codex PMO is unavailable, capacity-limited, degraded, or recovering.

## Short Template

```markdown
## Fallback PMO Handoff

Reason:
- Codex PMO was capacity-constrained / unavailable / degraded.

Fallback tool:
- ChatGPT Business / Gemini / Claude / Cowork / User / other

Authority level:
- Level 0 Read-only / Level 1 Draft-only / Level 2 Scoped write / Level 3 User-confirmed provisional PMO write

Actions performed:
- [Issue/comment/update URL]

User confirmation:
- Confirmed before write: yes/no
- Confirmation summary: ...

Sources read:
- ...

Pending review for Codex recovery:
- Check whether routing target was correct.
- Check whether duplicate Issue/comment was created.
- Check whether Drive SSOT / GitHub Mirror / Notion needs reconciliation.
- Check whether #38 / #36 / #39 / #42 / #45 needs additional cross-link.

Risks / possible gaps:
- ...

Next owner:
- Codex PMO after recovery / User / specific tool
```

## Full Template

```markdown
## Fallback PMO Handoff

### 1. Reason

- Codex PMO state:
  - unavailable / capacity-limited / degraded / recovering / unknown
- Trigger:
  - usage limit / 5-hour limit / automation stopped / connector issue / user request / other
- Related Issue:
  - #38 / #44 / #45 / other

### 2. Fallback Tool

- Tool:
  - ChatGPT Business / Gemini Chat-Gems / Gemini CLI / Claude Chat / Claude Code / Claude Cowork / User manual
- Account / project / source:
  - ...
- Source freshness check:
  - Drive SSOT current? yes/no/unknown
  - GitHub Mirror current? yes/no/unknown
  - Project Knowledge resynced? yes/no/unknown

### 3. Authority Level

- Level:
  - 0 Read-only
  - 1 Draft-only
  - 2 明示スコープ内・軽量確認付きIssue書き込み
  - 3 ユーザー事前確認付き・代替PMO暫定更新権限
- Why this level was appropriate:
  - ...

### 4. User Confirmation

- Was user confirmation obtained before write?
  - yes / no / not applicable
- Confirmation text or summary:
  - ...
- If no, why not:
  - read-only / draft-only / emergency / no write performed

### 5. Actions Performed

- GitHub Issue comments:
  - ...
- New Issues:
  - ...
- Issue updates / close / labels:
  - ...
- Docs or Drive updates:
  - ...
- Notion / Sheets updates:
  - ...

### 6. Comment vs New Issue Decision

- Existing parent Issue considered:
  - #38 / #36 / #39 / #42 / #45 / other
- Decision:
  - comment existing Issue / create incident Issue / create permanent countermeasure Issue / draft only
- Reason:
  - ...

### 7. Pending Review for Codex Recovery

Codex PMO should check:

- [ ] Was the routing target correct?
- [ ] Was #38 used first for capacity context?
- [ ] Was a duplicate Issue/comment created?
- [ ] Are parent/child/cross-links complete?
- [ ] Does Drive SSOT need update?
- [ ] Does GitHub Mirror need commit/push?
- [ ] Does Notion need reconciliation?
- [ ] Does Tool Configuration Register need update?
- [ ] Does Project Ownership Register need update?
- [ ] Does #39 need an abstracted Token-aware lesson?

### 8. Risks / Possible Gaps

- ...

### 9. Next Owner

- Codex PMO after recovery / User / ChatGPT Business / Gemini / Claude / Cowork / other

### 10. Suggested Next Action

- ...
```

## One-Line Footer for Fallback Comments

Use this at the end of Issue comments created during fallback operation:

```markdown
_Fallback PMO note: Added during Codex PMO capacity constraint. Codex PMO should review this entry after recovery._
```
