import imageio as image
import numpy as np
import matplotlib.pyplot as plt

def histEqual(image):
  hist, bins = np.histogram(image.flatten(), bins=256, range=[0, 256])
  cdf = hist.sum()
  cdf_normal = (cdf / cdf.max()) * 255
  img_equal = np.interp(image.flatten(), bins[:-1], cdf_normal)
  return img_equal.reshape(image.shape).astype(np.int8)

path = "cat.png"

img = image.imread(path)
img_equal = histEqual(img)

plt.figure(figsize=(15,8.1))

plt.subplot(2,2,1)
plt.imshow(img)

plt.subplot(2,2,2)
plt.plot(img_equal)

plt.show()