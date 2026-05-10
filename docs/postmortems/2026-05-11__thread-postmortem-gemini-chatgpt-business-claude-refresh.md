# スレッド全体ポストモーテム: Gemini Ops / ChatGPT Business / Claude Refresh / SHIFT AI-BPaaS文脈

**日付**: 2026-05-11  
**対象**: 本スレッド全体  
**Owner**: Codex PMO  

## エグゼクティブサマリー

本スレッドは、Gemini Ops Laneの設定継続から始まり、最終的にはAI PMOアーキテクチャ全体の強化セッションになった。

主な成果は以下。

- Gemini / Gemsを、長文コンテクスト処理・Token relief用レーンとして実運用可能にした。
- ChatGPT Businessを、外部顧問レビュー / 壁打ち / 文脈整理レーンとして設定した。
- ChatGPT BusinessのGitHub connectorを読み取り専用運用で確認した。
- Claude Code、Claude Chat、Claude Coworkを、Claude側の制限復旧後に最新コンテクストへ追随させた。
- Gemini CLIをローカルで初回利用し、専務PJ用の起動方法と役割を確認した。
- SHIFT AI-BPaaSに関する本業・キャリア文脈を追加し、誤読防止メモも明示した。
- ツール側設定を正式な構成管理対象として扱い始めた。
- 各ツールが実際に何を情報源として読むのかを、Drive / GitHub / Project Knowledge / local / memory に分けて理解した。

要するに、Token/capacity危機と複数のconnector摩擦を、再利用可能なAI PMO運用アーキテクチャに変換できたスレッドだった。

## 流れ

### 1. Gemini Ops Laneの設定

OpenAI / ClaudeのToken容量がボトルネックになりつつあったため、Geminiを優先して導入した。

決めたこと:

- GeminiはGitHub、Drive SSOT、Notion、Sheetsを直接更新しない。
- Geminiは長文資料、現場メモ、議事録、Drive/GitHub/Notionエクスポート、整合性監査を担う。
- Geminiは、事実、推測、推奨アクション、リスク、Codexへのhandoff候補を分けて返す。
- Gemini / Gemsは、古いローカル添付ではなくDriveリンク型のKnowledgeを使う。

成果:

- Gemini Ops Laneが、長文処理とToken reliefの実用レーンになった。

### 2. Token-aware Process Design

ユーザーは、Token/capacity制約についてより大きな仮説を立てた。

主な仮説:

- Token/capacity制約は、個人のツール利用上限だけの話ではない。
- AIエージェント時代の業務プロセス設計における制約資源になりうる。
- コストセンター、非営利団体、中堅中小、社内システム部門PoCでは、十分なAI利用量を常に買えるとは限らない。
- AI導入設計では、Token上限、プラン制約、コスト、ルーティング、冗長化、退避先を含める必要がある。

成果:

- Token-aware Process Designが研究テーマ / 運用テーマとして明確化された。
- Capacity incidentを、ROIやQCDの観点と接続できるようになった。

### 3. Human-AI Mutual Optimization

ユーザー自身の認知特性、動機、仕事の進め方について深掘りした。

重要なモデル:

- 意味づけ、構造化、抽象と具体の往復、領域横断の総合に強い。
- 一方で、反復的な実務遂行、細かい期限管理、ルーチンの継続的なcloseには負荷が高い。
- AI PMOは、ユーザー本人を無理に運用エンジン化するのではなく、外付けの実行・追跡・収束レイヤーとして機能するべき。

成果:

- `HUMAN_OPERATING_MANUAL_FOR_AI_PMO.md`
- `PMO_MOTIVATION_DESIGN.md`
- 支援スタイルの明文化:

```text
意味づけ -> 最小アクション -> 発散退避 -> 収束外部化
```

### 4. SHIFT AI-BPaaS文脈

ユーザーがSHIFTの公開決算資料を提供し、自身の本業文脈を補足した。

重要な補足:

- ユーザーはSHIFTのAI-BPaaS事業部に所属している。
- ただし、決算資料に掲載されたAI-BPaaS新サービスそのものだけを専任で担当している、という意味ではない。
- 主担当文脈は既存BPaaS領域、特に情報システムアウトソーシング / 要員代替領域。
- その既存BPaaS領域がAI-BPaaSへ業態転換していく中で、担当顧客群へのAI-BPaaSを含むサービス展開も担う。

