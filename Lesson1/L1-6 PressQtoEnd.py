# ch1_5_1.py
import cv2

img = cv2.imread("jk.jpg")              # 讀取影像
cv2.imshow("MyPicture", img)            # 顯示影像
ret_value = cv2.waitKey(0)              # 無限等待
if ret_value == ord('Q') or ret_value == ord('q'):
    cv2.destroyWindow("MyPicture")      # 關閉視窗




 
