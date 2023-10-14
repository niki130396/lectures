
# Integers

"""
In Python, integers are zero, positive or negative whole numbers without a fractional part
and having unlimited precision, e.g. 0, 100, -10.
The followings are valid integer literals in Python.
Integers can be binary, octal, and hexadecimal values.
All integer literals or variables are objects of the int class.
"""


"""
In Python 3, there is no limit to how long an integer value can be as long as it fits in RAM.
If you want to know how large of an integer you can create use sys.maxsize.
The value would be around 8^sys.maxsize. That is 8 to the power of whatever sys,maxsize returns.
"""
import sys
print(sys.maxsize)

"""
In Python we don't have short, int and long like some other languages have, instead we only have int.
The Python int doesn't reserve a predefined size in memory like the other datatypes like short, int and long do.
Python integers are arbitrary-precision integers, also known as bignums. 
This means that they can be as large as we want, and their sizes are only limited by the amount of available memory.
More on how integers are implemented in Python: 
https://tenthousandmeters.com/blog/python-behind-the-scenes-8-how-python-integers-work/
"""

int_example = 555
print(type(int_example))

"""
1) In Python 3, the maximum value for an integer is 263 - 1:

a) True
b) False
"""
