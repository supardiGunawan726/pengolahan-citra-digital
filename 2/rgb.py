import numpy as np
import imageio.v3 as img

image_path = "aku_bluetooth.jpeg"
image = img.imread(image_path)

if len(image.shape) < 3 or image.shape[2] != 3:
  print("Format gambar harus RGB")
  exit()

red = image[:,:,0]
green = image[:,:,1]
blue = image[:,:,2]

image_red = np.zeros_like(image)
image_red[:,:,0] = red

image_blue = np.zeros_like(image)
image_blue[:,:,1] = blue

image_green = np.zeros_like(image)
image_green[:,:,2] = green

gray = 0.299 * red + 0.587 * green + 0.114 * blue
image_gray = np.zeros_like(image)
image_gray[:,:,0] = gray
image_gray[:,:,1] = gray
image_gray[:,:,2] = gray

threshold = 100
image_bw = np.zeros_like(image)

for i in range(0, len(gray)):
  for j in range(0, len(gray[i])):
    if (gray[i,j] > threshold):
      image_bw[i,j] = 255
    else:
      image_bw[i,j] = 0


image = img.imwrite("image_red.jpeg", image_red)
image = img.imwrite("image_blue.jpeg", image_blue)
image = img.imwrite("image_green.jpeg", image_green)
image = img.imwrite("image_gray.jpeg", image_gray)
image = img.imwrite("image_bw.jpeg", image_bw)

print("Proses berhasil")