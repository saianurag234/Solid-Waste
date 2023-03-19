import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.title("Solid Waste Classification")

img_url = "https://raw.githubusercontent.com/saianurag234/Solid-Waste/main/images/SolidWaste.jpg"
st.image(img_url, width=650)

want_to_contribute = st.button("Click Here to upload the Image")
if want_to_contribute:
    switch_page("Upload Image")
