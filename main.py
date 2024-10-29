
import google.generativeai as genai
import os
from dotenv import load_dotenv, find_dotenv
import streamlit as st


#to convert streamlit-image to a pil-image-object, coz the genai model only takes pil-image-object
def st_image_to_pil(st_image):
    import io
    from PIL import Image
    image_data = st_image.read()
    pil_image = Image.open(io.BytesIO(image_data))
    return pil_image


#to create model, generate and return the response
def get_response(prompt, uploaded_image):
    #to create model, generte and return response
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([prompt, uploaded_image])
    return response.text




#to find the .env file and to load the env vars
load_dotenv(find_dotenv(), override=True)
api_key = os.environ.get('GOOGLE_API_KEY')

#to configure the api key
genai.configure(api_key=api_key)


#to design a basic streamlit webpage with a logo, heading and file_uploader
st.image('visualtalk.jpg')
st.subheader('Talk to an image through prompts')
uploaded_image = st.file_uploader('Please upload the image', type=['jpg', 'jpeg', 'png', 'gif', 'webp'])

#to not to display the prompt-area and the button unless a valid image is uploaded
#if a valid image is uploaded, display - image, prompt area and the ask button
if uploaded_image:
    st.image(uploaded_image, caption='Talk with this image') #to display the uploaded image
    prompt = st.text_area('Ask a question about this image: ')
    btn = st.button('Ask')

    # only if prompt is none and the button is clicked
    if prompt and btn:
        with st.spinner("MMMmmmmm......."): #spiiner while fetching the response
            st.write(get_response(prompt, st_image_to_pil(uploaded_image)))




