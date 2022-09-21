import argparse
import numpy as np
from matplotlib import pyplot as plt


parser = argparse.ArgumentParser(description="Script for plotting a paraboloid image.",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("--x-bound", help="Bound in X-coordinate for x values", default=15., type=float)
parser.add_argument("--y-bound", help="Bound in Y-coordinate for y values", default=15., type=float)
parser.add_argument("-S", "--size", help="Size of a grid SxS pixels", required=True, type=int)
parser.add_argument("-a", help="Parameter 'a' of z = (x-x0)^2 / a^2 + (y-y0)^2 / b^2", default=1.5, type=float)
parser.add_argument("-b", help="Parameter 'b' of z = (x-x0)^2 / a^2 + (y-y0)^2 / b^2", default=3., type=float)
args = parser.parse_args()

config = vars(args)

x_bound, y_bound, size, a, b = config.values()

x = np.linspace(-x_bound, x_bound, size)
y = np.linspace(-y_bound, y_bound, size)

xx, yy = np.meshgrid(x, y)

z = (xx / a)**2 + (yy / b)**2

plt.matshow(z)
plt.title("Paraboloid Image")
plt.xticks([]), plt.yticks([])
plt.show()