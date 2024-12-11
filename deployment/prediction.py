import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.vgg16 import preprocess_input
from keras.models import load_model
from PIL import Image
import numpy as np

# Load pretrained model
model_tl = load_model('model_tl.h5')

# Preprocess input image
def preprocess_image(image, target_size=(224, 224)):
    """
    Preprocess the uploaded image to match the input requirements of the model.
    - Resize the image to 224x224.
    - Convert the image to a NumPy array.
    - Apply preprocess_input for VGG16.
    """
    image = image.resize(target_size)  # Resize image
    image = img_to_array(image)       # Convert to array
    image = preprocess_input(image)   # Apply preprocessing for VGG16
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

# Function to make prediction
def make_prediction():
    st.title("Car vs Bike Image Classification")
    st.write("Upload an image with a car or bike object. Supported formats: jpg, jpeg, png.")

    # Upload image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Open the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        st.write("Processing...")

        # Preprocess the image
        processed_image = preprocess_image(image)

        # Make prediction
        prediction = model_tl.predict(processed_image)

        # Interpret prediction
        if prediction[0][0] > 0.5:  # Probability > 0.5 is "Car"
            st.write("### The object in this picture is **Car** 🚗")
        else:  # Probability <= 0.5 is "Bike"
            st.write("### The object in this picture is **Bike** 🏍️")

# Main function
if __name__ == "__main__":
    make_prediction()
