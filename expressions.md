
# Expressions and operators

[https://realpython.com/python-operators-expressions/]( https://realpython.com/python-operators-expressions/)

**In programming, an operator is usually a symbol or \
combination of symbols that allows you to perform a specific operation. \
This operation can act on one or more operands.**

**Python divides operators in the following groups:**


- **Arithmetic operators**
- **Assignment operators**
- **Comparison operators**
- **Logical operators**
- **Identity operators**
- **Membership operators**
- **Bitwise operators**

## Python Arithmetic Operators

| Operator | Name           | Example |
|----------|----------------|---------|
| +        | Addition       | x + y   |
| -        | Subtraction    | x - y   |
| *        | Multiplication | x * y   |
| /        | Division       | x / y   |
| %        | Modulus        | x % y   |
| **       | Exponentiation | x ** y  |
| //       | Floor division | x // y  |


## Python Assignment Operators

| Operator | Example    | Same As    |
|----------|------------|------------|
| =        | x = 5      | x = 5      |
| +=       | x += 3     | x = x + 3  |
| -=       | x -= 3     | x = x - 3  |
| *=       | x *= 3     | x = x * 3  |
| /=       | x /= 3     | x = x / 3  |
| %=       | x %= 3     | x = x % 3  |
| //=      | x //= 3    | x = x // 3 |
| **=      | x **= 3    | x = x ** 3 |
| &=       | x &= 3     | x = x & 3  |
| \|=      | x \|= 3    | x = x \| 3 |
| ^=       | x ^= 3     | x = x ^ 3  |
| >>=      | x >>= 3    | x = x >> 3 |
| <<=      | x <<= 3    | x = x << 3 |


## Python Comparison Operators

| Operator | Name                     | Example |
|----------|--------------------------|---------|
| ==       | Equal                    | x == y  |
| !=       | Not equal                | x != y  |
| >        | Greater than             | x > y   |
| <        | Less than                | x < y   |
| >=       | Greater than or equal to | x >= y  |
| <=       | Less than or equal to    | x <= y  |


## Python Logical Operators

| Operator | Description                                              | Example               |
|----------|----------------------------------------------------------|-----------------------|
| and      | Returns True if both statements are true                 | x < 5 and  x < 10     |
| or       | Returns True if one of the statements is true            | x < 5 or x < 4        |
| not      | Reverse the result, returns False if the result is true  | not(x < 5 and x < 10) |


## Python Identity Operators

| Operator | Description                                            | Example    |
|----------|--------------------------------------------------------|------------|
| is       | Returns True if both variables are the same object     | x is y     |
| is not   | Returns True if both variables are not the same object | x is not y |

## Python Membership Operators

| Operator | Description                                                                      | Example    |
|----------|----------------------------------------------------------------------------------|------------|
| in       | Returns True if a sequence with the specified value is present in the object     | x in y     |
| not in   | Returns True if a sequence with the specified value is not present in the object | x not in y |


**If the operation involves a single operand, then the operator is unary.**

```python
negative = -274.15
```

**If the operator involves two operands, then the operator is binary.**

```python
subtraction = 5 - 2
```

**Operators provide a quick shortcut for you to manipulate data, \
perform mathematical calculations, compare values, run Boolean tests, \
assign values to variables, and more. \
In Python, an operator may be a symbol, a combination of symbols, \
or a keyword, depending on the type of operator that you’re dealing with.**

```python
4 == 4
True is False
True == 1
False == 0
```

**Boolean or logical operators in Python are keywords rather than signs, \
as you’ll learn in the section about Boolean operators and expressions. \
So, instead of the odd signs like ||, &&, and ! that many other programming languages use, 
Python uses or, and, and not.**

**Using keywords instead of odd signs is a really cool design decision that’s consistent 
with the fact that Python loves and encourages code’s readability.**

**Operators by themselves don’t do much. \
If you use an operator without the required operands, then you’ll get a syntax error. \
So, operators must be part of expressions, which you can build using Python objects as operands. \
An expression is a simple statement that produces and returns a value.**

```python
7 + 5
42 / 2
```

**Note that not all expressions use operators. \
For example, a bare function call is an expression that doesn’t require any operator:**

```python
abs(-7)
7 ** 2
pow(7, 2)
print("Hello World")
```

## The Assignment Operator and Statements

**The assignment operator allows you to assign values to variables. \
Strictly speaking, in Python, this operator makes variables or \
names refer to specific objects in your computer’s memory. \
In other words, an assignment creates a reference to a \
concrete object and attaches that reference to the target variable.**

*Base assignment*
```python
random_string = "some string"
```

*Multiple assignments*
```python
random_string, random_int = "some string", 1
```

*Augmented assignments*
```python
some_int = 1
some_int += 3
```

> **_NOTE:_** Variables in Python do not store values directly. They work with references pointing to objects in memory.

**For more on Python's assignment operator:**
[https://realpython.com/python-assignment-operator/]( https://realpython.com/python-assignment-operator/)

**Assignment statements not only assign a value to a variable \
but also determine the data type of the variable at hand. \
This additional behavior is another important detail to consider in this kind of statement.**

**Because Python is a dynamically typed language, \
successive assignments to a given variable can change the variable’s data type. \
Changing the data type of a variable during a program’s execution is considered \
bad practice and highly discouraged. \
It can lead to subtle bugs that can be difficult to track down.**


## Arithmetic Operators and Expressions in Python

```python
10 / 5
10.0 / 5
```

> **_NOTE:_** The standard division operator (/) always returns a floating-point number, \
> even if the dividend is evenly divisible by the divisor \
> In order to get an integer use the floor division (//) operator.

```python
10 // 5
```

> **_NOTE_** A very common use case for the modulus operator (%) is to find if a number is even or odd

```python
10 % 2 == 0 # True
11 % 2 == 0 # False
```