成果:

- `docs/reference/shift_ai_bpaas_q2_2026_context.md`
- 下位モデル向けの誤読防止メモ。
- 能力ラベル候補:

```text
Multi-vendor AI Deployment Strategist
```

### 5. ChatGPT Business移行

OpenAI / Codexの利用上限に到達し、ChatGPT Businessへ移行した。

起きたこと:

- Business WorkspaceとProject設定により、個人プラン時代とは別の設定・connector挙動が発生した。
- `Connector scope creator has left this project` により、connector ownership / scopeのリスクに気づいた。
- 怪しい旧Projectを修復するより、新Projectを作る方針にした。
- Drive sourceの再同期 / 再インデックスが必要になりうることを確認した。
- GitHub connectorを読み取り専用で確認した。

成果:

- ChatGPT Businessは、外部顧問レビュー / 壁打ち / 文脈整理レーンとして使える状態になった。
- ChatGPT Business側も、責務境界と情報源階層を理解できた。

### 6. Claude復旧後の反映

Claude側は一時的に利用制限に達していたが、復旧後に以下を確認した。

- Claude Codeがrepo contextを最新化。
- ただし最初は新規contextファイルを見つけられなかった。
- 原因は、ファイルがDrive / Codexローカルには存在したが、GitHub Mirrorへcommit/pushされていなかったため。
- Codexが必要ファイルをcommit/pushした後、Claude Codeが読み込み成功。
- Claude ChatはDrive contextを直接読めた。
- Claude CoworkはDriveファイルを見つけ、ローカル取り込みも行った。

成果:

- Claude Code / Chat / Coworkが最新コンテクストに追随した。
- 以下の違いが明確になった。

```text
Claude CodeはGitHub/repoを読む。
Claude Chat / CoworkはDriveを直接読める。
```

### 7. Gemini CLIローカル設定

ユーザーがGemini CLIをローカルで初回起動した。

観測:

- 初期起動場所が `C:\Windows\System32` だった。
- 専務PJで使う場合はrepo rootから起動する必要がある。
- `no sandbox` 状態だったため、原則は読み取り・レビュー用途が安全。

成果:

- Gemini CLIがプロジェクトdocsを読み、役割・権限境界を正しく理解した。

## 学んだアーキテクチャ

### 情報源階層

```text
Drive SSOT
-> GitHub Mirror / Version Layer
-> Notion Operational Task Layer
-> Tool-local Project Knowledge / Memory / Attachments
```

### ツール別役割

```text
Codex PMO:
実行、GitHub反映、docs更新、Drive/GitHub同期、PMO close処理。

Gemini / Gemini CLI:
長文一次処理、監査、現場メモ構造化、Token relief。

ChatGPT Business:
外部顧問レビュー、壁打ち、論点整理、Issue/Notion候補作成。

Claude Code:
GitHub/repo文脈、実装、コード寄り推論。

Claude Chat:
対話、レビュー、文章化、セカンドオピニオン、Drive文脈の反映。

Claude Cowork:
Notion / Sheets / Drive系の実務支援。Codex PMOでスコープ管理する。

Notion:
実務タスクと進捗の運用レイヤー。
```

## なぜ重要だったか

このスレッドで分かったのは、AI PMOの信頼性はプロンプトの良し悪しだけでは決まらないということ。

必要なのは以下。

- 情報源の鮮度
- connector ownership
- workspace設定
- 読み取り / 書き込み権限
- 役割境界
- Token / capacity routing
- ツール間のcontext伝播
- postmortem logging

これは、そのまま企業向けAI導入・AI-BPaaSデプロイの論点にも接続する。

- AI capacityは制約資源。
- Knowledge freshnessはガバナンス論点。
- Connector ownershipは運用リスク。
- Tool configurationはアーキテクチャ。
- Human-AI fitは導入定着とスループットに効く。

## So What

このスレッドにより、システムは以下の意味で強くなった。

