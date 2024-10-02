import streamlit as st
import cv2
import numpy as np
from filters import edge_detection, vignette, pencil_sketch, stylization

# Title and description of the app
st.title("PhotoEditor Application")
st.write("Upload your image, apply filters, and download the result.")

# Sidebar for filter selection
st.sidebar.title("Select a Filter")

# File uploader for image upload
uploaded_file = st.file_uploader("Upload your image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Convert file to OpenCV format
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img_bgr = cv2.imdecode(file_bytes, 1)  # Decode the image into OpenCV format (BGR)
    
    # Convert BGR to RGB for correct color display in Streamlit
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    
    st.image(img_rgb, caption='Uploaded Image', use_column_width=True)  # Display uploaded image in correct colors

    # Let user select a filter from the sidebar
    filter_option = st.sidebar.selectbox("Filter Type", ["Edge Detection", "Vignette", "Pencil Sketch", "Stylization"])

    # Make a copy of the image for applying the filter (still in BGR for OpenCV processing)
    img_copy = img_bgr.copy()

    # Apply filters based on user selection
    if filter_option == "Edge Detection":
        st.write("Applying Edge Detection...")
        img_filtered = edge_detection.apply_edge_detection(img_copy)  # Apply edge detection filter
        img_filtered_rgb = cv2.cvtColor(img_filtered, cv2.COLOR_BGR2RGB)  # Convert filtered image back to RGB
        st.image(img_filtered_rgb, caption="Edge Detection Applied", use_column_width=True)

    elif filter_option == "Vignette":
        st.write("Applying Vignette...")
        img_filtered = vignette.apply_vignette(img_copy)  # Apply vignette filter
        img_filtered_rgb = cv2.cvtColor(img_filtered, cv2.COLOR_BGR2RGB)  # Convert filtered image back to RGB
        st.image(img_filtered_rgb, caption="Vignette Applied", use_column_width=True)

    elif filter_option == "Pencil Sketch":
        st.write("Applying Pencil Sketch...")
        img_filtered = pencil_sketch.apply_pencil_sketch(img_copy)  # Apply pencil sketch filter
        st.image(img_filtered, caption="Pencil Sketch Applied", use_column_width=True)  # Pencil sketch is grayscale, no need for RGB conversion

    elif filter_option == "Stylization":
        st.write("Applying Stylization...")
        img_filtered = stylization.apply_stylization(img_copy)  # Apply stylization filter
        img_filtered_rgb = cv2.cvtColor(img_filtered, cv2.COLOR_BGR2RGB)  # Convert filtered image back to RGB
        st.image(img_filtered_rgb, caption="Stylization Applied", use_column_width=True)

    # Convert the filtered image (NumPy array) to PNG format
    is_success, img_buffer = cv2.imencode(".png", img_filtered)
    if is_success:
        # Convert the buffer to bytes
        img_bytes = img_buffer.tobytes()

        # Option to download the filtered image
        st.download_button('Download Result', img_bytes, file_name="filtered_image.png", mime="image/png")
