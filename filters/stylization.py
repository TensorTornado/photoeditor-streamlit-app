import cv2

def apply_stylization(image):
    # Apply the stylization filter using OpenCV's stylization function
    stylized_image = cv2.stylization(image, sigma_s=60, sigma_r=0.07)
    
    return stylized_image
