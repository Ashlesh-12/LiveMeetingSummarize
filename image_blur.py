from PIL import Image, ImageFilter
import matplotlib.pyplot as plt
import numpy as np

im = Image.open("/content/flower.jpg")
im1 = im.filter(ImageFilter.BoxBlur(2))

plt.imshow(im1)
plt.title("Blurred image")

# REMOVE axis off
# plt.axis('off')

# ---- ADD proper axis settings ----
plt.xlim(0, im1.size[0])               # image width
plt.ylim(im1.size[1], 0)               # image height (reverse for images)

# ticks: 20, 40, 60, 80, ...
plt.xticks(np.arange(20, im1.size[0], 20))
plt.yticks(np.arange(20, im1.size[1], 20))

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
# ----------------------------------

plt.show()