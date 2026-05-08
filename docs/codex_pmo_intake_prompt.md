# Codex PMO 連絡受け取り・処理プロンプト

**用途**: Code からの指示受け取り → 自動読み取り・テンプレート埋め → PMO 報告  
**対象**: Codex セッション（当セッション・別セッション両対応）  
**更新日**: 2026-05-08

---

## 🎯 Codex 実行プロンプト（テンプレート）

Code からこのような指示を受けたとき：

```
「Issue #XX の修正が完了しました。
docs/pmo_lowops_notification_template.md のパターン A を使って
PMO に簡潔に連絡してください（3-5行）」
```

**Codex は以下のプロンプトに従って自動処理**:

---

## 📋 Codex 処理プロンプト（コピペ用）

```
【指示分析】
Code からの指示内容を解析：
- [ ] Issue 番号特定: Issue #XX
- [ ] パターン特定: A（完了確認待ち）/ B（リスク）/ C（進捗）/ D（レビュー）
- [ ] 実行アクション: PMO に [パターン] で報告

【コンテキスト自動取得】
GitHub から以下を自動取得：
1. [ ] Issue #XX のコメント欄 → 修正内容の詳細確認
2. [ ] 最新 Commit メッセージ → What changed の記載内容
3. [ ] 関連ファイル差分 → 修正箇所を 3 行以内に要約
4. [ ] 現在の Status → ✅完了 / 🚀進行中 / ⏳保留中 / ⚠️確認待ち

【テンプレート埋め込み】
docs/pmo_lowops_notification_template.md から パターン A テンプレートを使用：

```markdown
## 🔔 Codex PMO: [Issue短名] [ステータス]
**Status**: ✅ [修正内容・コミット] (commit: [ハッシュ])
**What changed**:
- [ファイル名]: [修正内容・1行] ✅
- [ファイル名]: [修正内容・1行] ✅
**Waiting for**: Your re-verification on Issue #XX
**Next**: Issue #XX close → Issue #YY launch
---
_Low-ops verification request. See Issue #XX for full details._
```

【投稿先判定】
- [ ] 指示がスレッド内 → Chat スレッド にコメント
- [ ] 指示が Issue コメント → 同一 Issue にコメント追加
- [ ] 指示が DM/直接 → GitHub Issue #XX のコメント欄に投稿

【実行内容確認】
投稿前に以下を確認：
- [ ] テンプレート形式は正しいか（見出し・太字・改行）
- [ ] 修正内容は 3 行以内か
- [ ] Issue 番号は正確か
- [ ] Commit ハッシュは取得済みか（GitHub から確認）
- [ ] Next フェーズは正確か（関連 Issue と連携）

【投稿 & 報告】
1. GitHub Issue #XX のコメント / Chat スレッド に投稿
2. Code へ 「PMO 連絡完了」と簡潔に報告
   例：「✅ Issue #XX 検証依頼を PMO に投稿しました」

【PMO受信返信】
Codex PMOとして受信・検証した結果は、必ず以下を分けて返す：
- 受信結果: トリガー・Issue・文脈を認識できたか
- 実行結果: 何を確認・実行し、何が分かったか
- Close判定: 対象Issueを閉じてよいか、追加対応が必要か

返信テンプレートは `docs/pmo_lowops_notification_template.md` の
「Codex PMO 受信返信テンプレート」を使用する。
```

---

## 🔄 実行フロー図

```
Code
  ↓
「Issue #XX 修正完了。パターン A で報告してください」
  ↓
Codex（このプロンプト実行）
  ├─ Issue #XX の詳細を GitHub から自動取得
  ├─ Commit メッセージ・差分から "What changed" を要約
  ├─ テンプレートを自動埋め込み
  └─ GitHub Issue / Chat に投稿
  ↓
PMO（連絡を受け取り）
  ├─ 受信結果を分離して記録
  ├─ 実行結果を分離して記録
  └─ Close判定を分離して返答
```

---

## 💾 別セッション対応（重要）

Code がいない別セッション（Codex だけの場合）：

1. **GitHub Issue で指示を検出**:
   ```
   # 上記スレッドで Code がこう言っていた：
   「Issue #XX 修正完了。パターン A で報告してください」
   ```

