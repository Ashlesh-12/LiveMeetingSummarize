from PIL import Image, ImageFilter
import matplotlib.pyplot as plt

# Opens an image in RGB mode
im = Image.open("flower.jpg")

# Blurring the image
im1 = im.filter(ImageFilter.BoxBlur(95))

# Shows the image in image viewer
plt.imshow(im1)
plt.title("Blurred Image")
plt.axis('off')
plt.show()
