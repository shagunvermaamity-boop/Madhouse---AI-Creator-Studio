import streamlit as st
import google.generativeai as genai
import os

# Configure API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash-latest")

st.title("🔥 Madhouse AI Creator Studio")
st.write("Paste a YouTube link → get full content stack")

url = st.text_input("Paste YouTube Link")

if st.button("Generate Content"):

    if not url:
        st.error("Please enter a link")
    else:
        st.success("🚀 Processing...")

        prompt = f"""
        You are an AI content engine.

        Input: {url}

        DO NOT download video.

        Generate the following clearly structured:

        ===== TRANSCRIPT =====
        A detailed summary of the video

        ===== SHORTS =====
        Create 5 shorts:

        Short 1:
        Timestamp:
        Hook:
        Caption:

        Short 2:
        Timestamp:
        Hook:
        Caption:

        Short 3:
        Timestamp:
        Hook:
        Caption:

        Short 4:
        Timestamp:
        Hook:
        Caption:

        Short 5:
        Timestamp:
        Hook:
        Caption:

        ===== INSTAGRAM =====
        Viral caption with emojis and hashtags

        ===== LINKEDIN =====
        Professional post

        ===== TWITTER =====
        3 engaging tweets (thread style)

        ===== BLOG =====
        SEO optimized blog:
        - Title
        - Meta description
        - Keywords
        - Full article
        """

        response = model.generate_content(prompt)
        result = response.text

        # Display clean sections

        st.subheader("📄 Transcript")
        if "===== TRANSCRIPT =====" in result:
            st.write(result.split("===== TRANSCRIPT =====")[1].split("===== SHORTS =====")[0])

        st.subheader("🎬 Shorts")
        if "===== SHORTS =====" in result:
            st.write(result.split("===== SHORTS =====")[1].split("===== INSTAGRAM =====")[0])

        st.subheader("📸 Instagram")
        if "===== INSTAGRAM =====" in result:
            st.write(result.split("===== INSTAGRAM =====")[1].split("===== LINKEDIN =====")[0])

        st.subheader("💼 LinkedIn")
        if "===== LINKEDIN =====" in result:
            st.write(result.split("===== LINKEDIN =====")[1].split("===== TWITTER =====")[0])

        st.subheader("🐦 Twitter")
        if "===== TWITTER =====" in result:
            st.write(result.split("===== TWITTER =====")[1].split("===== BLOG =====")[0])

        st.subheader("📝 Blog (SEO)")
        if "===== BLOG =====" in result:
            st.write(result.split("===== BLOG =====")[1])
