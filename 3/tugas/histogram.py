import numpy as np
import imageio.v3 as img
import matplotlib.pyplot as plt

image_path = "cat.png"
image = img.imread(image_path)

if len(image.shape) < 3 or image.shape[2] != 3:
  print("Format gambar harus RGB")
  exit()

red = image[:,:,0]
green = image[:,:,1]
blue = image[:,:,2]

gray = 0.2 * red + 0.5 * green + 0.3 * blue
image_gray = np.zeros_like(image)
image_gray[:,:,0] = gray
image_gray[:,:,1] = gray
image_gray[:,:,2] = gray

hist, bins = np.histogram(gray, bins=256, range=[0,256])

dominant_intensity = np.argmax(hist)
dominant_pixel_count = hist[dominant_intensity]

plt.figure(figsize=(15,15))

plt.subplot(2,2,1)
plt.imshow(image_gray)

plt.subplot(2,2,2)
plt.bar(range(0,256), hist, color="gray")
plt.title("Histogram")
plt.xlabel("Intensitas Pixel")
plt.ylabel("Frekuensi")

plt.annotate(f'Intensitas dominan: {dominant_intensity}\nJumlah piksel: {dominant_pixel_count}', 
             xy=(dominant_intensity, dominant_pixel_count), 
             xytext=(dominant_intensity+10, dominant_pixel_count), 
             arrowprops=dict(facecolor='red', shrink=0.05))

plt.show()

print("\nJumlah pixel untuk setiap intensitas")
intensity_level = 0
for pixel_count in hist:
  print(f"intensity {intensity_level}: {pixel_count} pixel")
  intensity_level += 1