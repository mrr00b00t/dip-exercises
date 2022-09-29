import cv2
import numpy as np
from matplotlib import pyplot as plt
import argparse


parser = argparse.ArgumentParser(description="Script for frequency filtering exercises.",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("-i", "--input", help="Path for the desired image", type=str, default="./lena.png")
args = parser.parse_args()

config = vars(args)

img_path = config['input']

img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
img_fft = np.fft.fft2(img)
img_shifted = np.fft.fftshift(img_fft)
scaled = 20*np.log(np.abs(img_shifted))

img_real, img_imag, img_abs = np.real(img_fft), np.imag(img_fft), np.abs(img_fft)
img_real_shifted, img_imag_shifted, img_abs_shifted = np.real(img_shifted), np.imag(img_shifted), np.abs(img_shifted)

# load with np.load("<filename>.npy")
np.save("img_fft_real", img_real), np.save("img_fft_imag", img_imag), np.save("img_fft_abs", img_abs)
np.save("img_fft_shifted_real", img_real_shifted), np.save("img_fft_shifted_imag", img_imag_shifted), np.save("img_fft_shifted_abs", img_abs_shifted)

h_center, w_center = img.shape[0]//2 , img.shape[1]//2
bound = 25

# LOW PASS FILTER: exclude higher frequencies
img_shifted_low_pass = img_shifted.copy()
img_shifted_low_pass[h_center+bound+1:, :] = 0
img_shifted_low_pass[:h_center-bound, :] = 0
img_shifted_low_pass[:, w_center+bound+1:] = 0
img_shifted_low_pass[:, :w_center-bound] = 0
img_ishifted_low_pass = np.fft.ifftshift(img_shifted_low_pass)
img_ifft_low_pass = np.fft.ifft2(img_ishifted_low_pass)
img_low_pass = np.real(img_ifft_low_pass)

# HIGH PASS FILTER: exclude lower frequencies
img_shifted_high_pass = img_shifted.copy()
img_shifted_high_pass[h_center-bound:h_center+bound+1, w_center-bound:w_center+bound+1] = 0
img_ishifted_high_pass = np.fft.ifftshift(img_shifted_high_pass)
img_ifft_high_pass = np.fft.ifft2(img_ishifted_high_pass)
img_high_pass = np.real(img_ifft_high_pass)

plt.subplot(2, 2, 1)
plt.imshow(img, cmap = 'gray')
plt.title("Lena")
plt.subplot(2, 2, 2)
plt.imshow(scaled, cmap = 'gray')
plt.title("FFT -> shift -> scale of Lena: \nWhiter at center means more \nlow frequencies than higher frequencies")
plt.subplot(2, 2, 3)
plt.imshow(img_low_pass, cmap = 'gray')
plt.title("Lena LOW PASS filtered")
plt.subplot(2, 2, 4)
plt.imshow(img_high_pass, cmap = 'gray')
plt.title("Lena HIGH PASS filtered")
plt.show()