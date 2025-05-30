import streamlit as st
import cv2
import numpy as np
import pytesseract
from PIL import Image


st.title("Dartrix podrá leer cualquier texto que le muestres")
image = Image.open('Dartrix.png')
st.image(image, width=350)

img_file_buffer = st.camera_input("Toma una foto del texto")

with st.sidebar:
      filtro = st.radio("Aplicar Filtro de Claridad",('Con Filtro', 'Sin Filtro'))


if img_file_buffer is not None:
    # To read image file buffer with OpenCV:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    
    if filtro == 'Con Filtro':
         cv2_img=cv2.bitwise_not(cv2_img)
    else:
         cv2_img= cv2_img
    
        
    img_rgb = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    text=pytesseract.image_to_string(img_rgb)
    st.write(text) 
    
st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://i.pinimg.com/736x/31/52/b1/3152b151b84a7016d0d150b5780944eb.jpg")
    }
   .sidebar .sidebar-content {
        background: url("https://i.pinimg.com/736x/31/52/b1/3152b151b84a7016d0d150b5780944eb.jpg")
    }
    </style>
    """,
    unsafe_allow_html=True
)

    


