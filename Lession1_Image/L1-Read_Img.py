# ch1_1.py
import cv2

img1 = cv2.imread("jk.jpg")                 # 讀取影像
print(f"成功讀取 : {type(img1)}")
img2 = cv2.imread("none.jpg")               # 讀取影像
print(f"讀取失敗 : {type(img2)}")



 
