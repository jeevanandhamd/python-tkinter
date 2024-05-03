from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import database

db=database("employee.db")

root=Tk()
root.title("EMPLOYEE MANAGEMENT SYSTEM")
root.geometry("1500x1080+0+0")
root.configure(bg="#2c3e50")
root.state("zoomed")
name=StringVar()
age=StringVar()
doj=StringVar()
gender=StringVar()
email=StringVar()
contact=StringVar()

#entry
ent_frame=Frame(root,bg="#535c68")
ent_frame.pack(side=TOP ,fill=X)
title=Label(ent_frame,text="EMPLOYEE MANAGEMENT SYSTEM",font=("calibri",18,"bold"),bg="#535c68",fg="white")
title.grid(row=0,columnspan=2,padx=10,pady=20)

lblname=Label(ent_frame,text="Name",font=("calibri",15),bg="#535c68",fg="white")
lblname.grid(row=1,column=0,padx=10,pady=10,sticky=W)
txtname=Entry(ent_frame,textvariable=name,font=("calibri",15),width=30)
txtname.grid(row=1,column=1)

lblagename=Label(ent_frame,text="Age",font=("calibri",15),bg="#535c68",fg="white")
lblagename.grid(row=1,column=2,padx=10,pady=10,sticky=W)
txtagename=Entry(ent_frame,textvariable=age,font=("calibri",15),width=30)
txtagename.grid(row=1,column=3)

lbldoj=Label(ent_frame,text="DOJ",font=("calibri",15),bg="#535c68",fg="white")
lbldoj.grid(row=2,column=0,padx=10,pady=10,sticky=W)
txtdoj=Entry(ent_frame,textvariable=doj,font=("calibri",15),width=30)
txtdoj.grid(row=2,column=1)

lblemail=Label(ent_frame,text="Email",font=("calibri",15),bg="#535c68",fg="white")
lblemail.grid(row=2,column=2,padx=10,pady=10,sticky=W)
txtmail=Entry(ent_frame,textvariable=email,font=("calibri",15),width=30)
txtmail.grid(row=2,column=3)

lblgender=Label(ent_frame,text="Gender",font=("calibri",15),bg="#535c68",fg="white")
lblgender.grid(row=3,column=0,padx=10,pady=10,sticky=W)
combogender=ttk.Combobox(ent_frame,textvariable=gender,font=("calibri",15),width=28,state="read only")
combogender["value"]=("Male","Female")
combogender.grid(row=3,column=1,padx=10,pady=10,sticky=W)

lblcon=Label(ent_frame,text="Contact",font=("calibri",15),bg="#535c68",fg="white")
lblcon.grid(row=3,column=2,padx=10,pady=10,sticky=W)
txtcon=Entry(ent_frame,textvariable=contact,font=("calibri",15),width=30)
txtcon.grid(row=3,column=3)

lbladd=Label(ent_frame,text="Address",font=("calibri",15),bg="#535c68",fg="white")
lbladd.grid(row=4,column=0,padx=10,pady=10,sticky=W)
txtadd=Text(ent_frame,width=85,height=5,font=("calibri",15))
txtadd.grid(row=5,column=0,padx=10,sticky=W,columnspan=4)

def getData(event):
    select=tv.focus()
    data=tv.item(select)
    global row 
    row=data["values"]
    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    gender.set(row[4])
    email.set(row[5])
    contact.set(row[6])
    txtadd.delete(1.0,END)
    txtadd.insert(END,row[7])
    

def displayall():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row)

def additem():
    if txtname.get()==""or txtagename.get()=="" or txtdoj.get()=="" or txtmail.get()=="" or txtcon.get()=="" or combogender.get()=="" or txtadd.get(1.0,END)=="" :
        messagebox.showerror("Error In Input")
        return
    db.insert(txtname.get(), txtagename.get(), txtdoj.get(),txtmail.get(), txtcon.get(),combogender.get(), txtadd.get(1.0,END)) 
    messagebox.showinfo("success","record stored")

    clearall()
    displayall()


def updateitem():
     if txtname.get()==""or txtagename.get()=="" or txtdoj.get()=="" or txtmail.get()=="" or txtcon.get()=="" or combogender.get()=="" or txtadd.get(1.0,END)=="" :
        messagebox.showerror("Error In Input")
        return
        db.update(row[0],txtname.get(), txtagename.get(), txtdoj.get(),txtmail.get(), txtcon.get(),combogender.get(), txtadd.get(1.0,END)) 
        messagebox.showinfo("success","record updated")
    
     clearall()
     displayall()

def deleteitem():
    db.remove(row[0])
    clearall()
    displayall()

    
def clearall():
    name.set("")
    age.set("")
    doj.set("")
    gender.set("")
    email.set("")
    contact.set("")
    txtadd.delete(1.0,END)
    

btn_frame=Frame(ent_frame,bg="#535c68")
btn_frame.grid(row=6,column=0,padx=10,pady=10,sticky=W,columnspan=4)

btnadd=Button( btn_frame,command= additem,text="Add Details",width=15,font=("calibri",15,"bold"),fg="white",bg="#16a085",bd=0).grid(row=0,column=0,padx=10)

btnadd=Button( btn_frame,command=updateitem ,text="Update Details",width=15,font=("calibri",15,"bold"),fg="white",bg="#16a085",bd=0).grid(row=0,column=1,padx=10)

btnadd=Button( btn_frame,command=deleteitem ,text="Delete Details",width=15,font=("calibri",15,"bold"),fg="white",bg="#16a085",bd=0).grid(row=0,column=2,padx=10)

btnadd=Button( btn_frame,command=clearall,text="Clear Details",width=15,font=("calibri",15,"bold"),fg="white",bg="#16a085",bd=0).grid(row=0,column=3,padx=10)

#table
table_frame=Frame(root,bg="#ecf0f1")
table_frame.place(x=0,y=450,width=1500,height=700)
style=ttk.Style()
style.configure("mystyle.Treeview",font=("calibri",18),rowheight=50)

tv=ttk.Treeview(table_frame,columns=(1,2,3,4,5,6,7,8),style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1",width=80)
tv.heading("2", text="Name")
tv.heading("3", text="Age")
#tv.column("3", width=5)
tv.heading("4", text="D.O.J")
#tv.column("4", width=10)
tv.heading("5", text="Email")
tv.heading("6", text="Gender")
#tv.column("6", width=10)
tv.heading("7", text="Contact")
tv.heading("8", text="Address")
tv["show"]="headings"
tv.bind("<ButtonRelease>", getData)
tv.pack(fill=X)



displayall()
root.mainloop()