- Claudeが制限に達しても、GeminiとChatGPT Businessで長文処理・壁打ちを継続できる。
- OpenAIが制限に達しても、GeminiとClaudeで一部の流れを継続できる。
- Drive contextが更新されたとき、各ツールのsource refreshを確認できる。
- repo型ツールがファイルを見失ったとき、GitHub Mirror状態を確認できる。
- SHIFT文脈を下位モデルが誤読しないよう、明示的なガードレールを持てた。
- AIが勝手にwrite authorityを持たないよう、役割境界を文書化できた。

ユーザーは、単にAIツールを使う状態から、小さなmulti-AI PMO systemを運用する状態へ移行した。

## So How

本スレッドから生まれた標準運用は以下。

1. ツール側設定は `TOOL_CONFIGURATION_REGISTER.md` に記録する。
2. Context更新後、対象ツールが何をsourceとして読むか確認する。
   - Drive
   - GitHub
   - Project Knowledge
   - local files
   - memory / record
3. Drive source型ツールでは、必要に応じてresync / re-indexを確認する。
4. GitHub/repo型ツールでは、refresh前にcommit/push済みか確認する。
5. Advisory toolはadvisoryのままにする。
6. 重い読解・監査・Token reliefはGeminiへ逃がす。
7. durableな反映はCodex PMOがIssue、docs、GitHubへ残す。
8. Capacity incidentは単なる不便ではなく、運用データとして扱う。
9. 摩擦は標準化Issueまたはcontext updateへ変換する。
10. 大きなtool setup作業はpostmortemで閉じる。

## うまくいったこと

- ユーザーがエラーやスクリーンショットをすぐ共有した。
- Codex PMOが発見事項をIssue、docs、Driveコピー、commit/pushへ変換した。
- OpenAI、Anthropic、Googleの3系統に冗長性ができた。
- SHIFT本業文脈を、他AIへ再利用する前に正しく補助線付きで整理できた。
- context freshnessのルールを、抽象論ではなく実際の失敗から発見できた。
- ツール側設定を、単なるUI設定ではなく構成管理対象として扱えた。

## 難しかったこと

- ツールごとに情報源モデルが違う。
- Business移行によりconnector ownershipが曖昧になった。
- 一部のDrive / shell出力に文字化けがあった。
- ChatGPT Businessのsource resync挙動がUI上分かりづらかった。
- Claude Codeのrepo視点とClaude Chat/CoworkのDrive視点が異なった。
- Capacity制約により、作業中にツール切り替えが発生した。
- 重要docsがローカルにはあるがGitHub Mirrorには未反映、という状態が発生した。

## 残リスク

- 今後のcontext更新も、source refreshを確認しないと伝播漏れが起きうる。
- Memory / RecordがSSOTとズレる可能性がある。
- Drive SSOTとGitHub Mirrorは今後も乖離しうる。
- アカウントやWorkspace変更でconnector ownershipが再びズレる可能性がある。
- network-enabled agent設定は、データ境界を意識して使う必要がある。
- このシステムは、postmortem disciplineを継続できるかに依存する。

## 後続推奨

### Close / Continue

- ユーザー確認後、#43をcloseする。
- #36でPMO / Issue / Notion / closeout標準化を継続する。
- #38でcapacity alertを継続する。
- #39でToken-aware Process Designを継続する。
- #40/#41でJC AI/DX、議案作成AXを継続する。

### 運用

- Issue close時に、Tool-side update suggestionsセクションを入れる。
- closeout checksにsource refresh stateを追加する。
- Project Ownership Registerを正式化する。
- 定期的に、主要AIレーンへrole / source freshness checkを投げる。

### キャリア / 本業

- JC / 個人AI PMO実験を、AI-BPaaSデプロイ知見として継続記録する。
- 以下に接続できる事例を残す。
  - 業務可視化
  - コストセンターAI ROI
  - multi-vendor AI routing
  - 制約条件下のAI導入
  - PMO / governance operating model

## クロージング

本スレッドの中核学習:

```text
AIエージェント運用は、モデルの賢さだけで失敗するのではなく、
古いcontext、不明確な権限、connector drift、capacity制約、close loop不足で失敗しやすい。
```

本スレッドでは、それらのリスクを明示的な運用ルールへ変換した。
