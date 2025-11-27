import tkinter as tk
from tkinter import messagebox

def add_pair():
    key = key_entry.get().strip()
    value = value_entry.get().strip()

    if key == "" or value == "":
        messagebox.showwarning("Missing Input", "Please enter both key and value.")
        return

    dictionary[key] = value
    key_entry.delete(0, tk.END)
    value_entry.delete(0, tk.END)


def stop_and_show():
      formatted_dict = "\n".join(f"{key}: {value}" for key, value in dictionary.items())
      messagebox.showinfo("Dictionary Contents", formatted_dict)
      GUI.destroy()



GUI = tk.Tk()
GUI.title("Assignment 7 GUI 😜")
GUI.geometry("400x200")

dictionary = {}


tk.Label(GUI, text="Enter 🎹").pack(pady=5)
key_entry = tk.Entry(GUI, width=30)
key_entry.pack()

tk.Label(GUI, text="Enter 🎶").pack(pady=5)
value_entry = tk.Entry(GUI, width=30)
value_entry.pack()


button_frame = tk.Frame(GUI)
button_frame.pack(pady=10)

stop_button = tk.Button(button_frame, text="🛑✋🏼✋🏼🛑", command=stop_and_show)
stop_button.pack(side="left", padx=5)

add_button = tk.Button(button_frame, text="➕➕➕➕", command=add_pair)
add_button.pack(side="left", padx=5)

GUI.mainloop()
