# If-Else statements 
# Before we delve into the If-Else statement, lets look at what kind of statement are they
# They are called Conditional Statement.

# WHAT IS CONDITIONAL STATEMENT 
''' 
A Conditional Statement lets your program decide whether or not to run certain code 
depending on a condition being true or false.
* It's like giving your computer a Yes/No question: "If this happens, do that".
'''
# (a) The If statement
# if condition: 
    # code runs only if condition is True

# Notes: 
"""
* If: This keyword tells python we are checking a condition.
* condition: any expression that returns True or False.
* colon(:): tells python that the following indented lines belong to the if block
* indentation: in python, indentation defines the code block usually 4 spaces.
"""
# E.g. 1:
age = 20

if age >= 18:
    print("You are an adult.")

"""
Explanation:
* age >= 18: This checks if age is greater than or equal to 18.
* since 20 >= 18: Is True, python runs print("You are an adult.")
* Output will display: You are an adult.
"""

# E.g. 2: Condition not met
temperature = 25

if temperature > 30:
    print("It's hot today!")

"""
Explanation:
* temperature > 30 is False (25 > 30? No).
* so nothing happens - python skips the code inside the if block.
"""

"""
Notes:
* The if clock only runs when the condition is True.
* You can have only one if in a block, but combine it later with else, 
  or elif for more cases
* You can compare numbers, strings, or even combine multiple conditions
  using and, or. 
"""

# (b) If...else statement
'''
An if...else statement allows your program to run one block of code if the 
condition is True, and a different block if the condition is False.

if condition: 
        # code runs if condition is true
    else: 
        # code runs if condition is false
'''

# E.g. 1: Age Check
age = 16

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# E.g. 2: Check for Even or Odd
number = 7

if number%2 == 0:
    print("Even number")
else:
    print("Odd number")


# (c) If...elif...else
'''
if...elif...else lets you check multiple conditions in sequence.
* The program checks the first if.
* If it's False, it checks the elif (which means else if)
* If none of them are True, the else block runs

if condition 1:
    runs if condition 1 is True
    elif condition 2:
        runs if condition 1 is False AND condition 2 is True.
        elif condition 3:
            runs if previous conditions are False AND condition 3 is True.
else:
    runs if all conditions are False
'''

# E.g. 1: Grading System
score = 78

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")

else:
    print("Grade: F")

'''
Explanation: 
* The elif condition checks from top to bottom 
* finds first condition False(78 >= 90 - False)
* second condition False(78 >= 80 - False)
* Third condition returns True(78 >= 70 - True), so Grade C is printed.
* If all conditions were False, the else block would run.
* Once a True condition is found, the rest are skipped.
'''

# E.g. 2: Temperature Check
temperature = 32

if temperature >= 35:
    print("It's very hot!")
elif temperature >= 25:
    print("It's warm.")
elif temperature >= 15:
    print("It's cool.")
else:
    print("It's cold.")

# E.g. 3: Number Comparison
number = 10

if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")   

# Notes:
"""
* You can have multiple elif blocks to check many conditions.
* The first True condition runs, and the rest are ignored.  
* If no conditions are True, the else block runs.
* You can use any expression that evaluates to True or False.   
"""

# (d) Nested if statements
''' 
A nested if means an if inside another if.
You can nest if statements inside each other to check multiple conditions.
It is useful when you need to check a condition only if another condition is True.

if condition 1:
    # code runs if condition 1 is True
    if condition 2:
        # code runs if both condition 1 and condition 2 are True
    else:
        # code runs if condition 1 is True but condition 2 is False
else:
    # code runs if condition 1 is False
'''

# E.g. 1: Checking Age and Citizenship
age = 20
citizen = True

if age >= 18:
    if citizen:
        print("You eligible to vote.")
    else:
        print("You must be a citizen to vote.")
else:
    print("You must be at least 18 years old to vote.")

# E.g. 2: Grading System with Distinction
score = 90

if score >= 60:
    if score >= 80:
        print("Pass with Distinction")
    elif score >= 70:
        print("Pass with Credit")
    elif score >= 60:
            print("Pass")
    else:
        print("Fail")

# Explanation:
'''
* The outer if checks if the student passed (>= 60).
* If yes, it checks again if the score is really high (>= 80 and prints "Pass with Distinction").
* If the first condition is False, it checks if the score is >= 70 and prints "Pass with Credit".
* If the score is >= 60, it prints "Pass".
* If the first conditions is False, it prints "Fail".
'''

