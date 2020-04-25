from _datetime import datetime
import tkinter as tk
from tkinter import ttk
from _datetime import *
from tkinter import messagebox
import datetime

win = tk.Tk()
win.title('Age Calculate')
win.geometry('600x400')
win.iconbitmap('icon.ico')     

############################################ Frame ############################################

canvas=tk.Canvas(win,width=310,height=190)
canvas.grid()
image = tk.PhotoImage(file=r"E:\Python Practice\Age_calculate\pic.png")
canvas.create_image(0,0,anchor='nw',image=image)

frame = ttk.Frame(win)
frame.place(x=40,y=220)

########################################## Label on Window Page ##########################################
ab = ttk.Label(win,text='This is Age Calculate Calculator ',font = ('',12,'bold'))
ab.place(x=320,y=80)

ab = ttk.Label(win,text='Show Reasult After Sumit',font = ('',12,'bold'))
ab.place(x=340,y=160)
# ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,, End ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

############################################ Label on Frame ############################################

name = ttk.Label(frame,text = 'Name : ',font = ('',12,'bold'))
name.grid(row=0,column=0,sticky = tk.W)

year = ttk.Label(frame,text = 'Year : ',font = ('',12,'bold'))
year.grid(row=1,column=0,sticky = tk.W)

month = ttk.Label(frame,text = 'Month : ',font = ('',12,'bold'))
month.grid(row=2,column=0,sticky = tk.W)

date = ttk.Label(frame,text = 'Date : ',font = ('',12,'bold'))
date.grid(row=3,column=0,sticky = tk.W)
# ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,, End ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

############################################ Entry Box ############################################
name_entry = ttk.Entry(frame,width=25)
name_entry.grid(row=0,column=1)
name_entry.focus()

date_entry = ttk.Entry(frame,width=25)
date_entry.grid(row=3,column=1,pady=5)
# ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,, End ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

############################################ Spin Box ############################################

var =tk.IntVar()
year_entry = ttk.Combobox(frame,width=22,textvariable=var,state='readonly')
year_entry['value'] = (1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,
2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020)
year_entry.current(0)
year_entry.grid(row=1,column=1,pady=5)


var2=tk.IntVar()
month_entry = ttk.Combobox(frame,width=22,textvariable=var2,state='readonly')
month_entry['value'] = (1,2,3,4,5,6,7,8,9,10,11,12)
month_entry.current(5)
month_entry.grid(row=2,column=1)
# ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,, End ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

def calculate_age():
    try:
        name = name_entry.get()
        bday = Person(name,datetime.date(int(year_entry.get()),int(month_entry.get()),int(date_entry.get())))
        
        textArea = tk.Text(master=win,height=10,width=30)
        textArea.grid(column=1,row=6)
        answer = "Heyy {bady}!!!.You are {age} years old!!! ".format(bady=name, age=bday.age())
        textArea.insert(tk.END,answer)

    # Clear Entry Box after click sumit Button
        name_entry.delete(0,tk.END)
        date_entry.delete(0,tk.END)

    except ValueError:
        return messagebox.askretrycancel('Warning','Plzz Enter Detail and Currect DOB ?')
    


btn = tk.Button(frame,text='Sumit',width=10,font = ('',11,'bold'),command=calculate_age,bg='pink')
btn.grid(row=4,column=1)


class Person:
    def __init__(self,name,birthdate):
        self.name = name
        self.birthdate = birthdate
    def age(self):
        today = datetime.date.today()
        age = today.year-self.birthdate.year
        return age

win.mainloop()
