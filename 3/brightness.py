import imageio as image
import numpy as np
import matplotlib.pyplot as plt

def brightness(image, factor):
  img_bright = image.astype(np.float32)
  img_bright += factor
  img_bright = np.clip(img_bright, 0, 255)

  return img_bright.astype(np.uint8)

path = "cat.png"
image_cat = image.imread(path)

image_cat_bright = brightness(image_cat, 100)

plt.figure(figsize=(15,15))

plt.subplot(2,2,1)
plt.imshow(image_cat)

plt.subplot(2,2,2)
plt.imshow(image_cat_bright)

plt.show()