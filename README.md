# 👁️ eye_color_detector
A Python-based project that detects and classifies eye colors from images using OpenCV and image processing techniques. This tool analyzes the dominant color in the eye region and classifies it into categories such as Blue, Green, Brown, Amber, or Gray.

# Features
- Detects faces and eyes in an image using Haar cascades.
- Analyzes the eye region's dominant color in HSV color space.
- Classifies eye color into common categories.
- Lightweight and efficient for real-time or batch image processing.

# How It Works
- The script uses OpenCV's Haar cascades to detect faces and eyes in the input image.
- For each detected eye, it calculates the dominant color using HSV (Hue, Saturation, Value) color space.
- Based on the HSV values, it classifies the eye color into:
    Blue
    Green
    Brown
    Amber
    Gray
# Technologies Used
- Python 3.x: Core programming language.
- OpenCV: For image processing and object detection.
- NumPy: For numerical computations.
- Haar Cascades: Pre-trained models for face and eye detection.
