# コンテクストファイル更新標準運用

**Status**: Active draft  
**Owner**: Codex PMO  
**Related issues**: #36, #37, #38  

## 目的

AI運用で使うコンテクストファイルを、毎回手作業で差し替えずに更新できるようにする。

この運用では、Drive SSOTを正式な原本、GitHub Mirrorを差分管理と検証の場、各AI向けKnowledge Packを派生ビューとして扱う。

## 基本方針

1. **SSOTとAI向けビューは分ける**
   - Drive SSOT: 正式な原本、確定ルール、引き継ぎ資産。
   - GitHub Mirror: 差分確認、レビュー、Issue/PR連携、スクリプト管理。
   - AI Knowledge Pack: Gemini / ChatGPT / Codex / Claudeが読みやすい圧縮ビュー。

2. **Knowledge Packは原本ではない**
   - Knowledge Packにだけ書かれた重要ルールを正式ルールにしない。
   - 重要ルールは、必ずSSOTまたはGitHub Mirrorの正本ドキュメントへ反映する。

3. **GemはDriveファイル参照を優先する**
   - GemのKnowledgeには、ローカルアップロードではなくGoogle Drive上のファイルを紐づける。
   - Driveファイルを更新すればGem側に最新化が反映される前提で運用する。
   - Gem側で毎回ファイルを差し替える運用は避ける。

4. **全部入りにしない**
   - AI向けKnowledge Packは、役割、禁止事項、現在地、優先Issue、QCD使い分け、重要リンクだけを中心にする。
   - 詳細ログ、古い議論、未整理メモは必要時に追加投入する。

## ファイル分類

| 分類 | 目的 | 例 | 更新頻度 |
| --- | --- | --- | --- |
| SSOT core | 正式な運用ルール・引き継ぎ資産 | Drive SSOT上の基本コンテクスト | 重要変更時 |
| GitHub mirror | 差分管理・レビュー・Issue連携 | `docs/*.md`, `docs/*.txt` | 作業単位 |
| Tool context | 各AIの入口 | `GEMINI.md`, `CONTEXT_FOR_CODEX.md`, `AGENTS.md.txt` | 役割変更時 |
| Knowledge Pack | AIに読ませる圧縮ビュー | `GEMINI_OPS_KNOWLEDGE_PACK.md`など | 週次または重要変更時 |
| Working note | 未整理メモ・議事録・一時素材 | field notes, transcripts | 都度 |

## 更新トリガー

次のいずれかが起きたら、コンテクスト更新対象にする。

- AIツールの役割、権限、禁止事項が変わった。
- Gemini / ChatGPT / Claude / Codexの使い分けが変わった。
- Token制限、QCD、ライセンス前提などの運用判断が変わった。
- Notion / GitHub Issue / Drive SSOTの連携ルールが変わった。
- 重要Issueの優先度、親子関係、進捗が変わった。
- 近藤さんの取扱説明書、PMO Motivation Design、議案AXなどコア思想が更新された。
- GemのKnowledgeに入れるべき代表ファイルが増減した。

## 標準更新プロセス

### Step 1: 変更を分類する

変更を次のどれかに分類する。

- **Rule change**: 今後の標準運用に影響する。
- **Context change**: AIが作業するために知るべき現在地が変わる。
- **Issue change**: GitHub Issue / Notion Project / Taskの関係が変わる。
- **Working memo**: まだ正式化しないメモ。

Rule changeまたはContext changeなら、Knowledge Packだけでなく正本にも反映する。

### Step 2: 正本を更新する

原則:

- 正式ルールはDrive SSOTまたはGitHub Mirrorの正本ドキュメントへ反映する。
- Tool contextには要約だけを書く。
- Knowledge PackにはAIが実行しやすい形で圧縮して書く。

判断:

- Gemini運用ルール: `GEMINI.md` / `docs/GEMINI_OPS_LANE_SETUP.md`
- Codex PMO運用: `docs/CONTEXT_FOR_CODEX.md` / `docs/PMO_REPORTING_WORKFLOW.md`
- AI役割分担: `docs/AGENTS.md.txt` / `docs/TOOL_CONTEXT_GUIDE.md`
- 人間側の取扱説明書: `docs/HUMAN_OPERATING_MANUAL_FOR_AI_PMO.md`
- Motivation / engagement: `docs/PMO_MOTIVATION_DESIGN.md`

### Step 3: Knowledge Packを更新する

Gemini向けは、詳細SSOTを丸ごと入れず、以下だけを短く入れる。

- 現在の目的
- Geminiが担当すること
- Geminiが直接更新してはいけないもの
- 現在の優先Issue
- QCD / Token / ライセンス前提
- Codexへの返し方
- 重要リンクと正本ファイル

推奨:

- `docs/GEMINI_OPS_KNOWLEDGE_PACK.md` を作る。
- GemのKnowledgeには、Drive上のこのファイルを紐づける。
- 詳細が必要な場合だけ、Geminiに追加ファイルを都度渡す。

