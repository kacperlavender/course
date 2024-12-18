import random

lowest = 1
highest = 10

answer = random.randint(lowest, highest)
guesses = 0

running = True

print("Python number guessing game")
print(f"select number between {lowest} and {highest}")

while running:
    guess = input("enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest or guess > highest:
            print("\n that numer is out of the range")
            print(f"select number between {lowest} and {highest}")
        elif guess < answer:
            print("\ntoo low, try again")
        elif guess > answer:
            print("\ntoo high, try again")
        elif guess == answer:
            print(f"\nyou guessed the number, it was {answer}, congratulations")
            running = False
    else:
        print("\nInvalid guess")
        print(f"select number between {lowest} and {highest}")