resources = {
    "milk": 3000,
    "water": 5000,
    "coffee": 300,
    "money": 500
}

menu = {
    "espresso": {"water": 50, "coffee": 18, "price": 5},
    "latte": {"water": 200, "coffee": 24, "milk": 250, "price": 10},
    "cappuccino": {"water": 250, "coffee": 24, "milk": 100, "price": 8}
}

coins = {"quarters":0.25, "dimes":0.10, "nickels":0.05, "pennies":0.01}


def report():
    """Display machine resources."""
    units = {"water":"ml","milk":"ml","coffee":"g"}
    print("\nResources:")
    for r,q in resources.items():
        print(f"{r}: {q}{units.get(r,'$')}")


def check_resources(drink):
    """Check if ingredients are available."""
    for item, amount in drink.items():
        if item != "price" and resources.get(item,0) < amount:
            print(f"Sorry, not enough {item}.")
            return False
    return True


def process_payment(price):
    """Handle coin payment."""
    print("\nInsert coins")
    total = sum(int(input(f"{c}: ")) * v for c,v in coins.items())
    total = round(total,2)

    if total < price:
        print("Not enough money. Refunded.")
        return False

    change = round(total - price,2)
    if change:
        print(f"Change: ${change}")

    resources["money"] += price
    return True


def make_coffee(choice):
    """Prepare coffee if resources and payment are valid."""
    drink = menu[choice]

    if not check_resources(drink):
        return

    if not process_payment(drink["price"]):
        return

    for item, amount in drink.items():
        if item != "price":
            resources[item] -= amount

    print(f"Here is your {choice}. Enjoy ")

