import quiz_application as QG

print("===== Welcome to the Quiz Game =====\n")

# take user information
QG.get_user_info()

while True:

    print("Game starts here...\n")

    QG.play_quiz()

    again = input("\nDo you want to play again? (yes/no): ").lower()

    if again != "yes":
        print("\nThe system is slowly shutting down...")
        break