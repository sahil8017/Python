import random

print("Welcome to Password Generator!")

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

numbers = "0123456789"

symbols = "!#$%&()*+-_=@?"

def password_generation(n_letters, n_numbers, n_symbols):
    
    password = []
    
    for i in range(n_letters):
        password.append(random.choice(letters))

    for i in range(n_numbers):
        password.append(random.choice(numbers))

    for i in range(n_symbols):
        password.append(random.choice(symbols))        

    random.shuffle(password)
    result = "".join(password)
    print(f"Your Password: {result}")    

def main():
    n_letters = int(input("How many letters would you like in your passwords?\n"))
    n_numbers = int(input("How many numbers would you like in your passwords?\n"))
    n_symbols = int(input("How many sumbols would you like in your passwords?\n"))

    password_generation(n_letters, n_numbers, n_symbols)

main()