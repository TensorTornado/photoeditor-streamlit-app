
# photo-editor-streamlit-app
Streamlit Photo Editor Application
=======
Streamlit PhotoEditor Application - An OpenCV-powered Image Processing Portfolio
********************************************************************************************************************
Introduction and Vision
In today’s world, image processing isn’t just for professionals. With social media booming and high-quality cameras in everyone’s pocket, the need for simple, easy-to-use photo editing tools is higher than ever. But what if you could take a professional approach, using complex algorithms, and make them accessible to anyone?
********************************************************************************************************************
This is where PhotoEditor, built using Streamlit and OpenCV, comes in. It is designed to be a powerful yet intuitive web-based tool, allowing users to upload their own images and apply sophisticated filters like edge detection, vignette effects, pencil sketching, and stylization—all with the click of a button. Best of all, this project is part of a GitHub brag portfolio, showcasing real-world problem-solving skills and the creation of a polished, user-friendly image editing solution.
********************************************************************************************************************
Features
Edge Detection: Detect and highlight edges in the uploaded image using OpenCV’s Canny algorithm.
Vignette: Apply a vignette effect to darken the edges of the image and focus on the center.
Pencil Sketch: Convert the image into a detailed black-and-white pencil sketch.
********************************************************************************************************************
Stylization: Apply an artistic, painterly effect to the image using advanced OpenCV filters.
Real-Time Processing: Process and preview filters in real-time as the user uploads and selects a filter.
********************************************************************************************************************
Challenge & Motivation
The primary goal of this project is to demonstrate proficiency in image processing, web-based interface design, and real-time performance optimization. The challenge wasn’t just to create another photo editor; it was to build a professional-grade application that handles real-world challenges such as:
********************************************************************************************************************
Managing large images
********************************************************************************************************************
Optimizing performance
Providing a seamless user experience
Additionally, this project highlights how advanced technical concepts, like OpenCV’s image filters and algorithms, can be made accessible to non-technical users via a highly intuitive web interface.
********************************************************************************************************************
Challenges and Solutions
********************************************************************************************************************
Challenge: Incorrect Color Display in Uploaded Image
Problem Encountered:
While building the app, the uploaded images appeared with incorrect colors—blue regions appeared orange and vice versa. This issue persisted even before filters were applied.
*******************************************************************************************************************
Steps Taken to Resolve:
**********************
Initial Hypothesis: The issue was suspected to be with the image upload process.
Research: The problem was identified as a mismatch between OpenCV’s default BGR format and Streamlit’s RGB format.
Solution: Applied a conversion using cv2.cvtColor() to transform the image from BGR to RGB before displaying it in Streamlit.
*********************************************************************************************************************
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
*********************************************************************************************************************
Outcome: After this fix, the images displayed correctly, and all filters could be applied without visual issues.
*******************************************************************************************************************
Challenge: Handling Large Image Sizes
Problem: Large, high-resolution images would slow down the app or even cause it to crash.
*******************************************************************************************************************
Solution:
*******************************************************************************************************************
Applied Gaussian blur to reduce noise and computational load before processing.
Converted images into smaller byte arrays before applying heavier filters.
Outcome: These optimizations ensured smooth performance even when handling large images.

Challenge: Ensuring Real-Time Filter Application
Problem: Applying filters in real-time without overloading the system was a challenge, especially for computationally heavy algorithms like edge detection and stylization.
*******************************************************************************************************************
Solution:
*******************************************************************************************************************
The app was structured to only process images after the user selected a filter.
Used Streamlit’s efficient integration with OpenCV for real-time image manipulation.
Outcome: The filters could be applied quickly and the results were displayed in real-time.

Project Structure
*******************************************************************************************************************
photoeditor-streamlit-app/
│
├── app.py                # Main Streamlit app file
├── filters/              # Folder for filter functions
│   ├── edge_detection.py
│   ├── vignette.py
│   ├── pencil_sketch.py
│   ├── stylization.py
├── assets/               # Static images such as logos, banners
│   ├── logo.png
├── README.md             # Project documentation
├── requirements.txt      # Python dependencies

How to Run Photo editor Application
*******************************************************************************************************************
Clone Repository:
git clone https://github.com/yourusername/photoeditor-streamlit-app.git
*******************************************************************************************************************
Navigate to the project directory:
cd photoeditor-streamlit-app
*******************************************************************************************************************
Install the required dependencies:
*******************************************************************************************************************
pip install -r requirements.txt
*******************************************************************************************************************
Run the application:
streamlit run app.py
*******************************************************************************************************************
Future Plans
*******************************************************************************************************************
Implement additional filters, such as HDR effect and cartoonification.
*******************************************************************************************************************
Improve performance for even larger image sizes.
*******************************************************************************************************************
Add options for image enhancements like brightness, contrast, and saturation adjustments.

Conclusion
********************************************************************************************************************
PhotoEditor is more than just an image editing app—it is a showcase of your technical proficiency in Python, OpenCV, and Streamlit, and highlights your ability to solve real-world challenges, all while creating an intuitive, user-friendly experience. This project is a testament to how powerful image processing can be made accessible, making it the perfect addition to your GitHub brag portfolio.

# photo-editor-streamlit-app
Streamlit Photo Editor Application

## Introduction and Vision
In today’s world, image processing isn’t just for professionals. With social media booming and high-quality cameras in everyone’s pocket, the need for simple, easy-to-use photo editing tools is higher than ever. But what if you could take a professional approach, using complex algorithms, and make them accessible to anyone?

This is where PhotoEditor, built using Streamlit and OpenCV, comes in. It is designed to be a powerful yet intuitive web-based tool, allowing users to upload their own images and apply sophisticated filters like edge detection, vignette effects, pencil sketching, and stylization—all with the click of a button. Best of all, this project is part of a GitHub brag portfolio, showcasing real-world problem-solving skills and the creation of a polished, user-friendly image editing solution.

## Features
- **Edge Detection**: Detect and highlight edges in the uploaded image using OpenCV’s Canny algorithm.
- **Vignette**: Apply a vignette effect to darken the edges of the image and focus on the center.
- **Pencil Sketch**: Convert the image into a detailed black-and-white pencil sketch.
- **Stylization**: Apply an artistic, painterly effect to the image using advanced OpenCV filters.
- **Real-Time Processing**: Process and preview filters in real-time as the user uploads and selects a filter.

## Challenge & Motivation
The primary goal of this project is to demonstrate proficiency in image processing, web-based interface design, and real-time performance optimization. The challenge wasn’t just to create another photo editor; it was to build a professional-grade application that handles real-world challenges such as:
- Managing large images
- Optimizing performance
- Providing a seamless user experience

Additionally, this project highlights how advanced technical concepts, like OpenCV’s image filters and algorithms, can be made accessible to non-technical users via a highly intuitive web interface.

## Challenges and Solutions

### Challenge: Incorrect Color Display in Uploaded Image
**Problem Encountered**:  
While building the app, the uploaded images appeared with incorrect colors—blue regions appeared orange and vice versa.

**Steps Taken to Resolve**:
- Initial Hypothesis: The issue was suspected to be with the image upload process.
- Research: The problem was identified as a mismatch between OpenCV’s default BGR format and Streamlit’s RGB format.
- **Solution**: Applied a conversion using `cv2.cvtColor()` to transform the image from BGR to RGB before displaying it in Streamlit:
  ```python
  img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
# photoeditor-streamlit-app
