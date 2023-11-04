import cv2

# 載入分類器
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

# 從視訊鏡頭擷取影片
#cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# 或者使用現有影片
cap = cv2.VideoCapture(r'source/20230825_164551.mp4')

while True:
    # Read the frame
    _, img = cap.read()
    # 轉成灰階
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 偵測臉部
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.09, minNeighbors=3, minSize=(60, 60))

    # 繪製人臉部份的方框
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # 顯示成果
    cv2.namedWindow('img', cv2.WINDOW_KEEPRATIO)  # 正常視窗大小
    cv2.imshow('img', img)  # 秀出圖片
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# Release the VideoCapture object
cap.release()
cv2.destroyAllWindows()

'''
scaleFactor:圖像大小在每個圖像尺度上減少了多少。
這個值用於創建縮放金字塔，以便檢測圖像中多個縮放的面部
(一些面可能更接近前景，因此更大；其他面可能更小並且在背景中，因此使用不同的縮放)。
比如設置值為1.05，則表明我們在金字塔中的每個級別將圖像的大小減小了5％。

minNeighbors:每個窗口應該有多少個neighbors才能將窗口中的區域視為一個臉。
級聯分類器將檢測面部周圍的多個窗口。
此參數控制需要檢測多少矩形(Neighbors)才能將窗口標記為面部。

minSize:寬度和高度(以像素為單位)的元組，表示窗口的最小尺寸。
小於此大小的邊界框將被忽略。從(30,30)開始並從那裡進行微調是一個好主意。

（1）cv2.WINDOW_NORMAL：視窗大小可改變。
（2）cv2.WINDOW_AUTOSIZE：視窗大小不可改變。
（3）cv2.WINDOW_FREERATIO：bai適應比例。
（4）cv2.WINDOW_KEEPRATIO：保持比例。


'''