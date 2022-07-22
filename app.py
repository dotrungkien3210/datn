import streamlit as st
import os
import pandas as pd
from PIL import Image
import streamlit.components.v1 as components

@st.cache
def load_image(image_file):
    img = Image.open(image_file)
    return img

def main():
    st.title("My Graduation Thesis")
    menu = ["Home", "Dataset", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Home":
        st.subheader("UploadImage")
        image_file = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'])
        if image_file is not None:
            file_details = {"File name": image_file.name, "File Type": image_file.type}
            st.write(file_details)
            img = load_image(image_file)
            st.image(img)
            img.save('D:/CODE/python/text_recognition/data/'+image_file.name)
            st.success("File saved")
        if st.button("Use my camera"):
            import take_photo
            take_photo.capture_image()

        if st.button("Recognise"):
            import pipeline
            pipeline.start_process()
    elif choice == "Dataset":
        st.subheader("Dataset")
        data_file = st.file_uploader("Upload_csv", type=['csv'])
        if data_file is not None:
            file_details = {"File name": data_file.name, "File type": data_file.type}
            st.write(file_details)
            df = pd.read_csv(data_file, encoding="utf-8")
            st.dataframe(df)
            st.success("Done")
    else:
        st.subheader("About App")


if __name__ == '__main__':
    main()
