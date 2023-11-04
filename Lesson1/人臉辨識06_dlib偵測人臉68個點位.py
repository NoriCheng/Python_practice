import numpy as np
import cv2                #影像處理模組 OpenCV
import dlib               #人臉識別模組 dlib

# dlib
detector = dlib.get_frontal_face_detector()    # 使用dlib模組提供的人臉偵測函式，基於HOG特徵，建立找尋人臉的物件
# cnn_face_detector = dlib.cnn_face_detection_model_v1('mmod_human_face_detector.dat')
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
# 人臉68個特徵形狀預測物件的產生，是基于 Ensemble of Regression Trees 理論


# cv2讀取影像
def cv2_imread(filepath):
    cv_img = cv2.imdecode( np.fromfile(filepath,dtype=np.uint8) , cv2.IMREAD_UNCHANGED )
    return cv_img


# img = cv2_imread(r"張代宜.png")
# img = cv2.imread(r'women1.png')
img = cv2.imread(r'12.jpg')

# 取灰度
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# 先看到人臉在甚麼地方
rects = detector(img_gray, 1) # 人臉方框的矩形左上右下座標
# 上面第二個參數：
# upsample_num_times：表示在進行偵測之前，要將圖片"放大"幾次；次數越多越能偵測到比較小的人臉，但花費的時間也更長
#dets = cnn_face_detector(img_gray, 0)
#rects1 = dlib.rectangles()
#rects1.extend([d.rect for d in dets])
#print(rects)
#print(rects1)


for i in range(len(rects)):
    landmarks = np.array([ [p.x, p.y]  for p in predictor( img, rects[i] ).parts() ])  #人臉關鍵點識別預測
    for idx, point in enumerate(landmarks):        #enumerate函式遍歷序列中的元素及它們的下標
        # 68點的座標
        pos = (point[0], point[1])
        #print(idx,pos)

        # 利用cv2.circle給每個特徵點畫一個圈，共68個
        cv2.circle(img, pos, 2, (255, 255, 255), -1)
        # 利用cv2.putText輸出1-68
        #font = cv2.FONT_HERSHEY_SIMPLEX
        #各引數依次是：圖片，新增的文字，座標，字型，字型大小，顏色，字型粗細
        #cv2.putText(img, str(idx+1), pos, font, 0.4, (0, 255, 255), 1 ,cv2.LINE_AA)

cv2.namedWindow("img", 0)
cv2.imshow("img", img)       #顯示影象
cv2.imwrite("linda2.jpg", img)
cv2.waitKey(0)        #等待按鍵，隨後退出