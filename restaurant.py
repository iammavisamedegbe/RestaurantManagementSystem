from tkinter import *
import random
import time
#main body
root=Tk()
root.geometry("1118x500+0+0")
root.title("Restaurant Management System")

#creating frames
Tops= Frame(root,width=1118,height=50,bg='powder blue',relief=SUNKEN)
Tops.pack(side=TOP)

f1= Frame(root,width=700,height=500,relief=SUNKEN)
f1.pack(side=LEFT)

f2= Frame(root,width=300,height=500,relief=SUNKEN)
f2.pack(side=RIGHT)
#time
localtime=time.asctime(time.localtime(time.time()))
#top frame
lblinfo=Label(Tops, font=('ariel',30,'bold'), text='Restaurant Management Systems', fg='steel blue',bd=5,anchor=W)
lblinfo.grid(row=0,column=0)
lblinfo=Label(Tops, font=('ariel',10,'bold'), text=localtime, fg='steel blue',bd=5,anchor=W)
lblinfo.grid(row=1,column=0)

#=================Calculator function=============
text_input= StringVar()
operator=''
def btnClick(number):
    global operator
    operator= operator + str(number)
    text_input.set( operator)

def btnClearDisplay():
    global operator
    operator=" "
    text_input.set(" ")
def btnEqualInput():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=" "

#=================f1 function=============
def Ref():
    x=random.randint(102034, 504590 )
    randRef=str(x)
    rand.set(randRef)

    CoF= float( Fries.get())
    CoD= float( Drinks.get())
    CoFilet=float(  Filet.get())
    CoBurgers=float( Burgers.get())
    CoChicken= float( Chicken.get())
    CoCheese=float(Cheese.get())

    CostOfFries= CoF * 1.99
    CostOfDrink=CoD * 1.88
    CostOfFilet =CoFilet* 2.99
    CostOfBurgers= CoBurgers *2.99
    CostOfChicken =CoChicken * 3.99
    CostOFCheese= CoCheese *2.52

    CostOfMeal="¢", str('%.2f' %(CostOfFries+CostOfDrink+CostOfFilet+CostOfBurgers+CostOfChicken+CostOFCheese))

    PayTax=((CostOfFries+CostOfDrink+CostOfFilet+CostOfBurgers+CostOfChicken+CostOFCheese)*0.2)

    TotalCost=(CostOfFries+CostOfDrink+CostOfFilet+CostOfBurgers+CostOfChicken+CostOFCheese)

    Ser_Charge=((CostOfFries+CostOfDrink+CostOfFilet+CostOfBurgers+CostOfChicken+CostOFCheese)/99)

    Service="¢", str('%.2f' %(Ser_Charge))
    OverallCost="¢", str('%.2f' %( PayTax+TotalCost+Ser_Charge))
    PaidTax="¢", str('%.2f' %(PayTax))

    Service_Charge.set(Service)
    Cost.set(CostOfMeal)
    State_Tax.set(PaidTax)
    SubTotal.set(CostOfMeal)
    Total.set(OverallCost)

def qExit():
    root.destroy()

def Reset():
    rand .set(" ")
    Fries .set(" ")
    Burgers .set(" ")
    Chicken.set(" ")
    Cheese .set(" ")
    Filet .set(" ")
    SubTotal.set(" ")
    Total .set(" ")
    Service_Charge .set(" ")
    Drinks .set(" ")
    State_Tax.set(" ")
    Tax .set(" ")
    Cost.set(" ")

#calculator
txtDisplay=Entry(f2,font=('ariel',18,'bold'),textvariable=text_input, bd=5, insertwidth=4, bg='powder blue',justify='right')
txtDisplay.grid(columnspan=5)
#buttons
btn7=Button(f2,padx=16,pady=16,bd=3,fg='black',font=('ariel',18,'bold'),text='7',bg='powder blue', command=lambda:btnClick(7))
btn7.grid(row=2,column=0)

btn8=Button(f2,padx=16,pady=16,bd=3,fg='black',font=('ariel',18,'bold'),text='8',bg='powder blue', command=lambda:btnClick(8))
btn8.grid(row=2,column=1)

