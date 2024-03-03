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
             "Working With Databases","Working With Async IO (Asyncrounous Programming)","Working With Networks, Sockets, and Network Interfaces",
             "Working With Pandas Library (Dataframes)","Working With Numpy Library (Arrays)",
             "Working With Matplotlib Library (Data Visualization)","Working With Scikit-Learn Library (Machine Learning)","Working With Plotly Library (Interactive Data Visualization)",
             "Working With Dates and Times",
             "Working With More Advanced List Comprehensions andLambda Functions","Working With Object Oriented Programming","Working With Decorators",
             "Working With GraphQL","Working With Regular Expressions","Working With Strings",
             "Working With Web Scraping","Working With pip (Package Management)","Working With Common Built-in Functions and Packages"
             ]

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
             "Generating Combinations","Random Number Generation","Working with Fractions",
             "Statistical Functions","Trigonometric Functions","Handling Infinity and NaN",
             "Establishing a Connection","Creating a Cursor","Executing a Query",
             "Fetching Query Results","Inserting Records","Updating Records",
             "Deleting Records","Creating a Table","Dropping a Table",
             "Using Transactions","Defining an Asynchronous Function","Running an Asynchronous Function",
             "Awaiting Multiple Coroutines","Creating Tasks","Asynchronous Iteration",
             "Using Asynchronous Context Managers","Handling Exceptions in Asynchronous Code","Asynchronous Generators",
             "Using Semaphores","Event Loops","",
             "Creating a Socket","Connecting to a Remote Server","Sending Data",
             "Receiving Data","Closing a Socket","Creating a Listening Socket",
             "Accepting Connections","Non-blocking Socket Operations","Working with UDP Sockets",
             "Enumerating Network Interfaces","Creating a DataFrame","Reading Data from a CSV File",
             "Inspecting the First Few Rows","Selecting Columns","Filtering Rows",
             "Creating New Columns","Grouping and Aggregating Data","Merging DataFrames",
             "Handling Missing Data","Pivoting and Reshaping Data","Creating a NumPy Array",
             "Array of Zeros or Ones","Creating a Range of Numbers","Creating a Linearly Spaced Array",
             "Reshaping an Array","Basic Array Operations","Matrix Multiplication",
             "Accessing Array Elements","Boolean Indexing","Aggregations and Statistics",
             "Creating a Basic Plot","Adding Titles and Labels","Creating a Scatter Plot",
             "Customizing Line Styles and Markers","Creating Multiple Plots on the Same Axes","Creating Subplots",
             "Creating a Histogram","Adding a Legend","Customizing Ticks",
             "Saving Figures","Loading a Dataset","Splitting Data into Training and Test Sets",
             "Training a Model","Making Predictions","Evaluating Model Performance",
             "Using Cross-Validation","Feature Scaling","Parameter Tuning with Grid Search",
             "Pipeline Creation","Saving and Loading a Model","Creating a Basic Line Chart",
             "Creating a Scatter Plot","Creating a Bar Chart","Creating a Pie Chart",
             "Creating a Histogram","Creating Box Plots","Creating Heatmaps",
             "Creating 3D Surface Plots","Creating Subplots","Creating Interactive Time Series",
             "Getting the Current Date and Time","Creating Specific Date and Time","Formatting Dates and Times",
             "Parsing Dates and Times from Strings","Working with Time Deltas","Comparing Dates and Times",
             "Extracting Components from a Date/Time","Working with Time Zones","Getting the Weekday",
             "Working with Unix Timestamps","Nested List Comprehensions","Conditional List Comprehensions",
             "List Comprehensions with Multiple Iterables","Using Lambda Functions","Lambda Functions in List Comprehensions",
             "List Comprehensions for Flattening Lists","Applying Functions to Elements","Using Lambda with Map and Filter",
             "List Comprehensions with Conditional Expressions","Complex Transformations with Lambda","Defining a Class",
             "Creating an Instance","Invoking Methods","Inheritance",
             "Overriding Methods","Polymorphism","Encapsulation",
             "Composition","Class Methods and Static Methods","Properties and Setters",
             "Basic Decorator","Decorator with Arguments","Using functools.wraps",
             "Class Decorator","Decorator with Arguments","Method Decorator",
             "Stacking Decorators","Decorator with Optional Arguments","Class Method Decorator",
             "Decorator for Static Method","","",
             "Setting Up a GraphQL Client","Executing a Simple Query","Executing a Query with Variables",
             "Mutations","Handling Errors","Subscriptions",
             "Fragments","Inline Fragments","Using Directives",
             "Batching Requests","Basic Pattern Matching","Compiling Regular Expressions",
             "Matching at the Beginning or End","Finding All Matches","Search and Replace (Substitution)",
             "Splitting a String","Escaping Special Characters","Grouping and Capturing",
             "Non-Capturing Groups","Lookahead and Lookbehind Assertions","Flags to Modify Pattern Matching Behavior",
             "Using Named Groups","Matching Across Multiple Lines","Lazy Quantifiers",
             "Verbose Regular Expressions","Concatenating Strings","String Formatting with",
             "Formatted String Literals (f-strings)","String Methods — Case Conversion","String Methods",
             "String Methods — Working with Characters","String Slicing","String Length with",
             "Multiline Strings","Raw Strings","Fetching Web Pages with",
             "Parsing HTML with","Navigating the HTML Tree","Using CSS Selectors",
             "Extracting Data from Tags","Handling Relative URLs","Dealing with Pagination",
             "Handling AJAX Requests","Using Regular Expressions in Web Scraping","Respecting",
             "Using Sessions and Cookies","Scraping with Browser Automation","Error Handling in Web Scraping",
             "Asynchronous Web Scraping","Data Storage (CSV, Database)","Installing a Package",
             "Listing Installed Packages","Upgrading a Package","Uninstalling a Package",
             "Searching for Packages","Installing Specific Versions of a Package","Generating a Requirements File",
             "Installing Packages from a Requirements File","Using Virtual Environments","Checking Package Dependencies",
             "Operating System Interface","System-specific Parameters and Functions","Basic Date and Time Types",
             "Mathematical Functions","Generate Pseudo-random Numbers","JSON Encoder and Decoder",
             "Regular Expressions","URL Handling Modules","HTTP Modules",
             "Subprocess Management","Low-level Networking Interface","Thread-based Parallelism",
             "Process-based Parallelism","Parser for Command-line Options, Arguments,and Sub-commands","Logging Facility",
             "Unit Testing Framework","Object-oriented Filesystem Paths","Higher-order Functions and Operations onCallable Objects",
             "Container Data Types","Functions Creating Iterators for Efficient Looping","Secure Hash and Message Digest Algorithms",
             "CSV File Reading and Writing","The ElementTree XML API","DB-API 2.0 Interface for SQLite Databases",
             "GUI Toolkit","Python Object Serialization","Core Tools for Working with Streams",
             "Time Access and Conversions","General Calendar-related Functions","A Synchronized Queue Class",
             "High-level File Operations","Unix Style Pathname Pattern Expansion","Generate Temporary Files and Directories",
             "Support for Bzip2 Compression","Support for Gzip Compression","TLS/SSL Wrapper for Socket Objects",
             "IMAP4 Protocol Client","SMTP Protocol Client","Managing Email Messages",
             "base64","Helpers for Computing Deltas","Multilingual Internationalization Services",
             "Internationalization Services","Generate Secure Random Numbers for ManagingSecrets","UUID Objects According to RFC 4122",
             "HyperText Markup Language Support","FTP Protocol Client","Read and Write Tar Archive Files",
             "1","2","3",
             "4","5"]



