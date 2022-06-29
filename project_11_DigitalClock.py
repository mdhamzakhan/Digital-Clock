import tkinter as tn
import datetime 

def date_time():
    time = datetime.datetime.now()
    hr = time.strftime("%I")
    mins = time.strftime("%M")
    sec = time.strftime("%S")
    am = time.strftime("%p")
    block_hr.config(text=hr)
    block_min.config(text=mins)
    block_sec.config(text=sec)
    block_am.config(text=am)
    # ***
    date = time.strftime("%d")
    month = time.strftime("%m")
    year = time.strftime("%y")
    day = time.strftime("%a")
    block_date.config(text=date)
    block_mon.config(text=month)
    block_year.config(text=year)
    block_day.config(text=day)

    block_hr.after(200,date_time)
clock = tn.Tk()

clock.title("Digital_Clock")
clock.geometry('1000x500')
clock.config(bg='black')

block_hr =tn.Label(clock,text="00",font=("arial",60,"bold"),bg="red",fg="white")
block_hr.place(x=120,y=50,height=110,width=100)
block_hr_txt =tn.Label(clock,text="Hours",font=("arial",20,"bold"),bg="red",fg="white")
block_hr_txt.place(x=120,y=190,height=40,width=100)

block_min =tn.Label(clock,text="00",font=("arial",60,"bold"),bg="red",fg="white")
block_min.place(x=340,y=50,height=110,width=100)
block_min_txt =tn.Label(clock,text="Min",font=("arial",20,"bold"),bg="red",fg="white")
block_min_txt.place(x=340,y=190,height=40,width=100)

block_sec =tn.Label(clock,text="00",font=("arial",60,"bold"),bg="red",fg="white")
block_sec.place(x=560,y=50,height=110,width=100)
block_sec_txt =tn.Label(clock,text="Sec",font=("arial",20,"bold"),bg="red",fg="white")
block_sec_txt.place(x=560,y=190,height=40,width=100)

block_am =tn.Label(clock,text="00",font=("arial",45,"bold"),bg="red",fg="white")
block_am.place(x=780,y=50,height=110,width=100)
block_am_txt =tn.Label(clock,text="Am/PM",font=("arial",20,"bold"),bg="red",fg="white")
block_am_txt.place(x=780,y=190,height=40,width=100)

# ******************************************************************************************

block_date =tn.Label(clock,text="00",font=("arial",60,"bold"),bg="red",fg="white")
block_date.place(x=120,y=270,height=110,width=100)
block_date_txt =tn.Label(clock,text="Date",font=("arial",20,"bold"),bg="red",fg="white")
block_date_txt.place(x=120,y=410,height=40,width=100)

block_mon =tn.Label(clock,text="00",font=("arial",60,"bold"),bg="red",fg="white")
block_mon.place(x=340,y=270,height=110,width=100)
block_mon_txt =tn.Label(clock,text="year",font=("arial",20,"bold"),bg="red",fg="white")
block_mon_txt.place(x=340,y=410,height=40,width=100)

block_year =tn.Label(clock,text="00",font=("arial",60,"bold"),bg="red",fg="white")
block_year.place(x=560,y=270,height=110,width=100)
block_year_txt =tn.Label(clock,text="year",font=("arial",20,"bold"),bg="red",fg="white")
block_year_txt.place(x=560,y=410,height=40,width=100)

block_day =tn.Label(clock,text="00",font=("arial",40,"bold"),bg="red",fg="white")
block_day.place(x=780,y=270,height=110,width=100)
block_day_txt =tn.Label(clock,text="day",font=("arial",20,"bold"),bg="red",fg="white")
block_day_txt.place(x=780,y=410,height=40,width=100)


date_time()
clock.mainloop()