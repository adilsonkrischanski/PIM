import cv2
from math import sqrt, atan2
import numpy as np
from scipy import ndimage # to install <sudo apt-get install python3-scipy>

from pixel import Pixel

class Image():
    def __init__(self, pathimage):
        self.img = self.img = cv2.imread(pathimage)
        self.neighbor_tam = None
        self.matrix = None
        self.img_grad = None
        self.w = self.img.shape[0]
        self.h = self.img.shape[1]

    def set_neighbor_tam(self, tam):
        self.neighbor_tam = tam

    def view_img(self, parametro):
        if parametro == 1:  # view base image
            cv2.namedWindow('Base Image', cv2.WINDOW_NORMAL)
            cv2.resizeWindow('Base Image', 800, 600)
            cv2.imshow('Base Image', self.img)
        elif parametro == 2:
            cv2.namedWindow('Limiar Image', cv2.WINDOW_NORMAL)
            cv2.resizeWindow('Limiar Image', 800, 600)
            cv2.imshow('Limiar Image', self.img_limiar)
            cv2.imwrite('img_limiar.jpg', self.img_limiar)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def prewitt(self):
        x = [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]
        y = [[-1, -1, -1], [0, 0, 0], [1, 1, 1]]
        return x,y

    def sobel(self):  
        x = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
        y = [[-1,-2,-1], [0, 0, 0], [1, 2, 1]]
        return x,y

    def scharr(self):  
        x = [[-3, 0, 3], [-10, 0, 10], [-3, 0, 3]]
        y = [[-3, -10, -3], [0, 0, 0], [3, 10, 3]]
        return x,y

    def filter(self, param): #param 1(prewitt) 2(Sobel) 3(scharr)
        x= None
        y = None
        if param == 1:
            x, y = self.prewitt()
        elif param == 2:
            x, y = self.sobel
        elif param == 3:
            x, y = self.scharr()
        
        
    def magnetude(self, i, j, filter):
        x,y = self.filter(filter)
        return sqrt(x[i][j]**2+y[i][j]**2)

    def direcao(self, i, j):
        x,y = self.filter(filter)
        return atan2(y[i][j]/(x[i][j])+1*10**-8)

    def sobel_filters(self, x, y, image):
        Kx = np.array(x, np.float32)
        Ky = np.array(y, np.float32)
    
        Ix = ndimage.filters.convolve(image, Kx)
        Iy = ndimage.filters.convolve(image, Ky)
    
        G = np.hypot(Ix, Iy)
        G = G / G.max() * 255
        theta = np.arctan2(Iy, Ix)
        return (G, theta)

    def neighbor(self):
        pass
        

