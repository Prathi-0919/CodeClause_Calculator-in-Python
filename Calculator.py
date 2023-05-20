from tkinter import*

def B_Click(number):
    global value
    value=value + str(number)
    data.set(value)

def B_Cancel():
    global value
    value=""
    data.set("")

def B_Equal():
    global value
    Result=str(eval(value))
    data.set(Result)
root = Tk()
root.title("PS Calculator")
root.geometry("500x509+460+125")
value=""
data=StringVar()
screen=Entry(root,textvariable=data,bd=25,justify="right",bg="orchid4",font=("Comic Sans MS",27))
screen.grid(row=0,columnspan=4)
B7=Button(root,text="7",font=("Comic Sans MS",15,"bold"),bg="pale violet red",bd=12,height=2,width=6,command=lambda:B_Click(7))
B7.grid(row=1,column=0)

B8=Button(root,text="8",font=("Comic Sans MS",15,"bold"),bg="thistle",bd=12,height=2,width=6,command=lambda:B_Click(8))
B8.grid(row=1,column=1)

B9=Button(root,text="9",font=("Comic Sans MS",15,"bold"),bd=12,bg="pale violet red",height=2,width=6,command=lambda:B_Click(9))
B9.grid(row=1,column=2)

B_add=Button(root,text="+",font=("Comic Sans MS",15,"bold"),bg="yellow green",bd=12,height=2,width=6,command=lambda:B_Click("+"))
B_add.grid(row=1,column=3)

B4=Button(root,text="4",font=("Comic Sans MS",15,"bold"),bg="thistle",bd=12,height=2,width=6,command=lambda:B_Click(4))
B4.grid(row=2,column=0)

B5=Button(root,text="5",font=("Comic Sans MS",15,"bold"),bg="pale violet red",bd=12,height=2,width=6,command=lambda:B_Click(5))
B5.grid(row=2,column=1)

B6=Button(root,text="6",font=("Comic Sans MS",15,"bold"),bg="thistle",bd=12,height=2,width=6,command=lambda:B_Click(6))
B6.grid(row=2,column=2)

B_sub=Button(root,text="-",font=("Comic Sans MS",15,"bold"),bg="yellow green",bd=12,height=2,width=6,command=lambda:B_Click("-"))
B_sub.grid(row=2,column=3)

B1=Button(root,text="1",font=("Comic Sans MS",15,"bold"),bg="pale violet red",bd=12,height=2,width=6,command=lambda:B_Click(1))
B1.grid(row=3,column=0)

B2=Button(root,text="2",font=("Comic Sans MS",15,"bold"),bg="thistle",bd=12,height=2,width=6,command=lambda:B_Click(2))
B2.grid(row=3,column=1)

B3=Button(root,text="3",font=("Comic Sans MS",15,"bold"),bg="pale violet red",bd=12,height=2,width=6,command=lambda:B_Click(3))
B3.grid(row=3,column=2)

B_multiply=Button(root,text="*",font=("Comic Sans MS",15,"bold"),bg="yellow green",bd=12,height=2,width=6,command=lambda:B_Click("*"))
B_multiply.grid(row=3,column=3)

B_cancel=Button(root,text="C",font=("Comic Sans MS",15,"bold"),bg="thistle",bd=12,height=2,width=6,command= B_Cancel)
B_cancel.grid(row=4,column=0)

B0=Button(root,text="0",font=("Comic Sans MS",15,"bold"),bg="pale violet red",bd=12,height=2,width=6,command=lambda:B_Click(0))
B0.grid(row=4,column=1)

B_division=Button(root,text="÷",font=("Comic Sans MS",15,"bold"),bg="yellow green",bd=12,height=2,width=6,command=lambda:B_Click("/"))
B_division.grid(row=4,column=3)

B_equal=Button(root,text="=",font=("Comic Sans MS",15,"bold"),bg="thistle",bd=12,height=2,width=6,command= B_Equal)
B_equal.grid(row=4,column=2)
root.mainloop()
