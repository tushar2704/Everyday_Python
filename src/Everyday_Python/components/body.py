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
    st.header("Working With Dictionaries")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("1) Creating a Dictionary")
        
        st.markdown(
            """
            ##### To forge a new dictionary:
            """
        )
        st.code(
            """
            # A tome of elements and their symbols
            elements = {'Hydrogen': 'H', 'Helium': 'He', 'Lithium': 'Li'}
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("2. Adding or Updating Entries")
        
        st.markdown(
            """
            ##### To add a new entry or update an existing one:
            """
        )
        st.code(
            """
            elements['Carbon'] = 'C'  # Adds 'Carbon' or updates its value to 'C'
            """
        )
        
        
        
        
        st.subheader("3. Removing an Entry")
        
        st.markdown(
            """
            ##### To banish an entry from the dictionary:
            """
        )
        st.code(
            """
            del elements['Lithium']  # Removes the key 'Lithium' and its value
            """
        )
        
        
        st.subheader("4. Checking for Key Existence")
        
        st.markdown(
            """
            ##### To check if a key resides within the dictionary:
            """
        )
        st.code(
            """
            if 'Helium' in elements:
                print('Helium is present')
            """
        )
        
        
        
        st.subheader("5. Iterating Over Keys")
        
        st.markdown(
            """
            ##### To iterate over the keys in the dictionary:
            """
        )
        st.code(
            """
            for element in elements:
                print(element)  # Prints each key
            """
        )
            
        
    with col2:
        st.subheader("6. Iterating Over Values")
        
        st.markdown(
            """
            ##### To traverse through the values in the dictionary:
            """
        )
        st.code(
            """
            for symbol in elements.values():
                print(symbol)  # Prints each value
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("7. Iterating Over Items")
        
        st.markdown(
            """
            ##### To journey through both keys and values together:
            """
        )
        st.code(
            """
            for element, symbol in elements.items():
                print(f'{element}: {symbol}')        
            """
        )
        
        
        
        
        st.subheader("8. Dictionary Comprehension")
        
        st.markdown(
            """
            ##### To conjure a new dictionary through an incantation over an iterable:
            """
        )
        st.code(
            """
            # Squares of numbers from 0 to 4
            squares = {x: x**2 for x in range(5)}
            print(squares)
            """
        )
        
        
        st.subheader("9. Merging Dictionaries")
        
        st.markdown(
            """
            ##### To merge two or more dictionaries, forming a new alliance of their entries:
            """
        )
        st.code(
            """
            alchemists = {'Paracelsus': 'Mercury'}
            philosophers = {'Plato': 'Aether'}
            merged = {**alchemists, **philosophers}
            """
        )
        
        
        
        st.subheader("10. Getting a Value with Default")
        
        st.markdown(
            """
            ##### To retrieve a value safely, providing a default for absent keys:
            """
        )
        st.code(
            """
            element = elements.get('Neon', 'Unknown')  # Returns 'Unknown' if 'Neon' is not found
            """
        )





def os_():
    st.header("Working With The Operating System")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("1. Navigating File Paths")
        
        st.markdown(
            """
            ##### To craft and dissect paths, ensuring compatibility across realms (operating systems):
            """
        )
        st.code(
            """
            import os
            # Craft a path compatible with the underlying OS
            path = os.path.join('mystic', 'forest', 'artifact.txt')
            # Retrieve the tome's directory
            directory = os.path.dirname(path)
            # Unveil the artifact's name
            artifact_name = os.path.basename(path)
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("2. Listing Directory Contents")
        
        st.markdown(
            """
            ##### To reveal all entities within a mystical directory:
            """
        )
        st.code(
            """
            import os
            contents = os.listdir('enchanted_grove')
            print(contents)
            """
        )
        
        
        
        
        st.subheader("3. Creating Directories")
        
        st.markdown(
            """
            ##### To conjure new directories within the fabric of the filesystem:
            """
        )
        st.code(
            """
            import os
            # create a single directory
            os.mkdir('alchemy_lab')
            # create a hierarchy of directories
            os.makedirs('alchemy_lab/potions/elixirs')
            """
        )
        
        
        st.subheader("4. Removing Files and Directories")
        
        st.markdown(
            """
            ##### To erase files or directories, banishing their essence:
            """
        )
        st.code(
            """
            import os
            # remove a file
            os.remove('unnecessary_scroll.txt')
            # remove an empty directory
            os.rmdir('abandoned_hut')
            # remove a directory and its contents
            import shutil
            shutil.rmtree('cursed_cavern')
            """
        )
        
        
        
        st.subheader("5. Executing Shell Commands")
        
        st.markdown(
            """
            ##### To invoke the shell’s ancient powers directly from Python:
            """
        )
        st.code(
            """
            import subprocess
            # Invoke the 'echo' incantation
            result = subprocess.run(['echo', 'Revealing the arcane'], capture_output=True, text=True)
            print(result.stdout)
            """
        )
            
        
    with col2:
        st.subheader("6. Working with Environment Variables")
        
        st.markdown(
            """
            ##### To read and inscribe upon the ethereal environment variables:
            """
        )
        st.code(
            """
            import os
            # Read the 'PATH' variable
            path = os.environ.get('PATH')
            # Create a new environment variable
            os.environ['MAGIC'] = 'Arcane'
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("7. Changing the Current Working Directory")
        
        st.markdown(
            """
            ##### To shift your presence to another directory within the filesystem:
            """
        )
        st.code(
            """
            import os
            # Traverse to the 'arcane_library' directory
            os.chdir('arcane_library')         
            """
        )
        
        
        
        
        st.subheader("8. Path Existence and Type")
        
        st.markdown(
            """
            ##### To discern the existence of paths and their nature — be they file or directory:
            """
        )
        st.code(
            """
            import os
            # Check if a path exists
            exists = os.path.exists('mysterious_ruins')
            # Ascertain if the path is a directory
            is_directory = os.path.isdir('mysterious_ruins')
            # Determine if the path is a file
            is_file = os.path.isfile('ancient_manuscript.txt')
            """
        )
        
        
        st.subheader("9. Working with Temporary Files")
        
        st.markdown(
            """
            ##### To summon temporary files and directories, fleeting and ephemeral:
            """
        )
        st.code(
            """
            import tempfile
            # Create a temporary file
            temp_file = tempfile.NamedTemporaryFile(delete=False)
            print(temp_file.name)
            # Erect a temporary directory
            temp_dir = tempfile.TemporaryDirectory()
            print(temp_dir.name)
            """
        )
        
        
        
        st.subheader("10. Getting System Information")
        
        st.markdown(
            """
            ##### To unveil information about the host system, its name, and the enchantments it supports:
            """
        )
        st.code(
            """
            import os
            import platform
            # Discover the operating system
            os_name = os.name  # 'posix', 'nt', 'java'
            # Unearth detailed system information
            system_info = platform.system()  # 'Linux', 'Windows', 'Darwin'
            """
        )





def cli():
    st.header("Working With CLI — STDIN, STDOUT, STDERR")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("1. Reading User Input")
        
        st.markdown(
            """
            ##### Getting input from STDIN:
            """
        )
        st.code(
            """
            user_input = input("Impart your wisdom: ")
            print(f"You shared: {user_input}")
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("2. Printing to STDOUT")
        
        st.markdown(
            """
            ##### To print messages to the console:
            """
        )
        st.code(
            """
            print("Behold, the message of the ancients!")
            """
        )
        
        
        
        
        st.subheader("3. Formatted Printing")
        
        st.markdown(
            """
            ##### To weave variables into your messages with grace and precision:
            """
        )
        st.code(
            """
            name = "Merlin"
            age = 300
            print(f"{name}, of {age} years, speaks of forgotten lore.")
            """
        )
        
        
        st.subheader("4. Reading Lines from STDIN")
        
        st.markdown(
            """
            ##### Trim whitespaces line by line from STDIN:
            """
        )
        st.code(
            """
            import sys
            for line in sys.stdin:
                print(f"Echo from the void: {line.strip()}")
            """
        )
        
        
        
        st.subheader("5. Writing to STDERR")
        
        st.markdown(
            """
            ##### To send message to STDERR:
            """
        )
        st.code(
            """
            import sys
            sys.stderr.write("Beware! The path is fraught with peril.\n")
            """
        )
            
        
    with col2:
        st.subheader("6. Redirecting STDOUT")
        
        st.markdown(
            """
            ##### To redirect the STDOUT:
            """
        )
        st.code(
            """
            import sys
            original_stdout = sys.stdout  # Preserve the original STDOUT
            with open('mystic_log.txt', 'w') as f:
                sys.stdout = f  # Redirect STDOUT to a file
                print("This message is inscribed within the mystic_log.txt.")
            sys.stdout = original_stdout  # Restore STDOUT to its original glory
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("7. Redirecting STDERR")
        
        st.markdown(
            """
            ##### Redirecting STDERR:
            """
        )
        st.code(
            """
            import sys
            with open('warnings.txt', 'w') as f:
                sys.stderr = f  # Redirect STDERR
                print("This warning is sealed within warnings.txt.", file=sys.stderr)         
            """
        )
        
        
        
        
        st.subheader("8. Prompting for Passwords")
        
        st.markdown(
            """
            ##### To prompt for passwords:
            """
        )
        st.code(
            """
            import getpass
            secret_spell = getpass.getpass("Whisper the secret spell: ")
            """
        )
        
        
        st.subheader("9. Command Line Arguments")
        
        st.markdown(
            """
            ##### Working with and parsing command line arguments:
            """
        )
        st.code(
            """
            import sys
            # The script's name is the first argument, followed by those passed by the invoker
            script, first_arg, second_arg = sys.argv
            print(f"Invoked with the sacred tokens: {first_arg} and {second_arg}")
            """
        )
        
        
        
        st.subheader("10. Using Argparse for Complex CLI Interactions")
        
        st.markdown(
            """
            ##### Adding descriptions and options/arguments:
            """
        )
        st.code(
            """
            import argparse
            parser = argparse.ArgumentParser(description="Invoke the ancient scripts.")
            parser.add_argument('spell', help="The spell to cast")
            parser.add_argument('--power', type=int, help="The power level of the spell")
            args = parser.parse_args()
            print(f"Casting {args.spell} with power {args.power}")
            """
        )





def math():
    st.header("Working With Mathematical Operations and Permutations")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("1. Basic Arithmetic Operations")
        
        st.markdown(
            """
            ##### To perform basic arithmetic:
            """
        )
        st.code(
            """
            sum = 7 + 3  # Addition
            difference = 7 - 3  # Subtraction
            product = 7 * 3  # Multiplication
            quotient = 7 / 3  # Division
            remainder = 7 % 3  # Modulus (Remainder)
            power = 7 ** 3  # Exponentiation
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("2. Working with Complex Numbers")
        
        st.markdown(
            """
            ##### To work with complex numbers:
            """
        )
        st.code(
            """
            z = complex(2, 3)  # Create a complex number 2 + 3j
            real_part = z.real  # Retrieve the real part
            imaginary_part = z.imag  # Retrieve the imaginary part
            conjugate = z.conjugate()  # Get the conjugate
            """
        )
        
        
        
        
        st.subheader("3. Mathematical Functions")
        
        st.markdown(
            """
            ##### Common math functions:
            """
        )
        st.code(
            """
            import math
            root = math.sqrt(16)  # Square root
            logarithm = math.log(100, 10)  # Logarithm base 10 of 100
            sine = math.sin(math.pi / 2)  # Sine of 90 degrees (in radians)
            """
        )
        
        
        st.subheader("4. Generating Permutations")
        
        st.markdown(
            """
            ##### Easy way to generate permutations from a given set:
            """
        )
        st.code(
            """
            from itertools import permutations
            paths = permutations([1, 2, 3])  # Generate all permutations of the list [1, 2, 3]
            for path in paths:
                print(path)
            """
        )
        
        
        
        st.subheader("5. Generating Combinations")
        
        st.markdown(
            """
            ##### Easy way to generate combinations:
            """
        )
        st.code(
            """
            from itertools import combinations
            combos = combinations([1, 2, 3, 4], 2)  # Generate all 2-element combinations
            for combo in combos:
                print(combo)
            """
        )
            
        
    with col2:
        st.subheader("6. Random Number Generation")
        
        st.markdown(
            """
            ##### To get a random number:
            """
        )
        st.code(
            """
            import random
            num = random.randint(1, 100)  # Generate a random integer between 1 and 100
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("7. Working with Fractions")
        
        st.markdown(
            """
            ##### When you need to work with fractions:
            """
        )
        st.code(
            """
            from fractions import Fraction
            f = Fraction(3, 4)  # Create a fraction 3/4
            print(f + 1)  # Add a fraction and an integer          
            """
        )
        
        
        
        
        st.subheader("8. Statistical Functions")
        
        st.markdown(
            """
            ##### To get Average, Median, and Standard Deviation:
            """
        )
        st.code(
            """
            import statistics
            data = [1, 2, 3, 4, 5]
            mean = statistics.mean(data)  # Average
            median = statistics.median(data)  # Median
            stdev = statistics.stdev(data)  # Standard Deviation
            """
        )
        
        
        st.subheader("9. Trigonometric Functions")
        
        st.markdown(
            """
            ##### To work with trigonometry:
            """
        )
        st.code(
            """
            import math
            angle_rad = math.radians(60)  # Convert 60 degrees to radians
            cosine = math.cos(angle_rad)  # Cosine of the angle
            """
        )
        
        
        
        st.subheader("10. Handling Infinity and NaN")
        
        st.markdown(
            """
            ##### To work with Infinity and NaN:
            """
        )
        st.code(
            """
            import math
            infinity = math.inf  # Representing infinity
            not_a_number = math.nan  # Representing a non-number (NaN)
            """
        )








def databases():
    st.header("Working With Databases")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("1. Establishing a Connection")
        
        st.markdown(
            """
            ##### To create a connection to a Postgres Database:
            """
        )
        st.code(
            """
            import psycopg2
            connection = psycopg2.connect(
                dbname='your_database',
                user='your_username',
                password='your_password',
                host='your_host'
            )
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("2. Creating a Cursor")
        
        st.markdown(
            """
            ##### To create a database cursor, enabling the traversal and manipulation of records:
            """
        )
        st.code(
            """
            cursor = connection.cursor()
            """
        )
        
        
        
        
        st.subheader("3. Executing a Query")
        
        st.markdown(
            """
            ##### Selecting data from Database:
            """
        )
        st.code(
            """
            cursor.execute("SELECT * FROM your_table")
            """
        )
        
        
        st.subheader("4. Fetching Query Results")
        
        st.markdown(
            """
            ##### Fetching data with a cursor:
            """
        )
        st.code(
            """
            records = cursor.fetchall()
            for record in records:
                print(record)
            """
        )
        
        
        
        st.subheader("5. Inserting Records")
        
        st.markdown(
            """
            ##### To insert data into tables in a database:
            """
        )
        st.code(
            """
            cursor.execute("INSERT INTO your_table (column1, column2) VALUES (%s, %s)", ('value1', 'value2'))
            connection.commit()  # Seal the transaction
            """
        )
            
        
    with col2:
        st.subheader("6. Updating Records")
        
        st.markdown(
            """
            ##### To alter the records:
            """
        )
        st.code(
            """
            cursor.execute("UPDATE your_table SET column1 = %s WHERE column2 = %s", ('new_value', 'condition_value'))
            connection.commit()
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("7. Deleting Records")
        
        st.markdown(
            """
            ##### To delete records from the table:
            """
        )
        st.code(
            """
            cursor.execute("DELETE FROM your_table WHERE condition_column = %s", ('condition_value',))
            connection.commit()          
            """
        )
        
        
        
        
        st.subheader("8. Creating a Table")
        
        st.markdown(
            """
            ##### To create a new table, defining its structure:
            """
        )
        st.code(
            """
            cursor.execute("
                        CREATE TABLE your_new_table (
                            id SERIAL PRIMARY KEY,
                            column1 VARCHAR(255),
                            column2 INTEGER
                        )
                    ")
            connection.commit()
            """
        )
        
        
        st.subheader("9. Dropping a Table")
        
        st.markdown(
            """
            ##### To drop a table:
            """
        )
        st.code(
            """
            cursor.execute("DROP TABLE if exists your_table")
            connection.commit()
            """
        )
        
        
        
        st.subheader("10. Using Transactions")
        
        st.markdown(
            """
            ##### To use transactions for atomicity:
            """
        )
        st.code(
            """
            try:
                cursor.execute("your first transactional query")
                cursor.execute("your second transactional query")
                connection.commit()  # Commit if all is well
            except Exception as e:
                connection.rollback()  # Rollback in case of any issue
                print(f"An error occurred: {e}")
            """
        )






def async_():
    st.header("Working With Async IO (Asyncrounous Programming)")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("1. Defining an Asynchronous Function")
        
        st.markdown(
            """
            ##### To declare an async function:
            """
        )
        st.code(
            """
            import asyncio
            async def fetch_data():
                print("Fetching data...")
                await asyncio.sleep(2)  # Simulate an I/O operation
                print("Data retrieved.")
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("2. Running an Asynchronous Function")
        
        st.markdown(
            """
            ##### To invoke an asynchronous function and await them:
            """
        )
        st.code(
            """
            async def main():
                await fetch_data()
            asyncio.run(main())
            """
        )
        
        
        
        
        st.subheader("3. Awaiting Multiple Coroutines")
        
        st.markdown(
            """
            ##### To invoke multiple async functions and await all:
            """
        )
        st.code(
            """
            async def main():
                task1 = fetch_data()
                task2 = fetch_data()
                await asyncio.gather(task1, task2)
            asyncio.run(main())
            """
        )
        
        
        st.subheader("4. Creating Tasks")
        
        st.markdown(
            """
            ##### To dispatch tasks:
            """
        )
        st.code(
            """
            async def main():
                task1 = asyncio.create_task(fetch_data())
                task2 = asyncio.create_task(fetch_data())
                await task1
                await task2
            asyncio.run(main())
            """
        )
        
        
        
        st.subheader("5. Asynchronous Iteration")
        
        st.markdown(
            """
            ##### To traverse through asynchronously, allowing time for other functions in between:
            """
        )
        st.code(
            """
            async def fetch_item(item):
                await asyncio.sleep(1)  # Simulate an I/O operation
                print(f"Fetched {item}")
            async def main():
                items = ['potion', 'scroll', 'wand']
                for item in items:
                    await fetch_item(item)
            asyncio.run(main())
            """
        )
            
        
    with col2:
        st.subheader("6. Using Asynchronous Context Managers")
        
        st.markdown(
            """
            ##### To ensure resources are managed within the bounds of an asynchronous function:
            """
        )
        st.code(
            """
            async def async_context_manager():
                print("Entering context")
                await asyncio.sleep(1)
                print("Exiting context")
            async def main():
                async with async_context_manager():
                    print("Within context")
            asyncio.run(main())
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("7. Handling Exceptions in Asynchronous Code")
        
        st.markdown(
            """
            ##### To gracefully catch and manage the errors with async functions:
            """
        )
        st.code(
            """
            async def risky_spell():
                await asyncio.sleep(1)
                raise ValueError("The spell backfired!")
            async def main():
                try:
                    await risky_spell()
                except ValueError as e:
                    print(f"Caught an error: {e}")
            asyncio.run(main())          
            """
        )
        
        
        
        
        st.subheader("8. Asynchronous Generators")
        
        st.markdown(
            """
            ##### To create async generators, each arriving in its own time:
            """
        )
        st.code(
            """
            async def fetch_items():
                items = ['crystal', 'amulet', 'dagger']
                for item in items:
                    await asyncio.sleep(1)
                    yield item
            async def main():
                async for item in fetch_items():
                    print(f"Found {item}")
            asyncio.run(main())
            """
        )
        
        
        st.subheader("9. Using Semaphores")
        
        st.markdown(
            """
            ##### To limit the number of concurrent tasks:
            """
        )
        st.code(
            """
            async def guarded_spell(semaphore, item):
                async with semaphore:
                    print(f"Processing {item}")
                    await asyncio.sleep(1)
            async def main():
                semaphore = asyncio.Semaphore(2)  # Allow 2 concurrent tasks
                await asyncio.gather(*(guarded_spell(semaphore, i) for i in range(5)))
            asyncio.run(main())
            """
        )
        
        
        
        st.subheader("10. Event Loops")
        
        st.markdown(
            """
            ##### To directly engage with the asynchronous loop, customizing the flow of execution:
            """
        )
        st.code(
            """
            async def perform_spell():
                print("Casting spell...")
                await asyncio.sleep(1)
                print("Spell cast.")
            loop = asyncio.get_event_loop()
            try:
                loop.run_until_complete(perform_spell())
            finally:
                loop.close()
            """
        )






def network():
    st.header("Working With Networks, Sockets, and Network Interfaces")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("1. Creating a Socket")
        
        st.markdown(
            """
            ##### To create a socket for network communication:
            """
        )
        st.code(
            """
            import socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("2. Connecting to a Remote Server")
        
        st.markdown(
            """
            ##### To establish a link with a remote server through the socket:
            """
        )
        st.code(
            """
            s.connect(('example.com', 80))  # Connect to example.com on port 80
            """
        )
        
        
        
        
        st.subheader("3. Sending Data")
        
        st.markdown(
            """
            ##### To dispatch data through the network to a connected entity:
            """
        )
        st.code(
            """
            s.sendall(b'Hello, server')
            """
        )
        
        
        st.subheader("4. Receiving Data")
        
        st.markdown(
            """
            ##### To receive data from the network:
            """
        )
        st.code(
            """
            data = s.recv(1024)  # Receive up to 1024 bytes
            print('Received', repr(data))
            """
        )
        
        
        
        st.subheader("5. Closing a Socket")
        
        st.markdown(
            """
            ##### To gracefully close the socket, severing the network link:
            """
        )
        st.code(
            """
            s.close()
            """
        )
            
        
    with col2:
        st.subheader("6. Creating a Listening Socket")
        
        st.markdown(
            """
            ##### To open a socket that listens for incoming connections:
            """
        )
        st.code(
            """
            serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            serversocket.bind(('localhost', 8080))  # Bind to localhost on port 8080
            serversocket.listen()  # Listen for incoming connections
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("7. Accepting Connections")
        
        st.markdown(
            """
            ##### To accept and establish a network link:
            """
        )
        st.code(
            """
            clientsocket, address = serversocket.accept()
            print(f"Connection from {address} has been established.")       
            """
        )
        
        
        
        
        st.subheader("8. Non-blocking Socket Operations")
        
        st.markdown(
            """
            ##### To set a socket’s mode to non-blocking:
            """
        )
        st.code(
            """
            s.setblocking(False)
            """
        )
        
        
        st.subheader("9. Working with UDP Sockets")
        
        st.markdown(
            """
            ##### To create a socket for UDP, a protocol for quicker, but less reliable communication:
            """
        )
        st.code(
            """
            udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            udp_socket.bind(('localhost', 8081))  # Bind UDP socket to localhost on port 8081
            """
        )
        
        
        
        st.subheader("10. Enumerating Network Interfaces")
        
        st.markdown(
            """
            ##### To discover the names and addresses of the machine’s network interfaces:
            """
        )
        st.code(
            """
            import socket
            import netifaces
            for interface in netifaces.interfaces():
                addr = netifaces.ifaddresses(interface).get(netifaces.AF_INET)
                if addr:
                    print(f"Interface: {interface}, Address: {addr[0]['addr']}")
            """
        )





def df_():
    st.header("Working With Pandas Library (Dataframes)")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("1. Creating a DataFrame")
        
        st.markdown(
            """
            ##### To create a DataFrame with your own columns and data:
            """
        )
        st.code(
            """
            import pandas as pd
            data = {
                'Element': ['Earth', 'Water', 'Fire', 'Air'],
                'Symbol': ['🜃', '🜄', '🜂', '🜁']
            }
            df = pd.DataFrame(data)
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("2. Reading Data from a CSV File")
        
        st.markdown(
            """
            ##### To read data from a CSV file, transforming it into a DataFrame:
            """
        )
        st.code(
            """
            df = pd.read_csv('elements.csv')
            """
        )
        
        
        
        
        st.subheader("3. Inspecting the First Few Rows")
        
        st.markdown(
            """
            ##### To get first rows from dataframe:
            """
        )
        st.code(
            """
            print(df.head())
            """
        )
        
        
        st.subheader("4. Selecting Columns")
        
        st.markdown(
            """
            ##### To select specific columns from dataframe:
            """
        )
        st.code(
            """
            symbols = df['Symbol']
            """
        )
        
        
        
        st.subheader("5. Filtering Rows")
        
        st.markdown(
            """
            ##### To sift through the DataFrame, selecting rows that meet your criteria:
            """
        )
        st.code(
            """
            fire_elements = df[df['Element'] == 'Fire']
            """
        )
            
        
    with col2:
        st.subheader("6. Creating New Columns")
        
        st.markdown(
            """
            ##### To create new columns in DataFrame derived from the data within:
            """
        )
        st.code(
            """
            df['Length'] = df['Element'].apply(len)
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("7. Grouping and Aggregating Data")
        
        st.markdown(
            """
            ##### To gather your data into groups and extract new data through aggregation:
            """
        )
        st.code(
            """
            element_groups = df.groupby('Element').agg({'Length': 'mean'})          
            """
        )
        
        
        
        
        st.subheader("8. Merging DataFrames")
        
        st.markdown(
            """
            ##### To weave together two DataFrames, joining them by a shared key:
            """
        )
        st.code(
            """
            df2 = pd.DataFrame({'Element': ['Earth', 'Fire'], 'Quality': ['Solid', 'Plasma']})
            merged_df = pd.merge(df, df2, on='Element')
            """
        )
        
        
        st.subheader("9. Handling Missing Data")
        
        st.markdown(
            """
            ##### To clean your DataFrame, filling the voids where data is absent:
            """
        )
        st.code(
            """
            df.fillna(value='Unknown', inplace=True)
            """
        )
        
        
        
        st.subheader("10. Pivoting and Reshaping Data")
        
        st.markdown(
            """
            ##### To transmute the shape of your DataFrame, revealing hidden patterns and structures with a pivot operation:
            """
        )
        st.code(
            """
            pivoted_df = df.pivot(index='Element', columns='Symbol', values='Length')
            """
        )





def numpy_():
    st.header("Working With Numpy Library (Arrays)")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("1. Creating a NumPy Array")
        
        st.markdown(
            """
            ##### To create an array:
            """
        )
        st.code(
            """
            import numpy as np
            array = np.array([1, 2, 3, 4, 5])
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("2. Array of Zeros or Ones")
        
        st.markdown(
            """
            ##### To create an array filled with zeros:
            """
        )
        st.code(
            """
            zeros = np.zeros((3, 3))  # A 3x3 array of zeros
            ones = np.ones((2, 4))  # A 2x4 array of ones
            """
        )
        
        
        
        
        st.subheader("3. Creating a Range of Numbers")
        
        st.markdown(
            """
            ##### To create a sequence of numbers:
            """
        )
        st.code(
            """
            range_array = np.arange(10, 50, 5)  # From 10 to 50, step by 5
            """
        )
        
        
        st.subheader("4. Creating a Linearly Spaced Array")
        
        st.markdown(
            """
            ##### To create a series of values, evenly spaced between two bounds:
            """
        )
        st.code(
            """
            linear_spaced = np.linspace(0, 1, 5)  # 5 values from 0 to 1
            """
        )
        
        
        
        st.subheader("5. Reshaping an Array")
        
        st.markdown(
            """
            ##### To transmute the shape of an array, altering its dimensions:
            """
        )
        st.code(
            """
            reshaped = np.arange(9).reshape(3, 3)  # Reshape a 1D array into a 3x3 2D array
            """
        )
            
        
    with col2:
        st.subheader("6. Basic Array Operations")
        
        st.markdown(
            """
            ##### To perform elemental manipulations upon the arrays:
            """
        )
        st.code(
            """
            a = np.array([1, 2, 3])
            b = np.array([4, 5, 6])
            sum = a + b  # Element-wise addition
            difference = b - a  # Element-wise subtraction
            product = a * b  # Element-wise multiplication
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("7. Matrix Multiplication")
        
        st.markdown(
            """
            ##### Basic dot product Operation:
            """
        )
        st.code(
            """
            result = np.dot(a.reshape(1, 3), b.reshape(3, 1))  # Dot product of a and b          
            """
        )
        
        
        
        
        st.subheader("8. Accessing Array Elements")
        
        st.markdown(
            """
            ##### Accessing array elements with useful syntax:
            """
        )
        st.code(
            """
            element = a[2]  # Retrieve the third element of array 'a'
            row = reshaped[1, :]  # Retrieve the second row of 'reshaped'
            """
        )
        
        
        st.subheader("9. Boolean Indexing")
        
        st.markdown(
            """
            ##### To filter the elements of an array through the sieve of conditionals:
            """
        )
        st.code(
            """
            filtered = a[a > 2]  # Elements of 'a' greater than 2
            """
        )
        
        
        
        st.subheader("10. Aggregations and Statistics")
        
        st.markdown(
            """
            ##### Statistical operations on np arrays:
            """
        )
        st.code(
            """
            mean = np.mean(a)
            maximum = np.max(a)
            sum = np.sum(a)
            """
        )






def plots():
    st.header("Working With Matplotlib Library (Data Visualization)")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("1. Creating a Basic Plot")
        
        st.markdown(
            """
            ##### To create a plot visualization:
            """
        )
        st.code(
            """
            import matplotlib.pyplot as plt
            x = [1, 2, 3, 4, 5]
            y = [1, 4, 9, 16, 25]
            plt.plot(x, y)
            plt.show()
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("2. Adding Titles and Labels")
        
        st.markdown(
            """
            ##### To create names for axes and title your plot to give better context:
            """
        )
        st.code(
            """
            plt.plot(x, y)
            plt.title('Growth Over Time')
            plt.xlabel('Time')
            plt.ylabel('Growth')
            plt.show()
            """
        )
        
        
        
        
        st.subheader("3. Creating a Scatter Plot")
        
        st.markdown(
            """
            ##### Creating a scatter plot:
            """
        )
        st.code(
            """
            plt.scatter(x, y)
            plt.show()
            """
        )
        
        
        st.subheader("4. Customizing Line Styles and Markers")
        
        st.markdown(
            """
            ##### To add symbols into your plot, enriching its usefulness:
            """
        )
        st.code(
            """
            plt.plot(x, y, linestyle='--', marker='o', color='b')
            plt.show()
            """
        )
        
        
        
        st.subheader("5. Creating Multiple Plots on the Same Axes")
        
        st.markdown(
            """
            ##### Creating Multiple Plots on the Same Axes:
            """
        )
        st.code(
            """
            z = [2, 3, 4, 5, 6]
            plt.plot(x, y)
            plt.plot(x, z)
            plt.show()
            """
        )
            
        
    with col2:
        st.subheader("6. Creating Subplots")
        
        st.markdown(
            """
            ##### To create subplots:
            """
        )
        st.code(
            """
            fig, ax = plt.subplots(2, 1)  # 2 rows, 1 column
            ax[0].plot(x, y)
            ax[1].plot(x, z)
            plt.show()
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("7. Creating a Histogram")
        
        st.markdown(
            """
            ##### To create a histogram:
            """
        )
        st.code(
            """
            data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
            plt.hist(data, bins=4)
            plt.show()        
            """
        )
        
        
        
        
        st.subheader("8. Adding a Legend")
        
        st.markdown(
            """
            ##### To create a legend for the plot:
            """
        )
        st.code(
            """
            plt.plot(x, y, label='Growth')
            plt.plot(x, z, label='Decay')
            plt.legend()
            plt.show()
            """
        )
        
        
        st.subheader("9. Customizing Ticks")
        
        st.markdown(
            """
            ##### To create your own marks upon the axes, defining the scale of your values:
            """
        )
        st.code(
            """
            plt.plot(x, y)
            plt.xticks([1, 2, 3, 4, 5], ['One', 'Two', 'Three', 'Four', 'Five'])
            plt.yticks([0, 5, 10, 15, 20, 25], ['0', '5', '10', '15', '20', '25+'])
            plt.show()
            """
        )
        
        
        
        st.subheader("10. Saving Figures")
        
        st.markdown(
            """
            ##### To save the plot as a .png:
            """
        )
        st.code(
            """
            plt.plot(x, y)
            plt.savefig('growth_over_time.png')
            """
        )





def scikit_():
    st.header("Working With Scikit-Learn Library (Machine Learning)")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("1. Loading a Dataset")
        
        st.markdown(
            """
            ##### To work with datasets for your ML experiments
            """
        )
        st.code(
            """
            from sklearn import datasets
            iris = datasets.load_iris()
            X, y = iris.data, iris.target
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("2. Splitting Data into Training and Test Sets")
        
        st.markdown(
            """
            ##### To divide your data, dedicating portions to training and evaluation:
            """
        )
        st.code(
            """
            from sklearn.model_selection import train_test_split
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
            """
        )
        
        
        
        
        st.subheader("3. Training a Model")
        
        st.markdown(
            """
            ##### Training a ML Model using RandomForestClassifier:
            """
        )
        st.code(
            """
            from sklearn.ensemble import RandomForestClassifier
            model = RandomForestClassifier()
            model.fit(X_train, y_train)
            """
        )
        
        
        st.subheader("4. Making Predictions")
        
        st.markdown(
            """
            ##### To access the model predictions:
            """
        )
        st.code(
            """
            predictions = model.predict(X_test)
            """
        )
        
        
        
        st.subheader("5. Evaluating Model Performance")
        
        st.markdown(
            """
            ##### To evaluate your model, measuring its accuracy in prediction:
            """
        )
        st.code(
            """
            from sklearn.metrics import accuracy_score
            accuracy = accuracy_score(y_test, predictions)
            print(f"Model accuracy: {accuracy}")
            """
        )
            
        
    with col2:
        st.subheader("6. Using Cross-Validation")
        
        st.markdown(
            """
            ##### To use Cross-Validation:
            """
        )
        st.code(
            """
            from sklearn.model_selection import cross_val_score
            scores = cross_val_score(model, X, y, cv=5)
            print(f"Cross-validation scores: {scores}")
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("7. Feature Scaling")
        
        st.markdown(
            """
            ##### To create the appropriate scales of your features, allowing the model to learn more effectively:
            """
        )
        st.code(
            """
            from sklearn.preprocessing import StandardScaler
            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train)
            X_test_scaled = scaler.transform(X_test)     
            """
        )
        
        
        
        
        st.subheader("8. Parameter Tuning with Grid Search")
        
        st.markdown(
            """
            ##### To refine your model’s parameters, seeking the optimal combination:
            """
        )
        st.code(
            """
            from sklearn.model_selection import GridSearchCV
            param_grid = {'n_estimators': [10, 50, 100], 'max_depth': [None, 10, 20]}
            grid_search = GridSearchCV(model, param_grid, cv=5)
            grid_search.fit(X_train, y_train)
            """
        )
        
        
        st.subheader("9. Pipeline Creation")
        
        st.markdown(
            """
            ##### To streamline your data processing and modeling steps, crafting a seamless flow:
            """
        )
        st.code(
            """
            from sklearn.pipeline import Pipeline
            pipeline = Pipeline([
                ('scaler', StandardScaler()),
                ('classifier', RandomForestClassifier())
            ])
            pipeline.fit(X_train, y_train)
            """
        )
        
        
        
        st.subheader("10. Saving and Loading a Model")
        
        st.markdown(
            """
            ##### To preserve your model:
            """
        )
        st.code(
            """
            import joblib
            # Saving the model
            joblib.dump(model, 'model.joblib')
            # Loading the model
            loaded_model = joblib.load('model.joblib')
            """
        )





def plotly_():
    st.header("Working With Plotly Library (Interactive Data Visualization)")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("1. Creating a Basic Line Chart")
        
        st.markdown(
            """
            ##### To create a line chart:
            """
        )
        st.code(
            """
            import plotly.graph_objs as go
            import plotly.io as pio
            x = [1, 2, 3, 4, 5]
            y = [1, 4, 9, 16, 25]
            fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines'))
            pio.show(fig)
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("2. Creating a Scatter Plot")
        
        st.markdown(
            """
            ##### To create a scatter plot:
            """
        )
        st.code(
            """
            fig = go.Figure(data=go.Scatter(x=x, y=y, mode='markers'))
            pio.show(fig)
            """
        )
        
        
        
        
        st.subheader("3. Creating a Bar Chart")
        
        st.markdown(
            """
            ##### To Create a Bar Chart:
            """
        )
        st.code(
            """
            categories = ['A', 'B', 'C', 'D', 'E']
            values = [10, 20, 15, 30, 25]
            fig = go.Figure(data=go.Bar(x=categories, y=values))
            pio.show(fig)
            """
        )
        
        
        st.subheader("4. Creating a Pie Chart")
        
        st.markdown(
            """
            ##### To create a Pie Chart:
            """
        )
        st.code(
            """
            labels = ['Earth', 'Water', 'Fire', 'Air']
            sizes = [25, 35, 20, 20]
            fig = go.Figure(data=go.Pie(labels=labels, values=sizes))
            pio.show(fig)
            """
        )
        
        
        
        st.subheader("5. Creating a Histogram")
        
        st.markdown(
            """
            ##### To create a Histogram:
            """
        )
        st.code(
            """
            data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
            fig = go.Figure(data=go.Histogram(x=data))
            pio.show(fig)
            """
        )
            
        
    with col2:
        st.subheader("6. Creating Box Plots")
        
        st.markdown(
            """
            ##### To create a Box Plot:
            """
        )
        st.code(
            """
            data = [1, 2, 2, 3, 4, 4, 4, 5, 5, 6]
            fig = go.Figure(data=go.Box(y=data))
            pio.show(fig)
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("7. Creating Heatmaps")
        
        st.markdown(
            """
            ##### To create a heatmap:
            """
        )
        st.code(
            """
            import numpy as np
            z = np.random.rand(10, 10)  # Generate random data
            fig = go.Figure(data=go.Heatmap(z=z))
            pio.show(fig)         
            """
        )
        
        
        
        
        st.subheader("8. Creating 3D Surface Plots")
        
        st.markdown(
            """
            ##### To create a 3D Surface Plot:
            """
        )
        st.code(
            """
            z = np.random.rand(20, 20)  # Generate random data
            fig = go.Figure(data=go.Surface(z=z))
            pio.show(fig)
            """
        )
        
        
        st.subheader("9. Creating Subplots")
        
        st.markdown(
            """
            ##### To create a subplot:
            """
        )
        st.code(
            """
            from plotly.subplots import make_subplots
            fig = make_subplots(rows=1, cols=2)
            fig.add_trace(go.Scatter(x=x, y=y, mode='lines'), row=1, col=1)
            fig.add_trace(go.Bar(x=categories, y=values), row=1, col=2)
            pio.show(fig)
            """
        )
        
        
        
        st.subheader("10. Creating Interactive Time Series")
        
        st.markdown(
            """
            ##### To work with Time Series:
            """
        )
        st.code(
            """
            import pandas as pd
            dates = pd.date_range('20230101', periods=5)
            values = [10, 11, 12, 13, 14]
            fig = go.Figure(data=go.Scatter(x=dates, y=values, mode='lines+markers'))
            pio.show(fig)
            """
        )





def time_():
    st.header("Working With Dates and Times")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("1. Getting the Current Date and Time")
        
        st.markdown(
            """
            ##### To get the current data and time:
            """
        )
        st.code(
            """
            from datetime import datetime
            now = datetime.now()
            print(f"Current date and time: {now}")
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("2. Creating Specific Date and Time")
        
        st.markdown(
            """
            ##### To conjure a moment from the past or future, crafting it with precision:
            """
        )
        st.code(
            """
            specific_time = datetime(2023, 1, 1, 12, 30)
            print(f"Specific date and time: {specific_time}")
            """
        )
        
        
        
        
        st.subheader("3. Formatting Dates and Times")
        
        st.markdown(
            """
            ##### Formatting Dates and Times:
            """
        )
        st.code(
            """
            formatted = now.strftime("%Y-%m-%d %H:%M:%S")
            print(f"Formatted date and time: {formatted}")
            """
        )
        
        
        st.subheader("4. Parsing Dates and Times from Strings")
        
        st.markdown(
            """
            ##### Parsing Dates and Times from Strings:
            """
        )
        st.code(
            """
            date_string = "2023-01-01 15:00:00"
            parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
            print(f"Parsed date and time: {parsed_date}")
            """
        )
        
        
        
        st.subheader("5. Working with Time Deltas")
        
        st.markdown(
            """
            ##### To traverse the distances between moments, leaping forward or backward through time:
            """
        )
        st.code(
            """
            from datetime import timedelta
            delta = timedelta(days=7)
            future_date = now + delta
            print(f"Date after 7 days: {future_date}")
            """
        )
            
        
    with col2:
        st.subheader("6. Comparing Dates and Times")
        
        st.markdown(
            """
            ##### Date and Times comparisons:
            """
        )
        st.code(
            """
            if specific_time > now:
                print("Specific time is in the future.")
            else:
                print("Specific time has passed.")
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("7. Extracting Components from a Date/Time")
        
        st.markdown(
            """
            ##### To extract dates year, month, day, and more:
            """
        )
        st.code(
            """
            year = now.year
            month = now.month
            day = now.day
            hour = now.hour
            minute = now.minute
            second = now.second
            print(f"Year: {year}, Month: {month}, Day: {day}, Hour: {hour}, Minute: {minute}, Second: {second}")         
            """
        )
        
        
        
        
        st.subheader("8. Working with Time Zones")
        
        st.markdown(
            """
            ##### To work with time zones honoring the local time:
            """
        )
        st.code(
            """
            from datetime import timezone, timedelta
            utc_time = datetime.now(timezone.utc)
            print(f"Current UTC time: {utc_time}")
            # Adjusting to a specific timezone (e.g., EST)
            est_time = utc_time - timedelta(hours=5)
            print(f"Current EST time: {est_time}")
            """
        )
        
        
        st.subheader("9. Getting the Weekday")
        
        st.markdown(
            """
            ##### To identify the day of the week:
            """
        )
        st.code(
            """
            weekday = now.strftime("%A")
            print(f"Today is: {weekday}")
            """
        )
        
        
        
        st.subheader("10. Working with Unix Timestamps")
        
        st.markdown(
            """
            ##### To converse with the ancient epochs, translating their count from the dawn of Unix:
            """
        )
        st.code(
            """
            timestamp = datetime.timestamp(now)
            print(f"Current timestamp: {timestamp}")
            # Converting a timestamp back to a datetime
            date_from_timestamp = datetime.fromtimestamp(timestamp)
            print(f"Date from timestamp: {date_from_timestamp}")
            """
        )






def adv_():
    st.header("Working With More Advanced List Comprehensions and Lambda Functions")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("1. Nested List Comprehensions")
        
        st.markdown(
            """
            ##### To work with nested list Comprehensions:
            """
        )
        st.code(
            """
            matrix = [[j for j in range(5)] for i in range(3)]
            print(matrix)  # Creates a 3x5 matrix
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("2. Conditional List Comprehensions")
        
        st.markdown(
            """
            ##### To filter elements that meet your criteria:
            """
        )
        st.code(
            """
            filtered = [x for x in range(10) if x % 2 == 0]
            print(filtered)  # Even numbers from 0 to 9
            """
        )
        
        
        
        
        st.subheader("3. List Comprehensions with Multiple Iterables")
        
        st.markdown(
            """
            ##### To merge and transform elements from multiple sources in a single dance:
            """
        )
        st.code(
            """
            pairs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
            print(pairs)  # Pairs of non-equal elements
            """
        )
        
        
        st.subheader("4. Using Lambda Functions")
        
        st.markdown(
            """
            ##### To summon anonymous functions, ephemeral and concise, for a single act of magic:
            """
        )
        st.code(
            """
            square = lambda x: x**2
            print(square(5))  # Returns 25
            """
        )
        
        
        
        st.subheader("5. Lambda Functions in List Comprehensionss")
        
        st.markdown(
            """
            ##### To employ lambda functions within your list comprehensions:
            """
        )
        st.code(
            """
            squared = [(lambda x: x**2)(x) for x in range(5)]
            print(squared)  # Squares of numbers from 0 to 4
            """
        )
            
        
    with col2:
        st.subheader("6. List Comprehensions for Flattening Lists")
        
        st.markdown(
            """
            ##### To flatten a nested list, spreading its elements into a single dimension:
            """
        )
        st.code(
            """
            nested = [[1, 2, 3], [4, 5], [6, 7]]
            flattened = [x for sublist in nested for x in sublist]
            print(flattened)
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("7. Applying Functions to Elements")
        
        st.markdown(
            """
            ##### To apply a transformation function to each element:
            """
        )
        st.code(
            """
            import math
            transformed = [math.sqrt(x) for x in range(1, 6)]
            print(transformed)  # Square roots of numbers from 1 to 5  
            """
        )
        
        
        
        
        st.subheader("8. Using Lambda with Map and Filter")
        
        st.markdown(
            """
            ##### To map and filter lists:
            """
        )
        st.code(
            """
            mapped = list(map(lambda x: x**2, range(5)))
            filtered = list(filter(lambda x: x > 5, mapped))
            print(mapped)    # Squares of numbers from 0 to 4
            print(filtered)  # Elements greater than 5
            """
        )
        
        
        st.subheader("9. List Comprehensions with Conditional Expressions")
        
        st.markdown(
            """
            ##### List Comprehensions with Condidtional Expressions:
            """
        )
        st.code(
            """
            conditional = [x if x > 2 else x**2 for x in range(5)]
            print(conditional)  # Squares numbers less than or equal to 2, passes others unchanged
            """
        )
        
        
        
        st.subheader("10. Complex Transformations with Lambda")
        
        st.markdown(
            """
            ##### To conduct intricate transformations, using lambda functions:
            """
        )
        st.code(
            """
            complex_transformation = list(map(lambda x: x**2 if x % 2 == 0 else x + 5, range(5)))
            print(complex_transformation)  # Applies different transformations based on even-odd condition
            """
        )






def oop():
    st.header("Working With Object Oriented Programming")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("1. Defining a Class")
        
        st.markdown(
            """
            ##### Creating a class:
            """
        )
        st.code(
            """
            class Wizard:
                def __init__(self, name, power):
                    self.name = name
                    self.power = power
                def cast_spell(self):
                        print(f"{self.name} casts a spell with power {self.power}!")
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("2. Creating an Instance")
        
        st.markdown(
            """
            ##### To create an instance of your class:
            """
        )
        st.code(
            """
            merlin = Wizard("Merlin", 100)
            """
        )
        
        
        
        
        st.subheader("3. Invoking Methods")
        
        st.markdown(
            """
            ##### To call methods on instance of class:
            """
        )
        st.code(
            """
            merlin.cast_spell()
            """
        )
        
        
        st.subheader("4. Inheritance")
        
        st.markdown(
            """
            ##### Subclassing:
            """
        )
        st.code(
            """
            class ArchWizard(Wizard):
                def __init__(self, name, power, realm):
                    super().__init__(name, power)
                    self.realm = realm
                def summon_familiar(self):
                    print(f"{self.name} summons a familiar from the {self.realm} realm.")
            """
        )
        
        
        
        st.subheader("5. Overriding Methods")
        
        st.markdown(
            """
            ##### To overide base classes:
            """
        )
        st.code(
            """
            class Sorcerer(Wizard):
                def cast_spell(self):
                    print(f"{self.name} casts a powerful dark spell!")
            """
        )
            
        
    with col2:
        st.subheader("6. Polymorphism")
        
        st.markdown(
            """
            ##### To interact with different forms through a common interface:
            """
        )
        st.code(
            """
            def unleash_magic(wizard):
                wizard.cast_spell()
            unleash_magic(merlin)
            unleash_magic(Sorcerer("Voldemort", 90))
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("7. Encapsulation")
        
        st.markdown(
            """
            ##### To use information hiding:
            """
        )
        st.code(
            """
            class Alchemist:
                def __init__(self, secret_ingredient):
                    self.__secret = secret_ingredient
                def reveal_secret(self):
                    print(f"The secret ingredient is {self.__secret}")       
            """
        )
        
        
        
        
        st.subheader("8. Composition")
        
        st.markdown(
            """
            ##### To assemble Objects from simpler ones:
            """
        )
        st.code(
            """
            class Spellbook:
                def __init__(self, spells):
                    self.spells = spells
            class Mage:
                def __init__(self, name, spellbook):
                    self.name = name
                    self.spellbook = spellbook
            """
        )
        
        
        st.subheader("9. Class Methods and Static Methods")
        
        st.markdown(
            """
            ##### To bind actions to the class itself or liberate them from the instance, serving broader purposes:
            """
        )
        st.code(
            """
            class Enchanter:
                @staticmethod
                def enchant(item):
                    print(f"{item} is enchanted!")
                @classmethod
                def summon(cls):
                    print("A new enchanter is summoned.")
            """
        )
        
        
        
        st.subheader("10. Properties and Setters")
        
        st.markdown(
            """
            ##### To elegantly manage access to an entity’s attributes, guiding their use and protection:
            """
        )
        st.code(
            """
            class Elementalist:
                def __init__(self, element):
                    self._element = element
                @property
                def element(self):
                    return self._element
                @element.setter
                    def element(self, value):
                        if value in ["Fire", "Water", "Earth", "Air"]:
                            self._element = value
                        else:
                            print("Invalid element!")
            """
        )






def deco_():
    st.header("Working With Decorators")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("1. Basic Decorator")
        
        st.markdown(
            """
            ##### To create a simple decorator that wraps a function:
            """
        )
        st.code(
            """
            def my_decorator(func):
                def wrapper():
                    print("Something is happening before the function is called.")
                    func()
                    print("Something is happening after the function is called.")
                return wrapper

            @my_decorator
            def say_hello():
                print("Hello!")

            say_hello()
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("2. Decorator with Arguments")
        
        st.markdown(
            """
            ##### To pass arguments to the function within a decorator:
            """
        )
        st.code(
            """
            def my_decorator(func):
                def wrapper(*args, **kwargs):
                    print("Before call")
                    result = func(*args, **kwargs)
                    print("After call")
                    return result
                return wrapper

            @my_decorator
            def greet(name):
                print(f"Hello {name}")

            greet("Alice")
            """
        )
        
        
        
        
        st.subheader("3. Using functools.wraps")
        
        st.markdown(
            """
            ##### To preserve the metadata of the original function when decorating:
            """
        )
        st.code(
            """
            from functools import wraps

            def my_decorator(func):
                @wraps(func)
                def wrapper(*args, **kwargs):
                    """Wrapper function"""
                    return func(*args, **kwargs)
                return wrapper

            @my_decorator
            def greet(name):
                """Greet someone"""
                print(f"Hello {name}")

            print(greet.__name__)  # Outputs: 'greet'
            print(greet.__doc__)   # Outputs: 'Greet someone'
            """
        )
        
        
        st.subheader("4. Class Decorator")
        
        st.markdown(
            """
            ##### To create a decorator using a class:
            """
        )
        st.code(
            """
            class MyDecorator:
                def __init__(self, func):
                    self.func = func
            def __call__(self, *args, **kwargs):
                    print("Before call")
                    self.func(*args, **kwargs)
                    print("After call")

            @MyDecorator
            def greet(name):
                print(f"Hello {name}")

            greet("Alice")
            """
        )
        
        
        
        st.subheader("5. Decorator with Arguments")
        
        st.markdown(
            """
            ##### To create a decorator that accepts its own arguments:
            """
        )
        st.code(
            """
            def repeat(times):
                def decorator(func):
                    @wraps(func)
                    def wrapper(*args, **kwargs):
                        for _ in range(times):
                            func(*args, **kwargs)
                    return wrapper
                return decorator

            @repeat(3)
            def say_hello():
                print("Hello")

            say_hello()
            """
        )
            
        
    with col2:
        st.subheader("6. Method Decorator")
        
        st.markdown(
            """
            ##### To apply a decorator to a method within a class:
            """
        )
        st.code(
            """
            def method_decorator(func):
                @wraps(func)
                def wrapper(self, *args, **kwargs):
                    print("Method Decorator")
                    return func(self, *args, **kwargs)
                return wrapper

            class MyClass:
                @method_decorator
                def greet(self, name):
                    print(f"Hello {name}")

            obj = MyClass()
            obj.greet("Alice")
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("7. Stacking Decorators")
        
        st.markdown(
            """
            ##### To apply multiple decorators to a single function:
            """
        )
        st.code(
            """
            @my_decorator
            @repeat(2)
            def greet(name):
                print(f"Hello {name}")

            greet("Alice")      
            """
        )
        
        
        
        
        st.subheader("8. Decorator with Optional Arguments")
        
        st.markdown(
            """
            ##### Creating a decorator that works with or without arguments:
            """
        )
        st.code(
            """
           def smart_decorator(arg=None):
                def decorator(func):
                    @wraps(func)
                    def wrapper(*args, **kwargs):
                        if arg:
                            print(f"Argument: {arg}")
                        return func(*args, **kwargs)
                    return wrapper
                if callable(arg):
                    return decorator(arg)
                return decorator

            @smart_decorator
            def no_args():
                print("No args")

            @smart_decorator("With args")
            def with_args():
                print("With args")

            no_args()
            with_args()
            """
        )
        
        
        st.subheader("9. Class Method Decorator")
        
        st.markdown(
            """
            ##### To decorate a class method:
            """
        )
        st.code(
            """
            class MyClass:
                @classmethod
                @my_decorator
                def class_method(cls):
                    print("Class method called")

            MyClass.class_method()
            """
        )
        
        
        
        st.subheader("10. Decorator for Static Method")
        
        st.markdown(
            """
            ##### To decorate a static method:
            """
        )
        st.code(
            """
            class MyClass:
                @staticmethod
                @my_decorator
                def static_method():
                    print("Static method called")

            MyClass.static_method()
            """
        )






def graphql():
    st.header("Working With GraphQL")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("1. Setting Up a GraphQL Client")
        
        st.markdown(
            """
            ##### To work with GraphQL:
            """
        )
        st.code(
            """
            from gql import gql, Client
            from gql.transport.requests import RequestsHTTPTransport
            transport = RequestsHTTPTransport(url='https://your-graphql-endpoint.com/graphql')
            client = Client(transport=transport, fetch_schema_from_transport=True)
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("2. Executing a Simple Query")
        
        st.markdown(
            """
            ##### Executing a Query:
            """
        )
        st.code(
            """
            query = gql('''
            {
            allWizards {
                id
                name
                power
            }
            }
            ''')

            result = client.execute(query)
            print(result)
            """
        )
        
        
        
        
        st.subheader("3. Executing a Query with Variables")
        
        st.markdown(
            """
            ##### Query with Variables:
            """
        )
        st.code(
            """
            query = gql('''
            query GetWizards($element: String!) {
            wizards(element: $element) {
                id
                name
            }
            }
            ''')
            params = {"element": "Fire"}
            result = client.execute(query, variable_values=params)
            print(result)
            """
        )
        
        
        st.subheader("4. Mutations")
        
        st.markdown(
            """
            ##### To create and execute a mutation:
            """
        )
        st.code(
            """
            mutation = gql('''
            mutation CreateWizard($name: String!, $element: String!) {
            createWizard(name: $name, element: $element) {
                wizard {
                id
                name
                }
            }
            }
            ''')
            params = {"name": "Gandalf", "element": "Light"}
            result = client.execute(mutation, variable_values=params)
            print(result)
            """
        )
        
        
        
        st.subheader("5. Handling Errors")
        
        st.markdown(
            """
            ##### Error handling:
            """
        )
        st.code(
            """
            from gql import gql, Client
            from gql.transport.exceptions import TransportQueryError
            try:
                result = client.execute(query)
            except TransportQueryError as e:
                print(f"GraphQL Query Error: {e}")
            """
        )
            
        
    with col2:
        st.subheader("6. Subscriptions")
        
        st.markdown(
            """
            ##### Working with Subscriptions:
            """
        )
        st.code(
            """
            subscription = gql('''
            subscription {
            wizardUpdated {
                id
                name
                power
            }
            }
            ''')
            for result in client.subscribe(subscription):
                print(result)
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("7. Fragments")
        
        st.markdown(
            """
            ##### Working with Fragments:
            """
        )
        st.code(
            """
            query = gql('''
            fragment WizardDetails on Wizard {
            name
            power
            }
            query {
            allWizards {
                ...WizardDetails
            }
            }
            ''')
            result = client.execute(query)
            print(result)          
            """
        )
        
        
        
        
        st.subheader("8. Inline Fragments")
        
        st.markdown(
            """
            ##### To tailor the response based on the type of the object returned:
            """
        )
        st.code(
            """
            query = gql('''
            {
            search(text: "magic") {
                __typename
                ... on Wizard {
                name
                power
                }
                ... on Spell {
                name
                effect
                }
            }
            }
            ''')
            result = client.execute(query)
            print(result)
            """
        )
        
        
        st.subheader("9. Using Directives")
        
        st.markdown(
            """
            ##### To dynamically include or skip fields in your queries based on conditions:
            """
        )
        st.code(
            """
            query = gql('''
            query GetWizards($withPower: Boolean!) {
            allWizards {
                name
                power @include(if: $withPower)
            }
            }
            ''')
            params = {"withPower": True}
            result = client.execute(query, variable_values=params)
            print(result)
            """
        )
        
        
        
        st.subheader("10. Batching Requests")
        
        st.markdown(
            """
            ##### To combine multiple operations into a single request, reducing network overhead:
            """
        )
        st.code(
            """
            from gql import gql, Client
            from gql.transport.requests import RequestsHTTPTransport

            transport = RequestsHTTPTransport(url='https://your-graphql-endpoint.com/graphql', use_json=True)
            client = Client(transport=transport, fetch_schema_from_transport=True)

            query1 = gql('query { wizard(id: "1") { name } }')
            query2 = gql('query { allSpells { name } }')

            results = client.execute([query1, query2])
            print(results)
            """
        )





def re_():
    st.header("Working With Regular Expressions")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("1. Basic Pattern Matching")
        
        st.markdown(
            """
            ##### To find a match for a pattern within a string:
            """
        )
        st.code(
            """
            import re
            text = "Search this string for patterns."
            match = re.search(r"patterns", text)
            if match:
                print("Pattern found!")
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("2. Compiling Regular Expressions")
        
        st.markdown(
            """
            ##### To compile a regular expression for repeated use:
            """
        )
        st.code(
            """
            pattern = re.compile(r"patterns")
            match = pattern.search(text)
            """
        )
        
        
        
        
        st.subheader("3. Matching at the Beginning or End")
        
        st.markdown(
            """
            ##### To check if a string starts or ends with a pattern:
            """
        )
        st.code(
            """
            if re.match(r"^Search", text):
                print("Starts with 'Search'")
            if re.search(r"patterns.$", text):
                print("Ends with 'patterns.'")
            """
        )
        
        
        st.subheader("4. Finding All Matches")
        
        st.markdown(
            """
            ##### To find all occurrences of a pattern in a string:
            """
        )
        st.code(
            """
            all_matches = re.findall(r"t\w+", text)  # Finds words starting with 't'
            print(all_matches)
            """
        )
        
        
        
        st.subheader("5. Search and Replace (Substitution)")
        
        st.markdown(
            """
            ##### To replace occurrences of a pattern within a string:
            """
        )
        st.code(
            """
            replaced_text = re.sub(r"string", "sentence", text)
            print(replaced_text)
            """
        )
            
        
    with col2:
        st.subheader("6. Splitting a String")
        
        st.markdown(
            """
            ##### To split a string by occurrences of a pattern:
            """
        )
        st.code(
            """
            words = re.split(r"\s+", text)  # Split on one or more spaces
            print(words)
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("7. Escaping Special Characters")
        
        st.markdown(
            """
            ##### To match special characters literally, escape them:
            """
        )
        st.code(
            """
            escaped = re.search(r"\bfor\b", text)  # \b is a word boundary        
            """
        )
        
        
        
        
        st.subheader("8. Grouping and Capturing")
        
        st.markdown(
            """
            ##### To group parts of a pattern and extract their values:
            """
        )
        st.code(
            """
            match = re.search(r"(\w+) (\w+)", text)
            if match:
                print(match.group())  # The whole match
                print(match.group(1)) # The first group
                
            """
        )
        
        
        st.subheader("9. Non-Capturing Groups")
        
        st.markdown(
            """
            ##### To define groups without capturing them:
            """
        )
        st.code(
            """
            match = re.search(r"(?:\w+) (\w+)", text)
            if match:
                print(match.group(1))  # The first (and only) group
            """
        )
        
        
        
        st.subheader("10. Lookahead and Lookbehind Assertions")
        
        st.markdown(
            """
            ##### To match a pattern based on what comes before or after it without including it in the result:
            """
        )
        st.code(
            """
            lookahead = re.search(r"\b\w+(?= string)", text)  # Word before ' string'
            lookbehind = re.search(r"(?<=Search )\w+", text)  # Word after 'Search '
            if lookahead:
                print(lookahead.group())
            if lookbehind:
                print(lookbehind.group())
            """
        )
        
        st.subheader("11. Flags to Modify Pattern Matching Behavior")
        
        st.markdown(
            """
            ##### To use flags like re.IGNORECASE to change how patterns are matched:
            """
        )
        st.code(
            """
            case_insensitive = re.findall(r"search", text, re.IGNORECASE)
            print(case_insensitive)
            """
        )
        
        
        st.subheader("12. Using Named Groups")
        
        st.markdown(
            """
            ##### To assign names to groups and reference them by name:
            """
        )
        st.code(
            """
            match = re.search(r"(?P<first>\w+) (?P<second>\w+)", text)
            if match:
                print(match.group('first'))
                print(match.group('second'))
            """
        )
        
        st.subheader("13. Matching Across Multiple Lines")
        
        st.markdown(
            """
            ##### To match patterns over multiple lines using the re.MULTILINE flag:
            """
        )
        st.code(
            """
            multi_line_text = "Start\nmiddle end"
            matches = re.findall(r"^m\w+", multi_line_text, re.MULTILINE)
            print(matches)
            """
        )
        
        
        st.subheader("14. Lazy Quantifiers")
        
        st.markdown(
            """
            ##### To match as few characters as possible using lazy quantifiers (*?, +?, ??):
            """
        )
        st.code(
            """
            html = "<body><h1>Title</h1></body>"
            match = re.search(r"<.*?>", html)
            if match:
                print(match.group())  # Matches '<body>'
            """
        )
        
        
        
        st.subheader("15. Verbose Regular Expressions")
        
        st.markdown(
            """
            ##### To use re.VERBOSE for more readable regular expressions:
            """
        )
        st.code(
            """
            pattern = re.compile(r"
                \b      # Word boundary
                \w+     # One or more word characters
                \s      # Space
                ", re.VERBOSE)
            match = pattern.search(text)
            """
        )





def strings():
    st.header("Working With Strings")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("1. Concatenating Strings")
        
        st.markdown(
            """
            ##### To join strings together:
            """
        )
        st.code(
            """
            greeting = "Hello"
            name = "Alice"
            message = greeting + ", " + name + "!"
            print(message)
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("2. String Formatting with str.format")
        
        st.markdown(
            """
            ##### To insert values into a string template:
            """
        )
        st.code(
            """
            message = "{}, {}. Welcome!".format(greeting, name)
            print(message)
            """
        )
        
        
        
        
        st.subheader("3. Formatted String Literals (f-strings)")
        
        st.markdown(
            """
            ##### To embed expressions inside string literals (Python 3.6+):
            """
        )
        st.code(
            """
            message = f"{greeting}, {name}. Welcome!"
            print(message)
            """
        )
        
        
        st.subheader("4. String Methods — Case Conversion")
        
        st.markdown(
            """
            ##### To change the case of a string:
            """
        )
        st.code(
            """
            s = "Python"
            print(s.upper())  # Uppercase
            print(s.lower())  # Lowercase
            print(s.title())  # Title Case
            """
        )
        
        
        
        st.subheader("5. String Methods — strip, rstrip, lstrip")
        
        st.markdown(
            """
            ##### To remove whitespace or specific characters from the ends of a string:
            """
        )
        st.code(
            """
            s = "   trim me   "
            print(s.strip())   # Both ends
            print(s.rstrip())  # Right end
            print(s.lstrip())  # Left end
            """
        )
            
        
    with col2:
        st.subheader("6. String Methods — startswith, endswith")
        
        st.markdown(
            """
            ##### To check the start or end of a string for specific text:
            """
        )
        st.code(
            """
            s = "filename.txt"
            print(s.startswith("file"))  # True
            print(s.endswith(".txt"))    # True
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("7. String Methods — split, join")
        
        st.markdown(
            """
            ##### To split a string into a list or join a list into a string:
            """
        )
        st.code(
            """
            s = "split,this,string"
            words = s.split(",")        # Split string into list
            joined = " ".join(words)    # Join list into string
            print(words)
            print(joined)         
            """
        )
        
        
        
        
        st.subheader("8. String Methods — replace")
        
        st.markdown(
            """
            ##### To replace parts of a string with another string:
            """
        )
        st.code(
            """
            s = "Hello world"
            new_s = s.replace("world", "Python")
            print(new_s)
            """
        )
        
        
        st.subheader("9. String Methods — find, index")
        
        st.markdown(
            """
            ##### To find the position of a substring within a string:
            """
        )
        st.code(
            """
            s = "look for a substring"
            position = s.find("substring")  # Returns -1 if not found
            index = s.index("substring")    # Raises ValueError if not found
            print(position)
            print(index)
            """
        )
        
        
        
        st.subheader("10. String Methods — Working with Characters")
        
        st.markdown(
            """
            ##### To process individual characters in a string:
            """
        )
        st.code(
            """
            s = "characters"
            for char in s:
                print(char)  # Prints each character on a new line
            """
        )

        st.subheader("11. String Methods — isdigit, isalpha, isalnum")
        
        st.markdown(
            """
            ##### To check if a string contains only digits, alphabetic characters, or alphanumeric characters:
            """
        )
        st.code(
            """
            print("123".isdigit())   # True
            print("abc".isalpha())   # True
            print("abc123".isalnum())# True
            """
        )
        
        
        st.subheader("12. String Slicing")
        
        st.markdown(
            """
            ##### To extract a substring using slicing:
            """
        )
        st.code(
            """
            s = "slice me"
            sub = s[2:7]  # From 3rd to 7th character
            print(sub)
            """
        )
        
        
        st.subheader("13. String Length with len")
        
        st.markdown(
            """
            ##### To get the length of a string:
            """
        )
        st.code(
            """
            s = "length"
            print(len(s))  # 6
            """
        )
        
        
        st.subheader("14. Multiline Strings")
        
        st.markdown(
            """
            ##### To work with strings spanning multiple lines:
            """
        )
        st.code(
            """
            multi = "Line one
                Line two
                Line three"
                print(multi)
            """
        )
        
        
        st.subheader("15. Raw Strings")
        
        st.markdown(
            """
            ##### To treat backslashes as literal characters, useful for regex patterns and file paths:
            """
        )
        st.code(
            """
            path = r"C:\User\name\folder"
            print(path)
            """
        )
        
        
    





def web_scraping():
    st.header("Working With Web Scraping")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("1. Fetching Web Pages with requests")
        
        st.markdown(
            """
            ##### To retrieve the content of a web page:
            """
        )
        st.code(
            """
            import requests

            url = 'https://example.com'
            response = requests.get(url)
            html = response.text
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("2. Parsing HTML with BeautifulSoup")
        
        st.markdown(
            """
            ##### To parse HTML and extract data:
            """
        )
        st.code(
            """
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(html, 'html.parser')
            print(soup.prettify())  # Pretty-print the HTML
            """
        )
        
        
        
        
        st.subheader("3. Navigating the HTML Tree")
        
        st.markdown(
            """
            ##### To find elements using tags:
            """
        )
        st.code(
            """
            title = soup.title.text  # Get the page title
            headings = soup.find_all('h1')  # List of all <h1> tags
            """
        )
        
        
        st.subheader("4. Using CSS Selectors")
        
        st.markdown(
            """
            ##### To select elements using CSS selectors:
            """
        )
        st.code(
            """
            articles = soup.select('div.article')  # All elements with class 'article' inside a <div>
            """
        )
        
        
        
        st.subheader("5. Extracting Data from Tags")
        
        st.markdown(
            """
            ##### To extract text and attributes from HTML elements:
            """
        )
        st.code(
            """
            for article in articles:
                title = article.h2.text  # Text inside the <h2> tag
                link = article.a['href']  # 'href' attribute of the <a> tag
                print(title, link)
            """
        )
            
        
    with col2:
        st.subheader("6. Handling Relative URLs")
        
        st.markdown(
            """
            ##### To convert relative URLs to absolute URLs:
            """
        )
        st.code(
            """
            from urllib.parse import urljoin
            absolute_urls = [urljoin(url, link) for link in relative_urls]
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("7. Dealing with Pagination")
        
        st.markdown(
            """
            ##### To scrape content across multiple pages:
            """
        )
        st.code(
            """
            base_url = "https://example.com/page/"
            for page in range(1, 6):  # For 5 pages
                page_url = base_url + str(page)
                response = requests.get(page_url)
                # Process each page's content         
            """
        )
        
        
        
        
        st.subheader("8. Handling AJAX Requests")
        
        st.markdown(
            """
            ##### To scrape data loaded by AJAX requests:
            """
        )
        st.code(
            """
            # Find the URL of the AJAX request (using browser's developer tools) and fetch it
            ajax_url = 'https://example.com/ajax_endpoint'
            data = requests.get(ajax_url).json()  # Assuming the response is JSON
            """
        )
        
        
        st.subheader("9. Using Regular Expressions in Web Scraping")
        
        st.markdown(
            """
            ##### To extract data using regular expressions:
            """
        )
        st.code(
            """
            import re
            emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', html)
            """
        )
        
        
        
        st.subheader("10. Respecting robots.txt")
        
        st.markdown(
            """
            ##### To check robots.txt for scraping permissions:
            """
        )
        st.code(
            """
            from urllib.robotparser import RobotFileParser

            rp = RobotFileParser()
            rp.set_url('https://example.com/robots.txt')
            rp.read()
            can_scrape = rp.can_fetch('*', url)
            """
        )
        
        
        st.subheader("11. Using Sessions and Cookies")
        
        st.markdown(
            """
            ##### To maintain sessions and handle cookies:
            """
        )
        st.code(
            """
            session = requests.Session()
            session.get('https://example.com/login')
            session.cookies.set('key', 'value')  # Set cookies, if needed
            response = session.get('https://example.com/protected_page')
            """
        )
        
        st.subheader("12. Scraping with Browser Automation (selenium Library)")
        
        st.markdown(
            """
            ##### To scrape dynamic content rendered by JavaScript:
            """
        )
        st.code(
            """
            from selenium import webdriver
            browser = webdriver.Chrome()
            browser.get('https://example.com')
            content = browser.page_source
            # Parse and extract data using BeautifulSoup, etc.
            browser.quit()
            """
        )
        
        
        st.subheader("13. Error Handling in Web Scraping")
        
        st.markdown(
            """
            ##### To handle errors and exceptions:
            """
        )
        st.code(
            """
            try:
                response = requests.get(url, timeout=5)
                response.raise_for_status()  # Raises an error for bad status codes
            except requests.exceptions.RequestException as e:
                print(f"Error: {e}")
            """
        )
        
        
        st.subheader("14. Asynchronous Web Scraping")
        
        st.markdown(
            """
            ##### To scrape websites asynchronously for faster data retrieval:
            """
        )
        st.code(
            """
            import aiohttp
            import asyncio

            async def fetch(url):
                async with aiohttp.ClientSession() as session:
                    async with session.get(url) as response:
                        return await response.text()

            urls = ['https://example.com/page1', 'https://example.com/page2']
            loop = asyncio.get_event_loop()
            pages = loop.run_until_complete(asyncio.gather(*(fetch(url) for url in urls)))
            """
        )
        
        
        st.subheader("15. Data Storage (CSV, Database)")
        
        st.markdown(
            """
            ##### To store scraped data in a CSV file or a database:
            """
        )
        st.code(
            """
            import csv

            with open('output.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Title', 'URL'])
                for article in articles:
                    writer.writerow([article['title'], article['url']])
            """
        )
        







def pip_():
    st.header("Working With pip (Package Management)")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("Basic GET Request")
        
        st.markdown(
            """
            ##### 1. Installing a Package
            """
        )
        st.code(
            """
            pip install numpy
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("2. Listing Installed Packages")
        
        st.markdown(
            """
            ##### To survey the compendium of libraries that reside within your realm, noting their versions and lineage:
            """
        )
        st.code(
            """
            pip list
            """
        )
        
        
        
        
        st.subheader("3. Upgrading a Package")
        
        st.markdown(
            """
            ##### To imbue an installed library with enhanced powers and capabilities, elevating it to its latest form:
            """
        )
        st.code(
            """
            pip install --upgrade numpy
            """
        )
        
        
        st.subheader("4. Uninstalling a Package")
        
        st.markdown(
            """
            ##### To uninstall a package:
            """
        )
        st.code(
            """
            pip uninstall numpy
            """
        )
        
        
        
        st.subheader("5. Searching for Packages")
        
        st.markdown(
            """
            ##### Searching packages:
            """
        )
        st.code(
            """
            pip search "data visualization"
            """
        )
            
        
    with col2:
        st.subheader("6. Installing Specific Versions of a Package")
        
        st.markdown(
            """
            ##### To install a specific version:
            """
        )
        st.code(
            """
            pip install numpy==1.18.5
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("7. Generating a Requirements File")
        
        st.markdown(
            """
            ##### Requirements file:
            """
        )
        st.code(
            """
            pip freeze > requirements.txt      
            """
        )
        
        
        
        
        st.subheader("8. Installing Packages from a Requirements File")
        
        st.markdown(
            """
            ##### To conjure a symphony of libraries in unison, each aligned with the notations in your tome of requirements:
            """
        )
        st.code(
            """
            pip install -r requirements.txt
            """
        )
        
        
        st.subheader("9. Using Virtual Environments")
        
        st.markdown(
            """
            ##### Create virtual Environments to manage package conflicts:
            """
        )
        st.code(
            """
            # Create a virtual environment named 'venv'
            python -m venv venv

            # Activate the virtual environment
            # On Windows
            .\venv\Scripts\activate

            # On Unix or MacOS
            source venv/bin/activate
            """
        )
        
        
        
        st.subheader("10. Checking Package Dependencies")
        
        st.markdown(
            """
            ##### Understanding Dependencies:
            """
        )
        st.code(
            """
            pip show numpy
            """
        )





def common_python():
    st.header("Working With Common Built-in Functions and Packages")
    
    
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    
    with col1:
        st.subheader("1. os - Operating System Interface")
        
        st.markdown(
            """
            ##### To interact with the operating system:
            """
        )
        st.code(
            """
            import os
            current_directory = os.getcwd()  # Get the current working directory
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("2. sys - System-specific Parameters and Functions")
        
        st.markdown(
            """
            ##### To access system-specific parameters and functions:
            """
        )
        st.code(
            """
            import sys
            sys.exit()  # Exit the script
            """
        )
        
        
        
        
        st.subheader("3. datetime - Basic Date and Time Types")
        
        st.markdown(
            """
            ##### To work with dates and times:
            """
        )
        st.code(
            """
            from datetime import datetime
            now = datetime.now()  # Current date and time
            """
        )
        
        
        st.subheader("4. math - Mathematical Functions")
        
        st.markdown(
            """
            ##### To perform mathematical operations:
            """
        )
        st.code(
            """
            import math
            result = math.sqrt(16)  # Square root
            """
        )
        
        
        
        st.subheader("5. random - Generate Pseudo-random Numbers")
        
        st.markdown(
            """
            ##### To generate pseudo-random numbers:
            """
        )
        st.code(
            """
            import random
            number = random.randint(1, 10)  # Random integer between 1 and 10   
            """
        )
        
        
        
        st.subheader("6. json - JSON Encoder and Decoder")
        
        st.markdown(
            """
            ##### To parse and generate JSON data:
            """
        )
        st.code(
            """
            import json
            json_string = json.dumps({'name': 'Alice', 'age': 30})  # Dictionary to JSON string
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("7. re - Regular Expressions")
        
        st.markdown(
            """
            ##### To work with regular expressions:
            """
        )
        st.code(
            """
            import re
            match = re.search('Hello', 'Hello, world!')  # Search for 'Hello' in the string
            """
        )
        
        
        
        
        st.subheader("8. urllib - URL Handling Modules")
        
        st.markdown(
            """
            ##### To work with URLs:
            """
        )
        st.code(
            """
            from urllib.request import urlopen
            content = urlopen('http://example.com').read()  # Fetch the content of a webpage
            """
        )
        
        
        st.subheader("9. http - HTTP Modules")
        
        st.markdown(
            """
            ##### To create HTTP servers and work with HTTP requests:
            """
        )
        st.code(
            """
            from http.server import HTTPServer, BaseHTTPRequestHandler
            
            class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
                def do_GET(self):
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(b'<html><head><title>Python HTTP Server</title></head>')
                    self.wfile.write(b'<body><h1>Hello from a simple Python HTTP server!</h1></body></html>')
            def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
                server_address = ('', 8000)  # Serve on all addresses, port 8000
                httpd = server_class(server_address, handler_class)
                print("Server starting on port 8000...")
                httpd.serve_forever()
            if __name__ == '__main__':
                run()
            """
        )
        
        
        
        st.subheader("10. subprocess - Subprocess Management")
        
        st.markdown(
            """
            ##### To spawn new processes and connect to their input/output/error pipes:
            """
        )
        st.code(
            """
            import subprocess
            subprocess.run(['ls', '-l'])  # Run the 'ls -l' command
            """
        )
        
        
        st.subheader("11. socket - Low-level Networking Interface")
        
        st.markdown(
            """
            ##### To create network clients and servers:
            """
        )
        st.code(
            """
            import socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP/IP socket
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("12. threading - Thread-based Parallelism")
        
        st.markdown(
            """
            ##### To manage concurrent execution of code:
            """
        )
        st.code(
            """
            import threading
            def worker():
                print("Worker thread executing")
            thread = threading.Thread(target=worker)
            thread.start()
            """
        )
        
        
        
        
        st.subheader("13. multiprocessing - Process-based Parallelism")
        
        st.markdown(
            """
            ##### To manage concurrent processes:
            """
        )
        st.code(
            """
            from multiprocessing import Process
            def worker():
                print("Worker process")
            p = Process(target=worker)
            p.start()
            """
        )
        
        
        st.subheader("14. argparse - Parser for Command-line Options, Arguments, and Sub-commands")
        
        st.markdown(
            """
            ##### To parse command-line arguments:
            """
        )
        st.code(
            """
            import argparse
            parser = argparse.ArgumentParser(description="Process some integers.")
            args = parser.parse_args()
            """
        )
        
        
        
        st.subheader("15. logging - Logging Facility")
        
        st.markdown(
            """
            ##### To log messages (debug, info, warning, error, and critical):
            """
        )
        st.code(
            """
            import logging
            logging.warning('This is a warning message')
            """
        )
        
        
        st.subheader("16. unittest - Unit Testing Framework")
        
        st.markdown(
            """
            ##### To create and run unit tests:
            """
        )
        st.code(
            """
            import unittest
            class TestStringMethods(unittest.TestCase):
                def test_upper(self):
                    self.assertEqual('foo'.upper(), 'FOO')
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("17. pathlib - Object-oriented Filesystem Paths")
        
        st.markdown(
            """
            ##### To work with filesystem paths in an object-oriented way:
            """
        )
        st.code(
            """
            from pathlib import Path
            p = Path('.')
            """
        )
        
        
        
        
        st.subheader("18. functools - Higher-order Functions and Operations on Callable Objects")
        
        st.markdown(
            """
            ##### To use higher-order functions and operations on callable objects:
            """
        )
        st.code(
            """
            from functools import lru_cache
            @lru_cache(maxsize=None)
            def fib(n):
                if n < 2:
                    return n
                return fib(n-1) + fib(n-2)
            """
        )
        
        
        st.subheader("19. collections - Container Data Types")
        
        st.markdown(
            """
            ##### To use specialized container data types (deque, Counter, OrderedDict, etc.):
            """
        )
        st.code(
            """
            from collections import Counter
            c = Counter('hello world')
            """
        )
        
        
        
        st.subheader("20. itertools - Functions Creating Iterators for Efficient Looping")
        
        st.markdown(
            """
            ##### To construct and use iterators for efficient looping:
            """
        )
        st.code(
            """
            import itertools
            for combination in itertools.combinations('ABCD', 2):
                print(combination)
            """
        )
        
        st.subheader("21. hashlib - Secure Hash and Message Digest Algorithms")
        
        st.markdown(
            """
            ##### To hash data:
            """
        )
        st.code(
            """
            import hashlib
            hash_object = hashlib.sha256(b'Hello World')
            hex_dig = hash_object.hexdigest()
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("22. csv - CSV File Reading and Writing")
        
        st.markdown(
            """
            ##### To read from and write to CSV files:
            """
        )
        st.code(
            """
            import csv
            with open('file.csv', mode='r') as infile:
                reader = csv.reader(infile)
            """
        )
        
        
        
        
        st.subheader("23. xml.etree.ElementTree - The ElementTree XML API")
        
        st.markdown(
            """
            ##### To parse and create XML data:
            """
        )
        st.code(
            """
            import xml.etree.ElementTree as ET
            tree = ET.parse('file.xml')
            root = tree.getroot()
            """
        )
        
        
        st.subheader("24. sqlite3 - DB-API 2.0 Interface for SQLite Databases")
        
        st.markdown(
            """
            ##### To interact with SQLite databases:
            """
        )
        st.code(
            """
            import sqlite3
            conn = sqlite3.connect('example.db')
            """
        )
        
        
        
        st.subheader("25. tkinter - GUI Toolkit")
        
        st.markdown(
            """
            ##### To create GUI applications:
            """
        )
        st.code(
            """
            import tkinter as tk
            root = tk.Tk()
            """
        )
            
        
    with col2:
        st.subheader("26. pickle - Python Object Serialization")
        
        st.markdown(
            """
            ##### To serialize and deserialize Python object structures:
            """
        )
        st.code(
            """
            import pickle
            serialized_obj = pickle.dumps(obj)
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("27. io - Core Tools for Working with Streams")
        
        st.markdown(
            """
            ##### To handle streams (file-like objects):
            """
        )
        st.code(
            """
            from io import StringIO
            f = StringIO("some initial text data")        
            """
        )
        
        
        
        
        st.subheader("28. time - Time Access and Conversions")
        
        st.markdown(
            """
            ##### To access time-related functions:
            """
        )
        st.code(
            """
            import time
            time.sleep(1)  # Sleep for 1 second
            """
        )
        
        
        st.subheader("29. calendar - General Calendar-related Functions")
        
        st.markdown(
            """
            ##### To work with calendars:
            """
        )
        st.code(
            """
            import calendar
            print(calendar.month(2023, 1))  # Print the calendar for January 2023
            """
        )
        
        
        
        st.subheader("30. queue - A Synchronized Queue Class")
        
        st.markdown(
            """
            ##### To manage a queue, useful in multithreaded programming:
            """
        )
        st.code(
            """
            from queue import Queue
            q = Queue()
            """
        )
        
        st.subheader("31. shutil - High-level File Operations")
        
        st.markdown(
            """
            ##### To perform high-level file operations, like copying and archiving:
            """
        )
        st.code(
            """
            import shutil
            shutil.copyfile('source.txt', 'dest.txt')
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        st.subheader("32. glob - Unix Style Pathname Pattern Expansion")
        
        st.markdown(
            """
            ##### To find files matching a specified pattern:
            """
        )
        st.code(
            """
            import glob
            for file in glob.glob("*.txt"):
                print(file)
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
            ##### 41. Leveraging the zip() function for parallel iteration:
            """
        )
        st.code(
            """
            pairs = list(zip([1, 2, 3], ['a', 'b', 'c']))
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        
        st.markdown(
            """
            ##### 42. The any() and all() functions for boolean checks:
            """
        )
        st.code(
            """
            has_positive = any(x > 0 for x in [1, -2, 3, -4])
            all_positive = all(x > 0 for x in [1, 2, 3, 4])        
            """
        )
        
        
        
        
        
        st.markdown(
            """
            ##### 43. Removing duplicates from a list while preserving order:
            """
        )
        st.code(
            """
            unique_list = list(dict.fromkeys([1, 2, 2, 3, 4]))
            """
        )
        
        
       
        
        st.markdown(
            """
            ##### 44. Removing whitespace from the beginning and end of a string:
            """
        )
        st.code(
            """
            trimmed_str = '  hello world  '.strip()
            """
        )
        
        
        
        
        st.markdown(
            """
            ##### 45. Parsing and extracting information from a string using regular expressions:
            """
        )
        st.code(
            """
            import re
            extracted_digits = re.findall(r'\d+', 'abc123def456')
            """
        )
        
        
       
        
        st.markdown(
            """
            ##### 46. Swapping case in a string using a list comprehension:
            """
        )
        st.code(
            """
            swapped_case = ''.join([char.upper() if char.islower() else char.lower() for char in 'Hello World'])
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        
        
        st.markdown(
            """
            ##### 47. Checking if a number is prime using all() and range:
            """
        )
        st.code(
            """
            is_prime = lambda num: num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))       
            """
        )
        
        
       
        st.markdown(
            """
            ##### 48. Finding the longest word in a sentence using max() and split:
            """
        )
        st.code(
            """
            longest_word = max("Hello World example sentence".split(), key=len)
            """
        )
        
        
        
        
        st.markdown(
            """
            ##### 49. Converting a binary string to an integer:
            """
        )
        st.code(
            """
            binary_to_int = int('1101', 2)
            """
        )
        
        
        

        
        st.markdown(
            """
            ##### 50. Filtering out non-positive numbers from a list:
            """
        )
        st.code(
            """
            positive_numbers = list(filter(lambda x: x > 0, [-2, 0, 3, -1, 5]))
            """
        )
        
        
        
        
        
        
        st.markdown(
            """
            ##### 51. Extract all email addresses from text:
            """
        )
        st.code(
            """
            emails = re.findall(r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b", text)
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        
        
        st.markdown(
            """
            ##### 52.Validate a phone number format:
            """
        )
        st.code(
            """
            pattern = re.compile(r"^\+?[\d\s]{7,}$")
            phone = pattern.match(phone_number)         
            """
        )
        
        
        
        
        
        st.markdown(
            """
            ##### 53. Download a file from a URL:
            """
        )
        st.code(
            """
            urllib.request.urlretrieve("https://example.com/file.zip", "downloaded_file.zip")
            """
        )
        
        
        
        
        st.markdown(
            """
            ##### 54. Check website status efficiently:
            """
        )
        st.code(
            """
            response = requests.get("https://example.com").status_code
            """
        )
        
        
        
    
        
        st.markdown(
            """
            ##### 55. List files in a directory:
            """
        )
        st.code(
            """
            files = [f for f in os.listdir("path/to/dir") if os.path.isfile(os.path.join("path/to/dir", f))]
            """
        )
        
        
        
        
        
        st.markdown(
            """
            ##### 56. Cache function results for efficiency:
            """
        )
        st.code(
            """
            @cache def expensive_calculation(): ...
            """
        )
        
        # if st.toggle("Show `st.write` sample output"):
        #     st.write("Did you know I have more then 101 Supreme apps like this?")
        
        
        
        
        st.markdown(
            """
            ##### 57. Safely open and close a file:
            """
        )
        st.code(
            """
            with open("file.txt", "r") as f: data = f.readlines()          
            """
        )
        
        
        
        
        st.markdown(
            """
            ##### 58. Lock a resource to prevent concurrency issues:
            """
        )
        st.code(
            """
            with threading.Lock(): shared_data += 1
            """
        )
        
        
        
        
        st.markdown(
            """
            ##### 59. Use Selenium to interact with webpages:
            """
        )
        st.code(
            """
            driver.find_element_by_id("button").click()
            """
        )
        
        
        
        
        
        st.markdown(
            """
            ##### 60. Get system information like CPU usage:
            """
        )
        st.code(
            """
            os.cpu_count(), psutil.cpu_percent()
            """
        )
        
        
    
        
        
    


















