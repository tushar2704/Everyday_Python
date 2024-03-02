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





def os():
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
























