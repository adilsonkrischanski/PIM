import numpy as np
from PIL import Image

path = 'figuraEscura.jpg'
arquivo_saida = 'output_image.jpg'

img = Image.open(path)

img_cinza = img.convert('L')

img_array = np.asarray(img_cinza)

histo = np.bincount(img_array.flatten(), minlength=256)

n_pixels = np.sum(histo)

histo = histo/n_pixels

c_histo = np.cumsum(histo)

transf = np.floor(255 * c_histo).astype(np.uint8)

img_lista = list(img_array.flatten())


out_img_lista = [transf[p] for p in img_lista]

out_img_array = np.reshape(np.asarray(out_img_lista), img_array.shape)

eq_img = Image.fromarray(out_img_array, mode='L')

eq_img.save(arquivo_saida)