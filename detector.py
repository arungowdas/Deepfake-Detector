import cv2
import os

# Image to be tested
image_path = "test_image.jpg"

print("=" * 45)
print("          DEEPFAKE DETECTOR")
print("=" * 45)

# Check whether image exists
if not os.path.exists(image_path):
    print("\nERROR: test_image.jpg not found!")
    print("Please place the image inside this folder.")
    exit()

# Read image
image = cv2.imread(image_path)

if image is None:
    print("\nERROR: Unable to read the image.")
    exit()

print("\nImage loaded successfully.")

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load OpenCV face detector
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

# Detect faces
faces = face_detector.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(50, 50)
)

print("Faces detected:", len(faces))

# Basic image analysis
brightness = gray.mean()
sharpness = cv2.Laplacian(gray, cv2.CV_64F).var()

print("Brightness:", round(brightness, 2))
print("Sharpness:", round(sharpness, 2))

# Basic prototype result
if len(faces) > 0:
    result = "LIKELY REAL"
    score = 25
else:
    result = "NEEDS FURTHER ANALYSIS"
    score = 50

print("\nAnalysis Score:", score, "%")
print("Result:", result)

print("\nThis is a basic prototype.")
print("Advanced detection requires a trained ML/DL model.")

print("=" * 45)