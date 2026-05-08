# Codex PMO 超低運用連絡テンプレート

**用途**: Code → Codex PMO への自動簡潔連絡  
**更新日**: 2026-05-08  
**運用**: 毎セッション発生時 / 重要イベント時

---

## 📋 テンプレート（基本形）

```markdown
## 🔔 Codex PMO: [Issue短名] [ステータス]

**Status**: [✅完了 / 🚀進行中 / ⚠️確認待ち]

**What changed**:
- [ファイル/設定]: [変更内容] ✅
- [ファイル/設定]: [変更内容] ✅

**Waiting for**: [次のアクション（PMO確認待ちなら明記）]

**Next**: [次フェーズ / 関連Issue]

---
_[簡潔な文脈説明]. See [関連Issue] for full details._
```

---

## 🎯 運用パターン別テンプレート

### パターン A: 修正完了 → 確認待ち（最頻出）

```markdown
## 🔔 Codex PMO: Issue #XX Verification Ready

**Status**: ✅ [修正内容] complete (commit: [ハッシュ])

**What changed**:
- [ファイル]: [修正内容] ✅
- [ファイル]: [修正内容] ✅

**Waiting for**: Your re-verification on Issue #XX

**Next**: Issue #XX close → Issue #YY launch

---
_Low-ops verification request. See Issue #XX for full details._
```

**使用例**: Issue #21完了 → Codex PMO確認待ち

---

### パターン B: リスク検出 → 対応依頼

```markdown
## 🔔 Codex PMO: Issue #XX [リスク種別]

**Status**: ⚠️ [リスク概要]

**Risk**: [具体的な問題]
- [原因1]
- [原因2]

**Action needed**: [対応内容]

**Owner**: [Code / Cowork / 両者]

---
_Risk alert: [簡潔な説明]. See Issue #XX for analysis._
```

**使用例**: SSOT差分検出 → Code/Cowork対応依頼

---

### パターン C: 進捗報告（日次/週次）

```markdown
## 📊 Codex PMO: [週次/日次] Status Report

**Completed**:
- [タスク] ✅
- [タスク] ✅

**In Progress**:
- [タスク] 🚀
- [タスク] 🚀

**Blockers**: [あれば記述]

---
_Routine status. Next update: [予定日]._
```

**使用例**: Phase進捗 → 定期報告

---

### パターン D: 外部レビュー結果

```markdown
## 🔍 Codex PMO: External Review Complete

**Target**: [Issue / File]

**Reviewer**: [ChatGPT / Gemini]

**Result**: [Blocker / Risk / Suggestion / No issue]

**Follow-up**: [必要なアクション]

---
_Review complete. See [Issue] for details._
```

**使用例**: GitHub Actions設計レビュー完了

---

## 📥 Codex PMO 受信返信テンプレート

Code / Cowork / Chat からの低運用連絡を受けた Codex PMO は、以下の3要素を分けて返信する。

1. **受信結果**: トリガー・Issue・文脈を認識できたか
2. **実行結果**: 実際に何を確認・実行し、何が分かったか
3. **Close判定**: 対象Issueを閉じてよいか、追加対応が必要か

### 標準版（検証・Close判断あり）

```markdown
## Codex PMO Intake Result

**Received**: ✅ / ⚠️ / ❌
**Pattern**: A / B / C / D / Unknown
**Issue**: #XX
**Context extraction**: ✅ / ⚠️ / ❌

### 1. 受信結果

- Trigger recognized: ✅ / ⚠️ / ❌
- Extracted issue: #XX
- Extracted status: [完了 / 進行中 / 確認待ち / リスク]
- Extracted commits: [commit ids]
- Extracted files: [files]

### 2. 実行結果

- Action taken: [Issueコメント / Drive確認 / スクリプト実行 / Git確認 / 保留]
- Verification result: ✅ / ⚠️ / ❌
- Findings:
  - [確認できたこと]
  - [残ったこと]
  - [副作用があれば記載]

### 3. Close判定

**Close judgment**: ✅ Close可能 / ⚠️ 軽微修正後 / ❌ 追加修正必要

**Reason**:
- [理由1]
- [理由2]

**Next action**:
- [Code / Codex / Cowork / User の次アクション]

### 4. PoCメトリクス

- Trigger recognition: ✅ / ⚠️ / ❌
- Context extraction: ✅ / ⚠️ / ❌
- Processing time: [分]
- Human intervention: [なし / あり: 内容]
- Side effect: [なし / あり: 内容]
```

