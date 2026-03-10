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
    """Ask the user which drink they want."""
    choice = input("\nWhat would you like to have (espresso/latte/cappuccino): ").lower()

    if choice in menu:
        print("\nChecking resources...")
        return sufficient_resource(choice)

    elif choice == "report":
        before_resource_report()
        return True

    elif choice == "off":
        return turn_off()

    else:
        print("Invalid choice. Please try again.")
        return True


def turn_off():
    """Turn off the coffee machine."""
    print("The machine is turning off...")
    return False


def before_resource_report():
    """Display current machine resources."""
    print("\n----- Resource Report -----")
    for resource, quantity in resources.items():

        if resource in ["milk", "water"]:
            unit = "ml"
        elif resource == "coffee":
            unit = "g"
        else:
            unit = "$"

        print(f"{resource}: {quantity}{unit}")
    print("----------------------------")


def sufficient_resource(choice):
    """Check if enough resources exist for the selected drink."""

    drink = menu[choice]

    for ingredient, amount in drink.items():
        if ingredient != "price" and resources.get(ingredient, 0) < amount:
            print(f"Sorry, not enough {ingredient}.")
            return True

    print("Resources available.")
    print("Please insert coins.")

    if not process_coins(drink["price"]):
        return True

    make_coffee(choice)
    return True


def process_coins(price):
    """Handle coin input and payment verification."""

    print("\nInsert coins")

    coins = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
        "pennies": 0.01
    }

    total = 0

    for coin, value in coins.items():
        try:
            count = int(input(f"How many {coin}? "))
        except ValueError:
            print("Invalid input. Transaction cancelled.")
            return False

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
    """Deduct ingredients and serve coffee."""

    drink = menu[choice]

    for ingredient, amount in drink.items():
        if ingredient != "price":
            resources[ingredient] -= amount

    print(f"\nHere is your {choice}. Enjoy ")