### Step 4: Issueに記録する

運用変更は関連Issueにコメントする。

- Gemini運用: #37
- Token / Capacity alert: #38
- Notion / Project / Task標準化: #36
- Token-aware Process Design: #39
- JC DX / AX構想: #40, #41

Issueコメントには最低限以下を書く。

```markdown
## Context update

Updated:
- `file/path`

Reason:
- ...

Impact:
- ...

Next:
- ...
```

### Step 5: 同期・反映を確認する

確認観点:

- GitHub Mirror上で差分が確認できる。
- Drive SSOTへ反映が必要な場合、反映待ちとして記録されている。
- GemのKnowledgeがDriveファイル参照になっている。
- Gem側でローカル再アップロードが不要になっている。
- 重要変更なら外部レビューまたはGemini auditに回せる。

## 更新頻度

| 種類 | 頻度 | 例 |
| --- | --- | --- |
| 即時更新 | 重要な役割・権限・禁止事項変更 | Geminiは直接更新禁止、Codexが最終反映 |
| 作業後更新 | 実務Issueの進捗・関連付け | #36, #37, #41の更新 |
| 週次棚卸 | Knowledge Packの肥大化・古い情報整理 | 週1回 |
| 月次棚卸 | SSOT / GitHub Mirror / Notion / Issue関係 | PMO定期チェック |

## Gemini Gems運用

Gemini Gemsでは、毎回Knowledgeファイルを差し替えない。

標準運用:

1. Drive上にGemini Ops Lane用Knowledge Packファイルを置く。
2. GemのKnowledgeでDriveファイルとして紐づける。
3. 更新はDrive上のKnowledge Packファイルに対して行う。
4. GemのInstructionsは頻繁に変えず、役割・禁止事項・出力形式だけに絞る。
5. Knowledge Packが大きくなりすぎたら、Gemを分けるか、詳細ファイルを必要時投入に切り替える。

## Driveディレクトリ構成

Drive上では、SSOT本体とGemini向けKnowledge Packを分ける。

推奨構成:

```text
SSOT/
  00_MANIFEST/
    MANIFEST
    update_log

  10_Core_Context/
    shared_source
    tool_context_guide
    agents
    codex_context
    human_operating_manual

  20_Operations/
    pmo_reporting_workflow
    context_update_workflow
    github_drive_sync_workflow
    external_review_workflow

  30_Project_Issues/
    issue_exports
    notion_exports
    pmo_reports

  40_Field_Inputs/
    meeting_notes
    field_notes
    transcripts
    ocr_inputs

  50_Gemini_Knowledge_Pack/
    00_Common/
      GEMINI_OPS_KNOWLEDGE_PACK
      source_index
      last_updated_note

    10_Gems/
      Gemini_Ops_Lane/
        knowledge_pack
        mode_prompts
        test_results

      Senmu_Field_Scribe/
        knowledge_pack
        field_intake_examples

      PMO_Integrity_Auditor/
        knowledge_pack
        audit_targets

    90_Full_Scan/
      full_scan_index
      scan_request_templates
      archive_snapshots
```

### 使い分け

- `10_Core_Context` と `20_Operations` は正式なSSOT側。
- `50_Gemini_Knowledge_Pack` はGeminiに読ませるための派生ビュー。
- `50_Gemini_Knowledge_Pack/00_Common` は複数Gemで共通利用する軽量コンテクスト。
- `50_Gemini_Knowledge_Pack/10_Gems/*` はGemごとの専用コンテクスト。
- `50_Gemini_Knowledge_Pack/90_Full_Scan` は、Geminiの長文コンテクスト特性を使った全走査・監査用。

通常運用では、Gemには `00_Common` と対象GemディレクトリだけをDrive参照で紐づける。

全走査・監査が必要なときだけ、`90_Full_Scan` のテンプレートを使って、SSOT本体・Issue exports・Notion exports・field inputsをまとめてGeminiに読ませる。

### 命名ルール

Drive上のGemini向けファイルは、以下を推奨する。

```text
YYYY-MM-DD__scope__purpose__status
```

例:

```text
2026-05-10__gemini-ops-lane__knowledge-pack__active
2026-05-10__pmo-integrity-auditor__audit-targets__active
2026-05-10__full-scan__ssot-issue-notion-index__draft
```

Gemから直接参照するファイルは、ファイル名末尾に `__active` を付ける。古いものは `__archived` にするか、archiveフォルダへ移す。

## リンク更新ルール

今回のようにフォルダを新規作成し、既存SSOTファイルを移動しない場合、既存リンク更新は原則不要。

ただし、今後既存ファイルを新ディレクトリへ移動する場合は、リンク更新が必要になる可能性がある。

リンク種別ごとの扱い:

