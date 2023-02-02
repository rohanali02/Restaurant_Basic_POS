#Project for System Programming using tkinter
#Importing Suitable Libraries 
from tkinter import *
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
import random
from datetime import datetime
from tkinter import filedialog


#Total Button Code 
def total_bills():

#Drinks Items price
        Coke_price = 50
        Pepsi_price = 50
        Sprite_price = 50
        Sting_price = 80
        Juice_price = 50
        Shake_price = 180
        Chai_price = 60
        Kahwa_price = 60
#Foods Items Price
        Chicken_Biryani_price = 280
        Beef_Biryani_price = 350
        Burger_price = 400
        Daal_Fry_price = 200
        Karahi_price = 900
        Nihari_price = 400
        Kabab_price = 350
        rice_price = 250


#Drinks Item quantity 
        Coke_q = Coke_qty.get()
        Pepsi_q = Pepsi_qty.get()
        Sprite_q = Sprite_qty.get()
        Sting_q = Sting_qty.get()
        Juice_q = Juice_qty.get()
        Shake_q = Shake_qty.get()
        Chai_q = Chai_qty.get()
        Kahwa_q = Kahwa_qty.get()

#Foods Item quantity
        Chicken_Biryani_q = Chicken_Biryani_qty.get()
        Beef_Biryani_q = Beef_Biryani_qty.get()
        Burger_q = Burger_qty.get()
        Daal_Fry_q = Daal_Fry_qty.get()
        Karahi_q = Karahi_qty.get()
        Nihari_q = Nihari_qty.get()
        Kabab_q = Kabab_qty.get()
        rice_q = rice_qty.get()


#Drinks Items Validation
        if Coke_var.get() == 0:
                Coke_q = 0
        elif Coke_var.get() == 1 and Coke_qty.get() == "":
                messagebox.showerror("error","please fill the Coke quantity")
                Coke_q = 0

        if Pepsi_var.get() == 0:
                Pepsi_q = 0
        elif Pepsi_var.get() == 1 and Pepsi_qty.get() == "":
                messagebox.showerror("error","please fill the Pepsi quantity")
                Pepsi_q = 0

        if Sprite_var.get() == 0:
                Sprite_q = 0
        elif Sprite_var.get() == 1 and Sprite_qty.get() == "":
                messagebox.showerror("error","please fill the Sprite quantity")
                Sprite_q = 0

        if Sting_var.get() == 0:
                Sting_q = 0
        elif Sting_var.get() == 1 and Sting_qty.get() == "":
                messagebox.showerror("error","please fill the Sting quantity")
                Sting_q = 0

        if Juice_var.get() == 0:
                Juice_q = 0
        elif Juice_var.get() == 1 and Juice_qty.get() == "":
                messagebox.showerror("error","please fill the Juice quantity")
                Juice_q = 0

        if Shake_var.get() == 0:
                Shake_q = 0
        elif Shake_var.get() == 1 and Shake_qty.get() == "":
                messagebox.showerror("error","please fill the Shake quantity")
                Shake_q = 0

        if Chai_var.get() == 0:
                Chai_q = 0
        elif Chai_var.get() == 1 and Chai_qty.get() == "":
                messagebox.showerror("error","please fill the Chai quantity")
                Chai_q = 0

        if Kahwa_var.get() == 0:
                Kahwa_q = 0
        elif Kahwa_var.get() == 1 and Kahwa_qty.get() == "":
                messagebox.showerror("error","please fill the Kahwa quantity")
                Kahwa_q = 0

        
