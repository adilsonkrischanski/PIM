#@adilson krischanski
import numpy as np
import cv2
img=cv2.imread('figuraEscura.jpg')
#display an image
cv2.imshow('image',img)
b,g,r=cv2.split(img)
cv2.imshow('b',b)
cv2.imshow('g',g)
cv2.imshow('r',r)
cv2.waitKey(0)
cv2.destroyAllWindows()