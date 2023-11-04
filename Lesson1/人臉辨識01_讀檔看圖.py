import numpy as np
import cv2 as cv

from PIL import Image, ImageDraw
img = Image.open(r'source\市府班AI大頭貼\12鄭楷諭.jpg')
draw = ImageDraw.Draw(img)
draw.line((0, 0) + img.size, fill=128)
draw.line((0, img.size[1], img.size[0], 0), fill=128)

# img = np.array(img)[:,:,::-1] # 變成 ndarray 符合 ＢＧＲ 要求
# img = Image.fromarray(img)  # 變成 ImageObject
img.show()

# def imread_np(file1) :
#     mem = np.fromfile(file1,dtype=np.uint8)
#     cv_img = cv.imdecode(mem,1)
#     return cv_img
#
# img = imread_np(r'source\市府班AI大頭貼\12鄭楷諭.jpg')
# # img = cv.imread(r'source\市府班AI大頭貼\12鄭楷諭.jpg')
# # img = cv.imread(r'imgs\face10.jpg')
# # img = imread_np(r'imgs\face10.jpg')
# assert img is not None, "file could not be read, check with os.path.exists()"

cv.namedWindow('img',0)
cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()