#Foods Items Validation
        if Chicken_Biryani_var.get() == 0:
                Chicken_Biryani_q = 0
        elif Chicken_Biryani_var.get() == 1 and Chicken_Biryani_qty.get() == "":
                messagebox.showerror("error","please fill the Chicken_Biryani quantity")
                Chicken_Biryani_q = 0

        if Beef_Biryani_var.get() == 0:
                Beef_Biryani_q = 0
        elif Beef_Biryani_var.get() == 1 and Beef_Biryani_qty.get() == "":
                messagebox.showerror("error","please fill the Dal Makhni quantity")
                Pepsi_q = 0

        if Burger_var.get() == 0:
                Burger_q = 0
        elif Burger_var.get() == 1 and Burger_qty.get() == "":
                messagebox.showerror("error","please fill the Mutter panner quantity")
                Burger_q = 0

        if Daal_Fry_var.get() == 0:
                Daal_Fry_q = 0
        elif Daal_Fry_var.get() == 1 and Daal_Fry_qty.get() == "":
                messagebox.showerror("error","please fill the Daal_Fry quantity")
                Daal_Fry_q = 0

        if Karahi_var.get() == 0:
                Karahi_q = 0
        elif Karahi_var.get() == 1 and Karahi_qty.get() == "":
                messagebox.showerror("error","please fill the Mix Veg quantity")
                Karahi_q = 0

        if Nihari_var.get() == 0:
               Nihari_q = 0
        elif Nihari_var.get() == 1 and Nihari_qty.get() == "":
                messagebox.showerror("error","please fill the Nihari quantity")
                Nihari_q = 0

        if Kabab_var.get() == 0:
                Kabab_q = 0
        elif Kabab_var.get() == 1 and Kabab_qty.get() == "":
                messagebox.showerror("error","please fill the Veg Biryani quantity")
                Kabab_q = 0

        if rice_var.get() == 0:
                rice_q = 0
        elif rice_var.get() == 1 and rice_qty.get() == "":
                messagebox.showerror("error","please fill the Rice quantity")
                rice_q = 0
        
        
#Total Drinks Items Price
        total_Coke_price = Coke_price * int(Coke_q)
        total_Pepsi_price = Pepsi_price * int(Pepsi_q)
        total_Sprite_price = Sprite_price * int(Sprite_q)
        total_Sting_price = Sting_price * int(Sting_q)
        total_Juice_price = Juice_price * int(Juice_q)
        total_Shake_price = Shake_price * int(Shake_q)
        total_Chai_price = Chai_price * int(Chai_q)
        total_Kahwa_price = Kahwa_price * int(Kahwa_q)

#Total Drinks cost
        total_drinks_cost = total_Coke_price + total_Pepsi_price + total_Sprite_price + total_Sting_price + total_Juice_price + total_Shake_price + total_Chai_price + total_Kahwa_price

        if drinks_cost.get() != "":
                drinks_cost.delete(0,"end")
                drinks_cost.insert("end",total_drinks_cost)
        else:
                drinks_cost.insert("end",total_drinks_cost)

        
#Total Foods Items Price
        try:
                total_Chicken_Biryani_price = Chicken_Biryani_price * int(Chicken_Biryani_q)
                total_Beef_Biryani_price = Beef_Biryani_price * int(Beef_Biryani_q)
                total_Burger_price = Burger_price * int(Burger_q)
                total_Daal_Fry_price = Daal_Fry_price * int(Daal_Fry_q)
                total_Karahi_price = Karahi_price * int(Karahi_q)
                total_Nihari_price = Nihari_price * int(Nihari_q)
                total_Kabab_price = Kabab_price * int(Kabab_q)
                total_rice_price = rice_price * int(rice_q)
        except:
                print("Enter Number Only")

 #Total Foods cost
        
        total_foods_cost = total_Chicken_Biryani_price + total_Beef_Biryani_price + total_Burger_price + total_Daal_Fry_price + total_Karahi_price + total_Nihari_price + total_Kabab_price + total_rice_price

        if foods_cost.get() != "":
                foods_cost.delete(0,"end")
                foods_cost.insert("end",total_foods_cost)
        else:
                foods_cost.insert("end",total_foods_cost)

        
        if service_charge_cost.get() != "":
                service_charge_cost.delete(0,"end")
                service_charge_cost.insert(0,"10")
        else:
                service_charge_cost.insert(0,"10")
        
        fc =  int(foods_cost.get())
        dc = int(drinks_cost.get())

        total_paid_tax = fc+dc
        total_paid_tax = total_paid_tax * 13 / 100


        if paid_tax_cost != "":
                paid_tax_cost.delete(0,"end")
                paid_tax_cost.insert(0,total_paid_tax)
        else:
                paid_tax_cost.insert(0,total_paid_tax)

        
        total_sub_cost = fc+dc+int(service_charge_cost.get())

        if sub_total_cost.get() != "":
                sub_total_cost.delete(0,"end")
                sub_total_cost.insert(0,total_sub_cost)
        else:
                sub_total_cost.insert(0,total_sub_cost)


        if total_cost_cost.get() != "":
                total_cost_cost.delete(0,"end")
                total_cost_cost.insert(0,float(total_sub_cost + total_paid_tax))
        else:
                total_cost_cost.insert(0,float(total_sub_cost + total_paid_tax))

        

