import cv2
import numpy as np
import argparse


parser = argparse.ArgumentParser(description="Script for rotating an image.",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("-R", "--radius", help="Radius of cicle mask.", type=int, required=True)
args = parser.parse_args()

config = vars(args)

radius = config['radius']

img = cv2.imread("lena.png")

center = (img.shape[1]//2, img.shape[0]//2)
color = (255, 255, 255)
thickness = -1

mask = cv2.circle(np.zeros(img.shape), center, radius, color, thickness).astype(np.uint8)

masked_img = np.bitwise_and(img, mask)

cv2.imwrite("lena-masked.png", masked_img)