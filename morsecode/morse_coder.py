import tkinter as tk
from tkinter import messagebox
import time
import winsound  # For sound feedback on Windows
import pyperclip  # For copying Morse code to clipboard

# Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ' ': ' '  # Space for visual pause
}

# Morse Code Converter
def text_to_morse(text):
    return ' '.join(MORSE_CODE_DICT.get(char.upper(), '') for char in text)

# Copy to Clipboard
def copy_to_clipboard():
    text = entry.get().strip()
    if not text:
        messagebox.showerror("Error", "Please enter text before copying.")
        return
    morse_code = text_to_morse(text)
    pyperclip.copy(morse_code)
    messagebox.showinfo("Copied!", "Morse code copied to clipboard.")

# Visual & Audio Feedback Logic
def show_morse_code():
    text = entry.get().strip()
    if not text:
        messagebox.showerror("Error", "Please enter a valid text.")
        return

    morse_code = text_to_morse(text)
    result_label.config(text=f"Morse Code: {morse_code}")

    speed_choice = speed_var.get()
    speed = 0.5 if speed_choice == 'Slow' else 0.3 if speed_choice == 'Normal' else 0.15

    def blink_morse():
        for symbol in morse_code:
            if symbol == '.':
                canvas.itemconfig(circle, fill='green')  # Dot → Green
                winsound.Beep(1000, 300)  # Beep for dot
                window.update()
                time.sleep(speed)
            elif symbol == '-':
                canvas.itemconfig(circle, fill='red')    # Dash → Red
                winsound.Beep(1000, 700)  # Beep for dash
                window.update()
                time.sleep(speed * 2)
            else:
                canvas.itemconfig(circle, fill='black')  # Space → Pause
                window.update()
                time.sleep(speed)

            canvas.itemconfig(circle, fill='white')  # Reset color
            window.update()
            time.sleep(speed)

    window.after(100, blink_morse)  # Ensures smooth color transition

# Tkinter GUI Setup
window = tk.Tk()
window.title("Morse Code Visualizer")
window.geometry("550x600")
window.configure(bg="#2C3E50")

title_label = tk.Label(window, text="Morse Code Visualizer", font=("Arial", 28, "bold"), bg="#2C3E50", fg="#ECF0F1")
title_label.pack(pady=10)

entry = tk.Entry(window, font=("Arial", 20), width=30)
entry.pack(pady=20)

speed_var = tk.StringVar(value="Normal")
speed_label = tk.Label(window, text="Select Speed:", font=("Arial", 14), bg="#2C3E50", fg="#ECF0F1")
speed_label.pack()
speed_menu = tk.OptionMenu(window, speed_var, "Slow", "Normal", "Fast")
speed_menu.pack(pady=5)

button_frame = tk.Frame(window, bg="#2C3E50")
button_frame.pack(pady=10)

show_button = tk.Button(button_frame, text="Show Morse Code", command=show_morse_code, bg="#3498DB", fg="white", font=("Arial", 14, "bold"))
show_button.grid(row=0, column=0, padx=5)

copy_button = tk.Button(button_frame, text="Copy to Clipboard", command=copy_to_clipboard, bg="#27AE60", fg="white", font=("Arial", 14, "bold"))
copy_button.grid(row=0, column=1, padx=5)

result_label = tk.Label(window, text="", font=("Arial", 16), bg="#2C3E50", fg="#ECF0F1")
result_label.pack(pady=10)

canvas = tk.Canvas(window, width=200, height=200, bg="#2C3E50", highlightthickness=0)
canvas.pack(pady=20)

circle = canvas.create_oval(50, 50, 150, 150, fill="white")

footer_label = tk.Label(window, text="Created by Yash Sharma", font=("Arial", 12), bg="#2C3E50", fg="#BDC3C7")
footer_label.pack(pady=10)

window.mainloop()
