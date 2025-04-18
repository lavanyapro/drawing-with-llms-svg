import streamlit as st
from model.model import Model

st.title("Drawing with LLMs - Text to SVG 🎨")

prompt = st.text_input("Enter a prompt", "A happy sun with sunglasses")
if prompt:
    model = Model()
    svg_code = model.predict(prompt)
    st.markdown("### Generated SVG:")
    st.code(svg_code, language='xml')
    st.image(f"data:image/svg+xml;utf8,{svg_code}")
