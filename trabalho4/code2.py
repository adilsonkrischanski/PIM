import numpy as np
from PIL import Image, ImageFilter
import matplotlib.pyplot as plt



class image():
    def __init__(self,path):
        # self.img = imread(path)
        self.img = Image.open(path)
        self.original = Image.open('folhas1.jpg')
        # self.img = imread(path)

    

    def fourier_masker_VerHor(self, i):
        image = self.img
        f_size = 15
        img = image.convert("L")
        dark_image_grey_fourier = np.fft.fftshift(np.fft.fft2(img))
        dark_image_grey_fourier[:580, 955:965] = i
        dark_image_grey_fourier[-580:,955:965] = i
        dark_image_grey_fourier[595:605, 0:930] = i
        dark_image_grey_fourier[595:605, 990:] = i
        fig, ax = plt.subplots(1,3,figsize=(15,15))
        ax[0].imshow(np.log(abs(dark_image_grey_fourier)), cmap='gray')
        ax[0].set_title('Masked Fourier', fontsize = f_size)
        ax[1].imshow(img, cmap = 'gray')
        ax[1].set_title('Greyscale Image', fontsize = f_size);
        ax[2].imshow(abs(np.fft.ifft2(dark_image_grey_fourier)), 
                        cmap='gray')
        ax[2].set_title('Transformed Greyscale Image', 
                        fontsize = f_size);


        
    def fourier_iterator(self, value_list):
        image = self.img
        for i in value_list:
            self.fourier_masker_VerHor(i)

    def fourier_transform_rgb(self, i):
        image = self.img
        f_size = 25
        transformed_channels = []
        image.convert()
        for i in range(3):
            rgb_fft = np.fft.fftshift(np.fft.fft2((image)))
            rgb_fft[:580, 955:965] = i
            rgb_fft[-580:,955:965] = i
            rgb_fft[595:605, 0:930] = i
            rgb_fft[595:605, 990:] = i
            transformed_channels.append(abs(np.fft.ifft2(rgb_fft)))
        
        final_image = np.dstack([transformed_channels[0].astype(int), 
                                transformed_channels[1].astype(int), 
                                transformed_channels[2].astype(int)])
    
        fig, ax = plt.subplots(1, 2, figsize=(17,12))
        ax[0].imshow(image)
        ax[0].set_title('Original Image', fontsize = f_size)
        ax[0].set_axis_off()
        plt.imshow(final_image)
        


if __name__== "__main__":

    img = image('folhas1_Reticulada.jpg')
    img.img = img.img.filter(ImageFilter.GaussianBlur)
    img.fourier_transform_rgb(1)
    # img.fourier_masker_VerHor(1)
    img.fourier_iterator([1,2,3,4,5])
    plt.show()