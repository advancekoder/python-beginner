# Operators in Python 
## ===============================================
# 1️⃣ Arithmetic Operators
# Arithmetic Operators are Used for math calculations.

#| Operator | Example  | Result               |
#| -------- | -------- | -------------------- |
#| `+`      | `5 + 2`  | `7`                  |
#| `-`      | `5 - 2`  | `3`                  |
#| `*`      | `5 * 2`  | `10`                 |
#| `/`      | `5 / 2`  | `2.5`                |
#| `//`     | `5 // 2` | `2` (floor division) |
#| `%`      | `5 % 2`  | `1` (remainder)      |
#| `**`     | `2 ** 3` | `8` (power)          |

# Exercise: Store two numbers and print their sum, difference, product, quotient, power and remainder
a = 10
b = 3
print(a + b)  # 13
print(a - b)  # 7
print(a * b)  # 30
print(a / b)  # 3.33 (division with decimals)
print(a // b) # 3 (floor division)
print(a % b)  # 1 (remainder)
print(a ** b) # 1000 (10 to the power of 3)
## =============================================

# 2️⃣ Comparison Operators
# These operator are used to compare values. They return True or False.

#| Operator | Example  | Result  |
#| -------- | -------- | ------- |
#| `==`     | `5 == 5` | `True`  |
#| `!=`     | `5 != 3` | `True`  |
#| `>`      | `5 > 3`  | `True`  |
#| `<`      | `5 < 3`  | `False` |
#| `>=`     | `5 >= 5` | `True`  |
#| `<=`     | `5 <= 2` | `False` |

# Exercise: Compare your age with 18 and print the result of the comparison.
age = 16
print(age == 18)  # False (equal to)
print(age != 18)  # True (not equal)
print(age > 18)   # False
print(age < 18)   # True
print(age >= 18)  # False
print(age <= 18)  # True
## =============================================

# 3️⃣ Logical Operators
# The logical operators are used to combine conditions.

#| Operator | Example               | Result  |
#| -------- | --------------------- | ------- |
#| `and`    | `(5 > 3) and (2 > 1)` | `True`  |
#| `or`     | `(5 > 3) or (2 < 1)`  | `True`  |
#| `not`    | `not (5 > 3)`         | `False` |

# Exercise: Check if a number is between 10 and 20 (inclusive)
number = 15
print(number >= 10 and number <= 20)  # True
print(number < 10 or number > 20)     # False
print(not(number > 10))               # False
## ===========================================

#4️⃣ Assignment Operators
# These operators are used to assign values to variables.

#| Operator | Example  | Same as     |
#| -------- | -------- | ----------- |
#| `=`      | `x = 5`  | —           |
#| `+=`     | `x += 3` | `x = x + 3` |
#| `-=`     | `x -= 3` | `x = x - 3` |
#| `*=`     | `x *= 3` | `x = x * 3` |
#| `/=`     | `x /= 3` | `x = x / 3` |

# Exercise: Start with x = 10 and update it using each assignment operator.
x = 10
x += 5   # 15
x -= 3   # 12
x *= 2   # 24
x /= 4   # 6.0
## ============================================

#5️⃣ Membership Operators

# These operators are used to check if something exists in a sequence.

#| Operator | Example            | Result |
#| -------- | ------------------ | ------ |
#| `in`     | `"a" in "cat"`     | `True` |
#| `not in` | `"b" not in "cat"` | `True` |

# Exercise: Check if "Python" contains "on".
print("on" in "Python")       # True
print("cat" not in "Python")  # True

## ================================================

#6️⃣ Identity Operators
# Identity operators are used to check if two variables point to the same object in memory.

#| Operator | Example      | Result                  |
#| -------- | ------------ | ----------------------- |
#| `is`     | `x is y`     | True if same object     |
#| `is not` | `x is not y` | True if not same object |

# Exercise: Create two lists with the same items. Then Check == vs is.
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print(list1 == list2)   # True (same content)
print(list1 is list2)   # False (different objects)
print(list1 is list3)   # True (same object)
print(list1 is not list2) # True

## ================================================