#Total Bill Receipt
        date = datetime.now().date()
        if bill_details.get(1.0,"end") != "":
                bill_details.delete(1.0,"end")
                bill_details.insert(1.0,f"Billno-{random.randint(100,100000)}\t{date}  \n=====================  Items(q) \t \tAmount  ===================== \n {'Coke ('+str(Coke_q) + ')' + '         ' + str(int(Coke_q) * Coke_price) + '   '  if Coke_var.get() == 1 else''}{'Pepsi ('+str(Pepsi_q) + ')' + '        ' + str(int(Pepsi_q) * Pepsi_price) + '  '  if Pepsi_var.get() == 1 else ''}{ ' Sprite ('+str(Sprite_q) + ')' + '           ' + str(int(Sprite_q) * Sprite_price) + '  '  if Sprite_var.get() == 1 else''}{' Sting ('+str(Sting_q) + ')' + '         ' + str(int(Sting_q) * Sting_price) + '   '  if Sting_var.get() == 1 else''}{'Juice('+str(Juice_q) + ')' + '         ' + str(int(Juice_q) * Juice_price) + '   '  if Juice_var.get() == 1 else''}{'Shake('+str(Shake_q) + ')' + '           ' + str(int(Shake_q) * Shake_price) + '   '  if Shake_var.get() == 1 else''}{'Chai('+str(Chai_q) + ')' + '     ' + str(int(Chai_q) * Chai_price) + '     '  if Chai_var.get() == 1 else''}{'Kahwa('+str(Kahwa_q) + ')' + '     ' + str(int(Kahwa_q) * Kahwa_price) + '     '  if Kahwa_var.get() == 1 else''}{'Chicken_Biryani('+str(Chicken_Biryani_q) + ')' + '          ' + str(int(Chicken_Biryani_q) * Chicken_Biryani_price) + '     '  if Chicken_Biryani_var.get() == 1 else''}{'Beef Biryani('+str(Beef_Biryani_q) + ')' + '     ' + str(int(Beef_Biryani_q) * Beef_Biryani_price) + '  '  if Beef_Biryani_var.get() == 1 else''}{'Burger('+str(Burger_q) + ')' + '  ' + str(int(Burger_q) * Burger_price) + '  '  if Burger_var.get() == 1 else''}{'Daal_Fry('+str(Daal_Fry_q) + ')' + '        ' + str(int(Daal_Fry_q) * Daal_Fry_price) + '   '  if Daal_Fry_var.get() == 1 else''}{'Karahi('+str(Karahi_q) + ')' + '        ' + str(int(Karahi_q) * Karahi_price) + '   '  if Karahi_var.get() == 1 else''}{'Nihari('+str(Nihari_q) + ')' + '        ' + str(int(Nihari_q) * Nihari_price) + '   '  if Nihari_var.get() == 1 else''}{'veg biryani('+str(Kabab_q) + ')' + '    ' + str(int(Kabab_q) * Kabab_price) + '  '  if Kabab_var.get() == 1 else''}{'Rice('+str(rice_q) + ')' + '          ' + str(int(rice_q) * rice_price) + '    '  if rice_var.get() == 1 else''}\n Service charge    {service_charge_cost.get()}\n Tax paid        {paid_tax_cost.get()}\n ===================== \n Total          {total_cost_cost.get()}\n =====================")
        

        

#Save button Code

def save():
        root.filename = filedialog.asksaveasfile(mode="w",defaultextension='.txt')
        if root.filename is None:
                return
        file_save =  str(bill_details.get(1.0,END))
        root.filename.write(file_save)
        root.filename.close()


#Drinks checkbutton validation

def Coke_chk():
        if Coke_var.get() == 1:
                Coke_qty['state'] = "normal"
                Coke_qty['bg'] = '#080808'
                Coke_qty['fg'] = "white"
                
        else:
                Coke_qty['state'] = "disabled"


