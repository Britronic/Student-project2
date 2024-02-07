from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import sqlite3

root=Tk()
root.title("MOYALE LINEAR PARCEL DASHBOARD")
root.geometry('925x550+350+250')
root.configure(bg="white")
root.resizable(False,False)
heading =Label(root,text='MOYALE LINEAR PARCEL DASHBOARD', fg='white',
               bg='white',font=('Microsoft Yahei UI Light',15,'bold'))
heading.place(x=205,y=5)
def go_to_admin():
    import Admin
    root.destroy()
    
Button(root,width=30,pady=1,text='Admin Page', bg='#57a1f8',fg='white',border=0,font=('Microsoft Yahei UI Light',10,'bold'),command=go_to_admin).place(x=10,y=10)
#---
def REG():
    import Parcel_registration
    root.destroy()
def LIST():
    import parcle_list
    root.destroy()
def ARRIVAL():
    import parcelArrival_update
    root.destroy()
Button(root,width=30,pady=1,text='PARCEL REGISTRATION', bg='#57a1f8',fg='white',border=0,font=('Microsoft Yahei UI Light',10,'bold'),command=REG).place(x=300,y=150)
Button(root,width=30,pady=1,text='PARCEL LIST', bg='#57a1f8',fg='white',border=0,font=('Microsoft Yahei UI Light',10,'bold'),command=LIST).place(x=300,y=200)
Button(root,width=30,pady=1,text='PARCEL ARRIVAL', bg='#57a1f8',fg='white',border=0,font=('Microsoft Yahei UI Light',10,'bold'),command=ARRIVAL).place(x=300,y=250)





root.mainloop()
