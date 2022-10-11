import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

baboon = cv2.imread('baboon.png', cv2.IMREAD_COLOR)
rgb = cv2.imread('rgb.png', cv2.IMREAD_COLOR)
rgbcube = cv2.imread('rgbcube_kBKG.png', cv2.IMREAD_COLOR)

# Imagem sem metadata ou icc profile, assumindo espaço de cores padrão
print(baboon.shape)
print(rgb.shape)
print(rgbcube.shape)

def plot_channels(img, colorspace):
    plt.clf()
    plt.cla()
    plt.close()
    
    n_channels = img.shape[-1]
    
    for i in range(n_channels):
        plt.subplot(1, n_channels, i + 1)
        plt.imshow(img[:, :, i], cmap = 'gray')
        plt.title(f"{colorspace} Canal {i}")

    plt.show()
    
def BGR2HSI(img):
    imgf = img.astype(float) / 255.0
    B, G, R = imgf[:,:,0], imgf[:,:,1], imgf[:,:,2]
    I = (B+G+R) / 3
    S = 1 - 3 * np.divide(np.minimum(B, G, R), B+G+R)
    H = np.arccos(np.divide( 0.5*((R-G) + (R-B)), np.sqrt(np.power(R-G, 2) + np.multiply(R-B, G-B)) ))
    H[B > G] = 2*np.pi - H[B > G]
    
    return np.dstack((H, S, I))

def RGB2YIQ(img):
    imgf = img.astype(float) / 255.0
    B, G, R = imgf[:,:,0], imgf[:,:,1], imgf[:,:,2]
    Y = 0.299*R + 0.587*G + 0.114*B
    I = 0.596*R - 0.274*G - 0.322*B
    Q = 0.211*R - 0.523*G + 0.312*B
    
    return np.dstack((Y, I, Q))
    
plot_channels(baboon.copy(), 'BGR')
plot_channels(rgb.copy(), 'BGR')
plot_channels(rgbcube.copy(), 'BGR')

plot_channels(RGB2YIQ(baboon.copy()), 'NTSC')
plot_channels(RGB2YIQ(rgb.copy()), 'NTSC')
plot_channels(RGB2YIQ(rgbcube.copy()), 'NTSC')

plot_channels(cv2.cvtColor(baboon.copy(), cv2.COLOR_BGR2HSV), 'HSV')
plot_channels(cv2.cvtColor(rgb.copy(), cv2.COLOR_BGR2HSV), 'HSV')
plot_channels(cv2.cvtColor(rgbcube.copy(), cv2.COLOR_BGR2HSV), 'HSV')

plot_channels(BGR2HSI(baboon.copy()), 'HSI')
plot_channels(BGR2HSI(rgb.copy()), 'HSI')
plot_channels(BGR2HSI(rgbcube.copy()), 'HSI')

plot_channels(cv2.cvtColor(baboon.copy(), cv2.COLOR_BGR2LAB), 'LAB')
plot_channels(cv2.cvtColor(rgb.copy(), cv2.COLOR_BGR2LAB), 'LAB')
plot_channels(cv2.cvtColor(rgbcube.copy(), cv2.COLOR_BGR2LAB), 'LAB')

plot_channels(cv2.cvtColor(baboon.copy(), cv2.COLOR_BGR2XYZ), 'CIE XYZ')
plot_channels(cv2.cvtColor(rgb.copy(), cv2.COLOR_BGR2XYZ), 'CIE XYZ')
plot_channels(cv2.cvtColor(rgbcube.copy(), cv2.COLOR_BGR2XYZ), 'CIE XYZ')

plot_channels(np.array(Image.open('baboon.png').convert('CMYK')), 'CMYK')
plot_channels(np.array(Image.open('rgb.png').convert('CMYK')), 'CMYK')
plot_channels(np.array(Image.open('rgbcube_kBKG.png').convert('CMYK')), 'CMYK')