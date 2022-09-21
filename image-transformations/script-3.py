import cv2
import argparse
import numpy as np


parser = argparse.ArgumentParser(description="Script for rotating an image.",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("--rotation", help="Degrees to rotate the image", type=float, required=True)
args = parser.parse_args()

config = vars(args)

rotation = config['rotation']

img = cv2.imread("lena.png")

M = cv2.getRotationMatrix2D((img.shape[1]/2, img.shape[0]/2), angle=rotation, scale=1)

img_translated = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

cv2.imwrite("img-rotated.png", img_translated)