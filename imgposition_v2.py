"""
MADE BY RDUAN CHEN, FOR RESEARCH ONLY

WARNING:
1. Please make sure requirement.txt already be install.
2. Please make sure all the variable was be set as you want(Please see README.md)
"""
import cv2
import csv
import os
import time


# 定義變數

directory = './videos' # 目錄路徑
video_extensions = ['.mp4', '.avi', '.mov']# 影片檔案的擴展名
horizontal_optima=True
"""
1. 設定True會針對「橫」向影片優化
2. 設定False會對「直」向影片優化
"""

# 存放影片檔案的清單
video_files = []

print(os.walk(directory))

# 遍歷目錄下的檔案
for root, dirs, files in os.walk(directory):
    for file in files:
        # 檢查檔案的擴展名是否為影片擴展名之一
        if os.path.splitext(file)[1].lower() in video_extensions:
            # 將符合條件的影片檔案加入清單
            video_files.append(os.path.join(root, file))

# # 輸出影片檔案清單
print("影片清單如下")
for video_file in video_files:
    print(video_file)



total=len(video_files)
count=0

# 建立影片撷取視窗
if horizontal_optima==False:
    cv2.namedWindow('Video')
    cv2.resizeWindow('Video', 540, 960)
elif horizontal_optima==True:
    cv2.namedWindow('Video')
    cv2.resizeWindow('Video',960,540)
else:
    cv2.namedWindow('Video')
time.sleep(1)

# 定義 "frame" 資料夾路徑
frame_directory = './frame'
if not os.path.exists(frame_directory):
    os.makedirs(frame_directory)


while True:
    video_file = video_files[count]
    
    filename=os.path.basename(video_files[count])
    csv_file = './csv_data/'+filename[:-4]+'.csv'

    cap = cv2.VideoCapture(video_file)

    if horizontal_optima==False:
        cv2.namedWindow('Video')
        cv2.resizeWindow('Video', 540, 960)
    elif horizontal_optima==True:
        cv2.namedWindow('Video')
        cv2.resizeWindow('Video',960,540)
    else:
        cv2.namedWindow('Video')


    # 建立CSV檔案
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Frame', 'X', 'Y'])

        # 滑鼠事件回呼函數
        def mouse_callback(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDOWN:
                frame_number = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
                writer.writerow([frame_number, x, y])
                print(f'Frame: {frame_number}, X: {x}, Y: {y}')
            elif event == cv2.EVENT_RBUTTONDOWN:
                # 建立目標資料夾路徑
                target_directory = os.path.join(frame_directory, os.path.splitext(filename)[0])

                # 確保目標資料夾不存在
                if not os.path.exists(target_directory):
                    os.makedirs(target_directory)

                # 複製當前幀的畫面到目標資料夾
                frame_number = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
                frame_filename = os.path.join(target_directory, f"{frame_number}.jpg")
                cv2.imwrite(frame_filename, frame)
                print(f"Saved frame: {frame_number}")


        # 設定滑鼠事件回呼函數
        cv2.setMouseCallback('Video', mouse_callback)
    
        while True:            
            # 讀取影格
            ret, frame = cap.read()
            if not ret:
                break

            if horizontal_optima==False:
                resized_frame = cv2.resize(frame, (540, 960))
            elif horizontal_optima==True:
                resized_frame = cv2.resize(frame, (960,540))
            else:
                resized_frame=frame

            # 顯示影格
            cv2.imshow('Video', resized_frame)
            # 等待按鍵輸入
            key = cv2.waitKey(0)
            # 按下 ESC 鍵結束迴圈
            if key == 27:
                break
            # 如果按下 'n' 鍵，切換到下一幀
            if key == ord('n'):
                while True:
                    ret, frame = cap.read()
                    if not ret:
                        break
                    if horizontal_optima==False:
                        resized_frame = cv2.resize(frame, (540, 960))
                    elif horizontal_optima==True:
                        resized_frame = cv2.resize(frame, (960,540))
                    else:
                        resized_frame=frame
        

                    cv2.imshow('Video', resized_frame)
                    key = cv2.waitKey(0)
                    if key == ord('n'):
                        break
                    elif key == 27:
                        break
   
    # 釋放影片捕捉物件和關閉視窗
    cap.release()
    cv2.destroyAllWindows()

    count+=1

    if count>=total:
        break
