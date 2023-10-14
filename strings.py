"""
Strings are sequences of character data. The string type in Python is called str.
String literals may be delimited using either single or double quotes.
All the characters between the opening delimiter and matching closing delimiter are part of the string:
"""

print("I am a string.")
print(type("I am a string."))
print('I am too.')
print(type('I am too.'))

"""
A string in Python can contain as many characters as you wish. 
The only limit is your machine’s memory resources. 
A string can also be empty:
"""

print("")
print(type(""))

"""
But how do computers deal with non-numeric values?
Computers deal with numbers, so how do we represent characters as numbers?
The process of mapping characters to numbers is known as character encoding.
One of the first adopted character encoding systems was ASCII, 
which stands for American Standard Code for Information Interchange.
"""

"""
And this is how characters are mapped to decimal numbers:
Decimal     Character
48          0
49          1
58          :
59          ;
65          A
66          B
97          a
99          c
"""

"""
Python has a built in function for us to check the ASCII number of ASCII characters. It's called `ord`
"""

print(ord("A"))
print(ord("a"))


"""
However, since there are multiple languages across the world ASCII doesn't fit well, because it only handles latin
symbols. This is where the Unicode encoding system steps in.
More on how Python handles strings by using the Unicode encoding system here:
https://tenthousandmeters.com/blog/python-behind-the-scenes-9-how-python-strings-work/
"""

string_example = "This is a string"

"""
But what if we want to include special characters in our string?
What if, for instance, we wanted to include another set of quotes inside the string?
"""

# string_example = "This is what happens is you try to include quotes " "

"""
The following piece of code results in a syntax error:
SyntaxError: EOL while scanning string literal
"""

"""
The process of suppressing special character meaning is called Escaping.
In Python escaping is done by including a backslash `\` before the special character
"""

# string_example = "This is what happens is you try to include quotes \" "

"""
Or you can use single quotes inside double quotes
"""
# string_example = "This is what happens is you try to include quotes ' "


#  Basic string operations

# 1) String concatenation
y = "This "
x = "is "
z = "a string"

s = y + x + z
print(s)

# 2) String multiplication
s = y * 4
print(s)

# 3) Check if string is present

print(y in s)
print("That" in s)
