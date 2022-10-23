import cv2
from this import d
from math import sqrt, atan2
import numpy as np
from scipy import ndimage  # to install <sudo apt-get install python3-scipy>
from skimage.exposure import rescale_intensity
import matplotlib.pyplot as plt


class Image():
    def __init__(self, pathimage):
        self.img = self.img = cv2.imread(pathimage)
        self.neighbor_tam = 8
        self.w = self.img.shape[0]
        self.h = self.img.shape[1]

    scharr_x = np.array(([[-3, 0, 3], [-10, 0, 10], [-3, 0, 3]]),dtype="int")
    scharr_y = np.array(([[-3, -10, -3], [0, 0, 0], [3, 10, 3]]),dtype="int")

    prewitt_x = np.array(([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]),dtype="int")
    prewitt_y = np.array(([[-1, -1, -1], [0, 0, 0], [1, 1, 1]]),dtype="int")

    sobel_x = np.array(([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]), dtype="int")
    sobel_y = np.array(([[-1, -2, -1], [0, 0, 0], [1, 2, 1]]), dtype="int")

    hoop = np.array(([[-1, -1, -1], [-1, 8, -1 ], [-1, -1, -1]]), dtype="int" )



    def view_img(self, parametro):
        if parametro == 1:  # view base image
                gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
                out_x = self.convolve(gray, self.sobel_x)
                out_y = self.convolve(gray, self.sobel_y)
                grad_mag = np.sqrt(np.square(out_x) + np.square(out_y))
                grad_mag *= 255.0 / grad_mag.max()
                cv2.imshow("original", self.img)
                cv2.imshow("kernel_x", out_x)
                cv2.imshow("kernel_y", out_y)
                plt.imshow(grad_mag, cmap='gray')
                plt.title("Gradient Magnitude")
                plt.show()
                cv2.waitKey(0)
                cv2.destroyAllWindows() 
        elif parametro == 2:
                gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
                out_x = self.convolve(gray, self.prewitt_x)
                out_y = self.convolve(gray, self.prewitt_y)
                grad_mag = np.sqrt(np.square(out_x) + np.square(out_y))
                grad_mag *= 255.0 / grad_mag.max()
                cv2.imshow("original", self.img)
                cv2.imshow("kernel_x", out_x)
                cv2.imshow("kernel_y", out_y)
                plt.imshow(grad_mag, cmap='gray')
                plt.title("Gradient Magnitude")
                plt.show()
                cv2.waitKey(0)
                cv2.destroyAllWindows() 
        elif parametro == 3:
                gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
                out_x = self.convolve(gray, self.scharr_x)
                out_y = self.convolve(gray, self.scharr_y)
                grad_mag = np.sqrt(np.square(out_x) + np.square(out_y))
                grad_mag *= 255.0 / grad_mag.max()
                cv2.imshow("original", self.img)
                cv2.imshow("scharr_x", out_x)
                cv2.imshow("scharr_y", out_y)
                plt.imshow(grad_mag, cmap='gray')
                plt.title("Gradient Magnitude")
                plt.show()
                cv2.waitKey(0)
                cv2.destroyAllWindows() 
        elif parametro == 4:
                gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
                out_x = self.convolve(gray, self.hoop)
                out_y = self.convolve(gray, self.scharr_y)
                grad_mag = np.sqrt(np.square(out_x))
                grad_mag *= 255.0 / grad_mag.max()
                # cv2.imshow("original", self.img)
                cv2.imshow("hoop", out_x)
                # plt.imshow(grad_mag, cmap='gray')
                plt.title("Gradient Magnitude")
                plt.show()
                cv2.waitKey(0)
                cv2.destroyAllWindows() 
        else:
            print("i'm  sorry, try again")



    def convolve(self, image, kernel):
        (iH, iW) = image.shape[:2]
        (kH, kW) = kernel.shape[:2]
        pad = (kW - 1) // 2
        image = cv2.copyMakeBorder(image, pad, pad, pad, pad,
		cv2.BORDER_REPLICATE)
        output = np.zeros((iH, iW), dtype="float32")
        for y in np.arange(pad, iH + pad):
            for x in np.arange(pad, iW + pad):
                roi = image[y - pad:y + pad + 1, x - pad:x + pad + 1]
                k = (roi * kernel).sum()
                output[y - pad, x - pad] = k
        output = rescale_intensity(output, in_range=(0, 255))
        output = (output * 255).astype("uint8")
        return output
        
    def direcao(self, i, j):
        x,y = self.filter(filter)
        return atan2(y[i][j]/(x[i][j])+1*10**-8)

        

    