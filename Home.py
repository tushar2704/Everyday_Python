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
    
    st.page_link("pages/page5.py", label="Pro Tips", icon="🐍")
    

 
#######################
#Body
sheet1,sheet2,sheet3,sheet4,sheet5,sheet6,sheet7,sheet8,sheet9,sheet10,sheet11,sheet12,sheet13,sheet14,sheet15=st.tabs(
    ["Files Handling","HTTP APIs","Lists","Dictionary","OS",
     "CLI","Math","Databases","AsyncIO","Network","DataFrame","NumPy","Plots","Scikit-learn","Plotly"]
    )


with sheet1:
    file_handling()


with sheet2:
    http_apis()


with sheet3:
    lists()


with sheet4:
    dict()


with sheet5:
    os_()


with sheet6:
    cli()


with sheet7:
    math()


with sheet8:
    databases()


with sheet9:
    async_()


with sheet10:
    network()


with sheet11:
    df_()


with sheet12:
    numpy_()


with sheet13:
    plots()


with sheet14:
    scikit_()

with sheet15:
    plotly_()

#######################################################################################################
#End of Everyday_Python by github.com/tushar2704
#######################################################################################################










footer()
#######################################################################################################
#End of Everyday_Python by github.com/tushar2704
#######################################################################################################
