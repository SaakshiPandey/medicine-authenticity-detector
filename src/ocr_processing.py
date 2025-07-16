import pytesseract
from PIL import Image
import cv2
import re

def preprocess_image(image_path):
    """Enhance image for better OCR"""
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return thresh

def extract_text(image_path):
    """Extract all text using Tesseract"""
    processed_img = preprocess_image(image_path)
    text = pytesseract.image_to_string(processed_img)
    return text.strip()

def parse_medicine_info(text):
    """Extract key fields from OCR text"""
    info = {
        "medicine_name": None,
        "batch_no": None,
        "expiry_date": None,
        "manufacturer": None
    }
    
    # Simple regex patterns (customize based on your dataset)
    patterns = {
        "batch_no": r"Batch[:]?\s*([A-Z0-9]+)",
        "expiry_date": r"Exp(?:iry)?[:]?\s*(\d{2}/\d{4})",
        "medicine_name": r"(?:Name|Drug)[:]?\s*([A-Z][a-z]+)",
        "manufacturer": r"Mfg[:]?\s*([A-Z][a-zA-Z\s]+)"
    }
    
    for field, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            info[field] = match.group(1)
    
    return info