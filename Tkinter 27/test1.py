import tkinter

window = tkinter.Tk()
window.title("First GUI")
window.minsize(width=500, height=400)

# command to perform when button is clicked
def button_command():
    str1 = input1.get() # get input text from entry box
    my_label1.config(text=str1) # change the label text


my_label1 = tkinter.Label(text="This is Label 1 ", font =("aerial", 24, "bold"))
my_label1.pack()

# my_label2 = tkinter.Label(text="This is Label 2", font=("aerial", 24, "bold"))
# my_label2.pack()

button1 = tkinter.Button(text="Click Me", command=button_command)
button1.pack()


input1 = tkinter.Entry()
input1.pack()













window.mainloop()