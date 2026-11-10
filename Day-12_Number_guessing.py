import random

def clear_screen():
    print("\033c", end="")

while True:
    print("Welcome to the number guessing game.")
    start_game = input("Do you want to start the game? Type 'y' to start or 'n' to exit: ").strip().lower()

    if start_game == "n":
        print("GoodBye!")
        break
    if start_game != "y":
        print("Invalid input. Please choose between 'y' and 'n'.")
        continue

    random_no = random.randint(1, 100)
    clear_screen()

    while True:
        difficulty = input("Choose the difficulty level: 'easy' or 'hard': ").strip().lower()
        if difficulty in ("easy", "hard"):
            break
        print("Invalid input. Please choose 'easy' or 'hard'.")

    lives = 10 if difficulty == "easy" else 5
    count = 1

    while lives > 0:
        print(f"You have total of {lives} to guess a number.")
        try:
            num = int(input("Guess a number: "))
        except ValueError:
            print("Invalid input. Enter a whole number.")
            continue

        if num == random_no:
            print(f"You guessed it right within {count} {'step' if count == 1 else 'steps'}. The number was {random_no}.")
            break

        lives -= 1
        count += 1
        print("Too high!" if num > random_no else "Too Low!")
    else:
        print(f"You Lose! The number was {random_no}.")
