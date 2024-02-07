from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import sqlite3

root=Tk()
root.title("MOYALE LINEAR PARCEL PORTAL")
root.geometry('925x550+350+250')
root.configure(bg="white")
heading =Label(root,text='Moyale Linear Online Booking Parcel List', fg='white',
               bg='white',font=('Microsoft Yahei UI Light',15,'bold'))
heading.place(x=205,y=5)
def go_to_admin():
    import parcelDashboard
    root.destroy()
    
Button(root,width=30,pady=1,text='Parcel Dashboard', bg='#57a1f8',fg='white',border=0,font=('Microsoft Yahei UI Light',10,'bold'),command=go_to_admin).place(x=10,y=10)
#--

#---  
tree=ttk.Treeview(root,columns=("PARCLE_TYPE","PARCEL_NUMBER","DEPARTURE_POINT","ARRIVAL_POINT","STATUS"), show="headings",height=450)
tree.heading("PARCLE_TYPE",text="PARCLE TYPE")
tree.heading("PARCEL_NUMBER",text="PARCEL NUMBER")
tree.heading("DEPARTURE_POINT",text="DEPARTURE POINT")
tree.heading("ARRIVAL_POINT",text="ARRIVAL POINT")
tree.heading("STATUS",text="STATUS")
tree.place(x=0,y=100,width=1000,height=700)
horizontal_scroll_bar=ttk.Scrollbar(root,orient="horizontal",command=tree.xview)
horizontal_scroll_bar.pack(fill="x",side="bottom")
vertical_scroll_bar=ttk.Scrollbar(root,orient="vertical",command=tree.yview)
vertical_scroll_bar.pack(fill="y",side="right")
conn=sqlite3.connect('MoyaleBus.db')
cursor=conn.cursor()
#Fetch data from the database
cursor.execute("SELECT * FROM parcelTable")
data=cursor.fetchall()

#Insert data into the Treeview

for row in data:
    tree.insert("","end",values=row)
#Commit and close the database connection
conn.commit()
conn.close()  


root.mainloop()
