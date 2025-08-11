# Data types in Python 
# Lesson 1: Python Data Types
# Data types tell Python what kind of value something is.

# 1️⃣ STRING (Text)
# Strings are used for words, sentences, or any text inside quotes.
name = "Charles"
print("Name:", name)                  # Prints the word Charles
print("Uppercase:", name.upper())     # .upper() changes all letters to BIG letters
print("First letter:", name[0])       # Indexing [0] means "first character"

# 2️⃣ INTEGER (Whole numbers)
# Integers are numbers without decimal points.
age = 30
year_of_birth = 2025 - age            # Math works on integers
print("Year of birth:", year_of_birth)

# 3️⃣ FLOAT (Decimal numbers)
# Floats are numbers with decimal points.
price = 19.99
print("Price:", price)
print("Half price:", price / 2)       # Division gives a float (even if it’s whole)

# 4️⃣ BOOLEAN (True or False)
# Booleans are like yes/no answers: True or False
is_active = True
is_tired = False
print("Active status:", is_active)
print("Tired status:", is_tired)

# 5️⃣ LIST (Ordered collection)
# Lists can store many items in one variable, and they can change.
fruits = ["apple", "banana", "cherry"]
print("First fruit:", fruits[0])      # Lists start at index 0
fruits.append("orange")               # Adds "orange" to the end
print("Updated list:", fruits)

# 6️⃣ TUPLE (Unchangeable list)
# Tuples are like lists but you cannot change them after creation.
coordinates = (10, 20)
print("Coordinates:", coordinates)
# coordinates[0] = 15  # ❌ This will give an error because tuples can't change

# 7️⃣ DICTIONARY (Key-Value pairs)
# Dictionaries store information in "label:value" format.
person = {
    "name": "Charles",
    "age": 30,
    "country": "Nigeria"
}
print("Person's name:", person["name"])  # Access using the key "name"

# 8️⃣ NONE (No value)
# None means "nothing here" or "empty".
nothing = None
print("Nothing is:", nothing)
