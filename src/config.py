import os

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET_PATH = os.path.join(BASE_DIR, "data/counterfeit_med_detection")
MODEL_PATH = os.path.join(BASE_DIR, "yolov5/runs/train/counterfeit_detector/weights/best.pt")
REFERENCE_DATA = os.path.join(BASE_DIR, "data/reference_data/medicine_db.csv")

# YOLOv5 Settings
CONF_THRESHOLD = 0.7  # Minimum confidence score
IOU_THRESHOLD = 0.5   # Intersection Over Union threshold

# OCR Settings
TESSERACT_CONFIG = r'--oem 3 --psm 6'