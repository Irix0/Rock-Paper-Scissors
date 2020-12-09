from Archives.game_components import *
from game_ui import *


# Create main window
main_window = Tk()
main_window.title("Rock, Paper, Scissors")
main_window.geometry("720x480")
main_window.minsize(360, 320)
main_window.iconbitmap("iconbitmap.ico")
main_window.config(background='#212121')

# Main Static UI
title_frame = Frame(main_window, bg="#212121")

main_title = Label(title_frame, text="Rock, Paper, Scissors", font=("Segoe UI", 30), bg="#212121", fg="#d4d4d5")
main_subtitle = Label(title_frame, text="Click on Start to begin.", font=("Segoe UI", 20), bg="#212121", fg="#d4d4d5")
main_title.pack()
main_subtitle.pack()
# Start button
start_button = Button(title_frame, text="Start", font=("Segoe UI", 20), bg="#d4d4d5", fg="#212121", command=game_ui)
start_button.pack(pady=25)

title_frame.pack(expand=YES)

# Show main window
main_window.mainloop()
