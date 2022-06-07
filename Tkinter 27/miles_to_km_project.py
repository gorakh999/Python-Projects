import tkinter

window = tkinter.Tk()
window.title("Miles-KM")
window.minsize(width=400, height=300)
# window.config(padx=10 ,pady=10)

# command to perform when button is clicked
def button_command():
    str1 = input1.get() # get input text from entry box
    str1 = str(round((int(str1) * 1.609), 2))
    my_label3.config(text=str1) # change the label text



input1 = tkinter.Entry()
input1.grid(column=1, row=0)

my_label1 = tkinter.Label(text=f" Miles", font =("aerial", 16, "bold"))
my_label1.grid(column=2, row=0)
my_label1.config(padx=10, pady=10)

my_label2 = tkinter.Label(text=f" is Equal to ", font =("aerial", 16, "bold"))
my_label2.grid(column=0, row=1)
my_label2.config(padx=10, pady=10)

my_label3 = tkinter.Label(text=f" {0}", font =("aerial", 16, "bold"))
my_label3.grid(column=1, row=1)
my_label3.config(padx=10, pady=10)

my_label4 = tkinter.Label(text=f" KM", font =("aerial", 16, "bold"))
my_label4.grid(column=2, row=1)
my_label4.config(padx=10, pady=10)


button1 = tkinter.Button(text="Calculate", command=button_command)
button1.grid(column=1, row=2)
















window.mainloop()