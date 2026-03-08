import random

QUESTIONS = {
    "python": [
        {"question": "What does len() do?",
         "options": ["A. Counts items", "B. Deletes items", "C. Adds items", "D. Sorts items"],
         "answer": "A"},

        {"question": "Which keyword is used to define a function?",
         "options": ["A. func", "B. define", "C. def", "D. function"],
         "answer": "C"},

        {"question": "What is the output of: print(2**3)?",
         "options": ["A. 6", "B. 8", "C. 9", "D. 5"],
         "answer": "B"},

        {"question": "Which data type is immutable?",
         "options": ["A. List", "B. Dictionary", "C. Set", "D. Tuple"],
         "answer": "D"},

        {"question": "What is the output of print(type([]))?",
         "options": ["A. <class 'list'>", "B. <class 'tuple'>", "C. <class 'dict'>", "D. <class 'set'>"],
         "answer": "A"}
    ],

    "math": [
        {"question": "What is 12 + 8?",
         "options": ["A. 18", "B. 20", "C. 22", "D. 24"],
         "answer": "B"},

        {"question": "What is 15 ÷ 3?",
         "options": ["A. 4", "B. 6", "C. 5", "D. 3"],
         "answer": "C"},

        {"question": "What is 7 × 9?",
         "options": ["A. 63", "B. 56", "C. 72", "D. 69"],
         "answer": "A"},

        {"question": "What is the square root of 81?",
         "options": ["A. 8", "B. 9", "C. 7", "D. 6"],
         "answer": "B"}
    ],

    "science": [
        {"question": "What gas do humans breathe in?",
         "options": ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"],
         "answer": "A"},

        {"question": "What planet is closest to the Sun?",
         "options": ["A. Earth", "B. Venus", "C. Mercury", "D. Mars"],
         "answer": "C"},

        {"question": "What is H2O commonly known as?",
         "options": ["A. Hydrogen", "B. Oxygen", "C. Water", "D. Salt"],
         "answer": "C"},

        {"question": "What force pulls objects toward Earth?",
         "options": ["A. Magnetism", "B. Gravity", "C. Friction", "D. Pressure"],
         "answer": "B"}
    ],

    "history": [
        {"question": "Who was the first President of India?",
         "options": ["A. Mahatma Gandhi", "B. Jawaharlal Nehru", "C. Dr. Rajendra Prasad", "D. Sardar Patel"],
         "answer": "C"},

        {"question": "In which year did India gain independence?",
         "options": ["A. 1945", "B. 1947", "C. 1950", "D. 1930"],
         "answer": "B"},

        {"question": "Who was known as the Iron Man of India?",
         "options": ["A. Bhagat Singh", "B. Subhash Chandra Bose", "C. Sardar Patel", "D. Nehru"],
         "answer": "C"},

        {"question": "The Taj Mahal was built by?",
         "options": ["A. Akbar", "B. Shah Jahan", "C. Aurangzeb", "D. Humayun"],
         "answer": "B"}
    ]
}


def show_subjects():
    print("\nAvailable Subjects:")
    print(", ".join(subject.capitalize() for subject in QUESTIONS))


def get_user_info():
    print("\nEnter your details")
    name = input("Name: ")
    input("Email: ")
    input("Standard/Class: ")
    print(f"\nHello {name}! Let's start the quiz.")


def ask_questions(subjects):
    score = total = 0

    for subject in subjects:
        if subject not in QUESTIONS:
            print(f"\nNo questions available for {subject}")
            continue

        print(f"\n--- {subject.upper()} QUIZ ---")

        for q in random.sample(QUESTIONS[subject], min(3, len(QUESTIONS[subject]))):
            total += 1
            print("\n" + q["question"])

            for option in q["options"]:
                print(option)

            ans = input("Your answer (A/B/C/D): ").upper()

            if ans == q["answer"]:
                print("Correct!")
                score += 2
            else:
                print("Wrong! Correct answer:", q["answer"])

    return score, total


def play_quiz():
    show_subjects()

    subjects = [s.strip() for s in input("\nChoose subjects (comma separated): ").lower().split(",")]

    score, total = ask_questions(subjects)

    print(f"\nQuiz Finished\nScore: {score} / {total*2}")


def main():
    print("===== Welcome to the Quiz Game =====")

    get_user_info()

    while True:
        play_quiz()

        if input("\nPlay again? (yes/no): ").lower() != "yes":
            print("Thanks for playing!")
            break



