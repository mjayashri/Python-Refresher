from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

is_off = False
while not is_off:
    coffee_maker.report()
    input_drink = input(f"what would you like to drink? {menu.get_items()}")
    if input_drink == "off":
        is_off = True
        continue
    elif input_drink == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(input_drink)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