| リンク種別 | 移動時の扱い | 方針 |
| --- | --- | --- |
| Google Drive file URL | 多くの場合、ファイルIDベースなので移動しても維持されやすい | 重要リンクはDrive URLを優先 |
| Google Drive folder URL | フォルダ自体を移動しなければ維持される | ルートフォルダURLはMANIFESTに集約 |
| ローカル絶対パス `G:\...` | ファイルを移動すると壊れる | 参照用・作業用に限定し、正本リンクにしない |
| GitHub相対パス | GitHub内でファイルを移動すると壊れる | PR/Issueコメントでは移動後に更新 |
| Gem KnowledgeのDrive参照 | Driveファイル自体が同一なら追随しやすい | ファイル差し替えより同一ファイル更新を優先 |

安全な移行手順:

1. 既存ファイルはいきなり移動しない。
2. 新ディレクトリにコピーまたは派生ビューを作る。
3. MANIFEST / index / Issueに新旧対応を記録する。
4. 各AIコンテクストが新リンクを参照できることを確認する。
5. 古い場所のファイルは一定期間残すか、移転先案内を置く。
6. 問題がなければ旧ファイルをarchiveへ移す。

原則として、SSOT正本はDrive URL、作業補助はローカル絶対パス、差分確認はGitHubパスで使い分ける。

## してはいけないこと

- Gemに毎回ローカルファイルを再アップロードする。
- Knowledge Packだけを更新して、正本のSSOT / GitHub Mirrorを更新しない。
- 過去ログや未整理メモを常時Knowledgeに入れ続ける。
- Geminiの出力をそのままSSOTに確定反映する。
- Token節約のために、重要判断まで低品質モードへ落とす。

## Done Criteria

- 変更の正本が明確である。
- AI向け入口ファイルに必要最小限の要約がある。
- Knowledge PackはDrive参照でGemに紐づいている。
- 関連Issueに更新理由と影響が記録されている。
- 次にどのAIが読んでも、現行ルールと優先事項を誤解しない。

## Issue Close時のツール別更新サジェスト

Issueをcloseするときは、作業内容に応じて、各ツール側で必要な操作をユーザーへ短く提示する。

目的:

- 各AIツールの添付ファイル・Project files・Knowledge・repo checkoutが古いままになることを防ぐ。
- Drive SSOT / GitHub Mirror / Notion / Gemini Knowledge Packのどこを最新化すべきか明確にする。
- ユーザーが次にどのツールを開けばよいか迷わないようにする。

標準出力:

```markdown
## Tool-side update suggestions

Codex:
- [必要操作]

Claude Code:
- [必要操作]

Claude Chat:
- [必要操作]

Claude Cowork:
- [必要操作]

ChatGPT:
- [必要操作]

Gemini / Gems:
- [必要操作]

Gemini CLI:
- [必要操作]

Notion:
- [必要操作]

Drive SSOT:
- [必要操作]

GitHub:
- [必要操作]
```

### 共通判断

- GitHub Mirrorを更新した場合:
  - Claude Code / Codex / Gemini CLI は repo最新化が必要。
  - ChatGPT / Claude Chat / Gemsの手動添付はsnapshot扱いなので、必要に応じて再投入またはDrive参照へ切り替える。

- Drive SSOTを更新した場合:
  - Drive URL / MANIFEST / Knowledge Packの更新要否を確認する。
  - ローカル絶対パスだけを正本リンクとして扱わない。

- Gemini Knowledge Packを更新した場合:
  - GemsがDriveファイル参照になっているか確認する。
  - 初期ローカル添付に依存していないか確認する。

- Tool-side settingsを変更した場合:
  - `docs/TOOL_CONFIGURATION_REGISTER.md` に設定値、推奨理由、最終確認日を記録する。
  - バイパス権限、自動PR、自動修正、自動マージ、通知、Knowledge/Project files、容量制限に関わる設定は必ず記録する。

- Notion Project / Task / DBに影響する場合:
  - Notion側のProject / Task / Issue関連付けを確認する。
  - ただしNotionはSSOTではなく進捗管理レイヤーとして扱う。

### Issue closeコメントへの入れ方

Issueのclose時またはpostmortem時に、以下を簡易で入れる。

```markdown
Tool-side update suggestions:
- Codex: latest repo/context already reflected / N/A
- Claude Code: pull latest before next work
- Claude Chat: replace old project attachments if this context is needed
- Claude Cowork: update only if Notion/Drive task flow is affected
- ChatGPT: use latest context files or summary if wall-discussing this issue
- Gemini / Gems: update Drive Knowledge Pack or confirm Drive reference
- Gemini CLI: no extra action if `scripts/external_review.py` context list is updated
- Notion: [N/A / update project-task relation]
- Drive SSOT: [N/A / pending sync / updated]
- GitHub: [closed / follow-up issue created]
```

軽量Issueでは、影響があるツールだけ列挙してよい。大型Issueでは全ツール分を列挙する。
