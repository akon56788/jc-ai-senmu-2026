# Notion PoC 詳細設計書

**バージョン**: v1.1
**最終更新**: 2026-05-06
**用途**: Notion × Google Sheets/Drive 比較検証
**参照者**: Chat（設計相談）、Cowork（Notion 操作）、Code（Notion API 実装）
**ステータス**: 🟢 Master Task DB + Project DB + Committee Project DB 完成、テストデータ登録済み、リレーション設定完了

---

## 🎯 PoC 目的

### 検証項目
1. **GUI 使いやすさ** — Calendar/Board ビュー vs. Sheets の比較
2. **データ一元管理** — Database × 複数ビュー構成の運用性
3. **Claude 連携の容易さ** — Chat/Cowork/Code からの参照・更新効率
4. **組織拡張対応** — 個人利用 → 組織利用への段階的拡張の現実性

### 検証期間
- **期間**: 1～2 ヶ月（2026-05-04 ～ 2026-06-30）
- **判定**: 運用データ蓄積後、「Google 統一」or「Notion 並行」を決定

---

## 🗂️ Notion 構成（ハイブリッド実装）

```
📁 専務理事対応（PoC）
├── 📋 Master Task Database（手動作成）
├── 📋 Project Database（Code 自動生成）
└── 📋 Committee Project Database（Code 自動生成）
```

---

## 📋 Database 1: Master Task Database

**状態**: 手動作成・完成（2026-05-04）
**用途**: 全タスク・プロジェクトの一元管理

### プロパティ設計

| # | プロパティ名 | 型 | 説明 | 例 |
|---|------------|-----|------|-----|
| 1 | Task ID | Text | タスク一意識別子 | T001, P001, T001-1 |
| 2 | Task/Project Name | Title | タスク・プロジェクト名 | LOM 発送（2026年5月） |
| 3 | Type | Select | 業務分類 | 定常 / プロジェクト / 個別 |
| 4 | Category | Select | 主導体制 | 専務(執行部)主導 / 委員会主導 / その他 |
| 5 | Priority | Select | 優先度 | 高 / 中 / 低 |
| 6 | Due Date | Date | 期限 | 2026-05-15 |
| 7 | Status | Select | ステータス | 未実施 / 実行中 / 待ち / 完了 / 延期 |
| 8 | Progress % | Number | 進捗率 | 0～100 |
| 9 | Owner | Person | メイン責任者 | 専務理事 |
| 10 | Sub-Owners | People | サブ担当者 | 複数可（将来の組織利用対応） |
| 11 | Related Project | Relation | 関連プロジェクト | Project DB へのリンク |
| 12 | Parent Task | Relation | 親タスク | Master Task DB（自己参照） |
| 13 | Sub Tasks | Relation | サブタスク一覧 | Master Task DB（自己参照） |
| 14 | Description | Rich Text | 詳細説明 | タスクの背景・要件など |
| 15 | Created | Created time | 作成日時 | 自動 |
| 16 | Last Edited | Last edited time | 更新日時 | 自動 |

### ビュー構成（4つ）
- **View 1: Table** — 全タスク一覧（Due Date 昇順）
- **View 2: Calendar** — Due Date を軸にしたスケジュール可視化
- **View 3: Board** — Status 別 Kanban（未実施 → 実行中 → 待ち → 完了 → 延期）
- **View 4: Parent Tasks のみ** — Filter: Parent Task が空（親タスクのみ）

---

## 📋 Database 2: Project Database

**状態**: Code が Notion API で自動生成・完成（2026-05-04）
**Database ID**: cbf0473bd5c84f8ea7e9ade07fc4251e

### プロパティ設計（11個）
Project Name / Project ID / Category / Start Date / End Date / Status / Progress % / Owner / Related Tasks / Description / Risks-Issues

### ビュー構成（3つ）
- **View 1: Table** — 全プロジェクト一覧
- **View 2: Timeline** — Start Date ～ End Date の Gantt 風表示
- **View 3: Board** — Status 別（計画 / 準備 / 実行 / レビュー / 完了）

---

## 📋 Database 3: Committee Project Database

**状態**: Code が Notion API で自動生成・完成（2026-05-04）
**Database ID**: 62ed1897708549dd9d02419a2c4d8218

### プロパティ設計（6個）
Committee Name / Project（→Project DB リンク）/ Support Items / Next Report Date / Status / Owner

### ビュー構成（2つ）
- **View 1: Table** — Committee Name, Project, Status, Next Report Date
- **View 2: Calendar** — Next Report Date を軸にした委員会報告スケジュール

---

## 🔗 テストデータ（実装完了）

### T001: LOM 発送（2026年5月）
- **Page ID**: 356c80b2-9350-8184-a433-d21be5ee8fbc
- Type: 定常 / Priority: 高 / Status: 実行中 / Progress: 50%

### P001: LOM 発送（過去分棚卸・タスク化）
- **Page ID**: 356c80b2-9350-81c4-8bc8-f9b8ac31f4c9
- Status: 実行 / Progress: 35%
- **P001 ← Related Tasks → T001 リレーション設定完了**

---

## 🔄 Claude 連携方法

### Chat: 進捗確認・分析
Notion DB を参照して待ちタスク一覧・遅延プロジェクト分析を返す

### Cowork: 進捗更新・自動集計
Master Task DB を直接更新。将来的に週次 Slack 通知を自動化

### Code: レポート生成・データ同期
Notion API → Word レポート生成、または Notion → Google Sheets 定期同期

---

## 🗺️ PoC 判定基準（2026-06-30）

- **パターン A: Google 統一** — Notion GUI メリットが限定的 / API 連携が複雑
- **パターン B: Notion 並行運用** — GUI 使いやすさが大きなメリット / API も運用可能
- **パターン C: ハイブリッド** — Notion: Calendar/Board 表示用 / Sheets: 詳細分析用

---

## 📋 更新履歴

| バージョン | 日付 | 変更内容 | 担当 |
|-----------|------|----------|------|
| v1.1 | 2026-05-06 | Cowork ローカル同期。更新履歴テーブル追加。要点整理版として再構成 | Cowork |
| v1.0 | 2026-05-04 | 初版作成（Notion PoC 設計・実装完了） | Code |
