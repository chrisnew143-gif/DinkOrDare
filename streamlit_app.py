import streamlit as st
import base64

st.set_page_config(page_title="Pickleball Manager", layout="centered")

# =========================
# SET BACKGROUND IMAGE
# =========================
def set_bg(image_file):
    with open(image_file, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        /* FULL PAGE CENTERING */
        .main > div {{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }}

        .block-container {{
            background: rgba(255, 255, 255, 0.85);
            padding: 3rem;
            border-radius: 20px;
            text-align: center;
            max-width: 500px;
            width: 100%;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg("DFORHPHOTO1.jpg")

# =========================
# CONTENT
# =========================
st.title("🏠 Dink4Health Official Club")
st.write("Welcome to the Dink4Health Club!")

st.divider()

if st.button("🎾 Open Play Stacking", use_container_width=True):
    st.switch_page("pages/AutoStack.py")

st.divider()

if st.button("🏆 DUPR Match", use_container_width=True):
    st.switch_page("pages/DUPRMatch.py")

st.divider()

if st.button("🏆Player Profile", use_container_width=True):
    st.switch_page("pages/PlayerProfile.py")
