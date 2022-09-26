import numpy as np
import pandas as pd
import cv2

class color():
    def __init__(self, r, g, b, t): # t is percent
        self.r = self.calculate_limits(r,t)
        self.g = self.calculate_limits(g,t)
        self.b = self.calculate_limits(b,t)
      

    def calculate_limits(self, element, tolerance):
        min = 0
        max =255
        value_tolerance = int(255/tolerance)
        if element + value_tolerance < max:
            max = element +value_tolerance
        if element  - value_tolerance > min:
            min = element  - value_tolerance
        return (min,max)


    def limits(self, element):
        if element =='r':
            return (self.r)
        elif element =='g':
            return (self.g)
        elif element =='b':
            return (self.b)

CORES_DISPONIVEIS = {
    "RED": color(255,0,0,10),
    "GREEN": color(0,255,0,10),
    "BLUE": color(0,0,255,10),
    "WHITE": color(255,255,255,10),
    "BLACK": color(0,0,0, 10)
}

def checagem_pixel(img,cor):
    if cor not in CORES_DISPONIVEIS:
        return False

    b,g,r=cv2.split(img)

    for blue in b:
        for canal in blue:
            if canal < CORES_DISPONIVEIS[cor].limits('b')[0] or canal > CORES_DISPONIVEIS[cor].limits('b')[1]:
                return False

    for red in r:
        for canal in red:
            if canal < CORES_DISPONIVEIS[cor].limits('r')[0] or canal > CORES_DISPONIVEIS[cor].limits('r')[1]:
                return False
        
    for green in g:
        for canal in green:
            if canal < CORES_DISPONIVEIS[cor].limits('g')[0] or canal > CORES_DISPONIVEIS[cor].limits('g')[1]:
                return False

    return True
    

def media(matriz):
    ac= 0
    count =0
    for i in matriz:
        for j in i:
            ac+=j
            count+=1

    return int(ac/count)

def checagem_media(img,cor):
    if cor not in CORES_DISPONIVEIS:
        return False

    

    b,g,r=cv2.split(img)

    media_b = media(b)
    media_g = media(g)
    media_r = media(r)

    if media_b < CORES_DISPONIVEIS[cor].limits('b')[0] or media_b > CORES_DISPONIVEIS[cor].limits('b')[1]:
        return False
    if media_g < CORES_DISPONIVEIS[cor].limits('g')[0] or media_g > CORES_DISPONIVEIS[cor].limits('g')[1]:
        return False
    if media_r < CORES_DISPONIVEIS[cor].limits('r')[0] or media_r  > CORES_DISPONIVEIS[cor].limits('r')[1]:
        return False

    return True


if __name__=="__main__":

    cor_de_analize = "BLUE"
    img = cv2.imread("images/gray.bmp")
    print("HERE")
    if checagem_media(img,cor_de_analize ):
        print("Veiculo dentro dos padroes")
    else:
        print("Veiculo fora dos padros")

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    
    