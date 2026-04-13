import streamlit as st
import google.generativeai as genai
import os

# Configure API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

# UI
st.set_page_config(page_title="Madhouse AI Creator Studio", layout="centered")

st.title("🔥 Madhouse AI Creator Studio")
st.write("Turn any YouTube video into a full content engine 🚀")

url = st.text_input("Paste YouTube Link")

if st.button("Generate Content"):

    if not url:
        st.error("Please enter a link")

    else:
        st.success("🚀 Processing started...")

        prompt = f"""
        You are an expert content strategist and video repurposing specialist.

        Given this YouTube video:
        {url}

        Generate a COMPLETE content engine output:

        -----------------------------

        1. 🔹 SUMMARY
        - 5-6 crisp bullet points

        -----------------------------

        2. 🎬 SHORT FORM CONTENT

        Generate 3 HIGH-ENGAGEMENT short video ideas:

        For EACH short provide:
        - Timestamp range (e.g., 0:45–1:10)
        - Hook (VERY catchy first line)
        - Title
        - Caption (with emojis)
        - On-screen subtitles text

        Make them VIRAL, emotional, curiosity-driven.

        -----------------------------

        3. 📸 INSTAGRAM

        - 3 captions
        - Each must:
          - Start with a hook
          - Include emojis
          - Include hashtags

        -----------------------------

        4. 💼 LINKEDIN POST

        - Professional tone
        - Storytelling format
        - Strong opening line
        - Clear takeaway

        -----------------------------

        5. 📝 SEO BLOG

        - Title (SEO optimized)
        - Meta description
        - Headings (H1, H2, H3)
        - 300–500 words
        - Include keywords naturally

        -----------------------------

        Format everything clearly with sections.
        """

        try:
            response = model.generate_content(prompt)
            output = response.text

            st.subheader("📄 Generated Content")
            st.write(output)

        except Exception as e:
            st.error(f"Error: {e}")
