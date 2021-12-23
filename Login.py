from tkinter import *
root=Tk()
#creating a layout
root.geometry("500x300")
def move():
    root=Tk()
    #creating a layout
    root.geometry("500x300")

    def log():
        db=open("database.txt","r")
        db=open("database.txt","a")

        value1=nameentry.get()
        value2=passwordentry.get()

        if not len(value1 or value2)<1:
            d=[]
            f=[]
            for i in db:
                a,b=i.split(",")
                b=b.strip()
                d.append(a)
                f.append(b)
                data=dict(zip(d,f))
            try:
                if data[value1]:
                    try:
                        if value2 == data[value1]:
                            print("Login successfully")
                            print("Hi,",value1)
                        else:
                            print("Password or name incorrect")
                    except:
                        print("incorrect password or name")
                else:
                    print("name or password doesn't exist")
            except:
                print("name or password doesn't exist")
        else:
            print("Please enter a value")

    #creating a label
    Label(root,text="Python login Form",font="ar 15 bold").grid(row=0,column=3)

    #labeling fields
    name=Label(root,text="Name")
    password=Label(root,text="Password")

    #packing fields
    name.grid(row=1,column=2)
    password.grid(row=2,column=2)

    #valiables for storing data
    nameValue=StringVar
    passwordValue=StringVar

    #creating entry fields
    nameentry=Entry(root,textvariable=nameValue)
    passwordentry=Entry(root,textvariable=passwordValue)
    
    #packing all entry fields
    nameentry.grid(row=1,column=3)
    passwordentry.grid(row=2,column=3)
    Button(text="Submits",command=log).grid(row=3,column=3)
    root.mainloop()
def getvals():
    db=open("database.txt","r")
    db=open("database.txt","a")
    value1=nameentry.get()
    value2=emailentry.get()
    value3=passwordentry.get()
    value4=confirmentry.get()
    if value3!=value4:
        print("Password dont match,restart")
    else:
        if len(value3)<=6:
            print("Password too short,restart:")
       
        else:
            db.write(value1+","+value2+","+value3+","+value4+"\n")
            print("success!")

#creating a label
Label(root,text="Python Registration Form",font="ar 15 bold").grid(row=0,column=3)
#labeling fields
name=Label(root,text="Name")
email=Label(root,text="Email")
password=Label(root,text="Password")
confirm=Label(root,text="Confirm Password")
#packing fields
name.grid(row=1,column=2)
email.grid(row=2,column=2)
password.grid(row=3,column=2)
confirm.grid(row=4,column=2)
#valiables for storing data
nameValue=StringVar
emailValue=StringVar
passwordValue=StringVar
confirmValue=StringVar
#creating entry fields
nameentry=Entry(root,textvariable=nameValue)
emailentry=Entry(root,textvariable=emailValue)
passwordentry=Entry(root,textvariable=passwordValue)
confirmentry=Entry(root,textvariable=confirmValue)
#packing all entry fields
nameentry.grid(row=1,column=3)
emailentry.grid(row=2,column=3)
passwordentry.grid(row=3,column=3)
confirmentry.grid(row=4,column=3)
Button(text="Register",command=getvals).grid(row=7,column=3)
Button(text="Login",command=move).grid(row=8,column=3)



root.mainloop()