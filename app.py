import streamlit as st
import google.generativeai as genai
import os

# Configure API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

# UI
st.title("🔥 Madhouse AI Creator Studio")

url = st.text_input("Paste YouTube Link")

if st.button("Generate Content"):

    if not url:
        st.error("Please enter a link")

    else:
        st.success("🚀 Processing started...")

        prompt = f"""
        You are an AI content creator.

        Given this YouTube link:
        {url}

        Generate:

        1. Summary
        2. 3 Instagram captions
        3. 1 LinkedIn post
        4. 1 Blog article
        """

        response = model.generate_content(prompt)
        output = response.text

        st.subheader("📄 Generated Content")
        st.write(output)
