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
from src.Everyday_Python.components.header import *
from src.Everyday_Python.components.body import *
from src.Everyday_Python.components.navigation import *
from src.Everyday_Python.components.siderbar import *
from src.Everyday_Python.components.metrics import *
from src.Everyday_Python.components.charts import *
from src.Everyday_Python.components.test import *
#######################################################################################################
#Header of Everyday_Python by github.com/tushar2704
#######################################################################################################

main_title()

#######################################################################################################
#Page Config of Everyday_Python by github.com/tushar2704
#######################################################################################################
custom_style()
#######################################################################################################
#Body of Everyday_Python by github.com/tushar2704
#######################################################################################################
page_header('''
            ''')



#Sidebar Pages
with st.sidebar:
    logo()
    st.page_link("Home.py", label="Everyday Cheat Sheets", icon="🐍")
    
    # st.page_link("pages/page2.py", label="Everyday Cheat Sheets", icon="🐍")
    # st.page_link("pages/page3.py", label="Data Structures", icon="🐍")
    
    
    


pro1,pro2,pro3, pro4,pro5=st.tabs(["One Liner Py","Common Py","Advanced Py","Interview Code Snippets","Advanced PYTHON"])

with pro1:
    one_liner_60()
    
with pro2:
    common_python()
    
    
with pro3:
    adv_()
    st.divider()
    oop()
    st.divider()
    deco_()
    
with pro4:
    st.write("Interview Code Snippets upcoming...")
    
    
with pro5:
    st.write("Advanced PYTHON upcoming...")
    

footer()


