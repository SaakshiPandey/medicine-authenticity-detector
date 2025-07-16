import streamlit as st
import cv2
import torch
from PIL import Image
from yolov5.models.experimental import attempt_load
from src.blur_detection import is_blurry
from src.ocr_processing import extract_text, parse_medicine_info
from src.text_validation import MedicineValidator
from src.config import *

# Load Models
@st.cache_resource
def load_models():
    yolo_model = attempt_load(MODEL_PATH, device="cpu")
    validator = MedicineValidator(REFERENCE_DATA)
    return yolo_model, validator

yolo_model, validator = load_models()

# Streamlit UI
st.title("🩺 Medicine Authenticity Detector")
uploaded_file = st.file_uploader("Upload medicine package image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    # Save uploaded file
    with open("temp.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Check blur
    if is_blurry("temp.jpg"):
        st.error("⚠️ Image is too blurry. Please upload a clearer image.")
    else:
        # Display image
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Image", width=300)
        
        # YOLOv5 Detection
        results = yolo_model("temp.jpg", size=640)
        detected_img = results.render()[0]  # Image with bounding boxes
        st.image(detected_img, caption="Detection Results", width=300)
        
        # OCR Processing
        text = extract_text("temp.jpg")
        medicine_info = parse_medicine_info(text)
        
        # Validation
        errors = validator.validate_fields(medicine_info)
        
        # Verdict Logic
        verdict = "✅ Real"
        if len(results.pandas().xyxy[0]) > 0:  # If counterfeit marks detected
            verdict = "❌ Fake"
        elif errors:
            verdict = "⚠️ Suspicious"
        
        # Display Results
        st.subheader("Verdict: " + verdict)
        st.json({
            "verdict": verdict,
            "detected_issues": errors,
            "extracted_info": medicine_info
        })