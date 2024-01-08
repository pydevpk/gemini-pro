"""
Gemini Pro demo.
This example demonstrates how to use the Gemini protocol over a StreamLit app, and
how to use the Gemini Pro API to generate text from images.

About Developer:
    LinkedIn: @pydev
    Email: pydev.pk@gmail.com
    Github: @pydevpk
    Twitter: @mrraosahab
    Website: https://pydevpk.github.io
"""

from dotenv import load_dotenv

# load environment variables 
load_dotenv()

import os
import streamlit as st 
import google.generativeai as genai 
from PIL import Image

genai.configure(api_key=os.getenv('API_KEY_GEMINI'))

model = genai.GenerativeModel('gemini-pro-vision')


def get_gemini_response(input, image):
    if input != "":
        response = model.generate_content([input, image])
        return response
    else:
        response = model.generate_content(image)
        return response
    

# setting webpage title 
st.title("Gemini Pro")
# setting webpage header 
st.subheader("A generative AI that can create text from images")
# take an input
input = st.text_input("Enter a text prompt", "")
# take an image
uploader = st.file_uploader("Upload an image", type=['png', 'jpg', 'jpeg'])
image = ""
if not uploader is None:
    image = uploader.read()
    image = Image.open(uploader)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

# creating button on webpage
submit = st.button("know this image")
if submit:
    loader_text = st.empty()
    loader_text.write('Classifying...')
    # st.write("Classifying...")
    # Classify the image
    response = get_gemini_response(input, image)
    # Display the results
    st.write(response.text)
    # replace loader_text 
    loader_text.write('Response from Gemini Pro')