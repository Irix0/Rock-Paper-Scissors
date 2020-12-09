from tkinter import *
import ui_game_components as gc

# Window settings
game_window = Tk()
game_window.title("Rock, Paper, Scissors")
game_window.geometry("720x480")
game_window.minsize(360, 320)
game_window.iconbitmap("iconbitmap.ico")
game_window.config(background='#212121')

# Prepare variabletext
global status_var
global computer_points
global user_points
status_var = StringVar()
computer_points_var = IntVar()
user_points_var = IntVar()

# Create points system
user_points = gc.Points()
computer_points = gc.Points()


def status_change(a):
    if a == "won":
        status_var.set("You won!")
    elif a == "lost":
        status_var.set("You lost ...")
    elif a == "tie":
        status_var.set("Tie!")

    computer_points_var.set(computer_points.get_points())
    user_points_var.set(user_points.get_points())


def rock_command():
    status = gc.rock(user_points, computer_points)
    status_change(status)
    # print("Rock Command used")
    return status


def paper_command():
    status = gc.paper(user_points, computer_points)
    status_change(status)
    # print("Paper command used")
    return status


def scissors_command():
    status = gc.scissors(user_points, computer_points)
    status_change(status)
    # print("Scissors command used")
    return status


def game_ui():
    # Rock, Paper or Scissors question
    upper_frame = Frame(game_window, bg="#212121")
    question = Label(upper_frame, text="Rock, Paper or Scissors ?", font=("Segoe UI", 30), bg="#212121", fg="#d4d4d5")
    question.pack()
    upper_frame.pack(expand=YES)

    # Points and status
    status_frame = Frame(game_window, bg="#212121")

    status_var.set("Choose an object !")
    status_label = Label(status_frame, font=("Segoe UI", 30), bg="#212121", fg="#d4d4d5", textvariable=status_var)
    status_label.grid(row=2, column=0)

    user_points_static = Label(status_frame, text="Your points:", font=("Segoe UI", 30), bg="#212121", fg="#d4d4d5")
    user_points_label = Label(status_frame, textvariable=user_points_var, font=("Segoe UI", 30), bg="#212121", fg="#d4d4d5")
    user_points_static.grid(row=0, column=0, sticky=E)
    user_points_label.grid(row=0, column=1, sticky=E)

    computer_points_static = Label(status_frame, text="Computer points:", font=("Segoe UI", 30), bg="#212121", fg="#d4d4d5")
    computer_points_label = Label(status_frame, textvariable=computer_points_var, font=("Segoe UI", 30), bg="#212121", fg="#d4d4d5")
    computer_points_static.grid(row=1, column = 0, sticky=E)
    computer_points_label.grid(row=1, column=1, sticky=E)

    status_frame.pack(expand=YES)

    # Buttons Rock Paper and Scissors
    buttons_frame = Frame(game_window, bg="#212121")
    rock_button = Button(buttons_frame, text="Rock", command=rock_command)
    paper_button = Button(buttons_frame, text="Paper", command=paper_command)
    scissors_button = Button(buttons_frame, text="Scissors", command=scissors_command)

    rock_button.grid(row=0, column=0)
    paper_button.grid(row=0, column=1)
    scissors_button.grid(row=0, column=2)
    buttons_frame.pack(expand=YES)

    game_window.mainloop()


if __name__ == '__main__':
    game_ui()
