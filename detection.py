from ultralytics import YOLO
import cv2

model = YOLO("yolov8s.pt")   

img_path = "person.jpg"
image = cv2.imread(img_path)

target_object = "person"   

results = model(image)

names = model.names  

for r in results:
    for box in r.boxes:
        cls = int(box.cls[0])         
        label = names[cls]             

        if label.lower() == target_object.lower():
            x1, y1, x2, y2 = box.xyxy[0]
            conf = float(box.conf[0])

            cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(image, f"{label} {conf:.2f}", (int(x1), int(y1)-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

cv2.imwrite("output.jpg", image)
cv2.imshow("Detected", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
