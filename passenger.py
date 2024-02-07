from tkinter import *
from tkinter import messagebox
import sqlite3

root=Tk()
root.title("MOYALE LINER ONLINE BUS BOOKING SERVICES")
root.geometry('925x550+350+250')
root.configure(bg="#161C25")
root.resizable(False,False)
img=PhotoImage(file='frontpage.png')
Label(root,image=img,bg='#161C25').place(x=0,y=0)

frame =Frame (root,width=350,
              height=500,
              bg="white",)
frame.place(x=480,y=25)
heading =Label(frame,text='Bus Online Booking Portal', fg='black',
               bg='white',font=('Microsoft Yahei UI Light',14,'bold'))
heading.place(x=50,y=5)
sub_heading =Label(frame,text='Choose Your Route Below', fg='black',
               bg='white',font=('Microsoft Yahei UI Light',10,'bold',))
sub_heading.place(x=70,y=35)
#Check if the Sit is available
def check_sit():
    conn=sqlite3.connect('MoyaleBus.db')
    cursor=conn.cursor()
    sit_status=""
    sit_check=sit_number.get()
    cursor.execute("SELECT * FROM passengers WHERE Sit_number =?",(sit_check,))
    data=cursor.fetchone()
    if data :
        sit_status="Sit Taken"
    else:
        sit_status="Sit Yours"

    if sit_status== "Sit Taken":
        messagebox.showerror("Warning",f"Sit number{sit_check} is taken \n Kindly Choose another sit")
    else:
        messagebox.showinfo("Sit Booked",f"Sit number{sit_check} is available" )
        
def Book():
    ####Collect all the information from the field
    from_content=Route_F.get()# From
    to_content=Route_t.get()#To
    sit_number_content=sit_number.get()#Sit Number
    route_cost=0#Cost
    fullname_content=fullname.get()#First and Last Name
    idnumber_content=idnumber.get()#ID Number
    phonenumber_content=phonenumber.get()#Phone Number
    email_content=email.get()#Email
    route_no=0
    car_reg=""
    ######

    
    if from_content=="Moyale" and to_content == "Marsabit":
        route_no=1
        route_cost= 1200
    elif from_content=="Moyale" and to_content == "Isiolo":
        route_no=1
        route_cost= 2000
    elif from_content=="Moyale" and to_content == "Nairobi":
        route_no=1
        route_cost= 3000
    elif from_content=="Nairobi" and to_content == "Isiolo":
        route_no=2
        route_cost=1000
        
    if from_content=="From" or to_content == "To" or fullname_content=="First And Last Name" or idnumber_content=="Id Number" or phonenumber_content=="Phone Number" or email_content=="Email":
        messagebox.showerror("Invalid Entry","Kindly Enter your Details Please")
    ## AFTER VALIDATION WE ENTER OUR DATA TO THE DATABASE
    else:
        conn =sqlite3.connect('MoyaleBus.db')
        cursor=conn.cursor()
        cursor.execute("INSERT INTO passengers(From_town,To_town,Sit_number,Full_name,Id_number,phone_number,email) VALUES(?,?,?,?,?,?,?)",
                    (from_content,to_content,sit_number_content,fullname_content,idnumber_content,phonenumber_content,email_content))
        conn.commit()
        conn.close()
        messagebox.showinfo('Success', f'You booking has been received succesfuly \n Route {from_content} Destination {to_content} \n Transport Cost:{route_cost}') 
#####-----------------FROM------------------------
def on_enter(e):
    Route_F.delete(0,'end')
    

def on_leave(e):
    from_content=Route_F.get()
    if from_content=='':
        Route_F.insert(0,'From')

        
Route_F=Entry(frame,width=15,fg='black',border=0,bg="white",font=('Microsoft Yahei UI Light',11))
Route_F.place(x=30,y=80)
Route_F.insert(0,'From')
Route_F.bind('<FocusIn>',on_enter)
Route_F.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=1,bg='black').place(x=25,y=100)
#####----------------TO-----------------------------
def on_enter(e):
    Route_t.delete(0,'end')
    

