import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

rock_paper_scissors = [rock, paper, scissor]


def rock_paper_scissor(user_choice):
    random_number = random.randint(0,2)
    computer_choice = rock_paper_scissors[random_number]

    print(f"Computer choose:\n{computer_choice}")

    if user_choice == random_number:
        return "It's a draw!"
    elif (user_choice == 0 and random_number == 2) or (user_choice == 1 and random_number == 0) or (user_choice == 2 and random_number == 1):
        return "You win!"
    else:
        return "You lose!"
def main():
    while True:
        try:
            user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
            if user_choice < 0 or user_choice > 2:
                print("Invalid Choice! Please choose in between 0, 1 and 2.")
                continue
            print(f"You Said:{rock_paper_scissors[user_choice]}")
            results = rock_paper_scissor(user_choice)       
            print(results)

            while True:
                continue_game = input("Do you want to continue the game? Type 'yes' or 'no'.\n").lower()

                if continue_game == "yes":
                    break
                elif continue_game == "no":
                    return
                else:
                    print("Please choose between 'yes' and 'no'.")
        except ValueError:
            print("Only whole numbers are allowed.")

main()       