btn9=Button(f2,padx=16,pady=16,bd=3,fg='black',font=('ariel',18,'bold'),text='9',bg='powder blue', command=lambda:btnClick(9))
btn9.grid(row=2,column=2)

Addition=Button(f2,padx=16,pady=16,bd=3,fg='black',font=('ariel',18,'bold'),text='+',bg='powder blue', command=lambda:btnClick('+'))
Addition.grid(row=2,column=3)

btn4=Button(f2,padx=16,pady=16,bd=3,fg='black',font=('ariel',18,'bold'),text='4',bg='powder blue', command=lambda:btnClick(4))
btn4.grid(row=3,column=0)

btn5=Button(f2,padx=16,pady=16,bd=3,fg='black',font=('ariel',18,'bold'),text='5',bg='powder blue', command=lambda:btnClick(5))
btn5.grid(row=3,column=1)

btn6=Button(f2,padx=16,pady=16,bd=3,fg='black',font=('ariel',18,'bold'),text='6',bg='powder blue', command=lambda:btnClick(6))
btn6.grid(row=3,column=2)
Substraction=Button(f2,padx=16,pady=16,bd=3,fg='black',font=('ariel',18,'bold'),text='-',bg='powder blue', command=lambda:btnClick('-'))
Substraction.grid(row=3,column=3)

btn1=Button(f2,padx=16,pady=16,bd=3,fg='black',font=('ariel',18,'bold'),text='1',bg='powder blue', command=lambda:btnClick(1))
btn1.grid(row=4,column=0)

btn2=Button(f2,padx=16,pady=16,bd=3,fg='black',font=('ariel',18,'bold'),text='2',bg='powder blue', command=lambda:btnClick(2))
btn2.grid(row=4,column=1)

btn3=Button(f2,padx=16,pady=16,bd=3,fg='black',font=('ariel',18,'bold'),text='3',bg='powder blue', command=lambda:btnClick(3))
btn3.grid(row=4,column=2)

Multiplication=Button(f2,padx=16,pady=16,bd=3,fg='black',font=('ariel',18,'bold'),text='x',bg='powder blue', command=lambda:btnClick('*'))
Multiplication.grid(row=4,column=3)

btn0=Button(f2,padx=16,pady=16,bd=3,fg='black',font=('ariel',18,'bold'),text='0',bg='powder blue', command=lambda:btnClick(0))
btn0.grid(row=5,column=0)

btnClear=Button(f2,padx=16,pady=16,bd=3,fg='black',font=('ariel',18,'bold'),text='C',bg='powder blue', command=lambda:btnClearDisplay())
btnClear.grid(row=5,column=1)

btnEquals=Button(f2,padx=16,pady=16,bd=3,fg='black',font=('ariel',18,'bold'),text='=',bg='powder blue', command=lambda:btnEqualInput())
btnEquals.grid(row=5,column=2)

Division=Button(f2,padx=16,pady=16,bd=3,fg='black',font=('ariel',18,'bold'),text='/',bg='powder blue', command=lambda:btnClick('/'))
Division.grid(row=5,column=3)
#======================Next Phase===================Restaurant Info 1==============
rand=StringVar()
Fries= StringVar()
Burgers=StringVar()
Chicken=StringVar()
Cheese=StringVar()
Filet=StringVar()
SubTotal=StringVar()
Total=StringVar()
Service_Charge=StringVar()
Drinks=StringVar()
State_Tax=StringVar()
Tax=StringVar()
Cost=StringVar()
lblReference=Label(f1,font=('ariel',15,'bold'),text='Reference',bd='10')
lblReference.grid(row=0,column=0)
txtReference=Entry(f1,font=('ariel',15,'bold'),textvariable=rand,bd='10',bg='powder blue', insertwidth=4,justify='right')
txtReference.grid(row=0,column=1)

lblFries=Label(f1,font=('ariel',15,'bold'),text='Large Fries',bd='10')
lblFries.grid(row=1,column=0)
txtFries=Entry(f1,font=('ariel',15,'bold'),textvariable=Fries,bd='10',bg='powder blue', insertwidth=4,justify='right')
txtFries.grid(row=1,column=1)

