from img import Image
import matplotlib as plt
import cv2

if __name__=="__main__":
    img = Image('./imgs/img02.jpg') # set img path
    blur = img.my_gaussian_blur(img.img,3,1)
    x,y = img.sobel()
    G, theta = img.sobel_filters(x,y,blur)
    #G, theta = sobel_filters(gray_img)
    G = G.astype(int)
    theta = theta.astype(int)
    print(G)
    cv2.imshow('gray',G) # ta ai braia?? sabe o pq a img nao fica na tela  ??