import numpy as np
import imageio as img
import matplotlib.pyplot as plt

path = "tiger.png"
image = img.imread(path)

height, width = image.shape[:2]
horizontal = np.zeros_like(image)
vertical = np.zeros_like(image)
horizontal_vertical = np.zeros_like(image)

for y in range(height):
  for x in range(width):
    horizontal[y, x] = image[y, width - 1 - x]
    vertical[y, x] = image[height - 1 - y, x]
    horizontal_vertical[y, x] = image[height - 1 - y, width - 1 - x]

plt.figure(figsize=(16, 8))

plt.subplot(1,4,1)
plt.imshow(image)

plt.subplot(1,4,2)
plt.imshow(horizontal)

plt.subplot(1,4,3)
plt.imshow(vertical)

plt.subplot(1,4,4)
plt.imshow(horizontal_vertical)

plt.show()