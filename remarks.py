from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo
import sqlite3


root=Tk()
root.title("MOYALE LINEAR ADMIN RREMARKS PORTAL")
root.geometry('925x550+350+250')
root.configure(bg="#161C25")
root.resizable(False,False)
heading =Label(root,text='Moyale Linear Online Booking Remarks Portal', fg='white',
               bg='#161C25',font=('Microsoft Yahei UI Light',15,'bold'))
heading.place(x=205,y=5)
sub_heading =Label(root,text='Act According To Remarks', fg='white',
               bg='#161C25',font=('Microsoft Yahei UI Light',15,'bold'))
sub_heading.place(x=350,y=50)
def go_to_admin():
    import Admin
    root.destroy()

    
Button(root,width=15,pady=1,text='Admin Page', bg='#57a1f8',fg='white',border=0,font=('Microsoft Yahei UI Light',10,'bold'),command=go_to_admin).place(x=300,y=100)
#---  
tree=ttk.Treeview(root,columns=("remarks","phoneno"), show="headings",height=450)
tree.heading("remarks",text="Remarks")
tree.heading("phoneno",text="Phone Number(+254)")
tree.place(x=0,y=215,width=900,height=700)
horizontal_scroll_bar=ttk.Scrollbar(root,orient="horizontal",command=tree.xview)
horizontal_scroll_bar.pack(fill="x",side="bottom")
vertical_scroll_bar=ttk.Scrollbar(root,orient="vertical",command=tree.yview)
vertical_scroll_bar.pack(fill="y",side="right")
conn=sqlite3.connect('MoyaleBus.db')
cursor=conn.cursor()
#Fetch data from the database
cursor.execute("SELECT * FROM RemarksTable")
data=cursor.fetchall()

#Insert data into the Treeview

for row in data:
    tree.insert("","end",values=row)
#Commit and close the database connection
conn.commit()
conn.close()   

root.mainloop
