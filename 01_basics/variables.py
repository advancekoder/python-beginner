# Variables in Python 
"""
Python Variables - Beginner Lesson (clear, no-fluff explanation for adults)

A variable is a name that stores a value. Think of it as a labeled container:
instead of repeating a value throughout your code, store it once and reuse it.
"""

# --- Basic assignment ---
name = "Alice"          # store a text value (string)
print("name:", name)    # output: name: Alice

# --- Update a variable ---
name = "Bob"            # the previous value ("Alice") is replaced
print("updated name:", name)  # output: updated name: Bob

# --- Numbers ---
age = 30                # integer
height = 1.75           # float (decimal)
print(f"age: {age} (type: {type(age)})")
print(f"height: {height} (type: {type(height)})")

# --- Multiple assignment ---
x, y, z = 1, 2, 3
print("x, y, z =", x, y, z)

# --- Assign same value to multiple names ---
a = b = c = "Python"
print("a, b, c =", a, b, c)

# --- Combining strings ---
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name      # concatenation
print("Full name:", full_name)
# Modern and more readable: f-strings (Python 3.6+)
print(f"Full name (f-string): {first_name} {last_name}")

# --- Swapping values (clean and pythonic) ---
x, y = 10, 20
print("before swap:", x, y)
x, y = y, x
print("after swap:", x, y)

# --- Variable naming rules and best practices ---
# - Use descriptive names: user_name is better than u or n
# - Use lower_case_with_underscores for variables (PEP8)
# - Names must start with a letter or underscore, not a number
# - Avoid reserved words like 'class', 'def', 'if', etc.

# Example showing name rules
_user_count = 5   # valid but leading underscore implies "internal" use
# 2nd_user = 10   # invalid: can't start with a number (this line would crash if uncommented)

# ================================
# Challenge (try it yourself)
# ================================
# 1) Create a variable called 'city' and set it to your city name (example: "Los Angeles")
# 2) Create a variable called 'year' and store the current year (example: 2025)
# 3) Print both variables in one clear sentence using an f-string:
#    Example expected output: I live in Los Angeles and the year is 2025
#
# Hint:
# city = "Los Angeles"
# year = 2025
# print(f"I live in {city} and the year is {year}")
