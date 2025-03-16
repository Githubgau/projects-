
import tkinter as tk
import random

# Create the main window
root = tk.Tk()
root.title("captcha Generator")
root.geometry("300x150")

# Create a StringVar to store and update the random number
number_var = tk.StringVar()
number_var.set("Click the button to generate a capcha")

# Create a label to display the random number
label = tk.Label(root, textvariable=number_var, font=("Arial", 12))
label.pack(pady=20)

# Function to generate and update a random number
def generate_number():
    a = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789")
    global random_number
    random_number=""
    for i in range(3):
        d=random.choice(a)
        random_number = d+random_number  # Generate a random number between 1 and 100
    number_var.set(f"capcha: {random_number}")
    button.destroy()
    buttons = tk.Button(root,text="submit",command=submit)
    buttons.pack()

for i in range (1):
    tk.Label(root,text="captcha")
    e1=tk.Entry(root)
    label.pack()
    e1.pack()
    break

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Arial", 12))
result_label.pack()

def submit():
    user_input=e1.get()
    if user_input==random_number:
        result_var.set("done")
        
    else:
        result_var.set("wrong")
        button = tk.Button(root, text="Generate capcha", command=generate_number)
        button.pack()



# Create a button to generate a new random number
button = tk.Button(root, text="Generate capcha", command=generate_number)

button.pack()

# Run the application
root.mainloop()
