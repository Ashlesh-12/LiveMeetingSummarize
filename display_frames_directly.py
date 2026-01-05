import cv2
import os
from google.colab.patches import cv2_imshow   

video_path = "/content/13102459_3840_2160_30fps.mp4"
output_folder = "frames"

os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

frame_count = 0
max_frames = 10

while True:
    ret, frame = cap.read()
    if not ret:
        break

  
    frame_filename = os.path.join(output_folder, f"frame_{frame_count:03d}.jpg")
    cv2.imwrite(frame_filename, frame)

   
    print(f"Frame {frame_count}:")
    cv2_imshow(frame)

    frame_count += 1
    if frame_count >= max_frames:
        break

cap.release()
cv2.destroyAllWindows()
