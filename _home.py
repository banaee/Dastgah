import streamlit as st
from view import st_config
from view import st_gadgets

# STREAMLIT: Some global Configs ============================================
st_config.init()


if st_gadgets.check_password():
    st.markdown("### 🏠 Welcome to ...")
    st.markdown("#### << Select one of the modules")
