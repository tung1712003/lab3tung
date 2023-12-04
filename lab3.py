import tkinter as tk
from tkinter import ttk
import random
import pygame

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 630

def close(window, music):
    music.stop()
    window.destroy()

def clear(entry, key_label):
    entry.delete(0, tk.END)  # Clear the Entry widget
    key_label.config(text="")   # Clear the result label

def generate_key(hex_part):
    dec_part = int(hex_part, 16)
    key = f"{dec_part // 1000:03d}-{dec_part % 1000:03d}-{random.randint(0, 999):03d} {random.randint(0, 99):02d}"
    return key

def generate_button_clicked(hex_entry, key_label):
    hex_part = hex_entry.get()
    key = generate_key(hex_part)
    key_label.config(text=key)


# Create the main window and set its properties
window = tk.Tk()
window.title("Keygen")
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
bg_img = tk.PhotoImage(file='robot.png')

lbl_bg = tk.Label(window, image=bg_img)
lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(window)
frame.place(relx=0.5, rely=0.5, anchor='center')

# Create and place widgets
hex_label = ttk.Label(frame, text="Enter HEX part:")
hex_label.grid(column=0, row=0, padx=10, pady=15)

hex_entry = ttk.Entry(frame)
hex_entry.grid(column=5, row=0, padx=10, pady=15)

lbl_roots = ttk.Label(frame, text='The Result Key is:')
lbl_roots.grid(column=0, row=3, padx=10, pady=15)

key_label = ttk.Label(frame, text="")
key_label.grid(column=5, row=3, padx=10, pady=15)

generate_button = ttk.Button(frame, text="Generate Key", command=lambda: generate_button_clicked(hex_entry, key_label))
generate_button.grid(column=0, row=6, padx=10, pady=15)

btn_exit = ttk.Button(frame, text='Exit', command=lambda: close(window, pygame.mixer.music))
btn_exit.grid(column=5, row=6, padx=10, pady=15)

btn_clear = ttk.Button(frame, text='Clear', command=lambda: clear(hex_entry, key_label))
btn_clear.grid(column=3, row=6, padx=10, pady=15)


# Initialize Pygame mixer
pygame.mixer.init()
# Load and play background music (replace 'background_music.mp3' with your file)
pygame.mixer.music.load('background_music.mp3')
pygame.mixer.music.play(-1)  # -1 means loop indefinitely


# Start the main event loop
window.mainloop()
