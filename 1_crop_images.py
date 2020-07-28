import diskcache as dc
cache = dc.Cache('stage_1_db')
crops = dc.Cache('stage_1_images')
from tqdm import tqdm
import glob, os
import cv2
size = 32
storage = "./images/"
os.chdir(storage)
step = 10
print(len(crops))
cached=set(list(cache))
for file in tqdm(glob.glob("*.*")):
    try:
        if not file in cached:
            img = cv2.imread(file)
            shape=img.shape
            h = shape[0]
            w = shape[1]
            for x in tqdm(range(0,w-size, step)):
                for y in range(0,h-size, step):
                    crop_img = img[y:y+size, x:x+size]
                    target = f"crop-{str(x)}-{str(y)}-{str(file)}"
                    crops[target]=crop_img
            cache[file]="OK"
    except KeyboardInterrupt:
        cache.close()
        break
    finally:
        pass
    