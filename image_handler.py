from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

def detect_product(file_path):
    results = model(file_path)
    predictions = results[0].boxes.data
    labels = results[0].names
    if predictions:
        return labels[int(predictions[0][5].item())]
    return "Unknown item"