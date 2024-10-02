import cv2

def apply_pencil_sketch(image):
    # Apply the pencil sketch filter using OpenCV's pencilSketch function
    gray, sketch = cv2.pencilSketch(image, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
    
    return sketch
