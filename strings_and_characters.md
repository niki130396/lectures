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

> **_NOTE:_** Reversing a string can be done like so:
```python
a = "abcdefg"
reversed_a = a[::-1]
```
> This essentially means take a slice of the string from the start to the end with \
> a reverse step of 1


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

**But why are strings immutable? \
String immutability is a design choice taken by the Python \
language developers, so that we don't end up altering a value by mistake. \
Altering a value by mistake might lead to some serious bugs along the way \
Take the following piece of code as an example:**

[Why are strings immutable?](https://stackoverflow.com/questions/8680080/why-are-python-strings-immutable-best-practices-for-using-them)

```python
a = "Will Smith"

b = a

if b == "Will Smith":
    print(True)
else:
    print(False)

# This prints True
    
a[0] = "B"

if b == "Will Smith":
    print(True)
else:
    print(False)

# This prints False
```

**Now let's imagine that we were able to alter the state of `a` and change the name\
like so:**

```python
a[0] = "B"
```

**This would result in `a` becoming Bill Smith and `b` would now have a different value \
as well, because it points to `a`, and everything that points to `a` will be altered too. \
This is one of the reasons behind this design choice**

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

**Copying the string creates a new object, which means the variable `s` \
now points to a different block of memory where the copied value is stored**

```python
s = "foobar"
print(id(s))
s = s[:1] + s[1:]
print(id(s))
```

## Built-in String Methods

**You might be familiar with functions - they are callable procedures that you can invoke \
to perform specific tasks.**

**Methods are similar to functions. \
A method is a specialized type of callable procedure that is tightly associated with an object. \
Like a function, a method is called to perform a distinct task, \
but it is invoked on a specific object and has knowledge of its target object during execution.**

- `s.capitalize()`

**`s.capitalize()` returns a copy of s with the first character converted to uppercase \
and all other characters converted to lowercase**

```python
s = "foO BaR"
s = s.capitalize()
print(s)
```

- `s.lower()`

**`s.lower()` returns a copy of s with all alphabetic characters converted to lowercase:**

```python
s = "foO BaR"
s = s.lower()
print(s)
```

- `s.swapcase()`

**`s.swapcase()` returns a copy of s with uppercase alphabetic characters converted to lowercase and vice versa:**

```python
s = "foO BaR"
s = s.swapcase()
print(s)
```

- `s.title()`

**`s.title()` returns a copy of s in which the first letter of each word is converted to uppercase \
and remaining letters are lowercase:**

```python
s = "foO BaR"
s = s.title()
print(s)
```

- `s.upper()`

**`s.upper()` returns a copy of s with all alphabetic characters converted to uppercase:**

```python
s = "foO BaR"
s = s.upper()
print(s)
```

- `s.count(<sub>[, <start>[, <end>]])`

**`s.count(<sub>)` returns the number of non-overlapping occurrences of substring <sub> in s:**

```python
s = 'foo goo moo'
print(s.count('oo'))
```

**We can also search within a given substring:**

```python
s = 'foo goo moo'
print(s.count('oo', 1, 3))
```

> **_NOTE:_** This searches only within the index range 1 to 3 (NON-INCLUSIVE)

- `s.endswith(<suffix>[, <start>[, <end>]])`

**`s.endswith(<suffix>)` returns True if s ends with the specified <suffix> and False otherwise:**

```python
s = 'foobar'
print(s.endswith('bar'))
```

- `s.find(<sub>[, <start>[, <end>]])`

**You can use `s.find()` to see if a Python string contains a particular substring. \
`s.find(<sub>)` returns the lowest index in `s` where substring <sub> is found:**

```python
s = 'foo bar foo baz foo qux'
print(s.find('foo'))
```

> **_NOTE:_** Returns `-1` if substring is not found

- `s.index(<sub>[, <start>[, <end>]])`

**This method is identical to `s.find()`, \
except that it raises an exception if <sub> is not found rather than returning `-1`:**

**You can use this method for dynamic slicing:**

**Let's say that we have the following string `s = 'foo bar foo baz foo qux'`\
and we want to get a slice from the first occurrence of `foo` to the last occurrence:**

```python
s = 'foo bar foo baz foo qux'
s_slice = s[s.index("foo"):s.rindex("foo") + 3]
print(s_slice)
```

**What if we wanted to get a slice from the beginning to the last occurrence of `foo`?**

```python
s = 'aaa bbbb foo bar foo baz foo qux'
s_slice = s[:s.rindex("foo") + 3]
print(s_slice)
```

- `s.rfind(<sub>[, <start>[, <end>]])`

**`s.rfind(<sub>)` returns the highest index in s where substring <sub> is found:**

```python
s = 'foo bar foo baz foo qux'
print(s.rfind('foo'))
```

> **_NOTE:_** It's also worth noting that it might be beneficial to use `s.rfind()` in cases when you know \
> the substring exists only once and is closer to the last index than the first.

**Let's say we have the following string `s = 'aaa bbb ccc foo ddd'` and we want to find the index of substring `foo`. \
We can achieve that with using `s.find()` and `s.rfind()`. The difference is we know `s.rfind()` is going to \
find the substring faster because we have a guarantee that the substring will be closer to the last index than the \
first. The other case is when we know the substring is closer to the beginning - that's when we will benefit \
from using `s.find()`**


- `s.rindex(<sub>[, <start>[, <end>]])`

**This method is identical to `s.rfind()`, except that it raises an exception if <sub> is not found \
rather than returning -1:**

```python
s = 'foo bar foo baz foo qux'
print(s.rindex('coo'))
```

- `s.startswith(<prefix>[, <start>[, <end>]])`

**When you use the Python `s.startswith()` method, \
`s.startswith(<suffix>)` returns `True` if `s` starts with the specified <suffix> and `False` otherwise:**

```python
s = 'foobar'
print(s.startswith('foo'))
print(s.startswith('bar'))
```

- `s.isalnum()`

**`s.isalnum()` returns `True` if `s` is nonempty and all its characters are alphanumeric (either a letter or a number), \
and False otherwise:**

```python
s = 'abc123'
print(s.isalnum())
```

- `s.isalpha()`

**`s.isalpha()` returns `True` if `s` is nonempty and all its characters are alphabetic, and `False` otherwise:**

```python
s = 'abc123'
print(s.isalnum())
s = 'abcDEF'
print(s.isalpha())
```

- `s.isdigit()`

**You can use the `s.isdigit()` Python method to check if your string is made of only digits. \
`s.isdigit()` returns `True` if `s` is nonempty and all its characters are numeric digits, and `False` otherwise:**

```python
s = '12343'
print(s.isdigit())
s = '213asd'
print(s.isdigit())
```

- `s.islower()`



- `s.isspace()`
- `s.istitle()`
- `s.isupper()`
