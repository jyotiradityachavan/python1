import tkinter as tk


root = tk.Tk()
root.title("Simple Tkinter GUI")
root.geometry("300x200")


label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 16))
label.pack(pady=20)


def change_text():
    label.config(text="Button Clicked!")


button = tk.Button(root, text="Click Me", command=change_text)
button.pack(pady=10)


root.mainloop()
