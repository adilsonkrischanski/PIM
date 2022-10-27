from pickletools import uint8
from time import process_time_ns
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2 
from skimage import data, io, filters, color 


path = './imgs/outono_LC.png'
arquivo_saida = 'output_image.jpg'


# img_read=cv2.imread(path)
# r,g,b=cv2.split(img_read)

img = io.imread(path) # [:,:,:3]

img_np = np.asarray(img, np.uint8)

yiq =  color.rgb2yiq(img)

y, i, q = cv2.split(yiq)


img_array = np.asarray(y)

arraycerto = []
for x in img_array:
    aux =[]
    for j in x:
        j=int(j*1000)
        aux.append(j)
    arraycerto.append(aux)

arraycerto = np.asarray(arraycerto, np.uint8)

histo = np.bincount(arraycerto.flatten(), minlength=256)

n_pixels = np.sum(histo)

histo = histo/n_pixels

c_histo = np.cumsum(histo)

transf = np.floor(255 * c_histo).astype(np.uint8)

img_lista = list(arraycerto.flatten())

#merge e  mudar
mudado = []

for x in transf:
    j=j/1000
    mudado.append(j)

mudado = np.asarray(mudado, np.float64)
img_saida = cv2.merge([mudado,i,q])
rgb = color.yiq2rgb(img_saida)


out_img_lista = [rgb[p] for p in img_lista]

out_img_array = np.reshape(np.asarray(out_img_lista), arraycerto.shape)

eq_img = Image.fromarray(out_img_array, mode='L')

eq_img.save(arquivo_saida)
