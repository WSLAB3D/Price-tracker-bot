from ultralytics import YOLO

CONFIDENCE_THRESHOLD = 0.5
_model = None

def detect_product(file_path):
    global _model
    if _model is None:
        _model = YOLO("yolov8n.pt")

    results = _model(file_path)
    predictions = results[0].boxes.data
    names = results[0].names

    labels = [
        names[int(box[5].item())]
        for box in predictions
        if box[4].item() > CONFIDENCE_THRESHOLD
    ]

    return labels if labels else ["Unknown item"]