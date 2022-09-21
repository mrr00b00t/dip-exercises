import argparse
import numpy as np
from matplotlib import pyplot as plt
 
 
parser = argparse.ArgumentParser(description="Script for plotting a Gaussian 2D image.",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("--x-bound", help="Bound in X-coordinate for x values", default=15., type=float)
parser.add_argument("--y-bound", help="Bound in Y-coordinate for y values", default=15., type=float)
parser.add_argument("-S", "--size", help="Size of a grid SxS pixels", required=True, type=int)
parser.add_argument("-mx", help="Mean of x-coordinate distribution", default=0., type=float)
parser.add_argument("-sx", help="Standard deviation of x-coordinate distribution", default=2., type=float)
parser.add_argument("-my", help="Mean of y-coordinate distribution", default=0., type=float)
parser.add_argument("-sy", help="Standard deviation of y-coordinate distribution", default=5., type=float)
parser.add_argument("--rotation", help="Rotation of the image", default=np.pi/6, type=float)
args = parser.parse_args()

config = vars(args)
print(config)
x_bound, y_bound, size, mx, sx, my, sy, rotation = config.values()

x = np.linspace(-x_bound, x_bound, size)
y = np.linspace(-y_bound, y_bound, size)

xx, yy = np.meshgrid(x, y)

xx = xx-mx
yy = yy-my

x2 = np.cos(rotation)*(xx)-np.sin(rotation)*(yy)
y2 = np.sin(rotation)*(xx)+np.cos(rotation)*(yy)

z = (1/(2*np.pi*sx*sy) * np.exp(-(x2**2/(2*sx**2) + y2**2/(2*sy**2))))

plt.matshow(z)
plt.title("Rotated Gaussian with given parameters")
plt.xticks([]), plt.yticks([])
plt.show()
