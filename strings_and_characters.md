# Strings and Character

[https://realpython.com/python-strings/](https://realpython.com/python-strings/)

**Strings are sequences of character data. The string type in Python is called str. \
String literals may be delimited using either single or double quotes. \
All the characters between the opening delimiter and matching closing delimiter are part of the string:**

```python
a = "This is a string."
type(a)
```

**A string in Python can contain as many characters as you wish. \
The only limit is your machine’s memory resources. \
A string can also be empty:**

```python
a = ""
type(a)
```

**But how do computers deal with non-numeric values? \
Computers deal with numbers, so how do we represent characters as numbers? \
The process of mapping characters to numbers is known as character encoding. \
One of the first adopted character encoding systems was ASCII, \
which stands for American Standard Code for Information Interchange.**

**And this is how characters are mapped to decimal numbers:**

| Decimal | Character |
|---------|-----------|
| 48      | 0         |
| 49      | 1         |
| 58      | :         |
| 59      | ;         |
| 65      | A         |
| 66      | B         |
| 97      | a         |
| 99      | c         |

> **_NOTE:_** Python has a built in function for us to check the ASCII number of ASCII characters. It's called `ord`

```python
ord("A")
ord("a")
```

**If you want to see all of the ascii symbols you can use the string library:**

```python
from string import printable

print(printable)
```

**However, since there are multiple languages across the world ASCII doesn't fit well, because it only handles latin \
symbols. This is where the Unicode encoding system steps in. \
More on how Python handles strings by using the Unicode encoding system here: \
[https://tenthousandmeters.com/blog/python-behind-the-scenes-9-how-python-strings-work/](https://tenthousandmeters.com/blog/python-behind-the-scenes-9-how-python-strings-work/)**


**But what if we want to include special characters in our string? \
What if, for instance, we wanted to include another set of quotes inside the string?**

```python
string_example = "This is what happens fs you try to include quotes " "
```

**The following piece of code results in a syntax error: \
SyntaxError: EOL while scanning string literal**

**The process of suppressing special character meaning is called Escaping. \
In Python escaping is done by including a backslash `\` before the special character**

```python
string_example = "This is what happens is you try to include quotes \" "
```

**Or you can use single quotes inside double quotes**

```python
string_example = "This is what happens is you try to include quotes ' "
```

## Basic string operations

- String concatenation 

```python
y = "This "
x = "is "
z = "a string"

s = y + x + z
```

- String multiplication

```python
y = "This "

s = y * 4
print(s)
```

- Check if string is present

```python
y = "This "
x = "is "

y in s
"That" in s
```

## String Indexing

**In Python, strings are ordered sequences of character data, \
and thus can be indexed in this way. \
Individual characters in a string can be accessed by specifying \
the string name followed by a number in square brackets ([]).**

**String indexing in Python is zero-based: the first character in the string has index 0, \
the next has index 1, and so on. \
The index of the last character will be the length of the string minus one.**

| s   | t   | r   | i   | n   | g   |
|-----|-----|-----|-----|-----|-----|
| 0   | 1   | 2   | 3   | 4   | 5   |


```python
s = 'string'

print(s[0])
print(s[3])

print(s[len(s) - 1])
```

> **_NOTE:_** In Python you can access the last element of any ordered sequence by using the `-1` index

```python
s = 'string'
print(s[-1])
```

**Attempting to index beyond the end of the string results in an error:**

```python
s = 'string'
print(s[6])
```

> **_NOTE:_** String indices can also be specified with negative numbers, \
> in which case indexing occurs from the end of the string backward: -1 refers to the last character, \
> -2 the second-to-last character, and so on.

## String Slicing

**Python also allows a form of indexing syntax that extracts substrings from a string, \
known as string slicing. \
If s is a string, an expression of the form `s[m:n]` returns the portion of s starting with position m, \
and up to but not including position n:**

```python
s = 'foobar'
print(s[2:5])
```

> **_NOTE:_** If you omit the first index, the slice starts at the beginning of the string. \
> Thus, `s[:m]` and `s[0:m]` are equivalent:

```python
s = 'foobar'

s[:4]
s[0:4]
```

> **_NOTE:_** Similarly, if you omit the second index as in `s[n:]`, \
> the slice extends from the first index through the end of the string. \
> This is a nice, concise alternative to the more cumbersome `s[n:len(s)]`:

```python
s = 'foobar'

s[2:]
s[2:len(s)]
```


> **_NOTE:_** Negative indices can be used with slicing as well. \
> -1 refers to the last character, \
> -2 the second-to-last, and so on, just as with simple indexing. \
> The diagram below shows how to slice the substring 'oob' from the string 'foobar' \
> using both positive and negative indices:


| -6  | -5  | -4  | -3  | -2  | -1  |
|-----|-----|-----|-----|-----|-----|
| s   | t   | r   | i   | n   | g   |
| 0   | 1   | 2   | 3   | 4   | 5   |

```python
s = 'foobar'

s[-5:-2]
s[1:4]
s[-5:-2] == s[1:4]
```

## Specifying a Stride in a String Slice

**There is one more variant of the slicing syntax to discuss. \
Adding an additional: and a third index designates a stride (also called a step), \
which indicates how many characters to jump after retrieving each character in the slice.**

```python
s = 'foobar'

s[0:6:2]
s[1:6:2]
```

## Interpolating Variables Into a String

**In Python version 3.6, a new string formatting mechanism was introduced. \
This feature is formally named the Formatted String Literal, \
but is more usually referred to by its nickname f-string.**

**One simple feature of f-strings you can start using right away is variable interpolation. \
You can specify a variable name directly within an f-string literal, \
and Python will replace the name with the corresponding value.**

```python
n = 20
m = 25
prod = n * m
print(f'The product of {n} and {m} is {prod}')
```

## Modifying Strings

**In a nutshell, you can’t. Strings are one of the data types Python considers immutable, \
meaning not able to be changed. In fact, all the data types you have seen so far are immutable. \
(Python does provide data types that are mutable, as you will soon see.)**

**A statement like this will cause an error:**

```python
s = 'foobar'
s[3] = 'x'
```

**In truth, there really isn’t much need to modify strings. \
You can usually easily accomplish what you want by generating a copy of the original \
string that has the desired change in place. \
There are very many ways to do this in Python. Here is one possibility:**

```python
s = 'foobar'
s = s[:3] + 'x' + s[4:]
```

```python
s = 'foobar'
s = s.replace('b', 'x')
```

## Built-in String Methods

- `s.capitalize()`
- `s.lower()`
- `s.swapcase()`
- `s.title()`
- `s.upper()`
- `s.count(<sub>[, <start>[, <end>]])`
- `s.endswith(<suffix>[, <start>[, <end>]])`
- `s.find(<sub>[, <start>[, <end>]])`
- `s.index(<sub>[, <start>[, <end>]])`
- `s.rfind(<sub>[, <start>[, <end>]])`
- `s.rindex(<sub>[, <start>[, <end>]])`
- `s.startswith(<prefix>[, <start>[, <end>]])`
- `s.isalnum()`
- `s.isalpha()`
- `s.isdigit()`
- `s.islower()`
- `s.isspace()`
- `s.istitle()`
- `s.isupper()`
