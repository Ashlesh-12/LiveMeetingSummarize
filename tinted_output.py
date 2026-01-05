from PIL import Image,ImageEnhance
import matplotlib.pyplot as plt
im=Image.open("flower.jpg").convert("RGB")
blue_tint=Image.new("RGB",im.size,(225,0,255))
tinted=Image.blend(im, blue_tint ,alpha=0.5)
plt.imshow(tinted)
plt.axis("off")
plt.title("blue tinted image")
plt.show()
