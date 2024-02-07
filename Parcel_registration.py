from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import sqlite3

root=Tk()
root.title("MOYALE LINEAR PARCEL PORTAL")
root.geometry('925x550+350+250')
root.configure(bg="white")
root.resizable(False,False)
heading =Label(root,text='Moyale Linear Online Booking Parcel Registration', fg='white',
               bg='white',font=('Microsoft Yahei UI Light',15,'bold'))
def go_to_admin():
    import parcelDashboard
    root.destroy()
    
Button(root,width=30,pady=1,text='Parcel Dashboard', bg='#57a1f8',fg='white',border=0,font=('Microsoft Yahei UI Light',10,'bold'),command=go_to_admin).place(x=10,y=10)
#--- 


def on_enter(e):
    parcelType.delete(0,'end')

def on_leave(e):
    productName_=parcelType.get()
    if productName_=='':
        parcelType.insert(0,'Parcel Type')
parcelType=Entry(root, width=25,fg='black',border=0,bg="white",font=('Microsoft Yahei UI Light',11))
parcelType.place(x=10,y= 75)
parcelType.insert(0, 'Parcel Type')
parcelType.bind('<FocusIn>',on_enter)
parcelType.bind('<FocusOut>',on_leave)
Frame(root,width=295,height=1,bg='black').place(x=10,y=95)
#---
def on_enter(e):
    parcelNumber.delete(0,'end')

def on_leave(e):
    parcelNumber__=parcelNumber.get()
    if parcelNumber__=='':
        parcelNumber.insert(0,'Parcel Number')
parcelNumber=Entry(root, width=25,fg='black',border=0,bg="white",font=('Microsoft Yahei UI Light',11))
parcelNumber.place(x=400,y= 75)
parcelNumber.insert(0, 'Parcel Number')
parcelNumber.bind('<FocusIn>',on_enter)
parcelNumber.bind('<FocusOut>',on_leave)
Frame(root,width=295,height=1,bg='black').place(x=400,y=95)
#---
def on_enter(e):
    departurePoint.delete(0,'end')

def on_leave(e):
    departurePoint__=departurePoint.get()
    if departurePoint__=='':
        departurePoint.insert(0,'Departure')
departurePoint=Entry(root, width=25,fg='black',border=0,bg="white",font=('Microsoft Yahei UI Light',11))
departurePoint.place(x=10,y= 175)
departurePoint.insert(0, 'Departure')
departurePoint.bind('<FocusIn>',on_enter)
departurePoint.bind('<FocusOut>',on_leave)
Frame(root,width=295,height=1,bg='black').place(x=10,y=195)
#---
#---
def on_enter(e):
    arrivalPoint.delete(0,'end')

def on_leave(e):
    arrivalPoint__=arrivalPoint.get()
    if arrivalPoint__=='':
        arrivalPoint.insert(0,'Arrival')
arrivalPoint=Entry(root, width=25,fg='black',border=0,bg="white",font=('Microsoft Yahei UI Light',11))
arrivalPoint.place(x=400,y= 175)
arrivalPoint.insert(0, 'Arrival')
arrivalPoint.bind('<FocusIn>',on_enter)
arrivalPoint.bind('<FocusOut>',on_leave)
Frame(root,width=295,height=1,bg='black').place(x=400,y=195)
#---
def Submit():
    parceltype_value=parcelType.get()
    parcelnumber_value=parcelNumber.get()
    departurepoint_value=departurePoint.get()
    arrivalpoint_value=arrivalPoint.get()
    status_value="Pending"
    try:
        conn =sqlite3.connect('MoyaleBus.db')
        cursor=conn.cursor()
        cursor.execute("INSERT INTO parcelTable(parcelType,parcelNo,departurePoint,arrivalPoint,status) VALUES(?,?,?,?,?)",
                       (parceltype_value,parcelnumber_value,departurepoint_value,arrivalpoint_value,status_value))
        conn.commit()
        messagebox.showinfo("SYSTEM NITIFICATION","PARCEL REGISTERED")
    except sqlite3.Error as e:
        print("PARCEL REGISTRATION ERROR",e)
    finally:
        conn.close()

Button(root,width=15,pady=1,text='Submit', bg='#57a1f8',fg='white',border=0,font=('Microsoft Yahei UI Light',10,'bold'),command=Submit).place(x=220,y=210)


root.mainloop()
