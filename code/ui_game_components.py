from random import *


# ROCK = 0, PAPER = 1, SCISSORS = 2
class Points:
    def __init__(self):
        self.points = 0

    def get_points(self):
        return self.points

    def set_points(self, a):
        self.points = a

    def add_points(self, a):
        self.points += a


def random(x=1, y=150):
    value = randint(x,y)
    if value <= y / 3:
        return 0
    elif y / 3 < value <= (y / 3) * 2:
        return 1
    elif (y / 3) * 2 < value <= y:
        return 2
    else:
        raise ValueError("Debugging : else called in random function", value)


def rock(user, computer):
    computer_choice = random()
    print("Computer random choice :", computer_choice)
    if computer_choice == 0:
        user.add_points(1)
        computer.add_points(1)
        return "tie"
    elif computer_choice == 1:
        computer.add_points(3)
        return "lost"
    elif computer_choice == 2:
        user.add_points(3)
        return "won"
    else:
        raise ValueError("Debugging : else called in rock function", computer_choice)


def paper(user, computer):
    computer_choice = random()
    print("Computer random choice :", computer_choice)
    if computer_choice == 0:
        user.add_points(3)
        return "won"
    elif computer_choice == 1:
        user.add_points(1)
        computer.add_points(1)
        return "tie"
    elif computer_choice == 2:
        computer.add_points(3)
        return "lost"
    else:
        raise ValueError("Debugging : else called in paper function", computer_choice)


def scissors(user, computer):
    computer_choice = random()
    print("Computer random choice :", computer_choice)
    if computer_choice == 0:
        computer.add_points(3)
        return "lost"
    elif computer_choice == 1:
        user.add_points(3)
        return "won"
    elif computer_choice == 2:
        user.add_points(1)
        computer.add_points(1)
        return "tie"
    else:
        raise ValueError("Debugging : else called in scissors function", computer_choice)
