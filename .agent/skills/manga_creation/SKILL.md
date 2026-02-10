---
name: manga_creation
description: 参照漫画のスタイルを基に4コマ漫画を作成するスキル
---

# 漫画作成スキル

参照画像 `20260208degital_text.png` のスタイルに基づき、さまざまなストーリーの4コマ漫画を作成する。

## 作成フロー

### Step 1: ストーリー準備
1. ユーザーからストーリーのアイデア（テーマ・オチ）を受け取る
2. `story_templates.md` を参照し、起承転結の4コマ構成に整理する
3. 各コマの内容を台本として記述する：
   - **1コマ目（起）**: 状況設定・導入
   - **2コマ目（承）**: 展開・問題の提示
   - **3コマ目（転）**: 転換・意外な展開
   - **4コマ目（結）**: オチ・結末

### Step 2: 台本の保存
台本を `stories/` ディレクトリに以下の形式で保存：

```markdown
# [タイトル]
作成日: YYYY-MM-DD

## コマ割り

### 1コマ目（起）
- 場面: [場所・背景の説明]
- キャラ: [登場キャラとポーズ]
- セリフ/テキスト: [吹き出し内容]

### 2コマ目（承）
（同形式）

### 3コマ目（転）
（同形式）

### 4コマ目（結）
（同形式）
```

### Step 3: 画像生成
`style_guide.md` を参照し、各コマの画像を `generate_image` ツールで生成する。

**プロンプトテンプレート（各コマ共通のベース）:**

```
Japanese 4-koma manga panel, black and white ink drawing, simple clean lines, minimal detail.
Characters: anthropomorphic cats standing on two legs.
- Gray cat: main character, lazy/tired expression, slightly slouched posture
- White cat: supporting character, deadpan/cool expression, calm posture
Style: manga pen and ink, thick panel borders, speech bubbles with Japanese text.
[コマ固有の内容をここに追記]
```

**画像生成の手順：**
1. 参照画像 `/Users/aoyamahiroki/Desktop/manga2026/20260208degital_text.png` を `ImagePaths` に指定してスタイルを参照させる
2. 各コマを個別に生成（panel_1, panel_2, panel_3, panel_4）
3. 最後に4コマを1枚にまとめた縦長画像を生成

### Step 4: 出力
- 各コマ画像と完成版を `output/` ディレクトリに保存
- ファイル名: `[日付]_[タイトル]_panel_N.png` / `[日付]_[タイトル]_final.png`

## キャラクター設定

### 灰色猫（グレにゃん）
- **性格**: けだるい、面倒くさがり、でも共感されるキャラ
- **外見**: 灰色の体、半開きの目、リュックを背負っていることが多い
- **役割**: 主人公。日常のあるあるを体現する

### 白猫（シロにゃん）
- **性格**: クール、合理的、時代の先を行くタイプ
- **外見**: 白い体、無表情〜やや冷めた目
- **役割**: 相方。オチの要因になることが多い

## 画風ルール

> **重要**: 生成時は必ず `style_guide.md` の内容も確認すること

- 白黒の線画（カラー不可）
- 線は細すぎず太すぎず、均一な太さ
- 背景はシンプル（必要最小限の線）
- 吹き出しは丸型、モノローグは雲型
- コマ枠は太い黒線
- テキストは日本語
