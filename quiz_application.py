import random
# we are using this as a small dataset for our program but we could also provide big data using
questions = {
    "python": [
        {
            "question": "What does len() do?",
            "options": ["A. Counts items", "B. Deletes items", "C. Adds items", "D. Sorts items"],
            "answer": "A"
        },
        {
            "question": "Which keyword is used to define a function?",
            "options": ["A. func", "B. define", "C. def", "D. function"],
            "answer": "C"
        },
        {
            "question": "What is the output of: print(2**3)?",
            "options": ["A. 6", "B. 8", "C. 9", "D. 5"],
            "answer": "B"
        },
        {
            "question": "Which data type is immutable?",
            "options": ["A. List", "B. Dictionary", "C. Set", "D. Tuple"],
            "answer": "D"
        }
    ],

    "math": [
        {
            "question": "What is 12 + 8?",
            "options": ["A. 18", "B. 20", "C. 22", "D. 24"],
            "answer": "B"
        },
        {
            "question": "What is 15 ÷ 3?",
            "options": ["A. 4", "B. 6", "C. 5", "D. 3"],
            "answer": "C"
        },
        {
            "question": "What is 7 × 9?",
            "options": ["A. 63", "B. 56", "C. 72", "D. 69"],
            "answer": "A"
        },
        {
            "question": "What is the square root of 81?",
            "options": ["A. 8", "B. 9", "C. 7", "D. 6"],
            "answer": "B"
        }
    ],

    "science": [
        {
            "question": "What gas do humans breathe in?",
            "options": ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"],
            "answer": "A"
        },
        {
            "question": "What planet is closest to the Sun?",
            "options": ["A. Earth", "B. Venus", "C. Mercury", "D. Mars"],
            "answer": "C"
        },
        {
            "question": "What is H2O commonly known as?",
            "options": ["A. Hydrogen", "B. Oxygen", "C. Water", "D. Salt"],
            "answer": "C"
        },
        {
            "question": "What force pulls objects toward Earth?",
            "options": ["A. Magnetism", "B. Gravity", "C. Friction", "D. Pressure"],
            "answer": "B"
        }
    ],

    "history": [
        {
            "question": "Who was the first President of India?",
            "options": ["A. Mahatma Gandhi", "B. Jawaharlal Nehru", "C. Dr. Rajendra Prasad", "D. Sardar Patel"],
            "answer": "C"
        },
        {
            "question": "In which year did India gain independence?",
            "options": ["A. 1945", "B. 1947", "C. 1950", "D. 1930"],
            "answer": "B"
        },
        {
            "question": "Who was known as the Iron Man of India?",
            "options": ["A. Bhagat Singh", "B. Subhash Chandra Bose", "C. Sardar Vallabhbhai Patel", "D. Nehru"],
            "answer": "C"
        },
        {
            "question": "The Taj Mahal was built by?",
            "options": ["A. Akbar", "B. Shah Jahan", "C. Aurangzeb", "D. Humayun"],
            "answer": "B"
        }
    ]
}


def personal_info():
    while True:
        print("\n")
        name = input("Enter your name: ")
        e_mail = input("Enter the e-mail: ")

        interest_subject = input("Enter your interests (comma separated)(Math, Science, Python, History): ")
        interest_list = [subject.strip() for subject in interest_subject.split(",")]
        standard = input("Enter the standard you are enrolled: ")

        

        print("\nPlease confirm your details:")
        print("Name:", name)
        print("E-mail:", e_mail)
        print("Interest subject:", interest_subject)
        print("Standard:", standard)

        output = input("\nAre these details correct? (yes/no/quit): ").lower()

        if output == "yes":
            print("\nNow, let's move on to play this interesting game...")
            return True

        elif output == "no":
            print("\nOkay, let's re-enter your details.\n")
            continue   

        elif output == "quit":
            return want_to_quit()

        else:
            print("Invalid input. Please type yes, no, or quit.\n")


def want_to_quit():
    print("The system is slowly shutting down......")
    return False


def predefined_subjects():
    subjects = ["Math", "Science", "Python", "History"]

    print("Available subjects:")
    for subject in subjects:
        print("-", subject)



def start_quiz():
    score = 0
    total_questions = 0

    interest_subject = input("\nEnter again the subjects you want quiz from (comma separated): ").lower()
    interest_list = [subject.strip().lower() for subject in interest_subject.split(",")]

    for subject in interest_list:
        if subject in questions:

            print(f"\n--- {subject.upper()} QUESTIONS ---")

            selected_questions = random.sample(
                questions[subject],
                min(3, len(questions[subject]))
            )

            for q in selected_questions:
                total_questions += 2

                print("\n" + q["question"])
                for option in q["options"]:
                    print(option)

                answer = input("Your answer (A/B/C/D): ").upper()

                if answer == q["answer"]:
                    print("Correct! ")
                    score += 2
                else:
                    print("Wrong Correct answer:", q["answer"])
        else:
            print(f"No questions available for subject: {subject}")

    print("\nQuiz Finished!")
    print("Your Final Score:", score, "/", total_questions)        

print("Welcome to the Quiz Game.....")
predefined_subjects()

power = personal_info()

while power:
    print("Game starts here...")
    start_quiz()
    break