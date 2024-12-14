how to add this to my github profile:SHOP MANAGEMENT SYSTEM
PROGRAM:
#PROJECT FOR SHOP MANAGEMENT SYSTEM
#IMPORTING REQUIRED MODULES
import tkinter
from tkinter import *
from tkinter import Tk
from tkinter import messagebox
from tkinter import font
import mysql.connector
#connecting to the database and creating table
db=mysql.connector.connect(user='root',passwd='',host='localhost')
my_cursor=db.cursor()#creating cursor object
my_cursor.execute("CREATE DATABASE IF NOT EXISTS shop")#creating the database named library
db=mysql.connector.connect(user='root',passwd='',host='localhost',db='shop')
my_cursor=db.cursor()
#query to create a table products
query="CREATE TABLE IF NOT EXISTS products(date VARCHAR(10),prodName VARCHAR(20),prodPrice VARCHAR(50))"
my_cursor.execute(query)#executing the query
db=mysql.connector.connect(user='root',passwd='',host='localhost',database='shop')
my_cursor=db.cursor()
#query to create a table sale
query="CREATE TABLE IF NOT EXISTS sale(custName VARCHAR(20),date VARCHAR(10),prodName VARCHAR(30),qty INTEGER,price INTEGER)"
my_cursor.execute(query)#executing the query
#Function to add the product to the database
def prodtoTable():
    #getting the user inputs of product details from the user
    pname=prodName.get()
    price=prodPrice.get()
    dt=date.get()
    #connecting to the database
    db=mysql.connector.connect(user='root',passwd='',host='localhost',database='shop')
    cursor=db.cursor()
    #query to add the product details to the table
    query="INSERT INTO products(date,prodName,prodPrice) VALUES(%s,%s,%s)"
    details=(dt,pname,price)
    #executing the query and showing the pop up message
    try:
        cursor.execute(query,details)
        db.commit()
        messagebox.showinfo('Success',"Product added successfully")
        wn.mainloop()
    except Exception as e:
        print("The exception is:",e)
        messagebox.showinfo("Error","Trouble adding data into Database")
        wn.destroy()
#Function to get details of the product to be added
def addProd():
    global prodName,prodPrice,date,Canvas1,wn
    #Creating the window
    wn=tkinter.Tk()
    wn.title("THILLAI'S SHOP MANAGEMENT SYSTEM")
    wn.configure(bg='mint cream')
    wn.minsize(width=500,height=500)
    wn.geometry("700x600")
    Canvas1=Canvas(wn)
    Canvas1.config(bg='LightBlue1')
    Canvas1.pack(expand=True,fill=BOTH)
    headingFrame1=Frame(wn,bg='LightBlue1',bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel=Label(headingFrame1,text="Add a Product",fg='grey19',font=('Courier',15,'bold'))
    headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)
    labelFrame=Frame(wn)
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
    #getting date
    label1=Label(labelFrame,text="Date:",fg='black')
    label1.place(relx=0.05,rely=0.3,relheight=0.08)
    date=Entry(labelFrame)
    date.place(relx=0.3,rely=0.3,relwidth=0.62,relheight=0.08)
    #product Name
    lable2=Label(labelFrame,text='Product Name:',fg='black')
    lable2.place(relx=-0.2,rely=0.45,relwidth=0.62,relheight=0.08)
    prodName=Entry(labelFrame)
    prodName.place(relx=0.3,rely=0.45,relwidth=0.62,relheight=0.08)
    # Product Price
    lable3 = Label(labelFrame,text="Product Price : ", fg='black')
    lable3.place(relx=0.05,rely=0.6, relheight=0.08)
        
    prodPrice = Entry(labelFrame)
    prodPrice.place(relx=0.3,rely=0.6, relwidth=0.62, relheight=0.08)
    #Add Button
    btn=Button(wn,text="ADD",bg='#d1ccc0',fg='black',command=prodtoTable)
    btn.place(relx=0.28,rely=0.85,relwidth=0.18,relheight=0.08)
    Quit=Button(wn,text="Quit",bg='#f7f1e3',fg='black',command=wn.destroy)
    Quit.place(relx=0.53,rely=0.85,relwidth=0.18,relheight=0.08)
    wn.mainloop()
#function to remove the product from the database
def removeProd():
    #getting the product name from the user to be removed
    name=prodName.get()
    name=name.lower()
    #connecting to the database
    db=mysql.connector.connect(user='root',passwd='',host='localhost',database='shop')
    cursor=db.cursor()
    #query to delete the respective product from the database
    query="DELETE from products where LOWER(prodName)='"+name+"'"
    #executing the query and showing the message box
    try:
        cursor.execute(query)
        db.commit()
        #cur.execute(deleteIssue)
        #con.commit()
        messagebox.showinfo('Success',"Product Record Deleted Successfully")
    except Exception as e:
        print("The exception is:",e)
        messagebox.showinfo("Please check Product Name")
        wn.destroy()
