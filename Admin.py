from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo
import sqlite3

root=Tk()
root.title("MOYALE LINEAR ADMIN PORTAL")
root.geometry('925x550+350+250')
root.configure(bg="#161C25")
root.resizable(False,False)

heading =Label(root,text='Moyale Linear Online Booking Admin Portal', fg='white',
               bg='#161C25',font=('Microsoft Yahei UI Light',15,'bold'))
heading.place(x=205,y=5)
sub_heading =Label(root,text='Moyale Linear Online Booking', fg='white',
               bg='#161C25',font=('Microsoft Yahei UI Light',15,'bold'))
def Update():
    pass
#sub_heading.place(x=295,y=5)
def moyaletonairobibus():
    vehiclereg=""
    if moyale_nairobi.get()== "":
        messagebox.showerror("Missing Entry","Kindly Indicate Car Registration Number")
    else:
        vehiclereg=moyale_nairobi.get()
    return vehiclereg

def nairobitomoyalebus():
    vehicleReg=""
    if nairobi_moyale.get()== "":
        messagebox.showerror("Missing Entry","Kindly Indicate Car Registration Number")
    else:
        vehicleReg=nairobi_moyale.get()
    return vehicleReg
#------------
sub_heading =Label(root,text='Moyale To Nairobi Bus', fg='white',
               bg='#161C25',font=('Microsoft Yahei UI Light',11,'bold'))
sub_heading.place(x=20,y=40)
def on_enter(e):
    moyale_nairobi.delete(0,'end')
    

def on_leave(e):
    moyale_nairobi_content=moyale_nairobi.get()
    if moyale_nairobi_content=='':
        moyale_nairobi.insert(0,'KDD 456A')

moyale_nairobi=Entry(root,width=25,fg='white',border=0,bg="#161C25",font=('Microsoft Yahei UI Light',11))
moyale_nairobi.place(x=20,y=60)
moyale_nairobi.insert(0,'KDD 456A')
moyale_nairobi.bind('<FocusIn>',on_enter)
moyale_nairobi.bind('<FocusOut>',on_leave)
Frame(root,width=225,height=1,bg='white').place(x=20,y=85)
#------------------
sub_heading =Label(root,text='Nairobi To Moyale Bus', fg='white',
               bg='#161C25',font=('Microsoft Yahei UI Light',11,'bold'))
sub_heading.place(x=390,y=40)
def on_enter(e):
    nairobi_moyale.delete(0,'end')
    

def on_leave(e):
    nairobi_moyale_content=nairobi_moyale.get()
    if nairobi_moyale_content=='':
        nairobi_moyale.insert(0,'KDA 347G')

nairobi_moyale=Entry(root,width=25,fg='white',border=0,bg="#161C25",font=('Microsoft Yahei UI Light',11))
nairobi_moyale.place(x=390,y=60)
nairobi_moyale.insert(0,'KDA 347G')
nairobi_moyale.bind('<FocusIn>',on_enter)
nairobi_moyale.bind('<FocusOut>',on_leave)
Frame(root,width=225,height=1,bg='white').place(x=390,y=85)
Button(root,width=15,pady=1,text='Update Vehicle', bg='#57a1f8',fg='white',border=0,font=('Microsoft Yahei UI Light',10,'bold'),command=moyaletonairobibus).place(x=20,y=95)
Button(root,width=15,pady=1,text='Update Vehicle', bg='#57a1f8',fg='white',border=0,font=('Microsoft Yahei UI Light',10,'bold'),command=nairobitomoyalebus).place(x=390,y=95)

#-------------
#FUNCTION TO PERFORM SEARCH
def perform_search():
    conn = sqlite3.connect('MoyaleBus.db')
    cursor=conn.cursor()
    query=""
    if search_entry.get()=="Search By National ID...":
        messagebox.showerror("Warning","Search by Id")
    else:
        query = search_entry.get()
    
    cursor.execute("SELECT * FROM passengers WHERE Id_number = ?",(query,))
    data=cursor.fetchone()
    #Clear the treeview
    for item in tree.get_children():
        tree.delete(item)
    #Populate the treeview with the search results
    for item in data:
        tree.insert("","end", values=item)
    conn.commit()
    conn.close()
#RESET THE TREEVIEW
def reset_treeview():
    conn = sqlite3.connect('MoyaleBus.db')
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM passengers")
    data =cursor.fetchall()
    for item in tree.get_children():
        tree.delete(item)
    for item in data:
        tree.insert("","end",values=item)
    conn.commit()
    conn.close()
           
