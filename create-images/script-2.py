import argparse
import numpy as np
from matplotlib import pyplot as plt
 
 
parser = argparse.ArgumentParser(description="Script for plotting a sin(x+y) image.",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("--x-bound", help="Bound in X-coordinate for x values", default=15., type=float)
parser.add_argument("--y-bound", help="Bound in Y-coordinate for y values", default=15., type=float)
parser.add_argument("-S", "--size", help="Size of a grid SxS pixels", required=True, type=int)
parser.add_argument("--rotation", help="Rotation of the image", default=np.pi/6, type=float)
args = parser.parse_args()

config = vars(args)

x_bound, y_bound, size, rotation = config.values()

x = np.linspace(-x_bound, x_bound, size)
y = np.linspace(-y_bound, y_bound, size)

xx, yy = np.meshgrid(x, y)

x = np.cos(rotation)*(xx)-np.sin(rotation)*(yy)
y = np.sin(rotation)*(xx)+np.cos(rotation)*(yy)

z = np.sin(x + y)

plt.matshow(z)
plt.title("Rotated sin(x+y) Image")
plt.xticks([]), plt.yticks([])
plt.show()