#function to get product details from the user to be deleted
def delProd():
    global prodName,Canvas1,wn
    #creating a window
    wn=tkinter.Tk()
    wn.title("THILLAI'S SHOP MANAGEMENT SYSTEM")
    wn.configure(bg="mint cream")
    wn.minsize(width=500,height=500)
    wn.geometry("700x600")
    Canvas1=Canvas(wn)
    Canvas1.config(bg="misty rose")
    Canvas1.pack(expand=True,fill=BOTH)
    headingFrame1=Frame(wn,bg="misty rose",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel=Label(headingFrame1,text="Delete Product",fg='grey19',font=('Courier',15,'bold'))
    headingLabel.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)
    LabelFrame=Frame(wn)
    LabelFrame.place(relx=0,rely=0.3,relwidth=1,relheight=1)
    #product name to delete
    lable=Label(LabelFrame,text="Product Name:",fg="black")
    lable.place(relx=0.05,rely=0.5)
    prodName=Entry(LabelFrame)
    prodName.place(relx=0.3,rely=0.5,relwidth=0.62)
    #delete button
    btn=Button(wn,text="DELETE",bg='#d1ccc0',fg='black',command=removeProd)
    btn.place(relx=0.28,rely=0.9,relwidth=0.18,relheight=0.08)
    wn.mainloop()
#Function to show all the products in the database
def viewProds():
    global wn
    #creating the window to show the products details
    wn=tkinter.Tk()
    wn.title("THILLAI'S SHOP MANAGEMENT SYSTEM")
    wn.configure(bg='mint cream')
    wn.minsize(width=500,height=500)
    wn.geometry("700x600")
    Canvas1=Canvas(wn)
    Canvas1.config(bg="old lace")
    Canvas1.pack(expand=True,fill=BOTH)
    headingFrame1=Frame(wn,bg='old lace',bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel=Label(headingFrame1,text="View Products",fg='black',font=('Courier',15,'bold'))
    headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)
    labelFrame=Frame(wn)
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y=0.25
    #connecting to database
    db=mysql.connector.connect(user="root",passwd='',host="localhost",database="shop")
    cursor=db.cursor()
    #query to select all products from the table
    query='SELECT * FROM products'
    Label(labelFrame,text="%-50s%-50s%-50s"%('Date','Product','Price'),font=('calibri',11,'bold'),fg='black').place(relx=0.07,rely=0.1)
    Label(labelFrame,text="-------------------------------------------------------------------------------------------------------",fg='black').place(relx=0.05,rely=0.2)
    #executing the query and showing the products details
    try:
        cursor.execute(query)
        res=cursor.fetchall()
        for i in res:
            Label(labelFrame,text="%-50s%-50s%-50s"%(i[0],i[1],i[2]),fg='black').place(relx=0.07,rely=y)
            y+=0.1
    except Exception as e:
        print("The exception is:",e)
        messagebox.showinfo("Failed to fetch files from database")
        Quit=Button(wn,text="Quit",bg='#f71e3',fg='black',command=wn.destroy)
        Quit.place(relx=0.4,rely=0.9,relwidth=0.18,relheight=0.08)
        wn.mainloop()
#Function to generate the bill
def bill():
    #creating a window
    wn=tkinter.Tk()
    wn.title("THILLAI'S SHOP MANAGEMENT SYSTEM")
    wn.configure(bg='lavender blush2')
    wn.minsize(width=500,height=500)
    wn.geometry("700x600")
    headingFrame1=Frame(wn,bg="lavender blush2",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel=Label(headingFrame1,text="Bill",fg="grey19",font=('Courier',15,'bold'))
    headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)
    labelFrame=Frame(wn)
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y=0.35
    Label(labelFrame,text="%-40s%-40s%-40s%-40s"%('Product','Price','Quantity','Total'),font=('calibri',11,'bold'),fg='black').place(relx=0.07,rely=0.2)
    #getting date and customer name
    dt=date.get()
    cName=custName.get()
    print(cName,dt)
    totalBill=0
    #Connecting to database
    db=mysql.connector.connect(user="root",passwd="",host="localhost",database="Shop")
    cursor=db.cursor()
    #query to select all the products
    query='SELECT* FROM products'
    cursor.execute(query)
    res=cursor.fetchall()
    print(res)
    c=len(res)
    print("c is printed here ",c)
    #Checking if the quantity of the product is entered and calculating price,showing it on window and adding to database
    for j in range(0,c):
        print("name get is printed",name[j].get())
        if(name[j].get()!=0):
            i=res[j]
            print("printed here",i[1],i[2])
            qty=int(name[j].get())
            print(qty)
            print("qty is printed",qty)
            total=qty*int(i[2])
            print(total)
            Label(labelFrame,text="%-40s%-40s%-40s%-40s"%(i[1],i[2],qty,total),fg='black').place(relx=0.07,rely=y)
            totalBill+=total
            print(totalBill)
            y+=0.1
            query="INSERT INTO sale(custName,date,prodName,qty,price) VALUES(%s,%s,%s,%s,%s)"
            details=(cName,dt,i[1],qty,total)
            #executing the query and showing the pop up message
            try:
                cursor.execute(query,details)
            except Exception as e:
                print("The exception is:",e)
                messagebox.showinfo("Error","Trouble adding data into Database")
                wn.destroy()
    db.commit()
    messagebox.showinfo('Success',"Bill added successfully")
    wn.mainloop()
    #showing total of the bill
    Label(labelFrame,text="--------------------------------------------------------------------------------",fg='black').place(relx=0.05,rely=y)
    y+=0.1
    Label(labelFrame,text="\t\t\t\t\t\t\t\t"+str(totalBill),fg='black').place(relx=0.07,rely=y)
    Quit=Button(wn,text="Quit",bg='#f7f1e3',fg='black',command=wn.destroy)
    Quit.place(relx=0.53,rely=0.9,relwidth=0.18,relheight=0.08)
    wn.mainloop()
