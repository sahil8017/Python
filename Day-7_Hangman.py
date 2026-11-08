import random

stages = [
    r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''',
    r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''',
    r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',
    r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
    r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
    r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
    r'''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

logo = r'''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/
'''

print(logo)

words = ["sahil", "surya", "chandra"]

random_no = random.randint(0,2)
random_word = words[random_no]

display = ["-"]*len(random_word)

lives = 6
guessed = []

while True:
    guess = input("Guess a letter:\n")
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet.")
        continue
    if guess in guessed:
        print(f"You already guessed {guess}. Guess a new letter.")
        continue

    for i in range(len(random_word)):
        if random_word[i] == guess:
            display[i] = guess

    guessed.append(guess)        
    
    result = "".join(display)        
    
    if guess not in random_word:
        print(f"You guessed the wrong letter. Try again.")
        lives -= 1

    if "-" not in result:
        print("You Won!")
        break

    print(stages[lives])
    print(result)

    if lives == 0:
        print(f"Game Over. The word is {random_word}")
        break

