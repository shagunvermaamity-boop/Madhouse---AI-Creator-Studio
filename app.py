import streamlit as st
import google.generativeai as genai
import os
from youtube_transcript_api import YouTubeTranscriptApi

# Configure Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-flash")

# UI
st.title("🔥 Madhouse AI Creator Studio")
st.write("Paste YouTube link → get real content engine")

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
            transcript_data = YouTubeTranscriptApi.get_transcript(video_id)

            # Build transcript text + timestamps
            transcript_text = ""
            timestamps = []

            for entry in transcript_data:
                time = round(entry["start"])
                text = entry["text"]

                transcript_text += text + " "
                timestamps.append(f"{time}s: {text}")

            transcript_preview = " ".join(transcript_text.split()[:300])

            prompt = f"""
            You are an expert content strategist.

            Based on this transcript:
            {transcript_preview}

            Use REAL FLOW from transcript.

            -----------

            1. SUMMARY
            Bullet points

            -----------

            2. SHORTS (based on timestamps)

            Create 3 shorts:

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

            -----------

            3. INSTAGRAM
            Viral caption with hashtags

            -----------

            4. LINKEDIN
            Professional post

            -----------

            5. TWITTER
            3 tweets

            -----------

            6. BLOG (SEO)
            Title
            Meta description
            Keywords
            Article
            """

            response = model.generate_content(prompt)
            result = response.text

            # OUTPUT

            st.subheader("📄 Transcript (Real)")
            st.write(transcript_preview)

            st.subheader("🎬 Shorts")
            st.write(result)

        except Exception as e:
            st.error("Could not fetch transcript. Video may not have captions.")
            st.error(e)