def file_handling():
    st.header("File Handling")
    
    # Create a two-column layout
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("Reading a File")
        
        st.markdown(
            """
            ##### To read the entire content of a file:
            """
        )
        st.code(
            """
            with open('Tushar.txt', 'r') as file:
                content = file.read()
                print(content)
           
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("Writing to a File")
        
        st.markdown(
            """
            ##### To write text to a file, overwriting existing content:
            """
        )
        st.code(
            """
            with open('Tushar.txt', 'w') as file:
                content= file.write("www.tushar-aggarwal.com")
                print(content)
           
            """
        )
        
        
        
        
        st.subheader("Appending to a File")
        
        st.markdown(
            """
            ##### To add text to the end of an existing file:
            """
        )
        st.code(
            """
            with open('Tushar.txt', 'a') as file:
                content = file.write("\n https://www.linkedin.com/in/tusharaggarwalinseec/")
                print(content)
           
            """
        )
        
        
        st.subheader("Reading Lines into a List")
        
        st.markdown(
            """
            ##### To read a file line by line into a list:
            """
        )
        st.code(
            """
            with open('Tushar.txt', 'r') as file:
                content = file.readlines()
                print(content)
           
            """
        )
        
        
        
        st.subheader("Iterating Over Each Line in a File")
        
        st.markdown(
            """
            ##### To process each line in a file:
            """
        )
        st.code(
            """
            with open('Tushar.txt', 'a') as file:
                for line in file:
                    print(line.strip())
           
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






def http_apis():
    st.header("Working With Simple HTTP APIs")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("Basic GET Request")
        
        st.markdown(
            """
            ##### To fetch data from an API endpoint using a GET request:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            data = response.json() # Convert the response to JSON
            print(data)
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("GET Request with Query Parameters")
        
        st.markdown(
            """
            ##### To send a GET request with query parameters:
            """
        )
        st.code(
            """
            import requests
            params = {'page': 2}
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', params={'page': 2})
            data = response.json()
            print(data)
            """
        )
        
        
        
        
        st.subheader("Handling HTTP Errors")
        
        st.markdown(
            """
            ##### To handle possible HTTP errors gracefully:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            try:
                response.raise_for_status()
                data = response.json()
                print(data)
            except requests.exceptions.HTTPError as err:
                print(f'HTTP Error:{err}')
            """
        )
        
        
        st.subheader("Setting Timeout for Requests")
        
        st.markdown(
            """
            ##### To set a timeout for API requests to avoid hanging indefinitely:
            """
        )
        st.code(
            """
            import requests
            try:
                response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', timeout=5)
                data = response.json()
                print(data)
            except requests.exceptions.Timeout:
                print('The request timed out, Please try again')
            """
        )
        
        
        
        st.subheader("Using Headers in Requests")
        
        st.markdown(
            """
            ##### To include headers in your request (e.g., for authorization):
            """
        )
        st.code(
            """
            import requests
            headers = {
                'Authorization': 'YOUR_API_KEY'
            }
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', headers=headers)
            data = response.json()
            print(data)
            """
        )
            
        
    with col2:
        st.subheader("POST Request with JSON Payload")
        
        st.markdown(
            """
            ##### To send data to an API endpoint using a POST request with a JSON payload:
            """
        )
        st.code(
            """
            import requests
            payload = {'key1': 'value1', 'key2': 'value2'}
            headers = {'Content-type': 'application/json'}
            response = requests.post('https://httpbin.org/post', data=json.dumps(payload), headers=headers)
            print(response.json())
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("Handling Response Encoding")
        
        st.markdown(
            """
            ##### To handle the response encoding properly:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            response.encoding = 'utf-8'
            data = response.text
            print(data)          
            """
        )
        
        
        
        
        st.subheader("Using Sessions with Requests")
        
        st.markdown(
            """
            ##### To use a session object for making multiple requests to the same host, whichcan improve performance:
            """
        )
        st.code(
            """
            import requests
            with requests.Session() as session:
                session.headers.update({'Authorization': 'YOUR_API_KEY'})
                response = session.get('https://api.github.com/users/tushar-aggarwalinseec')
                print(response.json())
                
            """
        )
        
        
        st.subheader("Handling Redirects")
        
        st.markdown(
            """
            ##### To handle or disable redirects in requests:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', allow_redirects=False)
            print(response.status_code)
            """
        )
        
        
        
        st.subheader("Streaming Large Responses")
        
        st.markdown(
            """
            ##### To stream a large response to process it in chunks, rather than loading it all into memory:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', stream=True)
            for chunk in response.iter_content(chunk_size=1024):
                process_chunk(chunk) #replace 'process' with your own function
            """
        )




def lists():
    st.header("Working With Lists")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("Creating a List")
        
        st.markdown(
            """
            ##### To conjure a list into being:
            """
        )
        st.code(
            """
            # Initialize an list
            my_list = ['tushar', 'aggarwal', 'inseec']
            print(my_list)
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("Appending to a List")
        
        st.markdown(
            """
            ##### To append a new element to the end of a list:
            """
        )
        st.code(
            """
            # Append an element
            my_list.append('supreme', 'apps')
            print(my_list)
            """
        )
        
        
        
        
        st.subheader("Inserting into a List")
        
        st.markdown(
            """
            ##### To insert an element at a specific position in the list:
            """
        )
        st.code(
            """
            # Insert 'AGGARWAL' at index #1 in the list
            my_list.insert(1, 'AGGARWAL')
            print(my_list)
            """
        )
        
        
        st.subheader("Removing from a List")
        
        st.markdown(
            """
            ##### To remove an element by value from the list:
            """
        )
        st.code(
            """
            # Remove 'apps' from the list
            my_list.remove('apps')
            print(my_list)
            """
        )
        
        
        
        st.subheader("Popping an Element from a List")
        
        st.markdown(
            """
            ##### To remove and return an element at a given index (default is the last item):
            """
        )
        st.code(
            """
            # Pop an element
            my_list.pop()
            print(my_list)
            """
        )
            
        
    with col2:
        st.subheader("Finding the Index of an Element")
        
        st.markdown(
            """
            ##### To find the index of the first occurrence of an element:
            """
        )
        st.code(
            """
            # Find the index
            my_list.index('aggarwal')
            print(my_list)
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("List Slicing")
        
        st.markdown(
            """
            ##### To slice a list, obtaining a sub-list:
            """
        )
        st.code(
            """
            # Get elements from index 1 to 3
            indexed = my_list[1:3]
            print(indexed)          
            """
        )
        
        
        
        
        st.subheader("List Comprehension")
        
        st.markdown(
            """
            ##### To create a new list by applying an expression to each element of an existingone:
            """
        )
        st.code(
            """
            # Create a new list with lengths of each element
            new_list = [len(item) for item in my_list]
            print(new_list)
                
            """
        )
        
        
        st.subheader("Sorting a List")
        
        st.markdown(
            """
            ##### To sort a list in ascending order (in-place):
            """
        )
        st.code(
            """
            # Sort elements in ascending order
            my_list.sort()
            print(my_list)
            """
        )
        
        
        
        st.subheader("Reversing a List")
        
        st.markdown(
            """
            ##### To reverse the elements of a list in-place:
            """
        )
        st.code(
            """
            # Reverse elements 
            my_list.reverse()
            print(my_list)
            """
        )





def dict():
    st.header("Working With Simple HTTP APIs")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("Basic GET Request")
        
        st.markdown(
            """
            ##### To fetch data from an API endpoint using a GET request:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            data = response.json() # Convert the response to JSON
            print(data)
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("GET Request with Query Parameters")
        
        st.markdown(
            """
            ##### To send a GET request with query parameters:
            """
        )
        st.code(
            """
            import requests
            params = {'page': 2}
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', params={'page': 2})
            data = response.json()
            print(data)
            """
        )
        
        
        
        
        st.subheader("Handling HTTP Errors")
        
        st.markdown(
            """
            ##### To handle possible HTTP errors gracefully:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            try:
                response.raise_for_status()
                data = response.json()
                print(data)
            except requests.exceptions.HTTPError as err:
                print(f'HTTP Error:{err}')
            """
        )
        
        
        st.subheader("Setting Timeout for Requests")
        
        st.markdown(
            """
            ##### To set a timeout for API requests to avoid hanging indefinitely:
            """
        )
        st.code(
            """
            import requests
            try:
                response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', timeout=5)
                data = response.json()
                print(data)
            except requests.exceptions.Timeout:
                print('The request timed out, Please try again')
            """
        )
        
        
        
        st.subheader("Using Headers in Requests")
        
        st.markdown(
            """
            ##### To include headers in your request (e.g., for authorization):
            """
        )
        st.code(
            """
            import requests
            headers = {
                'Authorization': 'YOUR_API_KEY'
            }
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', headers=headers)
            data = response.json()
            print(data)
            """
        )
            
        
    with col2:
        st.subheader("POST Request with JSON Payload")
        
        st.markdown(
            """
            ##### To send data to an API endpoint using a POST request with a JSON payload:
            """
        )
        st.code(
            """
            import requests
            payload = {'key1': 'value1', 'key2': 'value2'}
            headers = {'Content-type': 'application/json'}
            response = requests.post('https://httpbin.org/post', data=json.dumps(payload), headers=headers)
            print(response.json())
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("Handling Response Encoding")
        
        st.markdown(
            """
            ##### To handle the response encoding properly:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            response.encoding = 'utf-8'
            data = response.text
            print(data)          
            """
        )
        
        
        
        
        st.subheader("Using Sessions with Requests")
        
        st.markdown(
            """
            ##### To use a session object for making multiple requests to the same host, whichcan improve performance:
            """
        )
        st.code(
            """
            import requests
            with requests.Session() as session:
                session.headers.update({'Authorization': 'YOUR_API_KEY'})
                response = session.get('https://api.github.com/users/tushar-aggarwalinseec')
                print(response.json())
                
            """
        )
        
        
        st.subheader("Handling Redirects")
        
        st.markdown(
            """
            ##### To handle or disable redirects in requests:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', allow_redirects=False)
            print(response.status_code)
            """
        )
        
        
        
        st.subheader("Streaming Large Responses")
        
        st.markdown(
            """
            ##### To stream a large response to process it in chunks, rather than loading it all into memory:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', stream=True)
            for chunk in response.iter_content(chunk_size=1024):
                process_chunk(chunk) #replace 'process' with your own function
            """
        )





def os_():
    st.header("Working With Simple HTTP APIs")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("Basic GET Request")
        
        st.markdown(
            """
            ##### To fetch data from an API endpoint using a GET request:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            data = response.json() # Convert the response to JSON
            print(data)
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("GET Request with Query Parameters")
        
        st.markdown(
            """
            ##### To send a GET request with query parameters:
            """
        )
        st.code(
            """
            import requests
            params = {'page': 2}
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', params={'page': 2})
            data = response.json()
            print(data)
            """
        )
        
        
        
        
        st.subheader("Handling HTTP Errors")
        
        st.markdown(
            """
            ##### To handle possible HTTP errors gracefully:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            try:
                response.raise_for_status()
                data = response.json()
                print(data)
            except requests.exceptions.HTTPError as err:
                print(f'HTTP Error:{err}')
            """
        )
        
        
        st.subheader("Setting Timeout for Requests")
        
        st.markdown(
            """
            ##### To set a timeout for API requests to avoid hanging indefinitely:
            """
        )
        st.code(
            """
            import requests
            try:
                response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', timeout=5)
                data = response.json()
                print(data)
            except requests.exceptions.Timeout:
                print('The request timed out, Please try again')
            """
        )
        
        
        
        st.subheader("Using Headers in Requests")
        
        st.markdown(
            """
            ##### To include headers in your request (e.g., for authorization):
            """
        )
        st.code(
            """
            import requests
            headers = {
                'Authorization': 'YOUR_API_KEY'
            }
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', headers=headers)
            data = response.json()
            print(data)
            """
        )
            
        
    with col2:
        st.subheader("POST Request with JSON Payload")
        
        st.markdown(
            """
            ##### To send data to an API endpoint using a POST request with a JSON payload:
            """
        )
        st.code(
            """
            import requests
            payload = {'key1': 'value1', 'key2': 'value2'}
            headers = {'Content-type': 'application/json'}
            response = requests.post('https://httpbin.org/post', data=json.dumps(payload), headers=headers)
            print(response.json())
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("Handling Response Encoding")
        
        st.markdown(
            """
            ##### To handle the response encoding properly:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            response.encoding = 'utf-8'
            data = response.text
            print(data)          
            """
        )
        
        
        
        
        st.subheader("Using Sessions with Requests")
        
        st.markdown(
            """
            ##### To use a session object for making multiple requests to the same host, whichcan improve performance:
            """
        )
        st.code(
            """
            import requests
            with requests.Session() as session:
                session.headers.update({'Authorization': 'YOUR_API_KEY'})
                response = session.get('https://api.github.com/users/tushar-aggarwalinseec')
                print(response.json())
                
            """
        )
        
        
        st.subheader("Handling Redirects")
        
        st.markdown(
            """
            ##### To handle or disable redirects in requests:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', allow_redirects=False)
            print(response.status_code)
            """
        )
        
        
        
        st.subheader("Streaming Large Responses")
        
        st.markdown(
            """
            ##### To stream a large response to process it in chunks, rather than loading it all into memory:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', stream=True)
            for chunk in response.iter_content(chunk_size=1024):
                process_chunk(chunk) #replace 'process' with your own function
            """
        )





def cli():
    st.header("Working With Simple HTTP APIs")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("Basic GET Request")
        
        st.markdown(
            """
            ##### To fetch data from an API endpoint using a GET request:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            data = response.json() # Convert the response to JSON
            print(data)
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("GET Request with Query Parameters")
        
        st.markdown(
            """
            ##### To send a GET request with query parameters:
            """
        )
        st.code(
            """
            import requests
            params = {'page': 2}
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', params={'page': 2})
            data = response.json()
            print(data)
            """
        )
        
        
        
        
        st.subheader("Handling HTTP Errors")
        
        st.markdown(
            """
            ##### To handle possible HTTP errors gracefully:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            try:
                response.raise_for_status()
                data = response.json()
                print(data)
            except requests.exceptions.HTTPError as err:
                print(f'HTTP Error:{err}')
            """
        )
        
        
        st.subheader("Setting Timeout for Requests")
        
        st.markdown(
            """
            ##### To set a timeout for API requests to avoid hanging indefinitely:
            """
        )
        st.code(
            """
            import requests
            try:
                response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', timeout=5)
                data = response.json()
                print(data)
            except requests.exceptions.Timeout:
                print('The request timed out, Please try again')
            """
        )
        
        
        
        st.subheader("Using Headers in Requests")
        
        st.markdown(
            """
            ##### To include headers in your request (e.g., for authorization):
            """
        )
        st.code(
            """
            import requests
            headers = {
                'Authorization': 'YOUR_API_KEY'
            }
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', headers=headers)
            data = response.json()
            print(data)
            """
        )
            
        
    with col2:
        st.subheader("POST Request with JSON Payload")
        
        st.markdown(
            """
            ##### To send data to an API endpoint using a POST request with a JSON payload:
            """
        )
        st.code(
            """
            import requests
            payload = {'key1': 'value1', 'key2': 'value2'}
            headers = {'Content-type': 'application/json'}
            response = requests.post('https://httpbin.org/post', data=json.dumps(payload), headers=headers)
            print(response.json())
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("Handling Response Encoding")
        
        st.markdown(
            """
            ##### To handle the response encoding properly:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            response.encoding = 'utf-8'
            data = response.text
            print(data)          
            """
        )
        
        
        
        
        st.subheader("Using Sessions with Requests")
        
        st.markdown(
            """
            ##### To use a session object for making multiple requests to the same host, whichcan improve performance:
            """
        )
        st.code(
            """
            import requests
            with requests.Session() as session:
                session.headers.update({'Authorization': 'YOUR_API_KEY'})
                response = session.get('https://api.github.com/users/tushar-aggarwalinseec')
                print(response.json())
                
            """
        )
        
        
        st.subheader("Handling Redirects")
        
        st.markdown(
            """
            ##### To handle or disable redirects in requests:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', allow_redirects=False)
            print(response.status_code)
            """
        )
        
        
        
        st.subheader("Streaming Large Responses")
        
        st.markdown(
            """
            ##### To stream a large response to process it in chunks, rather than loading it all into memory:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', stream=True)
            for chunk in response.iter_content(chunk_size=1024):
                process_chunk(chunk) #replace 'process' with your own function
            """
        )





def math():
    st.header("Working With Simple HTTP APIs")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("Basic GET Request")
        
        st.markdown(
            """
            ##### To fetch data from an API endpoint using a GET request:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            data = response.json() # Convert the response to JSON
            print(data)
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("GET Request with Query Parameters")
        
        st.markdown(
            """
            ##### To send a GET request with query parameters:
            """
        )
        st.code(
            """
            import requests
            params = {'page': 2}
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', params={'page': 2})
            data = response.json()
            print(data)
            """
        )
        
        
        
        
        st.subheader("Handling HTTP Errors")
        
        st.markdown(
            """
            ##### To handle possible HTTP errors gracefully:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            try:
                response.raise_for_status()
                data = response.json()
                print(data)
            except requests.exceptions.HTTPError as err:
                print(f'HTTP Error:{err}')
            """
        )
        
        
        st.subheader("Setting Timeout for Requests")
        
        st.markdown(
            """
            ##### To set a timeout for API requests to avoid hanging indefinitely:
            """
        )
        st.code(
            """
            import requests
            try:
                response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', timeout=5)
                data = response.json()
                print(data)
            except requests.exceptions.Timeout:
                print('The request timed out, Please try again')
            """
        )
        
        
        
        st.subheader("Using Headers in Requests")
        
        st.markdown(
            """
            ##### To include headers in your request (e.g., for authorization):
            """
        )
        st.code(
            """
            import requests
            headers = {
                'Authorization': 'YOUR_API_KEY'
            }
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', headers=headers)
            data = response.json()
            print(data)
            """
        )
            
        
    with col2:
        st.subheader("POST Request with JSON Payload")
        
        st.markdown(
            """
            ##### To send data to an API endpoint using a POST request with a JSON payload:
            """
        )
        st.code(
            """
            import requests
            payload = {'key1': 'value1', 'key2': 'value2'}
            headers = {'Content-type': 'application/json'}
            response = requests.post('https://httpbin.org/post', data=json.dumps(payload), headers=headers)
            print(response.json())
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("Handling Response Encoding")
        
        st.markdown(
            """
            ##### To handle the response encoding properly:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            response.encoding = 'utf-8'
            data = response.text
            print(data)          
            """
        )
        
        
        
        
        st.subheader("Using Sessions with Requests")
        
        st.markdown(
            """
            ##### To use a session object for making multiple requests to the same host, whichcan improve performance:
            """
        )
        st.code(
            """
            import requests
            with requests.Session() as session:
                session.headers.update({'Authorization': 'YOUR_API_KEY'})
                response = session.get('https://api.github.com/users/tushar-aggarwalinseec')
                print(response.json())
                
            """
        )
        
        
        st.subheader("Handling Redirects")
        
        st.markdown(
            """
            ##### To handle or disable redirects in requests:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', allow_redirects=False)
            print(response.status_code)
            """
        )
        
        
        
        st.subheader("Streaming Large Responses")
        
        st.markdown(
            """
            ##### To stream a large response to process it in chunks, rather than loading it all into memory:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', stream=True)
            for chunk in response.iter_content(chunk_size=1024):
                process_chunk(chunk) #replace 'process' with your own function
            """
        )





def databases():
    st.header("Working With Simple HTTP APIs")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("Basic GET Request")
        
        st.markdown(
            """
            ##### To fetch data from an API endpoint using a GET request:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            data = response.json() # Convert the response to JSON
            print(data)
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("GET Request with Query Parameters")
        
        st.markdown(
            """
            ##### To send a GET request with query parameters:
            """
        )
        st.code(
            """
            import requests
            params = {'page': 2}
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', params={'page': 2})
            data = response.json()
            print(data)
            """
        )
        
        
        
        
        st.subheader("Handling HTTP Errors")
        
        st.markdown(
            """
            ##### To handle possible HTTP errors gracefully:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            try:
                response.raise_for_status()
                data = response.json()
                print(data)
            except requests.exceptions.HTTPError as err:
                print(f'HTTP Error:{err}')
            """
        )
        
        
        st.subheader("Setting Timeout for Requests")
        
        st.markdown(
            """
            ##### To set a timeout for API requests to avoid hanging indefinitely:
            """
        )
        st.code(
            """
            import requests
            try:
                response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', timeout=5)
                data = response.json()
                print(data)
            except requests.exceptions.Timeout:
                print('The request timed out, Please try again')
            """
        )
        
        
        
        st.subheader("Using Headers in Requests")
        
        st.markdown(
            """
            ##### To include headers in your request (e.g., for authorization):
            """
        )
        st.code(
            """
            import requests
            headers = {
                'Authorization': 'YOUR_API_KEY'
            }
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', headers=headers)
            data = response.json()
            print(data)
            """
        )
            
        
    with col2:
        st.subheader("POST Request with JSON Payload")
        
        st.markdown(
            """
            ##### To send data to an API endpoint using a POST request with a JSON payload:
            """
        )
        st.code(
            """
            import requests
            payload = {'key1': 'value1', 'key2': 'value2'}
            headers = {'Content-type': 'application/json'}
            response = requests.post('https://httpbin.org/post', data=json.dumps(payload), headers=headers)
            print(response.json())
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("Handling Response Encoding")
        
        st.markdown(
            """
            ##### To handle the response encoding properly:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            response.encoding = 'utf-8'
            data = response.text
            print(data)          
            """
        )
        
        
        
        
        st.subheader("Using Sessions with Requests")
        
        st.markdown(
            """
            ##### To use a session object for making multiple requests to the same host, whichcan improve performance:
            """
        )
        st.code(
            """
            import requests
            with requests.Session() as session:
                session.headers.update({'Authorization': 'YOUR_API_KEY'})
                response = session.get('https://api.github.com/users/tushar-aggarwalinseec')
                print(response.json())
                
            """
        )
        
        
        st.subheader("Handling Redirects")
        
        st.markdown(
            """
            ##### To handle or disable redirects in requests:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', allow_redirects=False)
            print(response.status_code)
            """
        )
        
        
        
        st.subheader("Streaming Large Responses")
        
        st.markdown(
            """
            ##### To stream a large response to process it in chunks, rather than loading it all into memory:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', stream=True)
            for chunk in response.iter_content(chunk_size=1024):
                process_chunk(chunk) #replace 'process' with your own function
            """
        )






def async_():
    st.header("Working With Simple HTTP APIs")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("Basic GET Request")
        
        st.markdown(
            """
            ##### To fetch data from an API endpoint using a GET request:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            data = response.json() # Convert the response to JSON
            print(data)
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("GET Request with Query Parameters")
        
        st.markdown(
            """
            ##### To send a GET request with query parameters:
            """
        )
        st.code(
            """
            import requests
            params = {'page': 2}
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', params={'page': 2})
            data = response.json()
            print(data)
            """
        )
        
        
        
        
        st.subheader("Handling HTTP Errors")
        
        st.markdown(
            """
            ##### To handle possible HTTP errors gracefully:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            try:
                response.raise_for_status()
                data = response.json()
                print(data)
            except requests.exceptions.HTTPError as err:
                print(f'HTTP Error:{err}')
            """
        )
        
        
        st.subheader("Setting Timeout for Requests")
        
        st.markdown(
            """
            ##### To set a timeout for API requests to avoid hanging indefinitely:
            """
        )
        st.code(
            """
            import requests
            try:
                response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', timeout=5)
                data = response.json()
                print(data)
            except requests.exceptions.Timeout:
                print('The request timed out, Please try again')
            """
        )
        
        
        
        st.subheader("Using Headers in Requests")
        
        st.markdown(
            """
            ##### To include headers in your request (e.g., for authorization):
            """
        )
        st.code(
            """
            import requests
            headers = {
                'Authorization': 'YOUR_API_KEY'
            }
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', headers=headers)
            data = response.json()
            print(data)
            """
        )
            
        
    with col2:
        st.subheader("POST Request with JSON Payload")
        
        st.markdown(
            """
            ##### To send data to an API endpoint using a POST request with a JSON payload:
            """
        )
        st.code(
            """
            import requests
            payload = {'key1': 'value1', 'key2': 'value2'}
            headers = {'Content-type': 'application/json'}
            response = requests.post('https://httpbin.org/post', data=json.dumps(payload), headers=headers)
            print(response.json())
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("Handling Response Encoding")
        
        st.markdown(
            """
            ##### To handle the response encoding properly:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            response.encoding = 'utf-8'
            data = response.text
            print(data)          
            """
        )
        
        
        
        
        st.subheader("Using Sessions with Requests")
        
        st.markdown(
            """
            ##### To use a session object for making multiple requests to the same host, whichcan improve performance:
            """
        )
        st.code(
            """
            import requests
            with requests.Session() as session:
                session.headers.update({'Authorization': 'YOUR_API_KEY'})
                response = session.get('https://api.github.com/users/tushar-aggarwalinseec')
                print(response.json())
                
            """
        )
        
        
        st.subheader("Handling Redirects")
        
        st.markdown(
            """
            ##### To handle or disable redirects in requests:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', allow_redirects=False)
            print(response.status_code)
            """
        )
        
        
        
        st.subheader("Streaming Large Responses")
        
        st.markdown(
            """
            ##### To stream a large response to process it in chunks, rather than loading it all into memory:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', stream=True)
            for chunk in response.iter_content(chunk_size=1024):
                process_chunk(chunk) #replace 'process' with your own function
            """
        )






def network():
    st.header("Working With Simple HTTP APIs")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("Basic GET Request")
        
        st.markdown(
            """
            ##### To fetch data from an API endpoint using a GET request:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            data = response.json() # Convert the response to JSON
            print(data)
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("GET Request with Query Parameters")
        
        st.markdown(
            """
            ##### To send a GET request with query parameters:
            """
        )
        st.code(
            """
            import requests
            params = {'page': 2}
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', params={'page': 2})
            data = response.json()
            print(data)
            """
        )
        
        
        
        
        st.subheader("Handling HTTP Errors")
        
        st.markdown(
            """
            ##### To handle possible HTTP errors gracefully:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            try:
                response.raise_for_status()
                data = response.json()
                print(data)
            except requests.exceptions.HTTPError as err:
                print(f'HTTP Error:{err}')
            """
        )
        
        
        st.subheader("Setting Timeout for Requests")
        
        st.markdown(
            """
            ##### To set a timeout for API requests to avoid hanging indefinitely:
            """
        )
        st.code(
            """
            import requests
            try:
                response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', timeout=5)
                data = response.json()
                print(data)
            except requests.exceptions.Timeout:
                print('The request timed out, Please try again')
            """
        )
        
        
        
        st.subheader("Using Headers in Requests")
        
        st.markdown(
            """
            ##### To include headers in your request (e.g., for authorization):
            """
        )
        st.code(
            """
            import requests
            headers = {
                'Authorization': 'YOUR_API_KEY'
            }
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', headers=headers)
            data = response.json()
            print(data)
            """
        )
            
        
    with col2:
        st.subheader("POST Request with JSON Payload")
        
        st.markdown(
            """
            ##### To send data to an API endpoint using a POST request with a JSON payload:
            """
        )
        st.code(
            """
            import requests
            payload = {'key1': 'value1', 'key2': 'value2'}
            headers = {'Content-type': 'application/json'}
            response = requests.post('https://httpbin.org/post', data=json.dumps(payload), headers=headers)
            print(response.json())
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("Handling Response Encoding")
        
        st.markdown(
            """
            ##### To handle the response encoding properly:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            response.encoding = 'utf-8'
            data = response.text
            print(data)          
            """
        )
        
        
        
        
        st.subheader("Using Sessions with Requests")
        
        st.markdown(
            """
            ##### To use a session object for making multiple requests to the same host, whichcan improve performance:
            """
        )
        st.code(
            """
            import requests
            with requests.Session() as session:
                session.headers.update({'Authorization': 'YOUR_API_KEY'})
                response = session.get('https://api.github.com/users/tushar-aggarwalinseec')
                print(response.json())
                
            """
        )
        
        
        st.subheader("Handling Redirects")
        
        st.markdown(
            """
            ##### To handle or disable redirects in requests:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', allow_redirects=False)
            print(response.status_code)
            """
        )
        
        
        
        st.subheader("Streaming Large Responses")
        
        st.markdown(
            """
            ##### To stream a large response to process it in chunks, rather than loading it all into memory:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', stream=True)
            for chunk in response.iter_content(chunk_size=1024):
                process_chunk(chunk) #replace 'process' with your own function
            """
        )





def df_():
    st.header("Working With Simple HTTP APIs")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("Basic GET Request")
        
        st.markdown(
            """
            ##### To fetch data from an API endpoint using a GET request:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            data = response.json() # Convert the response to JSON
            print(data)
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("GET Request with Query Parameters")
        
        st.markdown(
            """
            ##### To send a GET request with query parameters:
            """
        )
        st.code(
            """
            import requests
            params = {'page': 2}
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', params={'page': 2})
            data = response.json()
            print(data)
            """
        )
        
        
        
        
        st.subheader("Handling HTTP Errors")
        
        st.markdown(
            """
            ##### To handle possible HTTP errors gracefully:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            try:
                response.raise_for_status()
                data = response.json()
                print(data)
            except requests.exceptions.HTTPError as err:
                print(f'HTTP Error:{err}')
            """
        )
        
        
        st.subheader("Setting Timeout for Requests")
        
        st.markdown(
            """
            ##### To set a timeout for API requests to avoid hanging indefinitely:
            """
        )
        st.code(
            """
            import requests
            try:
                response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', timeout=5)
                data = response.json()
                print(data)
            except requests.exceptions.Timeout:
                print('The request timed out, Please try again')
            """
        )
        
        
        
        st.subheader("Using Headers in Requests")
        
        st.markdown(
            """
            ##### To include headers in your request (e.g., for authorization):
            """
        )
        st.code(
            """
            import requests
            headers = {
                'Authorization': 'YOUR_API_KEY'
            }
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', headers=headers)
            data = response.json()
            print(data)
            """
        )
            
        
    with col2:
        st.subheader("POST Request with JSON Payload")
        
        st.markdown(
            """
            ##### To send data to an API endpoint using a POST request with a JSON payload:
            """
        )
        st.code(
            """
            import requests
            payload = {'key1': 'value1', 'key2': 'value2'}
            headers = {'Content-type': 'application/json'}
            response = requests.post('https://httpbin.org/post', data=json.dumps(payload), headers=headers)
            print(response.json())
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("Handling Response Encoding")
        
        st.markdown(
            """
            ##### To handle the response encoding properly:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            response.encoding = 'utf-8'
            data = response.text
            print(data)          
            """
        )
        
        
        
        
        st.subheader("Using Sessions with Requests")
        
        st.markdown(
            """
            ##### To use a session object for making multiple requests to the same host, whichcan improve performance:
            """
        )
        st.code(
            """
            import requests
            with requests.Session() as session:
                session.headers.update({'Authorization': 'YOUR_API_KEY'})
                response = session.get('https://api.github.com/users/tushar-aggarwalinseec')
                print(response.json())
                
            """
        )
        
        
        st.subheader("Handling Redirects")
        
        st.markdown(
            """
            ##### To handle or disable redirects in requests:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', allow_redirects=False)
            print(response.status_code)
            """
        )
        
        
        
        st.subheader("Streaming Large Responses")
        
        st.markdown(
            """
            ##### To stream a large response to process it in chunks, rather than loading it all into memory:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', stream=True)
            for chunk in response.iter_content(chunk_size=1024):
                process_chunk(chunk) #replace 'process' with your own function
            """
        )





def numpy_():
    st.header("Working With Simple HTTP APIs")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("Basic GET Request")
        
        st.markdown(
            """
            ##### To fetch data from an API endpoint using a GET request:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            data = response.json() # Convert the response to JSON
            print(data)
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("GET Request with Query Parameters")
        
        st.markdown(
            """
            ##### To send a GET request with query parameters:
            """
        )
        st.code(
            """
            import requests
            params = {'page': 2}
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', params={'page': 2})
            data = response.json()
            print(data)
            """
        )
        
        
        
        
        st.subheader("Handling HTTP Errors")
        
        st.markdown(
            """
            ##### To handle possible HTTP errors gracefully:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            try:
                response.raise_for_status()
                data = response.json()
                print(data)
            except requests.exceptions.HTTPError as err:
                print(f'HTTP Error:{err}')
            """
        )
        
        
        st.subheader("Setting Timeout for Requests")
        
        st.markdown(
            """
            ##### To set a timeout for API requests to avoid hanging indefinitely:
            """
        )
        st.code(
            """
            import requests
            try:
                response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', timeout=5)
                data = response.json()
                print(data)
            except requests.exceptions.Timeout:
                print('The request timed out, Please try again')
            """
        )
        
        
        
        st.subheader("Using Headers in Requests")
        
        st.markdown(
            """
            ##### To include headers in your request (e.g., for authorization):
            """
        )
        st.code(
            """
            import requests
            headers = {
                'Authorization': 'YOUR_API_KEY'
            }
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', headers=headers)
            data = response.json()
            print(data)
            """
        )
            
        
    with col2:
        st.subheader("POST Request with JSON Payload")
        
        st.markdown(
            """
            ##### To send data to an API endpoint using a POST request with a JSON payload:
            """
        )
        st.code(
            """
            import requests
            payload = {'key1': 'value1', 'key2': 'value2'}
            headers = {'Content-type': 'application/json'}
            response = requests.post('https://httpbin.org/post', data=json.dumps(payload), headers=headers)
            print(response.json())
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("Handling Response Encoding")
        
        st.markdown(
            """
            ##### To handle the response encoding properly:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            response.encoding = 'utf-8'
            data = response.text
            print(data)          
            """
        )
        
        
        
        
        st.subheader("Using Sessions with Requests")
        
        st.markdown(
            """
            ##### To use a session object for making multiple requests to the same host, whichcan improve performance:
            """
        )
        st.code(
            """
            import requests
            with requests.Session() as session:
                session.headers.update({'Authorization': 'YOUR_API_KEY'})
                response = session.get('https://api.github.com/users/tushar-aggarwalinseec')
                print(response.json())
                
            """
        )
        
        
        st.subheader("Handling Redirects")
        
        st.markdown(
            """
            ##### To handle or disable redirects in requests:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', allow_redirects=False)
            print(response.status_code)
            """
        )
        
        
        
        st.subheader("Streaming Large Responses")
        
        st.markdown(
            """
            ##### To stream a large response to process it in chunks, rather than loading it all into memory:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', stream=True)
            for chunk in response.iter_content(chunk_size=1024):
                process_chunk(chunk) #replace 'process' with your own function
            """
        )






def plots():
    st.header("Working With Simple HTTP APIs")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("Basic GET Request")
        
        st.markdown(
            """
            ##### To fetch data from an API endpoint using a GET request:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            data = response.json() # Convert the response to JSON
            print(data)
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("GET Request with Query Parameters")
        
        st.markdown(
            """
            ##### To send a GET request with query parameters:
            """
        )
        st.code(
            """
            import requests
            params = {'page': 2}
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', params={'page': 2})
            data = response.json()
            print(data)
            """
        )
        
        
        
        
        st.subheader("Handling HTTP Errors")
        
        st.markdown(
            """
            ##### To handle possible HTTP errors gracefully:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            try:
                response.raise_for_status()
                data = response.json()
                print(data)
            except requests.exceptions.HTTPError as err:
                print(f'HTTP Error:{err}')
            """
        )
        
        
        st.subheader("Setting Timeout for Requests")
        
        st.markdown(
            """
            ##### To set a timeout for API requests to avoid hanging indefinitely:
            """
        )
        st.code(
            """
            import requests
            try:
                response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', timeout=5)
                data = response.json()
                print(data)
            except requests.exceptions.Timeout:
                print('The request timed out, Please try again')
            """
        )
        
        
        
        st.subheader("Using Headers in Requests")
        
        st.markdown(
            """
            ##### To include headers in your request (e.g., for authorization):
            """
        )
        st.code(
            """
            import requests
            headers = {
                'Authorization': 'YOUR_API_KEY'
            }
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', headers=headers)
            data = response.json()
            print(data)
            """
        )
            
        
    with col2:
        st.subheader("POST Request with JSON Payload")
        
        st.markdown(
            """
            ##### To send data to an API endpoint using a POST request with a JSON payload:
            """
        )
        st.code(
            """
            import requests
            payload = {'key1': 'value1', 'key2': 'value2'}
            headers = {'Content-type': 'application/json'}
            response = requests.post('https://httpbin.org/post', data=json.dumps(payload), headers=headers)
            print(response.json())
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("Handling Response Encoding")
        
        st.markdown(
            """
            ##### To handle the response encoding properly:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            response.encoding = 'utf-8'
            data = response.text
            print(data)          
            """
        )
        
        
        
        
        st.subheader("Using Sessions with Requests")
        
        st.markdown(
            """
            ##### To use a session object for making multiple requests to the same host, whichcan improve performance:
            """
        )
        st.code(
            """
            import requests
            with requests.Session() as session:
                session.headers.update({'Authorization': 'YOUR_API_KEY'})
                response = session.get('https://api.github.com/users/tushar-aggarwalinseec')
                print(response.json())
                
            """
        )
        
        
        st.subheader("Handling Redirects")
        
        st.markdown(
            """
            ##### To handle or disable redirects in requests:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', allow_redirects=False)
            print(response.status_code)
            """
        )
        
        
        
        st.subheader("Streaming Large Responses")
        
        st.markdown(
            """
            ##### To stream a large response to process it in chunks, rather than loading it all into memory:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', stream=True)
            for chunk in response.iter_content(chunk_size=1024):
                process_chunk(chunk) #replace 'process' with your own function
            """
        )





def scikit_():
    st.header("Working With Simple HTTP APIs")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("Basic GET Request")
        
        st.markdown(
            """
            ##### To fetch data from an API endpoint using a GET request:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            data = response.json() # Convert the response to JSON
            print(data)
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("GET Request with Query Parameters")
        
        st.markdown(
            """
            ##### To send a GET request with query parameters:
            """
        )
        st.code(
            """
            import requests
            params = {'page': 2}
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', params={'page': 2})
            data = response.json()
            print(data)
            """
        )
        
        
        
        
        st.subheader("Handling HTTP Errors")
        
        st.markdown(
            """
            ##### To handle possible HTTP errors gracefully:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            try:
                response.raise_for_status()
                data = response.json()
                print(data)
            except requests.exceptions.HTTPError as err:
                print(f'HTTP Error:{err}')
            """
        )
        
        
        st.subheader("Setting Timeout for Requests")
        
        st.markdown(
            """
            ##### To set a timeout for API requests to avoid hanging indefinitely:
            """
        )
        st.code(
            """
            import requests
            try:
                response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', timeout=5)
                data = response.json()
                print(data)
            except requests.exceptions.Timeout:
                print('The request timed out, Please try again')
            """
        )
        
        
        
        st.subheader("Using Headers in Requests")
        
        st.markdown(
            """
            ##### To include headers in your request (e.g., for authorization):
            """
        )
        st.code(
            """
            import requests
            headers = {
                'Authorization': 'YOUR_API_KEY'
            }
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', headers=headers)
            data = response.json()
            print(data)
            """
        )
            
        
    with col2:
        st.subheader("POST Request with JSON Payload")
        
        st.markdown(
            """
            ##### To send data to an API endpoint using a POST request with a JSON payload:
            """
        )
        st.code(
            """
            import requests
            payload = {'key1': 'value1', 'key2': 'value2'}
            headers = {'Content-type': 'application/json'}
            response = requests.post('https://httpbin.org/post', data=json.dumps(payload), headers=headers)
            print(response.json())
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("Handling Response Encoding")
        
        st.markdown(
            """
            ##### To handle the response encoding properly:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            response.encoding = 'utf-8'
            data = response.text
            print(data)          
            """
        )
        
        
        
        
        st.subheader("Using Sessions with Requests")
        
        st.markdown(
            """
            ##### To use a session object for making multiple requests to the same host, whichcan improve performance:
            """
        )
        st.code(
            """
            import requests
            with requests.Session() as session:
                session.headers.update({'Authorization': 'YOUR_API_KEY'})
                response = session.get('https://api.github.com/users/tushar-aggarwalinseec')
                print(response.json())
                
            """
        )
        
        
        st.subheader("Handling Redirects")
        
        st.markdown(
            """
            ##### To handle or disable redirects in requests:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', allow_redirects=False)
            print(response.status_code)
            """
        )
        
        
        
        st.subheader("Streaming Large Responses")
        
        st.markdown(
            """
            ##### To stream a large response to process it in chunks, rather than loading it all into memory:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', stream=True)
            for chunk in response.iter_content(chunk_size=1024):
                process_chunk(chunk) #replace 'process' with your own function
            """
        )





def plotly_():
    st.header("Working With Simple HTTP APIs")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("Basic GET Request")
        
        st.markdown(
            """
            ##### To fetch data from an API endpoint using a GET request:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            data = response.json() # Convert the response to JSON
            print(data)
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("GET Request with Query Parameters")
        
        st.markdown(
            """
            ##### To send a GET request with query parameters:
            """
        )
        st.code(
            """
            import requests
            params = {'page': 2}
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', params={'page': 2})
            data = response.json()
            print(data)
            """
        )
        
        
        
        
        st.subheader("Handling HTTP Errors")
        
        st.markdown(
            """
            ##### To handle possible HTTP errors gracefully:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            try:
                response.raise_for_status()
                data = response.json()
                print(data)
            except requests.exceptions.HTTPError as err:
                print(f'HTTP Error:{err}')
            """
        )
        
        
        st.subheader("Setting Timeout for Requests")
        
        st.markdown(
            """
            ##### To set a timeout for API requests to avoid hanging indefinitely:
            """
        )
        st.code(
            """
            import requests
            try:
                response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', timeout=5)
                data = response.json()
                print(data)
            except requests.exceptions.Timeout:
                print('The request timed out, Please try again')
            """
        )
        
        
        
        st.subheader("Using Headers in Requests")
        
        st.markdown(
            """
            ##### To include headers in your request (e.g., for authorization):
            """
        )
        st.code(
            """
            import requests
            headers = {
                'Authorization': 'YOUR_API_KEY'
            }
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', headers=headers)
            data = response.json()
            print(data)
            """
        )
            
        
    with col2:
        st.subheader("POST Request with JSON Payload")
        
        st.markdown(
            """
            ##### To send data to an API endpoint using a POST request with a JSON payload:
            """
        )
        st.code(
            """
            import requests
            payload = {'key1': 'value1', 'key2': 'value2'}
            headers = {'Content-type': 'application/json'}
            response = requests.post('https://httpbin.org/post', data=json.dumps(payload), headers=headers)
            print(response.json())
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("Handling Response Encoding")
        
        st.markdown(
            """
            ##### To handle the response encoding properly:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            response.encoding = 'utf-8'
            data = response.text
            print(data)          
            """
        )
        
        
        
        
        st.subheader("Using Sessions with Requests")
        
        st.markdown(
            """
            ##### To use a session object for making multiple requests to the same host, whichcan improve performance:
            """
        )
        st.code(
            """
            import requests
            with requests.Session() as session:
                session.headers.update({'Authorization': 'YOUR_API_KEY'})
                response = session.get('https://api.github.com/users/tushar-aggarwalinseec')
                print(response.json())
                
            """
        )
        
        
        st.subheader("Handling Redirects")
        
        st.markdown(
            """
            ##### To handle or disable redirects in requests:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', allow_redirects=False)
            print(response.status_code)
            """
        )
        
        
        
        st.subheader("Streaming Large Responses")
        
        st.markdown(
            """
            ##### To stream a large response to process it in chunks, rather than loading it all into memory:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', stream=True)
            for chunk in response.iter_content(chunk_size=1024):
                process_chunk(chunk) #replace 'process' with your own function
            """
        )





def func():
    st.header("Working With Simple HTTP APIs")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("Basic GET Request")
        
        st.markdown(
            """
            ##### To fetch data from an API endpoint using a GET request:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            data = response.json() # Convert the response to JSON
            print(data)
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("GET Request with Query Parameters")
        
        st.markdown(
            """
            ##### To send a GET request with query parameters:
            """
        )
        st.code(
            """
            import requests
            params = {'page': 2}
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', params={'page': 2})
            data = response.json()
            print(data)
            """
        )
        
        
        
        
        st.subheader("Handling HTTP Errors")
        
        st.markdown(
            """
            ##### To handle possible HTTP errors gracefully:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            try:
                response.raise_for_status()
                data = response.json()
                print(data)
            except requests.exceptions.HTTPError as err:
                print(f'HTTP Error:{err}')
            """
        )
        
        
        st.subheader("Setting Timeout for Requests")
        
        st.markdown(
            """
            ##### To set a timeout for API requests to avoid hanging indefinitely:
            """
        )
        st.code(
            """
            import requests
            try:
                response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', timeout=5)
                data = response.json()
                print(data)
            except requests.exceptions.Timeout:
                print('The request timed out, Please try again')
            """
        )
        
        
        
        st.subheader("Using Headers in Requests")
        
        st.markdown(
            """
            ##### To include headers in your request (e.g., for authorization):
            """
        )
        st.code(
            """
            import requests
            headers = {
                'Authorization': 'YOUR_API_KEY'
            }
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', headers=headers)
            data = response.json()
            print(data)
            """
        )
            
        
    with col2:
        st.subheader("POST Request with JSON Payload")
        
        st.markdown(
            """
            ##### To send data to an API endpoint using a POST request with a JSON payload:
            """
        )
        st.code(
            """
            import requests
            payload = {'key1': 'value1', 'key2': 'value2'}
            headers = {'Content-type': 'application/json'}
            response = requests.post('https://httpbin.org/post', data=json.dumps(payload), headers=headers)
            print(response.json())
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("Handling Response Encoding")
        
        st.markdown(
            """
            ##### To handle the response encoding properly:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            response.encoding = 'utf-8'
            data = response.text
            print(data)          
            """
        )
        
        
        
        
        st.subheader("Using Sessions with Requests")
        
        st.markdown(
            """
            ##### To use a session object for making multiple requests to the same host, whichcan improve performance:
            """
        )
        st.code(
            """
            import requests
            with requests.Session() as session:
                session.headers.update({'Authorization': 'YOUR_API_KEY'})
                response = session.get('https://api.github.com/users/tushar-aggarwalinseec')
                print(response.json())
                
            """
        )
        
        
        st.subheader("Handling Redirects")
        
        st.markdown(
            """
            ##### To handle or disable redirects in requests:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', allow_redirects=False)
            print(response.status_code)
            """
        )
        
        
        
        st.subheader("Streaming Large Responses")
        
        st.markdown(
            """
            ##### To stream a large response to process it in chunks, rather than loading it all into memory:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', stream=True)
            for chunk in response.iter_content(chunk_size=1024):
                process_chunk(chunk) #replace 'process' with your own function
            """
        )






def func():
    st.header("Working With Simple HTTP APIs")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("Basic GET Request")
        
        st.markdown(
            """
            ##### To fetch data from an API endpoint using a GET request:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            data = response.json() # Convert the response to JSON
            print(data)
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("GET Request with Query Parameters")
        
        st.markdown(
            """
            ##### To send a GET request with query parameters:
            """
        )
        st.code(
            """
            import requests
            params = {'page': 2}
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', params={'page': 2})
            data = response.json()
            print(data)
            """
        )
        
        
        
        
        st.subheader("Handling HTTP Errors")
        
        st.markdown(
            """
            ##### To handle possible HTTP errors gracefully:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            try:
                response.raise_for_status()
                data = response.json()
                print(data)
            except requests.exceptions.HTTPError as err:
                print(f'HTTP Error:{err}')
            """
        )
        
        
        st.subheader("Setting Timeout for Requests")
        
        st.markdown(
            """
            ##### To set a timeout for API requests to avoid hanging indefinitely:
            """
        )
        st.code(
            """
            import requests
            try:
                response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', timeout=5)
                data = response.json()
                print(data)
            except requests.exceptions.Timeout:
                print('The request timed out, Please try again')
            """
        )
        
        
        
        st.subheader("Using Headers in Requests")
        
        st.markdown(
            """
            ##### To include headers in your request (e.g., for authorization):
            """
        )
        st.code(
            """
            import requests
            headers = {
                'Authorization': 'YOUR_API_KEY'
            }
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', headers=headers)
            data = response.json()
            print(data)
            """
        )
            
        
    with col2:
        st.subheader("POST Request with JSON Payload")
        
        st.markdown(
            """
            ##### To send data to an API endpoint using a POST request with a JSON payload:
            """
        )
        st.code(
            """
            import requests
            payload = {'key1': 'value1', 'key2': 'value2'}
            headers = {'Content-type': 'application/json'}
            response = requests.post('https://httpbin.org/post', data=json.dumps(payload), headers=headers)
            print(response.json())
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("Handling Response Encoding")
        
        st.markdown(
            """
            ##### To handle the response encoding properly:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            response.encoding = 'utf-8'
            data = response.text
            print(data)          
            """
        )
        
        
        
        
        st.subheader("Using Sessions with Requests")
        
        st.markdown(
            """
            ##### To use a session object for making multiple requests to the same host, whichcan improve performance:
            """
        )
        st.code(
            """
            import requests
            with requests.Session() as session:
                session.headers.update({'Authorization': 'YOUR_API_KEY'})
                response = session.get('https://api.github.com/users/tushar-aggarwalinseec')
                print(response.json())
                
            """
        )
        
        
        st.subheader("Handling Redirects")
        
        st.markdown(
            """
            ##### To handle or disable redirects in requests:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', allow_redirects=False)
            print(response.status_code)
            """
        )
        
        
        
        st.subheader("Streaming Large Responses")
        
        st.markdown(
            """
            ##### To stream a large response to process it in chunks, rather than loading it all into memory:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', stream=True)
            for chunk in response.iter_content(chunk_size=1024):
                process_chunk(chunk) #replace 'process' with your own function
            """
        )






def func():
    st.header("Working With Simple HTTP APIs")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("Basic GET Request")
        
        st.markdown(
            """
            ##### To fetch data from an API endpoint using a GET request:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            data = response.json() # Convert the response to JSON
            print(data)
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("GET Request with Query Parameters")
        
        st.markdown(
            """
            ##### To send a GET request with query parameters:
            """
        )
        st.code(
            """
            import requests
            params = {'page': 2}
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', params={'page': 2})
            data = response.json()
            print(data)
            """
        )
        
        
        
        
        st.subheader("Handling HTTP Errors")
        
        st.markdown(
            """
            ##### To handle possible HTTP errors gracefully:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            try:
                response.raise_for_status()
                data = response.json()
                print(data)
            except requests.exceptions.HTTPError as err:
                print(f'HTTP Error:{err}')
            """
        )
        
        
        st.subheader("Setting Timeout for Requests")
        
        st.markdown(
            """
            ##### To set a timeout for API requests to avoid hanging indefinitely:
            """
        )
        st.code(
            """
            import requests
            try:
                response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', timeout=5)
                data = response.json()
                print(data)
            except requests.exceptions.Timeout:
                print('The request timed out, Please try again')
            """
        )
        
        
        
        st.subheader("Using Headers in Requests")
        
        st.markdown(
            """
            ##### To include headers in your request (e.g., for authorization):
            """
        )
        st.code(
            """
            import requests
            headers = {
                'Authorization': 'YOUR_API_KEY'
            }
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', headers=headers)
            data = response.json()
            print(data)
            """
        )
            
        
    with col2:
        st.subheader("POST Request with JSON Payload")
        
        st.markdown(
            """
            ##### To send data to an API endpoint using a POST request with a JSON payload:
            """
        )
        st.code(
            """
            import requests
            payload = {'key1': 'value1', 'key2': 'value2'}
            headers = {'Content-type': 'application/json'}
            response = requests.post('https://httpbin.org/post', data=json.dumps(payload), headers=headers)
            print(response.json())
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("Handling Response Encoding")
        
        st.markdown(
            """
            ##### To handle the response encoding properly:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            response.encoding = 'utf-8'
            data = response.text
            print(data)          
            """
        )
        
        
        
        
        st.subheader("Using Sessions with Requests")
        
        st.markdown(
            """
            ##### To use a session object for making multiple requests to the same host, whichcan improve performance:
            """
        )
        st.code(
            """
            import requests
            with requests.Session() as session:
                session.headers.update({'Authorization': 'YOUR_API_KEY'})
                response = session.get('https://api.github.com/users/tushar-aggarwalinseec')
                print(response.json())
                
            """
        )
        
        
        st.subheader("Handling Redirects")
        
        st.markdown(
            """
            ##### To handle or disable redirects in requests:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', allow_redirects=False)
            print(response.status_code)
            """
        )
        
        
        
        st.subheader("Streaming Large Responses")
        
        st.markdown(
            """
            ##### To stream a large response to process it in chunks, rather than loading it all into memory:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', stream=True)
            for chunk in response.iter_content(chunk_size=1024):
                process_chunk(chunk) #replace 'process' with your own function
            """
        )






def func():
    st.header("Working With Simple HTTP APIs")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("Basic GET Request")
        
        st.markdown(
            """
            ##### To fetch data from an API endpoint using a GET request:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            data = response.json() # Convert the response to JSON
            print(data)
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("GET Request with Query Parameters")
        
        st.markdown(
            """
            ##### To send a GET request with query parameters:
            """
        )
        st.code(
            """
            import requests
            params = {'page': 2}
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', params={'page': 2})
            data = response.json()
            print(data)
            """
        )
        
        
        
        
        st.subheader("Handling HTTP Errors")
        
        st.markdown(
            """
            ##### To handle possible HTTP errors gracefully:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            try:
                response.raise_for_status()
                data = response.json()
                print(data)
            except requests.exceptions.HTTPError as err:
                print(f'HTTP Error:{err}')
            """
        )
        
        
        st.subheader("Setting Timeout for Requests")
        
        st.markdown(
            """
            ##### To set a timeout for API requests to avoid hanging indefinitely:
            """
        )
        st.code(
            """
            import requests
            try:
                response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', timeout=5)
                data = response.json()
                print(data)
            except requests.exceptions.Timeout:
                print('The request timed out, Please try again')
            """
        )
        
        
        
        st.subheader("Using Headers in Requests")
        
        st.markdown(
            """
            ##### To include headers in your request (e.g., for authorization):
            """
        )
        st.code(
            """
            import requests
            headers = {
                'Authorization': 'YOUR_API_KEY'
            }
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', headers=headers)
            data = response.json()
            print(data)
            """
        )
            
        
    with col2:
        st.subheader("POST Request with JSON Payload")
        
        st.markdown(
            """
            ##### To send data to an API endpoint using a POST request with a JSON payload:
            """
        )
        st.code(
            """
            import requests
            payload = {'key1': 'value1', 'key2': 'value2'}
            headers = {'Content-type': 'application/json'}
            response = requests.post('https://httpbin.org/post', data=json.dumps(payload), headers=headers)
            print(response.json())
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("Handling Response Encoding")
        
        st.markdown(
            """
            ##### To handle the response encoding properly:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            response.encoding = 'utf-8'
            data = response.text
            print(data)          
            """
        )
        
        
        
        
        st.subheader("Using Sessions with Requests")
        
        st.markdown(
            """
            ##### To use a session object for making multiple requests to the same host, whichcan improve performance:
            """
        )
        st.code(
            """
            import requests
            with requests.Session() as session:
                session.headers.update({'Authorization': 'YOUR_API_KEY'})
                response = session.get('https://api.github.com/users/tushar-aggarwalinseec')
                print(response.json())
                
            """
        )
        
        
        st.subheader("Handling Redirects")
        
        st.markdown(
            """
            ##### To handle or disable redirects in requests:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', allow_redirects=False)
            print(response.status_code)
            """
        )
        
        
        
        st.subheader("Streaming Large Responses")
        
        st.markdown(
            """
            ##### To stream a large response to process it in chunks, rather than loading it all into memory:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', stream=True)
            for chunk in response.iter_content(chunk_size=1024):
                process_chunk(chunk) #replace 'process' with your own function
            """
        )






def func():
    st.header("Working With Simple HTTP APIs")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("Basic GET Request")
        
        st.markdown(
            """
            ##### To fetch data from an API endpoint using a GET request:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            data = response.json() # Convert the response to JSON
            print(data)
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("GET Request with Query Parameters")
        
        st.markdown(
            """
            ##### To send a GET request with query parameters:
            """
        )
        st.code(
            """
            import requests
            params = {'page': 2}
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', params={'page': 2})
            data = response.json()
            print(data)
            """
        )
        
        
        
        
        st.subheader("Handling HTTP Errors")
        
        st.markdown(
            """
            ##### To handle possible HTTP errors gracefully:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            try:
                response.raise_for_status()
                data = response.json()
                print(data)
            except requests.exceptions.HTTPError as err:
                print(f'HTTP Error:{err}')
            """
        )
        
        
        st.subheader("Setting Timeout for Requests")
        
        st.markdown(
            """
            ##### To set a timeout for API requests to avoid hanging indefinitely:
            """
        )
        st.code(
            """
            import requests
            try:
                response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', timeout=5)
                data = response.json()
                print(data)
            except requests.exceptions.Timeout:
                print('The request timed out, Please try again')
            """
        )
        
        
        
        st.subheader("Using Headers in Requests")
        
        st.markdown(
            """
            ##### To include headers in your request (e.g., for authorization):
            """
        )
        st.code(
            """
            import requests
            headers = {
                'Authorization': 'YOUR_API_KEY'
            }
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', headers=headers)
            data = response.json()
            print(data)
            """
        )
            
        
    with col2:
        st.subheader("POST Request with JSON Payload")
        
        st.markdown(
            """
            ##### To send data to an API endpoint using a POST request with a JSON payload:
            """
        )
        st.code(
            """
            import requests
            payload = {'key1': 'value1', 'key2': 'value2'}
            headers = {'Content-type': 'application/json'}
            response = requests.post('https://httpbin.org/post', data=json.dumps(payload), headers=headers)
            print(response.json())
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("Handling Response Encoding")
        
        st.markdown(
            """
            ##### To handle the response encoding properly:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            response.encoding = 'utf-8'
            data = response.text
            print(data)          
            """
        )
        
        
        
        
        st.subheader("Using Sessions with Requests")
        
        st.markdown(
            """
            ##### To use a session object for making multiple requests to the same host, whichcan improve performance:
            """
        )
        st.code(
            """
            import requests
            with requests.Session() as session:
                session.headers.update({'Authorization': 'YOUR_API_KEY'})
                response = session.get('https://api.github.com/users/tushar-aggarwalinseec')
                print(response.json())
                
            """
        )
        
        
        st.subheader("Handling Redirects")
        
        st.markdown(
            """
            ##### To handle or disable redirects in requests:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', allow_redirects=False)
            print(response.status_code)
            """
        )
        
        
        
        st.subheader("Streaming Large Responses")
        
        st.markdown(
            """
            ##### To stream a large response to process it in chunks, rather than loading it all into memory:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', stream=True)
            for chunk in response.iter_content(chunk_size=1024):
                process_chunk(chunk) #replace 'process' with your own function
            """
        )





def func():
    st.header("Working With Simple HTTP APIs")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("Basic GET Request")
        
        st.markdown(
            """
            ##### To fetch data from an API endpoint using a GET request:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            data = response.json() # Convert the response to JSON
            print(data)
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("GET Request with Query Parameters")
        
        st.markdown(
            """
            ##### To send a GET request with query parameters:
            """
        )
        st.code(
            """
            import requests
            params = {'page': 2}
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', params={'page': 2})
            data = response.json()
            print(data)
            """
        )
        
        
        
        
        st.subheader("Handling HTTP Errors")
        
        st.markdown(
            """
            ##### To handle possible HTTP errors gracefully:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            try:
                response.raise_for_status()
                data = response.json()
                print(data)
            except requests.exceptions.HTTPError as err:
                print(f'HTTP Error:{err}')
            """
        )
        
        
        st.subheader("Setting Timeout for Requests")
        
        st.markdown(
            """
            ##### To set a timeout for API requests to avoid hanging indefinitely:
            """
        )
        st.code(
            """
            import requests
            try:
                response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', timeout=5)
                data = response.json()
                print(data)
            except requests.exceptions.Timeout:
                print('The request timed out, Please try again')
            """
        )
        
        
        
        st.subheader("Using Headers in Requests")
        
        st.markdown(
            """
            ##### To include headers in your request (e.g., for authorization):
            """
        )
        st.code(
            """
            import requests
            headers = {
                'Authorization': 'YOUR_API_KEY'
            }
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', headers=headers)
            data = response.json()
            print(data)
            """
        )
            
        
    with col2:
        st.subheader("POST Request with JSON Payload")
        
        st.markdown(
            """
            ##### To send data to an API endpoint using a POST request with a JSON payload:
            """
        )
        st.code(
            """
            import requests
            payload = {'key1': 'value1', 'key2': 'value2'}
            headers = {'Content-type': 'application/json'}
            response = requests.post('https://httpbin.org/post', data=json.dumps(payload), headers=headers)
            print(response.json())
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("Handling Response Encoding")
        
        st.markdown(
            """
            ##### To handle the response encoding properly:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            response.encoding = 'utf-8'
            data = response.text
            print(data)          
            """
        )
        
        
        
        
        st.subheader("Using Sessions with Requests")
        
        st.markdown(
            """
            ##### To use a session object for making multiple requests to the same host, whichcan improve performance:
            """
        )
        st.code(
            """
            import requests
            with requests.Session() as session:
                session.headers.update({'Authorization': 'YOUR_API_KEY'})
                response = session.get('https://api.github.com/users/tushar-aggarwalinseec')
                print(response.json())
                
            """
        )
        
        
        st.subheader("Handling Redirects")
        
        st.markdown(
            """
            ##### To handle or disable redirects in requests:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', allow_redirects=False)
            print(response.status_code)
            """
        )
        
        
        
        st.subheader("Streaming Large Responses")
        
        st.markdown(
            """
            ##### To stream a large response to process it in chunks, rather than loading it all into memory:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', stream=True)
            for chunk in response.iter_content(chunk_size=1024):
                process_chunk(chunk) #replace 'process' with your own function
            """
        )





def func():
    st.header("Working With Simple HTTP APIs")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("Basic GET Request")
        
        st.markdown(
            """
            ##### To fetch data from an API endpoint using a GET request:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            data = response.json() # Convert the response to JSON
            print(data)
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("GET Request with Query Parameters")
        
        st.markdown(
            """
            ##### To send a GET request with query parameters:
            """
        )
        st.code(
            """
            import requests
            params = {'page': 2}
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', params={'page': 2})
            data = response.json()
            print(data)
            """
        )
        
        
        
        
        st.subheader("Handling HTTP Errors")
        
        st.markdown(
            """
            ##### To handle possible HTTP errors gracefully:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            try:
                response.raise_for_status()
                data = response.json()
                print(data)
            except requests.exceptions.HTTPError as err:
                print(f'HTTP Error:{err}')
            """
        )
        
        
        st.subheader("Setting Timeout for Requests")
        
        st.markdown(
            """
            ##### To set a timeout for API requests to avoid hanging indefinitely:
            """
        )
        st.code(
            """
            import requests
            try:
                response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', timeout=5)
                data = response.json()
                print(data)
            except requests.exceptions.Timeout:
                print('The request timed out, Please try again')
            """
        )
        
        
        
        st.subheader("Using Headers in Requests")
        
        st.markdown(
            """
            ##### To include headers in your request (e.g., for authorization):
            """
        )
        st.code(
            """
            import requests
            headers = {
                'Authorization': 'YOUR_API_KEY'
            }
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', headers=headers)
            data = response.json()
            print(data)
            """
        )
            
        
    with col2:
        st.subheader("POST Request with JSON Payload")
        
        st.markdown(
            """
            ##### To send data to an API endpoint using a POST request with a JSON payload:
            """
        )
        st.code(
            """
            import requests
            payload = {'key1': 'value1', 'key2': 'value2'}
            headers = {'Content-type': 'application/json'}
            response = requests.post('https://httpbin.org/post', data=json.dumps(payload), headers=headers)
            print(response.json())
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("Handling Response Encoding")
        
        st.markdown(
            """
            ##### To handle the response encoding properly:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            response.encoding = 'utf-8'
            data = response.text
            print(data)          
            """
        )
        
        
        
        
        st.subheader("Using Sessions with Requests")
        
        st.markdown(
            """
            ##### To use a session object for making multiple requests to the same host, whichcan improve performance:
            """
        )
        st.code(
            """
            import requests
            with requests.Session() as session:
                session.headers.update({'Authorization': 'YOUR_API_KEY'})
                response = session.get('https://api.github.com/users/tushar-aggarwalinseec')
                print(response.json())
                
            """
        )
        
        
        st.subheader("Handling Redirects")
        
        st.markdown(
            """
            ##### To handle or disable redirects in requests:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', allow_redirects=False)
            print(response.status_code)
            """
        )
        
        
        
        st.subheader("Streaming Large Responses")
        
        st.markdown(
            """
            ##### To stream a large response to process it in chunks, rather than loading it all into memory:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', stream=True)
            for chunk in response.iter_content(chunk_size=1024):
                process_chunk(chunk) #replace 'process' with your own function
            """
        )






def func():
    st.header("Working With Simple HTTP APIs")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("Basic GET Request")
        
        st.markdown(
            """
            ##### To fetch data from an API endpoint using a GET request:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            data = response.json() # Convert the response to JSON
            print(data)
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("GET Request with Query Parameters")
        
        st.markdown(
            """
            ##### To send a GET request with query parameters:
            """
        )
        st.code(
            """
            import requests
            params = {'page': 2}
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', params={'page': 2})
            data = response.json()
            print(data)
            """
        )
        
        
        
        
        st.subheader("Handling HTTP Errors")
        
        st.markdown(
            """
            ##### To handle possible HTTP errors gracefully:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            try:
                response.raise_for_status()
                data = response.json()
                print(data)
            except requests.exceptions.HTTPError as err:
                print(f'HTTP Error:{err}')
            """
        )
        
        
        st.subheader("Setting Timeout for Requests")
        
        st.markdown(
            """
            ##### To set a timeout for API requests to avoid hanging indefinitely:
            """
        )
        st.code(
            """
            import requests
            try:
                response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', timeout=5)
                data = response.json()
                print(data)
            except requests.exceptions.Timeout:
                print('The request timed out, Please try again')
            """
        )
        
        
        
        st.subheader("Using Headers in Requests")
        
        st.markdown(
            """
            ##### To include headers in your request (e.g., for authorization):
            """
        )
        st.code(
            """
            import requests
            headers = {
                'Authorization': 'YOUR_API_KEY'
            }
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', headers=headers)
            data = response.json()
            print(data)
            """
        )
            
        
    with col2:
        st.subheader("POST Request with JSON Payload")
        
        st.markdown(
            """
            ##### To send data to an API endpoint using a POST request with a JSON payload:
            """
        )
        st.code(
            """
            import requests
            payload = {'key1': 'value1', 'key2': 'value2'}
            headers = {'Content-type': 'application/json'}
            response = requests.post('https://httpbin.org/post', data=json.dumps(payload), headers=headers)
            print(response.json())
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("Handling Response Encoding")
        
        st.markdown(
            """
            ##### To handle the response encoding properly:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            response.encoding = 'utf-8'
            data = response.text
            print(data)          
            """
        )
        
        
        
        
        st.subheader("Using Sessions with Requests")
        
        st.markdown(
            """
            ##### To use a session object for making multiple requests to the same host, whichcan improve performance:
            """
        )
        st.code(
            """
            import requests
            with requests.Session() as session:
                session.headers.update({'Authorization': 'YOUR_API_KEY'})
                response = session.get('https://api.github.com/users/tushar-aggarwalinseec')
                print(response.json())
                
            """
        )
        
        
        st.subheader("Handling Redirects")
        
        st.markdown(
            """
            ##### To handle or disable redirects in requests:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', allow_redirects=False)
            print(response.status_code)
            """
        )
        
        
        
        st.subheader("Streaming Large Responses")
        
        st.markdown(
            """
            ##### To stream a large response to process it in chunks, rather than loading it all into memory:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', stream=True)
            for chunk in response.iter_content(chunk_size=1024):
                process_chunk(chunk) #replace 'process' with your own function
            """
        )







def func():
    st.header("Working With Simple HTTP APIs")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("Basic GET Request")
        
        st.markdown(
            """
            ##### To fetch data from an API endpoint using a GET request:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            data = response.json() # Convert the response to JSON
            print(data)
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("GET Request with Query Parameters")
        
        st.markdown(
            """
            ##### To send a GET request with query parameters:
            """
        )
        st.code(
            """
            import requests
            params = {'page': 2}
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', params={'page': 2})
            data = response.json()
            print(data)
            """
        )
        
        
        
        
        st.subheader("Handling HTTP Errors")
        
        st.markdown(
            """
            ##### To handle possible HTTP errors gracefully:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            try:
                response.raise_for_status()
                data = response.json()
                print(data)
            except requests.exceptions.HTTPError as err:
                print(f'HTTP Error:{err}')
            """
        )
        
        
        st.subheader("Setting Timeout for Requests")
        
        st.markdown(
            """
            ##### To set a timeout for API requests to avoid hanging indefinitely:
            """
        )
        st.code(
            """
            import requests
            try:
                response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', timeout=5)
                data = response.json()
                print(data)
            except requests.exceptions.Timeout:
                print('The request timed out, Please try again')
            """
        )
        
        
        
        st.subheader("Using Headers in Requests")
        
        st.markdown(
            """
            ##### To include headers in your request (e.g., for authorization):
            """
        )
        st.code(
            """
            import requests
            headers = {
                'Authorization': 'YOUR_API_KEY'
            }
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', headers=headers)
            data = response.json()
            print(data)
            """
        )
            
        
    with col2:
        st.subheader("POST Request with JSON Payload")
        
        st.markdown(
            """
            ##### To send data to an API endpoint using a POST request with a JSON payload:
            """
        )
        st.code(
            """
            import requests
            payload = {'key1': 'value1', 'key2': 'value2'}
            headers = {'Content-type': 'application/json'}
            response = requests.post('https://httpbin.org/post', data=json.dumps(payload), headers=headers)
            print(response.json())
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("Handling Response Encoding")
        
        st.markdown(
            """
            ##### To handle the response encoding properly:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            response.encoding = 'utf-8'
            data = response.text
            print(data)          
            """
        )
        
        
        
        
        st.subheader("Using Sessions with Requests")
        
        st.markdown(
            """
            ##### To use a session object for making multiple requests to the same host, whichcan improve performance:
            """
        )
        st.code(
            """
            import requests
            with requests.Session() as session:
                session.headers.update({'Authorization': 'YOUR_API_KEY'})
                response = session.get('https://api.github.com/users/tushar-aggarwalinseec')
                print(response.json())
                
            """
        )
        
        
        st.subheader("Handling Redirects")
        
        st.markdown(
            """
            ##### To handle or disable redirects in requests:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', allow_redirects=False)
            print(response.status_code)
            """
        )
        
        
        
        st.subheader("Streaming Large Responses")
        
        st.markdown(
            """
            ##### To stream a large response to process it in chunks, rather than loading it all into memory:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', stream=True)
            for chunk in response.iter_content(chunk_size=1024):
                process_chunk(chunk) #replace 'process' with your own function
            """
        )





def func():
    st.header("Working With Simple HTTP APIs")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("Basic GET Request")
        
        st.markdown(
            """
            ##### To fetch data from an API endpoint using a GET request:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            data = response.json() # Convert the response to JSON
            print(data)
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("GET Request with Query Parameters")
        
        st.markdown(
            """
            ##### To send a GET request with query parameters:
            """
        )
        st.code(
            """
            import requests
            params = {'page': 2}
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', params={'page': 2})
            data = response.json()
            print(data)
            """
        )
        
        
        
        
        st.subheader("Handling HTTP Errors")
        
        st.markdown(
            """
            ##### To handle possible HTTP errors gracefully:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            try:
                response.raise_for_status()
                data = response.json()
                print(data)
            except requests.exceptions.HTTPError as err:
                print(f'HTTP Error:{err}')
            """
        )
        
        
        st.subheader("Setting Timeout for Requests")
        
        st.markdown(
            """
            ##### To set a timeout for API requests to avoid hanging indefinitely:
            """
        )
        st.code(
            """
            import requests
            try:
                response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', timeout=5)
                data = response.json()
                print(data)
            except requests.exceptions.Timeout:
                print('The request timed out, Please try again')
            """
        )
        
        
        
        st.subheader("Using Headers in Requests")
        
        st.markdown(
            """
            ##### To include headers in your request (e.g., for authorization):
            """
        )
        st.code(
            """
            import requests
            headers = {
                'Authorization': 'YOUR_API_KEY'
            }
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', headers=headers)
            data = response.json()
            print(data)
            """
        )
            
        
    with col2:
        st.subheader("POST Request with JSON Payload")
        
        st.markdown(
            """
            ##### To send data to an API endpoint using a POST request with a JSON payload:
            """
        )
        st.code(
            """
            import requests
            payload = {'key1': 'value1', 'key2': 'value2'}
            headers = {'Content-type': 'application/json'}
            response = requests.post('https://httpbin.org/post', data=json.dumps(payload), headers=headers)
            print(response.json())
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("Handling Response Encoding")
        
        st.markdown(
            """
            ##### To handle the response encoding properly:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            response.encoding = 'utf-8'
            data = response.text
            print(data)          
            """
        )
        
        
        
        
        st.subheader("Using Sessions with Requests")
        
        st.markdown(
            """
            ##### To use a session object for making multiple requests to the same host, whichcan improve performance:
            """
        )
        st.code(
            """
            import requests
            with requests.Session() as session:
                session.headers.update({'Authorization': 'YOUR_API_KEY'})
                response = session.get('https://api.github.com/users/tushar-aggarwalinseec')
                print(response.json())
                
            """
        )
        
        
        st.subheader("Handling Redirects")
        
        st.markdown(
            """
            ##### To handle or disable redirects in requests:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', allow_redirects=False)
            print(response.status_code)
            """
        )
        
        
        
        st.subheader("Streaming Large Responses")
        
        st.markdown(
            """
            ##### To stream a large response to process it in chunks, rather than loading it all into memory:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', stream=True)
            for chunk in response.iter_content(chunk_size=1024):
                process_chunk(chunk) #replace 'process' with your own function
            """
        )





def one_liner_60():
    
    st.header("Powerful Python One-Liners for Everyday Coding Tasks")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        
        st.markdown(
            """
            ##### 1) Print the systems’s hostname:
            """
        )
        st.code(
            """
            from socket import gethostname; print gethostname()
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        
        st.markdown(
            """
            ##### 2) Decode string written in Hex:
            """
        )
        st.code(
            """
            python -c "print ''.join(chr(int(''.join(i), 16)) for i in zip(*[iter('\\x01\\x02\\x03\\x04\\x05\\x06\\x07\\x08\\x09\\x0a\\x0b\\x0c\\x0d\\x0e\\x0f\\x10\\x11\\x12\\x13\\x14\\x15\\x16\\x17\\x18\\x19\\x1a\\x1b\\x1c\\x1d\\x1e\\x1f')] * 16))"
            """
        )
        
        
        
        st.markdown(
            """
            ##### 3) Read Lines from a File:
            """
        )
        st.code(
            """
            lines = [line.strip() for line in open ('example.txt')]
            """
        )
        
        
        
        
        st.markdown(
            """
            ##### 4) Count Lines in a File:
            """
        )
        st.code(
            """
            line_count = sum(1 for line in open('example.txt'))
            """
        )
        
        
        
        st.markdown(
            """
            ##### 5) Extract Digits from a String:
            """
        )
        st.code(
            """
            digits = ''.join(filter(str.isdigit, mystring))
            """
        )
        
        
        
        
        st.markdown(
            """
            ##### 6) List Comprehension with Conditional:
            """
        )
        st.code(
            """
            filtered_list = [x for x in my_list if x > 0]
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        
        st.markdown(
            """
            ##### 7) Remove Duplicates from a List:
            """
        )
        st.code(
            """
            unique_list = list(set(original_list))
            """
        )
        
        
        
        
        
        st.markdown(
            """
            ##### 8) Calculate Average of a List:
            """
        )
        st.code(
            """
            average = sum(my_list) / len(my_list) if len(my_list) > 0 else 0
            """
        )
        
        
        
        
        st.markdown(
            """
            ##### 9) Generate Fibonacci Sequence:
            """
        )
        st.code(
            """
            fibonacci = lambda n: n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
            """
        )
        
        
        
        
        st.markdown(
            """
            ##### 10) Conditional Value Assignment:
            """
        )
        st.code(
            """
            result = x if condition else y
            """
        )
        
        
        
        st.markdown(
            """
            ##### 11) One-Liner For Loop:
            """
        )
        st.code(
            """
            squares = [x**2 for x in range(10)]
            """
        )
        
        squares = [x**2 for x in range(10)]
        if st.toggle("Show sample output",):
            st.write(squares)
        
        
        
        st.markdown(
            """
            ##### 12) Handle Zero Division Error:
            """
        )
        st.code(
            """
            result = numerator / denominator if denominator != 0 else 0
            """
        )
        
        
        
        
        
        st.markdown(
            """
            ##### 13) One-Liner Try-Except Block:
            """
        )
        st.code(
            """
            result = try_block() if success else except_block()
            """
        )
        
        
        
        
        st.markdown(
            """
            ##### 14) Object Initialization with Default Values:
            """
        )
        st.code(
            """
            my_object = MyClass(**kwargs) if kwargs else MyClass()
            """
        )
        
        
        
        
        
        st.markdown(
            """
            ##### 15) Fetch HTML Content with Requests:
            """
        )
        st.code(
            """
            import requests; html_content = requests.get('https://example.com').text
            """
        )
        
        
       
        
        st.markdown(
            """
            ##### 16) Pandas DataFrame Initialization:
            """
        )
        st.code(
            """
            import pandas as pd; df = pd.DataFrame(data, columns=['col1', 'col2'])
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        
        
        st.markdown(
            """
            ##### 17. Filter DataFrame Rows with Pandas:
            """
        )
        st.code(
            """
            filtered_df = df[df['column'] > value]
            """
        )
        
        
        
        st.markdown(
            """
            ##### 18. Generating a list of leap years using list comprehension:
            """
        )
        st.code(
            """
            leap_years = [year for year in range(2000, 2051) if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)]
            """
        )
        
    
        
        st.markdown(
            """
            ##### 19. Retrieve Public IP Address:
            """
        )
        st.code(
            """
            public_ip = requests.get('https://api64.ipify.org?format=json').json()['ip']
            """
        )
        
    
        
        st.markdown(
            """
            ##### 20. Create Basic Tkinter Window:
            """
        )
        st.code(
            """
            import tkinter.messagebox as mb; mb.showinfo('Title', 'Message')
            """
        )
        
        
       
        st.markdown(
            """
            ##### 21. Display Message Box with Tkinter:
            """
        )
        st.code(
            """
            import tkinter.messagebox as mb; mb.showinfo('Title', 'Message')
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        
        
        st.markdown(
            """
            ##### 22. Multithreading with threading Module:
            """
        )
        st.code(
            """
            import threading; threading.Thread(target=my_function).start()
            """
        )
        
        
        
    
        
        st.markdown(
            """
            ##### 23. Hashing with hashlib:
            """
        )
        st.code(
            """
            import hashlib; hashed_password = hashlib.sha256(password.encode()).hexdigest()
            """
        )
        
        
        
        
        st.markdown(
            """
            ##### 24. Check if all elements in a list are equal:
            """
        )
        st.code(
            """
            are_equal = all(x == [1, 1, 1, 1])
            """
        )
        
        
        
        st.markdown(
            """
            ##### 25. Find the second largest number in a list:
            """
        )
        st.code(
            """
            second_largest = sorted([3, 1, 4, 1, 5, 9])[-2]
            """
        )
        
        
        
       
        
        st.markdown(
            """
            ##### 26. Check if a number is prime:
            """
        )
        st.code(
            """
            is_prime = all(7 % i != 0 for i in range(2, 7))
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        
        
        st.markdown(
            """
            ##### 27. Find the most common element in a list:
            """
        )
        st.code(
            """
            most_common = max(set([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]), key=[1, 2, 2, 3, 3, 3, 4, 4, 4, 4].count)
            """
        )
        
        
        
        
        
        st.markdown(
            """
            ##### 28. Find the most common word in a list:
            """
        )
        st.code(
            """
            most_common_word = max(words, key=words.count)
            """
        )
        
        
        
        st.markdown(
            """
            ##### 29. Filter a list of numbers to get only even numbers:
            """
        )
        st.code(
            """
            even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
            """
        )
        
        
        
        
        st.markdown(
            """
            ##### 30. Merge two dictionaries:
            """
        )
        st.code(
            """
            merged_dict = {**dict1, **dict2}
            """
        )
            
        
    with col2:
        
        
        st.markdown(
            """
            ##### 31. Find the index of the first occurrence of an item in a list:
            """
        )
        st.code(
            """
            index = next((i for i, v in enumerate(my_list) if v == 1), None)
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
       
        
        st.markdown(
            """
            ##### 32. Remove vowels from a string:
            """
        )
        st.code(
            """
            without_vowels = ''.join(char for char in my_string if char.lower() not in 'aeiou')       
            """
        )
        
        
        
        
       
        
        st.markdown(
            """
            ##### 33. Transpose a matrix using zip:
            """
        )
        st.code(
            """
            transposed = list(zip(*matrix))
            """
        )
        
        
        
        
        st.markdown(
            """
            ##### 34. Check if a key exists in a dictionary:
            """
        )
        st.code(
            """
            is_present = 'key' in {'key': 'value'}
            """
        )
        
        
        
        
        
        st.markdown(
            """
            ##### 35. Check if a number is odd:
            """
        )
        st.code(
            """
            is_odd = num % 2 != 0
            """
        )
        
        
        
        
        
        st.markdown(
            """
            ##### 36. Check if a number is even:
            """
        )
        st.code(
            """
            is_even = num % 2 == 0
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        
        
        st.markdown(
            """
            ##### 37. Check if a number is a perfect square:
            """
        )
        st.code(
            """
            is_perfect_square = lambda n: n**0.5 == int(n**0.5)          
            """
        )
        
        
        
        
    
        st.markdown(
            """
            ##### 38. Check if a number is a power of two:
            """
        )
        st.code(
            """
            is_power_of_two = lambda n: (n & (n - 1)) == 0 and n != 0
            """
        )
        
        
        
        st.markdown(
            """
            ##### 39. Check if a year is a leap year:
            """
        )
        st.code(
            """
            is_leap_year = lambda year: (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
            """
        )
        
        
        
        
        
        st.markdown(
            """
            ##### 40. Extracting domain from an email address using regex:
            """
        )
        st.code(
            """
            import re
            domain = re.search(r'@(\w+\.\w+)', 'user@example.com').group(1)
            """
        )
        
        
        
        
        
        st.markdown(
            """
            ##### To send data to an API endpoint using a POST request with a JSON payload:
            """
        )
        st.code(
            """
            import requests
            payload = {'key1': 'value1', 'key2': 'value2'}
            headers = {'Content-type': 'application/json'}
            response = requests.post('https://httpbin.org/post', data=json.dumps(payload), headers=headers)
            print(response.json())
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        
        st.markdown(
            """
            ##### To handle the response encoding properly:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            response.encoding = 'utf-8'
            data = response.text
            print(data)          
            """
        )
        
        
        
        
        
        st.markdown(
            """
            ##### To use a session object for making multiple requests to the same host, whichcan improve performance:
            """
        )
        st.code(
            """
            import requests
            with requests.Session() as session:
                session.headers.update({'Authorization': 'YOUR_API_KEY'})
                response = session.get('https://api.github.com/users/tushar-aggarwalinseec')
                print(response.json())
                
            """
        )
        
        
       
        
        st.markdown(
            """
            ##### To handle or disable redirects in requests:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', allow_redirects=False)
            print(response.status_code)
            """
        )
        
        
        
        
        st.markdown(
            """
            ##### To stream a large response to process it in chunks, rather than loading it all into memory:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', stream=True)
            for chunk in response.iter_content(chunk_size=1024):
                process_chunk(chunk) #replace 'process' with your own function
            """
        )
        
        
       
        
        st.markdown(
            """
            ##### To send data to an API endpoint using a POST request with a JSON payload:
            """
        )
        st.code(
            """
            import requests
            payload = {'key1': 'value1', 'key2': 'value2'}
            headers = {'Content-type': 'application/json'}
            response = requests.post('https://httpbin.org/post', data=json.dumps(payload), headers=headers)
            print(response.json())
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        
        
        st.markdown(
            """
            ##### To handle the response encoding properly:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            response.encoding = 'utf-8'
            data = response.text
            print(data)          
            """
        )
        
        
       
        st.markdown(
            """
            ##### To use a session object for making multiple requests to the same host, whichcan improve performance:
            """
        )
        st.code(
            """
            import requests
            with requests.Session() as session:
                session.headers.update({'Authorization': 'YOUR_API_KEY'})
                response = session.get('https://api.github.com/users/tushar-aggarwalinseec')
                print(response.json())
                
            """
        )
        
        
        
        
        st.markdown(
            """
            ##### To handle or disable redirects in requests:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', allow_redirects=False)
            print(response.status_code)
            """
        )
        
        
        

        
        st.markdown(
            """
            ##### To stream a large response to process it in chunks, rather than loading it all into memory:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', stream=True)
            for chunk in response.iter_content(chunk_size=1024):
                process_chunk(chunk) #replace 'process' with your own function
            """
        )
        
        
        
        
        
        
        st.markdown(
            """
            ##### To send data to an API endpoint using a POST request with a JSON payload:
            """
        )
        st.code(
            """
            import requests
            payload = {'key1': 'value1', 'key2': 'value2'}
            headers = {'Content-type': 'application/json'}
            response = requests.post('https://httpbin.org/post', data=json.dumps(payload), headers=headers)
            print(response.json())
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        
        
        st.markdown(
            """
            ##### To handle the response encoding properly:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            response.encoding = 'utf-8'
            data = response.text
            print(data)          
            """
        )
        
        
        
        
        
        st.markdown(
            """
            ##### To use a session object for making multiple requests to the same host, whichcan improve performance:
            """
        )
        st.code(
            """
            import requests
            with requests.Session() as session:
                session.headers.update({'Authorization': 'YOUR_API_KEY'})
                response = session.get('https://api.github.com/users/tushar-aggarwalinseec')
                print(response.json())
                
            """
        )
        
        
        
        
        st.markdown(
            """
            ##### To handle or disable redirects in requests:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', allow_redirects=False)
            print(response.status_code)
            """
        )
        
        
        
    
        
        st.markdown(
            """
            ##### To stream a large response to process it in chunks, rather than loading it all into memory:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', stream=True)
            for chunk in response.iter_content(chunk_size=1024):
                process_chunk(chunk) #replace 'process' with your own function
            """
        )
        
        
        
        
        
        st.markdown(
            """
            ##### To send data to an API endpoint using a POST request with a JSON payload:
            """
        )
        st.code(
            """
            import requests
            payload = {'key1': 'value1', 'key2': 'value2'}
            headers = {'Content-type': 'application/json'}
            response = requests.post('https://httpbin.org/post', data=json.dumps(payload), headers=headers)
            print(response.json())
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        
        
        st.markdown(
            """
            ##### To handle the response encoding properly:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            response.encoding = 'utf-8'
            data = response.text
            print(data)          
            """
        )
        
        
        
        
        st.markdown(
            """
            ##### To use a session object for making multiple requests to the same host, whichcan improve performance:
            """
        )
        st.code(
            """
            import requests
            with requests.Session() as session:
                session.headers.update({'Authorization': 'YOUR_API_KEY'})
                response = session.get('https://api.github.com/users/tushar-aggarwalinseec')
                print(response.json())
                
            """
        )
        
        
        
        
        st.markdown(
            """
            ##### To handle or disable redirects in requests:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', allow_redirects=False)
            print(response.status_code)
            """
        )
        
        
        
        
        
        st.markdown(
            """
            ##### To stream a large response to process it in chunks, rather than loading it all into memory:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', stream=True)
            for chunk in response.iter_content(chunk_size=1024):
                process_chunk(chunk) #replace 'process' with your own function
            """
        )
        
        
    
        
        st.markdown(
            """
            ##### To send data to an API endpoint using a POST request with a JSON payload:
            """
        )
        st.code(
            """
            import requests
            payload = {'key1': 'value1', 'key2': 'value2'}
            headers = {'Content-type': 'application/json'}
            response = requests.post('https://httpbin.org/post', data=json.dumps(payload), headers=headers)
            print(response.json())
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        
        st.markdown(
            """
            ##### To handle the response encoding properly:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec')
            response.encoding = 'utf-8'
            data = response.text
            print(data)          
            """
        )
        
        
    
        
        st.markdown(
            """
            ##### To use a session object for making multiple requests to the same host, whichcan improve performance:
            """
        )
        st.code(
            """
            import requests
            with requests.Session() as session:
                session.headers.update({'Authorization': 'YOUR_API_KEY'})
                response = session.get('https://api.github.com/users/tushar-aggarwalinseec')
                print(response.json())
                
            """
        )
        
        
        
        st.markdown(
            """
            ##### To handle or disable redirects in requests:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', allow_redirects=False)
            print(response.status_code)
            """
        )
        
        
        
        
        st.markdown(
            """
            ##### To stream a large response to process it in chunks, rather than loading it all into memory:
            """
        )
        st.code(
            """
            import requests
            response = requests.get('https://api.github.com/users/tushar-aggarwalinseec', stream=True)
            for chunk in response.iter_content(chunk_size=1024):
                process_chunk(chunk) #replace 'process' with your own function
            """
        )
    


















