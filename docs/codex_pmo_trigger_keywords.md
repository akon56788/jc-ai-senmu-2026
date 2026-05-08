# Codex PMO トリガーキーワード辞書

**用途**: Code → Codex への超短縮指示（数文字～十数文字）  
**対象**: Codex セッション（当セッション・別セッション両対応）  
**更新日**: 2026-05-08

---

## 🎯 基本概念

Code が短い一言で指示 → Codex が文脈から自動読み取り → 詳細処理プロンプトへ

**Before（現在）:**
```
「Issue #21 修正完了。パターン A で PMO に連絡してください」(47文字)
```

**After（目指す形）:**
```
「PMOに確認連絡」(8文字)
```

Codex が「PMOに確認連絡」だけで、以下を自動判定：
- [ ] Issue 番号は？ → GitHub / Chat スレッドから自動特定
- [ ] パターンは？ → トリガーキーワードから A を自動認識
- [ ] コンテキストは？ → 最新 Commit / 差分から自動取得
- [ ] 処理は？ → `docs/codex_pmo_intake_prompt.md` へ自動遷移

---

## 📋 トリガーキーワード辞書

### 📤 PMO 連絡系（最頻出）

| トリガー | パターン | 意味 | GitHub 情報自動取得 |
|---------|---------|------|------------------|
| **PMOに確認連絡** | A | 修正完了 → 確認待ち | Issue#・Commit・What changed |
| **PMOに確認** | A | (短形)同上 | 同上 |
| **確認待ち** | A | (略形)同上 | 同上 |
| **検証待ち** | A | 同上（別言葉） | 同上 |

### 🚨 リスク系

| トリガー | パターン | 意味 | GitHub 情報自動取得 |
|---------|---------|------|------------------|
| **PMOにリスク報告** | B | リスク検出 → 対応依頼 | リスク詳細・原因分析 |
| **SSOT差分検出** | B | SSoT 差分 → Code・Cowork 対応 | 差分内容 |
| **リスク報告** | B | (短形)リスク報告 | 同上 |

### 📊 進捗系

| トリガー | パターン | 意味 | GitHub 情報自動取得 |
|---------|---------|------|------------------|
| **進捗報告** | C | 日次/週次進捗 → PMO 報告 | Code の整理内容 |
| **週次報告** | C | 週次進捗報告 | 同上 |
| **日次報告** | C | 日次進捗報告 | 同上 |

### 🔍 レビュー系

| トリガー | パターン | 意味 | GitHub 情報自動取得 |
|---------|---------|------|-----------------|
| **レビュー完了** | D | 外部レビュー → 結果報告 | ChatGPT/Gemini 結果 |
| **外部レビュー報告** | D | 同上（長形） | 同上 |

---

## 🧠 Codex トリガー認識・文脈読み取りプロンプト

Code がトリガーキーワードを送ったとき、Codex はこのプロンプトを実行：

```
【トリガー認識フロー】

1️⃣ Code の指示を受け取る
   例）「PMOに確認連絡」

2️⃣ トリガーキーワード辞書から検索
   - 「PMOに確認連絡」を「PMO連絡系」から検索
   - パターン A → 「修正完了 → 確認待ち」
   - ✅ マッチしました

3️⃣ 指示が来た「文脈」から自動抽出
   現在のスレッド / Issue から以下を特定：
   - [ ] Issue 番号: GitHub Issue コメント or スレッドタイトルから抽出
   - [ ] 関連コミット: GitHub からリポジトリ最新 Commit 取得
   - [ ] 修正ファイル: Commit 差分から自動抽出
   - [ ] Status: Issue ラベル / コメント内容から自動判定

4️⃣ 詳細処理プロンプトへ自動遷移
   → docs/codex_pmo_intake_prompt.md を実行
   
   入力パラメータ自動設定：
   {
     "trigger": "PMOに確認連絡",
     "pattern": "A",
     "issue_number": "[自動抽出]",
     "commit_hash": "[GitHub から取得]",
     "files_changed": "[diff から抽出]",
     "context": "[スレッド or Issue から読み取り]"
   }

5️⃣ 処理実行 & PMO に投稿
   詳細処理プロンプトの結果から自動生成：
   
   ## 🔔 Codex PMO: Issue #XX Verification Ready
   **Status**: ✅ [修正内容] (commit: [ハッシュ])
   **What changed**: [3行以内]
   ...

6️⃣ Code へ報告
   「✅ Issue #XX の PMO 連絡を投稿しました」
```

---

## 💾 トリガー別・処理フロー図

### フロー A: PMOに確認連絡

