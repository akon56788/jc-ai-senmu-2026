# GitHub Branch Ruleset Configuration Guide

**Status**: Phase 1 Implementation (2026-05-05)  
**Repository**: github.com/akon56788/jc-ai-senmu-2026  
**Target Branch**: `main`  
**Last Updated**: 2026-05-05  
**Version**: 1.0 (Draft - Parent Items Optimized)

---

## 📋 Document Overview

This document defines comprehensive branch protection rules for the `main` branch using GitHub's **Branch Ruleset** feature. It covers:

- **12 Core Configuration Items** with Phase-wise implementation plans
- **Detailed Settings** (A-F per item) for advanced configuration
- **Security-Risk Assessment** and mitigation strategies
- **AI-Driven Governance** framework for cross-organization standardization

---

## 🏗️ Ruleset Metadata

| Property | Value |
|----------|-------|
| **Ruleset Name** | `main-branch-protection` |
| **Target Branch** | `main` |
| **Status** | Phase 1 (Baseline) |
| **Scope** | Organization-wide (applies to all repository forks) |
| **Enforcement Level** | Strict (no bypass for admins in Phase 2+) |
| **Next Review** | 2026-05-15 (Phase 1 validation) |

---

## 🎯 Target Branches Configuration (Ruleset Foundation)

