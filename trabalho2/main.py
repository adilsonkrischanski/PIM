from img import Image
import matplotlib.pyplot as plt
import cv2
import numpy as np

if __name__=="__main__":
    img = Image('./imgs/chessboard_inv.png')
    # img.view_img(1)
    # img.view_img(2)
    # img.view_img(3)
    # img.view_img(4)

    img_1 = Image('./imgs/Lua1_gray.jpg')
    # img_1.view_img(1)
    # img_1.view_img(2)
    # img_1.view_img(3)
    # img_1.view_img(4)

    img_2 = Image('./imgs/img02.jpg')
    # img_2.view_img(1)
    # img_2.view_img(2)
    # img_2.view_img(3)
    img_2.view_img(4)

    
    