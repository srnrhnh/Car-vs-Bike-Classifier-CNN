import streamlit as st
from eda import run_eda
from prediction import make_prediction

def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Select", ["Home", "EDA", "Prediction"])

    if selection == "Home":
        st.title("Welcome to the Vehicle Prediction Application")
        st.subheader("By Serina Roihaanah",divider = 'rainbow')
        st.write(
            "This application is designed to provide insights and predictions related to vehicle images. "
            "It features two main functionalities:"
        )

        st.subheader("1. Exploratory Data Analysis (EDA)")
        st.write(
            "In the EDA section, you can explore various visualizations and statistical summaries of the vehicle dataset. "
            "The visualizations will help you gain a deeper understanding of the data and make more informed decisions based on historical behavior."
        )
        st.markdown(
            """
            <style>
            .big-font {
                font-size:20px !important;
                color: #4CAF50;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.markdown('<p class="big-font">Explore insights and enhance your vehicle classification strategies!</p>', unsafe_allow_html=True)

        st.subheader("2. Prediction Model")
        st.write(
            "The Prediction section allows you to upload an image of a vehicle and predict whether it is a car or a motorcycle. "
            "By uploading an image, you will receive a prediction indicating the classification of the vehicle. "
            "This feature is beneficial for developers or users who want to quickly and accurately identify vehicle types."
        )
        st.markdown(
            """
            <style>
            .highlight {
                color: #FF5733;
                font-weight: bold;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.markdown('<p class="highlight">Make informed decisions to enhance your vehicle identification!</p>', unsafe_allow_html=True)

    elif selection == "EDA":
        run_eda()  # Call EDA function
    elif selection == "Prediction":
        make_prediction()  # Call prediction function

if __name__ == "__main__":
    main()
