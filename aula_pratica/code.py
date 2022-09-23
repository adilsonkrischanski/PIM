from PIL import Image
# import pandas as pd
import cv2
import numpy as np
import matplotlib as plot


def limiar(img):
    ig = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    limiar, thresh2 = cv2.threshold(ig, 120, 255, cv2.THRESH_TOZERO)
    return thresh2


def ploting_graph(img):
    image= limiar(img)
    cv2.namedWindow('a', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('a', 800, 600)
    cv2.imshow('a', image)
    


if __name__ == "__main__":

    # open image
    img = cv2.imread("image.png")
    # cv2.imshow('image', img)
    ploting_graph(img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
