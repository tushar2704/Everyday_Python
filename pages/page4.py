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
# from src.Everyday_Python.components.header import *
# from src.Everyday_Python.components.body import *
# from src.Everyday_Python.components.navigation import *
# from src.Everyday_Python.components.siderbar import *
# from src.Everyday_Python.components.metrics import *
# from src.Everyday_Python.components.charts import *
# from src.Everyday_Python.components.test import *
#######################################################################################################
#Header of Everyday_Python by github.com/tushar2704
#######################################################################################################

# main_title()

#######################################################################################################
#Page Config of Everyday_Python by github.com/tushar2704
#######################################################################################################
# custom_style()
#######################################################################################################
#Body of Everyday_Python by github.com/tushar2704
#######################################################################################################
# page_header('''
#             ''')


#Sidebar Pages
# with st.sidebar:
#     logo()
#     st.page_link("Home.py", label="Back to Home", icon="🏠")
    
#     st.page_link("pages/page2.py", label="Everyday Cheat Sheets", icon="🐍")
#     st.page_link("pages/page3.py", label="Data Structures", icon="🐍")
#     st.page_link("pages/page5.py", label="Pro Tips", icon="🐍")
    


#######################################################################################################
#Body of Everyday_Python [Interview Questiona] by github.com/tushar2704
#######################################################################################################

def interview_question():
    st.header("Top 500 Python Interview Problems and Solutions")
    
    # Create a two-column layout
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("Common Problems")
        
        st.markdown(
            """
            ##### 1) Write a Python function to check whether a givennumber is prime or not.
            """
        )
        st.code(
            """
            #Proposed Solution
            def is_prime(num):
                if num > 1:
                    for i in range(2, num):
                        if (num % i) == 0:
                            return False
                        else:
                            return True
                            
           
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        
        
        st.markdown(
            """
            ##### 2) Write a Python function to find the largest continuous sum in a given list of integers.
            """
        )
        st.code(
            """
            #Proposed Solution
            def largest_continuous_sum(numbers):
                max_sum = 0
                current_sum = 0
                for number in numbers:
                    current_sum += number
                    if current_sum < 0:
                        current_sum = 0
                    if current_sum > max_sum:
                        max_sum = current_sum
                return max_sum
            
            print(largest_continuous_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
            """
        )
        
        
        
        
        
        
        st.markdown(
            """
            ##### 3) What is the difference erence between 'is' and '==' inPython?
            """
        )
        st.code(
            """
            #The 'is' operator in Python checks if two objects are the sameobject 
            #(i.e., they have the same memory address), whereas the'==' operator checks 
            #if two objects have the same value. Here's anexample:

            # create two different lists with the same elements
            list1 = [1, 2, 3]
            list2 = [1, 2, 3]
            
            # use 'is' to check if they are the same object
            print(list1 is list2) # prints 'False'
            
            # use '==' to check if they have the same value
            print(list1 == list2)# Output: True
            """
        )
        
        
        
        
        st.markdown(
            """
            ##### 4) What is the purpose of the 'enumerate' function in Python? Provide an example.
            """
        )
        st.code(
            """
            #The 'enumerate' function in Python is used to iterate over aniterable 
            #(such as a list) and return a tuple for each element thatincludes the 
            #index of the element and the element itself. Here's anexample:

            my_list = ['a','b','c']
            
            for i, value in enumerate(my_list):
                print(f"Index: {i}, Value: {value})
            """
        )
        
        
        
        
        
        st.markdown(
            """
            ##### 5) What is the purpose of the 'zip' function in Python? Provide an example.
            """
        )
        st.code(
            """
            #The 'zip' function in Python is used to combine multiple iterables(such as lists) 
            # into a single iterable that produces tuples of corresponding elements from 
            # each of the input iterables. Here's anexample:
            
            # create two lists:
            list1=[1,2,3]
            list2=[4,5,6]
            
            # use the 'zip' function to combine the lists combined_list
            combined_list =list(zip(list1, list2))
            
            # print the resulting list of tuples
            print(combined_list)
            """
        )
            
        
    with col2:
        st.subheader("Checking If a File Exists")
        
        st.markdown(
            """
            ##### To check if a file exists before performing file operations:
            """
        )
        st.code(
            """
            import os
            if os.path.exists("Tushar.txt"):
                print("File exists.")
            else:
                print("File does not exists.")
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("Writing Lists to a File")
        
        st.markdown(
            """
            ##### To write each element of a list to a new line in a file:
            """
        )
        st.code(
            """
            lines = ['First line', 'Second line', 'Third line']
            with open("Tushar.txt","w") as file:
                for line in lines:
                    file.write(f'{file}\n')           
            """
        )
        
        
        
        
        st.subheader("Using With Blocks for Multiple Files")
        
        st.markdown(
            """
            ##### To work with multiple files simultaneously using `with` blocks:
            """
        )
        st.code(
            """
            with open("source.txt","r") as source,
                open("destination.txt","w") as destination
                
                content = source.read()
                destination.write(content)
            """
        )
        
        
        st.subheader("Deleting a File")
        
        st.markdown(
            """
            ##### To safely delete a file if it exists:
            """
        )
        st.code(
            """
            import os
            if os.path.exists("Tushar.txt"):
                os.remove("Tushar.txt")
                print("File deleted.")
            else:
                print("File does not exist.")
            """
        )
        
        
        
        st.subheader("Reading and Writing Binary Files")
        
        st.markdown(
            """
            ##### To read from and write to a file in binary mode (useful for images, videos,etc.):
            """
        )
        st.code(
            """
            # Reading a binary file
            with open('image.jpg','rb') as file:
                content = file.read()
            #Writing to a binary file
            with open('copy.jpg','wb') as file:
                file.write(content)
            """
        )





































































































































































































































































































































































































interview_question()
#######################################################################################################
#Body of Everyday_Python [Interview Questiona] by github.com/tushar2704
#######################################################################################################
# footer()