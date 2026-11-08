logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _b| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                       .-------------.
                      /_______________\
'''

print(logo)
print("Welcome to the secret auction program.")

def clear_screen():
    print("\033c",end="")

bids = {}

while True:
    name = input("Enter your name: ")
    amount = int(input("Enter the bid amount: $"))
    
    bids[name] = amount

    continue_bidding = input("Continue bidding? Type 'yes' or 'no': ")

    if continue_bidding == "yes":
        clear_screen()
        continue
    else:
        max_bid = max(bids.values())
        winnner = max(bids, key=bids.get)

        print(f"The highest bid is ${max_bid}")
        print(f"The winner is {winnner}")
        break