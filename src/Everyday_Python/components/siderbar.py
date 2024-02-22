##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##All-About-Langchain
#######################################################################################################
#Importing dependecies
#######################################################################################################

import streamlit as st
from pathlib import Path
import base64
import sys
from pathlib import Path
script_dir = Path(__file__).resolve().parent
project_root = script_dir.parent
sys.path.append(str(project_root))
import warnings
warnings.filterwarnings("ignore")
import os


#######################################################################################################
#Importing from SRC
#######################################################################################################
from src.all_about_langchain.components.header import *
from src.all_about_langchain.components.body import *
from src.all_about_langchain.components.navigation import *
from src.all_about_langchain.components.siderbar import *
from src.all_about_langchain.components.metrics import *
from src.all_about_langchain.components.charts import *
from src.all_about_langchain.components.test import *


#######################################################################################################
#sidebar of all_about_llms by github.com/tushar2704
#######################################################################################################

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded


#Left Panel Navigation
def left_main_panel():
    custom_css = f"""
    <style>
        .sidebar .stImage {{
            display: block;
            margin: 0;
            padding: 0;
        }}
        .st-emotion-cache-10oheav {{padding: 0.1rem 0.2rem;}}
        img{{
            vertical-align: middle;
            margin-right: 70px;
            float:right;
        }}
    </style>
    """

      # Example usage in the Streamlit sidebar
    st.sidebar.markdown(custom_css, unsafe_allow_html=True)
    # st.sidebar.markdown(f'''[<img src='data:image/png;base64,{img_to_bytes("src/QueryMaster/images/data unboxed.png")}' class='img-fluid' width=100 height=100>](https://Tushar-Aggarwal.com/)''', unsafe_allow_html=True)
    
    st.sidebar.markdown(f"##### <span style='margin-left: 45px;'>[Tushar-Aggarwal.com](https://tushar-aggarwal.com/)</span>", unsafe_allow_html=True)

    
    
    
    
    
    
    
    
def sidebar_main():
    with st.sidebar:
        main_navbar =option_menu(
            menu_title="",
            options=['Basics','Intermediate', 'Advanced'],
            icons=['magic','blockquote-left','body-text'],
            menu_icon="house-fill",
            default_index=0, 
            )
    
    if main_navbar=="Basics":
        st.write("testing")
    if main_navbar=="Intermediate":
        st.write("testing1")
    if main_navbar=="Advanced":
        st.write("testing2")
    
   
    
        
    
















































































































































































