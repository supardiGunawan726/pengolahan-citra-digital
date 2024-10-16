import imageio as image
import numpy as np
import matplotlib.pyplot as plt

path = "./negative.png"

img_negatif = image.imread(path)
r_neg = img_negatif[:,:,0]
hist_rneg, rneg_bins = np.histogram(r_neg.flatten(), bins=256, range=[0,256])

img_positif = 255 - img_negatif
r_pos = img_positif[:,:,0]
hist_rpos, rpos_bins = np.histogram(r_pos.flatten(), bins=256, range=[0,256])

plt.figure(figsize=(15,15))

plt.subplot(2,2,1)
plt.imshow(img_negatif)

plt.subplot(2,2,2)
plt.imshow(img_positif)

plt.subplot(2,2,3)
plt.plot(hist_rneg)

plt.subplot(2,2,4)
plt.plot(hist_rpos)

plt.show()