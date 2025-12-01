import cv2
import os
from Ipython.display import Image,display
video_path="/content/AI.mp4"
output_folder="frames"
os.makedirs(output_folder,exist_ok=True)
cap=cv2.VideoCapture("/content/AI.mp4")
if not cap.isOpened():
  print("Error: could not open video")
  exit()
frame_count=0
max_frames=10
while frame_count<max_frames:
  ret,frame=cap.read()
  if not ret:
    break
  frame_filename=os.path.join(output_folder,f"frame_{frame_count:03d}.jpg")
  cv2.imwrite(frame_filename,frame)
  print(f"saved {frame_filename}")
  frame_count+=1
cap.release()
cv2.destroyAllWindows()
print("extracted 10 frames successfully")
print("\n saved images:")
print(os.listdir(output_folder))

for  i in range(10):
  frame_path=os.path.join(output_folder,f"frame_{frame_count:03d}.jpg")
  if os.path.exists(frame_path):
     display(Image(filename=frame_path))