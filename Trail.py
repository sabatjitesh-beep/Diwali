import tkinter as tk

def check_name():
    name = entry.get()
    if name == "Jitesh":
        result.set("You are a true hero")
    elif name == "Jyotika":
        result.set("You have a devil in your heart")
    elif name == "Jeshika":
        result.set("You are too stubborn, always trying to pick a fight with others!!!!")
    else:
        result.set("You are always right")

# GUI setup
root = tk.Tk()
root.title("Name Personality Checker")

tk.Label(root, text="Enter your name:").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Check", command=check_name).pack()
result = tk.StringVar()
tk.Label(root, textvariable=result, fg="blue").pack()

root.mainloop()
