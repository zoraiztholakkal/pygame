import random
def get_user_choice():
    user_choice = str(input("Enter your choice(rock,paper or scissors): ")).lower()
    while user_choice  not in ['rock','paper','scissors']:
        print("invalid choice.please enter rock,paper,or scissors.")
       user_choice = input ("Enter your choice(rock,paper or scissors): ").lower()
    return user_choice
