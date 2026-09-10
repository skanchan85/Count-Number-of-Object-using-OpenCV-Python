from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np
from ultralytics import YOLO
import supervision as sv

app = Flask(__name__)
CORS(app)  # allow frontend requests

# Load YOLO model once
model = YOLO("yolov8s.pt")

@app.route("/VideoObj", methods=["POST"])
def detect_objects():
    if "image" not in request.files:
        return jsonify({"error": "No image provided"}), 400

    file = request.files["image"]
    image_bytes = file.read()

    # Decode image
    np_img = np.frombuffer(image_bytes, np.uint8)
    frame = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    # YOLO inference
    results = model(frame, conf=0.4, classes=[2])  # class 2 = car

    detections = sv.Detections.from_ultralytics(results[0])

    count = len(detections)

    boxes = []
    for xyxy in detections.xyxy:
        boxes.append({
            "x1": int(xyxy[0]),
            "y1": int(xyxy[1]),
            "x2": int(xyxy[2]),
            "y2": int(xyxy[3])
        })

    return jsonify({
        "count": count,
        "boxes": boxes
    })


if __name__ == "__main__":
    app.run(debug=True)
