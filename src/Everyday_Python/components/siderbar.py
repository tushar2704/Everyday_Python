###© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Everyday_Python
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
from src.Everyday_Python.components.header import *
from src.Everyday_Python.components.body import *
from src.Everyday_Python.components.navigation import *
from src.Everyday_Python.components.siderbar import *
from src.Everyday_Python.components.metrics import *
from src.Everyday_Python.components.charts import *
from src.Everyday_Python.components.test import *

#######################################################################################################
# Sidebar of Everyday_Python by github.com/tushar2704
#######################################################################################################

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded


#Left Panel Navigation
def logo():
    custom_css = f"""
    <style>
        .img1{{
            display: block;
            position: top;
            margin: 0;
            padding-left: 10px;
            padding-top:0px;
            width: 150px;
            height: auto;
        }}
        
        
    </style>
    """

      # Example usage in the Streamlit sidebar
    st.sidebar.markdown(custom_css, unsafe_allow_html=True)
    st.sidebar.markdown(f'''[<img class="img1" src='data:image/png;base64,{img_to_bytes("src/Everyday_Python/everyday_python.png")}'>](https://Tushar-Aggarwal.com/)''', unsafe_allow_html=True)
    
    # st.sidebar.markdown(f"##### <span style='margin-left: 45px;'>[Tushar-Aggarwal.com](https://tushar-aggarwal.com/)</span>", unsafe_allow_html=True)

    
    
    
    
    
    
    
    
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
    
   
    
def sidebar():
    # page1()
    with st.sidebar:
        st.page_link("Home.py", label="Home", icon="🏠")
        st.page_link("pages/page1.py", label="Python", icon="🐍")
        # st.page_link("src/Everyday_Python/pages/page2.py", label="Page 2", icon="🐍", disabled=True)
        st.page_link("http://www.tushar-aggarwal.com", label="Portfolio", icon="🌎")
    
    
















































































































































































