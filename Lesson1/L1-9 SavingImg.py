# ch1_7.py
import cv2
cv2.namedWindow("MyPicture")            # 使用預設
img = cv2.imread("jk.jpg")              # 彩色讀取
cv2.imshow("MyPicture", img)            # 顯示影像img
ret = cv2.imwrite("out1_7_1.tiff", img) # 將檔案寫入out1_7_1.tiff
if ret:
    print("儲存檔案成功")
else:
    print("儲存檔案失敗")
ret = cv2.imwrite("out1_7_2.png", img)  # 將檔案寫入out1_7_2.png
if ret:
    print("儲存檔案成功")
else:
    print("儲存檔案失敗")
cv2.waitKey(3000)                       # 等待3秒
cv2.destroyAllWindows()                 # 刪除所有視窗






 
