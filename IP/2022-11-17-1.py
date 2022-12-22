# https://data-flair.training/blogs/numpy-features/

import cv2
import numpy as np

image = np.ones((500, 900, 3), np.uint8)  * 255 # 高再寬

imageK = np.zeros((300, 300, 3), np.uint8)
imageW = np.ones((300, 300, 3), np.uint8) * 255

image[100:400,100:400,:] = imageK
image[100:400,500:800,:] = imageW

#  左邊  加色法
imageR = np.zeros((300, 300), np.uint8)
imageG = np.zeros((300, 300), np.uint8)
imageB = np.zeros((300, 300), np.uint8)

cv2.circle(imageR,(100,100),100,255,-1)
cv2.circle(imageG,(200,100),100,255,-1)
cv2.circle(imageB,(150,200),100,255,-1)

image[100:400,100:400,2] = imageR
image[100:400,100:400,1] = imageG
image[100:400,100:400,0] = imageB

'''
for r in image[100:400,100:400] :
    for c in r :
        if c[0]==0 and c[1]==0 and c[2]==0 :
            c[0] = c[1] = c[2] = 255
'''

a = np.where((image[:450,:450,0]==0) & (image[:450,:450,1]==0) & (image[:450,:450,2]==0))
#print(a)
image[a] = (255,255,255)

# 右邊  減色法
imageR = np.ones((300, 300), np.uint8) * 255
imageG = np.ones((300, 300), np.uint8) * 255
imageB = np.ones((300, 300), np.uint8) * 255

cv2.circle(imageR,(100,100),100,0,-1)
cv2.circle(imageG,(200,100),100,0,-1)
cv2.circle(imageB,(150,200),100,0,-1)

image[100:400,500:800,2] = imageR
image[100:400,500:800,1] = imageG
image[100:400,500:800,0] = imageB

cv2.imshow("MyPicture", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

'''
ndarray.dtype：陣列元素型態。
ndarray.itemsize：陣列元素資料型態大小(或稱所佔空間)，單位是為位元組。
ndarray.ndim：陣列的維度。
ndarray.shape：陣列維度元素個數的元組，也可以用於調整陣列大小。
ndarray.size：陣列元素個數。

'''