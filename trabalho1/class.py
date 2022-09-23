from re import M
from PIL import Image
# import pandas as pd
import cv2
import numpy as np
import matplotlib as plot


class pixel():
    def __init__(self):
        self.marked = None
        self.rot = None
        self.value = None

    def is_marked(self):
        if self.marked == 1:
            return 1
        return 0


class image():
    def __init__(self):
        self.img = None
        self.matrix = None
        self.img_limiar = None
        self.limiar = None

    def read_image(self, pathimage):
        self.img = cv2.imread(pathimage)

    def limiar_convert(self):
        ig = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        limiar, thresh2 = cv2.threshold(ig, 120, 255, cv2.THRESH_BINARY)
        self.limiar = limiar
        self.img_limiar = thresh2

    def create_mat(self):
        m = self.img.shape[0]
        n = self.img.shape[1]
        linha = []
        for i in range(0, n):
            linha.append(pixel())
        mat = []
        for i in range(0, m):
            mat.append(linha)
        self.matrix = mat

    def view_img(self, parametro):
        if parametro == 1:  # view base image
            cv2.namedWindow('Base Image', cv2.WINDOW_NORMAL)
            cv2.resizeWindow('Base Image', 800, 600)
            cv2.imshow('Base Image', self.img)
        elif parametro == 2:
            cv2.namedWindow('Limiar Image', cv2.WINDOW_NORMAL)
            cv2.resizeWindow('Limiar Image', 800, 600)
            cv2.imshow('Limiar Image', self.img_limiar)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def rotulation(self):  # TODO
        pass

    def calcate_value(self):  # TODO
        pass

    def plot_limiar_grapf(self):  # TODO
        pass


if __name__ == "__main__":
    # PARAMS
    image_path = 'foto.jpg'

    img = image()
    img.read_image(image_path)
    img.create_mat()
    img.limiar_convert()
    img.view_img(1)
    img.view_img(2)
