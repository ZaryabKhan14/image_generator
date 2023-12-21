import os

import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("api_key")
# Set your OpenAI API key
client = OpenAI(api_key=api_key)

# Streamlit app title and description
st.title("Text To Image Generator")
st.write("Enter a prompt to generate an image!")

# User input for the prompt
user_input = st.text_input("Enter a prompt:")

# Function to generate and display the image
def generate_and_display_image(text, model="dall-e-3", size="1024x1024", quality="standard"):
    try:
        response = client.images.generate(
            model=model,
            prompt=text,
            size=size,
            quality=quality,
            n=1
        )
        image_url = response.data[0].url
        st.image(image_url,width=800)  # Display the image in the Streamlit app
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Generate and display the image when the user clicks a button
if st.button("Generate Image"):
    generate_and_display_image(user_input)

# Optionally, you can add more Streamlit components for further customization.
