# Install the client library and import necessary modules.
import google.generativeai as genai
import base64
import io
import json
import mimetypes
import pathlib
import pprint
import requests
import streamlit as st

# Configure the client library by providing your API key.
genai.configure(api_key='AIzaSyBFCeAPTlZiYw9NYrrRPvw4pETGFo6Awuc')
generation_config_b64 = 'eyJ0ZW1wZXJhdHVyZSI6MC45LCJ0b3BfcCI6MSwidG9wX2siOjEsIm1heF9vdXRwdXRfdG9rZW5zIjoyMDQ4LCJzdG9wX3NlcXVlbmNlcyI6W119' # @param {isTemplate: true}
safety_settings_b64 = 'W3siY2F0ZWdvcnkiOiJIQVJNX0NBVEVHT1JZX0hBUkFTU01FTlQiLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn0seyJjYXRlZ29yeSI6IkhBUk1fQ0FURUdPUllfSEFURV9TUEVFQ0giLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn0seyJjYXRlZ29yeSI6IkhBUk1fQ0FURUdPUllfU0VYVUFMTFlfRVhQTElDSVQiLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn0seyJjYXRlZ29yeSI6IkhBUk1fQ0FURUdPUllfREFOR0VST1VTX0NPTlRFTlQiLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn1d' # @param {isTemplate: true}
generation_config = json.loads(base64.b64decode(generation_config_b64))
safety_settings = json.loads(base64.b64decode(safety_settings_b64))
model = 'gemini-pro'


with st.sidebar:
    st.title("PoeAIm")
    st.write('With an intuitive user interface and a user-friendly design, this web application invites users to embark on a creative odyssey. By simply providing a few details about the individual, such as their name, interests, and passions, the application harnesses the transformative power of Gemini Pro to generate a personalized poem. Whether it"s a heartfelt tribute to a loved one, a celebration of personal achievements, or a reflective exploration of lifes complexities, the application adapts to the users preferences, producing poems that resonate with authenticity and emotional depth.')

aoi = [
    "Reading",
    "Writing",
    "Listening to music",
    "Watching movies",
    "Playing ",
    "Traveling",
    "Cooking",
    "Gardening",
    "Photography",
    "Learning new skills",
    "Meditation",
    "Family Time",
    "Volunteering",
    "Technology",
    "Science",
    "History",
    "Politics",
    "Economics",
    "Philosophy",
    "Psychology",
    "Sociology",
    "Art",
    "Music",
    "Literature",
    "Fashion",
    "Travel",
    "Food and drink",
    "Health and wellness",
    "Sports",
    "Current events",
    "Sports",
    "Researching",
    "Spiritual Journeys"
]

col1, col2, col3 = st.columns(3)
with col1:
    name = st.text_input('Name')
    age = st.text_input('Age')
    interest = st.multiselect('Interests',options=aoi)
    others = st.text_input('Other interest (if any)',placeholder='separated by comma')

with col2:
    Country = st.text_input('Country')
    state = st.text_input('State ')
    profession = st.text_input('Profession')
    fav_singer = st.text_input('Favourite singer',placeholder='separated by comma')
    fav_movie = st.text_input('Favourite movie/Web Show/Drama ', placeholder='separated by comma')

with col3:
    gender = st.selectbox('Gender',options=['Male','Female'])
    fav_songs = st.text_input('Favourite Songs/Gazals', placeholder='separated by comma')
    language = st.selectbox('What language would you recommend for this poem?',options=['English','Hindi', 'Telugu'])
    

contents = 'A person whose name is '+name+'. Gender is '+gender+'. Age is '+age+'. Area of interest are '+",".join(interest)
contents += '. Lives in state of '+state+' located in country '+Country+'.'
contents += 'Profession is '+profession+'. Favourite show and movies are '+fav_movie+'. And Favourite songs are '+fav_songs+'.'
contents += 'Write a  quality poem  describing the person"s specified incident which will be a masterpiece when read by a user . Language of the poem would be'+language+'.'

a = st.button('Generate',key='gen')
if st.session_state.get("gen"):
    with st.spinner('Wait for it'):
        gemini = genai.GenerativeModel(model_name=model)
        response = gemini.generate_content(
            contents,
            generation_config=generation_config,
            safety_settings=safety_settings,
            stream=False)

        if generation_config.get('candidate_count', 1) == 1:
            try:
                st.text_area(label ="",value=response.text,height=500)
            except Exception as e:
                st.failure('Retry after Some time')
        else:
            st.failure('It is Prohibited.')
        
    st.success('Done')
