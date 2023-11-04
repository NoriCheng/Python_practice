# -*- coding: utf-8 -*-
import dlib
import cv2

# 選擇第一隻攝影機
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# cap = cv2.VideoCapture('20230720_162403.mp4')

# 調整預設影像大小，預設值很大，很吃效能
# cap.set(cv2. CAP_PROP_FRAME_WIDTH, 1000)
# cap.set(cv2. CAP_PROP_FRAME_HEIGHT, 1000)

# 取得預設的臉部偵測器
detector = dlib.get_frontal_face_detector()
# 根據shape_predictor方法載入68個特徵點模型，此方法為人臉表情識別的偵測器
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

# 當攝影機打開時，對每個frame進行偵測

while True:
    # 讀出frame資訊
    _, frame = cap.read()
    # frame = cv2.flip(frame,0)

    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_rects = detector(img_gray, 0)

    # 取出偵測的結果
    for d in face_rects:
        x1 = d.left()
        y1 = d.top()
        x2 = d.right()
        y2 = d.bottom()

        # 繪製出偵測人臉的矩形範圍
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2, cv2.LINE_AA)

        # 找出特徵點位置
        shape = predictor(img_gray, d)

        # 繪製68個特徵點
        for i in range(68):
            cv2.circle(frame, (shape.part(i).x, shape.part(i).y), 2, (255, 255, 255), 2)

    # 輸出到畫面
    cv2.namedWindow('Face Detection', 0)
    cv2.imshow("Face Detection", frame)

    # 如果按下ESC键，就退出
    if cv2.waitKey(10) == 27:
        break

# 釋放記憶體
cap.release()
# 關閉所有視窗
cv2.destroyAllWindows()