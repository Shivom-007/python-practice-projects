resources = {
    "milk": 3000,
    "water": 5000,
    "coffee": 300,   
    "money_present": 500
}


def like_to_have():
    ''' This function takes input from user and based on that particular input
        it do as written in this file.'''
    output = input("\nWhat would you like to have (espresso/latte/cappuccino): ").lower()

    if output in ["espresso", "latte", "cappuccino"]:
        print("Processing the data about what you have opted.")
        print("\nChecking whether there are enough resources.....")
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
    '''This function makes the machine to "turn off" itself by returning False.'''
    print("The machine is slowly turning off.......")
    return False


def before_resource_report():
    '''This function checks the quantity of resources present in the machine.'''
    for resource, quantity in resources.items():
        if resource in ["milk", "water"]:
            print(f"{resource}: {quantity}ml")
        elif resource == "coffee":
            print(f"{resource}: {quantity}g")
        else:
            print(f"Money: ${quantity}")


def sufficient_resource(choice):
    ''' checks whether their are enough resources or not depending on the choice.'''
    menu = {
        "espresso": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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

    drink = menu[choice]

    for ingredient in ["water", "milk", "coffee"]:
        if drink[ingredient] > resources[ingredient]:
            print(f"Sorry, not enough {ingredient}.")
            print("Sorry for the inconvenience ")
            return True   

    print("There are enough resources .")
    print("The process to make coffee will start after payment .")

    price = drink["price"]

    if not process_coins(price):
        return True

    print("The process to make coffee will start ")

    for ingredient in ["water", "milk", "coffee"]:
        resources[ingredient] -= drink[ingredient]

    print(f"Here is your {choice}. Enjoy! ")
    return True

  

def process_coins(price):
    '''Calculate the money received and give change.'''
    print("Insert coins ")

    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))

    total = quarters*0.25 + dimes*0.10 + nickels*0.05 + pennies*0.01

    print("Total inserted:", total)

    if total < price:
        print("Sorry, that's not enough money. Money refunded.")
        return False   

    change = round(total - price, 2)

    if change > 0:
        print(f"Here is ${change} in change.")

    resources["money_present"] += price
    print("Payment successful ")
    return True