def on_leave(e):
    to_content=Route_t.get()
    if to_content=='':
        Route_t.insert(0,'To')

Route_t=Entry(frame,width=15,fg='black',border=0,bg="white",font=('Microsoft Yahei UI Light',11))
Route_t.place(x=30,y=130)
Route_t.insert(0,'To')
Route_t.bind('<FocusIn>',on_enter)
Route_t.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=1,bg='black').place(x=25,y=150)
#####----------------BOOK SIT-----------------------------
def on_enter(e):
    sit_number.delete(0,'end')
    

def on_leave(e):
    sit_number_content=sit_number.get()
    if sit_number_content=='':
        sit_number.insert(0,'Book a seat')
        
sit_number=Entry(frame,width=15,fg='black',border=0,bg="white",font=('Microsoft Yahei UI Light',11))
sit_number.place(x=30,y=180)
sit_number.insert(0,'Book a seat')
sit_number.bind('<FocusIn>',on_enter)
sit_number.bind('<FocusOut>',on_leave)
Button(frame,width=10,pady=4,text='Confirm Sit', bg='#57a1f8',fg='white',border=0,font=('Microsoft Yahei UI Light',10,'bold'),command=check_sit).place(x=225,y=165)
Frame(frame,width=295,height=1,bg='black').place(x=25,y=200)

####----------------------------------------------
sub_heading =Label(frame,text='Fill Your Details To Complete The Booking', fg='black',
               bg='white',font=('Microsoft Yahei UI Light',10,'bold',))
sub_heading.place(x=35,y=210)
#####----------------FULL NAME-----------------------------
def on_enter(e):
    fullname.delete(0,'end')
    

def on_leave(e):
    fullname_content=fullname.get()
    if fullname_content=='':
        fullname.insert(0,'First And Last Name')
        
fullname=Entry(frame,width=20,fg='black',border=0,bg="white",font=('Microsoft Yahei UI Light',11))
fullname.place(x=30,y=250)
fullname.insert(0,'First And Last Name')
fullname.bind('<FocusIn>',on_enter)
fullname.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=1,bg='black').place(x=25,y=270)
#####----------------ID NUMBER-----------------------------
def on_enter(e):
    idnumber.delete(0,'end')
    

def on_leave(e):
    idnumber_content=idnumber.get()
    if idnumber_content=='':
        idnumber.insert(0,'Id Number')
        
idnumber=Entry(frame,width=20,fg='black',border=0,bg="white",font=('Microsoft Yahei UI Light',11))
idnumber.place(x=30,y=300)
idnumber.insert(0,'Id Number')
idnumber.bind('<FocusIn>',on_enter)
idnumber.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=1,bg='black').place(x=25,y=320)
####-------------------PHONE NUMBER---------------------------
def on_enter(e):
    phonenumber.delete(0,'end')
    

def on_leave(e):
    phonenumber_content=phonenumber.get()
    if phonenumber_content=='':
        phonenumber.insert(0,'Phone Number')
        
phonenumber=Entry(frame,width=20,fg='black',border=0,bg="white",font=('Microsoft Yahei UI Light',11))
phonenumber.place(x=30,y=350)
phonenumber.insert(0,'Phone Number')
phonenumber.bind('<FocusIn>',on_enter)
phonenumber.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=1,bg='black').place(x=25,y=370)
####--------------------EMAIL--------------------------

def on_enter(e):
    email.delete(0,'end')
    

def on_leave(e):
    email_content=email.get()
    if email_content=='':
        email.insert(0,'Email')
        
email=Entry(frame,width=20,fg='black',border=0,bg="white",font=('Microsoft Yahei UI Light',11))
email.place(x=30,y=400)
email.insert(0,'Email')
email.bind('<FocusIn>',on_enter)
email.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=1,bg='black').place(x=25,y=420)
####----------------------------------------------
Button(frame,width=30,pady=7,text='Book Now', bg='#57a1f8',fg='white',border=0,font=('Microsoft Yahei UI Light',10,'bold'),command=Book).place(x=30,y=450)
root.mainloop()
