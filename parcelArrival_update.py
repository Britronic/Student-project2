import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo
import sqlite3

root=tk.Tk()
root.title("MOYALE LINEAR PARCEL PORTAL")
root.geometry('925x550+350+250')
root.configure(bg="white")
root.resizable(False,False)
frame=Frame(root,width=850,height=950,bg="white")
frame.place(x=40,y=25)
def go_to_admin():
    import parcelDashboard
    root.destroy()
    
Button(root,width=30,pady=1,text='Parcel Dashboard', bg='#57a1f8',fg='white',border=0,font=('Microsoft Yahei UI Light',10,'bold'),command=go_to_admin).place(x=10,y=10)

def perform_search():
    #Search based on user Id
    #Then Assign each value to Variable
    query=""
    if search_entry.get()=='Search By Parcel Number...':
        messagebox.showerror("Warning","Search by Loan Id")
    else:
        try:
            query=search_entry.get()
            conn = sqlite3.connect('MoyaleBus.db')
            cursor=conn.cursor()
            cursor.execute("SELECT parcelNo,status FROM parcelTable WHERE parcelNo=?",(query,))
            data=cursor.fetchone()
            print(data)
            conn.commit()
            if data:
                parcelNo_value,status_value=data
                print("DATA FOUND")
                #------------
                def on_enter(e):
                    loanId.delete(0,'end')

                def on_leave(e):
                    Loan=laonId.get()
                    if Loan=='':
                        loanId.insert(0,f'{parcelNo_value}')
        
                loanId=Entry(frame,width=25,fg="black",border=0,bg="white",font=('Microsoft Yahei UI Light',11))
                loanId.place(x=270,y=140)
                loanId.insert(0,f'{parcelNo_value}')
                loanId.bind('<FocusIn>',on_enter)
                loanId.bind('<FocusOut>',on_leave)
                Frame(frame,width=195,height=2,bg="black").place(x=270,y=167)
                #-------------
                
                def on_enter(e):
                    loanAmount.delete(0,'end')

                def on_leave(e):
                    LoanAmount=loanAmount.get()
                    if LoanAmount=='':
                        loanAmount.insert(0,f'{status_value}')
        
                
                loanAmount=Entry(frame,width=25,fg="black",border=0,bg="white",font=('Microsoft Yahei UI Light',11))
                loanAmount.place(x=550,y=140)
                loanAmount.insert(0,f'{status_value}')
                loanAmount.bind('<FocusIn>',on_enter)
                loanAmount.bind('<FocusOut>',on_leave)
                Frame(frame,width=195,height=2,bg="black").place(x=550,y=167)
                #-------------
                def CheckInn():
                    query=search_entry.get()
                    updated__="Arrived"
                    conn = sqlite3.connect('MoyaleBus.db')
                    cursor=conn.cursor()
                    cursor.execute("UPDATE parcelTable SET status=? WHERE parcelNo=?",(updated__,query))
                    conn.commit()
                    messagebox.showinfo("SYSTEM NOTIFICATION","PARCEL HAS ARRIVED SUCCESFULLY")
                Button(root,width=20,pady=1,text='CheckInn Parcel', bg='#57a1f8',fg='white',border=0,font=('Microsoft Yahei UI Light',10,'bold'),command=CheckInn).place(x=300,y=220)
                def parcelPicked():
                    query=search_entry.get()
                    conn = sqlite3.connect('MoyaleBus.db')
                    cursor=conn.cursor()
                    cursor.execute("DELETE FROM parcelTable WHERE parcelNo=?",(query,))
                    conn.commit()
                    messagebox.showinfo("SYSTEM NOTIFICATION","PARCEL HAS BEEN GIVEN TO RECEIPTIENT")
                                
                    
                Button(root,width=20,pady=1,text='Parcel Picking', bg='#57a1f8',fg='white',border=0,font=('Microsoft Yahei UI Light',10,'bold'),command=parcelPicked).place(x=300,y=320)


            else:
                messagebox.showinfo("SYSTEM NOTIFICATION","NO PARCLE RELATED TO THE PARCLE NUMBER")


                    
        except sqlite3.Error as e:
            print(e)
        finally:
            conn.close()
        
    




#----SEARCH WIDGET
def on_enter(e):
    search_entry.delete(0,'end')
    
def on_leave(e):
    search_entry_content=search_entry.get()
    if search_entry_content=='':
        search_entry.insert(0,'Search By Parcel Number...')    
        
search_entry=Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft Yahei UI Light',11))
search_entry.place(x=550,y=40)
search_entry.insert(0,'Search By Parcel Number...')
search_entry.bind('<FocusIn>',on_enter)
search_entry.bind('<FocusOut>',on_leave)
Frame(frame,width=225,height=1,bg='black').place(x=550,y=70)
Button(root,width=10,pady=1,text='Search', bg='#57a1f8',fg='white',border=0,font=('Microsoft Yahei UI Light',10,'bold'),command=perform_search).place(x=600,y=100)
##---------LABELS
label=Label(frame,text='Parcel Number',fg="black",bg="white",font=('Microsoft Yahei UI Light',10,'bold'))
label.place(x=270,y=120)
label=Label(frame,text='Status',fg="black",bg="white",font=('Microsoft Yahei UI Light',10,'bold'))
label.place(x=550,y=120)




root.mainloop()
