import torch
import torchvision
from torchvision.ops import nms
from torchvision.transforms import functional as F
from torchvision.models.detection import FasterRCNN_ResNet50_FPN_Weights
import cv2

# # Load model
weights = FasterRCNN_ResNet50_FPN_Weights.DEFAULT
model = torchvision.models.detection.fasterrcnn_resnet50_fpn(weights=weights)
model.eval()
labels = weights.meta["categories"]

# # Load image
img_path = "test1.jpg"
image = cv2.imread(img_path)
orig = image.copy()

# Add a check here as advised in previous response, though not strictly required for the change requested
if image is None:
    print("ERROR: Image could not be loaded. Check 'test1.jpg' file.")
    exit()

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
tensor = F.to_tensor(image_rgb).unsqueeze(0)

# # Run detection
with torch.no_grad():
    pred = model(tensor)[0]

# --- CHANGES START HERE ---

# 1. Use the initial prediction variables directly
boxes = pred["boxes"]
scores = pred["scores"]
classes = pred["labels"]

h, w = image.shape[:2]

# The filtering loop is removed entirely to keep all detected objects.
# We'll use a lower confidence threshold directly in the NMS setup for a cleaner result.

# 2. Define minimum score threshold for ALL objects (e.g., 0.50)
MIN_SCORE_THRESHOLD = 0.50 

# 3. Filter boxes and scores based on the new threshold
# We are keeping all labels (objects)
filtered_indices = scores > MIN_SCORE_THRESHOLD
all_objects_boxes = boxes[filtered_indices]
all_objects_scores = scores[filtered_indices]
all_objects_classes = classes[filtered_indices]

# # Apply NMS to ALL objects
if len(all_objects_boxes) > 0:
    # Non-Maximum Suppression (NMS) with an IOU threshold of 0.30
    iou_threshold = 0.30
    # Apply NMS to the filtered boxes and scores
    keep = nms(all_objects_boxes, all_objects_scores, iou_threshold)
    
    final_boxes = all_objects_boxes[keep]
    final_scores = all_objects_scores[keep]
    final_classes = all_objects_classes[keep] # Keep the class labels for drawing
else:
    final_boxes = []
    final_scores = []
    final_classes = []


object_count = len(final_boxes)
print("Number of objects detected:", object_count)

# # Draw boxes
# 4. Draw all objects using the class labels for the text
for box, score, cls in zip(final_boxes, final_scores, final_classes):
    x1, y1, x2, y2 = box.int().tolist()
    
    # Get the human-readable label for the detected object
    label_text = f"{labels[cls]} {score:.2f}"
    
    # Draw rectangle (use a general color, e.g., blue BGR: 255, 0, 0)
    cv2.rectangle(orig, (x1, y1), (x2, y2), (255, 0, 0), 2)
    
    # Draw label and score
    cv2.putText(orig, label_text, (x1, y1 - 5), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

cv2.imshow("Detection", orig)
cv2.waitKey(0)
cv2.destroyAllWindows()