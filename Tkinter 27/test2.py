import tkinter

window = tkinter.Tk()
window.title("First GUI")
window.minsize(width=500, height=400)
window.config(padx=10 ,pady=10)

# command to perform when button is clicked
def button_command():
    str1 = input1.get() # get input text from entry box
    if len(str1.strip()) > 4:
        my_label1.config(text=str1) # change the label text


my_label1 = tkinter.Label(text="This is Label 1 ", font =("aerial", 24, "bold"))
my_label1.grid(column=0, row=0)

# my_label2 = tkinter.Label(text="This is Label 2", font=("aerial", 24, "bold"))
# my_label2.pack()

button1 = tkinter.Button(text="Click Me", command=button_command)
button1.grid(column=1, row=1)

button2 = tkinter.Button(text="New Button", command=button_command)
button2.grid(column=2, row=0)


input1 = tkinter.Entry()
input1.grid(column=3, row=3)













window.mainloop()