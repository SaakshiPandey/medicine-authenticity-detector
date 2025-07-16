#  Medicine Authenticity Detector
  
*An end-to-end deep learning system to detect counterfeit medicines using YOLOv5 object detection and Tesseract OCR*

---

## 🚀 Key Features
| Feature | Technology | Performance |
|---------|------------|-------------|
| Visual counterfeit detection | YOLOv5 | 93.6% mAP@0.5 |
| Package text verification | Tesseract OCR | 89.2% accuracy |
| Blur/quality check | OpenCV Laplacian | 94% correct rejections |
| Web interface | Streamlit | 850ms response time |

---

## 📦 Repository Structure
```
medicine-authenticity-detector/
├── data/                        # Dataset configuration
│   └── counterfeit_med_detection/
│       ├── train/              # Training images
│       ├── valid/              # Validation images
│       └── data.yaml           # Dataset config
├── models/
│   ├── yolov5/                 # YOLOv5 implementation
│   └── best.pt                 # Trained weights
├── src/
│   ├── app.py                  # Streamlit web app
│   ├── blur_detection.py       # Image quality check
│   ├── ocr_processing.py       # Text extraction
│   ├── text_validation.py      # Medicine info validation
│   └── config.py               # Path configurations
├── requirements.txt            # Python dependencies
├── LICENSE
└── README.md
```

---

## 🛠️ Installation Guide

### Prerequisites
- Python 3.8+
- NVIDIA GPU (Recommended)

### Step-by-Step Setup
```bash
# 1. Clone repository
git clone https://github.com/your-username/medicine-authenticity-detector.git
cd medicine-authenticity-detector

# 2. Install dependencies
pip install -r requirements.txt

# 3. Download Tesseract OCR (Linux)
sudo apt install tesseract-ocr
```

---

## 🖥️ Usage Instructions

### Web Application
```bash
streamlit run src/app.py
```

---

### Command Line Detection
```bash
python detect.py \
  --weights models/best.pt \
  --source input.jpg \
  --conf 0.7
```

**Expected Output**
```json
{
  "verdict": "Fake",
  "confidence": 0.91,
  "issues": ["Counterfeit label", "Missing batch number"]
}
```

---

## 📊 Model Performance

### Training Metrics

### Evaluation Results
| Class       | Precision | Recall | mAP@0.5 |
|-------------|-----------|--------|---------|
| Counterfeit | 0.88      | 0.929  | 0.947   |
| Real        | 0.861     | 0.929  | 0.925   |

---

## 🔧 Troubleshooting

| Issue                  | Solution                           |
|------------------------|------------------------------------|
| CUDA Out of Memory     | Reduce batch size `--batch 8`      |
| Tesseract Errors       | `sudo apt install libtesseract-dev`|
| Streamlit Port Busy    | Use `--server.port 8502`           |

---

## 📝 License
MIT License - See [LICENSE](./LICENSE) for details.

---

## 🤝 Contribution Guide

- Report issues via **GitHub Issues**
- Submit pull requests to the **dev branch**
- Improve dataset annotations on **Roboflow**

---

## 📮 Contact

**Project Maintainer**: Saakshi Pandey    
**Institution**: SRMIST  

---

### ✅ Key Improvements:
1. **Perfect Alignment**: All tables and code blocks are gap-free  
2. **Complete Documentation**: Every component is documented  
3. **Ready-to-Use**: Copy-paste friendly commands  
4. **Visual Hierarchy**: Clear section separation  
5. **Troubleshooting**: Common issues covered  

---
 
