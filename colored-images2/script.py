import cv2
import numpy as np
 
img = cv2.imread('img.jpg')
bg = cv2.imread('bg.jpg')


img = cv2.resize(img, (840, 680))
bg = cv2.resize(bg, (840, 680))

lower = np.array([0, 94, 0])
upper = np.array([69, 255, 69])

mask = cv2.inRange(img, lower, upper)
res = cv2.bitwise_and(img, img, mask = mask)

f = img - res
f = np.where(f == 0, bg, f)

cv2.imshow("image-chroma-key", img)
cv2.imshow("image-with-bg", f)

kernel_blur = np.ones((3,3), np.float32) / 9

kernel_shapen = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

blur_img = cv2.filter2D(f, -1, kernel_blur)
sharpen_img = cv2.filter2D(f, -1, kernel_shapen) 

cv2.imshow("blur-img", blur_img)
cv2.imshow("sharpen-img", sharpen_img)

cv2.waitKey()
cv2.destroyAllWindows()