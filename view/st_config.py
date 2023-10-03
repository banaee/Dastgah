
import streamlit as st

def init():

    # STREAMLIT: Some Configs ====================================================
    footer_style = """
                <style>
                # MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                footer:after {
                    content:'Powered by Streamlit, developed by FLAI@AASS';
                    visibility: visible;
                    display: block;
                    position: relative;
                    # background-color: white;
                    padding: 5px;
                    top: 2px;
                }
                </style>
                """
    st.markdown(footer_style, unsafe_allow_html=True)
    # st.write(
    #     '<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    st.markdown(
        '<style>.stButton>button {color:black;background-color:#f5dce1;}</style>', unsafe_allow_html=True)
    # display:inline-block

pages = {
    "realtime_alarm_simulation" : 0,
    "realtime_alarm_mqtt" : 1,
    "explore_positions": 2,
    "explore_trajectories": 3,

}