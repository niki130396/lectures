
# 1. Create a new variable (using the assignment operator).

new_string = "test"

new_float = 5.2

# 2. Create a statement using the following expression: a + 5 - b (you need to define a and b).

a = 32
b = 8

print(f"#2: {a + 5 - b}")

# 3. What is the difference between the `/` operator and the `//` operator?

a = 15
b = 6

print(f"#3.1: {b/a}")  # used for integer division

print(f"#3.2: {a//b}")  # used for floor division

# 4. Consider the following statements:
x = 10.0
y = (x < 100.0) and isinstance(x, float)
# What is the value of y? -> True

if y == (x < 100.0) and isinstance(x, float):
    print(f"#4: {y}")
else:
    print("check")

# 5. Write an expression (or statement) to find the square root of 9.

print(f"#5: {9**0.5}")

# 6. Write a statement to:
# Create a variable x with the value 100
x = 100

# Increase the value of x fivefold using an augmented assignment operator
x *= 5
print(f"#6: {x}")

# 7. Cast the string defined below into upper case.

s = "this should be upper case"
s = s.upper()
print(f"#7: {s}")

# 8. Make sure the below string starts with a capital letter.

x = "this should start with a capital letter."
x = x.capitalize()

print(f"#8: {x}")

# 9. Swap the cases of the letters of the string below - upper case letters become lower case and vice versa.

z = "tHIS STRING NEEDS IT'S CASE SWAPPED."

z = z.swapcase()

print(f"#9: {z}")