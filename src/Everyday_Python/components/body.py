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
#Body of Everyday_Python by github.com/tushar2704
#######################################################################################################


main_topics=["File Handling","Working With Simple HTTP APIs","Working With Lists","Working With Dictionaries",
             "Working With The Operating System","Working With CLI — STDIN, STDOUT, STDERR","Working With Mathematical Operations and Permutations",
             "","","",
             "","","",
             "","","",]

sub_stopics=["Reading a File","Writing to a File","Appending to a File","Reading Lines into a List",
             "Iterating Over Each Line in a File","Checking If a File Exists","Writing Lists to a File",
             "Using With Blocks for Multiple Files","Deleting a File","Reading and Writing Binary Files",
             "Basic GET Request","GET Request with Query Parameters","Handling HTTP Errors",
             "Setting Timeout for Requests","Using Headers in Requests","POST Request with JSON Payload",
             "Handling Response Encoding","Using Sessions with Requests","Handling Redirects",
             "Streaming Large Responses","Creating a List","Appending to a List",
             "Inserting into a List","Removing from a List","Popping an Element from a List",
             "Finding the Index of an Element","List Slicing","List Comprehension",
             "Sorting a List","Reversing a List","Creating a Dictionary",
             "Adding or Updating Entries","Removing an Entry","Checking for Key Existence",
             "Iterating Over Keys","Iterating Over Values","Iterating Over Items",
             "Dictionary Comprehension","Merging Dictionaries","Getting a Value with Default",
             "Navigating File Paths","Listing Directory Contents","Creating Directories",
             "Removing Files and Directories","Executing Shell Commands","Working with Environment Variables",
             "Changing the Current Working Directory","Path Existence and Type","Working with Temporary Files",
             "Getting System Information","Reading User Input","Printing to STDOUT",
             "Formatted Printing","Reading Lines from STDIN","Writing to STDERR",
             "Redirecting STDOUT","Redirecting STDERR","Prompting for Passwords",
             "Command Line Arguments","Using Argparse for Complex CLI Interactions","Basic Arithmetic Operations",
             "Working with Complex Numbers","Mathematical Functions","Generating Permutations",
             "Generating Combinations","","",
             "","","",
             "","","",
             "","","",
             "","","",
             "","","",
             "","","",
             "","","",
             "","","",
             "","","",
             "","","",
             "","","",
             "","","",
             "","","",
             "","","",
             "","","",]




























