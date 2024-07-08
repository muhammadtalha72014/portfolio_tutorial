import streamlit as st
import google.generativeai as genai
import os

api_key = st.secrets["GOOGLE_API_KEY"]

genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

col1 , col2 = st.columns(2)

with col1:
    st.subheader("Hi :wave:")
    st.title("I am Muhammad Talha")

with col2:
    st.image("images/WhatsApp Image 2023-06-04 at 11.53.23.jpg")

st.title(" ")

persona = """
        You are Murtaza AI bot. You help people answer questions about your self (i.e Murtaza)
        Answer as if you are responding . dont answer in second or third person.
        If you don't know they answer you simply say "That's a secret"
        Here is more info about Murtaza: 

        Murtaza Hassan is an Educator/Youtuber/Entrepreneur in the field of Computer Vision and Robotics.
        He runs one of the largest YouTube channels in the field of Computer Vision,
        educating over 3 Million developers,
        hobbyists and students. Murtaza obtained his Bachelor’s degree in
        Mechatronics and later specialized in the field of Robotics from
        Bristol University (UK). He is also a serial entrepreneur having launched several
        successful ventures including CVZone, which is a one stop solution for learning 
        and building vision projects. Prior to starting his entrepreneurial career, 
        Murtaza worked as a university lecturer and a design engineer, evaluating 
        and developing rapid prototypes of US patents.

        Murtaza's Youtube Channel: https://www.youtube.com/channel/UCYUjYU5FveRAscQ8V21w81A
        Murtaza's Email: contact@murtazahassan.com 
        Murtaza's Facebook: https://www.facebook.com/murtazasworkshop
        Murtaza's Instagram: https://www.instagram.com/murtazasworkshop/
        Murtaza's Linkdin: https://www.linkedin.com/in/murtaza-hassan-8045b38a/
        Murtaza's Github :https://github.com/murtazahassan
        """

st.title("Artificial Intelligence and Machine Learning Engineer")

user_question = st.text_input("Ask anything about me ")

if st.button("ASK"):
    prompt = persona+" Here is the question that user asked : "+user_question
    response = model.generate_content(prompt)
    print(response.text)
    st.write(response.text)

st.title(" ")

st.title("Robotics Project")

st.video("https://www.youtube.com/watch?v=DxqzwBQVCNw&t=1958s")

st.title(" ")

st.title("My Skills")

st.slider("Python",0,100,80)

st.file_uploader("Upload a files")

st.title("Contact")

st.write("talhahamid123@gmail.com")