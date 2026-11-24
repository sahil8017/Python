MENU = {
    "espresso": {
        "ingredients": {"water": 50, "milk": 0,"coffee": 18},
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.00,
    }
}

# print(MENU["espresso"]["ingredients"]["water"])
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def is_resource_sufficient(order_resources):
    for item in order_resources:
        if resources[item]  <= order_resources[item]:
            return False
    return True

def process_coins():
    print("Please insert coins.")
    total = int(input("How many quaters?: "))*0.25
    total += int(input("How many dimes?: "))*0.1
    total += int(input("How many nickles?: "))*0.05
    total += int(input("How many pennies?: "))*0.01
    return round(total,2)

def is_transaction_successful(user_payment, drink_cost):
    if user_payment > drink_cost:
        change = user_payment - drink_cost
        print(f"Here is ${change} as change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, but that's not enough money. Money refunded")
        return False
def make_coffee(drink_name, drink_ingredients):
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here is your {drink_name}, enjoy.")    
profit = 0
while True:
    choice = input("What would you like to order: (espresso | latte | cappuccino)?: ").strip().lower()
    if choice == "off":
        break
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Milk: {resources['milk']}ml")            
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])