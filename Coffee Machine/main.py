MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def total_coins():
    coin_values = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01,
    }
    total = sum(coin_values[coin] * int(input(f"{coin}?")) for coin in coin_values)
    return round(total, 2)


def check_resources(drink):
    ingredients = MENU[drink]["ingredients"]
    for item, amount in ingredients.items():
        if RESOURCES[item] < amount:
            print(f"Sorry, not enough {item}.")
            return False
    return True


def make_coffee(drink):
    ingredients = MENU[drink]["ingredients"]
    for item, amount in ingredients.items():
        RESOURCES[item] -= amount
    RESOURCES["money"] += MENU[drink]["cost"]
    print(f"Here is your {drink}. Enjoy!")


def coffee_machine():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if choice == "off":
            print("See you later.")
            break
        elif choice == "report":
            for item, amount in RESOURCES.items():
                print(f"{item.capitalize()}: {amount}")
        elif choice in MENU:
            if check_resources(choice):
                money = total_coins()
                if money == MENU[choice]["cost"]:
                    make_coffee(choice)
                elif money > MENU[choice]["cost"]:
                    change = round(money - MENU[choice]["cost"], 2)
                    make_coffee(choice)
                    print(f"Here is ${change} in change.")
                else:
                    print("Sorry, that's not enough money. Money refunded.")
            else:
                continue
        else:
            print("Invalid choice. Please choose from espresso, latte, cappuccino, report, or off.")


coffee_machine()
