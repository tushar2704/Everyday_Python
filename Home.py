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
sheet1,sheet2,sheet3,sheet4,sheet5,sheet6,sheet7,sheet8,sheet9,sheet10,sheet11,sheet12,sheet13,sheet14,sheet15,sheet16,sheet17,sheet18, sheet19, sheet20, sheet21, sheet22, sheet23, sheet24, sheet25=st.tabs(
    ["Commons","Pip","OS","CLI","Files","Http","Lists","Dict",
     "Math","DB","GraphQL","Regex","Strings","Scraping","Async","Network","DF","NP","Plots","SKL","Px",
     "Time", "Adv","OOPs","Deco"]
    )


with sheet1:
    common_python()
with sheet2:
    pip_()
with sheet3:
    os_()
with sheet4:
    cli()


with sheet5:
    file_handling()


with sheet6:
    http_apis()


with sheet7:
    list()


with sheet8:
    dict()


with sheet9:
    math()


with sheet10:
    databases()


with sheet11:
    graphql()


with sheet12:
    re_()


with sheet13:
    strings()


with sheet14:
    web_scraping

with sheet15:
    async_()
    
with sheet16:
    network()
    
with sheet17:
    df_()
    
with sheet18:
    numpy_()

with sheet19:
    plots()
    
with sheet20:
    scikit_()
    
with sheet21:
    plotly_()
    
with sheet22:
    time_()
    
with sheet23:
    adv_()
    
with sheet24:
    oop()
    
with sheet25:
    deco_()
    

#######################################################################################################
#End of Everyday_Python by github.com/tushar2704
#######################################################################################################










footer()
#######################################################################################################
#End of Everyday_Python by github.com/tushar2704
#######################################################################################################
