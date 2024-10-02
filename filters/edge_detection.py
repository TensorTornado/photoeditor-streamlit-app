import cv2

def apply_edge_detection(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Use Canny edge detection
    edges = cv2.Canny(gray, 100, 200)
    
    # Convert back to BGR so it can be displayed properly
    edges_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    
    return edges_bgr
