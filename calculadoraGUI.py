from operações import *
from tkinter import *
from functools import partial
#baseTkinter------------------------------------------------------------------------------------------------
janelaC = Tk()
janelaC.geometry("277x560+50+50")
janelaC.resizable(False,False)
frame1=Frame(janelaC,width=30,height=10)
frame1.grid(row=0,column=0,sticky="WE")
janelaC.title("Calculadora")
displayvar=StringVar()
displayvar.set("0")
display=Label(frame1,bg="white",textvariable=displayvar,height=2,font=("Arial",25),anchor=CENTER)
display.pack(side=TOP,fill=BOTH)
#funçoes----------------------------------------------------------------------------------------------------
n1=0
n2=0
operador=""
def addn(button):
    a=displayvar.get()
    button=button["text"]
    if button=="." and a[-1] in ["/","+","-","x","^","."]:
        return 0
    if a!="0" or button==".":
        displayvar.set(a+button)
    else:
        displayvar.set(button)
def deletelast():
    global operador
    a=displayvar.get()
    a=list(a)
    b=a.pop()
    displayvar.set("".join(a))
    if displayvar.get()=="":
        displayvar.set("0")
    if b in ["/","+","-","x","^"]:
        operador=""
def deleteall():
    global n1,n2,operador
    displayvar.set("0")
    n1,n2,=0,0
    operador=""
def operações(button):
    global n1,n2,operador
    a=displayvar.get()
    if n1==0:
        n1=a
    if operador=="":
        operador=button["text"]
        displayvar.set(a+operador)
        return 0
    if n1!=0 and operador!="":
        b=displayvar.get()
        finalproduct=b.split(operador)
        try:
            n2=int(finalproduct[1])
        except:
            n2=float(finalproduct[1])
        try:
            n1=int(finalproduct[0])
        except:
            n1=float(finalproduct[0])
        displayvar.set((operaçõesST(n1,n2,operador)))
        b=displayvar.get()
        if ".0" in b:
            b=list(b)
            b.pop()
            b.pop()
            displayvar.set("".join(b))
        n1=0
        n2=0
        operador=""
def resultado():
    global n1,n2,operador
    if operador=="" or n1==0:
        return 0
    b=displayvar.get()
    finalproduct=b.split(operador)
    try:
         n2=int(finalproduct[1])
    except:
         n2=float(finalproduct[1])
    try:
        n1=int(finalproduct[0])
    except:
        n1=float(finalproduct[0])
    displayvar.set((operaçõesST(n1,n2,operador)))
    b=displayvar.get()
    if ".0" in b:
        b=list(b)
        b.pop()
        b.pop()
        displayvar.set("".join(b))
    n1=0
    n2=0
    operador=""
#botoes---------------------------------
f1=Frame(janelaC)
f1.grid(row=1,column=0,sticky=NW)
#---------------------------------------
b1=Button(f1,text="1",font=("Ariel",36))
b1.config(command=partial(addn,b1))
b1.grid(row=0,column=0,sticky="NEWS")


b2=Button(f1,text="2",font=("Ariel",36))
b2.config(command=partial(addn,b2))
b2.grid(row=0,column=1,sticky="NEWS")

b3=Button(f1,text="3",font=("Ariel",36))
b3.config(command=partial(addn,b3))
b3.grid(row=0,column=2,sticky="NEWS")

b4=Button(f1,text="+",font=("Ariel",36))
b4.config(command=partial(operações,b4))
b4.grid(row=0,column=3,sticky="NEWS")
#---------------------------------------

b5=Button(f1,text="4",font=("Ariel",36))
b5.config(command=partial(addn,b5))
b5.grid(row=1,column=0,sticky="NEWS")

b6=Button(f1,text="5",font=("Ariel",36))
b6.config(command=partial(addn,b6))
b6.grid(row=1,column=1,sticky="NEWS")

b7=Button(f1,text="6",font=("Ariel",36))
b7.config(command=partial(addn,b7))
b7.grid(row=1,column=2,sticky="NEWS")

b8=Button(f1,text="-",font=("Ariel",36))
b8.config(command=partial(operações,b8))
b8.grid(row=1,column=3,sticky="NEWS")

#---------------------------------------

b9=Button(f1,text="7",font=("Ariel",36))
b9.config(command=partial(addn,b9))
b9.grid(row=2,column=0,sticky="NEWS")

b10=Button(f1,text="8",font=("Ariel",36))
b10.config(command=partial(addn,b10))
b10.grid(row=2,column=1,sticky="NEWS")

b11=Button(f1,text="9",font=("Ariel",36))
b11.config(command=partial(addn,b11))
b11.grid(row=2,column=2,sticky="NEWS")

b12=Button(f1,text="x",font=("Ariel",36))
b12.config(command=partial(operações,b12))
b12.grid(row=2,column=3,sticky="NEWS")

#---------------------------------------

b13=Button(f1,text="⌫",font=("Ariel",15),command=deletelast)
b13.grid(row=3,column=0,sticky="NEWS")

b14=Button(f1,text="0",font=("Ariel",36))
b14.config(command=partial(addn,b14))
b14.grid(row=3,column=1,sticky="NEWS")

b15=Button(f1,text=".",font=("Ariel",36))
b15.config(command=partial(addn,b15))
b15.grid(row=3,column=2,sticky="NEWS")

b16=Button(f1,text="/",font=("Ariel",36))
b16.config(command=partial(operações,b16))
b16.grid(row=3,column=3,sticky="NEWS")

#---------------------------------------

b17=Button(f1,text="^",font=("Ariel",36))
b17.config(command=partial(operações,b17))
b17.grid(row=4,column=0,sticky="NEWS")

b18=Button(f1,text="C",font=("Ariel",36),command=deletelast)
b18.grid(row=4,column=1,sticky="NEWS")

b19=Button(f1,text="CE",font=("Ariel",15),command=deleteall)
b19.grid(row=4,column=2,sticky="NEWS")

b20=Button(f1,text="=",font=("Ariel",36),command=resultado)
b20.grid(row=4,column=3,sticky="NEWS")
#---------------------------------------
janelaC.mainloop()
