import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
from keras.models import load_model
from PIL import Image
import numpy as np

model_tl = load_model('model_tl.h5')

def make_prediction():

    def preprocess_image(image, target_size=(224, 224)):
        image = image.resize(target_size)
        image = img_to_array(image) / 255.0
        image = np.expand_dims(image, axis=0)
        return image

    st.title("Image Classification Prediction")
    st.write("Upload an image with a car or bike object. Available for jpg, jpeg, and png type only.")

    # Mengambil gambar
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Membuka gambar
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        st.write("Processing...")

        # Preprocessing gambar
        processed_image = preprocess_image(image)

        # Melakukan prediksi
        prediction = model_tl.predict(processed_image)

        
        if prediction[0][0] > 0.5:
            st.write("The object of this picture is **Car**")
            color = 'blue'
        else:
            st.write("The object of this picture is **Bike**")
            color = 'red'

            
            
if __name__ == "__main__":
    make_prediction()