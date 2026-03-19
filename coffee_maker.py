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
    print("\nResources:")
    for k, v in resources.items():
        print(f"{k}: {v}{'ml' if k in ('water','milk') else 'g' if k=='coffee' else '$'}")


def process_payment(price):
    try:
        total = round(sum(int(input(f"{c}: ")) * v for c, v in coins.items()), 2)
    except ValueError:
        print("Invalid input.")
        return False

    if total < price:
        print("Not enough money.")
        return False

    if total > price:
        print(f"Change: ${round(total - price, 2)}")

    resources["money"] += price
    return True


def make_coffee(choice):
    drink = menu[choice]

    # single-pass check
    if any(resources.get(i, 0) < a for i, a in drink.items() if i != "price"):
        print("Sorry, not enough resources.")
        return

    if not process_payment(drink["price"]):
        return

    # single-line deduction
    for i, a in drink.items():
        if i != "price":
            resources[i] -= a

    print(f"Here is your {choice}. Enjoy!!!! ")