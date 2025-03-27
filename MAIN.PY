import tkinter as tk
from tkinter import ttk
import random
import apti as a
import ds as d
import dbms as dbms
import oos as o

root = tk.Tk()
root.geometry("1600x900")  
root.title(" PRACTICE QUESTION")

# Set default module
z = a  

def queans():
    global question, option1, option2, option3, option4

    # Update question before displaying
    selected_value = combobox.get()  
    dd = options.index(selected_value)  

    # Assign module based on selection
    if dd == 1:
        z = a
        z.qb()
    elif dd == 2:
        z = d
        z.d()
    elif dd == 3:
        z = dbms
        z.dbms()
    elif dd == 4:
        z = o  
        z.o()

    # Destroy previous widgets (if exist)
    try:
        question.destroy()
        option1.destroy()
        option2.destroy()
        option3.destroy()
        option4.destroy()
    except:
        pass  

    # Create new question and options
    question = tk.Text(root, width=80, height=5, font=("Arial", 18), bg="lightgray", fg="black")
    question.place(x=450, y=100)
    question.insert("1.0", z.question1[z.select])
    question.config(state="disabled")

    option1 = tk.Button(root, height=5, width=40, bg="skyblue", text=z.d1)
    option1.place(x=550, y=300)
    option2 = tk.Button(root, height=5, width=40, bg="skyblue", text=z.d2)
    option2.place(x=550, y=450)
    option3 = tk.Button(root, height=5, width=40, bg="skyblue", text=z.d3)
    option3.place(x=1000, y=300)
    option4 = tk.Button(root, height=5, width=40, bg="skyblue", text=z.d4)
    option4.place(x=1000, y=450)
    # "NEXT" button now properly changes the question
    next = tk.Button(root, height=3, width=30, bg="red", text="NEXT...", command=queans)
    next.place(x=1100, y=600)
def show_selection(event):
    global z
    selected_value = combobox.get()  
    dd = options.index(selected_value)  

    # Assign module based on selection
    if dd == 1:
        z = a
    elif dd == 2:
        z = d
    elif dd == 3:
        z = dbms
    elif dd == 4:
        z = o

    queans()  # Load new question
    label.config(text=f"Selected: {selected_value} (Index: {dd})")   

options = ["SUBJECT", "APTITUDE", "DATA STRUCTURE", "DBMS", "OPERATING SYSTEM"]
combobox = ttk.Combobox(root, values=options, state="readonly", font=("Arial", 25))
combobox.current(0)  
combobox.place(x=0, y=1)
combobox.bind("<<ComboboxSelected>>", show_selection)

label = tk.Label(root, font=("Arial", 25), text="Selected: " + combobox.get())
label.pack()



root.mainloop()
