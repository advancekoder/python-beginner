city = "Los Angeles"
year = 2025
print(f"I live in {city} and the year is {year}")


# ================================
# If you see an error with the message "The ampersand (&) character is not allowed."
# It means you are trying to run this code in a context that does not support f-strings. or
# you are using the python terminal instead of power shell.
# Make sure to run this in a Python script file or a compatible environment.
# Ensure to use ctrl + . = *toggle the terminal*
# ================================

# =================================
# Exercise 1: Basic Variables in Python
language = "Python"
experience_months = 6
print(f"I have been learning {language} for {experience_months} months.")
# ==================================
# Exercise 2: Update values
status = "Learning"
status = "Practicing"
print(f"Current status: {status}")
# ==================================
# Exercise 3: Numbers and types
projects_completed = 3
hours_per_week = 10.5
print(f"Projects completed: {projects_completed} (type: {type(projects_completed)})")
print(f"Hours per week: {hours_per_week} (type: {type(hours_per_week)})")
# ==================================
# Exercise 4: Combine strings
first_name = "Charles"
last_name = "Effanga"
full_name = first_name + " " + last_name
print(f"Full name: {first_name} {last_name}")
# ===================================
# Exercise 5: Challenge
name = input("What is your name? ")
age = input("How old are you? ")
print(f"Hello {name}, you are {age} years old.")
# ===================================

## ===================================
## DATA TYPES EXERCISES
## ===================================
## 1. String Practice
name = "Charles"
print("Name:", name)
print("Uppercase:", name.upper())
print("lowercase:", name.lower())
## ===================================

## 2. Integer and Float
# -- Integer Practice--
age = 32
print("Age:", age, "Type:", type(age))
# Calculate year you will turn 100
current_year = 2025
year_turn_100 = current_year + (100 - age)
print("You will turn 100 in the year:", year_turn_100)
## ===========================================

# -- Float Practice --
price = 49.99
print("Price:", price, "Type:", type(price))
# Adding tax to the price
tax_rate = 0.07 # 7% tax
final_price = price + (price * tax_rate )
print("Final price with tax:", final_price)
## ===================================

## 3. Boolean 
like_python = True
print("Do you like Python?", like_python)
# Example of using boolean in a sentence 
if like_python:
    print("Great! Python is awesome!")
else:
    print("Not really my thing.")

## ===================================

## 4. List Practice
# Create a list of your 5 favorite foods.
favorite_foods = ["Wheat", "Semovita", "Beans", "Rice", "Yam"]
print("Favorite Foods:", favorite_foods)
# Add a new food to the list
favorite_foods.append("Pasta")
print("Updated Favorite Foods:", favorite_foods)
# Access the first food in the list
print("First favorite food:", favorite_foods[0])
# =============================================

## 5. Tuple Practice
# Create a tuple of your 3 favorite colors
favorite_colors = ("Red", "Blue", "Green")
print("Favorite Colors:", favorite_colors)
# Attempting to change a value in the tuple will raise an error
# favorite_colors[0] = "Yellow"  # This will give an error because tuples are immutable
print("Second favorite color:", favorite_colors[1])  
# ============================================

## 6. Dictionary Practice
# Store your name, age, and favorite hobby in a dictionary
my_info = {
    "name": "Charles",
    "age": 30,
    "favorite_hobby": "Coding"
}
print("My Info:", my_info)
# Print each value using its key
print("Name:", my_info["name"])
print("Age:", my_info["age"])
print("Favorite Hobby:", my_info["favorite_hobby"])
# =================================================

## 7. None Practice
# Create a variable that is None
empty_variable = None
print("Empty Variable:", empty_variable)
# Check if the variable is None
if empty_variable is None:
    print("This variable is empty.")
# ===============================================

### ADDITIONAL DATA TYPES
# For more advanced usage, here are additional data types in Python:
# 8️⃣ COMPLEX NUMBER (Real and Imaginary)
# Complex numbers have a real part and an imaginary part.
complex_number = 3 + 4j
print("Complex Number:", complex_number)
print("Real part:", complex_number.real)
print("Imaginary part:", complex_number.imag)
# Complex numbers are used in advanced mathematics and engineering.
# =============================================

# 9️⃣ SET (Unique collection)
# Sets are unordered collections of unique items.
# Sets are like lists but they only keep unique items and are unordered.
unique_numbers = {1, 2, 3, 4, 5}
print("Unique numbers:", unique_numbers)
# Adding a number to the set
unique_numbers.add(6)
print("Updated unique numbers:", unique_numbers)
# Removing a number from the set
unique_numbers.remove(2)
print("After removing 2:", unique_numbers)
# ================================================

# 10️⃣ FROZEN SET (Unchangeable set)
# Frozen sets are like sets but you cannot change them after creation.
frozen_numbers = frozenset([1, 2, 3, 4])
print("Frozen set:", frozen_numbers)
# frozen_numbers.add(5)  # ❌ This will give an error because frozen sets can't change
# ===============================================

