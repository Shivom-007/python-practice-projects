import coffee_maker as cm

while True:

    choice = input("\nChoose drink (espresso/latte/cappuccino) or 'report'/'off': ").lower()

    if choice == "off":
        print("Machine turned off.")
        break

    elif choice == "report":
        cm.report()

    elif choice in cm.menu:
        cm.make_coffee(choice)

    else:
        print("Invalid option.")