#Function to take the inputs from the user to generate bill
def newCust():
    global wn,name,date,custName,res
    #creating a window
    wn=tkinter.Tk()
    wn.title("THILLAI'S SHOP MANAGEMENT SYSTEM")
    wn.configure(bg='lavender blush2')
    wn.minsize(width=500,height=500)
    wn.geometry("700x600")
    headingFrame1=Frame(wn,bg="lavender blush2",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel=Label(headingFrame1,text="New Customer",fg='grey19',font=('Courier',15,'bold'))
    headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)
    lable1=Label(wn,text="Date:",fg='black')
    lable1.place(relx=0.05,rely=0.3)
    #getting date
    date=Entry(wn)
    date.place(relx=0.3,rely=0.3,relwidth=0.62)
    lable2=Label(wn,text="Customer Name:",fg="black")
    lable2.place(relx=0.05,rely=0.4)
    #Getting customer name
    custName=Entry(wn)
    custName.place(relx=0.3,rely=0.4,relwidth=0.62)
    labelFrame=Frame(wn)
    labelFrame.place(relx=0.1,rely=0.45,relwidth=0.8,relheight=0.4)
    y=0.3
    Label(labelFrame,text="Please enter the quantity of the products you want to buy",font=('calibri',11,'bold'),fg='black').place(relx=0.07,rely=0.1)
    Label(labelFrame,text="%-50s%-50s%-30s"%('Product','Price','Quantity'),font=('calibri',11,'bold'),fg='black').place(relx=0.07,rely=0.2)
    
    #connecting to the database
    db=mysql.connector.connect(user="root",passwd="",host="localhost",database='Shop')
    cursor=db.cursor()
    query='SELECT* FROM products'
    cursor.execute(query)
    res=cursor.fetchall()
    print(res)
    c=len(res)
    name=res
    #showing all the products and creating entries to take the input of the quantity
    for j in range(0,c):
        i=res[j]
        Label(labelFrame,text="%-50s%-50s"%(i[1],i[2]),fg='black').place(relx=0.07,rely=y)
        name[j]=Entry(labelFrame)
        name[j].place(relx=0.6,rely=y,relwidth=0.2)
        y+=0.1
    #button to generate bill
    Btn=Button(wn,text="Generate Bill",bg='#d1ccc0',fg='black',command=bill)
    Btn.place(relx=0.28,rely=0.7,relwidth=0.18,relheight=0.08)
    Quit = Button(wn,text="Quit",bg='#f7f1e3', fg='black', command=wn.destroy)
    Quit.place(relx=0.55,rely=0.7, relwidth=0.18,relheight=0.08)
    wn.mainloop()
def home():
    wn=tkinter.Tk()
    wn.title("Shop Management System")
    wn.configure(bg='honeydew2')
    wn.minsize(width=500,height=500)
    wn.geometry("700x600")
    headingFrame1=Frame(wn,bg="snow3",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel=Label(headingFrame1,text="Welcome to THILLAI's Shop \n Shop Management System",fg='grey19',font=('Courier',15,'bold'))
    headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)
    #Button to add a new product
    btn1=Button(wn,text="Add a Product",bg='LightBlue1',fg='black',width=20,height=2,command=addProd)
    btn1['font']=font.Font(size=12)
    btn1.place(x=270,y=175)
    #Button to delete a product
    btn2=Button(wn,text="Delete a Product",bg='misty rose',fg='black',width=20,height=2,command=delProd)
    btn2['font']=font.Font(size=12)
    btn2.place(x=270,y=255)
    #Button to view all products
    btn3=Button(wn,text="View Products",bg='old lace',fg='black',width=20,height=2,command=viewProds)
    btn3['font']=font.Font(size=12)
    btn3.place(x=270,y=335)
    #Button to add a new sale and generate bill
    btn4=Button(wn,text="New Customer",bg='lavender blush2',fg='black',width=20,height=2,command=newCust)
    btn4['font']=font.Font(size=12)
    btn4.place(x=270,y=415)
    #Button to quit
    btn5=Button(wn,text="Quit",bg='lightgreen',fg="black",width=20,height=2,command=wn.destroy)
    btn5['font']=font.Font(size=12)
    btn5.place(x=270,y=495)
    wn.mainloop()

home()        



