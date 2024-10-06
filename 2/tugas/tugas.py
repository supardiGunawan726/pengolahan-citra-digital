import numpy as np
import imageio.v3 as img

def process_image(image_path):
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

  gray = 0.2 * red + 0.5 * green + 0.3 * blue
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



  image = img.imwrite(f"output/{image_path}_red.jpeg", image_red)
  image = img.imwrite(f"output/{image_path}_blue.jpeg", image_blue)
  image = img.imwrite(f"output/{image_path}_green.jpeg", image_green)
  image = img.imwrite(f"output/{image_path}_gray.jpeg", image_gray)
  image = img.imwrite(f"output/{image_path}_bw.jpeg", image_bw)

  print(f"Berhasil memproses gambar {image_path}")

images_path = ["daun_pepaya.png", "daun_singkong.png", "daun_kenikir.png"]

for image_path in images_path:
  process_image(image_path)