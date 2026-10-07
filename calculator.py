import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("350x500")

# Display
display = tk.Entry(
    root,
    font=("Arial", 28),
    justify="right",
    bd=10
)
display.pack(fill="x", padx=10, pady=15, ipady=10)


# Functions
def press(value):
    display.insert(tk.END, value)


def clear():
    display.delete(0, tk.END)


def delete():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])


def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


# Button area
button_frame = tk.Frame(root)
button_frame.pack(expand=True, fill="both", padx=5, pady=5)


# Buttons
buttons = [
    ["C", "⌫", "(", ")"],
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]


for r, row in enumerate(buttons):

    for c, value in enumerate(row):

        if value == "C":
            command = clear

        elif value == "⌫":
            command = delete

        elif value == "=":
            command = calculate

        else:
            command = lambda x=value: press(x)

        button = tk.Button(
            button_frame,
            text=value,
            font=("Arial", 18),
            command=command
        )

        button.grid(
            row=r,
            column=c,
            sticky="nsew",
            padx=3,
            pady=3
        )


# Make buttons expand
for i in range(4):
    button_frame.columnconfigure(i, weight=1)

for i in range(5):
    button_frame.rowconfigure(i, weight=1)


root.mainloop()