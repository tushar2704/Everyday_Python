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
        
        
        
        st.markdown(
            """
            ##### 6) What is the purpose of the 'yield' keyword in Python? Provide an example.
            """
        )
        st.code(
            """
            #The 'yield' keyword is used in a function to defi ne a generator that
            # can be iterated over using a 'for' loop. When the 'yield' keyword is
            # encountered in the function, the current state of the function is
            # saved and the yielded value is returned to the caller. The next time
            # the function is called, execution resumes from where it left off , with
            # the saved state restored. Here's an example:
            
            # define a generator function that yields a sequence of squares
            def squares(n):
                for i in range(n):
                    yield i**2
                    
            # use the generator to print the first 5 squares
            for quare in squares(5):
                print(square)
            """
        )
        
        
        
        st.markdown(
            """
            ##### 7) What is the diff erence between a list
            ##### comprehension and a generator expression in Python?Provide an example of each.
            """
        )
        st.code(
            """
            #A list comprehension is a concise way to create a new list by
            # applying an expression to each element of an existing list oriterable. 
            # A generator expression is similar, but instead of creating a
            # new list, it creates a generator object that can be iterated over. The
            # key diff erence is that a list comprehension creates the entire list in
            # memory all at once, whereas a generator expression generatesvalues on-the-fly 
            # as they are needed. Here are examples of each:
            
            # create a new list using a list comprehension
            list1 = [1, 2, 3, 4, 5]
            squared_list = [x**2 for x in list1]
            print(squared_list)
            
            # create a generator expression
            generator = (x**2 for x in list1)
            
            # iterate over the generator to print the squared numbers
            for square in generator:
                print(square)
            """
        )
        
        
        
        
        st.markdown(
            """
            ##### 8) Write a Python function to check whether a given string is a palindrome or not.
            """
        )
        st.code(
            """
            #Proposed Solution
            def is_palindrome(s):
                return s == s[::-1]
            
            # Example usage:   
            print(is_palindrome('racecar')) # Output: True
            print(is_palindrome('hello')) # Output: False
            """
        )
        
        
        
        st.markdown(
            """
            ##### 9) Write a Python function to fi nd the second highest number in a list.
            """
        )
        st.code(
            """
            #Proposed Solution
            def second_highest(numbers):
                numbers=sorted(set(numbers))
                return numbers[-2] if len(numbers) >= 2 else None
            
            # Example usage:
            print(second_highest([1,3,2,4,4,5])) # Output: 4
            print(second_highest([1])) # Output: None
            """
        )
        
        
        
        
        st.markdown(
            """
            ##### 10) Write a Python function to count the number of vowels in a given string.
            """
        )
        st.code(
            """
            #Proposed Solution
            def count_vowels(s):
                return sum(1 for c s.lower() if c in 'aeiou')
            
            # Example usage:
            print(count_vowels('hello world')) # Output: 3
            """
        )
        
        
        
        st.markdown(
            """
            ##### 11) Write a Python function to fi nd the common elements between two lists.
            """
        )
        st.code(
            """
            #Proposed Solution
            def common_elements(list1, list2):
                return list(set(list1) & set(list2))
            
            # Example usage:
            print(common_elements([1,2,3], [2,3,4])) # Output: [2, 3]
            """
        )
        
        
        
        
        st.markdown(
            """
            ##### 12) Write a Python function to reverse a linked list.
            """
        )
        st.code(
            """
            #Proposed Solution
            def reverse_linked_list(head):
                prev = None
                while head:
                    next = head.next
                    head.next = prev
                    prev = head
                    head = next
                return prev
        
            """
        )
        
        
        
        
        st.markdown(
            """
            ##### 13) Write a Python function to fi nd the shortest pathbetween two nodes in a graph.
            """
        )
        st.code(
            """
            #Proposed Solution
            from collections import deque
            def shortest_path(graph, start, end):
                queue = deque([(start, [start])])
                while queue:
                    node, path = queue.popleft()
                    if node == end:
                        return path
                    for next_node in graph[node] - set(path):
                        queue.append((next_node, path + [next_node]))
                return None
                
            """
        )
        
        
        
        
        st.markdown(
            """
            ##### 14) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        
        
        st.markdown(
            """
            ##### 15)
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        
        st.markdown(
            """
            ##### 16) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        
        
        st.markdown(
            """
            ##### 17) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        st.markdown(
            """
            ##### 18) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        
        st.markdown(
            """
            ##### 19) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        
        st.markdown(
            """
            ##### 20) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        
        
        st.markdown(
            """
            ##### 21) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        
        st.markdown(
            """
            ##### 22) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        
        st.markdown(
            """
            ##### 23) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        st.markdown(
            """
            ##### 24) 
            """
        )
        st.code(
            """
            
            """
        )
        
        
        st.markdown(
            """
            ##### 25) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        st.markdown(
            """
            ##### 26) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        
        st.markdown(
            """
            ##### 27) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        st.markdown(
            """
            ##### 28) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        
        st.markdown(
            """
            ##### 29) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        
        st.markdown(
            """
            ##### 30) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        st.markdown(
            """
            ##### 31) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        
        st.markdown(
            """
            ##### 32) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        
        st.markdown(
            """
            ##### 33) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        
        st.markdown(
            """
            ##### 34) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        
        
        st.markdown(
            """
            ##### 35) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        
        
        st.markdown(
            """
            ##### 36) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        
        
        
        st.markdown(
            """
            ##### 37) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        st.markdown(
            """
            ##### 38) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
            
        
    with col2:
        st.markdown(
            """
            ##### 39) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        st.markdown(
            """
            ##### 40) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        st.markdown(
            """
            ##### 41) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        st.markdown(
            """
            ##### 42) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        st.markdown(
            """
            ##### 43) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        st.markdown(
            """
            ##### 44) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        
        st.markdown(
            """
            ##### 45) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        
        st.markdown(
            """
            ##### 46) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        
        st.markdown(
            """
            ##### 47) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        
        st.markdown(
            """
            ##### 48) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        
        st.markdown(
            """
            ##### 49) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        
        st.markdown(
            """
            ##### 50) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        
        st.markdown(
            """
            ##### 51) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        
        st.markdown(
            """
            ##### 52) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        
        st.markdown(
            """
            ##### 53) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        
        st.markdown(
            """
            ##### 54) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        
        st.markdown(
            """
            ##### 55) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        
        st.markdown(
            """
            ##### 56) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        
        st.markdown(
            """
            ##### 57) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        
        st.markdown(
            """
            ##### 58) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        
        st.markdown(
            """
            ##### 59) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        
        st.markdown(
            """
            ##### 60) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        st.markdown(
            """
            ##### 61) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        
        st.markdown(
            """
            ##### 62) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        
        st.markdown(
            """
            ##### 63) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        
        st.markdown(
            """
            ##### 64) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        st.markdown(
            """
            ##### 65) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        st.markdown(
            """
            ##### 66) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        
        st.markdown(
            """
            ##### 67) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )

        st.markdown(
            """
            ##### 68) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        st.markdown(
            """
            ##### 69) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )


        st.markdown(
            """
            ##### 70) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        
        st.markdown(
            """
            ##### 71) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )


        st.markdown(
            """
            ##### 72) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        st.markdown(
            """
            ##### 73) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        st.markdown(
            """
            ##### 74) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        
        
        st.markdown(
            """
            ##### 75) 
            """
        )
        st.code(
            """
            #Proposed Solution
            """
        )
        

































































































































































































































































































































































































interview_question()
#######################################################################################################
#Body of Everyday_Python [Interview Questiona] by github.com/tushar2704
#######################################################################################################
# footer()