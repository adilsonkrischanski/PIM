import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imshow
from skimage.color import rgb2hsv, rgb2gray, rgb2yuv
from skimage import color, exposure, transform
from skimage.exposure import equalize_hist

class image():
    def __init__(self,path):
        self.img = imread(path)

    

    def fourier_masker_ver(self, i):
        image = self.img
        f_size = 15
        dark_image_grey_fourier = np.fft.fftshift(np.fft.fft2(rgb2gray(image)))
        dark_image_grey_fourier[:225, 235:240] = i
        dark_image_grey_fourier[-225:,235:240] = i
        fig, ax = plt.subplots(1,3,figsize=(15,15))
        ax[0].imshow(np.log(abs(dark_image_grey_fourier)), cmap='gray')
        ax[0].set_title('Masked Fourier', fontsize = f_size)
        ax[1].imshow(rgb2gray(image), cmap = 'gray')
        ax[1].set_title('Greyscale Image', fontsize = f_size);
        ax[2].imshow(abs(np.fft.ifft2(dark_image_grey_fourier)), 
                        cmap='gray')
        ax[2].set_title('Transformed Greyscale Image', 
                        fontsize = f_size);


    def fourier_masker_hor(self, i):
        image = self.img
        f_size = 15
        dark_image_grey_fourier = np.fft.fftshift(np.fft.fft2(rgb2gray(image)))
        dark_image_grey_fourier[235:240, :230] = i
        dark_image_grey_fourier[235:240,-230:] = i
        fig, ax = plt.subplots(1,3,figsize=(15,15))
        ax[0].imshow(np.log(abs(dark_image_grey_fourier)), cmap='gray')
        ax[0].set_title('Masked Fourier', fontsize = f_size)
        ax[1].imshow(rgb2gray(image), cmap = 'gray')
        ax[1].set_title('Greyscale Image', fontsize = f_size);
        ax[2].imshow(abs(np.fft.ifft2(dark_image_grey_fourier)), 
                        cmap='gray')
        ax[2].set_title('Transformed Greyscale Image', 
                        fontsize = f_size);
        
    def fourier_iterator(self, value_list):
        image = self.img
        for i in value_list:
            self.fourier_masker_ver(i)

    def fourier_transform_rgb(self):
        image = self.img
        f_size = 25
        transformed_channels = []
        for i in range(3):
            rgb_fft = np.fft.fftshift(np.fft.fft2((image[:, :, i])))
            rgb_fft[:225, 235:237] = 1
            rgb_fft[-225:,235:237] = 1
            transformed_channels.append(abs(np.fft.ifft2(rgb_fft)))
        
        final_image = np.dstack([transformed_channels[0].astype(int), 
                                transformed_channels[1].astype(int), 
                                transformed_channels[2].astype(int)])
    
        fig, ax = plt.subplots(1, 2, figsize=(17,12))
        ax[0].imshow(image)
        ax[0].set_title('Original Image', fontsize = f_size)
        ax[0].set_axis_off()
        


if __name__== "__main__":

    img = image('mandril.jpg')
    img.fourier_transform_rgb()
    img.fourier_masker_ver(5)
    img.fourier_masker_hor(5)
    img.fourier_iterator([1,2,3,4,5])
    plt.show()