resources = {
    "milk": 3000,
    "water": 5000,
    "coffee": 300,
    "money_present": 500
}

menu = {
    "espresso": {"water": 50, "coffee": 18, "price": 5},
    "latte": {"water": 200, "coffee": 24, "milk": 250, "price": 10},
    "cappuccino": {"water": 250, "coffee": 24, "milk": 100, "price": 8}
}


def like_to_have():
    choice = input("\nWhat would you like (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        print("Machine turning off...")
        return False

    if choice == "report":
        print_report()
        return True

    if choice not in menu:
        print("Invalid choice.")
        return True

    if not check_resources(choice):
        return True

    if not process_payment(menu[choice]["price"]):
        return True

    make_coffee(choice)
    return True


def print_report():
    print("\n---- Resources ----")
    for item, amount in resources.items():
        if item in ["water", "milk"]:
            print(f"{item}: {amount}ml")
        elif item == "coffee":
            print(f"{item}: {amount}g")
        else:
            print(f"Money: ${amount}")


def check_resources(choice):
    drink = menu[choice]

    for ingredient, required in drink.items():
        if ingredient == "price":
            continue
        if resources.get(ingredient, 0) < required:
            print(f"Sorry, not enough {ingredient}.")
            return False

    return True


def process_payment(price):
    print("\nInsert coins")

    coins = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
        "pennies": 0.01
    }

    total = 0

    for coin, value in coins.items():
        total += int(input(f"How many {coin}? ")) * value

    total = round(total, 2)

    if total < price:
        print("Sorry, not enough money. Refunded.")
        return False

    change = round(total - price, 2)

    if change > 0:
        print(f"Here is ${change} change.")

    resources["money_present"] += price
    return True


def make_coffee(choice):
    drink = menu[choice]

    for ingredient, amount in drink.items():
        if ingredient != "price":
            resources[ingredient] -= amount

    print(f"\nHere is your {choice}. Enjoy Coffee.....")