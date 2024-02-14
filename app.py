import streamlit as st
from PIL import Image
import numpy as np
import base64

st.write('# RGB to Grayscale')

uploaded_file = st.file_uploader(label='원본 이미지를 업로드해주세요', type=['png', 'jpg', 'jpeg'])

def render_svg(svg):
    """Renders the given svg string."""
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = r'<img src="data:image/svg+xml;base64,%s"/>' % b64
    st.write(html, unsafe_allow_html=True)

svg = """
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><!--!Font Awesome Free 6.5.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.--><path d="M438.6 278.6c12.5-12.5 12.5-32.8 0-45.3l-160-160c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3L338.8 224 32 224c-17.7 0-32 14.3-32 32s14.3 32 32 32l306.7 0L233.4 393.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0l160-160z"/></svg>
"""

grayscale_numpy = None;

if uploaded_file is not None:
  grayscale = Image.open(uploaded_file).convert('L')
  grayscale_numpy = np.array(grayscale, 'uint8')

col1, col2, col3 = st.columns([4,2,4]);

if uploaded_file is not None:
  with col1:
    st.image(uploaded_file)

  with col2:
    render_svg(svg)

with col3:
  if grayscale_numpy is not None:
    st.image(grayscale_numpy)