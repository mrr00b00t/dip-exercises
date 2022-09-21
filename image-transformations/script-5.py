import cv2
import numpy as np


img = cv2.imread("lena.png")

aleatory_image = ((np.random.rand(*img.shape) > 0.5) * 255).astype(np.uint8)

bitwise_or  = np.bitwise_or(img, aleatory_image)
bitwise_and = np.bitwise_and(img, aleatory_image)
bitwise_xor = np.bitwise_xor(img, aleatory_image)

cv2.imwrite("img-bitwise-or.png", bitwise_or)
cv2.imwrite("img-bitwise-and.png", bitwise_and)
cv2.imwrite("img-bitwise-xor.png", bitwise_xor)