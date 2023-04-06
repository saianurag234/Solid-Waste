import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.title("Solid Waste Classification")

st.markdown(
   f”””
   <style>
   p {
   background-image: url('https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.istockphoto.com%2Fvector%2Frubbish-bins-for-recycling-different-types-of-waste-on-city-background-sort-plastic-gm1182399503-332004011&psig=AOvVaw2rgWfz9fRBHoqgK_htHsvH&ust=1680871834381000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCKCX79allf4CFQAAAAAdAAAAABAE');
   }
   </style>
   ”””,
   unsafe_allow_html=True)



want_to_contribute = st.button("Click Here to upload the Image")
if want_to_contribute:
    switch_page("Upload Image")
