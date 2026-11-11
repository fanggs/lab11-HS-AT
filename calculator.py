import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Zero Division Error"

def logarithm(a, b):
    try:
        return math.log(b, a)
    except ValueError:
        return "Value Error"

def exponent(a, b):
    return a**b



