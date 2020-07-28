from skimage import io, color, feature
import numpy as np
import skimage
from skimage.filters import rank
import diskcache as dc
gray = dc.Cache('stage_2_gray_dataset')
from tqdm import tqdm
import cv2
from skimage.feature import greycomatrix, greycoprops
import cv2
import numpy as np
from matplotlib import pyplot as plt
    
def GetGLCM(img):
    return greycomatrix(img, 
        distances=distances, 
        angles=angles,
        symmetric=True,
        normed=True)


#index = set(entropy)
for key in tqdm(gray):
    #if not key in index:
    #img = cv2.medianBlur(gray[key],5)
    th3 = cv2.adaptiveThreshold(gray[key],255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
    cv2.imshow(key, th3)
    cv2.waitKey(0)
    