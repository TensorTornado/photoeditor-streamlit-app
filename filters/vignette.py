import cv2
import numpy as np

def apply_vignette(image):
    rows, cols = image.shape[:2]
    
    # Create a vignette mask using Gaussian kernels
    kernel_x = cv2.getGaussianKernel(cols, 200)
    kernel_y = cv2.getGaussianKernel(rows, 200)
    kernel = kernel_y * kernel_x.T
    mask = 255 * kernel / np.linalg.norm(kernel)
    
    # Apply the mask to each channel of the input image
    output = np.copy(image)
    for i in range(3):
        output[:, :, i] = output[:, :, i] * mask

    return output
