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

coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01
}


def report():
    print("\nResources:")
    for k, v in resources.items():
        unit = "ml" if k in ["water", "milk"] else "g" if k == "coffee" else "$"
        print(f"{k}: {v}{unit}")


def check_and_make(choice):
    drink = menu[choice]

    for item, amount in drink.items():
        if item != "price" and resources.get(item, 0) < amount:
            print(f"Sorry, not enough {item}.")
            return

    if not payment(drink["price"]):
        return

    for item, amount in drink.items():
        if item != "price":
            resources[item] -= amount

    print(f"Here is your {choice}. Enjoy ☕")


def payment(price):
    print("\nInsert coins")

    total = sum(
        int(input(f"{coin}: ")) * value
        for coin, value in coins.items()
    )

    total = round(total, 2)

    if total < price:
        print("Not enough money. Refunded.")
        return False

    change = round(total - price, 2)

    if change:
        print(f"Change: ${change}")

    resources["money"] += price
    return True


machine_on = True

while machine_on:

    choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        machine_on = False

    elif choice == "report":
        report()

    elif choice in menu:
        check_and_make(choice)

    else:
        print("Invalid option.")