def Pepsi_chk():
        if Pepsi_var.get() == 1:
                Pepsi_qty['state'] = "normal"
                Pepsi_qty['bg'] = '#080808'
                Pepsi_qty['fg'] = "white"
        else:
                Pepsi_qty['state'] = "disabled"

def Sprite_chk():
        if Sprite_var.get() == 1:
                Sprite_qty['state'] = "normal"
                Sprite_qty['bg'] = '#080808'
                Sprite_qty['fg'] = "white"
        else:
                Sprite_qty['state'] = "disabled"

def Sting_chk():
        if Sting_var.get() == 1:
                Sting_qty['state'] = "normal"
                Sting_qty['bg'] = '#080808'
                Sting_qty['fg'] = "white"
        else:
                Sting_qty['state'] = "disabled"

def Juice_chk():
        if Juice_var.get() == 1:
                Juice_qty['state'] = "normal"
                Juice_qty['bg'] = '#080808'
                Juice_qty['fg'] = "white"
        else:
                Juice_qty['state'] = "disabled"

def Shake_chk():
        if Shake_var.get() == 1:
                Shake_qty['state'] = "normal"
                Shake_qty['bg'] = '#080808'
                Shake_qty['fg'] = "white"
        else:
                Shake_qty['state'] = "disabled"

def Chai_chk():
        if Chai_var.get() == 1:
                Chai_qty['state'] = "normal"
                Chai_qty['bg'] = '#080808'
                Chai_qty['fg'] = "white"
        else:
                Chai_qty['state'] = "disabled"

def Kahwa_chk():
        if Kahwa_var.get() == 1:
                Kahwa_qty['state'] = "normal"
                Kahwa_qty['bg'] = '#080808'
                Kahwa_qty['fg'] = "white"
        else:
                Kahwa_qty['state'] = "disabled"




#Foods checkbutton validation

def Chicken_Biryani_chk():
        if Chicken_Biryani_var.get() == 1:
                Chicken_Biryani_qty['state'] = "normal"
                Chicken_Biryani_qty['bg'] = '#080808'
                Chicken_Biryani_qty['fg'] = "white"
                
        else:
                Chicken_Biryani_qty['state'] = "disabled"

def Beef_Biryani_chk():
        if Beef_Biryani_var.get() == 1:
                Beef_Biryani_qty['state'] = "normal"
                Beef_Biryani_qty['bg'] = '#080808'
                Beef_Biryani_qty['fg'] = "white"
        else:
               Beef_Biryani_qty['state'] = "disabled"

def Burger_chk():
        if Burger_var.get() == 1:
                Burger_qty['state'] = "normal"
                Burger_qty['bg'] = '#080808'
                Burger_qty['fg'] = "white"
        else:
                Burger_qty['state'] = "disabled"

def Daal_Fry_chk():
        if Daal_Fry_var.get() == 1:
                Daal_Fry_qty['state'] = "normal"
                Daal_Fry_qty['bg'] = '#080808'
                Daal_Fry_qty['fg'] = "white"
        else:
                Daal_Fry_qty['state'] = "disabled"

def Karahi_chk():
        if Karahi_var.get() == 1:
                Karahi_qty['state'] = "normal"
                Karahi_qty['bg'] = '#080808'
                Karahi_qty['fg'] = "white"
        else:
                Karahi_qty['state'] = "disabled"

def Nihari_chk():
        if Nihari_var.get() == 1:
                Nihari_qty['state'] = "normal"
                Nihari_qty['bg'] = '#080808'
                Nihari_qty['fg'] = "white"
        else:
                Nihari_qty['state'] = "disabled"

def Kabab_chk():
        if Kabab_var.get() == 1:
                Kabab_qty['state'] = "normal"
                Kabab_qty['bg'] = '#080808'
                Kabab_qty['fg'] = "white"
        else:
                Kabab_qty['state'] = "disabled"

def rice_chk():
        if rice_var.get() == 1:
                rice_qty['state'] = "normal"
                rice_qty['bg'] = '#080808'
                rice_qty['fg'] = "white"
        else:
                rice_qty['state'] = "disabled"




#Exit button code
def exit():
        message = messagebox.askquestion('Notepad',"Do you want to exit the application")
        if message == "yes":
                root.destroy()
        else:
                "return"


