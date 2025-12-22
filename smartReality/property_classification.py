import cv2
import numpy as np
from sklearn.svm import SVC

#Dummy training data (feature-based)
X_train=[[100],[150],[200]] #image brightness
y_train=["New","Average","Old"]

model=SVC()
model.fit(X_train,y_train)

#Test Image
img=cv2.imread("images/house.jpg",0)
brightness=int(np.mean(img))

prediction=model.predict([[brightness]])
print("Property Condition:",prediction[0])