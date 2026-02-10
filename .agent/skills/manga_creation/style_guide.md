# スタイルガイド

参照画像 `20260208degital_text.png` の分析に基づく画風定義。

## 画風の特徴

### 線画
- **線の種類**: ペンインク風、均一な太さ
- **線の量**: 最小限。細部は省略して輪郭線中心
- **ハッチング**: ほぼなし。陰影は最小限のベタ塗り

### コマ枠
- **枠線**: 太い黒線（2-3px相当）
- **形状**: 長方形、角は直角
- **配置**: 縦に4コマ、等間隔
- **余白**: コマ間に適度な余白

### 背景
- **描き込み度**: 簡素（場所がわかる最低限の要素）
- **パターン**: 直線的な建築要素（階段、壁、机、黒板など）
- **トーン**: 使用しない。白背景ベース

### 吹き出し
- **通常セリフ**: 丸型の吹き出し、尾は話者方向へ
- **モノローグ/心の声**: 雲型（もくもく）吹き出し
- **テキスト**: 手書き風フォント、日本語
- **効果音**: 吹き出し外にフリーハンド文字

### キャラクター描写
- **頭身**: 3〜4頭身
- **体型**: 丸みのあるシンプルな体
- **表情**: 目と眉で表現（口は小さめ）
- **ポーズ**: 直立二足歩行、人間的な動作

## generate_image プロンプト構成

### 基本プロンプト（すべてのコマに適用）

```
Japanese yonkoma (4-koma) manga style, single panel, black and white pen and ink drawing,
clean simple lines, minimal hatching, white background with simple architectural elements,
thick black panel border, anthropomorphic cats standing upright on two legs,
3-4 head-tall proportions, round simple body shapes, expressive eyes.
```

### キャラクター指定

**灰色猫を含む場合に追加：**
```
A gray-furred cat character with half-closed sleepy/lazy eyes, slightly slouched posture,
wearing a large backpack when outdoors.
```

**白猫を含む場合に追加：**
```
A white-furred cat character with a deadpan calm expression, upright posture,
sometimes holding a laptop or tablet device.
```

### 場面別の背景指定例

| 場面       | プロンプト追加文                                    |
| ---------- | --------------------------------------------------- |
| 学校の階段 | `staircase with handrail, school building interior` |
| 教室       | `classroom with desks, blackboard, windows`         |
| 通学路     | `simple street with buildings, sidewalk`            |
| 家         | `simple room interior, minimal furniture`           |
| 公園       | `park bench, simple tree`                           |
| コンビニ   | `convenience store interior, shelves`               |

### 吹き出し指定

```
Speech bubble containing [日本語テキスト], rounded oval shape with tail pointing to speaker.
```

または心の声の場合：
```
Thought cloud bubble containing [日本語テキスト], cloud-shaped with small circles leading to thinker.
```

## 品質チェックリスト

生成後、以下を確認：
- [ ] 白黒線画になっているか（カラー要素なし）
- [ ] キャラクターが二足歩行の猫か
- [ ] 線がシンプルで少ないか
- [ ] 背景が簡素か
- [ ] コマ枠が太い黒線か
- [ ] 全体的に参照画像の雰囲気に近いか
