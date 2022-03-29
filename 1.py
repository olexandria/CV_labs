import numpy as np
from PIL import Image
from matplotlib import pyplot as plt


def set_rgb(rgb: int):
    return min(255, rgb) if rgb > 0 else 0


def increasing_contrast(img_arr, a: float, s: int, t: int):
    x, y, z = img_arr.shape
    for i in range(0, x):
        for j in range(0, y):
            r, g, b = img_arr[i][j]
            new_red_value = set_rgb(a * (r + s) - t)
            new_green_value = set_rgb(a * (g + s) - t)
            new_blue_value = set_rgb(a * (b + s) - t)
            img_arr[i][j] = [new_red_value, new_green_value, new_blue_value]
    return img_arr


input_image = Image.open('img.png')
input_image_array = np.asarray(input_image)

contrast_image = increasing_contrast(input_image_array, 1.8, 0, 3)
output_image = Image.fromarray(contrast_image)

fig, axes = plt.subplots(1, 2)
axes[0].imshow(input_image)
axes[0].set_title('Original Image', fontsize=12)
axes[1].imshow(output_image)
axes[1].set_title('High Contrast Image', fontsize=12)
plt.show()
