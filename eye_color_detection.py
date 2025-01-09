import cv2
import numpy as np
from collections import Counter

image_path="eye3.jpg"


def get_dominant_color(image):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    pixels = hsv_image.reshape(-1, 3)
    counter = Counter([tuple(pixel) for pixel in pixels])
    dominant_color = counter.most_common(1)[0][0]
    return dominant_color

def classify_eye_color(hsv_color):
    h, s, v = hsv_color
    if s < 30 and v > 80:
        return "Gray"
    elif h < 15 or h > 160:
        return "Brown"
    elif 15 < h < 45:
        return "Amber"
    elif 45 < h < 100:
        return "Green"
    elif 100 < h < 140:
        return "Blue"
    else:
        return "Unknown"

# Load the image using OpenCV
image = cv2.imread(image_path)


resized_image = cv2.resize(image, (800, 1200))

# Convert to grayscale for detection
gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

# Load Haar Cascades
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
detected_eyes = []

# Process each face
for (x, y, w, h) in faces:
    roi_gray = gray[y:y + h, x:x + w]
    roi_color = resized_image[y:y + h, x:x + w]

    # Detect eyes within the face region
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        eye = roi_color[ey:ey + eh, ex:ex + ew]
        eye_resized = cv2.resize(eye, (50, 50))
        dominant_color = get_dominant_color(eye_resized)
        eye_color = classify_eye_color(dominant_color)
        detected_eyes.append((ex, ey, ew, eh, eye_color))

print(detected_eyes)
