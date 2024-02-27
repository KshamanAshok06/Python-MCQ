from tkinter import *
from tkinter import simpledialog, messagebox

# define question dictionary 
question = {
    "What is the output of the following Python code?  print(1 + 2 * 3)  ":['(A)5','(B)7','(C)9','(D)11'],
    "Which of the following is not a valid data type in Python?":['(A)int','(B)float','(C)string','(D)boolean','(E)object'],
    "What is the difference between the == and is operators in Python?":['(A) The == operator compares the values of two objects, while the is operator compares the object identities of two objects.','(B) The == operator compares the types of two objects, while the is operator compares the values of two objects.','(C) The == operator is used to assign values to variables, while the is operator is used to compare values.','(D) The == operator is a logical operator, while the is operator is a relational operator.']
}

ans =['(B)7','(E)object','(A) The == operator compares the values of two objects, while the is operator compares the object identities of two objects.']

current_question = 0
timer_expired = False  # Flag to track if timer has expired

def start_quiz():
    start_button.forget()
    next_button.pack()
    start_timer()  # Start the timer
    next_question()

def next_question():
    global current_question, timer_expired
    if current_question<len(question):
        check_ans()
        user_ans.set('None')
        c_question = list(question.keys())[current_question]
        clear_frame()
        Label(f1,text=f"Question : {c_question}",padx=15,font="calibre 12 normal").pack(anchor=NW)
        for option in question[c_question]:
            Radiobutton(f1,text=option,variable=user_ans,value=option,padx=28).pack(anchor=NW)
        current_question+=1
    else:
        next_button.forget()
        check_ans()
        clear_frame()
        timer_expired = True
        next_button.config(state=DISABLED)  # Disable next button
        clear_frame()
        timer_label.pack_forget()  # Hide timer label
        show_result_button.pack()  # Show "Show Result" button

def check_ans():
    temp_ans = user_ans.get()
    if temp_ans != 'None' and temp_ans==ans[current_question-1]:
        print(f"{temp_ans} {ans[current_question-1]}")
        user_score.set(user_score.get()+1)
        print(user_score.get())

def clear_frame():
    for widget in f1.winfo_children():
        widget.destroy()

# Define timer function
def start_timer():
    global timer
    timer = 60  # Set the initial time in seconds (for testing purposes, you can set it to 60 for a minute)
    update_timer()

def update_timer():
    global timer, timer_expired
    if timer > 0 and not timer_expired:
        timer_label.config(text=f"Timer: {timer}")
        timer -= 1
        root.after(1000, update_timer)  # Schedule the function to be called after 1 second (1000 ms)
    elif timer == 0 and not timer_expired:
        timer_label.config(text="Time's up!")
        timer_expired = True
        next_button.config(state=DISABLED)  # Disable next button
        clear_frame()
        timer_label.pack_forget()  # Hide timer label
        show_result_button.pack()  # Show "Show Result" button

def show_result():
    password = simpledialog.askstring("Password", "Enter the password:")  # Ask for password
    if password == "kshaman":  
        clear_frame()
        output = f"Your Score is {user_score.get()} out of {len(question)}"
        Label(f1,text=output,font="calibre 25 bold").pack()
        show_result_button.pack_forget()  # Hide "Show Result" button
        exit_button.pack()  # Show "Exit" button
    else:
        messagebox.showerror("Error", "Incorrect password. Access denied.")

def exit_app():
    root.destroy()

if __name__ == "__main__":
    root = Tk()
    root.title("QUIZ APP")
    root.geometry("850x520")
    root.minsize(800,400)

    user_ans = StringVar()
    user_ans.set('None')
    user_score = IntVar()
    user_score.set(0)

    Label(root,text="Quiz App",font="calibre 40 bold",relief=SUNKEN,background="cyan",padx=10,pady=9).pack()
    Label(root,text="",font="calibre 10 bold").pack()
    start_button = Button(root,text="Start Quiz",command=start_quiz,font="calibre 17 bold")
    start_button.pack()

    f1 = Frame(root)
    f1.pack(side=TOP,fill=X)

    next_button = Button(root,text="Next Question",command=next_question,font="calibre 17 bold")

    show_result_button = Button(root,text="Show Result",command=show_result,font="calibre 17 bold")

    exit_button = Button(root, text="Exit", command=exit_app, font="calibre 17 bold")

    # Add a timer label
    timer_label = Label(root, text="Timer: 60", font="calibre 14 bold")
    timer_label.pack()

    root.mainloop()
