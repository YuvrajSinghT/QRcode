import tkinter as tk
from tkinter import *
import qrcode

root=Tk()
root.title("QR CODE GENERATOR")
root.geometry("1000x500")
root.config(bg="white")
root.resizable(False,False)

#give the file name to the icon
'''image_icon=PhotoImage(file="")
root.iconphoto(False,image_icon)'''

def generate():
    name=title.get()
    text=entery.get()

    qr=qrcode.make(text)
    qr.save("Qrcode/"+str(name)+".png")

    global Image
    Image=PhotoImage(file="Qrcode/"+str(name)+".png")
    Image_view.config(image=Image)

Image_view=Label(root,bg="white")
Image_view.pack(padx=50,pady=10,side=RIGHT)

hello=Label(root,text="title",fg="black",bg="white",font=15)
hello.place(x=50,y=170)

title=tk.Entry(root,width=15,font="arial 13")
title.place(x=50,y=200)

entery=tk.Entry(root,width=15,font="arial 13")
entery.place(x=50,y=250)

butt=Button(root,text="generate",width=20,height=2,bg="black",fg="white",command=generate)
butt.place(x=50,y=300)

button_mode=True
def customize():
    global button_mode
    if button_mode:
        button.config(image=off,bg="#26242f",activebackground="#26242f")
        root.config(bg="#26242f")
        button_mode=False
    else:
        button.config(image=on,bg="white",activebackground="white")
        root.config(bg="white")
        button_mode=True

on=PhotoImage(file="images/light.png")
off=PhotoImage(file="images/dark.png")

button=Button(root,image=on,bd=0,bg="white",activebackground="white",command=customize)
button.pack(padx=50,pady=50)

root.mainloop()