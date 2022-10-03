import cv2

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

    

    def prewitt(self): # Todo
        pass

    def Sobel(self):  # todo 
        pass

    def scharr(self): # todo 
        pass

    
    

    