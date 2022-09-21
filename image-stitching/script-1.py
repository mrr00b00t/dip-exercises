import cv2
import argparse
import os


parser = argparse.ArgumentParser(description="Script for stitching images (panorama)",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("-i", "--input", help="Path containing images to stitch together", type=str, required=True)
parser.add_argument("-o", "--output", help="Output path of stitched image.", type=str, required=True)
args = parser.parse_args()

config = vars(args)

input_imgs, output_img = config.values()

imgs_filenames = os.listdir(input_imgs)
imgs = []

for img_filename in imgs_filenames:
    imgs.append(
        cv2.imread(os.path.join(input_imgs, img_filename))
    )
    
stitcher = cv2.Stitcher_create()
status, img_stitched = stitcher.stitch(imgs)

cv2.imwrite(
    output_img + '.' + img_filename.split('.')[-1],
    img_stitched
)