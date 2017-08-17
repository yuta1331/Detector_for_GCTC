# Detector_for_GCTC
GCTCで使うアプリ

## 目的
機能としては3つ

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

## How To Use
```bash
python main.py
```
以上を実行すると以下が実行される

### http request
1. 指定したURIにGETしてレスポンスボディをget prev_watermark.htmlとして保管
2. 指定したURIにGETしてレスポンスボディをwatermarked.htmlとして保管

ここで指定するURIはそれぞれ
1. http://ホスト:ポート/org/家ID_YYYY-MM-DD.html
2. http://ホスト:ポート/mod/家ID_YYYY-MM-DD.html

今回はhtml名は固定したが、実際のデモでは外から指定された値に従ってリクエストを送る

### detection
1. watemark.htmlをパースして電力データをdata_listに格納
2. data_listからextract_bitsを作成
3. extract_bitsをasciiデコードすることでwatermarkを検出
また、GUIのために、
4. 以上の3つの変数を```output_wm.json```に格納して保存

### parse prev_watermark
以上を実行すると
1. prev_watermark.htmlをパースして電力データをdata_listに格納
2. ```output_prev.json```に格納して保存

ただし、for detectionと同形式にしたかったため、<br>
'extract_bits' : '00000000000000000000000000000000'<br>
'watermark' : '0'<br>
としてoutput_prev.jsonに入れておいた

~~~実際には、```watermark.html```と```prev_watermark.html```は、Webサーバからデータを受け取る。~~~

## To Do
- [ ] WebサーバにHTTPリクエストしてデータを受け取る
- [ ] エラー処理とかもっとしっかりする
