# Science net 使用說明

>警告:本工具僅限於學術用途  
MADE BY RDUAN, FOR RESEARCH ONLY


## 程式目的
>本工具目的為在相機所錄製的實驗影片中提取數據，需事先錄製好影片，在設置相機時請確保相**機垂直於地面，並與物體運動方向平行**，可用於觀測運動學中大部分的實驗。



## 必要安裝項目:
1. python環境 (具有pip工具)
2. vscode (建議使用)
3. 必要使用函式庫，請在終端機中執行下列代碼
   ```shell
   pip install -r requirement.txt
   ```

## 請確認本專案中是否有以下的資料夾
1. ./csv_data
2. ./csv_displacement
3. ./videos


## 這些資料夾裝的東西如下
1. ./csv_data:
   影片中標記球點的位置
2. ./csv_displacement
   經過位移後的資料
3. ./videos:
   影片資源
3. ./frame
   截圖影像


## 請確認有兩.py的檔案，執行順序如下
1. imgposition.py
2. data_process.py
3. requirement.txt

## imgposition的作用如下:
imgposition可以手動將videos底下的影片的球點標示出來，並且存成csv檔，操作按鍵分成兩個
1. 按下 `n` 鍵可以切換下一幀
2. 按下`esc`可以退出影片，並切換下一個影片，原數據會被覆蓋掉
3. 按下`滑鼠左鍵`可以進行標點
4. 按下`滑鼠右鍵`可以進行截圖
5. 使用前請先確認horizontal_optima設定正確。
6. 使用imgposition轉出的csv檔案會與匯入的影片檔名相同
7. 若有將座標轉換成公分的需求,請放一個已知長度的參考物於實驗運動的直線上，且平行於相機，並且與相機垂直於地面，並錄製一個一秒鐘的影片,標點時在第一幀標記參考物的底部,第二幀為參考物的上方


## CSV_data的資料結構
|frame    |x  |y  |
|---------|----|----|
|frame_num|座標|座標|
## data_process.py 的操控方式如下:
data_process.py 這個程式可以將imgposition所做的標記全部平移到原點，以及將每個點與原點的距離轉成公分，特別適合在標記拋物線運動時使用

1. 修改參考物件的高度`object_height=____(cm)`,請注意，單位為公分。
2. 修改ratio_switch,設定True 程式會自動將單位轉成公分,False則是使用opencv中的座標。
3. 若資料中有錯誤，會在`shell`中顯示`FILE {} Index out of range error occurred.`