#clear button code
def cleared_bill():
#Drinks
        Coke_qty.delete(0,'end')
        Coke.deselect()
        Coke_qty['state'] = "disabled"
        Pepsi_qty.delete(0,'end')
        Pepsi.deselect()
        Pepsi_qty['state'] = "disabled"
        Sprite_qty.delete(0,'end')
        Sprite.deselect()
        Sprite_qty['state'] = "disabled"
        Sting_qty.delete(0,'end')
        Sting.deselect()
        Sting_qty['state'] = "disabled"
        Juice_qty.delete(0,'end')
        Juice.deselect()
        Juice_qty['state'] = "disabled"
        Shake_qty.delete(0,'end')
        Shake.deselect()
        Shake_qty['state'] = "disabled"
        Chai_qty.delete(0,'end')
        Chai.deselect()
        Chai_qty['state'] = "disabled"
        Kahwa_qty.delete(0,'end')
        Kahwa.deselect()
        Kahwa_qty['state'] = "disabled"
#Drinks
        Chicken_Biryani_qty.delete(0,'end')
        Chicken_Biryani.deselect()
        Chicken_Biryani_qty['state'] = "disabled"
        Beef_Biryani_qty.delete(0,'end')
        Beef_Biryani.deselect()
        Beef_Biryani_qty['state'] = "disabled"
        Burger_qty.delete(0,'end')
        Burger.deselect()
        Burger_qty['state'] = "disabled"
        Daal_Fry_qty.delete(0,'end')
        Daal_Fry.deselect()
        Daal_Fry_qty['state'] = "disabled"
        Karahi_qty.delete(0,'end')
        Karahi.deselect()
        Karahi_qty['state'] = "disabled"
        Nihari_qty.delete(0,'end')
        Nihari.deselect()
        Nihari_qty['state'] = "disabled"
        Kabab_qty.delete(0,'end')
        Kabab.deselect()
        Kabab_qty['state'] = "disabled"
        rice_qty.delete(0,'end')
        rice.deselect()
        rice_qty['state'] = "disabled"
#Total cost
        drinks_cost.delete(0,'end')
        foods_cost.delete(0,'end')
        service_charge_cost.delete(0,'end')
        paid_tax_cost.delete(0,'end')
        sub_total_cost.delete(0,'end')
        total_cost_cost.delete(0,'end')
#Bill Details
        bill_details.delete(1.0,'end')

#Main Window code
root = tk.Tk()
root.geometry('650x400')
root.maxsize(650,390)
root.minsize(650,390)
root.title("Cafe Karachi")

frame = Frame(root,width=650,height=70,relief=RIDGE,borderwidth=5,bg='#080808')
frame.place(x=0,y=0)

l1 = Label(frame,text="Cafe Karachi",font=('roboto',30,'bold'),bg='#080808',fg="#ffffff")
l1.place(x=10,y=4)


frame1= Frame(root,width=450,height=230,relief=RIDGE,borderwidth=5,bg='#080808')
frame1.place(x=0,y=70)

innerframe1 = Frame(frame1,width=150,height=220,relief=RIDGE,borderwidth=3,bg='#080808',highlightbackground="white", highlightcolor="white", highlightthickness=2)        
innerframe1.place(x=0,y=0)

drinks  = LabelFrame(innerframe1,text="Drinks",width=135,height=205,borderwidth=3,font=('verdana',10,'bold'),fg='#080808',relief=RIDGE,highlightbackground="white", highlightcolor="white", highlightthickness=2)
drinks.place(x=2,y=2)



Coke_var = IntVar()
Coke = Checkbutton(drinks,text="Coke",variable=Coke_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=Coke_chk)
Coke.place(x=2,y=2)

Coke_qty = Entry(drinks,width=5,borderwidth=4,relief=SUNKEN,state='disabled')
Coke_qty.place(x=85,y=2)
Coke_qty.insert(0,"0")

Pepsi_var = IntVar()
Pepsi = Checkbutton(drinks,text="Pepsi",variable=Pepsi_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=Pepsi_chk)
Pepsi.place(x=2,y=22)

Pepsi_qty = Entry(drinks,width=5,borderwidth=4,relief=SUNKEN,state="disabled")
Pepsi_qty.place(x=85,y=22)

