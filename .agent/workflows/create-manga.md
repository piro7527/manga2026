---
description: 4コマ漫画を作成する（ストーリーのアイデアから完成画像まで）
---

# 漫画作成ワークフロー

## 前提条件
- `.agent/skills/manga_creation/SKILL.md` のスキルを使用する
- 参照画像: `/Users/aoyamahiroki/Desktop/manga2026/20260208degital_text.png`

## 手順

1. ユーザーからストーリーのアイデア（テーマ、シチュエーション、オチのイメージ）を聞く

2. `.agent/skills/manga_creation/SKILL.md` を読み、作成フローを確認する

3. `.agent/skills/manga_creation/story_templates.md` を参照し、テーマに合うテンプレートを選ぶ

4. 4コマの台本を作成し、ユーザーに確認する：
   - 1コマ目（起）: 導入シーン
   - 2コマ目（承）: 展開
   - 3コマ目（転）: 転換
   - 4コマ目（結）: オチ

5. ユーザーがOKしたら、台本を `stories/[日付]_[タイトル].md` に保存する

6. `.agent/skills/manga_creation/style_guide.md` を読み、プロンプトを構成する

7. `generate_image` ツールで各コマの画像を生成する。参照画像を `ImagePaths` に含める：
   - パネル1〜4を個別に生成
   - 参照画像パス: `/Users/aoyamahiroki/Desktop/manga2026/20260208degital_text.png`

8. 最後に4コマを1枚にまとめた縦長画像を生成する

9. 完成画像を `output/[日付]_[タイトル]/` に保存する

10. ユーザーに完成した漫画を見せ、修正の要望があれば対応する
