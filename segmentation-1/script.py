import cv2
import numpy as np
from matplotlib import pyplot as plt
 
def imsave(path, img1, cmap):
    img2 = img1.copy()
    img2 = img2.astype(np.float64)
    
    minv, maxv = np.min(img2), np.max(img2)
    
    img2 = (img2 - minv) / (maxv - minv)
    img2 = (img2 * 255).astype('uint8')
    plt.imsave(path, img2, cmap=cmap)
 
img = cv2.imread('building.tif', cv2.IMREAD_GRAYSCALE)

img = img.astype(np.float64) / np.max(img)

ykernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
xkernel = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
avgkernel = np.ones((5, 5)) / 25

gx = cv2.filter2D(img.copy(), -1, xkernel)
gy = cv2.filter2D(img.copy(), -1, ykernel)

alpha = np.arctan2(gy, gx)

cv2.imshow("building", img)
cv2.imshow("building |Gx|", np.abs(gx))
imsave('building-|Gx|.png', np.abs(gx), cmap='gray')
cv2.imshow("building |Gy|", np.abs(gy))
imsave('building-|Gy|.png', np.abs(gy), cmap='gray')
cv2.imshow("building |Gx| + |Gy|", np.abs(gy) + np.abs(gx))
imsave('building-|Gy|+|Gy|.png', np.abs(gy) + np.abs(gx), cmap='gray')
cv2.imshow("alpha = tan-1(Gy/Gx)", alpha)
imsave('building-tan-1GyGx.png', alpha, cmap='gray')

avg = cv2.filter2D(img.copy(), -1, avgkernel)
avg = avg.astype(np.float64) / np.max(avg)

avggx = cv2.filter2D(avg.copy(), -1, xkernel)
avggy = cv2.filter2D(avg.copy(), -1, ykernel)

cv2.imshow("smoothed", avg)
imsave('smoothed.png', avg, cmap='gray')
cv2.imshow("smoothed |Gx|", np.abs(avggx))
imsave('smoothed-|Gx|.png', np.abs(avggx), cmap='gray')
cv2.imshow("smoothed |Gy|", np.abs(avggy))
imsave('smoothed-|Gy|.png', np.abs(avggy), cmap='gray')
cv2.imshow("smoothed |Gx| + |Gy|", np.abs(avggy) + np.abs(avggx))
imsave('smoothed-|Gx|+|Gy|.png', np.abs(avggy) + np.abs(avggx), cmap='gray')

d1kernel = np.array([[0, 1, 2], [-1, 0, 1], [-2, -1, 0]])
d2kernel = np.array([[-2, -1, 0], [-1, 0, 1], [0, 1, 2]])

avgd1 = cv2.filter2D(avg.copy(), -1, d1kernel)
avgd2 = cv2.filter2D(avg.copy(), -1, d2kernel)

cv2.imshow("diagonal kernel 1", avgd1)
imsave('smoothed-diagonal-1.png', avgd1, cmap='gray')
cv2.imshow("diagonal kernel 2", avgd2)
imsave('smoothed-diagonal-2.png', avgd2, cmap='gray')

thavg = np.abs(avggy) + np.abs(avggx)
th = np.max(thavg) * 3./9.
resthavg = thavg.copy()
resthavg[thavg > th] = 1.
resthavg[thavg <= th] = 0.

thimg = np.abs(gy) + np.abs(gx)
th = np.max(thimg) * 3./9.
resthimg = thimg.copy()
resthimg[thimg > th] = 1.
resthimg[thimg <= th] = 0.

cv2.imshow("building threshold", resthimg)
imsave('threshold-building.png', resthimg, cmap='gray')
cv2.imshow("smoothed threshold", resthavg)
imsave('threshold-smoothed.png', resthavg, cmap='gray')

cv2.waitKey()
cv2.destroyAllWindows()