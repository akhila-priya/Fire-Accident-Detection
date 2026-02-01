from ultralytics import YOLO
import cv2

# Load YOLOv8 model (pretrained)
model = YOLO("yolov8n.pt")

# =========================
# Choose input source
# =========================

# Webcam
source = 0

# Image (uncomment to use)
# source = "images/fire.jpg"

# Video (uncomment to use)
# source = "videos/fire.mp4"

# =========================
# Run detection
# =========================
model(source, conf=0.4, show=True)

print("🔥 YOLO detection finished")

