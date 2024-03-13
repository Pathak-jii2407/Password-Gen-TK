import tkinter as tk
import random
import string
import pyperclip

lower_letters = [letter for letter in string.ascii_lowercase]
upper_letters = [letter for letter in string.ascii_uppercase]
numbers = [str(number) for number in range(10)]
symbols = ['_', '@']
all_characters = lower_letters + upper_letters + numbers + symbols


def generate_password():
    password = ''
    while len(password) != 10:
        random_character = random.choice(all_characters)
        password += str(random_character)
    return password


def display_and_return_password():
    generated_password = generate_password()
    result_label.config(text=f"{generated_password} (copied)")
    root.after(5000, lambda: text_change(generated_password))

def text_change(password):
    result_label.config(text=f"Generated Password:")
    pyperclip.copy(password) #copy on keyboard
    return result_label

root = tk.Tk()
root.title("Password Generator")
result_label = tk.Label(root, text="Generated Password: ")
roll_button = tk.Button(root, text="Click Here", command=display_and_return_password)

result_label.pack(pady=10)
roll_button.pack(pady=10)

root.mainloop()
