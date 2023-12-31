import os 
import time
from PIL import Image
import streamlit as st
from main import runner_code

st.header("LLM Diagram Generation")

# Get user inputs
input1 = st.text_input("Paste the Question - ")
input2 = st.text_input("Paste the Answer - ")
input3 = st.text_input("Paste your OpenAI API Key", type="password")
input4 = st.slider('Select a range of values', min_value=0.0, max_value=1.0, value=0.0, step=0.1)

os.environ['OPENAI_API_KEY'] = str(input3)

if st.button("Compute!"):
    # Generate diagram and code
    runner_code(input1, input2, input4)
    time.sleep(2)
    # Display the generated diagram
    image = Image.open('image.gv.png')
    st.image(image, caption='Diagram')