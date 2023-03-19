import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.title("Solid Waste Classification")

img_url = "https://raw.githubusercontent.com/saianurag234/Solid-Waste/main/images/SolidWaste.jpg"
st.image(img_url, width=650)

want_to_contribute = st.button("Click Here to upload the Image")
if want_to_contribute:
    switch_page("Upload Image")

# Use the Streamlit `beta_container()` function to create a container
button_container = st.beta_container()

# Add the left button to the container using `button_container.button()`
with button_container:
    left_button = st.button("Left button")

# Add the right button to the container using `button_container.button()`
with button_container:
    right_button = st.button("Right button", key="right_button", help="This is the right button")

# Use CSS to position the buttons within the container
button_container.write("""
<style>
div.stButton > button:first-child {
    margin-right: 1em;
}
</style>
""", unsafe_allow_html=True)