# 11️⃣ BYTE (Binary data)
# Bytes are used to store binary data, like images or files.
byte_data = b"Hello"
print("Byte data:", byte_data)
# =================================================

# 12️⃣ BYTEARRAY (Mutable byte data)
# Bytearrays are like bytes but you can change them.
byte_array = bytearray(b"Hello")
print("Bytearray data:", byte_array)
byte_array[0] = 74  # Change first byte to 'H'
print("Updated Bytearray data:", byte_array)
# Note: Bytearrays are useful when you need to modify binary data.
# but to see the actual change of character (as string) in this case use '.decode()'
print("Updated Bytearray data:", byte_array.decode())
# =================================================

# 13️⃣ Range
# Range is a special type used for creating a sequence of numbers.
number_range = range(5)
print("Range from 0 to 4:", list(number_range))  # Convert range to a list for display
# ==================================================

## ===================================
## OPERATORS EXERCISES
## ===================================

# 1. Arithmetic Challenge 
mango_price = 120
banana_price = 50

total_cost = (3 * mango_price) + (2 * banana_price)
print("Total cost:", total_cost)

# ==================================================

# 2. Comparison Challenge 

age = int(input("Enter your age: "))
print("You are an adult:", age >= 18)

# ==================================================

# 3. Logical Challenge 

age = 25
has_card = True

can_enter = (age >= 18 and age <= 35) and has_card
print("Can enter the club:", can_enter)

# ==================================================

# 4. Membership Challenge 

word = "Elephant"
print("e" in word.lower())

# ==================================================

# 5. Identity Challenge 

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print("a is b:", a is b)  # False
print("a is c:", a is c)  # True

# ==================================================

## ===================================
## COMMENT EXERCISES
## ===================================

# 1. Single-line comment 
# This is my name 
name = "Charles"
print("Name:", name)
## ===================================

# 2. Inline comment
a = 5 # This is the value of a
b = 7 # This is the value of b
total = a + b  # Adding a and b
print("Total:", total) # Result of addition
## ===================================

# 3. Multi-line comment
age = 32
print(f"You are an adult:", age >= 18)
''' 
This program checks if a person is an adult 
and prints the result.
'''
## ===================================

# 4. Real-world example

"""
This program simulates a simple quiz game.
It asks the user questions and checks their answers.
"""
"""
WHO WANTS TO BE A MILLIONAIRE
------------------------------
Rules:
- The player chooses a question (1 to 4).
- Each choice has a different question.
- Answer correctly to win $1000
- The game ends afterwards.
This docstring is a multi-line comment for game instruction.
"""
# Step 1: Ask the player to choose a Question
# Using int() to convert the input string to a number
question_number = int(input("Choose a question (1/2/3/4): "))

# Step 2: Store the prize ammount in a variable
prize_amount = 1000 # Inline comment showing the prize amount

# Step 3: Decide which question to ask based on the player's choice
if question_number == 1:
    # Question 1
    print("Question 1: Which team won the 2022 FIFA World Cup?")
    print("A) Brazil\nB) Argentina\nC) France\nD) Germany")
    answer = input("Your answer: ").strip().upper() # Strip whitespace and convert to uppercase
    if answer == "B":
        print(f"✅ Correct! You win ${prize_amount}!") 
    else:
        print("❌ Wrong! The correct answer was A) Argentina.")

elif question_number == 2:
    # Question 2
    print("Question 2: Which team lost the 2022 FIFA World Cup Final?")
    print("A) Brazil\nB) Argentina\nC) France\nD) Germany")
    answer = input("Your answer: ").strip().upper()
    if answer == "C":
        print(f"✅ Correct! You win ${prize_amount}!")
    else:
        print("❌ Wrong! The correct answer was C) France.")

elif question_number == 3:
    # Question 3
    print("Question 3: Who scored the most goals in the 2022 FIFA World Cup?")
    print("A) Messi\nB) Mbappe\nC) Neymar\nD) Ronaldo")
    answer = input("Your answer: ").strip().upper()
    if answer == "B":
        print(f"✅ Correct! You win ${prize_amount}!")
    else:
        print("❌ Wrong! The correct answer was B) Mbappe.")

elif question_number == 4:
    # Question 4
    print("Question 4: Which country hosted the 2022 FIFA World Cup?")
    print("A) Saudi Arabia\nB) USA\nC) Qatar\nD) Kuwait")
    answer = input("Your answer: ").strip().upper()
    if answer == "C":
        print(f"✅Correct! You win ${prize_amount}")
    else:
        print("❌ Wrong! The correct answer was C) Qatar.")

else:
    # Invalid choice handling
    print("That's not a valid question number!") # This is shown if the number isn't 1-4
# ================================================
# End of exercises