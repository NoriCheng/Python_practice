import cv2
import numpy as np

videoFile = "FrontDoorCCTV.mp4"
cap = cv2.VideoCapture(videoFile)

# 設定影像尺寸
width = 1920
height = 1080

# 設定擷取影像的尺寸大小
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
area = width * height

# 取得初始平均影像，並濾波or平滑影像
ret, frame = cap.read()
avg = cv2.blur(frame, (4, 4))
avg_float = np.float32(avg)

while True:
    ret, frame = cap.read()

    # 影片結尾時跳出
    if ret == False:
        break

    # 模糊處理
    blur = cv2.blur(frame, (4, 4))

    # 計算目前影像與平均影像的差異值
    diff = cv2.absdiff(avg, blur)

    # 將圖片轉為灰階
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    # 二值化篩選出變動程度大於門檻值的區域
    ret, thresh = cv2.threshold(gray, 15, 255, cv2.THRESH_BINARY)

    # 去除雜訊，使用cv2.MORPH_OPEN & cv2.MORPH_CLOSE，腐蝕與擴張
    kernel = np.ones((5, 5), np.uint8)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)

    # 產生偵測範圍
    contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        # 忽略範圍太小的區域
        if cv2.contourArea(c) < 10000:
            continue
        # 取得動態偵測範圍
        (x, y, w, h) = cv2.boundingRect(c)

        # 畫出外框
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # 顯示偵測結果影像
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # 更新平均影像
    cv2.accumulateWeighted(blur, avg_float, 0.01)

    # 提高對比
    # avg = cv2.convertScaleAbs(avg_float)

    # 按下Esc 關閉影片
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
