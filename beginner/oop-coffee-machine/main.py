from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like to drink? ({options}): ").lower()

    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)

        if drink:
            isSufficient = coffee_maker.is_resource_sufficient(drink)
            canMakePayment = money_machine.make_payment(drink.cost)
            
            if isSufficient and canMakePayment:
                coffee_maker.make_coffee(drink)
