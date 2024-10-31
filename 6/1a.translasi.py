import imageio.v3 as img
import numpy as np
import matplotlib.pyplot as plt

def Translasi(image, shiftX, shiftY):

  imgTranslasi = np.roll(image, shift=shiftY, axis=0) # Geser Vertikal
  imgTranslasi = np.roll(imgTranslasi, shift=shiftX, axis=1) # Geser Horizontal

  # Mengisi bagian kosong dengan warna hitam (0)
  if shiftY > 0:
    imgTranslasi[:shiftY, :] = 0 # Bagian atas jika geser ke bawah
  elif shiftY < 0:
    imgTranslasi[shiftY:, :] = 0 # Bagian bawah jika geser ke atas

  if shiftX > 0:
    imgTranslasi[: , :shiftX] = 0 # Bagian kiri jika geser ke kanan
  elif shiftX < 0:
    imgTranslasi[:, shiftX:] = 0 # Bagian kanan jika geser ke kiri

  return imgTranslasi

image = img.imread("tiger.png")

imageResult = Translasi(image, shiftX=50, shiftY=-300)

plt.figure(figsize=(16, 8))
plt.subplot(2,1,1)
plt.imshow(image)
plt.subplot(2,1,2)
plt.imshow(imageResult)
plt.show()