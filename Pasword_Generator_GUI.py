from tkinter import *
import string
from random import *
window=Tk()
window.title('Password Generator')
window.geometry('360x200')

lbl1=Label(window,text='This is Random Password Generator',fg='orange',font=("Arial Bold", 15))
lbl1.grid(column=0,row=0)

def click():
    char=string.ascii_letters+string.punctuation+string.digits
    passs="".join(choice(char) for x in range(randint(8, 16)))
    lbl1.configure(text='Password: '+passs)

bt=Button(window,text='GENERATE',bg='red',fg='orange',command=click)
bt.grid(column=0,row=1)

window.mainloop()
