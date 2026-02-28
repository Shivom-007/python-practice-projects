import random
import quiz_application as QG


print(f"Welcome to the Quiz Game....." )
print("Enter you details here:")
name = input("Name: ")
e_mail = input("email: ")
interest_subject = input("interest_subject: ")
standard = input("standard: ")
print("\n")


power = True
while power:
    power = QG.personal_info(name, e_mail, interest_subject, standard)