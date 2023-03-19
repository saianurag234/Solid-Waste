import streamlit as st
from streamlit_extras.switch_page_button import switch_page
st.sidebar.image(https://icon2.cleanpng.com/20180321/ahq/kisspng-recycling-symbol-natural-environment-paper-recycli-environmental-logos-cliparts-5ab27c46258207.7081041315216466621536.jpg, width=50, height=60) 


st.title("Solid Waste Classification")
want_to_contribute = st.button("Click Here to upload the Image")
if want_to_contribute:
    switch_page("Upload Image")
