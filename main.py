import math
import sys

import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy import constants
from scipy.optimize import root
from math import cos
from os import system


if __name__ == '__main__':

    x = np.random.randint(10, size=(10))
    print(x)
    y = np.random.randint(10, size=(10))
    colors = np.random.randint(10, size=(10))
    sizes = 10 * np.random.randint(10, size=(10))

    plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

    plt.colorbar()

    plt.show()


    #plt.savefig(sys.stdout.buffer)
    #sys.stdout.flush()

