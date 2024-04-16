from dotenv import load_dotenv
load_dotenv()##loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

##fun to load gemini pro model and get response
model=genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

##initialize our streamlit app

st.set_page_config(page_title="ChatAi")

st.header("MED chat Bot")

input=st.text_input("Ask me question: ",key="input")
submit=st.button("Submit")

##when submit is clicked

if submit:
    response=get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)
