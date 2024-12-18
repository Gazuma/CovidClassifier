import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np
import cv2
import tempfile
model = load_model('pneumonia.keras')

def preprocess_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (256, 256))
    img = np.expand_dims(img, axis=0)
    return img


def predict(image_path):
    # Preprocess the image
    processed_img = preprocess_image(image_path)
    
    # Make prediction
    prediction = model.predict(processed_img)
    return prediction

st.title('Chest X-ray Pneumonia Classifier')
st.write("Made by - Deep Raut, Varun Kadu, Devanshu Bhagwatkar")
st.write('Upload an image for prediction')
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    temp_image = tempfile.NamedTemporaryFile(delete=False)
    temp_image.write(uploaded_file.read())
    st.image(temp_image.name, caption='Uploaded Image', use_column_width=True)
    prediction = predict(temp_image.name)
    if(prediction==0):
        prediction = "Pneumonia Negative"
    else:
        prediction = "Pneumonia Positive"
    st.write('Prediction:',prediction)
