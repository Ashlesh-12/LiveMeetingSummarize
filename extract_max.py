import cv2  
import os

video_path = "/content/13102459_3840_2160_30fps.mp4"

output_folder = "frames"

os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture("/content/13102459_3840_2160_30fps.mp4")

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

frame_count = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break   
    frame_filename = os.path.join(output_folder, f"frame_{frame_count:03d}.jpg")
    cv2.imwrite(frame_filename, frame)
    print(f"Saved {frame_filename}")

    frame_count += 1
cap.release()
cv2.destroyAllWindows()
