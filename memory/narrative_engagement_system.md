---
name: 次セッション引き継ぎ - ナラティブSSoT化&エンゲージメント・システム
description: GitHub Issue #21「ナラティブ統合&エンゲージメント・システム」の Part1（Git管理）& Part2（テンプレート化）実装の準備完了
type: project
---

## 🚀 次セッションのタスク（GitHub Issue #21）

**Issue**: [ナラティブ統合&エンゲージメント・システム](https://github.com/akon56788/jc-ai-senmu-2026/issues/21)

**Why**: 近藤さんのエンゲージメント・活力を高めるために、タスク説明時に「意味・効果」を示唆できるシステムが必要。そのために、ナラティブ（キャリア・価値観）をSSoT化してから、テンプレート化する。

---

## 📦 引き継ぎ内容

### 完成物
✅ ナラティブファイル v1.16 統合版
- 場所: `C:\Users\User\Downloads\kondo_narrative_v_1_16_integrated.md`
- 内容: 近藤さんの幼少期～現在のキャリア・価値観・動機の整理

### 決定事項
- **目的**: 近藤さんのエンゲージメント・活力を高める「UX システム」を構築
- **対象**: PMO・LLM が「タスクの意味・効果」を示唆できるようにする

---

## 🎯 Part 1: ナラティブファイルの Git コミット + SSoT 登録

**やること**:
1. リポジトリをGit初期化（既に GitHub 連携済み）
2. ナラティブファイルをリポジトリ内の適切なフォルダに配置
3. Git コミット（ブランチ・メッセージはこのセッションで決定）
4. memory/MEMORY.md に登録

**次セッションで決めること**:
- [ ] コミット先ブランチ（main? develop?）
- [ ] フォルダ構造（`/docs/narrative/` ? `/memory/` 配下?）
- [ ] SSoT の扱い（Notion との連携方法）

---

## 🎯 Part 2: コア・ロール抽象化 → テンプレート化 → PMO/LLM ガイド作成

**やること**:

### Step 1: コア・ロール抽象化
ナラティブから「近藤さんの本質的なロール」を3～5個抽出・整理

**例**（調整予定）:
- 「複雑な情報を整理して、意思決定を支える」
- 「道具・仕組みを設計して、人や組織の可能性を広げる」
- 「見えない構造を可視化して、つながりを作る」

### Step 2: テンプレート化（抽象度高く）

```
【タスク】XXX
【効果】この作業が生む具体的な効果・意味
【あなたの役割】あなたのコア価値観/ロールがどう発揮されるか
【チーム/組織への影響】これが波及する範囲
```

⚠️ **重要**: 具体例（小学3年の決算報告書など）は実装層で補足する。テンプレートは抽象度を高く保つ。

### Step 3: PMO 向けガイド作成
- タスク割り当て時の使用方法
- 「意味」「効果」をどう伝えるか
- 実装例

### Step 4: LLM 向けシステムプロンプト作成
- Claude・ChatGPT が同じテンプレートで説明するプロンプト
- 「近藤さんのコア・ロール」をプロンプトに埋め込む

---

## 📋 成果物

| 成果物 | 場所 | 説明 |
|--------|------|------|
| ナラティブファイル（Git管理） | `jc-ai-senmu-2026/docs/narrative/` など | SSoT 化 |
| コア・ロール定義 | `memory/kondo_core_roles.md` | 抽象化済み |
| タスク説明テンプレート | `docs/pmo_engagement_template.md` | PMO用 |
| PMO ガイド | `docs/pmo_engagement_guide.md` | 実装マニュアル |
| LLM システムプロンプト | リポジトリまたは設定ファイル | Claude・ChatGPT用 |

---

## 🔗 関連リンク

- **GitHub Issue #21**: https://github.com/akon56788/jc-ai-senmu-2026/issues/21
- **Narrative file**: `C:\Users\User\Downloads\kondo_narrative_v_1_16_integrated.md`
- **CLAUDE.md**: 種別3（環境開発・改善系）の定義確認

---

## ⚡ 優先度

🟢 ベストエフォート（環境開発系）
- 期限なし
- 実装後は PMO・LLM の運用精度が向上

---

## 💡 実装時の心構え

- 近藤さんの「ナラティブ」を深く読み込む
- コア・ロールの抽象度は「複数の場面に応用できるレベル」を目指す
- テンプレートは「汎用的」に、実装例は「具体的」に
- 完成後、実際に 1 タスクで試運用してみる

---

## ✅ 2026-05-08 実装完了

### Part 1: ナラティブファイル管理
- ✅ Git 初期化・リモート追加（origin: GitHub jc-ai-senmu-2026）
- ✅ ブランチ決定: main
- ✅ フォルダ構造: `docs/narrative/`
- ✅ コミット: ebeaa7f「feat: add narrative file v1.16 as SSoT for engagement system」

**SSoT 登録**: 
- **GitHub（正本）**: `docs/narrative/kondo_narrative.md` (commit: ebeaa7f)
- **Google Drive（ミラー）**: ID `1LsrD7u-Jd5Py1Qv2d3FkWe1oeUoFVwd-xhYaCM4y6TU`
  - Folder: 専務理事対応（AI活用）/kondo_narrative_v1.16.md
  - Purpose: 全ツール（Code・Codex・Cowork）アクセス
  - 配置日: 2026-05-08
- Memory: `memory/narrative_engagement_system.md`
- Notion 連携: 次フェーズで検討（現在は GitHub を正本）

### Part 2: エンゲージメント・システム構築完了
#### 成果物
1. **docs/kondo_core_roles.md**: 5つのコア・ロール定義
   - Role 1: 複雑な情報・構造を整理して、意思決定を支える
   - Role 2: 道具・仕組みを設計して、人や組織の体験・可能性を広げる
   - Role 3: 見えない構造をつなぎ、複数視点から全体を推進する
   - Role 4: 試行錯誤の中で、小さな成功体験を積んで前に進む
   - Role 5: 自分の要素を残しながら、周囲を支援・賦能するヒーローを目指す

2. **docs/pmo_engagement_template.md**: PMO向けタスク説明テンプレート
   - テンプレート構造: 【Task】【Effect】【Your Role】【Team Impact】
   - 3つの実装例（情報整理系、チーム連携系、試行錯誤系）
   - 運用フロー・効果測定指標

3. **docs/llm_engagement_systemprompt.md**: LLM向けシステムプロンプト
   - Claude・ChatGPT が同じテンプレートで説明するプロンプト
   - トーン・態度ガイドライン
   - 実装例・測定指標

#### コミット
- Commit: c5fd5d2「feat: add engagement system - Part 2 (core roles & templates)」

### 実運用準備
- [ ] 1タスクで試運用テスト（5月中に実施予定）
- [ ] フィードバック基づく改善
- [ ] PMO/LLM チームへのガイド共有

**ステータス**: 🚀 実装完了 → 実運用開始準備中