### 超短縮版（受付・進捗報告向け）

```markdown
## Codex PMO Intake Result

**Received**: ✅
**Pattern**: A / B / C / D
**Issue**: #XX
**Context extraction**: ✅

**Action taken**: [実施内容]
**Result**: ✅ / ⚠️ / ❌

**Close judgment**: ✅ Close可能 / ⚠️ 軽微修正後 / ❌ 追加修正必要
**Next**: [次アクション]

_PoC: trigger ✅ / extraction ✅ / side effect [なし/あり]_
```

### 使用例: Pattern A 受信後のPMO返信

```markdown
## Codex PMO Intake Result

**Received**: ✅
**Pattern**: A
**Issue**: #21
**Context extraction**: ✅

**Action taken**: Issue #23 / #27 にPMO報告、Drive MANIFESTとスクリプト挙動を確認
**Result**: ⚠️ 冪等性チェックが期待通り skip せず、MANIFEST重複が一時発生。重複はPMO側で復旧済み。

**Close judgment**: ⚠️ 軽微修正後
**Next**: `scripts/update_manifest.py` のskip判定修正後、再実行で `status: skipped` を確認

_PoC: trigger ✅ / extraction ✅ / side effect あり・復旧済み_
```

---

## 🛠️ Code からの使用方法

### 短期運用（このセッション・連続セッション）

1. **修正完了時**: パターン A を使用
   ```
   Codex PMOへ "Issue #XX Verification Ready" 連絡
   → GitHub Issue #XX にコメント
   → または Chat スレッド
   ```

2. **リスク検出時**: パターン B を使用
   ```
   Codex PMOへ リスク詳細 + 対応依頼
   → GitHub Issue に urgency フラグ
   ```

3. **進捗報告**: パターン C を使用
   ```
   毎朝 / 毎週末 定期報告
   → Notion / Chat スレッド
   ```

---

### 長期運用（1ヶ月以上継続）

1. **テンプレート配置**:
   - このファイル: `docs/pmo_lowops_notification_template.md`
   - Memory: `memory/pmo_notification_patterns.md`

2. **定期的な見直し**:
   - 月1回、使用実績から効率性検証
   - 新しいパターンを追加 / 不要なパターンを削除

3. **自動化検討**:
   - GitHub Actions による定期報告自動化
   - Notion API による status update 自動化

---

## 📝 プロンプト例（Code→Codex指示用）

### 短期：当セッション内で Codex に簡潔連絡を指示

```
Codex さんへ：

以下の形式で Codex PMO (自分) に Issue #21 完了を連絡してください。

テンプレート：
## 🔔 Codex PMO: Issue #21 Verification Ready
**Status**: ✅ Soft modifications complete (commit: e3a2ace)
**What changed**:
- IMPLEMENTATION_SUMMARY.md: MANIFEST ID canonical ✅
- scripts/update_manifest.py: Idempotency check added ✅
**Waiting for**: Your re-verification on Issue #23
**Next**: Issue #21 close → Issue #22 Pre-Release launch (May 8-15)

形式はシンプルに、要点だけ。GitHub Issue #23 のコメントまたは Chat スレッドに投稿でOK。
```

---

### 長期：継続的な低運用連絡スタイル

```
Codex PMO ロール定義への追加：

「毎セッション開始時に Code の作業状況を 3 行程度で報告する」

使用テンプレート：
- パターン A（修正完了）
- パターン B（リスク）
- パターン C（進捗）

から、状況に応じて選択して簡潔に報告。

重要：
- 詳細は GitHub Issue / Memory で参照可能にしておく
- 連絡自体は 3-5 行に収める（超低運用）
- リスクだけは即座に（遅延なし）
```

---

## 📊 運用メトリクス（今後計測）

毎週末に以下を確認：
- パターン別使用頻度 (A > B > C > D 想定)
- PMO確認遅延時間（目標: 24時間以内）
- 誤報 / 見落としの発生
- PMO受信結果: Received / Context extraction / Action result / Close judgment
- 検証副作用: なし / あり / 復旧済み / 未復旧
- Close判定の精度: Close可能 / 軽微修正後 / 追加修正必要 の後続結果

---

**Last Updated**: 2026-05-08  
**Owner**: Code (Communication with Codex PMO)  
**Related**: Issue #21, Codex PMO Context, CONTEXT_FOR_CODEX.md
