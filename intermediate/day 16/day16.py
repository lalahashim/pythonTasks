from day16_menu import Menu, MenuItem
from day16_cofeemaker import CoffeeMaker
from day16_moneymachine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True
while is_on:
    options = menu.get_items()
    clients_choice = input(f"What would you like? {options}: ")
    if clients_choice == "off":
        is_on = False
    elif clients_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(clients_choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
