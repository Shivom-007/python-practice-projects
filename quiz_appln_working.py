import quiz_application as QG

print("===== Welcome to the Quiz Game =====\n")

# show available subjects
QG.predefined_subjects()

# take user information
power = QG.get_user_info()

while power:

    print("\nGame starts here...\n")

    QG.play_quiz()

    again = input("\nDo you want to play again? (yes/no): ").lower()

    if again == "no":
        print("\nThe system is slowly shutting down...")
        power = False