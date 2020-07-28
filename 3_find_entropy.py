from skimage import io, color, feature
import numpy as np
import skimage
from skimage.filters import rank
import diskcache as dc
gray = dc.Cache('stage_2_gray_dataset')
entropy = dc.Cache('stage_3_entropy_dataset')
from tqdm import tqdm
import cv2
from skimage.feature import greycomatrix, greycoprops
distances = [1, 2, 3]
angles = [0, np.pi/4, np.pi/2, 3*np.pi/4]
properties = ['energy', 'homogeneity']
    
def GetGLCM(img):
    return greycomatrix(img, 
        distances=distances, 
        angles=angles,
        symmetric=True,
        normed=True)


index = set(entropy)
for key in tqdm(gray):
    if not key in index:
        entropy[key]=skimage.measure.shannon_entropy(gray[key])
        cv2.imshow(str(entropy[key]), gray[key])
        break
        

data = []
for key in tqdm(gray):
    data.append(entropy[key])
    
mink = min(data)
maxk = max(data)
avg = sum(data)/len(data)

n1 = 0
n2 = 0
for key in tqdm(gray):
    if entropy[key] >avg:
        n1 += 1 
    else:
        n2 += 1
print(n1,n2)
# glcm = feature.greycomatrix(grayImg, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4])
# print(glcm.shape) # (256, 256, 1, 4)

# rank.entropy(glcm, disk(5)) # throws an error since entropy expects a 2-D array in its arguments

# rank.entropy(grayImg, disk(5)) # given an output.