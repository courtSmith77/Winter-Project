from ultralytics import YOLO
import torch

# Load pretrained yolov8 nano model
model = YOLO("yolov8n-cls.pt")

if torch.cuda.is_available():
    model.train(data="./special_classes", epochs=500, device=0)
else :
    model.train(data="./special_classes", epochs=500)
