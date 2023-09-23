from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money = MoneyMachine()
c_maker = CoffeeMaker()


def machine():
    options = menu.get_items()
    choice = input(f"What would you like? {options}:")
    if choice == "off":
        print("See you!")
        return 0
    elif choice == "report":
        c_maker.report()
        money.report()
        machine()
    else:
        drink = menu.find_drink(choice)
        if c_maker.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            c_maker.make_coffee(drink)
            machine()
        else:
            machine()


machine()
