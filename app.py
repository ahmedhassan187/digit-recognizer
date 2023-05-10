import streamlit as st
import cv2
import numpy as np
from Utilites import *
import tensorflow as tf
usage = Model()
# Create a file uploader widget
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

# Check if an image was uploaded
if uploaded_file is not None:
    # Use OpenCV to read the uploaded image file
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    new_image = usage.process_image(image)
    reshaped = usage.reshape_im(new_image)
    number = usage.prediction(reshaped)
    fig,ax = plt.subplots()
    plt.imshow(new_image,cmap="gray")
    st.markdown(f"<h1 style='text-align: center; font-size: 48px;'>{number}</h1>", unsafe_allow_html=True)
    st.pyplot(fig)