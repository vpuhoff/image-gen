from skimage import io, color, feature
from skimage.filters import rank
import diskcache as dc
crops = dc.Cache('stage_1_images')
gray = dc.Cache('stage_2_gray_dataset')
from tqdm import tqdm
import cv2

def ToGray(img):
    return color.rgb2gray(img)

index = set(gray)

for crop in tqdm(crops):
    try:
        if crop not in gray:
            gray[crop] = ToGray(crops[crop])
    except KeyboardInterrupt:
        crops.close()
        gray.close()
        break
# glcm = feature.greycomatrix(grayImg, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4])
# print(glcm.shape) # (256, 256, 1, 4)

# rank.entropy(glcm, disk(5)) # throws an error since entropy expects a 2-D array in its arguments

# rank.entropy(grayImg, disk(5)) # given an output.