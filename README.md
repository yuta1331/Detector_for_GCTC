# Detector_for_GCTC
GCTCで使うアプリ

## 目的
機能としては3つ

### read config_json
ここでの目的は1つ
- 予め設定されている，家IDと日付を含むjsonファイルを読みに行く

### http request
ここでの目的は1つ
- 透かし前と透かし後のデータをWebサーバから取ってくること

### detection
ここでの目的は2つ
- 透かし後のデータを成形すること
- 透かし情報を検出すること

### parse prev_watermark.html
ここでの目的は1つ
- 透かし前のデータを成形すること

## Config
### main.py
#### HOST_PORT: WebサーバのIPとポートを書く
```python
HOST_PORT = "192.168.0.3:8080"
```
### launchContainer.sh
#### CONF_DIR: recommendation.jsonのあるホストのディレクトリのパスを書く
絶対パスでも相対パスでもいい
```shellscript
CONF_DIR = "config_jsons"
```

## Run
```bash
sh launchContainer.sh
```
これだけで，Dockerイメージのbuildからrun，main.pyの実行までやってくれる

もし，コンテナ内のconfig_jsonsへのマウントがうまくいかない場合は，config_jsons内のjsonファイルを削除してから実行するとうまくいく

---
以下は別に読まなくてもおけ（Docker導入以前に書いた，プログラムの説明）

## How To Use
```bash
python main.py
```
以上を実行すると以下が実行される

### read config_json
1. recommendation.jsonを読む
2. paramsをhomeID_YYYY-MM-DDの形式に成形

### http request
1. 指定したURIにGETしてレスポンスボディをhtml/prev_watermark.htmlとして保管
2. 指定したURIにGETしてレスポンスボディをhtml/watermarked.htmlとして保管

ここで指定するURIはそれぞれ
1. http://ホスト:ポート/org/家ID_YYYY-MM-DD.html
2. http://ホスト:ポート/mod/家ID_YYYY-MM-DD.html

homeID_YYYY-MM-DDにはread config_jsonで成形した値を持ってくる

### detection
1. watemark.htmlをパースして電力データをdata_listに格納
2. data_listからextract_bitsを作成
3. extract_bitsをasciiデコードすることでwatermarkを検出
また、GUIのために、
4. 以上の3つの変数を```output/output_wm.json```に格納して保存

### parse prev_watermark
以上を実行すると
1. prev_watermark.htmlをパースして電力データをdata_listに格納
2. ```output/output_prev.json```に格納して保存

ただし、for detectionと同形式にしたかったため、<br>
'extract_bits' : '00000000000000000000000000000000'<br>
'watermark' : '0'<br>
としてoutput_prev.jsonに入れておいた

~~~実際には、```watermark.html```と```prev_watermark.html```は、Webサーバからデータを受け取る。~~~

## To Do
- [ ] WebサーバにHTTPリクエストしてデータを受け取る
- [ ] エラー処理とかもっとしっかりする
