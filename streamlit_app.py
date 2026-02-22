import streamlit as st

st.set_page_config(page_title="Pickleball Manager", layout="centered")

# =========================
# HEADER PHOTO
# =========================
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image("DFORHphoto.jpg", width=300)

st.title("🏠 Dink4Health Official Club")
st.write("Welcome to the Dink4Health Club!")

st.divider()

# Open Play Button
if st.button("🎾 Open Play Stacking", use_container_width=True):
    st.switch_page("pages/AutoStack.py")

st.divider()

# DUPR Match Button
if st.button("🏆 DUPR Match", use_container_width=True):
    st.switch_page("pages/DUPRMatch.py")

st.divider()
