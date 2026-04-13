import streamlit as st
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="Madhouse AI Creator Studio", layout="centered")

st.title("🔥 Madhouse AI Creator Studio")
st.write("Paste a YouTube link → get full content stack")

url = st.text_input("Paste YouTube Link")

if st.button("Generate Content"):

    if not url:
        st.error("Please enter a link")

    else:
        st.success("🚀 Processing...")

        prompt = f"""
You are a content repurposing engine.

Input: {url}

Generate structured output:

=== SUMMARY ===
5 bullet points

=== SHORTS (3) ===
For each:
- Timestamp
- Hook (viral)
- Title
- Caption
- On-screen subtitles

=== INSTAGRAM ===
3 captions with hooks + hashtags

=== LINKEDIN ===
1 professional post

=== SEO BLOG ===
- Title
- Meta description
- Headings
- 300-500 words
"""

        try:
            response = model.generate_content(prompt)
            st.subheader("📄 Output")
            st.write(response.text)
        except Exception as e:
            st.error(str(e))