2. **Codex がこのプロンプトで自動処理**:
   - GitHub Issue #XX を検索 & 開く
   - 最新 Commit / 差分 から "What changed" 取得
   - テンプレート埋め込み
   - Issue / Chat に投稿

3. **Code へ報告**（戻し先明確）:
   ```
   「Code へ: Issue #XX の PMO 連絡を完了しました。
   投稿先: https://github.com/akon56788/jc-ai-senmu-2026/issues/XX#commentXXX」
   ```

---

## 🛠️ 実装チェックリスト（Codex セッション開始時）

セッション開始時に以下を確認：

```markdown
## Codex PMO Intake Ready ✅

**確認項目:**
- [ ] GitHub API 権限確認（Issues / Commits 読取可）
- [ ] docs/pmo_lowops_notification_template.md にアクセス可
- [ ] Code からの指示を受け取り待機中

**待機中の指示:**
- [ ] Issue #XX: [指示内容] ← あればここに記載

**処理済み:**
- [ ] Issue #YY: パターン A 投稿済み (2026-05-08 14:30)
```

---

## 📝 パターン別の処理詳細

### パターン A: 修正完了 → 確認待ち

```
Code 指示:
「Issue #21 修正完了。パターン A で報告してください」

Codex 処理:
1. Issue #21 から最新コメント / Commit メッセージ取得
2. What changed を修正内容から抽出（3行以内）
3. Issue #21 のコメント欄に「## 🔔 Codex PMO: Issue #21 Verification Ready」投稿
4. PMO受信返信テンプレートで以下を分けて記録
   - 受信結果
   - 実行結果
   - Close判定
5. Code へ報告: 「✅ Issue #21 検証依頼を投稿しました」
```

### パターン B: リスク検出 → 対応依頼

```
Code 指示:
「SSOT 差分を検出。パターン B で Code と Cowork にリスク報告してください」

Codex 処理:
1. リスク詳細から「What」「Root Cause」を抽出
2. 「Action needed」に対応内容を記載
3. GitHub Issue / Chat に投稿
4. Code・Cowork 両者へ通知
```

### パターン C: 進捗報告（日次/週次）

```
Code 指示:
「週次進捗を整理しました。パターン C で報告してください」

Codex 処理:
1. Code が整理した内容から「Completed」「In Progress」「Blockers」を抽出
2. テンプレートに埋め込み
3. Notion / Chat スレッドに定期投稿
4. 次回報告日を記載
```

---

## 🚨 エラーハンドリング

Codex が以下に遭遇した場合の対応：

| 状況 | 対応 |
|------|------|
| **GitHub API エラー（Issue 取得失敗）** | Code に報告、Issue URL を手動指定依頼 |
| **指示が不明確（パターン未指定など）** | Code に確認「Issue #XX、パターン A でいいですか？」 |
| **コミットハッシュが見つからない** | "commit: [pending]" と記載して投稿、後で更新 |
| **テンプレートが見つからない** | GitHub から直接ファイル内容取得 or Code に教示依頼 |

---

## 📊 メトリクス（定期確認）

毎日/毎週末に記録：

```markdown
## Codex PMO Intake Metrics

**処理実績**:
- パターン A 処理数: XX 件
- パターン B 処理数: XX 件
- パターン C 処理数: XX 件

**平均処理時間**:
- 指示受け取り → 投稿完了: X 分

**エラー発生**:
- 0 件 / 1 件 / etc.

**PMO受信判定**:
- Received: ✅ X 件 / ⚠️ X 件 / ❌ X 件
- Context extraction: ✅ X 件 / ⚠️ X 件 / ❌ X 件
- Action result: ✅ X 件 / ⚠️ X 件 / ❌ X 件
- Close judgment: Close可能 X 件 / 軽微修正後 X 件 / 追加修正必要 X 件
- Side effect: なし X 件 / あり・復旧済み X 件 / あり・未復旧 X 件

**改善提案**:
- [ ] なし
- [ ] あり: [具体内容]
```

---

## 🔗 関連ファイル

- **送り手**: `docs/pmo_lowops_notification_template.md` (パターン定義)
- **受け手**: このファイル（処理プロンプト）
- **参考**: `docs/CONTEXT_FOR_CODEX.md` (Codex ロール定義)

---

**Last Updated**: 2026-05-08  
**Owner**: Codex PMO  
**Related**: Issue #21, Code → Codex 連携, PMO 低運用通信
