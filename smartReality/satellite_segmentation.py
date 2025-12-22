import cv2
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("images/house.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Simple threshold segmentation
_, segmented = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)

plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Segmented Image")
plt.imshow(segmented, cmap="gray")
plt.axis("off")

plt.show()
