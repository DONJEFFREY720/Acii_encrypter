# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from tkinter import*
root=Tk()
root.title("Fibonacci") 
root.geometry("400x400")
root.configure(bg="cyan")


input = Entry(root)
input.place(relx=0.5,rely=0.4,anchor=CENTER) 

label = Label(root,text="Name In Acii : ",bg="light yellow",fg = "black")
label2 = Label(root,text="Encrypted Name : ",bg="light yellow",fg = "black")
label3 = Label(root,text="Entered Name : ",bg="light yellow",fg = "black")
label0 = Label(root,text="TEXT ENCRYPTER",bg="yellow",fg = "black")



def convertacci():
    name = input.get()
    label3 ["text"]+= str(name) 
    
    for letter in name :
        label["text"]+= str(ord(letter))+"  " 
        acii = int(ord(letter))
        encrypt = acii-1
        label2 ["text"] += str (chr (encrypt))
        
    
def reset():
    label ["text"]= "Name In Acii : "
    label2 ["text"]= "Encrypted Name : " 
    label3 ["text"]= "Entered Name : " 
    
    
label.place(relx=0.5,rely=0.6,anchor=CENTER)
label2.place(relx=0.5,rely=0.7,anchor=CENTER)
label3.place(relx=0.5,rely=0.8,anchor=CENTER)
label0.place(relx=0.5,rely=0.1,anchor=CENTER)
    
btn=Button(root, text="ENCRYPT", command=convertacci, bg='blue', fg = 'white') 
btn.place(relx=0.5, rely=0.5, anchor=CENTER)
btn=Button(root, text="RESET", command=reset, bg='red', fg = 'white') 
btn.place(relx=0.5, rely=0.9, anchor=CENTER)


root.mainloop()