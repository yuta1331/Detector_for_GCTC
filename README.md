# Detector_for_GCTC
GCTCで使うアプリ

## How To Use
### for detection
```bash
python main_detect.py
```
以上を実行すると
1. watemark.htmlをパースして電力データをdata_listに格納
2. data_listからextract_bitsを作成
3. extract_bitsをasciiデコードすることでwatermarkを検出
また、GUIのために、
4. 以上の3つの変数を```output_wm.json```に格納して保存

### for prev_watermark
```bash
python main_prev.py
```
以上を実行すると
1. prev_watermark.htmlをパースして電力データをdata_listに格納
2. ```output_prev.json```に格納して保存

ただし、for detectionと同形式にしたかったため、<br>
'extract_bits' : '00000000000000000000000000000000'<br>
'watermark' : '0'<br>
としてoutput_prev.jsonに入れておいた

実際には、```watermark.html```と```prev_watermark.html```は、Webサーバからデータを受け取る。

## To Do
~~~- [ ] WebサーバにHTTPリクエストしてデータを受け取る~~~
- [ ] エラー処理とかもっとしっかりする
