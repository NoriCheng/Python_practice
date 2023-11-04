import cv2

# 載入分類器
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
# 讀取圖片
img = cv2.imread(r'source/231104_2.jpg')
# 轉成灰階圖片
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 偵測臉部
faces = face_cascade.detectMultiScale(gray,     # 要識別的圖檔(灰階)
                                      scaleFactor=1.05,     # 每次偵測的比例
                                      minNeighbors=5,       # 成功取得特徵須達幾次
                                      minSize=(30, 30),     # 偵測的最小範圍
                                      flags=cv2.CASCADE_SCALE_IMAGE     #
                                      )
'''
flags:default=0
CASCADE_DO_CANNY_PRUNING=1：利用 Canny 邊緣檢測器來排除一些邊緣很少或者很多的區域
CASCADE_SCALE_IMAGE=2：案比例正常檢測
CASCADE_FIND_BIGGEST_OBJECT=4：只檢測最大的物體
CASCADE_DO_ROUGH_SEARCH=8：初略檢測
'''


# 繪製人臉部份的方框
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
# (0, 255, 0)欄位可以變更方框顏色(Blue,Green,Red)

# 顯示成果
cv2.namedWindow('img', cv2.WINDOW_NORMAL)  # 正常視窗大小
cv2.imshow('img', img)                     # 秀出圖片
cv2.imwrite( "result.jpg", img )           # 保存圖片
cv2.waitKey(0)                             # 等待按下任一按鍵
cv2.destroyAllWindows()                    # 關閉視窗
