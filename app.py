import streamlit as st
import google.generativeai as genai
import os
from youtube_transcript_api import YouTubeTranscriptApi

# Configure Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-flash")

# UI
st.title("🔥 Madhouse AI Creator Studio")
st.write("Paste YouTube link → get full content engine")

url = st.text_input("Paste YouTube Link")

def get_video_id(url):
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("/")[-1]
    return None

if st.button("Generate Content"):

    if not url:
        st.error("Please enter a link")
    else:
        st.success("🚀 Processing...")

        video_id = get_video_id(url)

        try:
            # Fetch transcript (multi-language)
            transcript_data = YouTubeTranscriptApi().fetch(video_id, languages=['hi', 'en'])

            transcript_text = ""
            for entry in transcript_data:
                transcript_text += entry.text + " "

            # Translate to clean English
            translation_prompt = f"""
            Convert this transcript into clean English:

            {transcript_text[:4000]}
            """

            translated = model.generate_content(translation_prompt).text

            # MAIN PROMPT
            prompt = f"""
You are an expert content strategist and viral growth operator.

You are given a transcript from a YouTube video.

------------------------

TRANSCRIPT:
{translated}

------------------------

Follow these rules STRICTLY:

- Use REAL FLOW of content
- Hooks must be HIGHLY engaging
- Captions must be viral-ready
- Blog must be SEO optimized

------------------------

OUTPUT FORMAT:

### 1. SUMMARY
- 5–7 bullet points

------------------------

### 2. SHORTS

Create 3 shorts.

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

------------------------

### 3. INSTAGRAM POST
Caption + hashtags

------------------------

### 4. LINKEDIN POST
Professional + insight

------------------------

### 5. TWITTER THREAD
3–5 tweets

------------------------

### 6. SEO BLOG

Title:
Meta Description:
Keywords:
Article:
"""

            response = model.generate_content(prompt)
            result = response.text

            # OUTPUT
            st.subheader("📄 Transcript (English)")
            st.write(translated)

            st.subheader("🚀 Generated Content")
            st.write(result)

        except Exception as e:
            st.error("❌ Could not fetch transcript (video may be restricted or no captions)")