Sprite_var = IntVar()
Sprite = Checkbutton(drinks,text="Sprite",variable=Sprite_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=Sprite_chk)
Sprite.place(x=2,y=44)
Sprite_qty = Entry(drinks,width=5,borderwidth=4,relief=SUNKEN,state="disabled")
Sprite_qty.place(x=85,y=44)

Sting_var = IntVar()
Sting = Checkbutton(drinks,text="Sting",variable=Sting_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=Sting_chk)
Sting.place(x=2,y=66)
Sting_qty = Entry(drinks,width=5,borderwidth=4,relief=SUNKEN,state="disabled")
Sting_qty.place(x=85,y=66)

Juice_var = IntVar()
Juice = Checkbutton(drinks,text="Juice",variable=Juice_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=Juice_chk)
Juice.place(x=2,y=88)
Juice_qty = Entry(drinks,width=5,borderwidth=4,relief=SUNKEN,state="disabled")
Juice_qty.place(x=85,y=88)

Shake_var = IntVar()
Shake = Checkbutton(drinks,text="Shake",variable=Shake_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=Shake_chk)
Shake.place(x=2,y=110)
Shake_qty = Entry(drinks,width=5,borderwidth=4,relief=SUNKEN,state="disabled")
Shake_qty.place(x=85,y=110)

Chai_var = IntVar()
Chai = Checkbutton(drinks,text="Chai",variable=Chai_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=Chai_chk)
Chai.place(x=2,y=132)
Chai_qty = Entry(drinks,width=5,borderwidth=4,relief=SUNKEN,state="disabled")
Chai_qty.place(x=85,y=132)

Kahwa_var = IntVar()
Kahwa = Checkbutton(drinks,text="Kahwa",variable=Kahwa_var,font=('verdana',8,'bold'),onvalue=1,offvalue=0,command=Kahwa_chk)
Kahwa.place(x=2,y=154)
Kahwa_qty = Entry(drinks,width=5,borderwidth=4,relief=SUNKEN,state="disabled")
Kahwa_qty.place(x=85,y=154)


innerframe2 = Frame(frame1,width=290,height=220,relief=RIDGE,borderwidth=3,bg='#080808',highlightbackground="white", highlightcolor="white", highlightthickness=2)        
innerframe2.place(x=151,y=0)


foods  = LabelFrame(innerframe2,text="Foods",width=275,height=205,borderwidth=3,font=('verdana',10,'bold'),fg='#080808',relief=RIDGE,highlightbackground="white", highlightcolor="white", highlightthickness=2)
foods.place(x=2,y=2)

Chicken_Biryani_var = IntVar()
Chicken_Biryani = Checkbutton(foods,text="Chicken Biryani",variable=Chicken_Biryani_var,font=('verdana',8,'bold'),command=Chicken_Biryani_chk)
Chicken_Biryani.place(x=2,y=2)
Chicken_Biryani_qty = Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state="disabled")
Chicken_Biryani_qty.place(x=140,y=2)

Beef_Biryani_var = IntVar()
Beef_Biryani = Checkbutton(foods,text="Beef Biryani",variable=Beef_Biryani_var,font=('verdana',8,'bold'),command=Beef_Biryani_chk)
Beef_Biryani.place(x=2,y=22)
Beef_Biryani_qty = Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state="disabled")
Beef_Biryani_qty.place(x=140,y=22)

Burger_var = IntVar()
Burger = Checkbutton(foods,text="Burger",variable=Burger_var,font=('verdana',8,'bold'),command=Burger_chk)
Burger.place(x=2,y=44)
Burger_qty = Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state="disabled")
Burger_qty.place(x=140,y=44)

Daal_Fry_var = IntVar()
Daal_Fry = Checkbutton(foods,text="Daal Fry",variable=Daal_Fry_var,font=('verdana',8,'bold'),command=Daal_Fry_chk)
Daal_Fry.place(x=2,y=66)
Daal_Fry_qty = Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state="disabled")
Daal_Fry_qty.place(x=140,y=66)

Karahi_var = IntVar()
Karahi = Checkbutton(foods,text="Karahi",variable=Karahi_var,font=('verdana',8,'bold'),command=Karahi_chk)
Karahi.place(x=2,y=88)
Karahi_qty = Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state="disabled")
Karahi_qty.place(x=140,y=88)

