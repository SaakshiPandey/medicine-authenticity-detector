import cv2

def is_blurry(image_path, threshold=100):
    """Check if image is blurry using Laplacian variance"""
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    variance = cv2.Laplacian(gray, cv2.CV_64F).var()
    return variance < threshold