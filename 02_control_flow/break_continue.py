# Break and Continue in loops 
# Control flow in a jiffy is the order in which instructions in a program are executed.
# Control flow lets you tell python; 
# * "Do this only if a condition is true."
# * "Repeat this action several times."
# * "Stop if something happens."

# For better understanding, we can divide them into 3 main types:
# 1. Conditional Statements: (a) if (b) if...else (c) if...elif...else & (d) nested if
# 2. Loops: (a) for loop (b) while loop
# 3. Loop Control Statements: (a) break (b) continue (c) pass

# In here, we want to look at break and continue;
# (a) break statement: This is used to exit a loop early - even if the loop condition hasn't finished

# E.g STOP at 3
for i in range (1, 10):
    if i == 3:
        break
    print(i)

# output: 1, 2
# The loop stops as soon as i equals 3.

# (b) continue statement: This statement skips the current iteration and moves to the next one.

# E.g:
for i in range (1, 6):
    if i == 3:
        continue
    print(i)

# Output: 1, 2, 4, 5, 
# Here, 3 is skipped, but the loop continues for the rest.

# (c) while loop with break: This statement is often used when waiting for a condition.

# E.g:
while True:
    name = input("Enter your name (or 'quit' to stop): ")
    if name == "quit":
        break
    print("Hello,", name)

# The loop will keep running until the user types quit.