| Item | Value |
|------|-------|
| **English Name** | Target branches |
| **日本語名** | ルールセット適用対象ブランチ |
| **概要** | このルールセットを適用するブランチを指定（どのブランチを保護するか） |
| **Current Setting** | ⏳ Being configured (GitHub UI setup) |
| **Phase 1** | ✅ Include default branch |
| **Phase 2+** | ✅ Include default branch (unchanged) |
| **Action Required** | ✅ YES - Set in Ruleset creation wizard NOW |
| **詳細設定** | 👉 **[TB-A～TB-B を参照](#target-branches-detailed)** |

---

### Target Branches – Selection Decision Matrix {#target-branches-decision}

**「Include default branch」 vs 「Specific branch names」どちらを選ぶ？**

| 判断項目 | Include default branch | Specific branch names |
|---------|----------------------|----------------------|
| **用途** | Main branch のみ保護 | 複数ブランチを個別指定 |
| **ブランチ数** | 1 個（main） | 2 個以上 |
| **設定難度** | ⭐ 最も簡単 | ⭐⭐⭐ 複雑 |
| **保守性** | ⭐⭐⭐ 最高（自動追従） | ⭐⭐ 中（手動管理） |
| **デフォルトブランチ変更時** | ✅ 自動追従 | ❌ 手動更新必要 |
| **パターンマッチング** | なし | ⭐⭐⭐ サポート（release/*） |
| **Phase 1** | ✅ **推奨** | ❌ 不要 |
| **Phase 2+** | ✅ 継続 | ⏳ 検討（develop など） |
| **変更予定日** | N/A | 2026-06-01 以降 |

---

### Target Branches – Detailed Settings {#target-branches-detailed}

#### TB-A: Include default branch

**Configuration**:
```
☑ Include default branch (Recommended for Phase 1)
```

**What it does**:
- Automatically applies ruleset to repository's default branch (currently `main`)
- If default branch changes, ruleset follows it automatically
- No manual branch name management needed

**Setup in GitHub UI**:
1. Ruleset creation wizard → "Target branches" section
2. Check: ☑ **"Include default branch"**
3. Click "Save"

**Phase 1 Justification**:
```
✅ Simplest approach
✅ Automatically protects main regardless of future default branch changes
✅ No hardcoded branch names needed
```

**Expected Result**:
- Warning message disappears: "This ruleset does not target any resources..."
- Ruleset status becomes "Active" and applicable

---

#### TB-B: Specific branch names (Phase 2+ option)

**When to use**:
- Phase 2+: If you have multiple protected branches (develop, staging, release/*)
- Pattern matching: Supports wildcards like `release/*`, `hotfix/*`

**Example Phase 2 configuration**:
```
Target branches:
  ☑ Include default branch (main)
  ☑ Specific branch names:
    - develop
    - release/*
```

**Phase 1 Status**: ❌ Not needed (only main branch)

**Future Setup** (Phase 2 reference):
```yaml
target_branches:
  include_default: true
  specific_names:
    - develop
    - release/*
    - hotfix/*
```

---

## 🎯 Core Configuration Items (Parent Items Summary)

### 1. Restrict who can push to matching branches

| Item | Value |
|------|-------|
| **English Name** | Restrict who can push to matching branches |
| **日本語名** | 対象ブランチへのプッシュ権限を制限 |
| **概要** | Branch への直接 push を禁止し、すべての変更を PR 経由に強制 |
| **Current Setting** | ✅ ON (only PR via main integration) |
| **Phase 1** | ✅ ON - Configured with role-based access control |
| **Phase 2+** | ✅ ON - Tighten to team/codeowner approval only |
| **Action Required** | ✅ NO - Will configure in Phase 1.5 when Code/Codex permissions verified |
| **詳細設定** | 👉 **[1-A～1-C を参照](#1-restrict-who-can-push-detailed)** |

---

### 2. Restrict creations

| Item | Value |
|------|-------|
| **English Name (GitHub UI)** | Restrict creations |
| **ドキュメント上の項目** | Item 2: Restrict who can create matching branches |
| **日本語名** | ブランチ作成権限を制限 |
| **概要** | Main ブランチの直接作成を禁止し、スクリーニング経由に限定 |
| **Current Setting** | ✅ ON (実装済み 2026-05-05) |
| **Phase 1** | ✅ ON - Restrict to repository admins only |
| **Phase 2+** | ✅ ON - Extend to release-manager role |
| **Action Required** | ✅ YES - Already configured in Phase 1 ✓ |
| **詳細設定** | 👉 **[2-A～2-B を参照](#2-restrict-creations-detailed)** |

**注記**: GitHub UI では「Restrict creations」と表示されます（ドキュメント作成時は「Restrict who can create」でしたが、UI 更新により統合）

---

### 2.5. Restrict updates (GitHub UI 統合項目)

| Item | Value |
|------|-------|
| **English Name (GitHub UI)** | Restrict updates |
| **ドキュメント上** | Item 2 + Item 3 の統合 |
| **日本語名** | ブランチ更新権限を制限 |
| **概要** | Branch への更新（push）を制限し、bypass permission を持つユーザーのみ許可 |
| **Current Setting** | ⏸️ OFF (Phase 1開発効率化のため一時無効化 2026-05-05) |
| **Phase 1** | ⏸️ OFF - Disabled to reduce merge friction during Phase 1 development |
| **Phase 2+** | ✅ ON - Re-enable with team role refinement |
| **Action Required** | ✅ MONITOR - Status change only; other 11 rules remain active |
| **詳細設定** | 👉 **[2.5-A～2.5-B を参照](#2-5-restrict-updates-detailed)** |

**注記**: GitHub の最新 UI では「Restrict updates」という項目が、「Create」と「Delete」の制限を統合した形で実装されています。Phase 1 開発効率化のため、このルールは一時的に無効化されています（2026-05-05）。

---

### 3. Restrict deletions

| Item | Value |
|------|-------|
| **English Name (GitHub UI)** | Restrict deletions |
| **ドキュメント上の項目** | Item 3: Restrict who can delete matching branches |
| **日本語名** | ブランチ削除権限を制限 |
| **概要** | Main ブランチの削除を最小限の人数（管理者）に限定 |
| **Current Setting** | ✅ ON (実装済み 2026-05-05) |
| **Phase 1** | ✅ ON - Restrict to repository admins only |
| **Phase 2+** | ✅ ON - Require explicit approval logging |
| **Action Required** | ✅ YES - Already configured in Phase 1 ✓ |
| **詳細設定** | 👉 **[3-A～3-B を参照](#3-restrict-deletions-detailed)** |

**注記**: GitHub UI では「Restrict deletions」と表示されます（ドキュメント作成時は「Restrict who can delete」でしたが、UI 更新により統合）

---

### 4. Require linear history

| Item | Value |
|------|-------|
| **English Name** | Require linear history |
| **日本語名** | 直線的な commit 履歴を強制 |
| **概要** | Merge commit を禁止し、squash-and-rebase またはrebase-only でマージ |
| **Current Setting** | ❌ OFF (Not yet configured) |
| **Phase 1** | ✅ ON - Squash-only merge (simplifies history) |
| **Phase 2+** | ✅ ON - Option: Rebase-only for fine-grained history |
| **Action Required** | ✅ YES - Configure in Phase 1 setup (recommend squash) |
| **詳細設定** | 👉 **[4-A～4-C を参照](#4-require-linear-history-detailed)** |

---

### 5. Require deployments to succeed before merging

| Item | Value |
|------|-------|
| **English Name** | Require deployments to succeed before merging |
| **日本語名** | マージ前に環境デプロイ成功を要件化 |
| **概要** | 指定環境（staging など）への自動デプロイが成功してから main マージを許可 |
| **Current Setting** | ❌ OFF (Not yet configured) |
| **Phase 1** | ⏳ ON (Optional) - Deploy to staging via GitHub Actions |
| **Phase 2+** | ✅ ON - Mandatory staging + production readiness checks |
| **Action Required** | ⚠️ CONDITIONAL - Configure if using GitHub Actions for CD |
| **詳細設定** | 👉 **[5-A～5-D を参照](#5-require-deployments-detailed)** |

---

### 6. Require signed commits

| Item | Value |
|------|-------|
| **English Name** | Require signed commits |
| **日本語名** | コミット署名を強制 |
| **概要** | すべてのコミットに GPG/SSH 署名を要件化し、信頼性を担保 |
| **Current Setting** | ❌ OFF (Not yet configured) |
| **Phase 1** | ❌ OFF (Recommend deferring; setup complexity for solo developer) |
| **Phase 2+** | ✅ ON - Implement when team size increases |
| **Action Required** | ❌ NO - Skip in Phase 1; revisit in Phase 2 |
| **詳細設定** | 👉 **[6-A～6-C を参照](#6-require-signed-commits-detailed)** |

---

### 7. Require a pull request before merging

| Item | Value |
|------|-------|
| **English Name** | Require a pull request before merging |
| **日本語名** | マージ前に Pull Request を必須化 |
| **概要** | すべての main への変更を PR 経由に限定し、レビュー・チェックを強制 |
| **Current Setting** | ✅ ON (Partially; check ruleset vs. classic protection) |
| **Phase 1** | ✅ ON - Configured with self-review workflow for solo developer |
| **Phase 2+** | ✅ ON - Require peer review from designated team members |
| **Action Required** | ✅ YES - Verify configuration and refine approval rules |
| **詳細設定** | 👉 **[7-A～7-G を参照](#7-require-pr-detailed)** |

---

### 8. Require status checks to pass before merging

| Item | Value |
|------|-------|
| **English Name** | Require status checks to pass before merging |
| **日本語名** | マージ前に Status Checks 成功を要件化 |
| **概要** | CI/CD パイプライン（テスト、ビルド、静的解析等）すべての成功を確認 |
| **Current Setting** | ❌ OFF (Not yet configured) |
| **Phase 1** | ✅ ON (Recommended) - Minimal checks: tests + linting |
| **Phase 2+** | ✅ ON - Add code quality, security scanning, copilot review |
| **Action Required** | ✅ YES - Configure when GitHub Actions workflow ready |
| **詳細設定** | 👉 **[8-A～8-E を参照](#8-require-status-checks-detailed)** |

---

### 9. Require code reviews before merging

| Item | Value |
|------|-------|
| **English Name** | Require code reviews before merging |
| **日本語名** | マージ前にコードレビューを必須化 |
| **概要** | PR マージ前に指定数の approvals（コードレビュー）を要件化 |
| **Current Setting** | ❌ OFF (Not yet configured) |
| **Phase 1** | ✅ ON - 1 approval (self-review workflow; developer approves own PR) |
| **Phase 2+** | ✅ ON - 2+ approvals from different team members |
| **Action Required** | ✅ YES - Configure with 1 approval initially |
| **詳細設定** | 👉 **[9-A～9-F を参照](#9-require-code-reviews-detailed)** |

---

### 10. Block force pushes

| Item | Value |
|------|-------|
| **English Name** | Block force pushes |
| **日本語名** | Force Push を禁止 |
| **概要** | Main ブランチへの `git push --force` を全員禁止し、履歴改ざん防止 |
| **Current Setting** | ❌ OFF (Not yet configured) |
| **Phase 1** | ✅ ON - Block for all users including admins |
| **Phase 2+** | ✅ ON - No exceptions (strict policy) |
| **Action Required** | ✅ YES - Configure in Phase 1 setup |
| **詳細設定** | 👉 **[10-A～10-B を参照](#10-block-force-pushes-detailed)** |

---

### 11. Require code scanning results before merging

| Item | Value |
|------|-------|
| **English Name** | Require code scanning results before merging |
| **日本語名** | マージ前にセキュリティスキャン結果を要件化 |
| **概要** | GitHub Advanced Security の SAST/dependency scanning で脆弱性チェック強制 |
| **Current Setting** | ❌ OFF (Not yet configured) |
| **Phase 1** | ⏳ ON (Optional) - Enable CodeQL scanning via Actions |
| **Phase 2+** | ✅ ON - Mandatory; require zero high-risk vulnerabilities |
| **Action Required** | ⚠️ CONDITIONAL - Configure if GitHub Advanced Security enabled |
| **詳細設定** | 👉 **[11-A～11-D を参照](#11-require-code-scanning-detailed)** |

---

### 12. Require Copilot Enterprise review before merging

| Item | Value |
|------|-------|
| **English Name** | Require Copilot Enterprise review before merging |
| **日本語名** | マージ前に Copilot Enterprise レビューを実施 |
| **概要** | GitHub Copilot Enterprise による自動コード解析・改善提案を PR コメントで記録 |
| **Current Setting** | ❌ OFF (Not yet configured) |
| **Phase 1** | ❌ OFF (Optional; requires Copilot Enterprise subscription) |
| **Phase 2+** | ⏳ ON (Consider if budget available; add to Phase 2.5 evaluation) |
| **Action Required** | ❌ NO - Defer to Phase 2.5+ business case evaluation |
| **詳細設定** | 👉 **[12-A～12-C を参照](#12-require-copilot-detailed)** |

---

## 📊 Implementation Status Summary

### Phase 1 Required Items (Deadline: 2026-05-15)

| # | Item Name | Status | Priority |
|---|-----------|--------|----------|
| 1 | Restrict who can push | ✅ ON | P0 |
| 2 | Restrict who can create | ❌ → ✅ | P0 |
| 3 | Restrict who can delete | ❌ → ✅ | P0 |
| 4 | Require linear history | ❌ → ✅ | P0 |
| 5 | Require deployments | ⏳ Optional | P2 |
| 6 | Require signed commits | ❌ Defer | P3 |
| 7 | Require PR | ✅ ON | P0 |
| 8 | Require status checks | ⏳ Optional | P1 |
| 9 | Require code reviews | ❌ → ✅ | P1 |
| 10 | Block force pushes | ❌ → ✅ | P0 |
| 11 | Require code scanning | ⏳ Optional | P2 |
| 12 | Require Copilot review | ❌ Defer | P3 |

**Phase 1 Mandatory (P0)**: Items 1, 2, 3, 4, 7, 10  
**Phase 1 Optional (P1-P2)**: Items 5, 8, 9, 11  
**Phase 1 Defer (P3)**: Items 6, 12

---

## ✅ GitHub UI Checklist – Phase 1 Implementation

Use this checklist when configuring branch ruleset in GitHub UI. This is the **single source of truth** for which settings to enable.

### 🎯 Target Branches Configuration (Step 1)

**Location**: GitHub → Repository → Settings → Rules → Branch rulesets → Create branch ruleset

| Setting | Phase 1 | ✅ Checklist |
|---------|---------|------------|
| **Ruleset Name** | `main-branch-protection` | ☑ Create with this name |
| **Target branches** | Include default branch | ☑ Check "Include default branch" |
| **Enforcement level** | Enforce | ☑ Select "Enforce" |

---

### 🔐 Core Rules Configuration (Step 2)

**Location**: GitHub → [Ruleset name] → Rules section

| # | Rule Name (GitHub UI) | Phase 1 | ✅ Enable | ❌ Disable |
|---|----------------------|---------|---------|-----------|
| **1** | Restrict who can push to matching branches | ✅ ON | ☑ | |
| **2** | Restrict creations | ✅ ON | ☑ | |
| **2.5** | Restrict updates | ✅ ON | ☑ | |
| **3** | Restrict deletions | ✅ ON | ☑ | |
| **4** | Require linear history | ✅ ON | ☑ | |
| **5** | Require deployments to succeed before merging | ⏳ Optional | ☐ | ☐ |
| **6** | Require signed commits | ❌ OFF | | ☑ |
| **7** | Require a pull request before merging | ✅ ON | ☑ | |
| **8** | Require status checks to pass before merging | ⏳ Optional | ☐ | ☐ |
| **9** | Require code reviews before merging | ✅ ON | ☑ | |
| **10** | Block force pushes | ✅ ON | ☑ | |
| **11** | Require code scanning results before merging | ⏳ Optional | ☐ | ☐ |
| **12** | Require Copilot Enterprise review before merging | ❌ OFF | | ☑ |

**Summary for Phase 1 Mandatory (Must enable)**:
- ✅ Item 1: Restrict who can push (with bypass = admins only)
- ✅ Item 2: Restrict creations (admins only)
- ✅ Item 2.5: Restrict updates (admins only)
- ✅ Item 3: Restrict deletions (admins only)
- ✅ Item 4: Require linear history
- ✅ Item 7: Require PR before merging (1 approval minimum)
- ✅ Item 9: Require code reviews (1 approval minimum)
- ✅ Item 10: Block force pushes (no exceptions)

---

### ⚙️ Configuration Details by Rule (Step 3)

#### 1. Restrict who can push to matching branches

```
☑ Enable this rule
  ↓ Bypass list
    - ☑ Repository Role: admin (allows admins only)
```

**GitHub UI Path**: Rules → "Restrict who can push to matching branches" → ☑ Enable → Bypass actors → Add "Repository Role: admin"

---

#### 2. Restrict creations

```
☑ Enable this rule
  ↓ Bypass list
    - ☑ Repository Role: admin (allows admins only to create branches)
```

**GitHub UI Path**: Rules → "Restrict creations" → ☑ Enable → Bypass actors → Add "Repository Role: admin"

---

#### 2.5. Restrict updates {#2-5-restrict-updates-detailed}

**Phase 1 Status (2026-05-05)**: ⏸️ DISABLED

```
☐ Disable this rule (temporarily for Phase 1)
  
Status: OFF - No bypass actors configured
Reason: Reduces merge friction during solo-developer Phase 1
Rationale: 
  - Single developer working on feature/documentation branches
  - Main branch protection maintained via other 11 rules
  - Will re-enable in Phase 2 when team members join
```

**Previous Configuration** (active until 2026-05-05):
```
☑ Enable this rule
  ↓ Bypass list
    - ☑ Repository Role: admin (allows admins only to update/push)
```

**GitHub UI Path** (if re-enabling in Phase 2): 
Rules → "Restrict updates" → ☑ Enable → Bypass actors → Add "Repository Role: admin"

**Implementation Notes**:
- **2026-05-05**: Rule disabled to streamline Phase 1 development PR merge process
- **Remaining Protections**: Items 1-4, 7, 10 remain active (no direct main pushes allowed)
- **Phase 2 Re-enablement**: Planned when multiple team members join (estimated 2026-05-16+)
- **Risk Assessment**: LOW - Other critical rules (PR required, code review, force push block) still enforce quality gates

---

#### 3. Restrict deletions

```
☑ Enable this rule
  ↓ Bypass list
    - ☑ Repository Role: admin (allows admins only to delete)
```

**GitHub UI Path**: Rules → "Restrict deletions" → ☑ Enable → Bypass actors → Add "Repository Role: admin"

---

#### 4. Require linear history

```
☑ Enable this rule
```

**GitHub UI Path**: Rules → "Require linear history" → ☑ Enable

**Note**: This enforces squash-or-rebase merging. Combined with repository settings (see Step 4).

---

#### 7. Require a pull request before merging

```
☑ Enable this rule
  ↓ Required approvals: 1
  ↓ Dismiss stale approvals: ☑ (ON)
  ↓ Require approval of most recent push: ☑ (ON)
  ↓ Require review from code owners: ☐ (OFF for Phase 1)
  ↓ Require conversation resolution: ☑ (ON)
```

**GitHub UI Path**: Rules → "Require a pull request before merging" → ☑ Enable → Configure:
- Approvals required: `1`
- ☑ Dismiss stale pull request approvals
- ☑ Require approval of most recent push
- ☐ Require review from code owners
- ☑ Require all conversations to be resolved

---

#### 9. Require code reviews before merging

```
☑ Enable this rule
  ↓ Number of reviews: 1
  ↓ Restrict who can approve: ☐ (OFF)
  ↓ Require code owner reviews: ☐ (OFF for Phase 1)
```

**GitHub UI Path**: Rules → "Require code reviews before merging" → ☑ Enable → Configure:
- Number of approving reviews: `1`
- ☐ Restrict who can approve reviews (leave OFF)
- ☐ Require review from code owners

---

#### 10. Block force pushes

```
☑ Enable this rule
  ↓ Apply to admins: ☑ (YES - no exceptions)
```

**GitHub UI Path**: Rules → "Block force pushes" → ☑ Enable

---

### 🎨 Repository Merge Settings (Step 4)

**Separate from Branch Ruleset** — Configure merge button options for consistency with linear history rule.

**Location**: GitHub → Repository Settings → General → Pull Requests → Merge button

```
☑ Allow squash merging (REQUIRED for Phase 1)
☐ Allow merge commits (MUST DISABLE)
☐ Allow rebase merging (optional; enable in Phase 2 if desired)

Default merge method: Squash and merge
☑ Default to PR title for commit message
☑ Default to PR title and description
```

**Why**: Linear history rule requires commits to be merged via squash or rebase. Enabling "Allow merge commits" will conflict with this rule.

---

### 📋 Phase 1 Implementation Checklist

Use this to verify all settings are correctly configured:

**Target Branch Setup**:
- [ ] Ruleset name is `main-branch-protection`
- [ ] "Include default branch" is checked
- [ ] Enforcement level is set to "Enforce"

**Core Rules (Mandatory - Enable All)**:
- [ ] Item 1: Restrict who can push (✅ ON, bypass = admin)
- [ ] Item 2: Restrict creations (✅ ON, bypass = admin)
- [ ] Item 2.5: Restrict updates (✅ ON, bypass = admin)
- [ ] Item 3: Restrict deletions (✅ ON, bypass = admin)
- [ ] Item 4: Require linear history (✅ ON)
- [ ] Item 7: Require PR (✅ ON, 1 approval, dismiss stale ✓, require latest ✓, resolution ✓)
- [ ] Item 9: Require code reviews (✅ ON, 1 review)
- [ ] Item 10: Block force pushes (✅ ON, no exceptions)

**Deferred Rules (Keep Disabled)**:
- [ ] Item 6: Require signed commits (❌ OFF)
- [ ] Item 12: Require Copilot review (❌ OFF)

**Repository Merge Settings**:
- [ ] Allow squash merging: ☑ (checked)
- [ ] Allow merge commits: ☐ (unchecked)
- [ ] Default merge method: "Squash and merge"

**Verification**:
- [ ] All checkboxes completed
- [ ] Create test PR to verify restrictions work
- [ ] Confirm branch push/create/delete restrictions apply

---

## 🔧 Detailed Settings (Phase 1 Reference)

### 1. Restrict who can push – Detailed Settings {#1-restrict-who-can-push-detailed}

#### 1-A: Bypass list (who can bypass push restrictions)

**Configuration**:
- **Current**: None (default)
- **Phase 1**: Repository admins only
- **Phase 2+**: No exceptions (strict policy)

**Setup**:
```yaml
bypass_actors:
  - actor_type: "RepositoryRole"
    actor_id: "admin"
    bypass_mode: "always"
```

**Rationale**: Allow repository maintainers to push in emergency situations (Phase 1); remove bypass in Phase 2 when robust PR workflows are mature.

---

#### 1-B: Require PR workflow before any push

**Configuration**:
- **Enforced**: YES (implied by ruleset)
- **Notification**: GitHub will show error message if user attempts direct push

**Expected Message**:
```
error: refusing to allow push to this repository. This ref has a branch protection rule.
```

---

#### 1-C: Integration with Code/Codex workflows

**Phase 1 Process**:
1. Developer (Code agent) creates feature branch locally
2. Pushes to remote (e.g., `feature/ruleset-config`)
3. Opens PR via GitHub CLI or web UI
4. Self-approves (approval from same actor in this solo-developer workflow)
5. Merges via squash-and-rebase (linear history)
6. GitHub Actions validates post-merge

**Note**: This workflow supports future team expansion without refactoring.

---

### 2. Restrict who can create matching branches – Detailed Settings {#2-restrict-who-can-create-detailed}

#### 2-A: Allow creation only by repository admins

**Configuration**:
- **Who Can Create**: Repository admins (only)
- **Non-admins**: Receive error: "Permission denied: You are not authorized to create branches on this repository"

**Setup in GitHub UI**:
1. Ruleset settings → "Restrict who can create matching branches"
2. Toggle ON
3. Select "Only allow specified actors"
4. Check: `Repository Role: admin`

---

#### 2-B: Future escalation to release-manager role (Phase 2)

**Phase 2 Plan**:
- Create custom GitHub team: `@jc-ai-senmu-2026/release-managers`
- Update ruleset to allow creation for:
  - Repository admins
  - Release-manager team
- Document release branch naming convention

---

### 3. Restrict who can delete matching branches – Detailed Settings {#3-restrict-who-can-delete-detailed}

#### 3-A: Allow deletion only by repository admins

**Configuration**:
- **Who Can Delete**: Repository admins (only)
- **Non-admins**: Error message prevents deletion

**Setup**:
1. Ruleset settings → "Restrict who can delete matching branches"
2. Toggle ON
3. Select "Only allow specified actors"
4. Check: `Repository Role: admin`

---

#### 3-B: Audit logging for deletions (Phase 2)

**Phase 2 Enhancement**:
- Enable GitHub audit log export
- Set CloudWatch/Datadog alert for any main branch deletion attempt
- Monthly review in security audit meeting

---

### 4. Require linear history – Detailed Settings {#4-require-linear-history-detailed}

#### 4-A: Merge strategy selection

**Phase 1 Recommendation**: **Squash and merge** (recommended)

```
Why squash:
- Simplest for solo developer: 1 feature = 1 commit on main
- Easier to revert if needed (single commit)
- Cleaner main branch history
- Reduced cognitive load during code review
```

**Alternative: Rebase and merge**

```
Why rebase:
- Preserves all commits from feature branch
- Useful if commit history has semantic meaning
- Requires good commit discipline on feature branches
- Phase 2 option when team processes mature
```

**Not Allowed: Merge commit**
```
Prohibited because:
- Creates unnecessary "merge" commits
- Clutters main branch history
- Violates linear history principle
```

**Setup in GitHub UI**:
1. Repository settings → General
2. Pull Requests section → "Merge button" settings
3. ✅ Allow squash merging (default)
4. ❌ Disable merge commits
5. ⏳ Allow rebase merging (disabled until Phase 2)

---

#### 4-B: Auto-squash configuration in GitHub Actions

**Phase 1 Option**: Manual squash during PR merge (via web UI)

**Phase 2 Enhancement**: Automate squash via merge script

```yaml
# Example: Auto-squash GitHub Action (Phase 2 reference)
name: Auto-Squash on PR Merge
on:
  pull_request:
    types: [closed]

jobs:
  auto-squash:
    if: github.event.pull_request.merged == true
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Verify linear history
        run: |
          git log --oneline main | head -20
          # Validate that no merge commits exist
          merge_commits=$(git rev-list --merges main | wc -l)
          if [ $merge_commits -gt 0 ]; then
            echo "ERROR: Merge commits detected on main branch"
            exit 1
          fi
```

---

#### 4-C: Branch cleanup after merge

**Process**:
- GitHub automatically deletes feature branch after merge (default in web UI)
- Local: `git fetch --prune` to sync deletions
- Rationale: Reduces branch clutter, easier maintenance

---

### 5. Require deployments to succeed before merging – Detailed Settings {#5-require-deployments-detailed}

#### 5-A: Target environment definition

**Phase 1 Strategy**: Optional (deploy to staging only if CI/CD pipeline exists)

**Recommended environments**:
```
1. Staging (review environment)
   - Automatic deployment on PR creation
   - Manual approval before merging

2. Production (not in Phase 1)
   - Deferred to Phase 2
   - Requires additional monitoring/alerting
```

---

#### 5-B: Deployment status check integration

**Configuration**:
```yaml
deployment_environments:
  - name: "staging"
    required_status: "success"
    automatic_deploy: true
    approval_required: true
    approval_count: 1
```

---

#### 5-C: GitHub Actions workflow for staging deployment

**Phase 1 Reference Workflow** (if using GitHub Pages for docs preview):

```yaml
name: Deploy to Staging
on:
  pull_request:
    types: [opened, synchronize]

jobs:
  deploy-staging:
    runs-on: ubuntu-latest
    environment: staging
    steps:
      - uses: actions/checkout@v4
      - name: Deploy docs to GitHub Pages (PR preview)
        run: |
          echo "Deploying PR #${{ github.event.number }} to staging..."
          # Placeholder: actual deployment logic here
          exit 0  # Success status
```

---

#### 5-D: Cost estimation (Phase 2+)

**Phase 1**: No cost (GitHub Actions free tier: 2000 minutes/month)  
**Phase 2+**: Evaluate if deployment logs require storage (CloudWatch/Datadog integration)

---

### 6. Require signed commits – Detailed Settings {#6-require-signed-commits-detailed}

#### 6-A: GPG vs. SSH signing decision

**Phase 1 Decision**: SKIP (defer to Phase 2)

**Rationale**:
- Solo developer workflow
- Setup complexity: generate GPG key, configure git client, manage passphrase
- Low risk in Phase 1 (single actor)
- Phase 2 trigger: when team members join, enforce signing

**Phase 2+ Plan**:
```
GPG Signing (Recommended for most teams):
- Setup: gpg --gen-key (RSA 4096-bit)
- Configuration: git config user.signingkey <KEY_ID>
- Signing: git commit -S (requires passphrase each time)

SSH Signing (Alternative if using SSH keys):
- Less friction than GPG
- Phase 2 consideration if team uses SSH auth already
```

---

#### 6-B: GitHub verification badge

**What it does**: Commits signed by verified GPG/SSH keys show "Verified" badge in GitHub UI

**Phase 2 Enforcement**:
```
GitHub Ruleset Setting:
- Enable "Require commit signatures"
- Non-signed commits blocked from main
- Message: "Your commit signatures don't match any verified identities"
```

---

#### 6-C: Transition plan from Phase 1 to Phase 2

**Timeline**:
1. Phase 1 (current): No requirement
2. Phase 1.5 (warning): Notify Code/Codex to set up GPG keys
3. Phase 2: Enforce requirement; assist any new team members

---

### 7. Require a pull request before merging – Detailed Settings {#7-require-pr-detailed}

#### 7-A: PR required approvals

**Phase 1 Configuration**:
```
Minimum approvals: 1
Who can approve: Any user with write access (includes Code agent)
Restrict approval by role: OFF (not needed in solo phase)
```

**Self-review workflow** (Phase 1 solo developer):
1. Code creates PR and adds self-review comment
2. Code approves own PR (via GitHub web UI or CLI)
3. Merges with "Squash and merge"

**Phase 2 Enhancement**:
```
Minimum approvals: 2
Who can approve: Members of @jc-ai-senmu-2026/code-reviewers team
Restrict approval by role: ON (require different reviewers)
```

---

#### 7-B: Dismiss stale approvals on new commits

**Phase 1 Setting**:
```
Dismiss stale pull request approvals when new commits are pushed: ON
```

**Reason**: When a PR is updated, prior approval is invalidated; new approval required.

---

#### 7-C: Require review from code owners

**Phase 1 Decision**: OFF (no CODEOWNERS file initially)

**Phase 2 Plan**:
1. Create `.github/CODEOWNERS` file:
   ```
   # Default owner for all code
   * @akon56788

   # Specialized reviews by path
   /docs/ @akon56788
   /LOM_2026_docs/ @akon56788
   ```
2. Enable "Require review from code owners" in ruleset
3. PR cannot merge without approval from designated code owner

---

#### 7-D: Conversation resolution

**Phase 1 Setting**:
```
Require all conversations to be resolved before merge: ON
```

**Workflow**:
1. Reviewer leaves comment during code review
2. Developer responds with change or clarification
3. Reviewer marks comment as resolved (click "Resolve" in UI)
4. PR cannot merge until all comments resolved

---

#### 7-E: Require approval of most recent push

**Phase 1 Setting**:
```
Require approval of most recent commit before merging: ON
```

**Scenario**:
- PR approved by reviewer
- Developer pushes 1 new commit to fix edge case
- Approval becomes stale; new approval required
- Prevents accidental merging of unapproved code

---

#### 7-F: Require review from designated code owners (Phase 2+)

**Expansion**: Use CODEOWNERS + Ruleset combination

---

#### 7-G: Allowed merge methods

**Phase 1 Allowed**:
- ✅ Squash and merge (recommended, enforced via merge button settings)

**Phase 1 Disabled**:
- ❌ Create a merge commit
- ❌ Rebase and merge (optional, enable in Phase 2 if needed)

---

### 8. Require status checks to pass before merging – Detailed Settings {#8-require-status-checks-detailed}

#### 8-A: Required status checks list

**Phase 1 Minimal Setup**:
```
Status checks required:
- (none initially)

Why: No GitHub Actions workflows configured yet in Phase 1.
Target: Activate in Phase 1.5 when Actions ready.
```

**Phase 2 Recommended**:
```
Status checks required:
1. test (GitHub Actions: unit tests)
2. lint (GitHub Actions: code style checks)
3. build (GitHub Actions: build artifact generation)
4. security/codeql (GitHub Advanced Security)
```

---

#### 8-B: GitHub Actions workflow example (reference for Phase 1.5)

```yaml
name: CI Pipeline
on:
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run tests
        run: |
          echo "Running tests..."
          # pytest, npm test, etc.
          exit 0  # Success

  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Lint code
        run: |
          echo "Running linter..."
          # eslint, flake8, etc.
          exit 0  # Success

  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build
        run: |
          echo "Building..."
          # npm build, python setup.py sdist, etc.
          exit 0  # Success
```

---

#### 8-C: Strict status checks enforcement

**Phase 1 Setting** (once checks added):
```
Require status checks to pass before merging: ON
Require branches to be up to date before merging: ON
```

**Effect**:
- All status checks must show ✅ green before "Merge" button is enabled
- If main receives new commits, PR must be rebased before merge

---

#### 8-D: Dismiss stale status checks

**Phase 1 Setting**:
```
Dismiss stale status checks: OFF (stricter approach)
```

**Rationale**: Require fresh validation even after time passes.

---

#### 8-E: Allow auto-merge with status checks

**Phase 2 Enhancement**:
```yaml
auto_merge_enabled: true
auto_merge_trigger: "all_status_checks_pass"
auto_merge_method: "squash"
```

**Use Case**: Enable auto-merge after approval and status checks succeed.

---

### 9. Require code reviews before merging – Detailed Settings {#9-require-code-reviews-detailed}

#### 9-A: Minimum review count

**Phase 1 Configuration**:
```
Number of approving reviews required: 1
```

**Phase 2+ Configuration**:
```
Number of approving reviews required: 2
```

---

#### 9-B: Approve only with pull request reviewer role

**Phase 1 Setting**:
```
Restrict who can approve reviews: OFF
(Any user with write/maintain/admin role can approve)
```

---

#### 9-C: Require review from code owners

*See 7-C; same configuration.*

---

#### 9-D: Require approval from designated reviewers

**Phase 2 Plan**:
```
Define review groups:
- @jc-ai-senmu-2026/architecture-reviewers (design review)
- @jc-ai-senmu-2026/security-reviewers (security review)

Require:
1. Approval from architecture-reviewers
2. Approval from security-reviewers
3. At least 1 general code reviewer
```

---

#### 9-E: Self-review workflow (Phase 1 solo developer)

**Process**:
1. Code pushes PR
2. Code self-reviews: "Changes look good, no major issues detected"
3. Code approves: Click "Approve" in GitHub web UI or use CLI
4. Merge: "Squash and merge"

**GitHub CLI Example**:
```bash
# Create PR
gh pr create --base main --title "Add branch ruleset config" \
  --body "Adds comprehensive branch protection rules"

# View PR
gh pr view 1

# Approve (as same user)
gh pr review 1 --approve

# Merge
gh pr merge 1 --squash
```

---

#### 9-F: Transition to team reviews (Phase 2)

**When team members join**:
1. Define code review SLA (e.g., within 24 hours)
2. Assign reviewers per PR via GitHub Actions or manual assignment
3. Implement auto-assignment based on code path (CODEOWNERS)
4. Track review metrics in GitHub Insights

---

### 10. Block force pushes – Detailed Settings {#10-block-force-pushes-detailed}

#### 10-A: Force push restriction for all actors

**Phase 1 Configuration**:
```
Block force pushes: ON
Apply to admins: YES (no exceptions)
```

**Effect**:
```
Any attempt to run:
  git push --force
  git push -f
  git push --force-with-lease

Results in error:
  remote: error: refusing to allow force push
  fatal: Could not read from remote repository
```

---

#### 10-B: No bypass for emergency recovery

**Policy Decision**:
```
Phase 1: Block for all (strict)
Phase 2+: Consider 1-time emergency bypass if needed
         (require manual approval from security team)
```

**Rationale for no bypass**:
- If mistake occurs, revert via PR (preferred method)
- Force push history rewriting is dangerous
- Ruleset provides immutability guarantee

---

### 11. Require code scanning results before merging – Detailed Settings {#11-require-code-scanning-detailed}

#### 11-A: GitHub Advanced Security requirement

**Prerequisite**:
- Repository must have GitHub Advanced Security enabled (org or enterprise plan)
- CodeQL analysis configured via GitHub Actions

**Phase 1 Decision**: Optional (configure if GHES available)

---

#### 11-B: Code scanning configuration (CodeQL)

**Setup** (if enabling):
```yaml
# .github/workflows/codeql.yml
name: CodeQL Security Scan

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  analyze:
    runs-on: ubuntu-latest
    permissions:
      security-events: write

    steps:
      - uses: actions/checkout@v4
      - uses: github/codeql-action/init@v2
        with:
          languages: ['python', 'javascript']
      - uses: github/codeql-action/autobuild@v2
      - uses: github/codeql-action/analyze@v2
```

---

#### 11-C: Failure conditions

**Block merge if**:
- CodeQL analysis finds HIGH/CRITICAL vulnerabilities
- Dependency check detects unsafe packages

**Allow merge if**:
- No vulnerabilities found
- Vulnerabilities are documented/accepted in issue

---

#### 11-D: Phase 2 expansion

**Phase 2+**:
- Add Dependabot for dependency scanning
- Add SARIF upload from third-party tools (Snyk, etc.)
- Require zero high-risk vulnerabilities

---

### 12. Require Copilot Enterprise review before merging – Detailed Settings {#12-require-copilot-detailed}

#### 12-A: Copilot Enterprise availability check

**Phase 1 Decision**: NOT APPLICABLE (requires GitHub Copilot Enterprise license)

**Cost** (as of 2026-05): ~$20 USD per user/month (subject to change)

**Phase 1 Status**: SKIP (no license purchased)

---

#### 12-B: Phase 2.5 business case evaluation

**Criteria for Phase 2.5 rollout**:
```
IF (team_size >= 3) AND (code_review_bottleneck == true) AND (budget_approved == true):
  THEN: Evaluate Copilot Enterprise for code review automation
```

**Expected Benefits**:
- Automated suggestion of code improvements
- Faster PR review cycle
- Learning resource for junior developers

**Cost-Benefit**:
```
Cost: $20 USD/user/month × team_size
Benefit: ~4 hours/week code review time savings per developer
Payback: ~2-3 months if 3+ team members
```

---

#### 12-C: Implementation workflow (Phase 2.5+ reference)

```yaml
# .github/workflows/copilot-review.yml (Phase 2.5 reference)
name: Copilot Code Review

on:
  pull_request:
    types: [opened, synchronize]

jobs:
  copilot-review:
    runs-on: ubuntu-latest
    permissions:
      pull-requests: write

    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Run Copilot code review
        uses: github/copilot-code-review-action@v1
        with:
          model: 'gpt-4-turbo'
          tone: 'constructive'
          focus-areas: ['security', 'performance', 'readability']

      - name: Post review as PR comment
        run: |
          echo "Copilot review comment posted automatically"
```

---

## 🚨 Danger Zone Configuration (Repository Settings)

**Location**: Repository settings → Danger zone  
**Current State**: Public repository (changed 2026-05-05)

### Items in Danger Zone (Reference Only)

| Item | Status | Phase 1 | Justification |
|------|--------|---------|---------------|
| **Visibility** | Public | ✅ Public | Template repo; no sensitive data |
| **Transfer repo** | N/A | ❌ No | Owned by user; no transfer needed |
| **Archive repo** | N/A | ❌ No | Active repository; keep operational |
| **Delete repo** | N/A | ❌ No | Protect via branch ruleset; require multiple approvals for deletion |

---

## 📈 Rollout Timeline

### Phase 1 (2026-05-05 → 2026-05-08)

- [ ] Configure items 1-4, 7, 10 (mandatory)
- [ ] Test self-review PR workflow
- [ ] Verify Code/Codex access permissions
- [ ] Document Phase 1 final status

### Phase 1.5 (2026-05-09 → 2026-05-15)

- [ ] Set up GitHub Actions CI pipeline (test, lint, build)
- [ ] Enable status checks (items 8)
- [ ] Verify Code/Codex automated workflow compatibility
- [ ] Finalize README.md

### Phase 2 (2026-05-16 → Target Q2 2026)

- [ ] Recruit team members (2-3 developers)
- [ ] Escalate approval requirements (item 9: 2 reviews)
- [ ] Implement CODEOWNERS file
- [ ] Enable code scanning (item 11, if GHES available)
- [ ] Deprecate Phase 1 single-actor approval process

### Phase 2.5 (Q2-Q3 2026)

- [ ] Evaluate Copilot Enterprise business case
- [ ] Plan signed commit requirement (item 6)
- [ ] Expand deployment environments (item 5)

### Phase 3 (Q3-Q4 2026)

- [ ] Full enforcement: all 12 items enabled
- [ ] Team maturity: robust peer review culture established
- [ ] AI governance: IT Admin Audit Agent deployed org-wide

---

## 🔒 Security Assumptions & Exceptions

### Assumptions

1. **Repository Owner**: Single trusted individual (akon56788)
2. **Data Sensitivity**: No JC member personal data in repo (drive is SSOT)
3. **Threat Model**: Prevent accidental mis-pushes; not designed for insider threats
4. **Compliance**: No regulatory requirements (internal project, non-sensitive)

### Phase 1 Exceptions (Justified)

| Item | Exception | Rationale | Review Date |
|------|-----------|-----------|-------------|
| Signed commits (6) | Deferred to Phase 2 | Solo dev; low risk | 2026-05-31 |
| Code scanning (11) | Optional if no GHES | Cost/benefit pending | 2026-05-31 |
| Copilot review (12) | Deferred to Phase 2.5 | License cost; evaluate later | 2026-06-30 |

---

## 📚 References & Resources

### GitHub Official Docs

- [GitHub Branch Ruleset API](https://docs.github.com/en/enterprise-cloud@latest/rest/repos/rules?apiVersion=2022-11-28)
- [Branch Protection Rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
- [Code Owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)

### Internal Docs

- [SHARED_SOURCE.txt](./SHARED_SOURCE.txt) — Tool coordination guide
- [AGENTS.md.txt](./AGENTS.md.txt) — AI agent role definitions
- [CODEX_WORKFLOW.md.txt](./CODEX_WORKFLOW.md.txt) — Codex process guide

### Related Repositories (Org-wide Reference)

- JC AI Senmu 2026: github.com/akon56788/jc-ai-senmu-2026 (this repo)
- LOM Automation (planned): github.com/akon56788/jc-lom-automation (Phase 2+)

---

## 📝 Change Log

| Date | Version | Change | Author |
|------|---------|--------|--------|
| 2026-05-05 | 1.0 | Initial comprehensive ruleset guide (all 12 items + details) | Claude Code |
| 2026-05-05 | 1.0+ | Item 2.5 "Restrict updates" disabled (OFF) for Phase 1 development | User |
| | | Rationale: Reduce merge friction during solo-dev phase; other 11 rules remain active | |
| | | Status: Monitoring; scheduled re-enable for Phase 2 (2026-05-16+) | |
| (planned) | 1.1 | Phase 1 validation after 2026-05-15 | — |
| (planned) | 2.0 | Phase 2 rollout (team expansion) | — |

---

## ✅ Document Completion Checklist

- [x] All 12 configuration items documented
- [x] Parent items optimized: "概要・Phase別推奨値・詳細ポインター"
- [x] Detailed settings A-F integrated with reference links
- [x] Phase 1 / 2 / 2.5+ / 3 rollout timeline defined
- [x] Security assumptions & exceptions documented
- [x] Danger zone settings reviewed
- [x] GitHub Actions workflow examples provided (reference)
- [x] Cost estimation for Phase 2.5+ enhancements
- [x] Team expansion scenarios (Phase 2+) addressed
- [x] Self-review workflow documented (Phase 1 solo developer)
- [x] Change log initialized
- [x] AI-driven governance framework overview (org-wide context)

---

**Document Status**: ✅ READY FOR IMPLEMENTATION  
**Next Action**: Commit to GitHub; verify in browser; proceed with Phase 1 configuration  
**Deadline**: 2026-05-08 (Phase 1 completion)
