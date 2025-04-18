import tkinter as tk
import random
import time
from threading import Thread

def roll_dice():
    def game_logic():
        roll_button.config(state=tk.DISABLED)
        result_label.config(text="Rolling...")
        time.sleep(1)

        num1 = random.randint(1, 6)
        num2 = random.randint(1, 6)
        num3 = random.randint(1, 6)

        dice_label.config(text=f"{num1}, {num2}, {num3}")
        time.sleep(1)

        if num1 == num2 and num2 == num3:
            result = "You won the lottery!"
        elif num1 == num2 or num2 == num3 or num1 == num3:
            result = random.choice(['Close!', 'Almost!'])
        else:
            result = random.choice(['Try again!', "You'll win the next one!"])

        result_label.config(text=result)
        roll_button.config(state=tk.NORMAL)

    Thread(target=game_logic).start()

def quit_game():
    num1 = random.randint(1, 5)
    num2 = random.randint(1, 5)
    num3 = random.randint(1, 5)
    if num1 == num2 and num2 == num3:
        result_label.config(text="You would've won that one!")
    else:
        result_label.config(text="Come again next time!")
    roll_button.config(state=tk.DISABLED)


root = tk.Tk()
root.title("Dice Roller")
root.geometry("300x250")

title_label = tk.Label(root, text="Lottery", font=("Helvetica", 20))
title_label.pack(pady=10)

dice_label = tk.Label(root, text="Ready?", font=("Helvetica", 16))
dice_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

roll_button = tk.Button(root, text="Roll the Dice", command=roll_dice, font=("Helvetica", 12))
roll_button.pack(pady=5)

root.mainloop()
