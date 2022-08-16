import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('foto.jpeg')
imgplot = plt.imshow(img)
plt.show()