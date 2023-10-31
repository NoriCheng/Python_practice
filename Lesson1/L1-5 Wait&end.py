# ch1_5.py
import cv2

img = cv2.imread("jk.jpg")              # 讀取影像
cv2.imshow("MyPicture", img)            # 顯示影像
ret_value = cv2.waitKey(5000)           # 等待 5 秒
cv2.destroyWindow("MyPicture")          # 關閉視窗
print(f"ret_value = {ret_value}")





 
