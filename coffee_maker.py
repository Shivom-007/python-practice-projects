resources = {
    "milk": 3000,
    "water": 5000,
    "coffee": 300,
    "money_present": 500
}

menu = {
    "espresso": {"water": 50, "coffee": 18, "milk": 0, "price": 5},
    "latte": {"water": 200, "coffee": 24, "milk": 250, "price": 10},
    "cappuccino": {"water": 250, "coffee": 24, "milk": 100, "price": 8}
}


def like_to_have():
    """Ask user what drink they want."""
    choice = input("\nWhat would you like (espresso/latte/cappuccino): ").lower()

    actions = {
        "report": before_resource_report,
        "off": turn_off
    }

    if choice in menu:
        return sufficient_resource(choice)

    elif choice in actions:
        result = actions[choice]()
        return result if result is not None else True

    else:
        print("Invalid choice. Try again.")
        return True


def turn_off():
    """Turn off the coffee machine."""
    print("Machine is turning off...")
    return False


def before_resource_report():
    """Display machine resources."""
    print("\n------ Resource Report ------")
    for resource, quantity in resources.items():
        units = {"water": "ml", "milk": "ml", "coffee": "g"}
        unit = units.get(resource, "$")
        print(f"{resource}: {quantity}{unit}")
    print("-----------------------------")


def sufficient_resource(choice):
    """Check resources before making drink."""

    drink = menu[choice]

    for ingredient, amount in drink.items():
        if ingredient == "price":
            continue

        if resources.get(ingredient, 0) < amount:
            print(f"Sorry, not enough {ingredient}.")
            return True

    print("Resources available. Please insert coins.")

    if process_coins(drink["price"]):
        make_coffee(choice)

    return True


def process_coins(price):
    """Handle coin payment."""

    coin_values = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
        "pennies": 0.01
    }

    total = 0

    print("\nInsert coins:")

    for coin, value in coin_values.items():
        while True:
            try:
                count = int(input(f"How many {coin}? "))
                if count < 0:
                    print("Please enter a positive number.")
                    continue
                break
            except ValueError:
                print("Invalid input. Enter a number.")

        total += count * value

    total = round(total, 2)

    if total < price:
        print("Sorry, that's not enough money. Money refunded.")
        return False

    change = round(total - price, 2)

    if change > 0:
        print(f"Here is ${change} in change.")

    resources["money_present"] += price
    print("Payment successful.")
    return True


def make_coffee(choice):
    """Deduct ingredients and serve drink."""

    drink = menu[choice]

    for ingredient, amount in drink.items():
        if ingredient != "price":
            resources[ingredient] -= amount

    print(f"\nHere is your {choice}. Enjoy ")