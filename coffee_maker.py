resources = {
    "milk": 3000,
    "water": 5000,
    "coffee": 300,
    "money_present": 500
}

menu = {
    "espresso": {
        "water": 50,
        "coffee": 18,
        "price": 5
    },
    "latte": {
        "water": 200,
        "coffee": 24,
        "milk": 250,
        "price": 10
    },
    "cappuccino": {
        "water": 250,
        "coffee": 24,
        "milk": 100,
        "price": 8
    }
}


def like_to_have():
    output = input("\nWhat would you like to have (espresso/latte/cappuccino): ").lower()

    if output in menu:
        print("\nChecking resources...")
        return sufficient_resource(output)

    elif output == "off":
        return turn_off()

    elif output == "report":
        before_resource_report()
        return True

    else:
        print("Invalid choice. Try again.\n")
        return True


def turn_off():
    print("The machine is turning off...")
    return False


def before_resource_report():
    print("\n---- Current Resources ----")
    for resource, quantity in resources.items():
        if resource in ["milk", "water"]:
            print(f"{resource}: {quantity}ml")
        elif resource == "coffee":
            print(f"{resource}: {quantity}g")
        else:
            print(f"Money: ${quantity}")
    print("----------------------------\n")


def sufficient_resource(choice):
    drink = menu[choice]

    # Check ingredients dynamically
    for ingredient in drink:
        if ingredient != "price":
            if drink.get(ingredient, 0) > resources.get(ingredient, 0):
                print(f"Sorry, not enough {ingredient}.")
                return True

    print("Resources are sufficient.")
    print("Please make payment.")

    if not process_coins(drink["price"]):
        return True

    # Deduct ingredients
    for ingredient in drink:
        if ingredient != "price":
            resources[ingredient] -= drink.get(ingredient, 0)

    print(f"\nHere is your {choice}. Enjoy ☕")
    return True


def process_coins(price):
    print("\nInsert coins:")

    try:
        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        nickels = int(input("How many nickels? "))
        pennies = int(input("How many pennies? "))
    except ValueError:
        print("Invalid input. Transaction cancelled.")
        return False

    total = quarters*0.25 + dimes*0.10 + nickels*0.05 + pennies*0.01
    total = round(total, 2)

    print("Total inserted:", total)

    if total < price:
        print("Sorry, that's not enough money. Money refunded.")
        return False

    change = round(total - price, 2)

    if change > 0:
        print(f"Here is ${change} in change.")

    resources["money_present"] += price
    print("Payment successful.")
    return True