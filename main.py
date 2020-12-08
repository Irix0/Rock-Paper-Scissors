import random


def clear():
    clear = "\n" * 100
    print(clear)


def number_translation(user_choice):
    while True:
        if user_choice == "rock":
            return 0
            break
        elif user_choice == "paper":
            return 1
            break
        elif user_choice == "scissors":
            return 2
            break
        elif user_choice == "quit":
            "Quitting ..."
            quit()
        else:
            user_choice = input("Please enter a valid choice ! (Rock, Paper, Scissors) : ")


def comparison(user_choice, program_choice):
    global user_points
    global program_points
    if user_choice == program_choice:
        print("Tied game !")
        print("+1 point for both")
        user_points += 1
        program_points += 1
    elif (user_choice == 0 and program_choice == 1) or (user_choice == 1 and program_choice == 2) or (
            user_choice == 2 and program_choice == 0):
        print("Lost!")
        print("+3 point for program")
        program_points += 3
    elif (user_choice == 0 and program_choice == 2) or (user_choice == 1 and program_choice == 0) or (
            user_choice == 2 and program_choice == 1):
        print("Won!")
        print("+3 point for you")
        user_points += 3
    else:
        print("Error")


def display_points(user_points, program_points):
    if user_points > 0 or program_points > 0:
        clear()
        print("-*- Points -*-")
        print("You : ", user_points)
        print("Program : ", program_points)
        print("-*----------*-")
        print("\n " * 6)


def main():
    global user_points
    global program_points
    user_points = 0
    program_points = 0
    choices = ["Rock", "Paper", "Scissors"]
    print("Type quit to quit the game at any moment.")
    while user_points <= 100 or program_points <= 100:
        display_points(user_points, program_points)
        program_choice = random.randint(0, 2)
        user_choice = input("What is your choice ? (" + choices[0] + ", " + choices[1] + ", " + choices[2] + ") ")
        comparison(number_translation(user_choice.lower()), program_choice)


if __name__ == '__main__':
    main()
