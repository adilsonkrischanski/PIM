import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2 

from skimage import data, io, filters, color 


path = 'figuraEscura.jpg'
arquivo_saida = 'output_image.jpg'


# img_read=cv2.imread(path)
# r,g,b=cv2.split(img_read)

img = io.imread(path) # [:,:,:3]
print(img)
# print(img)
img_rgb=img

img_np = np.asarray(img_rgb, np.uint8)

yiq =  color.rgb2yiq(img).reshape(-1, 3)
print(yiq)

# io.imshow(img)
# plt.show()