Nihari_var = IntVar()
Nihari = Checkbutton(foods,text="Nihari",variable=Nihari_var,font=('verdana',8,'bold'),command=Nihari_chk)
Nihari.place(x=2,y=110)
Nihari_qty = Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state="disabled")
Nihari_qty.place(x=140,y=110)

Kabab_var = IntVar()
Kabab = Checkbutton(foods,text="Kabab",variable=Kabab_var,font=('verdana',8,'bold'),command=Kabab_chk)
Kabab.place(x=2,y=132)
Kabab_qty = Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state="disabled")
Kabab_qty.place(x=140,y=132)

rice_var = IntVar()
rice = Checkbutton(foods,text="Rice",variable=rice_var,font=('verdana',8,'bold'),command=rice_chk)
rice.place(x=2,y=154)
rice_qty = Entry(foods,width=15,borderwidth=4,relief=SUNKEN,state="disabled")
rice_qty.place(x=140,y=154)


frame2= Frame(root,width=450,height=90,relief=RIDGE,borderwidth=5,bg='#080808')
frame2.place(x=0,y=300)

innerframe3 = Frame(frame2,width=440,height=80,relief=RIDGE,borderwidth=3,bg='#080808',highlightbackground="white", highlightcolor="white", highlightthickness=2)        
innerframe3.place(x=0,y=0)


cost_of_drinks = Label(innerframe3,text="Cost of Drinks",font=('verdana',8,'bold'))
cost_of_drinks.place(x=2,y=2)
drinks_cost = Entry(innerframe3,width=13,borderwidth=4,relief=SUNKEN)
drinks_cost.place(x=130,y=0)

cost_of_foods = Label(innerframe3,text="Cost of Foods",font=('verdana',8,'bold'))
cost_of_foods.place(x=2,y=24)
foods_cost = Entry(innerframe3,width=13,borderwidth=4,relief=SUNKEN)
foods_cost.place(x=130,y=22)

service_charge = Label(innerframe3,text="Service Charge",font=('verdana',8,'bold'))
service_charge.place(x=2,y=46)
service_charge_cost = Entry(innerframe3,width=13,borderwidth=4,relief=SUNKEN)
service_charge_cost.place(x=130,y=44)


paid_tax = Label(innerframe3,text="Paid Tax",font=('verdana',8,'bold'))
paid_tax.place(x=250,y=2)
paid_tax_cost = Entry(innerframe3,width=13,borderwidth=4,relief=SUNKEN)
paid_tax_cost.place(x=330,y=0)

sub_total = Label(innerframe3,text="Sub Total",font=('verdana',8,'bold'))
sub_total.place(x=250,y=24)
sub_total_cost = Entry(innerframe3,width=13,borderwidth=4,relief=SUNKEN)
sub_total_cost.place(x=330,y=22)

total_cost = Label(innerframe3,text="Total Cost",font=('verdana',8,'bold'))
total_cost.place(x=250,y=46)
total_cost_cost = Entry(innerframe3,width=13,borderwidth=4,relief=SUNKEN)
total_cost_cost.place(x=330,y=44)

frame3= Frame(root,width=200,height=320,relief=RIDGE,borderwidth=5,bg='#080808')
frame3.place(x=450,y=70)

innerframe4 = Frame(frame3,width=190,height=310,relief=RIDGE,borderwidth=3,bg='#080808',highlightbackground="white", highlightcolor="white", highlightthickness=2)        
innerframe4.place(x=0,y=0)

bill_details = ScrolledText(innerframe4,width=23,height=17.5,relief=SUNKEN,borderwidth=3,font=('courier',9,''))
bill_details.place(x=0,y=0)


total = Button(innerframe4,text="Total",relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#080808',fg="white",command=total_bills)
total.place(x=0,y=275)

save = Button(innerframe4,text="Save",relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#080808',fg="white",command=save)
save.place(x=43,y=275)

exit = Button(innerframe4,text="Exit",relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#080808',fg="white",command=exit)
exit.place(x=82,y=275)

clr = Button(innerframe4,text="C",relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#080808',fg="white",command=cleared_bill)
clr.place(x=120,y=275)

root.mainloop()

