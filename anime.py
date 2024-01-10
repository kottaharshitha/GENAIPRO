import streamlit as st
from PIL import Image
from your_image_to_anime_module import convert_to_anime  # Replace with your actual module

st.title("Image to Anime Converter")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Convert to Anime"):
        result_image = convert_to_anime(image)  # Replace with your actual conversion function
        st.image(result_image, caption="Anime Version", use_column_width=True)
