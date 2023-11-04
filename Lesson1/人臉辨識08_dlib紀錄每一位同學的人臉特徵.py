import dlib,cv2,numpy
from PIL import Image
from imutils import paths   # 更簡潔呼叫opencv，影象的平移，旋轉，縮放，骨架化
import pickle


def cv_imread(filepath) :
    cv_img = cv2.imdecode( numpy.fromfile(filepath,dtype=numpy.uint8) , cv2.IMREAD_UNCHANGED )
    return cv_img


def print_array_details(a):
    print('Dimensions: %d, shape: %s, dtype: %s'\
            %(a.ndim, a.shape, a.dtype))


predictor = "shape_predictor_68_face_landmarks.dat"  #人臉68特徵點模型
recogmodel = "dlib_face_recognition_resnet_model_v1.dat"  #人臉辨識模型

face_folder_path = r"source/市府班AI大頭貼"  # 內存中文姓名為檔名的jpg檔

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor)
facerec = dlib.face_recognition_model_v1(recogmodel)  #讀入人臉辨識模型

descriptors = []   #  存基準人頭的特徵矩陣
candidate = []     #  候選人姓名

for imagePath in paths.list_images(face_folder_path) :  # imutils模組提供的好用功能
    c = imagePath.strip(face_folder_path)[1:-4]
    candidate.append(c)

    # opencv
    # img_cv = cv_imread(imagePath)
    # print_array_details(img_cv) # Dimensions: 3, shape: (591, 437, 3), dtype: uint8

    # pil
    im_pil = Image.open(imagePath)
    im_pil_np = numpy.array(im_pil)  # 將影像變成 numpy

    rects = detector(im_pil_np, 1)

    for n,d in enumerate(rects):
        if n == 0 :
            shape = predictor(im_pil_np, d)  # 68特徵點偵測
            feature = facerec.compute_face_descriptor(im_pil_np, shape)  # 取得128維特徵向量
            descriptors.append( numpy.array(feature) )
            print(imagePath)  # ./source3\"Name".jpg  檢查大頭照是否會被測到二個頭

print(candidate)
print(len(descriptors))  # 23
print(type(descriptors))  # <class 'list'> 但是這個串列中的元素均為 <class 'numpy.ndarray'>
print_array_details(descriptors[0])     # Dimensions: 1, shape: (128,), dtype: float64

pickle_file1 = 'source/市府班AI大頭貼/staff_descriptors.pickle'
pickle_file2 = 'source/市府班AI大頭貼/staff_candidate.pickle'

with open(pickle_file1, 'wb') as f1:
    pickle.dump(descriptors, f1)

with open(pickle_file2, 'wb') as f2:
    pickle.dump(candidate, f2)