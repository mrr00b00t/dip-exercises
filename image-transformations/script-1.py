import cv2
import argparse


def check_type(x):
    x = float(x)
    if x < .0 or x > 1.:
        raise argparse.ArgumentTypeError("%s is an invalid float in range [0, 1]" % x)
    return x

parser = argparse.ArgumentParser(description="Script for cropping and flipping an image.",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("--h-min", help="Minimum height percentage for cropping", type=check_type, required=True)
parser.add_argument("--h-max", help="Maximum height percentage for cropping", type=check_type, required=True)
parser.add_argument("--w-min", help="Minimum width percentage for cropping", type=check_type, required=True)
parser.add_argument("--w-max", help="Maximum width percentage for cropping", type=check_type, required=True)
args = parser.parse_args()

config = vars(args)

h_min, h_max, w_min, w_max = config.values()

img = cv2.imread("lena.png")
h, w = img.shape[:2]

cropped_image = img[int(h_min*h):int(h_max*h),int(w_min*w):int(w_max*w),:]
cv2.imwrite("lena-cropped.png", cropped_image)

cv2.imwrite("lena-vertically-flipped.png", img[::-1, :, :])
cv2.imwrite("lena-horizontally-flipped.png", img[:, ::-1, :])