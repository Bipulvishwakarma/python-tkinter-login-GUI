from tkinter import *
root=Tk()
root.geometry("400x300")
frame = Frame(root)
frame.pack()
#frame.pack(fill=BOTH, expand=False)

signin=Label(frame,text="Sign In",font="bold").grid(row=0,column=2)

email_address=Label(frame,text="Email address",font="bold").grid(row=1,column=2,sticky="W")
password=Label(frame,text="Password",font="bold").grid(row=3,column=2,sticky="W")


email_address=Entry(frame,text="",width="50").grid(row=2,column=2,padx=0,pady=0,ipady=3)
password=Entry(frame,text="",width="50",show="*").grid(row=4,column=2,padx=0,pady=0,ipady=3)

checkbtn=Checkbutton(frame,text="Remember me").grid(row=5,column=2,sticky="W")

submit=Button(frame,text="Submit",width="42",bg="blue",fg="white").grid(row=6,column=2,padx=0,pady=0,ipady=3)

def fun(event):
	print("change password")



pwd=Label(frame,text="forgot password ?",fg="blue")
pwd.grid(row=8,column=2,padx=0,pady=0,ipady=3,sticky="E")

pwd.bind("<Button>",fun)

root.mainloop()
