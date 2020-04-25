import tkinter as tk
from tkinter import ttk, messagebox
import math,random,os

class Billing:
    def __init__(self,win):
        self.win=win
        win.title('Billing Software')
        win.geometry('1350x700+0+0')
        
        l = tk.Label(self.win,text='Prashant Retail Shop',bg='#A93226',fg='yellow',font=('',25,'bold'),relief='groove',pady=10)
        l.pack(fill=tk.X)

        f = tk.LabelFrame(self.win,text='Customer Details',bd=10,bg='#CB4335',relief='groove',fg='#1C2833',font=('',13,'bold'))
        f.place(x=0,y=67,relwidth=1)
        ################################ Variables #########################################
        self.cname=tk.StringVar()
        self.phone_no=tk.StringVar()
        self.cbill_no=tk.StringVar()
        x=random.randint(1000,9999)
        self.cbill_no.set(str(x))
        self.search=tk.StringVar()
        
        ########## Cosmetics ##########
        self.cos_info = {
            'soap': tk.IntVar(),
            'creame': tk.IntVar(),
            'wash': tk.IntVar(),
            'spray': tk.IntVar(),
            'gel': tk.IntVar(),
            'loshion': tk.IntVar()
        }

        ########## Cosmetics ##########
        self.grocery_info = {
            'rice': tk.IntVar(),
            'oil': tk.IntVar(),
            'daal': tk.IntVar(),
            'wheat': tk.IntVar(),
            'sugar': tk.IntVar(),
            'tea': tk.IntVar()
            
        }

        ########## Cosmetics ##########
        self.drink_info = {
            'maza': tk.IntVar(),
            'coak': tk.IntVar(),
            'frooti': tk.IntVar(),
            'thumbs': tk.IntVar(),
            'limka': tk.IntVar(),
            'sprite': tk.IntVar()
        }

        ########## Total Cosmetics, Grocery, Drink variable ##########
        self.total_var = {
            'cosmetic':tk.StringVar(),
            'grocery':tk.StringVar(),
            'drink':tk.StringVar()
        }

        ########## GST Cosmetics, Grocery, Drink variable ##########
        self.gst_var = {
            'c_gst':tk.StringVar(),
            'g_gst':tk.StringVar(),
            'd_gst':tk.StringVar()
        }

        cname_l = tk.Label(f,text='Customer Name',background='#CB4335',fg='white',font=('',15,'bold'))
        cname_l.grid(row=0,column=0,padx=20,pady=5)

        cname_entry=tk.Entry(f,width=20,font=('',15,''),textvariable=self.cname)
        cname_entry.grid(row=0,column=1,padx=5,pady=10)
        cname_entry.focus()


        cnum_l = tk.Label(f,text='Contact No.',background='#CB4335',fg='white',font=('',15,'bold'))
        cnum_l.grid(row=0,column=2,padx=10)

        cnum_entry=tk.Entry(f,width=20,font=('',15,''),textvariable=self.phone_no)
        cnum_entry.grid(row=0,column=3,padx=5,pady=10)

        cbill_l = tk.Label(f,text='Bill No.',background='#CB4335',fg='white',font=('',15,'bold'))
        cbill_l.grid(row=0,column=4,padx=10)

        cbill_entry=tk.Entry(f,width=20,font=('',15,''),textvariable=self.cbill_no)
        cbill_entry.grid(row=0,column=5,padx=5,pady=10)

        


        ################################ Cosmetics Frame #########################################

        f2 = tk.LabelFrame(self.win,text='Cosmetics',bd=10,bg='#CB4335',relief='groove',fg='black',font=('',13,'bold'))
        f2.place(x=0,y=148,width=325,height=380)

        self.labels = ['Bath Soap','Face Creame','Face Wash','Hair Spray','Haire Gel','Body Loashion']

        counter=0
        for i in range(len(self.labels)):
            l=tk.Label(f2,text=self.labels[i],font=('',15,'bold'),pady=5,padx=5,bg='#CB4335',fg='#E1DDDD')
            l.grid(row=i,column=0,sticky=tk.W,pady=10)

        for i in self.cos_info:
            entry = tk.Entry(f2,width=10,font=('',12,'bold'),relief='groove',textvariable=self.cos_info[i])
            entry.grid(row=counter,column=1,padx=18)
            counter+=1

        ################################ Grocery Frame #########################################

        f3 = tk.LabelFrame(self.win,text='Grocery',bd=10,bg='#CB4335',relief='groove',fg='black',font=('',13,'bold'))
        f3.place(x=330,y=148,width=325,height=380)

        labels = ['Rice','Food Oil','Daal','Wheat','Sugar','Tea']

        counter=0
        for i in range(len(labels)):
            l=tk.Label(f3,text=labels[i],font=('',15,'bold'),pady=5,padx=5,bg='#CB4335',fg='#E1DDDD')
            l.grid(row=i,column=0,sticky=tk.W,pady=10)

        for i in self.grocery_info:
            entry = tk.Entry(f3,width=10,font=('',12,'bold'),relief='groove',textvariable=self.grocery_info[i])
            entry.grid(row=counter,column=1,padx=18)
            counter+=1

        ################################### Cold Drinks ###########################################

        f4 = tk.LabelFrame(self.win,text='Cold Drinks',bd=10,bg='#CB4335',relief='groove',fg='black',font=('',13,'bold'))
        f4.place(x=660,y=148,width=325,height=380)

        labels = ['Maza','Cock','Frooti','Thumbs Up','Limca','Sprite']

        counter=0
        for i in range(len(labels)):
            l=tk.Label(f4,text=labels[i],font=('',15,'bold'),pady=5,padx=5,bg='#CB4335',fg='#E1DDDD')
            l.grid(row=i,column=1,sticky=tk.W,pady=10)

        for i in self.drink_info:
            entry = tk.Entry(f4,width=10,font=('',12,'bold'),relief='groove',textvariable=self.drink_info[i])
            entry.grid(row=counter,column=2,padx=18)
            counter+=1

        ################################### Bill Area ###########################################

        f5 = tk.LabelFrame(self.win,text='',bd=10,bg='white',relief='groove',fg='yellow')
        f5.place(x=993,y=148,width=365,height=380)

        bill_title = tk.Label(f5,text='Bill Area',font=('',15,'bold'),relief='groove',bg='#CB4335',bd=7)
        bill_title.pack(fill=tk.X)

        scroll_y=tk.Scrollbar(f5,orient='vertical')
        self.textarea=tk.Text(f5,yscrollcommand=scroll_y.set)
        scroll_y.pack(fill=tk.Y,side=tk.RIGHT)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=tk.BOTH,expand=1)

        
        ################################### Buttons Frame ###########################################

        f6 = tk.LabelFrame(self.win,text='Billing Menu',bd=10,bg='#CB4335',relief='groove',fg='#1C2833',font=('',13,'bold'))
        f6.place(x=0,y=533,width=1353,height=160)

        label1 = ['Total Cosmetic Price','Total Grocery Price','Total Cold Drink Price']
        label2 = ['Cosmetic GST','Grocery GST','Cold Drink GST']

        counter=0
        for i in range(len(label1)):
            l1=tk.Label(f6,text=label1[i],font=('',15,'bold'),pady=5,padx=5,bg='#CB4335',fg='White')
            l1.grid(row=i,column=0,sticky=tk.W,pady=2)

        for i in self.total_var: 
            l1_entry =tk.Entry(f6,width=15,textvariable=self.total_var[i],font=('',12,'bold'),relief='groove')
            l1_entry.grid(row=counter,column=1,padx=18)
            counter+=1

        count=0
        for i in range(len(label2)):
            l1=tk.Label(f6,text=label2[i],font=('',15,'bold'),pady=5,padx=5,bg='#CB4335',fg='White')
            l1.grid(row=i,column=2,sticky=tk.W,pady=2)

        for i in self.gst_var:
            l2_entry=tk.Entry(f6,width=15,textvariable=self.gst_var[i],font=('',12,'bold'),relief='groove')
            l2_entry.grid(row=count,column=4,padx=22)
            count+=1


        ##################################### Buttons ############################################

        btn_f7 = tk.LabelFrame(f6,text='',bd=7,bg='white',relief='groove')
        btn_f7.place(x=745,y=8,width=585,height=110)

        total_btn=tk.Button(btn_f7,text="Total",command=self.total,width=10,bg='#63403C',fg='white',pady=15,font=('',15,'bold'))
        total_btn.grid(row=0,column=0,padx=5,pady=10)

        total_btn=tk.Button(btn_f7,text="Generate Bill",command=self.bill_area,width=10,bg='#63403C',fg='white',padx=5,pady=15,font=('',15,'bold'))
        total_btn.grid(row=0,column=1,padx=5,pady=10)

        total_btn=tk.Button(btn_f7,text="Clear",command=self.clear,width=10,bg='#63403C',fg='white',pady=15,font=('',15,'bold'))
        total_btn.grid(row=0,column=2,padx=5,pady=5)

        total_btn=tk.Button(btn_f7,text="Exit",command=self.iExit,width=10,bg='#63403C',fg='white',pady=15,font=('',15,'bold'))
        total_btn.grid(row=0,column=3,padx=5,pady=5)

        search=tk.Button(f,text='Search',command=self.find_bill,width=15)
        search.grid(row=0,column=6,padx=20)
        
        self.bill_welcom()

    def total(self):
        self.total_cos_price = float(
            (self.cos_info['soap'].get()*50)+
            (self.cos_info['creame'].get()*160)+
            (self.cos_info['wash'].get()*120)+
            (self.cos_info['spray'].get()*90)+
            (self.cos_info['gel'].get()*30)+
            (self.cos_info['loshion'].get()*45)
        ) 
        self.total_var['cosmetic'].set(str(self.total_cos_price))
        self.c_tax = round((self.total_cos_price*0.05),2)
        self.gst_var['c_gst'].set("Rs. "+str(self.c_tax))
        
        self.total_grocery_price = (
            (self.grocery_info['rice'].get()*42)+
            (self.grocery_info['oil'].get()*115)+
            (self.grocery_info['daal'].get()*75)+
            (self.grocery_info['wheat'].get()*28)+
            (self.grocery_info['sugar'].get()*45)+
            (self.grocery_info['tea'].get()*150)
        ) 
        self.total_var['grocery'].set(str(self.total_grocery_price))
        self.g_tax = round((self.total_grocery_price*0.1),2)
        self.gst_var['g_gst'].set("Rs. "+str(self.g_tax))

        
        self.total_drink_price = (
            (self.drink_info['maza'].get()*65)+
            (self.drink_info['coak'].get()*70)+
            (self.drink_info['frooti'].get()*85)+
            (self.drink_info['thumbs'].get()*60)+
            (self.drink_info['limka'].get()*70)+
            (self.drink_info['sprite'].get()*75)
        ) 
        self.total_var['drink'].set(str(self.total_drink_price))
        self.d_tax = round((self.total_drink_price*0.2),2)
        self.gst_var['d_gst'].set("Rs. "+str(self.d_tax))

    def bill_welcom(self):
        self.textarea.delete('1.0',tk.END)
        self.textarea.insert(tk.END,'\tPrashant Retail Management \n')
        self.textarea.insert(tk.END,f'\n Bill No : {self.cbill_no.get()}')
        self.textarea.insert(tk.END,f'\n Customer Name : {self.cname.get()}')
        self.textarea.insert(tk.END,f'\n Phone No. : {self.phone_no.get()}')
        self.textarea.insert(tk.END,'\n########################################')
        self.textarea.insert(tk.END,'\n Product\t\tQty\t\tPrice')
        self.textarea.insert(tk.END,'\n########################################\n')

    def bill_area(self):    # For Generate Bill Button
        if self.cname.get()=='' or self.phone_no.get()=='':
            messagebox.askyesno('Error','PLease Enter Custor Name OR Phone No.')
        
        elif self.total_cos_price == 0 and self.total_grocery_price==0 and self.total_drink_price==0:        
            messagebox.askretrycancel('Error','Please Enter Produnct Qty')
        
        else:
            self.bill_welcom()
            # this dictionary for one pice price use 
            self.cosmetic_one_pc = {
                'soap':50,
                'wash':160,
                'creame':120,
                'spray':90,
                'gel':30,
                'loshion':45
            }
            self.grocery_one_pc ={
                'rice':42,
                'oil':115,
                'daal':75,
                'wheat':28,
                'sugar':45,
                'tea':150
            }

            self.drink_one_pc = {
                'maza':65,
                'coak':70,
                'frooti':85,
                'thumbs':60,
                'limka':70,
                'sprite':75
            }
        # Print Amount Products
            for k,v in self.cos_info.items():
                if v.get()!=0:
                    # item dict*one pice dict access {key} then print {value}
                    cos_total = int(self.cos_info[k].get())*self.cosmetic_one_pc[k] 
                    self.textarea.insert(tk.END,f'{k}\t\t{v.get()}\t\t{float(cos_total)}\n')
            for k,v in self.grocery_info.items():
                if v.get()!=0:
                    grocery_total = int(self.grocery_info[k].get())*self.grocery_one_pc[k]
                    self.textarea.insert(tk.END,f'{k}\t\t{v.get()}\t\t{float(grocery_total)}\n')
            for k,v in self.drink_info.items():
                if v.get()!=0:
                    drink_total = int(self.drink_info[k].get())*self.drink_one_pc[k]
                    self.textarea.insert(tk.END,f'{k}\t\t{v.get()}\t\t{float(drink_total)}\n')
            # GST Print Bill Area of Product 
            self.textarea.insert(tk.END,'........................................\n')
            for i,j in self.gst_var.items():
                if j.get()!='Rs. 0.0':
                    self.textarea.insert(tk.END,f'{i}\t\t\t     {j.get()}\n')
                
            self.textarea.insert(tk.END,'........................................\n')
        # Add GST + Amount and show Bill Area
            total_amount = (self.c_tax+
                        self.g_tax+
                        self.d_tax+
                        self.total_cos_price+
                        self.total_grocery_price+
                        self.total_drink_price
                        )
            self.textarea.insert(tk.END,f'Total Amount\t\t\t\t{str(total_amount)}')
            self.save_bill()
    
    def save_bill(self):
        op=messagebox.askyesno("Save File","Do You Want To Save Bill")
        if op>0:
            self.data = self.textarea.get('1.0',tk.END)
            f1 = open(f'E:\Python Projects\Billing/'+str(self.cbill_no.get())+'.txt','w')
            f1.write(self.data)
            f1.close()
            messagebox.showinfo('Saved',f'Bill No : {self.cbill_no.get()} saved successfully')
        else:
            return

    def find_bill(self):
        present='no'
        for i in os.listdir('E:\Python Projects\Billing/'):
            if i.split('.')[0]==self.cbill_no.get():
                f1=open(f'E:\Python Projects\Billing/{i}','r')
                self.textarea.delete('1.0',tk.END)
                for b in f1:
                    self.textarea.insert(tk.END,b)
                f1.close()
                present='yes'
        if present=='no':
            messagebox.showerror('Error','Invalid Bill No.')
                            
    def clear(self):
        op=messagebox.askyesno('Clear','Do you want to clear')
        if op>0:
            self.textarea.delete('1.0',tk.END)
            self.cname.set("")
            self.phone_no.set("")
            self.cbill_no.set(int(self.cbill_no.get())+int(1))
            for i in self.cos_info:    
                self.cos_info[i].set(0)
            for i in self.grocery_info:
                self.grocery_info[i].set(0)
            for i in self.drink_info:
                self.drink_info[i].set(0)
            for i in self.total_var:
                self.total_var[i].set(float(0))
            for i in self.gst_var:
                self.gst_var[i].set(float(0))
            self.bill_welcom()

    def iExit(self):
        exit=tk.messagebox.askyesno("Exit Restaurant System","Confirm if you want to exit")
        if exit > 0:
            win.destroy()
            return






win = tk.Tk()
obj = Billing(win)
win.mainloop()
