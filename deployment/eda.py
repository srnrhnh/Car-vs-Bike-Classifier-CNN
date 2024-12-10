import streamlit as st
from PIL import Image
import os

def display_image_with_caption(image_path, caption, width=None):
    img = Image.open(image_path)
    st.image(img, use_column_width=(width is None), width=width)
    st.write(caption)

def run_eda():
    st.title("Visualization of Vehicle Classification")
    st.write("This page aims to provide a clear visualization of vehicle classification in the dataset being used.")
    st.header("",divider='rainbow')

    # Path folder gambar
    folder_path = './'

    st.header("Category Distribution (Cars vs Bikes)")
    display_image_with_caption(
        os.path.join(folder_path, 'image_1.png'), 
        "This pie chart illustrates the distribution of the dataset's categories: cars and bikes.It is evident that the data has the same number in both classes.",
        width=300  
    )

    st.divider()

    st.header("Car Image")
    display_image_with_caption(
        os.path.join(folder_path, 'image_2.png'), 
        "- In this dataset, which is randomly sampled, for the category of cars, it can be seen that the available images feature a variety of car colors. In the displayed images, it appears that the cars are dominated by blue, black, red, and white colors. This may lead to prediction errors for vehicles with unusual colors." 
        "\n- Visually, it can be seen that the displayed images have different sizes." 
        "\n- Visually, these car images have diverse backgrounds."
    )

    st.divider()

    st.header("Bike Image")
    display_image_with_caption(
        os.path.join(folder_path, 'image_3.png'), 
        "- In this dataset, which is randomly sampled, for the category of bikes, it can be visually observed that the available bike images are predominantly black in color." 
        "\n- Visually, it can be seen that the displayed images have different sizes." 
        "\n- Visually, these bike images have diverse backgrounds."
    )

if __name__ == "__main__":
    run_eda()