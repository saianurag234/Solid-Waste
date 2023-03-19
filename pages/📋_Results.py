import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import cv2
import numpy as np
import time
import tensorflow as tf


model = tf.keras.models.load_model('waste_vgg16.h5')

def import_n_pred(image_data,model):
    size = (224,224)
    image = cv2.resize(image_data,size)
    image = image.astype('float32') / 255.0
    image = np.expand_dims(image, axis=0) 
    pred = model.predict(image)
    return pred

if 'image' in st.session_state:
    image = st.session_state['image']
    prediction = import_n_pred(image,model)
    pred = prediction[0][0]

    st.image(image,  width=450)
    
    if(pred < 0.5):
        st.title("The waste is Organic and Bio-degradable")
    else:
        st.title("The waste is Recyclable")
       
else:
    st.write("No image is found")
    
    
back = st.button("Click here to try again")
if back:
    switch_page("Upload Image")
