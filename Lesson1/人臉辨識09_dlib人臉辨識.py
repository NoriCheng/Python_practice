import dlib, numpy
from PIL import Image, ImageDraw, ImageFont
import pickle

font_file = "NotoSansCJKtc-Regular.otf"  # 思源黑體
_font = ImageFont.truetype(font_file,10) # PIL


def print_array_details(a):
    print('Dimensions: %d, shape: %s, dtype: %s' % (a.ndim, a.shape, a.dtype))


pickle_file1 = 'source/市府班AI大頭貼/staff_descriptors.pickle'
pickle_file2 = 'source/市府班AI大頭貼/staff_candidate.pickle'

with open(pickle_file1, 'rb') as f1:
    descriptors = pickle.load(f1)  # 存13個 基準人頭的特徵矩陣，每一個元素都是 numpy

with open(pickle_file2, 'rb') as f2:
    candidate = pickle.load(f2)    # 候選人姓名

predictor = "shape_predictor_68_face_landmarks.dat"  #人臉68特徵點模型
recogmodel = "dlib_face_recognition_resnet_model_v1.dat"  #人臉辨識模型

img_path = r"source/231104_2.jpg"  # 班級點名截圖

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor)
facerec = dlib.face_recognition_model_v1(recogmodel)  #讀入人臉辨識模型

im_pil = Image.open(img_path)
im_pil_np = numpy.array(im_pil)
rects = detector(im_pil_np, 1) # 23

dist = []
dict_face_dist = {}
for n, d in enumerate(rects):
    shape = predictor(im_pil_np, d)  # 特徵點偵測
    feature = facerec.compute_face_descriptor(im_pil_np, shape)  # 取得128維特徵向量
    d_test = numpy.array(feature)    # 128維特徵向量轉成 numpy
    # 計算歐式距離
    for item in descriptors:
        dist_ = numpy.linalg.norm(item - d_test)
        dist.append(dist_)
    dict_face_dist[n] = [(d.left(),d.top(),d.right(),d.bottom()),dist]
    dist = []

# for key,value in dict_face_dist.items():
#    print(f'{key}  {value}')
#    0  [(1166, 725, 1274, 832), [0.56, 0.64, 0.52, 0.62, 0.55, 0.68, 0.58, 0.61, 0.59, 0.62, 0.49, 0.59, 0.61]]

draw = ImageDraw.Draw(im_pil)
for n,key in enumerate(dict_face_dist):

    # 將比對人名和比對出來的歐式距離組成一個dict
    c_d = dict(zip(candidate, dict_face_dist[key][1]))
    # 根據歐式距離由小到大排序
    cd_sorted = sorted(c_d.items(), key=lambda d: d[1])

    rec_name = cd_sorted[0][0] # + str(n)
    # rec_name = cd_sorted[0][0] + str(round(cd_sorted[0][1],2))
    print(f'{str(key) + cd_sorted[0][0]:10s} {round(cd_sorted[0][1],2)}')
    if round(cd_sorted[0][1],2) <= 0.99 :
        left = dict_face_dist[key][0][0]
        top = dict_face_dist[key][0][1]
        right = dict_face_dist[key][0][2]
        bottom = dict_face_dist[key][0][3]
        draw.rectangle(((left, top), (right, bottom)), outline='blue')
        # txt_w, txt_h = draw.textsize(rec_name, font=_font)
        draw.rectangle(((left, bottom), (right, bottom + 20 + 10)), fill='blue', outline='blue')
        draw.text((left + 8, bottom + 5), rec_name, fill='white', font=_font)

im_pil.show()
im_pil.save("辨識結果.jpg")


'''
linalg = linear（线性）+ algebra（代数），norm则表示范数。
首先需要注意的是范数是对向量（或者矩阵）的度量，是一个标量（scalar）：

函数参数
x_norm=np.linalg.norm(x, ord=None, axis=None, keepdims=False)
x: 表示矩阵（也可以是一维）
ord：范数类型  內定 sqrt(x1**2+x2**2+...)
'''