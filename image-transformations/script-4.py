import cv2
import argparse


parser = argparse.ArgumentParser(description="Script for rotating an image.",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("--scale-percentage", help="Percentage to scale the image (ex. 250% = 250)", type=float, required=True)
args = parser.parse_args()

config = vars(args)

scale_percentage = config['scale_percentage']

img = cv2.imread("lena.png")

height = int(img.shape[0] * scale_percentage / 100)
width = int(img.shape[1] * scale_percentage / 100)

resized = cv2.resize(img, (width, height), interpolation = cv2.INTER_AREA)

cv2.imwrite("img-resized.png", resized)