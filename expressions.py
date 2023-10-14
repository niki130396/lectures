
#  https://realpython.com/python-operators-expressions/


"""
In programming, an operator is usually a symbol or combination of
symbols that allows you to perform a specific operation.
This operation can act on one or more operands.
"""


"""
If the operation involves a single operand, then the operator is unary.
"""
negative = -274.15
print(negative)
print(negative < 0)

"""
If the operator involves two operands, then the operator is binary.
"""
subtraction = 5 - 2
print(subtraction)


"""
Operators provide a quick shortcut for you to manipulate data, 
perform mathematical calculations, compare values, run Boolean tests, 
assign values to variables, and more. 
In Python, an operator may be a symbol, a combination of symbols, 
or a keyword, depending on the type of operator that you’re dealing with.
"""

print(4 == 4)
print(True is False)
print(True == 1)
print(False == 0)


"""
Boolean or logical operators in Python are keywords rather than signs, 
as you’ll learn in the section about Boolean operators and expressions. 
So, instead of the odd signs like ||, &&, and ! that many other programming languages use, Python uses or, and, and not.

Using keywords instead of odd signs is a really cool design decision that’s consistent 
with the fact that Python loves and encourages code’s readability.
"""


"""
Operators by themselves don’t do much. 
If you use an operator without the required operands, then you’ll get a syntax error.
So, operators must be part of expressions, which you can build using Python objects as operands.
An expression is a simple statement that produces and returns a value.
"""

print(7 + 5)
print(42 / 2)

"""
Note that not all expressions use operators. 
For example, a bare function call is an expression that doesn’t require any operator:
"""

print(abs(-7))
print(7 ** 2)
print(pow(7, 2))
print("Hello World")

"""
The assignment operator allows you to assign values to variables. 
Strictly speaking, in Python, this operator makes variables or 
names refer to specific objects in your computer’s memory. 
In other words, an assignment creates a reference to a 
concrete object and attaches that reference to the target variable.
"""

# For more on Python's assignment operator -
# https://realpython.com/python-assignment-operator/


"""
Assignment statements not only assign a value to a variable but also determine the data type of the variable at hand. 
This additional behavior is another important detail to consider in this kind of statement.

Because Python is a dynamically typed language, 
successive assignments to a given variable can change the variable’s data type. 
Changing the data type of a variable during a program’s execution is considered bad practice and highly discouraged. 
It can lead to subtle bugs that can be difficult to track down.
"""

