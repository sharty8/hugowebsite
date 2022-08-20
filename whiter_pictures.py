import statistics

import cv2
import numpy as np
from matplotlib import image
from PIL import Image
from PIL import JpegImagePlugin as JIP


def filter_color(function, colors):
    """ function may be max or min """
    print(colors)
    filtered_values = [function(map(lambda x: x[i], colors)) for i in range(3)]

    best = list(list(filter(lambda x: x[0] == filtered_values[i], colors)) for i in range(3))
    best = best[2] + best[1] + best[2]

    sums = {sum(b): b for b in best}

    # fixes issue with median
    value = function(sums)
    if not value in sums:
        value = min(filter(lambda x: x > value, sums))

    return sums[value]


def linear_high_adjustment(array, degree):
    """increase the high values to max and leave low values untouched"""
    def linear_adjustment(x):
        return (((white_diff + 1) * x ** degree) // 256 ** degree)

    colors = img.reshape(img.shape[0] * img.shape[1], 3)
    higest_color = filter_color(max, colors)
    white_diff = np.array([255 - i for i in higest_color])
    new_array = np.array([np.array([x + linear_adjustment(x) for x in y]).astype(np.uint8) for y in array])
    return new_array



if __name__ == '__main__':
    image_path = '/Users/artygo/Desktop/sharty8.github.io/tests/EEC4A26C-6426-4A3C-935C-15988D5558CA_1_105_c copy.jpeg'

    img = cv2.imread(image_path)

    wtf = 1.23
    res = np.array([
            np.array([
                (x / sum(x)) ** wtf * sum(x) for x in y
            ]) for y in img
        ])

    cv2.imwrite(f'tests/copy_wtf.jpeg', res)



"""
3 + 1 = 4
-> 252 + 3
-> 0 + 0
255 / 3
"""
