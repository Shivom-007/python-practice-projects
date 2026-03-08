import quiz_application as QG

print("===== Welcome to the Quiz Game =====\n")

# show available subjects
QG.show_subjects()

# take user information
QG.get_user_info()

while True:

    print("\nGame starts here...\n")

    QG.play_quiz()

    again = input("\nDo you want to play again? (yes/no): ").lower()

    if again != "yes":
        print("\nThe system is slowly shutting down...")
        break