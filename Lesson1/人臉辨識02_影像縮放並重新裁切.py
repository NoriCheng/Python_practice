import numpy as np
import cv2 as cv


#  先讀檔
def imread_np(file1):
    # numpy.fromfile
    # Construct an array from data in a text or binary file.
    mem = np.fromfile(file1,dtype=np.uint8)     # mem 是一個一維陣列
    # cv.imdecode(	buf, flags	) ->	retval
    # Reads an image from a buffer in memory.
    cv_img = cv.imdecode(mem, cv.IMREAD_COLOR)  # flags:The same flags as in cv::imread
    return cv_img  # cv_img 變成了一個三維陣列


img = imread_np(r'source\市府班AI大頭貼\12鄭楷諭.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"

# 縮小照片
img = cv.resize(img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_AREA)

# 看圖並拉框決定人像範圍
dot1 = []                          # 記錄第一個座標
dot2 = []                          # 記錄第二個座標


# 滑鼠事件發生時要執行的函式
def show_xy(event,x,y,flags,param):
    global dot1, dot2, img         # 在函式內使用全域變數
    # 滑鼠拖曳發生時
    if flags == 1:  # cv2.EVENT_FLAG_LBUTTON	左鍵拖曳
        if event == 1:  # cv2.EVENT_LBUTTONDOWN	左鍵點擊
            dot1 = [x, y]          # 按下滑鼠時記錄第一個座標
        if event == 0:  # cv2.EVENT_MOUSEMOVE	滑動
            img2 = img.copy()      # 拖曳時不斷複製 img
            dot2 = [x, y]          # 拖曳時不斷更新第二個座標
            # 根據兩個座標繪製四邊形
            cv.rectangle(img2, (dot1[0], dot1[1]), (dot2[0], dot2[1]), (0,0,255), 2)
            # 不斷顯示新圖片 ( 如果不這麼做，會出現一堆四邊形殘影 )
            cv.imshow('openCV', img2)


cv.imshow('openCV', img)
cv.setMouseCallback('openCV', show_xy)  # 設定偵測事件的函式與視窗
cv.waitKey(0)     # 按下任意鍵停止
cv.destroyAllWindows()


# 將原影像切片並存成新影像
def imwrite_np(file1,img) :  # 存中文檔名
    # numpy.ndarray.tofile
    # Write array to a file as text or binary (default).
    # cv.imencode(	ext, img[, params]	) ->	retval, buf
    # Encodes an image into a memory buffer.
    try :
        cv.imencode(".png",img)[1].tofile(file1)
        return True
    except :
        return False


img2 = img[dot1[1]:dot2[1],dot1[0]:dot2[0],:]
imwrite_np('鄭楷諭.png', img2)

'''
當滑鼠在指定視窗中滑動進行某些行為，都會觸發一些事件，相關事件列表如下：
0	cv2.EVENT_MOUSEMOVE	滑動
1	cv2.EVENT_LBUTTONDOWN	左鍵點擊
2	cv2.EVENT_RBUTTONDOWN	右鍵點擊
3	cv2.EVENT_MBUTTONDOWN	中鍵點擊
4	cv2.EVENT_LBUTTONUP	左鍵放開
5	cv2.EVENT_RBUTTONUP	右鍵放開
6	cv2.EVENT_MBUTTONUP	中鍵放開
7	cv2.EVENT_LBUTTONDBLCLK	左鍵雙擊
8	cv2.EVENT_RBUTTONDBLCLK	右鍵雙擊
9	cv2.EVENT_MBUTTONDBLCLK	中鍵雙擊

除了事件，滑鼠的行為也會觸發一些 flag，相關 flag 列表如下：
1	cv2.EVENT_FLAG_LBUTTON	左鍵拖曳
2	cv2.EVENT_FLAG_RBUTTON	右鍵拖曳
4	cv2.EVENT_FLAG_MBUTTON	中鍵拖曳
8～15	cv2.EVENT_FLAG_CTRLKEY	按 Ctrl 不放事件
16～31	cv2.EVENT_FLAG_SHIFTKEY	按 Shift 不放事件
32～39	cv2.EVENT_FLAG_ALTKEY	按 Alt 不放事件
'''