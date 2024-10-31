import imageio as image
import numpy as np
import matplotlib.pyplot as plt

def brightness(image, factor):
  img_bright = image.astype(np.float32)
  img_bright = img_bright + factor
  img_bright = np.clip(img_bright, 0, 255)
  return img_bright.astype(np.uint8)

def contrast(image, factor):
  imgContrast = image.astype(np.float32)
  mean = 128
  imgContrast = mean + factor * (imgContrast - mean)
  imgContrast = np.clip(imgContrast, 0, 255)
  return imgContrast.astype(np.uint8)

def join(image1, f1, image2, f2):
  image1 = image1.astype(np.float32)
  image2 = image2.astype(np.float32)
  imageBlend = (image1 * f1) + (image2 * f2)
  imageBlend = np.clip(imageBlend, 0, 255)
  return imageBlend.astype(np.uint8)

def make_histogram(image):
  hist, bins = np.histogram(image.flatten(), bins=256, range=[0, 256])
  return hist

path = "cat.png"
path2 = "dog.png"

img = image.imread(path)
hist_img = make_histogram(img)

img_bright = brightness(img, 100)
hist_img_bright = make_histogram(img_bright)

img_contrast = contrast(img, 1.3)
hist_img_contrast = make_histogram(img_contrast)

img2 = image.imread(path2)
img_blend = join(img, 0.5, img2, 0.5)
hist_img_blend = make_histogram(img_blend)

plt.figure(figsize=(15,8.1))

plt.subplot(4,2,1)
plt.imshow(img)
plt.subplot(4,2,2)
plt.plot(hist_img)

plt.subplot(4,2,3)
plt.imshow(img_bright)
plt.subplot(4,2,4)
plt.plot(hist_img_bright)

plt.subplot(4,2,5)
plt.imshow(img_contrast)
plt.subplot(4,2,6)
plt.plot(hist_img_contrast)

plt.subplot(4,2,7)
plt.imshow(img_blend)
plt.subplot(4,2,8)
plt.plot(hist_img_blend)

plt.show()