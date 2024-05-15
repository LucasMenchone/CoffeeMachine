import sys

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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 5.00
}


def brew_coffee(coffe_type):
    global MENU
    global resources

    ingredients = MENU[coffe_type]["ingredients"]
    coffee_cost = MENU[coffe_type]["cost"]

    if resources["water"] < ingredients["water"]:
        return f"Not enough water on the machine for {coffe_type}"

    if resources["coffee"] < ingredients["coffee"]:
        return f"Not enough coffee on the machine for {coffe_type}"

    if "milk" in ingredients and resources["milk"] < ingredients["milk"]:
        return f"Not enough milk on the machine for {coffe_type}"

    print(f"\nthe cost of a {coffe_type} is ${"{:.2f}".format(coffee_cost)}, and this machine is operated by coins only")
    quarters = float(input("How many quarters ($0.25) you inserted?"))
    dimes = float(input("How many dimes ($0.10) you inserted?"))
    nickles = float(input("How many quarters ($0.05) you inserted?"))
    pennies = float(input("How many quarters ($0.01) you inserted?"))

    money_inserted = (quarters * .25) + (dimes * .10) + (nickles * .05) + (pennies * .01)

    if money_inserted < coffee_cost:
        return "Sorry, not enough money. Money refunded"

    change = money_inserted - coffee_cost

    resources["water"] -= ingredients["water"]
    resources["coffee"] -= ingredients["coffee"]
    resources["money"] += coffee_cost

    if "milk" in ingredients:
        resources["milk"] -= ingredients["milk"]

    if change == 0:
        return f"Here is your {coffe_type}, enjoy!"
    else:
        return f"Here is ${"{:.2f}".format(change)} dollars in change, enjoy your {coffe_type}"


def run():

    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == 'espresso' or choice == 'cappuccino' or choice == 'latte':
        cost_choice = MENU[choice]["cost"]
        print(brew_coffee(choice))

    elif choice == "report":
        print(f"\nWater: {resources["water"]}ml\n"
              f"Milk: {resources["milk"]}ml\n"
              f"Coffee: {resources["water"]}ml\n"
              f"Money: ${resources["money"]}\n")

    elif choice == "off":
        sys.exit()


running_app = True

while running_app:
    run()