```
Code
  ↓
「PMOに確認連絡」(8文字)
  ↓
Codex (トリガー認識)
  ├─ 辞書から「パターン A」を検出
  ├─ スレッド / Issue から Issue 番号を自動抽出
  ├─ GitHub から最新 Commit・diff を自動取得
  └─ 詳細処理プロンプトへ
  ↓
Codex (詳細処理)
  ├─ テンプレート自動埋め込み
  └─ GitHub Issue コメント に投稿
  ↓
PMO
  └─ 検証開始
```

### フロー B: PMOにリスク報告

```
Code
  ↓
「SSOT差分検出」 or 「PMOにリスク報告」
  ↓
Codex (トリガー認識)
  ├─ 辞書から「パターン B」を検出
  ├─ リスク詳細を Code スレッド / Issue から抽出
  ├─ 原因分析情報を自動取得
  └─ 詳細処理プロンプトへ
  ↓
Codex (詳細処理)
  ├─ リスク構造化（What・Root Cause・Action needed）
  └─ GitHub Issue / Chat に投稿
  ↓
Code・Cowork
  └─ 対応開始
```

---

## 🔧 実装チェックリスト（Codex セッション開始時）

```markdown
## Codex Trigger Recognition Ready ✅

**確認項目:**
- [ ] このファイル（codex_pmo_trigger_keywords.md）にアクセス可
- [ ] トリガーキーワード辞書を読み込み済み
- [ ] 詳細処理プロンプト（codex_pmo_intake_prompt.md）にアクセス可
- [ ] GitHub API で Issue / Commit 情報を自動取得可

**待機中:**
- Code からのトリガーキーワード受け取り待機

**実行例:**
- トリガー: 「PMOに確認連絡」
  → パターン: A
  → Issue 自動特定: Issue #21
  → GitHub から Commit 自動取得: commit e3a2ace
  → テンプレート自動埋め込み
  → GitHub Issue #21 にコメント投稿
  → Code へ報告: 「✅ Issue #21 検証依頼を投稿しました」
```

---

## 📝 よくある使用パターン

### パターン① 当セッション内（同じ Codex セッション）

```
Code: 「PMOに確認連絡」
  ↓
Codex: スレッド内容から Issue #21 を特定 → 処理実行
```

### パターン② 別セッション（Code が終了して Codex だけの場合）

```
前のセッションで Code が GitHub Issue にコメント：
「@Codex: PMOに確認連絡」

次のセッションで Codex が起動：
  1. GitHub Issue #21 を検索 → Code からのコメントを発見
  2. トリガーキーワード「PMOに確認連絡」を認識
  3. Issue 情報を自動取得 → 処理実行
```

### パターン③ Chat スレッド内（混合環境）

```
Chat スレッド:
Code: 「Issue #21 修正しました」
Code: 「PMOに確認連絡」
  ↓
Codex: 
  1. スレッドから Issue #21 と「PMOに確認連絡」を認識
  2. GitHub から最新 Commit 取得
  3. テンプレート埋め込み & PMO 投稿
```

---

## 🚀 拡張性（将来）

### 複合トリガー

```
「PMOに確認連絡、Codeの対応確認」
→ パターン A + 追加アクション
```

### コンテキスト読み取り拡張

```
「PMOに確認連絡」
→ 複数 Issue 検出時は、スレッド / Issue タイトルから正確に判定
→ リモートリポジトリから即座に Commit 取得（遅延なし）
```

---

## 📊 メトリクス（Codex 側で記録）

毎セッション終了時：

```markdown
## Codex Trigger Metrics: [DATE]

**使用実績:**
- PMO連絡系: X 回
- リスク系: X 回
- 進捗系: X 回
- レビュー系: X 回

**平均処理時間:**
- トリガー受け取り → 投稿完了: X 秒

**エラー:**
- Issue 自動特定失敗: X 回 / 理由: [具体]
- GitHub API エラー: X 回 / 対応: [代替手段]

**改善提案:**
- [ ] なし
- [ ] あり: [具体内容]
```

---

## 🔗 関連ファイル

| ファイル | 役割 |
|---------|------|
| **このファイル** | トリガーキーワード辞書 & 認識プロンプト |
| `docs/pmo_lowops_notification_template.md` | パターン定義・テンプレート本体 |
| `docs/codex_pmo_intake_prompt.md` | 詳細処理プロンプト（トリガー認識後の処理） |
| `docs/CONTEXT_FOR_CODEX.md` | Codex ロール定義・全体コンテキスト |

---

**Last Updated**: 2026-05-08  
**Owner**: Codex (Trigger Recognition & Auto-Processing)  
**Related**: Issue #21, Code-Codex automation, AI-to-AI handoff PoC (Issue #27)
