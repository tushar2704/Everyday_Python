##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
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
# # from src.Everyday_Python.components.header import *
# from src.Everyday_Python.components.body import *
# from src.Everyday_Python.components.navigation import *
# from src.Everyday_Python.components.siderbar import *
# from src.Everyday_Python.components.metrics import *
# from src.Everyday_Python.components.charts import *
# from src.Everyday_Python.components.test import *

#######################################################################################################
#Pages(1) of Everyday_Python by github.com/tushar2704
#######################################################################################################




#Sidebar Pages
with st.sidebar:
    st.page_link("Home.py", label="Back to Home", icon="🏠")
    
    st.page_link("pages/page1.py", label="Python", icon="🐍")
    st.page_link("pages/page2.py", label="Everyday Cheat Sheets", icon="🐍")
    st.page_link("pages/page4.py", label="Chatbot", icon="🐍")
    st.page_link("pages/page5.py", label="Pro Tips", icon="🐍")
    st.page_link("http://www.tushar-aggarwal.com", label="Tushar Aggarwal", icon="🌎")


def page1():
    st.header("Python Data Structures")


page1()