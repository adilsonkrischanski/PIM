from cProfile import label
from PIL import Image
# import pandas as pd
import cv2
import numpy as np
import matplotlib as plot


class Pixel():
    def __init__(self, value, i, j):
        self.i = i
        self.j = j
        self.rot = 0
        self.value = value

    def is_marked(self):
        return self.rot != 0

    def to_string(self):
        return f"posicao{self.i}:{self.j} valor{self.value} lable = {self.rot}"


class Image():
    def __init__(self, pathimage):
        self.img = self.img = cv2.imread(pathimage)
        self.matrix = None
        self.img_limiar = None
        self.limiar = None
        self.value = 0.0
        self.w = self.img.shape[0]
        self.h = self.img.shape[1]
        self.lables = None

    def limiar_convert(self):
        ig = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        limiar, thresh2 = cv2.threshold(ig, 120, 255, cv2.THRESH_BINARY)
        self.limiar = limiar
        self.img_limiar = thresh2

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

    def rotulation(self):
        print(self.w, self.h)
        direcao = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        pilha = [Pixel(0, 1, 1)]
        rot = 1
        for h in range(1, self.w-1):
            # print(f"\033[1;31mFOR 54\033[0;0m")
            for w in range(1, self.h-1):
                # print(f"\033[1;31mFOR 56\033[0;0m")
                print(f"pos {w}:{h} matrix valor = {self.matrix[w][h].value}")
                # print(self.matrix[w][h].value)
                if self.matrix[w][h].value == 0 and not self.matrix[w][h].is_marked():
                    self.matrix[w][h].rot = rot
                    pilha.append(self.matrix[w][h])
                    while len(pilha) != 0:
                        # print(f"\033[1;31mWHILE 62\033[0;0m")

                        for x in direcao:
                            aux_h = h + x[0]
                            aux_w = w + x[1]
                            if not self.matrix[aux_w][aux_h].is_marked() and self.matrix[aux_w][aux_h].value == 0:
                                pilha.append(self.matrix[aux_w][aux_h])
                                # print("append")
                        aux = pilha.pop()
                        # print("pop")
                        print(aux.to_string())
                        h = aux.j
                        w = aux.i
                        self.matrix[w][h].rot = rot
                    rot += 1
                    # print(f"\033[1;31mSAI DO WHILE\033[0;0m")

    def objectify(self):
        mat = []
        for i in range(0, self.h):
            line = []
            for j in range(0, self.w):
                pixel = Pixel(self.img_limiar[j][i], i, j)
                line.append(pixel)
            mat.append(line)
        self.matrix = mat

    def calculate_rots(self):  #
        self.lables = dict()
        for line in self.matrix:
            for pixel in line:
                if pixel.rot in self.lables:
                    quant = self.lables[pixel.rot]
                    self.lables[pixel.rot] = (quant+1)
                else:
                    self.lables[pixel.rot] = 1

        print(self.lables)

    def caculate_value(self):
        total = 0.0
        for i in self.lables.keys():
            print(i)
            print(self.lables[i])
            if self.lables[i] >= 130000 and self.lables[i] <= 150000:
                total += 0.05
                print("to aqui ")
            elif self.lables[i] >= 160000 and self.lables[i] <= 200000:
                total += 1.00
                print("agr to aqui")
        print("lancando o retorno", total)
        return total


class Moeda():
    def __init__(self, valor, mim_pixel, max_pixel):
        self.valor = valor
        self.min_pixel = mim_pixel
        self.max_pixel = max_pixel


# MOEDAS = {1.00: Moeda(1.00, 16000, 20000),
#           0.10: Moeda(0.10, 13500, 15.500)}


if __name__ == "__main__":

    image_path = 'foto.jpg'
    img = Image(image_path)
    img.limiar_convert()
    img.view_img(1)
    img.view_img(2)
    img.objectify()
    img.rotulation()
    img.calculate_rots()
    print(f"Total de R${img.caculate_value()}")
