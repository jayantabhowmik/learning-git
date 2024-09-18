import os, sys

def my_function(   a,b):
print(a+b)  # Indentation error, should be indented under the function
    return  a+b

def unused_function():
    pass # Function is never used

x  =  5
y= 10
z = my_function(x, y)

if z>  10 : print( "Greater than 10")   # E701: multiple statements on one line
