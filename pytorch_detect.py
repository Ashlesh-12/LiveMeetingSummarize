import torch
import torchvision
from torchvision.ops import nms
from torchvision.transforms import functional as F
from torchvision.models.detection import FasterRCNN_ResNet50_FPN_Weights
import cv2

# ---------------------------------------------
# Load model
# ---------------------------------------------
weights = FasterRCNN_ResNet50_FPN_Weights.DEFAULT
model = torchvision.models.detection.fasterrcnn_resnet50_fpn(weights=weights)
model.eval()
labels = weights.meta["categories"]

# ---------------------------------------------
# Load image
# ---------------------------------------------
img_path = "test1.jpg"
image = cv2.imread(img_path)
orig = image.copy()

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
tensor = F.to_tensor(image_rgb).unsqueeze(0)

# ---------------------------------------------
# Run detection
# ---------------------------------------------
with torch.no_grad():
    pred = model(tensor)[0]

boxes = pred["boxes"]
scores = pred["scores"]
classes = pred["labels"]

h, w = image.shape[:2]

person_boxes = []
person_scores = []

# ---------------------------------------------
# Filter PERSON only
# ---------------------------------------------
for box, score, cls in zip(boxes, scores, classes):
    if labels[cls] != "person":
        continue
    if score < 0.65:
        continue

    x1, y1, x2, y2 = box
    bw = x2 - x1
    bh = y2 - y1

    # Remove leg-only detections
    if bh < h * 0.18:
        continue

    person_boxes.append(box)
    person_scores.append(score)

# ---------------------------------------------
# Apply NMS
# ---------------------------------------------
person_boxes = torch.stack(person_boxes)
person_scores = torch.tensor(person_scores)

keep = nms(person_boxes, person_scores, iou_threshold=0.30)

final_boxes = person_boxes[keep]
final_scores = person_scores[keep]

person_count = len(final_boxes)
print("Number of persons detected:", person_count)

# ---------------------------------------------
# Draw boxes
# ---------------------------------------------
for box, score in zip(final_boxes, final_scores):
    x1, y1, x2, y2 = box.int().tolist()
    cv2.rectangle(orig, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.putText(orig,f"Person {score:.2f}",
        (x1, y1 - 5),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 255, 0),
        2,
    )

# Show output
cv2.imshow("Detection", orig)
cv2.waitKey(0)
cv2.destroyAllWindows()
