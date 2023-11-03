import cv2
import numpy as np
import os
import SendEmail

# 影片檔案
videoFile = "FrontDoorCCTV.mp4"

# 目錄名稱
outputFolder = "Capture"

# 若無此目錄名稱，建立目錄
if not os.path.exists(outputFolder):
    os.makedirs(outputFolder)

# cap = cv2.VideoCapture(0) 抓取攝影機
# 開啟影片
cap = cv2.VideoCapture(videoFile)

# 取得畫面尺寸
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
area = width * height

# 取得初始平均影像，並濾波or平滑影像
ret, frame = cap.read()
avg = cv2.blur(frame, (4, 4))
avg_float = np.float32(avg)

# 輸出圖檔用計數器
outputCounter = 0


# 當攝影機開啟時
while(cap.isOpened()):
    ret, frame = cap.read()
    # 影片結尾時跳出
    if ret == False:
        break

    # 模糊處理
    blur = cv2.blur(frame, (4, 4))

    # 計算目前影格與平均影像的差異值
    diff = cv2.absdiff(avg, blur)

    # 將圖片轉為灰階
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    # 二值化篩選出變動程度大於門檻值的區域
    ret, thresh = cv2.threshold(gray, 15, 255, cv2.THRESH_BINARY)

    # 去除雜訊，使用cv2.MORPH_OPEN & cv2.MORPH_CLOSE
    kernel = np.ones((5, 5), np.uint8)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)

    # 產生偵測範圍
    contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 偵測條件布林值
    hasMotion = False

    for c in contours:
        # 忽略太小的區域
        if cv2.contourArea(c) < 10000:
            continue
        hasMotion = True

        # 取得動態偵測範圍
        (x, y, w, h) = cv2.boundingRect(c)

        # 畫出外框
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        outputCounter += 1
        # 節省資源，每抓到10禎動態，存取10禎
        if (hasMotion is True) & (outputCounter % 10 == 0):
            # 儲存有變動的影像
            cv2.imwrite("%s/output_%04d.jpg" % (outputFolder, outputCounter/10), frame)

    # 更新平均影像
    cv2.accumulateWeighted(blur, avg_float, 0.1)
    avg = cv2.convertScaleAbs(avg_float)

# 自動寄送使用者警告信
SendEmail.frontdoor_warningemail()
cap.release()

