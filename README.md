# 🔥 Fire Accident Detection using Deep Learning and YOLO

This project implements a fire and smoke detection system using deep learning techniques. A Convolutional Neural Network (CNN) is used for classification, and YOLOv8 is used for real-time fire localization in images, videos, and webcam streams.

---

## 🚀 Features
- Fire / Smoke / No-Fire classification using CNN
- Real-time object detection using YOLOv8
- Supports webcam, images, and videos
- Trained on 17,000+ images
- CPU-based training and inference

---

## 🧠 Technologies Used
- Python 3.10
- TensorFlow & Keras
- YOLOv8 (Ultralytics)
- OpenCV
- NumPy

---

## 📂 Project Structure
Fire-Accident-Detection/
├── train_cnn.py
├── yolo_detect.py
├── fire_model.h5
├── requirements.txt
└── README.md

---

## ▶️ How to Run

### 1️⃣ Install dependencies
```bash
pip install ultralytics opencv-python tensorflow

2️⃣ Train CNN model
python train_cnn.py

3️⃣ Run YOLO detection
python yolo_detect.py
