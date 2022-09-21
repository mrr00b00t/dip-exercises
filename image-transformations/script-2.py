import cv2
import argparse
import numpy as np


parser = argparse.ArgumentParser(description="Script for translating an image.",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("-tx", "--x-translation", help="Minimum height percentage for cropping", type=int, required=True)
parser.add_argument("-ty", "--y-translation", help="Maximum height percentage for cropping", type=int, required=True)
args = parser.parse_args()

config = vars(args)

tx, ty = config.values()

M = np.array(
    [
        [1, 0, float(tx)],
        [0, 1, float(ty)]
    ]
)

img = cv2.imread("lena.png")
img_translated = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
cv2.imwrite("img-translated.png", img_translated)