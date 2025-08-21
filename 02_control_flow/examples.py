import random  

# Computer chooses a random number between 1 and 10
secret_number = random.randint(1, 10)

print("🎲 Welcome to the Guessing Game!")
print("Guess the number (between 1 and 10).")

while True:  # infinite loop until user guesses right
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("🎉 Correct! You guessed the number.")
        break  # exit loop when guessed correctly
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
# ========================================================



balance = 5000  # starting balance

print("🏦 Welcome to Python Bank ATM")

while True:
    print("\n--- Menu ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Choose an option (1/2/3/4): ")

    if choice == "1":
        print("💰 Your balance is:", balance)

    elif choice == "2":
        amount = int(input("Enter amount to deposit: "))
        balance += amount
        print("✅ Deposited! New balance:", balance)

    elif choice == "3":
        amount = int(input("Enter amount to withdraw: "))
        if amount > balance:
            print("❌ Insufficient funds!")
            continue  # skip to menu again
        balance -= amount
        print("✅ Withdrawal successful. New balance:", balance)

    elif choice == "4":
        print("👋 Thank you for banking with us!")
        break  # exit ATM program

    else:
        print("⚠️ Invalid choice. Please try again.")

# ===========================================================


import time

print("🧠 Welcome to the Advanced Python Quiz Game!")
print("Choose a difficulty level: Easy, Medium, Hard")
difficulty = input("Your choice: ").lower()

# Questions database (with difficulty levels)
questions = {
    "easy": [
        {
            "question": "What is the capital of France?",
            "options": ["A. London", "B. Paris", "C. Rome", "D. Madrid"],
            "answer": "b"
        },
        {
            "question": "Who won the 2022 FIFA World Cup?",
            "options": ["A. France", "B. Brazil", "C. Argentina", "D. Germany"],
            "answer": "c"
        }
    ],
    "medium": [
        {
            "question": "Which team did Argentina defeat in the 2022 final?",
            "options": ["A. Spain", "B. France", "C. England", "D. Brazil"],
            "answer": "b"
        },
        {
            "question": "Who was the top scorer of the 2022 World Cup?",
            "options": ["A. Messi", "B. Neymar", "C. Mbappe", "D. Ronaldo"],
            "answer": "c"
        }
    ],
    "hard": [
        {
            "question": "Which year did France first win the World Cup?",
            "options": ["A. 1998", "B. 2002", "C. 1986", "D. 1994"],
            "answer": "a"
        },
        {
            "question": "Who scored the winning penalty for Argentina in 2022 final?",
            "options": ["A. Messi", "B. Montiel", "C. Dybala", "D. Di Maria"],
            "answer": "b"
        }
    ]
}

# Select questions based on difficulty
selected_questions = questions.get(difficulty, questions["easy"])

score = 0
time_limit = 10  # seconds per question

for q in selected_questions:
    print("\n" + q["question"])
    for opt in q["options"]:
        print(opt)

    start_time = time.time()
    answer = input(f"Your answer (A/B/C/D), you have {time_limit} seconds: ").lower()
    elapsed_time = time.time() - start_time

    if elapsed_time > time_limit:
        print("⏰ Time’s up! No points for this question.")
        continue  # skip to next question

    if answer == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong! The correct answer was:", q["answer"].upper())

print("\n🎉 Game Over!")
print(f"Your final score is {score} out of {len(selected_questions)}")

# Save score to file
with open("scores.txt", "a") as file:
    file.write(f"Difficulty: {difficulty.capitalize()} | Score: {score}/{len(selected_questions)}\n")

print("📂 Your score has been saved in 'scores.txt'")

# ============================================================



