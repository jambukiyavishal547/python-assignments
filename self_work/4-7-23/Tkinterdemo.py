from tkinter import *
import mysql.connector
import tkinter.messagebox as msg

def create_con():
    return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="python_tk"
        )

def insert_data():
    if e_ename.get()=="" or e_dept.get()=="" or e_salary.get()=="":
        msg.showinfo("Insert Status","All Fields Are Mandatory!")
    else:
        con=create_con()
        cursor=con.cursor()
        query="insert into emp(ename,dept,salary) values(%s,%s,%s)"
        args=(e_ename.get(),e_dept.get(),e_salary.get())
        cursor.execute(query,args)
        con.commit()
        con.close()
        e_ename.delete(0,"end")
        e_dept.delete(0,"end")
        e_salary.delete(0,"end")
        msg.showinfo("Insert Status","Insert Data Successfully")

def search_data():
    e_ename.delete(0,"end")
    e_dept.delete(0,"end")
    e_salary.delete(0,"end")
    if e_id.get()=="":
       msg.showinfo("Search Status","Id IS Mandatory For Search")
    else:
        con=create_con()
        cursor=con.cursor()
        query="select * from emp where id=%s"
        args=(e_id.get(),)
        cursor.execute(query,args)
        row=cursor.fetchall()
        if row:
            for i in row:
                e_ename.insert(0,i[1])
                e_dept.insert(0,i[2])
                e_salary.insert(0,i[3])
        else:
            msg.showinfo("Search Status","Id's Data Not Found!")
        con.close()

def update_data():
    if e_ename.get()=="" or e_dept.get()=="" or e_salary.get()=="":
        msg.showinfo("update Status","All Fields Are Mandatory!")
    else: 
        con=create_con()
        cursor=con.cursor()
        query="update emp set ename=%s, dept=%s, salary=%s where id=%s"
        args=(e_ename.get(),e_dept.get(),e_salary.get(),e_id.get())
        cursor.execute(query,args)
        con.commit()
        con.close()
        
        e_ename.delete(0,"end")
        e_dept.delete(0,"end")
        e_salary.delete(0,"end")
        msg.showinfo("Update Status","Data Update Successfully")

def delete_data():
    if e_id=="":
        msg.showinfo("Delete Status","Id Is Mandatory!")
    else:
        con=create_con()
        cursor=con.cursor()
        query="delete from emp where id=%s"
        args=(e_id.get(),)
        cursor.execute(query,args)
        con.commit()
        con.close()

        e_id.delete(0,"end")
        e_ename.delete(0,"end")
        e_dept.delete(0,"end")
        e_salary.delete(0,"end")
        msg.showinfo("Delete Status","Data Is Deleted Successfully")

def refresh_data():
    e_id.delete(0,"end")
    e_ename.delete(0,"end")
    e_dept.delete(0,"end")
    e_salary.delete(0,"end")
        
root=Tk()
root.geometry("500x500")
root.title("My Desktop Application")
root.resizable(width=False,height=False)

l_id=Label(root,text="ID",font=("Vardana",15))
l_id.place(x=50,y=50)

l_ename=Label(root,text="Name",font=("Vardana",15))
l_ename.place(x=50,y=100)

l_dept=Label(root,text="Department",font=("Vardana",15))
l_dept.place(x=50,y=150)

l_salary=Label(root,text="Salary",font=("Vardana",15))
l_salary.place(x=50,y=200)

e_id=Entry(root)
e_id.place(x=170,y=50)

e_ename=Entry(root)
e_ename.place(x=170,y=100)

e_dept=Entry(root)
e_dept.place(x=170,y=150)

e_salary=Entry(root)
e_salary.place(x=170,y=200)

insert=Button(root,text="INSERT",font=("vardana",15),bg="Black",fg="White",command=insert_data)
insert.place(x=50,y=250)

search=Button(root,text="SEARCH",font=("vardana",15),bg="Black",fg="White",command=search_data)
search.place(x=180,y=250)

update=Button(root,text="UPDATE",font=("vardana",15),bg="Black",fg="White",command=update_data)
update.place(x=50,y=300)

delete=Button(root,text="DELETE",font=("vardana",15),bg="Black",fg="White",command=delete_data)
delete.place(x=180,y=300)

refresh=Button(root,text="RE-LOAD",font=("vardana",15),bg="Black",fg="White",command=refresh_data)
refresh.place(x=50,y=350)

root.mainloop()
