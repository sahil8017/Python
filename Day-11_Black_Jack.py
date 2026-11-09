import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
dealer_cards = []

def calc(hand):
  score = sum(hand)
  aces = hand.count(11)
  while score > 21 and aces > 0:
    score -= 10
    aces -= 1
  return score
def clear_screen():
    print("\033c",end="")
while True:
    start_game = input("Do you want to start the game? Type 'y' to start or type 'n' to exit: ").lower()
    if start_game not in ["y","n"]:
        print("Invalid input. Please choose between 'y' and 'n'.")
        continue
    if start_game == "y":
        clear_screen()
    else:
        print("GoodBye!")
        exit()
    user_cards.clear()
    dealer_cards.clear()
    for _ in range(2):
        user_cards.append(random.choice(cards))
        dealer_cards.append(random.choice(cards))
    print(f"Your Cards: {user_cards}, total: {calc(user_cards)}.\n\tDealer's first card: {dealer_cards[0]}")
    while calc(user_cards) < 21:  # no point asking once the player has 21 or busted
        stand_hit = input("Do you want to add another card? Type 'y' to add another card or type 'n' to stand: ").lower()
        if stand_hit not in ["y","n"]:
            print("Invalid input. Please choose between 'y' and 'n'.")
            continue
        if stand_hit == "y":
            user_cards.append(random.choice(cards))
            print(f"Your Cards: {user_cards}, total: {calc(user_cards)}.\n\tDealer's first card: {dealer_cards[0]}")
        else:
            break
    if calc(user_cards) <= 21:
        while calc(dealer_cards) < 17:
            dealer_cards.append(random.choice(cards))

    user_score = calc(user_cards)
    dealer_score = calc(dealer_cards)
    user_natural = (user_score == 21 and len(user_cards) == 2)
    dealer_natural = (dealer_score == 21 and len(dealer_cards) == 2)

    # always reveal both hands at the end
    print(f"\nFinal -> Your Cards: {user_cards}, total: {user_score}.\n\tDealer's cards: {dealer_cards}, total: {dealer_score}")

    if user_natural and dealer_natural:
        print("Push!")
    elif user_natural:
        print("You Win!")
    elif dealer_natural:
        print("Dealer Wins!")
    elif user_score > 21:
        print("You Lose!")
    elif dealer_score > 21:
        print("You Win!")
    elif user_score > dealer_score:
        print("You Win!")
    elif user_score < dealer_score:
        print("Dealer Wins!")
    else:
        print("Push!")