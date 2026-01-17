import tkinter as tk
import random
secret_number = None
attempts_left = 0
current_mode = ""
def start_easy():
    global secret_number, attempts_left, current_mode
    secret_number = random.randint(1, 20)
    attempts_left = 3
    current_mode = "Easy"
    show_game_screen("Easy Level (1-20)", attempts_left)
def start_hard():
    global secret_number, attempts_left, current_mode
    secret_number = random.randint(1, 100)
    attempts_left = 5
    current_mode = "Hard"
    show_game_screen("Hard Level (1-100)", attempts_left)
def check_guess():
    global attempts_left
    guess = guess_entry.get()
    if not guess.isdigit():
        result_label.config(text="Invalid input! Enter a number.")
        return
    guess = int(guess)
    if guess < secret_number:
        result_label.config(text="Higher!")
    elif guess > secret_number:
        result_label.config(text="Lower!")
    else:
        result_label.config(text=f"🎉 Correct! Number was {secret_number}")
        return
    attempts_left -= 1
    attempts_label.config(text=f"Attempts Left: {attempts_left}")
    if attempts_left == 0:
        result_label.config(text=f"❌ Game Over! Number was {secret_number}")
def go_back():
    game_frame.pack_forget()
    main_menu_frame.pack()
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x300")
root.resizable(False, False)
main_menu_frame = tk.Frame(root)
title_label = tk.Label(main_menu_frame, text="Number Guessing Game", font=("Arial", 16))
title_label.pack(pady=20)
easy_btn = tk.Button(main_menu_frame, text="Easy Mode (1-20)", width=20, command=start_easy)
easy_btn.pack(pady=5)
hard_btn = tk.Button(main_menu_frame, text="Hard Mode (1-100)", width=20, command=start_hard)
hard_btn.pack(pady=5)
exit_btn = tk.Button(main_menu_frame, text="Exit", width=20, command=root.quit)
exit_btn.pack(pady=20)
main_menu_frame.pack()
game_frame = tk.Frame(root)

level_label = tk.Label(game_frame, text="", font=("Arial", 14))
level_label.pack(pady=10)

attempts_label = tk.Label(game_frame, text="", font=("Arial", 12))
attempts_label.pack()

guess_entry = tk.Entry(game_frame, width=10)
guess_entry.pack(pady=10)

check_btn = tk.Button(game_frame, text="Check Guess", command=check_guess)
check_btn.pack()

result_label = tk.Label(game_frame, text="", font=("Arial", 12))
result_label.pack(pady=10)

back_btn = tk.Button(game_frame, text="Back to Menu", command=go_back)
back_btn.pack(pady=10)

def show_game_screen(level_text, attempts):
    main_menu_frame.pack_forget()
    level_label.config(text=level_text)
    attempts_label.config(text=f"Attempts Left: {attempts}")
    result_label.config(text="")
    guess_entry.delete(0, tk.END)
    game_frame.pack()


root.mainloop()