Button(root,width=10,pady=1,text='Search', bg='#57a1f8',fg='white',border=0,font=('Microsoft Yahei UI Light',10,'bold'),command=perform_search).place(x=650,y=170)
Button(root,width=10,pady=1,text='Reset', bg='#57a1f8',fg='white',border=0,font=('Microsoft Yahei UI Light',10,'bold'),command=reset_treeview).place(x=750,y=170)
#-------FUNCTION TO DELETE
def delete_selected_item():
    conn = sqlite3.connect('MoyaleBus.db')
    cursor=conn.cursor()
    selected_items=tree.selection()
    for item in selected_items:
        item_id=item
        cursor.execute("DELETE FROM passengers WHERE From_town =?",(item_id,))
        conn.commit()
        tree.delete(item)
  
#----SEARCH WIDGET
def on_enter(e):
    search_entry.delete(0,'end')
    
def on_leave(e):
    search_entry_content=search_entry.get()
    if search_entry_content=='':
        search_entry.insert(0,'Search By National ID...')    
        
search_entry=Entry(root,width=25,fg='white',border=0,bg="#161C25",font=('Microsoft Yahei UI Light',11))
search_entry.place(x=650,y=135)
search_entry.insert(0,'Search By National ID...')
search_entry.bind('<FocusIn>',on_enter)
search_entry.bind('<FocusOut>',on_leave)
Frame(root,width=225,height=1,bg='white').place(x=650,y=160)
##
def go_to_remarks():
    import remarks
    root.destroy()

def go_to_parcel():
    import parcelDashboard
    root.destroy()
#3

#----DELETE WIDGET
"""
def on_enter(e):
    delete_entry.delete(0,'end')
    
def on_leave(e):
    delete_entry_content=delete_entry.get()
    if delete_entry_content=='':
        delete_entry.insert(0,'Delete By Departure Point')    
        
delete_entry=Entry(root,width=25,fg='white',border=0,bg="#161C25",font=('Microsoft Yahei UI Light',11))
delete_entry.place(x=390,y=135)
delete_entry.insert(0,'Delete By Departure Point')
delete_entry.bind('<FocusIn>',on_enter)
delete_entry.bind('<FocusOut>',on_leave)
Frame(root,width=225,height=1,bg='white').place(x=390,y=160)"""
sub_heading =Label(root,text='Select Item To Delete', fg='white',
               bg='#161C25',font=('Microsoft Yahei UI Light',10,'bold'))
sub_heading.place(x=475,y=140)
Button(root,width=15,pady=1,text='Remove', bg='#57a1f8',fg='white',border=0,font=('Microsoft Yahei UI Light',10,'bold'),command=delete_selected_item).place(x=475,y=170)
Button(root,width=15,pady=1,text='Remarks', bg='#57a1f8',fg='white',border=0,font=('Microsoft Yahei UI Light',10,'bold'),command=go_to_remarks).place(x=247,y=170)
Button(root,width=15,pady=1,text='Parcel', bg='#57a1f8',fg='white',border=0,font=('Microsoft Yahei UI Light',10,'bold'),command=go_to_parcel).place(x=47,y=170)

#---  
tree=ttk.Treeview(root,columns=("ID","FROM","TO","SIT_NUMBER","FULL_NAME","ID_NUMBER","PHONE_NUMBER","EMAIL","ID_IMAGE"), show="headings",height=450)
tree.heading("ID",text="ID")
tree.heading("FROM",text="FROM")
tree.heading("TO",text="TO")
tree.heading("SIT_NUMBER",text="SIT_NUMBER")
tree.heading("FULL_NAME",text="FULL_NAME")
tree.heading("ID_NUMBER",text="ID_NUMBER")
tree.heading("PHONE_NUMBER",text="PHONE_NUMBER (+254)")
tree.heading("EMAIL",text="EMAIL")
tree.place(x=0,y=215,width=900,height=700)
horizontal_scroll_bar=ttk.Scrollbar(root,orient="horizontal",command=tree.xview)
horizontal_scroll_bar.pack(fill="x",side="bottom")
vertical_scroll_bar=ttk.Scrollbar(root,orient="vertical",command=tree.yview)
vertical_scroll_bar.pack(fill="y",side="right")
conn=sqlite3.connect('MoyaleBus.db')
cursor=conn.cursor()
#Fetch data from the database
cursor.execute("SELECT * FROM passengers")
data=cursor.fetchall()

#Insert data into the Treeview

for row in data:
    tree.insert("","end",values=row)
#Commit and close the database connection
conn.commit()
conn.close()          
#if __name__ == "__main__":
root.mainloop()
"""
#Create a database
conn = sqlite3.connect('MoyaleBus.db')
cursor=conn.cursor()
cursor.execute("SELECT * FROM passengers")
print(cursor.fetchall())
conn.commit()

conn.close
"""
