#Kg to gram,pound,ounce
from tkinter import *
window=Tk()
def kg_to_g():
    print(e1_val.get())
    grams=float(e1_val.get())*1000
    pounds=float(e1_val.get())*2.205
    ounces=float(e1_val.get())*35.274
    t1.insert(END,grams)
    t2.insert(END,pounds)
    t3.insert(END,ounces)
l1=Label(window,text='Kg')
l1.grid(row=0,column=1)
l2=Label(window,text='grams')
l2.grid(row=1,column=0)
l3=Label(window,text='pounds')
l3.grid(row=1,column=2)
l4=Label(window,text='ounces')
l4.grid(row=1,column=4)

e1_val=StringVar()
e1=Entry(window,textvariable=e1_val)
e1.grid(row=0,column=2,columnspan=2)
    
b1=Button(window,text='Convert',command=kg_to_g)
b1.grid(row=0,column=4)

t1=Text(window,height=1,width=10)
t1.grid(row=1,column=1)
t2=Text(window,height=1,width=10)
t2.grid(row=1,column=3)
t3=Text(window,height=1,width=10)
t3.grid(row=1,column=5)
window.mainloop()


    