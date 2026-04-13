import streamlit as st
import google.generativeai as genai
import os

# Configure Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-flash")

st.set_page_config(page_title="Madhouse AI Creator Studio", layout="centered")

st.title("🔥 Madhouse AI Creator Studio")
st.write("Paste YouTube link → get content engine")

url = st.text_input("Paste YouTube Link")

if st.button("Generate Content"):

    if not url:
        st.error("Please enter a link")
    else:
        st.success("🚀 Processing...")

        prompt = f"""
You are a high-level content strategist.

Analyze this YouTube video link:
{url}

IMPORTANT:
- You cannot access the video directly
- Infer content based on typical structure and topic
- Keep timestamps realistic and sequential

---

OUTPUT:

1. SUMMARY
- 5–7 bullet points

---

2. SHORTS (5)

Short 1:
Timestamp:
Hook:
Title:
Caption:
On-screen text:

Short 2:
Timestamp:
Hook:
Title:
Caption:
On-screen text:

Short 3:
Timestamp:
Hook:
Title:
Caption:
On-screen text:

Short 4:
Timestamp:
Hook:
Title:
Caption:
On-screen text:

Short 5:
Timestamp:
Hook:
Title:
Caption:
On-screen text:

---

3. INSTAGRAM POST
Caption + hashtags

---

4. LINKEDIN POST
Professional + insight-driven

---

5. TWITTER THREAD
4–6 tweets

---

6. SEO BLOG
Title
Meta description
Keywords
Article (400–600 words)
"""

        try:
            response = model.generate_content(prompt)
            st.subheader("🚀 Output")
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