lblBurgers=Label(f1,font=('ariel',15,'bold'),text='Burger Meals',bd='10')
lblBurgers.grid(row=2,column=0)
txtBurgers=Entry(f1,font=('ariel',15,'bold'),textvariable=Burgers,bd='10',bg='powder blue', insertwidth=4,justify='right')
txtBurgers.grid(row=2,column=1)

lblFilet=Label(f1,font=('ariel',15,'bold'),text='Filet_o_Meals',bd='10')
lblFilet.grid(row=3,column=0)
txtFilet=Entry(f1,font=('ariel',15,'bold'),textvariable=Filet,bd='10',bg='powder blue', insertwidth=4,justify='right')
txtFilet.grid(row=3,column=1)

lblChicken=Label(f1,font=('ariel',15,'bold'),text='Chicken Meal',bd='10')
lblChicken.grid(row=4,column=0)
txtChicken=Entry(f1,font=('ariel',15,'bold'),textvariable=Chicken,bd='10',bg='powder blue', insertwidth=4,justify='right')
txtChicken.grid(row=4,column=1)

lblCheese=Label(f1,font=('ariel',15,'bold'),text='Cheese Meals',bd='10')
lblCheese.grid(row=5,column=0)
txtCheese=Entry(f1,font=('ariel',15,'bold'),textvariable=Cheese,bd='10',bg='powder blue', insertwidth=4,justify='right')
txtCheese.grid(row=5,column=1)

#======================Next Phase===================Restaurant Info 2==============
lblDrinks=Label(f1,font=('ariel',15,'bold'),text='Drinks',bd='10')
lblDrinks.grid(row=0,column=2)
txtDrinks=Entry(f1,font=('ariel',15,'bold'),textvariable=Drinks,bd='10',bg='#ffffff',insertwidth=4,justify='right')
txtDrinks.grid(row=0,column=3)

lblCost=Label(f1,font=('ariel',15,'bold'),text='Cost',bd='10')
lblCost.grid(row=1,column=2)
txtCost=Entry(f1,font=('ariel',15,'bold'),textvariable=Cost,bd='10',bg='#ffffff', insertwidth=4,justify='right')
txtCost.grid(row=1,column=3)

lblService=Label(f1,font=('ariel',15,'bold'),text='Service',bd='10')
lblService.grid(row=2,column=2)
txtService=Entry(f1,font=('ariel',15,'bold'),textvariable=Service_Charge,bd='10',bg='#ffffff', insertwidth=4,justify='right')
txtService.grid(row=2,column=3)

lblStateTax=Label(f1,font=('ariel',15,'bold'),text='StateTax',bd='10')
lblStateTax.grid(row=3,column=2)
txtStateTax=Entry(f1,font=('ariel',15,'bold'),textvariable=State_Tax,bd='10',bg='#ffffff', insertwidth=4,justify='right')
txtStateTax.grid(row=3,column=3)

lblSubTotal=Label(f1,font=('ariel',15,'bold'),text='SubTotal',bd='10')
lblSubTotal.grid(row=4,column=2)
txtSubTotal=Entry(f1,font=('ariel',15,'bold'),textvariable=SubTotal,bd='10',bg='#ffffff', insertwidth=4,justify='right')
txtSubTotal.grid(row=4,column=3)

lblTotal=Label(f1,font=('ariel',15,'bold'),text='Total',bd='10')
lblTotal.grid(row=5,column=2)
txtTotal=Entry(f1,font=('ariel',15,'bold'),textvariable=Total,bd='10',bg='#ffffff', insertwidth=4,justify='right')
txtTotal.grid(row=5,column=3)

#==================Buttons================
btnTotal=Button(f1, padx=13, pady=3, bd=10, fg='black',font=('ariel',12,'bold'),width=10, text='Total', bg='powder blue', command=lambda:Ref())
btnTotal.grid(row=7,column=1)

btnReset=Button(f1, padx=13, pady=3, bd=10, fg='black',font=('ariel',12,'bold'),width=10, text='Reset', bg='powder blue', command=lambda:Reset())
btnReset.grid(row=7,column=2)

btnqExit=Button(f1, padx=13, pady=3, bd=10, fg='black',font=('ariel',12,'bold'),width=10, text='Exit', bg='powder blue', command=lambda:qExit())
btnqExit.grid(row=7,column=3)
root.mainloop()