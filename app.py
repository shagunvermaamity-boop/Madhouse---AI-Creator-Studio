import streamlit as st

st.title("🔥 Madhouse AI Creator Studio")

url = st.text_input("Paste YouTube Link")

if st.button("Generate Content"):
    if not url:
        st.error("Please enter a link")
    else:
        st.success("🚀 Processing started...")

        # Sections (empty but clean)
        st.subheader("📄 Transcript")
        st.divider()

        st.subheader("📸 Instagram")
        st.divider()

        st.subheader("💼 LinkedIn")
        st.divider()

        st.subheader("📝 Blog")
        st.divider()
