import os    
import random
from datetime import datetime
import ntplib
import time
from time import ctime
from tkinter import*    
from tkinter import ttk  
from tkinter import messagebox 
from tkinter import filedialog
from tkcalendar import Calendar,DateEntry
from PIL import ImageTk  
import sqlite3
import smtplib
from email.message import EmailMessage
from validate_email import validate_email
import pycountry
import phonenumbers
from phonenumbers.phonenumberutil import region_code_for_number
from phonenumbers.phonenumberutil import region_code_for_country_code

class win1(Tk):
    new=None
    def __init__(self,*arg):       # Constructors
        Tk.__init__(self,*arg)
        photo = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
        self.iconphoto(False, photo)
        F1 = Frame(self,bg="black",relief=GROOVE,bd=10)
        F1.pack()
        lab1=Label(F1,text='Welcome to',font=('Comic Sans MS',35),fg='red',bg="black",width=13)
        lab1.pack()
        lab2=Label(F1,text='Plasma Finder',bg="black",font=('Comic Sans MS',40,'bold'),fg='#994483',width=25)
        lab2.pack()
        lab1=Label(F1,text='Creator---                    ',bg="black",font=('Times',35,'bold'),fg='green',width=17,justify='right')
        lab1.pack()
        lab1=Label(F1,text='  Sanjeevani Sharma',font=('Verdana',30),bg="black",fg='lightgreen',width=23)
        lab1.pack()
        bottom=Frame()
        bottom.pack()
        but=Button(bottom,text='NEW USER',font=('Courier',15,'bold'),fg='#436632',bg='#abcdef',width=33,cursor='hand2',
                   activebackground='#86cc64',command=self.open1)
        but.pack(side='left')
        but=Button(bottom,text='EXISTING USER',font=('Courier',15,'bold'),fg='#436632',bg='#abcdef',width=34
                   ,cursor='hand2',
                   activebackground='#86cc64',command=self.open2)
        but.pack(side='right')

    def open1(self,*arg):  # Function calls window 2 that is Signup window
        self.destroy()
        win2().mainloop()

    def open2(self,*arg):  # Function calls Login window
        self.destroy()     # Used to destroy window
        root=Tk()
        clas=U_login(root)
        win1.new=clas
        
class win2(Tk):
    def __init__(self,*arg):
        Tk.__init__(self,*arg)
        self.title("Signup".center(420))  # title for Window 
        self.configure(background = "black")  # background color for window 
        self.geometry("1350x700+0+0")
        photo = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
        self.iconphoto(False, photo)

        self.bg_icon = ImageTk.PhotoImage(file="Pics\\1 (8).jpg")
        
        bg_color ="#074463"
        font_=("times new roman")

        title= Label(self, bd=10, relief=GROOVE, text="User SignUp Page", font=(font_,40,"bold"),bg=bg_color,fg="gold").pack(side=TOP, fill=X)
        bg_lbl = Label(self, image=self.bg_icon).pack(fill=Y) 

        self.uname=StringVar()
        self.pasw=StringVar()
        self.email=StringVar()
        self.gender=StringVar()
        self.contact=StringVar()
        self.dob=StringVar()
        

        now = datetime.now()
        self.today= now.strftime("%d/%m/%Y")
        self.label,self.calender="",""


        Manage_Frame=Frame(self,bd=10, relief=RIDGE,bg=bg_color)
        Manage_Frame.place(x=430, y=100, width=500, height=550)
        m_title=Label(Manage_Frame,text="SIGN UP", compound=LEFT, bg=bg_color,fg="white",font=(font_,30,"bold"))
        m_title.grid(row=0, columnspan=2,pady=20)

        lbl1=Label(Manage_Frame,text="Username",  bg=bg_color,fg="white",font=(font_,20,"bold"))
        lbl1.grid(row=1, column=0,padx=20,pady=10,sticky="w")

        txt1=Entry(Manage_Frame,textvariable=self.uname,  bd=5,relief=GROOVE,font=(font_,15,"bold"))
        txt1.grid(row=1, column=1,padx=20,pady=10,sticky="w")

        lbl2=Label(Manage_Frame,text="Password",  bg=bg_color,fg="white",font=(font_,20,"bold"))
        lbl2.grid(row=2, column=0,padx=20,pady=10,sticky="w")

        txt2=Entry(Manage_Frame,textvariable=self.pasw,  bd=5,relief=GROOVE,font=(font_,15,"bold"))
        txt2.grid(row=2, column=1,padx=20,pady=10,sticky="w")

        lbl3=Label(Manage_Frame,text="Email",  bg=bg_color,fg="white",font=(font_,20,"bold"))
        lbl3.grid(row=3, column=0,padx=20,pady=10,sticky="w")

        txt3=Entry(Manage_Frame,textvariable=self.email,  bd=5,relief=GROOVE,font=(font_,15,"bold"))
        txt3.grid(row=3, column=1,padx=20,pady=10,sticky="w")

        self.label=(Label(Manage_Frame,text="D.O.B", bg=bg_color,fg="white",font=(font_,20,"bold")))
        self.label.grid(row=4, column=0,padx=20,pady=10,sticky="w")
        
        self.calendar=(DateEntry(Manage_Frame, textvariable=self.dob,font=("times new roman",18,"bold"), locale='en_GB', width=16,state="readonly"))
        self.calendar.place(x=180, y=290, anchor="w")


        gender_lbl=Label(Manage_Frame,text="Gender",  bg=bg_color,fg="white",font=(font_,20,"bold"))
        gender_lbl.grid(row=5, column=0,padx=20,pady=10,sticky="w")
        
        # ================== Combobox (used to create Drop down Menu) ====================================       
        
        gender=ttk.Combobox(Manage_Frame,textvariable=self.gender, font=(font_,13,"bold"),width=21,state="readonly")
        gender['values']=("Male","Female","Others")
        gender.grid(row=5, column=1,padx=20,pady=10,sticky="w")



        lbl6=Label(Manage_Frame,text="Contact",  bg=bg_color,fg="white",font=(font_,20,"bold"))
        lbl6.grid(row=6, column=0,padx=20,pady=10,sticky="w")

        self.code=IntVar()
        self.code.set(0)
        combo_code = OptionMenu(Manage_Frame, self.code,"+93","+355","+213","+1684","+376","+244","+1264","+672","+1268","+54","+374","+297","+61","+880","+32","+226","+359","+387","+1246","+681","+590","+1441","+673","+591","+973","+257","+229","+975","+1876","+267","+685","+599","+55","+1242","+441534","+375","+501","+7","+250","+381","+670","+262","+993","+992","+40","+690","+245","+1671","+502","+30","+240","+590","+81","+592","+441481","+594","+995","+1473","+44","+241","+503","+224","+220","+299","+350","+233","+968","+216","+962","+385","+509","+36","+852""+504","+58","+1787","+1939","+970","+680","+351","+47","+595","+964","+507","+689","+675","+51","+92","+63","+870","+48","+508","+260","+212","+372","+20","+27","+593","+39","+84","+677","+251","+252","+263","+966","+34","+291","+382","+373","+261","+590","+212","+377","+998","+95","+223","+853","+976","+692","+389","+230","+356","+265","+960","+596","+1670","+1664","+222","+441624","+256","+255","+60","+52","+972","+33","+246","+290","+358","+679","+500","+691","+298","+505","+31","+47","+264","+678","+687","+227","+672","+234","+64","+977","+674","+683","+682","+225","+41","+57","+86","+237","+56","+61","+1","+242","+236","+243","+420","+357","+61","+506","+599","+238","+53","+268","+963","+599","+996","+254","+211","+597","+686","+855","+1869","+269","+239","+421","+82","+386","+850","+965","+221","+378","+232","+248","+7","+1345","+65","+46","+249","+1809","1-829","+1767","+253","+45","+1-284","+49","+967","+213","+1","+598","+262","+1","+961","+1758","+856","+688","+886","+1868","+90","+94","+423","+371","+676","+370","+352","+231","+266","+66","+228","+235","+1649","+218","+379","+1784","+971","+376","+1268","+93","+1264","+1340","+354","+98","+374","+355","+244","+1684","+54","+61","+43","+297","+91","+35818","+994","+353","+62","+380","+974","+258" )
        combo_code.place(x=180, y=390)
        combo_code.config(bg="#ffe5b4",bd=0,activebackground="#ffe5b4")

        txt6=Entry(Manage_Frame,textvariable=self.contact,  bd=3,relief=GROOVE,font=(font_,12,"bold"))
        txt6.place(x=227, y=390)

        
        Button_Frame=Frame(Manage_Frame,bd=4, relief=RIDGE,bg=bg_color)
        Button_Frame.place(x=10, y=450,width=460,height=70)

        btn_sgnup = Button(Button_Frame, text="SignUp",width =8, command = self.signup, font="bold").grid(row = 0,column=0,padx=15,pady=15 )
        btn_back = Button(Button_Frame, text="Back",width =8, command = self.back, font="bold").grid(row = 0,column=1,padx=15,pady=15 )
        btn_Clear = Button(Button_Frame, text="Clear",width =8, command = self.clear, font="bold").grid(row = 0,column=2,padx=15,pady=15 )
        btn_Exit = Button(Button_Frame, text="Exit",width =8, command = self.exit, font="bold").grid(row = 0,column=3,padx=15,pady=15 )
        btn_Signup_hos = Button(self, text="Hos_SignUp",width =15, command = self.h_signup,bd=5,relief=GROOVE, bg="red",activebackground="red", activeforeground="white",fg="white",font="bold").place(x=1000, y=20)
    
    def exit(self):
        self.destroy()  
    
    def h_signup(self):
        self.destroy()
        win3().mainloop()

    def clear(self):
        self.uname.set("")
        self.pasw.set("")
        self.email.set("")
        self.gender.set("")
        self.contact.set("")
        self.code.set(0)
        self.dob.set(self.today)
    
    
    def signup(self): 
        is_valid1 = validate_email(self.email.get())
        
        if self.uname.get()=="" and self.contact.get()=="" and self.pasw.get=="" and self.email.get()=="" and self.gender.get()=="" and self.dob.get()==self.today :
            return messagebox.showerror("Error","All Fields Required")
        
        if is_valid1 == False:
            return messagebox.showerror("Error","Email not valid")  
        
        if self.uname.get()==""  :
            return messagebox.showerror("Error","Username Required")
        
        if self.pasw.get=="" :
            return messagebox.showerror("Error","Password Required")
        
        if len(str(self.pasw.get()))<8:
            return messagebox.showerror("Error","Password should of minimum 8 character")
        
        if self.email.get()=="" :
            return messagebox.showerror("Error","Email Required")
            
        if self.gender.get()==""  :
            return messagebox.showerror("Error","Gender Required")

        if self.dob.get()>=self.today  :
            return messagebox.showerror("Error","DOB Not Possible")
        
        if self.contact.get()==""  :
            return messagebox.showerror("Error","Contact Required")
        
        try:
            temp=self.contact.get()
            int(temp)
        except ValueError:
            return messagebox.showerror("Error","Contact should be Integer")
 
        if len(str(self.contact.get()))<10 or len(str(self.contact.get()))>10 :
            return messagebox.showerror("Error","Contact should consist of 10 numbers")     
        
        else:
            self.otp = str(random.randint(100000,999999))
            #print(self.otp)

            self.conn=sqlite3.connect("plasma.db")
            self.c=self.conn.cursor()
            self.find_user = ("SELECT * FROM user WHERE Email= ?  or Phone_No = ?")
            self.c.execute(str(self.find_user),(self.email.get(),self.contact.get()))
            results = (self.c).fetchall()
            if results:
                messagebox.showerror("Error","Email or Contact  is already Used")
            else:
            
                send = smtplib.SMTP("smtp.gmail.com", 587)  # Create session for Gmail
                send.starttls()  # transport layer

                #===================Plain Text=====================

                msg = EmailMessage()
                msg["Subject"] = "OTP"
                msg["From"] = "aj147ps@gmail.com"
                msg["To"] = self.email.get()
                msg.set_content("Hi!"+str(self.uname.get())+" your OTP for registration is: "+"\'"+self.otp+"\'")        
                    
                try:
                    send.login("aj147ps@gmail.com","xcavbfayvnthixwy")
                except smtplib.SMTPAuthenticationError:
                    messagebox.showerror("Error","Error Occur Otp Not")    

                try:
                    try:
                        try:
                            send.send_message(msg)
                            messagebox.showinfo("Mailed","OTP Sent to Your Mail Id")                        
                            self.root2 = Toplevel()  # Child Window "Tk() can Also be use here"
                            self.root2.title("OTP")
                            self.root2.geometry("700x320+350+150")
                            self.root2.configure(bg="black")
                            photo2 = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
                            self.root2.iconphoto(False, photo2)
                            self.root2.focus_force() 
                            self.root2.grab_set()  
                            self.root2.resizable(False, False)
                        
                            title_child = Label(self.root2, text="ENTER OTP", bg="#152238", fg="white",compound=LEFT, font=("Goudy Old Style", 48, "bold"), anchor="w").place(x=0, y=0, relwidth=1)
                        
                            otp_lbl = Label(self.root2, text="Enter OTP", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=150)
                            self.otp_entry = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
                            self.otp_entry.place(x=230, y=150)

                            verify_btn = Button(self.root2, text="verify", font=("times new roman", 18, "bold"), activebackground="#262626",activeforeground="white", bg="#262626", fg="white", cursor="hand2", command=self.verify).place(x=300, y=260, width=140, height=30)
                        except smtplib.SMTPRecipientsRefused:
                            messagebox.showerror("Mailed","Mail Not Sent")
                    except smtplib.SMTPException:
                        messagebox.showerror("Mailed","Mail Not Sent")
                except smtplib.SMTPConnectError:
                    messagebox.showerror("Error","Connection Error")

    def verify(self):
        if self.otp == self.otp_entry.get():
            messagebox.showinfo("Success","Verified", parent=self.root2)
            self.count = str(region_code_for_country_code(self.code.get()))
            self.UID=self.uname.get()+str(random.randint(1000,40000))

            self.conn=sqlite3.connect("plasma.db")
            self.c=self.conn.cursor()
            self.c.execute("CREATE TABLE IF NOT EXISTS user(UID TEXT UNIQUE PRIMARY KEY NOT NULL ,Uname TEXT NOT NULL, Email TEXT UNIQUE NOT NULL ,Country_Code TEXT NOT NULL, Country TEXT NOT NULL,Phone_No TEXT UNIQUE NOT NULL,Password TEXT NOT NULL, DOB DATE NOT NULL)")
            self.find_user = ("SELECT * FROM user WHERE Email= ?  or Phone_No = ?")
            self.c.execute(str(self.find_user),(self.email.get(),self.contact.get()))
            results = (self.c).fetchall()
            if results:
                messagebox.showerror("Error","Email or Contact  is already Used")
            else:
                try:
                    self.c.execute("INSERT INTO user (UID ,Uname, Email ,Country_Code, Country,Phone_No,Password, DOB ) VALUES (?,?,?,?,?,?,?,?)",
                    (self.UID,self.uname.get(),self.email.get(),self.code.get(),self.count, self.contact.get(),self.pasw.get(), self.dob.get()))
                    self.conn.commit()
                    self.c.close()
                    self.conn.close()
                    self.otp_entry.delete(0,END)
                    self.otp=None
                    self.root2.destroy()
                    return messagebox.showinfo("Successfull","Successfully Added Data, Now You Can Login"+" You ID :"+self.UID)


                except Exception:
                    return messagebox.showerror("Error!!","Somthing went wrong not able to add data try again ")        
        else:
            messagebox.showerror("Error","OTP Enterd Is Wrong! Try Again To Resend again click on Resgister")            
        
    def back(self):
        self.destroy()
        win1()

class win3(Tk):
    def __init__(self,*arg):
        Tk.__init__(self,*arg)
        self.title("Signup".center(420))  # title for Window 
        self.configure(background = "black")  # background color for window 
        self.geometry("1350x700+0+0")
        photo = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
        self.iconphoto(False, photo)

       
        self.bg_icon = ImageTk.PhotoImage(file="Pics\\1 (8).jpg")

        
        bg_color ="#074463"
        font_=("times new roman")

        title= Label(self, bd=10, relief=GROOVE, text="Hospital SignUp Page", font=(font_,40,"bold"),bg=bg_color,fg="gold").pack(side=TOP, fill=X)
        bg_lbl = Label(self, image=self.bg_icon).pack(fill=Y) 


        #===========variables===================

        self.hname=StringVar()
        self.pasw=StringVar()
        self.email=StringVar()
        self.city=StringVar()
        self.contact=StringVar()
        self.doe=StringVar()
        

        now = datetime.now()
        self.today= now.strftime("%d/%m/%Y")
        self.label,self.calender="",""


        Manage_Frame=Frame(self,bd=10, relief=RIDGE,bg=bg_color)
        Manage_Frame.place(x=430, y=100, width=500, height=550)
        m_title=Label(Manage_Frame,text="SIGN UP", compound=LEFT, bg=bg_color,fg="white",font=(font_,30,"bold"))
        m_title.grid(row=0, columnspan=2,pady=20)

        lbl1=Label(Manage_Frame,text="Hosp Name",  bg=bg_color,fg="white",font=(font_,20,"bold"))
        lbl1.grid(row=1, column=0,padx=20,pady=10,sticky="w")

        txt1=Entry(Manage_Frame,textvariable=self.hname,  bd=5,relief=GROOVE,font=(font_,15,"bold"))
        txt1.grid(row=1, column=1,padx=20,pady=10,sticky="w")

        lbl2=Label(Manage_Frame,text="Password",  bg=bg_color,fg="white",font=(font_,20,"bold"))
        lbl2.grid(row=2, column=0,padx=20,pady=10,sticky="w")

        txt2=Entry(Manage_Frame,textvariable=self.pasw,  bd=5,relief=GROOVE,font=(font_,15,"bold"))
        txt2.grid(row=2, column=1,padx=20,pady=10,sticky="w")

        lbl3=Label(Manage_Frame,text="Email",  bg=bg_color,fg="white",font=(font_,20,"bold"))
        lbl3.grid(row=3, column=0,padx=20,pady=10,sticky="w")

        txt3=Entry(Manage_Frame,textvariable=self.email,  bd=5,relief=GROOVE,font=(font_,15,"bold"))
        txt3.grid(row=3, column=1,padx=20,pady=10,sticky="w")

        self.label=(Label(Manage_Frame,text="D.O.E", bg=bg_color,fg="white",font=(font_,20,"bold")))
        self.label.grid(row=4, column=0,padx=20,pady=10,sticky="w")
        
        self.calendar=(DateEntry(Manage_Frame, textvariable=self.doe,font=("times new roman",18,"bold"), locale='en_GB', width=16,state="readonly"))
        self.calendar.place(x=205, y=290, anchor="w")



        City_lbl=Label(Manage_Frame,text="City",  bg=bg_color,fg="white",font=(font_,20,"bold"))
        City_lbl.grid(row=5, column=0,padx=25,pady=10,sticky="w")
        
        # ================== Combobox (used to create Drop down Menu) ====================================       
        
        City=Entry(Manage_Frame,textvariable=self.city, font=(font_,15,"bold"),width=21)
        City.place(x=205, y=340)



        lbl6=Label(Manage_Frame,text="Contact",  bg=bg_color,fg="white",font=(font_,20,"bold"))
        lbl6.grid(row=6, column=0,padx=20,pady=10,sticky="w")

        self.code=IntVar()
        self.code.set(0)
        combo_code = OptionMenu(Manage_Frame, self.code,"+93","+355","+213","+1684","+376","+244","+1264","+672","+1268","+54","+374","+297","+61","+880","+32","+226","+359","+387","+1246","+681","+590","+1441","+673","+591","+973","+257","+229","+975","+1876","+267","+685","+599","+55","+1242","+441534","+375","+501","+7","+250","+381","+670","+262","+993","+992","+40","+690","+245","+1671","+502","+30","+240","+590","+81","+592","+441481","+594","+995","+1473","+44","+241","+503","+224","+220","+299","+350","+233","+968","+216","+962","+385","+509","+36","+852""+504","+58","+1787","+1939","+970","+680","+351","+47","+595","+964","+507","+689","+675","+51","+92","+63","+870","+48","+508","+260","+212","+372","+20","+27","+593","+39","+84","+677","+251","+252","+263","+966","+34","+291","+382","+373","+261","+590","+212","+377","+998","+95","+223","+853","+976","+692","+389","+230","+356","+265","+960","+596","+1670","+1664","+222","+441624","+256","+255","+60","+52","+972","+33","+246","+290","+358","+679","+500","+691","+298","+505","+31","+47","+264","+678","+687","+227","+672","+234","+64","+977","+674","+683","+682","+225","+41","+57","+86","+237","+56","+61","+1","+242","+236","+243","+420","+357","+61","+506","+599","+238","+53","+268","+963","+599","+996","+254","+211","+597","+686","+855","+1869","+269","+239","+421","+82","+386","+850","+965","+221","+378","+232","+248","+7","+1345","+65","+46","+249","+1809","1-829","+1767","+253","+45","+1-284","+49","+967","+213","+1","+598","+262","+1","+961","+1758","+856","+688","+886","+1868","+90","+94","+423","+371","+676","+370","+352","+231","+266","+66","+228","+235","+1649","+218","+379","+1784","+971","+376","+1268","+93","+1264","+1340","+354","+98","+374","+355","+244","+1684","+54","+61","+43","+297","+91","+35818","+994","+353","+62","+380","+974","+258" )
        combo_code.place(x=205, y=390)
        combo_code.config(bg="#ffe5b4",bd=0,activebackground="#ffe5b4")

        txt6=Entry(Manage_Frame,textvariable=self.contact,  bd=3,relief=GROOVE,font=(font_,12,"bold"))
        txt6.place(x=260, y=390)

        
        Button_Frame=Frame(Manage_Frame,bd=4, relief=RIDGE,bg=bg_color)
        Button_Frame.place(x=10, y=450,width=460,height=70)

        btn_sgnup = Button(Button_Frame, text="SignUp",width =8, command = self.signup, font="bold").grid(row = 0,column=0,padx=15,pady=15 )
        btn_back = Button(Button_Frame, text="Back",width =8, command = self.back, font="bold").grid(row = 0,column=1,padx=15,pady=15 )
        btn_Clear = Button(Button_Frame, text="Clear",width =8, command = self.clear, font="bold").grid(row = 0,column=2,padx=15,pady=15 )
        btn_Exit = Button(Button_Frame, text="Exit",width =8, command = self.exit, font="bold").grid(row = 0,column=3,padx=15,pady=15 )
        btn_Signup_hos = Button(self, text="User_SignUp",width =15, command = self.u_signup,bd=5,relief=GROOVE, bg="red",activebackground="red", activeforeground="white",fg="white",font="bold").place(x=1000, y=20)
    
    def exit(self):
        self.destroy()  
    
    def u_signup(self):
        self.destroy()
        win2().mainloop()

    def clear(self):
        self.uname.set("")
        self.pasw.set("")
        self.email.set("")
        self.gender.set("")
        self.contact.set("")
        self.code.set(0)
        self.dob.set(self.today)
    
    
    def signup(self): 
        is_valid1 = validate_email(self.email.get())
        
        if self.hname.get()=="" and self.contact.get()=="" and self.pasw.get=="" and self.email.get()=="" and self.city.get()=="" and self.doe.get()==self.today :
            return messagebox.showerror("Error","All Fields Required")
        
        if is_valid1 == False:
            return messagebox.showerror("Error","Email not valid")  
        
        if self.hname.get()==""  :
            return messagebox.showerror("Error","Hospital name Required")
        
        if self.pasw.get=="" :
            return messagebox.showerror("Error","Password Required")
        
        if len(str(self.pasw.get()))<8:
            return messagebox.showerror("Error","Password should of minimum 8 character")
        
        if self.email.get()=="" :
            return messagebox.showerror("Error","Email Required")
            
        if self.city.get()==""  :
            return messagebox.showerror("Error","City Required")

        if self.doe.get()>=self.today  :
            return messagebox.showerror("Error","Date of Establishment Not Possible")
        
        if self.contact.get()==""  :
            return messagebox.showerror("Error","Contact Required")
        
        try:
            temp=self.contact.get()
            int(temp)
        except ValueError:
            return messagebox.showerror("Error","Contact should be Integer")
 
        if len(str(self.contact.get()))<10 or len(str(self.contact.get()))>10 :
            return messagebox.showerror("Error","Contact should consist of 10 numbers")     
        
        else:
            self.otp = str(random.randint(100000,999999))
            #print(self.otp)
        
            self.conn=sqlite3.connect("plasma.db")
            self.c=self.conn.cursor()
            self.c.execute("CREATE TABLE IF NOT EXISTS hos(HID TEXT UNIQUE PRIMARY KEY NOT NULL ,Hname TEXT NOT NULL, Email TEXT UNIQUE NOT NULL ,Country_Code TEXT NOT NULL, Country TEXT NOT NULL,Phone_No TEXT UNIQUE NOT NULL,Password TEXT NOT NULL, DOE DATE NOT NULL)")
        
            self.find_user = ("SELECT * FROM hos WHERE Email= ?  or Phone_No = ?")
            self.c.execute(str(self.find_user),(self.email.get(),self.contact.get()))
            results = (self.c).fetchall()
            if results:
                messagebox.showerror("Error","Email or Contact  is already Used")
            else:
            
                send = smtplib.SMTP("smtp.gmail.com", 587)  # Create session for Gmail
                send.starttls()  # transport layer

                #===================Plain Text=====================

                msg = EmailMessage()
                msg["Subject"] = "OTP"
                msg["From"] = "aj147ps@gmail.com"
                msg["To"] = self.email.get()
                msg.set_content("Hi!"+str(self.hname.get())+" your OTP for registration is: "+"\'"+self.otp+"\'")        
                    
                try:
                    send.login("aj147ps@gmail.com","xcavbfayvnthixwy")
                except smtplib.SMTPAuthenticationError:
                    messagebox.showerror("Error","Error Occur Otp Not")    

                try:
                    try:
                        try:
                            send.send_message(msg)
                            messagebox.showinfo("Mailed","OTP Sent to Your Mail Id")                        
                            self.root2 = Toplevel()  # Child Window "Tk() can Also be use here"
                            self.root2.title("OTP")
                            self.root2.geometry("700x320+350+150")
                            self.root2.configure(bg="black")
                            photo2 = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
                            self.root2.iconphoto(False, photo2)
                            self.root2.focus_force() 
                            self.root2.grab_set()  
                            self.root2.resizable(False, False)
                        
                            title_child = Label(self.root2, text="ENTER OTP", bg="#152238", fg="white",compound=LEFT, font=("Goudy Old Style", 48, "bold"), anchor="w").place(x=0, y=0, relwidth=1)
                        
                            otp_lbl = Label(self.root2, text="Enter OTP", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=150)
                            self.otp_entry = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
                            self.otp_entry.place(x=230, y=150)

                            verify_btn = Button(self.root2, text="verify", font=("times new roman", 18, "bold"), activebackground="#262626",activeforeground="white", bg="#262626", fg="white", cursor="hand2", command=self.verify).place(x=300, y=260, width=140, height=30)
                        except smtplib.SMTPRecipientsRefused:
                            messagebox.showerror("Mailed","Mail Not Sent")
                    except smtplib.SMTPException:
                        messagebox.showerror("Mailed","Mail Not Sent")
                except smtplib.SMTPConnectError:
                    messagebox.showerror("Error","Connection Error")

    def verify(self):
        if self.otp == self.otp_entry.get():
            messagebox.showinfo("Success","Verified", parent=self.root2)
            self.count = str(region_code_for_country_code(self.code.get()))
            self.HID=self.hname.get()+str(random.randint(1000,40000))

            self.conn=sqlite3.connect("plasma.db")
            self.c=self.conn.cursor()
            self.c.execute("CREATE TABLE IF NOT EXISTS hos(HID TEXT UNIQUE PRIMARY KEY NOT NULL ,Hname TEXT NOT NULL, Email TEXT UNIQUE NOT NULL ,Country_Code TEXT NOT NULL, Country TEXT NOT NULL,Phone_No TEXT UNIQUE NOT NULL,Password TEXT NOT NULL, DOE DATE NOT NULL)")
            self.find_user = ("SELECT * FROM hos WHERE Email= ?  or Phone_No = ?")
            self.c.execute(str(self.find_user),(self.email.get(),self.contact.get()))
            results = (self.c).fetchall()
            if results:
                messagebox.showerror("Error","Email or Contact  is already Used")
            else:
                try:
                    self.c.execute("INSERT INTO hos (HID ,Hname, Email ,Country_Code, Country,Phone_No,Password, DOE ) VALUES (?,?,?,?,?,?,?,?)",
                    (self.HID,self.hname.get(),self.email.get(),self.code.get(),self.count, self.contact.get(),self.pasw.get(), self.doe.get()))
                    self.conn.commit()
                    self.c.close()
                    self.conn.close()
                    self.otp_entry.delete(0,END)
                    self.otp=None
                    self.root2.destroy()
                    return messagebox.showinfo("Successfull","Successfully Added Data, Now You Can Login"+" You ID :"+self.HID)


                except Exception:
                    return messagebox.showerror("Error!!","Somthing went wrong not able to add data try again ")        
        else:
            messagebox.showerror("Error","OTP Enterd Is Wrong! Try Again To Resend again click on Resgister")            
        
    def back(self):
        self.destroy()
        win1()

class U_login():
    def __init__(self,root):
        self.root=root
        self.root.title("Login Form".center(420))  
        self.root.configure(background="black")  
        self.root.geometry("1360x768+0+0")
        bg_color = "#2B547E"
        photo = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
        root.iconphoto(False, photo)

        # =========================== Image Storing ========================================
        # =========================== Image Storing ========================================
        # =========================== Image Storing ========================================
        # =========================== Image Storing ========================================

        self.eye_icon = PhotoImage(file="Pics\\2.png")
        self.bg_icon = ImageTk.PhotoImage(file="Pics\\1 (4).jpg")
        self._icon = ImageTk.PhotoImage(file="Pics\\6.jpg")    
        self.user_icon = ImageTk.PhotoImage(file="Pics\\4.png")
        self.pasw_icon = ImageTk.PhotoImage(file="Pics\\3.png")
        self.user_ = ImageTk.PhotoImage(file="Pics\\5.png")
        self.hos_icon = ImageTk.PhotoImage(file="Pics\\1 (2).jpg")

        self.uname = StringVar()
        self.pasw = StringVar()
        self.uname.set("User Id")
        self.pass_1 = StringVar()
        self.pass_1.set("Password Mode: Hidden")
        
        # ============================ GUI Window and Functional Buttons Creation ============================
        # ============================ GUI Window and Functional Buttons Creation ============================
        # ============================ GUI Window and Functional Buttons Creation ============================
        # ============================ GUI Window and Functional Buttons Creation ============================

        bg_lbl = Label(root, image=self.bg_icon).pack(fill=Y) 

        
        # ============================ Frame 1 (F1) ===============================
        # ============================ Frame 1 (F1) ===============================
        # ============================ Frame 1 (F1) ===============================
        # ============================ Frame 1 (F1) ===============================

        self.F1 = LabelFrame(root, bd=10, relief=GROOVE, bg=bg_color)
        self.F1.place(x=195, y=95, width=600, height=480)
        
        F1=self.F1
        
        lbl = Label(F1, text="User Login ", bg=bg_color, fg="gold", font=("times new roman", 30, "bold")).grid(row=0, column=0, padx=80, pady=30)

        logolbl = Label(F1, image=self.user_icon).place(x=80, y=200, anchor="w")
        
        lbl6 = Label(F1, text="User ID", fg="white", bg=bg_color, font=("times new roman", 18, "bold")).place(x=115, y=200, anchor="w")
        
        self.txtu = Entry(F1, bd=5, textvariable=self.uname, relief=GROOVE,font=("", 15)).place(x=250, y=200, anchor="w")

        logolbl2 = Label(F1, image=self.pasw_icon).place(x=80, y=260, anchor="w")
        
        lbl7 = Label(F1, text="Password", fg="white", bg=bg_color, font=("times new roman", 20, "bold"))
        
        lbl7.place(x=115, y=260, anchor="w")
        
        self.txtp = Entry(F1, bd=5, textvariable=self.pasw, show="*",relief=GROOVE, font=("", 15))
        
        self.txtp.place(x=250, y=260, anchor="w")

        
        self.txtp_1 = Entry(F1, bd=0, bg=bg_color, fg="white", textvariable=self.pass_1,relief=GROOVE, width="45", font=("times new roman", 10))
        
        self.txtp_1.place(x=250, y=10, anchor="w")

        self.txtp_1.config(state="readonly",width=23,fg="black")
        # ============================ Frame 2 (F2) ===============================
        # ============================ Frame 2 (F2) ===============================
        # ============================ Frame 2 (F2) ===============================
        # ============================ Frame 2 (F2) ===============================

        self.F2 = LabelFrame(root, bd=10, relief=GROOVE, bg="#3b444b")
        self.F2.place(x=790, y=95, width=310, height=480)
        F2 = self.F2 
        
        lbl2 = Label(F2, bg=bg_color, image=self.user_).grid(row=0, column=0, padx=100, pady=20)
        
        lbl3 = Label(F2, text="Get you all account details at ", bg="#3b444b", fg="#00FFFF", font=("times new roman", 15, "italic")).grid(row=1, column=0, padx=5)
        
        lbl4 = Label(F2, text="one place @PersonalAcc", fg="#00FFFF", bg="#3b444b", font=("times new roman", 10, "italic")).grid(row=2, column=0, padx=10)

        lbl6 = Label(F2, text="Developed by Aditya",fg="#4863A0", bg="#3b444b", font=("times new roman", 20)).place(x=20, y=420)

        img_lbl7 = Label(F2, image=self.hos_icon, bg="#3b444b").place(x=20, y=270, width=250, height=130) 
        # ========================== Buttons ======================================
        # ========================== Buttons ======================================
        # ========================== Buttons ======================================
        # ========================== Buttons ======================================

        btn_login1 = Button(F1, text="SignIn", relief=RAISED, width=12, height=1, font=("times new roman", 12, "bold"), bg="green", foreground="#FEFCFF", command=self.logfun).place(x=530, y=330, width=150, anchor="e")

        btn_Signup = Button(F1, text="Sign Up", relief=GROOVE, width=8, height=1, activebackground="Red", activeforeground="white", command=self.Signup, font=("times new roman", 14, "bold"), bg="Red", fg="white").place(x=330, y=330, width=150, anchor="e")

        btn_Eye = Button(F1, image=self.eye_icon, relief=GROOVE, font=("times new roman", 14, "bold"), bg="light green", command=self.show_pasw).place(x=528, y=260, height=35, anchor="e")    

        btn_Exit = Button(F2, text="Exit", relief=GROOVE, width=8, height=1, activebackground="Red", activeforeground="white", command=self.Exit, font=("times new roman", 14, "bold"), bg="Red", fg="white").grid(row=5, column=0, padx=15, pady=60, sticky="w")

        btn_Back = Button(F2, text="Back", relief=GROOVE, width=8, height=1, activebackground="Red", activeforeground="white", command=self.Back_T, font=("times new roman", 14, "bold"), bg="lightgreen", fg="black").place(x=170, y=215)
        
        btn_Login_h = Button(root, text="Login Hos", width=8, height=1, activebackground="blue", activeforeground="white", command=self.Login_H, font=("times new roman", 14, "bold"),bd=5, relief=GROOVE, bg="blue", fg="white").place(x=670, y=120)

    def Login_H(self):
        self.root.destroy()
        root=Tk()
        clas=H_login(root)
        win1.new=clas

    def Back_T(self,*arg):
        self.root.destroy()
        win1()
        
    def Signup(self,*arg):
        self.root.destroy()
        win2().mainloop()
        
    def logfun(self):
    
        if self.uname.get()=="" or self.pasw.get()=="":
            messagebox.showerror("Error","All fields should be entered")
        else:
            with open("Temp.txt", "w+") as file:
                file.write(self.uname.get())
            self.conn = sqlite3.connect("plasma.db")
            self.c = self.conn.cursor()
            self.find_user = (
                "SELECT * FROM user WHERE UID = ?  AND Password = ?")
            self.c.execute(str(self.find_user), (str(
                self.uname.get()), str(self.pasw.get())))
            results = (self.c).fetchall()
            if results:
                for i in results:
                    messagebox.showinfo("Success","Successfully Logined")
                    self.root.destroy()
                    self.HomeU()
                    
            else:
                messagebox.showerror(
                    "Error!", "Username or Password may be wrong")
    def HomeU(self,*arg):  # Function calls window 2 that is Signup window
        User_Page().mainloop()

    def Exit(self):
        self.root.destroy()

    def show_pasw(self):
    
        a = self.pasw.get()  # Storing Password Field Value to a Variable
        self.txtp_1.config(state="normal") # change the field state to normal so that we can read our mode of password type (Hidden or Shown)
        self.pasw.set(a) # Not set the vale into field again

        if self.txtp_1.get() == "Password Mode: Hidden": # If we get Mode hidden then when Button Clicks it should turn into show and visa-versa for elif condition
            self.txtp_1.config(state="normal") # Similar work as Above
            self.txtp_1.insert(0, "Password Mode: Shown")
            self.txtp_1.config(state="readonly",width=23,fg="black")
            
            self.txtp = Entry(self.F1, bd=5, textvariable=self.pasw, relief=GROOVE, font=("", 15))
            self.txtp.place(x=250, y=260, anchor="w")
            self.pass_1.set("Password Mode: Shown")
            self.pasw.set(a)
            self.txtp_1.config(state="readonly",width=23,fg="black")
        
        elif self.txtp_1.get() == "Password Mode: Shown":
            self.txtp_1.config(state="normal")
            self.txtp_1.delete(0, END)
            self.txtp_1.insert(0, "Password Mode: Hidden")
            self.txtp = Entry(self.F1, bd=5, textvariable=self.pasw,
                                relief=GROOVE, show="*", font=("", 15))
            self.txtp.place(x=250, y=260, anchor="w")
            self.pasw.set(a)
            self.txtp_1.config(state="readonly",width=23,fg="black")

        self.root.mainloop()

class H_login():
    def __init__(self,root):
        self.root=root
        self.root.title("Login Form".center(420))  
        self.root.configure(background="black")  
        self.root.geometry("1360x768+0+0")
        bg_color = "#2B547E"
        photo = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
        root.iconphoto(False, photo)

        # =========================== Image Storing ========================================
        # =========================== Image Storing ========================================
        # =========================== Image Storing ========================================
        # =========================== Image Storing ========================================

        self.eye_icon = PhotoImage(file="Pics\\2.png")
        self.bg_icon = ImageTk.PhotoImage(file="Pics\\1 (4).jpg")
        self._icon = ImageTk.PhotoImage(file="Pics\\6.jpg")    
        self.user_icon = ImageTk.PhotoImage(file="Pics\\4.png")
        self.pasw_icon = ImageTk.PhotoImage(file="Pics\\3.png")
        self.user_ = ImageTk.PhotoImage(file="Pics\\5.png")
        self.hos_icon = ImageTk.PhotoImage(file="Pics\\1 (2).jpg")

        self.hname = StringVar()
        self.pasw = StringVar()
        self.hname.set("HOS Id")
        self.pass_1 = StringVar()
        self.pass_1.set("Password Mode: Hidden")
        
        # ============================ GUI Window and Functional Buttons Creation ============================
        # ============================ GUI Window and Functional Buttons Creation ============================
        # ============================ GUI Window and Functional Buttons Creation ============================
        # ============================ GUI Window and Functional Buttons Creation ============================

        bg_lbl = Label(root, image=self.bg_icon).pack(fill=Y) 

        
        # ============================ Frame 1 (F1) ===============================
        # ============================ Frame 1 (F1) ===============================
        # ============================ Frame 1 (F1) ===============================
        # ============================ Frame 1 (F1) ===============================

        self.F1 = LabelFrame(root, bd=10, relief=GROOVE, bg=bg_color)
        self.F1.place(x=195, y=95, width=600, height=480)
        
        F1=self.F1
        
        lbl = Label(F1, text="Hospital Login ", bg=bg_color, fg="gold", font=("times new roman", 30, "bold")).grid(row=0, column=0, padx=80, pady=30)

        logolbl = Label(F1, image=self.user_icon).place(x=80, y=200, anchor="w")
        
        lbl6 = Label(F1, text="Hos ID", fg="white", bg=bg_color, font=("times new roman", 18, "bold")).place(x=115, y=200, anchor="w")
        
        self.txtu = Entry(F1, bd=5, textvariable=self.hname, relief=GROOVE,font=("", 15)).place(x=250, y=200, anchor="w")

        logolbl2 = Label(F1, image=self.pasw_icon).place(x=80, y=260, anchor="w")
        
        lbl7 = Label(F1, text="Password", fg="white", bg=bg_color, font=("times new roman", 20, "bold"))
        
        lbl7.place(x=115, y=260, anchor="w")
        
        self.txtp = Entry(F1, bd=5, textvariable=self.pasw, show="*",relief=GROOVE, font=("", 15))
        
        self.txtp.place(x=250, y=260, anchor="w")

        
        self.txtp_1 = Entry(F1, bd=0, bg=bg_color, fg="white", textvariable=self.pass_1,relief=GROOVE, width="45", font=("times new roman", 10))
        
        self.txtp_1.place(x=250, y=10, anchor="w")

        self.txtp_1.config(state="readonly",width=23,fg="black")
        # ============================ Frame 2 (F2) ===============================
        # ============================ Frame 2 (F2) ===============================
        # ============================ Frame 2 (F2) ===============================
        # ============================ Frame 2 (F2) ===============================

        self.F2 = LabelFrame(root, bd=10, relief=GROOVE, bg="#3b444b")
        self.F2.place(x=790, y=95, width=310, height=480)
        F2 = self.F2 
        
        lbl2 = Label(F2, bg=bg_color, image=self.user_).grid(row=0, column=0, padx=100, pady=20)
        
        lbl3 = Label(F2, text="Get you all account details at ", bg="#3b444b", fg="#00FFFF", font=("times new roman", 15, "italic")).grid(row=1, column=0, padx=5)
        
        lbl4 = Label(F2, text="one place @PersonalAcc", fg="#00FFFF", bg="#3b444b", font=("times new roman", 10, "italic")).grid(row=2, column=0, padx=10)

        lbl6 = Label(F2, text="Developed by Aditya",fg="#4863A0", bg="#3b444b", font=("times new roman", 20)).place(x=20, y=420)

        img_lbl7 = Label(F2, image=self.hos_icon, bg="#3b444b").place(x=20, y=270, width=250, height=130) 
        # ========================== Buttons ======================================
        # ========================== Buttons ======================================
        # ========================== Buttons ======================================
        # ========================== Buttons ======================================

        btn_login1 = Button(F1, text="SignIn", relief=RAISED, width=12, height=1, font=("times new roman", 12, "bold"), bg="green", foreground="#FEFCFF", command=self.logfun).place(x=530, y=330, width=150, anchor="e")

        btn_Signup = Button(F1, text="Sign Up", relief=GROOVE, width=8, height=1, activebackground="Red", activeforeground="white", command=self.Signup, font=("times new roman", 14, "bold"), bg="Red", fg="white").place(x=330, y=330, width=150, anchor="e")

        btn_Eye = Button(F1, image=self.eye_icon, relief=GROOVE, font=("times new roman", 14, "bold"), bg="light green", command=self.show_pasw).place(x=528, y=260, height=35, anchor="e")    

        btn_Exit = Button(F2, text="Exit", relief=GROOVE, width=8, height=1, activebackground="Red", activeforeground="white", command=self.Exit, font=("times new roman", 14, "bold"), bg="Red", fg="white").grid(row=5, column=0, padx=15, pady=60, sticky="w")

        btn_Back = Button(F2, text="Back", relief=GROOVE, width=8, height=1, activebackground="Red", activeforeground="white", command=self.Back_T, font=("times new roman", 14, "bold"), bg="lightgreen", fg="black").place(x=170, y=215)
        
        btn_Login_h = Button(root, text="Login User", width=8, height=1, activebackground="blue", activeforeground="white", command=self.Login_U, font=("times new roman", 14, "bold"),bd=5, relief=GROOVE, bg="blue", fg="white").place(x=670, y=120)

    def Login_U(self):
        self.root.destroy()
        root=Tk()
        clas=U_login(root)
        win1.new=clas

    def Back_T(self,*arg):
        self.root.destroy()
        win1()
        
    def Signup(self,*arg):
        self.root.destroy()
        win3().mainloop()
        
    def logfun(self):
    
        if self.hname.get()=="" or self.pasw.get()=="":
            messagebox.showerror("Error","All fields should be entered")
        else:
            with open("Temp1.txt", "w+") as file:
                file.write(self.hname.get())
            self.conn = sqlite3.connect("plasma.db")
            self.c = self.conn.cursor()
            self.find_user = (
                "SELECT * FROM hos WHERE HID = ?  AND Password = ?")
            self.c.execute(str(self.find_user), (str(
                self.hname.get()), str(self.pasw.get())))
            results = (self.c).fetchall()
            if results:
                for i in results:
                    messagebox.showinfo("Success","Successfully Logined")
                    self.root.destroy()
                    self.HomeU()
                    
            else:
                messagebox.showerror(
                    "Error!", "Username or Password may be wrong")
    def HomeU(self,*arg):  # Function calls window 2 that is Signup window
        Hospital_Page().mainloop()

    def Exit(self):
        self.root.destroy()

    def show_pasw(self):
    
        a = self.pasw.get()  # Storing Password Field Value to a Variable
        self.txtp_1.config(state="normal") # change the field state to normal so that we can read our mode of password type (Hidden or Shown)
        self.pasw.set(a) # Not set the vale into field again

        if self.txtp_1.get() == "Password Mode: Hidden": # If we get Mode hidden then when Button Clicks it should turn into show and visa-versa for elif condition
            self.txtp_1.config(state="normal") # Similar work as Above
            self.txtp_1.insert(0, "Password Mode: Shown")
            self.txtp_1.config(state="readonly",width=23,fg="black")
            
            self.txtp = Entry(self.F1, bd=5, textvariable=self.pasw, relief=GROOVE, font=("", 15))
            self.txtp.place(x=250, y=260, anchor="w")
            self.pass_1.set("Password Mode: Shown")
            self.pasw.set(a)
            self.txtp_1.config(state="readonly",width=23,fg="black")
        
        elif self.txtp_1.get() == "Password Mode: Shown":
            self.txtp_1.config(state="normal")
            self.txtp_1.delete(0, END)
            self.txtp_1.insert(0, "Password Mode: Hidden")
            self.txtp = Entry(self.F1, bd=5, textvariable=self.pasw,
                                relief=GROOVE, show="*", font=("", 15))
            self.txtp.place(x=250, y=260, anchor="w")
            self.pasw.set(a)
            self.txtp_1.config(state="readonly",width=23,fg="black")

        self.root.mainloop()

class User_Page(Tk):
    def __init__(self,*arg):       # Constructors
        Tk.__init__(self,*arg)
        photo = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
        self.iconphoto(False, photo)

        self.title("Plasma Finder".center(420))  # title for Window 
        self.configure(background = "black")  # background color for window 
        self.geometry("1360x768+0+0")
        photo = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
        self.iconphoto(False, photo)

        bg_color ="#FFFFF6"
        
     
        self.bg_icon = ImageTk.PhotoImage(file="Pics\\1 (1).jpg")
        bg_lbl = Label(self, image = self.bg_icon).pack(fill=Y) # we put image into our window
        
        self.hos_icon=ImageTk.PhotoImage(file="Pics\\1 (2) copy.jpg")
                
        
        F1 = LabelFrame(self,bd=10,relief=GROOVE,bg=bg_color)
        F1.place(x=0,relwidth=1,height=100 )

        lbl = Label(F1,text="Plasma Finder", compound=LEFT, image=self.hos_icon,bg=bg_color, font= ("times new roman",20,"bold")).place(x=0, y=5)

        self.lbl_hr = Label(F1,text="12" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_hr.place(x=890, y=40)
        
        self.lbl_COLON = Label(F1,text=":" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_COLON.place(x=915, y=40)
       
       
        self.lbl_min = Label(F1,text="12" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_min.place(x=925, y=40)
       
        self.lbl_COLON = Label(F1,text=":" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_COLON.place(x=950, y=40)
       
        self.lbl_sec = Label(F1,text="12" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_sec.place(x=960, y=40)
        

        self.lbl_abv = Label(F1,text="AM" , font = ("times new roman", 13,"bold"),bg=bg_color)
        self.lbl_abv.place(x=985, y=43)
       
       
        self.font=("times new roman",20,"bold")
        self.calendar = []

        ntpClient = ntplib.NTPClient()
        response = ntpClient.request('pool.ntp.org')
        a=ctime(response.tx_time)
        b=[a[i:i+10] for i in range(0, len(a), 10)]
        c=str(b[0])
        d=str(b[2])

        self.date = Label(F1, font=("times new roman",15,"bold"), text=c, bg=bg_color)
        self.date.place(x=740, y=40)

        self.date1 = Label(F1, font=("times new roman",15,"bold"), text=d,bg=bg_color)
        self.date1.place(x=840, y=40)

        
        self.date2 = Label(F1, font=("times new roman",15,"bold"), text="Calendar",bg=bg_color)
        self.date2.place(x=750, y=5)

        self.calendar.append(DateEntry(F1, font=("times new roman",15,"bold"), locale='en_GB',state="readonly",width=10))
        self.calendar[-1].place(x=855, y=20, anchor="w")

        
        btn_changepass = Button(F1, text="ChangePassword",relief=RAISED,width =15,height=1, font=("times new roman",14,"bold"),bg="red",foreground="white",command=self.change_pasw).place(x=1145,y=20,anchor="w")
        btn_logout = Button(F1, text="Logout",relief=RAISED,width =15,height=1, font=("times new roman",14,"bold"),bg="light green",foreground="black", command=self.logout).place(x=1145,y=60,anchor="w")

        lbl2 = Label(F1,bg=bg_color)
        lbl2.place(x=25,y=10)

        F2 = LabelFrame(self,bd=10,relief=GROOVE,bg=bg_color)
        F2.place(x=0,y=100,width=150,height=670 )

        F21 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F21.place(x=0,y=0,width=130,height=133 )
        
        F22 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F22.place(x=0,y=133,width=130,height=133)
        
        F23 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F23.place(x=0,y=266,width=130,height=133 )
        
        F24 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F24.place(x=0,y=399,width=130,height=133)
        
        F25 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F25.place(x=0,y=532,width=130,height=133)

        self.U_mange = PhotoImage(file="Pics\\User_Det.png")
        self.donor_b = ImageTk.PhotoImage(file="Pics\\Blood Donar.jpg")
        self.b_bank = ImageTk.PhotoImage(file="Pics\Blood Bank Search.jpg")    
        self.p_donar = ImageTk.PhotoImage(file="Pics\Plasma.png")
        self.exit = ImageTk.PhotoImage(file="Pics\\Exit.jpg")
        
        btn_U_det = Button(F21,image= self.U_mange,bg=bg_color,relief=RAISED,width =115,height=120,command=self.U_det).place(x=0,y=60,anchor="w")
        btn_blood_donor = Button(F22,image= self.donor_b,bg=bg_color,relief=RAISED,width =115,height=120,command=self.Blood_Donar ).place(x=0,y=60,anchor="w")
        btn_blood_bank = Button(F23,relief=RAISED,bg=bg_color,image=self.b_bank,width =115,height=120,command=self.Blood_Bank ).place(x=0,y=60,anchor="w")
        btn_Plasma = Button(F24,relief=RAISED,image=self.p_donar,bg=bg_color,width =115,height=120, command=self.Plasma).place(x=0,y=60,anchor="w")
        btn_Exit = Button(F25,relief=RAISED,bg=bg_color,image=self.exit,width =115,height=120, command=self.Exit).place(x=0,y=60,anchor="w")

        #------------------------------F3--------------------------------
        F3 = LabelFrame(self,bd=5,relief=FLAT,bg="light gray")
        F3.place(x=150,y=100,relwidth=1,height=30 )
        lbl_1= Label(F3,text="Dashboard / User",font=("comic sans",15,"italic"),bg="light gray")
        lbl_1.place(x=0,y=0)

        self.conn=sqlite3.connect("plasma.db")
        self.c=self.conn.cursor()
        

        F4 = LabelFrame(self,bd=10,relief=GROOVE,bg="#DC143C")
        F4.place(x=300,y=170,width=400,height=250 )

        F41 = LabelFrame(F4,bd=5,relief=SUNKEN,bg="#DC143C")
        F41.place(x=0,y=0,width=380,height=60 )
        lbl_2= Label(F41,text="Total Users",fg="#FFFFFF",bg="#DC143C",font=("times new roman",25,"bold"))
        lbl_2.place(x=0,y=0)

        
        F42 = LabelFrame(F4,bd=5,relief=GROOVE)
        F42.place(x=0,y=60,width=380,height=180 )

        text1=Text(F42,bd=5, font=("times new roman",30,"bold"))
        self.c.execute("SELECT COUNT(*) FROM user")
        self.results1 = ((self.c).fetchall())        
        text1.insert(INSERT,("\n             Total\n           Users: "))
        text1.insert(INSERT,self.results1)
        text1.place(x=0,y=0,width=370,height=170)
        text1.configure(state="disabled")
                        

        F5 = LabelFrame(self,bd=10,relief=GROOVE)
        F5.place(x=800,y=170,width=400,height=250 )

        F51 = LabelFrame(F5,bd=5,relief=SUNKEN, bg="#3B9C9C")
        F51.place(x=0,y=0,width=380,height=60 )
        lbl_3= Label(F51,text="Last Login",fg="#FFFFFF",bg="#3B9C9C",font=("times new roman",30,"bold"))
        lbl_3.place(x=0,y=0)

        
        F52 = LabelFrame(F5,bd=5,relief=GROOVE)
        F52.place(x=0,y=60,width=380,height=180 )

        with open("Temp.txt","r+") as file:
            self.read1=file.read()
        text2=Text(F52,bd=5, fg="white",font=("times new roman",15,"bold"),bg="#151B54")
        self.c.execute("SELECT * FROM Last_Login_User WHERE UID =\""+str(self.read1)+"\"")
        self.results2 = ((self.c).fetchall())        
        text2.insert(INSERT,(""))
        if self.results2:
            for i in self.results2:
                a=i    
            #self.EmpID.set(i[0])  
            text2.insert(INSERT,("\nUID                     :   "+str(i[0]+" ")))
            text2.insert(INSERT,("\nEmail                   :   "+str(i[1])+"\n"))
            text2.insert(INSERT,("Last Login Time :   "+str(i[2])+"\n"))
            text2.insert(INSERT,("Last Login Date :   "+str(i[3])+"\n"))

            text2.place(x=0,y=0,width=370,height=170)
            text2.configure(state="disabled")

        
        
        F6 = LabelFrame(self,bd=10,relief=GROOVE)
        F6.place(x=300,y=450,width=400,height=250 )

        F61 = LabelFrame(F6,bd=5,relief=SUNKEN,fg="#FFFFFF",bg="black")
        F61.place(x=0,y=0,width=380,height=60 )
        lbl_4= Label(F61,text="Total Hospitals",bg="black",fg="#FFFFFF",font=("times new roman",30,"bold"))
        lbl_4.place(x=0,y=0)


        F62 = LabelFrame(F6,bd=5,relief=GROOVE)
        F62.place(x=0,y=60,width=380,height=180 )

        text3=Text(F62,bd=5, fg="white",font=("times new roman",30,"bold"),bg="#151B54")
        self.c.execute("SELECT COUNT(*) FROM hos")
        self.results3 = ((self.c).fetchall())        
        text3.insert(INSERT,("\n             Total\n         Hospitals: "))
        text3.insert(INSERT,self.results3)
        text3.place(x=0,y=0,width=370,height=170)
        text3.configure(state="disabled")

        
        
        F7 = LabelFrame(self,bd=10,relief=GROOVE)
        F7.place(x=800,y=450,width=400,height=250 )
        
        F71 = LabelFrame(F7,bd=5,relief=SUNKEN,bg="white")
        F71.place(x=0,y=0,width=380,height=60 )
        lbl_4= Label(F71,text="Developer",bg="white",font=("times new roman",30,"bold"),fg="#DC143C")
        lbl_4.place(x=0,y=0)


        F72 = LabelFrame(F7,bd=5,relief=RAISED)
        F72.place(x=0,y=60,width=380,height=180 )

        text7=Text(F72,bd=5,font=("times new roman",15, "italic"),fg="#FFFFFF", bg="#DC143C",relief=GROOVE)
        text7.insert(INSERT,("                       Developed By\n\nAditya Jha\nEmail Id:aj147ps@gmail.com\nAlternate Email Id:codewithajofficial14@gmail.com\nFollow on #codewithajofficial on insta "))
        text7.place(x=0,y=0,width=370,height=170)
        text7.configure(state="disabled")
        self.clock()

    def U_det(self):
        self.destroy()
        U_Manage().mainloop()
        
    def Blood_Donar(self):
        self.destroy()
        Bload_Search().mainloop()
        
    
    def Blood_Bank(self):
        self.destroy()
        Bload_Bank().mainloop()

    def Plasma(self):
        self.destroy()
        Plasma_Search().mainloop()    
    
    def Exit(self):
        self.destroy()

    
    
    def Exit(self):
        self.destroy()

    
    def logout(self):
        self.read1=StringVar()
        with open("Temp.txt","r+") as file:
            self.read1=file.read()
            file.truncate()
    
        a=messagebox.askyesnocancel("Hey","Confirm again for Logout")
        if a>0:
            now = datetime.now()
            self.Time2=now.strftime('%H:%M:%S')

            self.today1= now.strftime("%d/%m/%Y")
            self.destroy()
            self.conn=sqlite3.connect("plasma.db")
            self.c=self.conn.cursor()
            y="UPDATE Last_Login_User set last_login_time=\""+str(self.Time2)+"\", last_login_date=\""+str(self.today1)+"\" where UID =\""+str(self.read1)+"\""
            #print(y)
            self.c.execute(y)
            self.conn.commit()
            root=Tk()
            clas=U_login(root)            
        else:
            pass



    def change_pasw(self):  
        self.root2 = Toplevel(self)  # Child Window "Tk() can Also be use here"
        self.root2.title("Change Password")
        self.root2.geometry("750x370+350+150")
        self.root2.configure(bg="black")
        photo1 = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
        self.root2.iconphoto(False, photo1)
        self.root2.grab_set() 
        self.root2.resizable(False, False)

        title_child = Label(self.root2, text="Reset Password", bg="#152238", fg="white",compound=LEFT, font=("Goudy Old Style", 48, "bold"), anchor="w").place(x=0, y=0, relwidth=1)
        
        phone_lbl = Label(self.root2, text="Phone No.", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=120)
        self.phone_ = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.phone_.place(x=260, y=120)
        
        current_lbl = Label(self.root2, text="Current Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=170)
        self.current_ = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.current_.place(x=260, y=170)
        
        pass_lbl = Label(self.root2, text="New Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=220)
        self.pass_ = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.pass_.place(x=260, y=220)
        
        passcon_lbl = Label(self.root2, text="Confirm Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=270)
        self.passcon = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.passcon.place(x=260, y=270)
        
        Reset_btn = Button(self.root2, text="Reset", font=("times new roman", 18, "bold"), activebackground="blue",activeforeground="white", bg="blue", fg="white", cursor="hand2", command=self.reset)
        Reset_btn.place(x=495, y=310, width=140, height=30) 

      
        
    def reset(self):
        with open("Temp.txt","r+") as file:
            self.read1=file.read()
        #print(self.read1)
        self.passw = self.pass_.get()
        self.passconw = self.passcon.get()
        self.current2_=self.current_.get()
        self.phone_2=self.phone_.get()
        
        self.conn = sqlite3.connect("plasma.db")
        self.c = self.conn.cursor()
        self.c.execute("SELECT Password from user WHERE Phone_No=" +self.phone_2)
        self.data = self.c.fetchall()
        if self.data==[]:
            return messagebox.showerror("Error"," Current Password not Matched to Your mail Id" , parent=self.root2)
        else:
            for i in self.data:
                    #print(i[0])
                    self.c.execute("SELECT Email from user WHERE Phone_No=" +self.phone_2)
                    self.data = self.c.fetchall()
                    for j in self.data:
                        a=str(j[0])
                    if i[0] == self.current2_:
                        self.OTP_Forget=str(random.randint(100000,999999))
                        send = smtplib.SMTP("smtp.gmail.com", 587)  # Create session for Gmail
                        send.starttls()  # transport layer

                        msg = EmailMessage()
                        msg["Subject"] = "OTP"
                        msg["From"] = "aj147ps@gmail.com"
                        msg["To"] = a
                        msg.set_content("Hi! your OTP for reset password: "+"\'"+str(self.OTP_Forget)+"\'")        
                            
                        try:
                            send.login("aj147ps@gmail.com","xcavbfayvnthixwy")
                        except smtplib.SMTPAuthenticationError:
                            messagebox.showerror("Error","Error Occur Otp Not")    

                        try:
                            try:
                                try:                                
                                    
                                    send.send_message(msg)
                                    messagebox.showinfo("Mailed","OTP Sent to Your Mail Id") 
                                    self.root2.destroy()
                                    self.root3 = Toplevel(self)  # Child Window "Tk() can Also be use here"
                                    self.root3.title("Verification")
                                    self.root3.geometry("750x320+350+150")
                                    self.root3.configure(bg="black")
                                    photo4 = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
                                    self.root3.iconphoto(False, photo4)
                                    self.root3.grab_set() 
                                    self.root3.resizable(False, False)
                                
                                    title_child = Label(self.root3, text="Reset Password", bg="#152238", fg="white",compound=LEFT, font=("Goudy Old Style", 48, "bold"), anchor="w").place(x=0, y=0, relwidth=1)
                                    otp_lbl = Label(self.root3, text="Enter OTP", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=120)
                                    self.otp_ = Entry(self.root3, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
                                    self.otp_.place(x=260, y=120)
                                    
                                    Reset_btn = Button(self.root3, text="Reset", font=("times new roman", 18, "bold"), activebackground="blue",activeforeground="white", bg="blue", fg="white", cursor="hand2", command=self.reset1)
                                    Reset_btn.place(x=495, y=260, width=140, height=30) 
                        
                                except smtplib.SMTPRecipientsRefused:
                                    messagebox.showerror("Mailed","Mail Not Sent")
                            except smtplib.SMTPException:
                                messagebox.showerror("Mailed","Mail Not Sent")
                        except smtplib.SMTPConnectError:
                            messagebox.showerror("Error","Connection Error")
                    else:
                        return messagebox.showerror("Error","Contact No. have not given Mail Id")

    def reset1(self):
        self.one_ = self.otp_.get()
        #print(self.one_)
        if str(self.one_)==str(self.OTP_Forget):
            if len(str(self.passw))>=8:
                if self.passw == self.passconw:
                    y= f"UPDATE user SET Password = {str(self.passw)} WHERE Phone_No = {str(self.phone_2)}"
                    self.c.execute(str(y))
                    self.conn.commit()
                    self.conn.close()
                    self.OTP_Forget=""
                    messagebox.showinfo("Info", "Successfully Changed!!", parent=self.root3)
                    self.root3.destroy()                    
                else:
                    return messagebox.showerror("Error", "Password Cann't Changed  password  and confirm password not match!!", parent=self.root3)
            else:
                return messagebox.showerror("Error", "Password should be of minimum 8 Characters", parent=self.root3)
        else:
            return messagebox.showerror("Error", "OTP Entered is Wrong", parent=self.root3)

    def clock(self):

        self.h = str(time.strftime("%H"))
        self.m = str(time.strftime("%M"))
        self.s = str(time.strftime("%S"))

        if int(self.h)<15 and int(self.m)>0:
            self.lbl_abv.config(text="PM")

        if int(self.h)>=15 and int(self.h)<20 and int(self.m)>0:
            self.lbl_abv.config(text="PM")
        
        if int(self.h)>=20 and int(self.h)<24 and int(self.m)>0:
            self.lbl_abv.config(text="PM")

        if int(self.h)>12 and int(self.h)<15 and int(self.m)>0:
            self.lbl_abv.config(text="PM")

        if int(self.h)>0 and int(self.h)<12 and int(self.m)>0:
            self.lbl_abv.config(text="AM")

         
        self.lbl_hr.config(text = self.h)
        self.lbl_min.config(text = self.m)
        self.lbl_sec.config(text = self.s)
        self.lbl_hr.after(200,self.clock)

class Hospital_Page(Tk):
    def __init__(self,*arg):       # Constructors
        Tk.__init__(self,*arg)
        photo = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
        self.iconphoto(False, photo)

        self.title("Plasma Finder".center(420))  # title for Window 
        self.configure(background = "black")  # background color for window 
        self.geometry("1360x768+0+0")
        photo = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
        self.iconphoto(False, photo)

        bg_color ="#FFFFF6"
        
     
        self.bg_icon = ImageTk.PhotoImage(file="Pics\\1 (1).jpg")
        bg_lbl = Label(self, image = self.bg_icon).pack(fill=Y) # we put image into our window
        
        self.hos_icon=ImageTk.PhotoImage(file="Pics\\1 (2) copy.jpg")
                
        
        F1 = LabelFrame(self,bd=10,relief=GROOVE,bg=bg_color)
        F1.place(x=0,relwidth=1,height=100 )

        lbl = Label(F1,text="Plasma Finder", compound=LEFT, image=self.hos_icon,bg=bg_color, font= ("times new roman",20,"bold")).place(x=0, y=5)

        self.lbl_hr = Label(F1,text="12" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_hr.place(x=890, y=40)
        
        self.lbl_COLON = Label(F1,text=":" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_COLON.place(x=915, y=40)
       
       
        self.lbl_min = Label(F1,text="12" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_min.place(x=925, y=40)
       
        self.lbl_COLON = Label(F1,text=":" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_COLON.place(x=950, y=40)
       
        self.lbl_sec = Label(F1,text="12" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_sec.place(x=960, y=40)
        

        self.lbl_abv = Label(F1,text="AM" , font = ("times new roman", 13,"bold"),bg=bg_color)
        self.lbl_abv.place(x=985, y=43)
       
       
        self.font=("times new roman",20,"bold")
        self.calendar = []

        ntpClient = ntplib.NTPClient()
        response = ntpClient.request('pool.ntp.org')
        a=ctime(response.tx_time)
        b=[a[i:i+10] for i in range(0, len(a), 10)]
        c=str(b[0])
        d=str(b[2])

        self.date = Label(F1, font=("times new roman",15,"bold"), text=c, bg=bg_color)
        self.date.place(x=740, y=40)

        self.date1 = Label(F1, font=("times new roman",15,"bold"), text=d,bg=bg_color)
        self.date1.place(x=840, y=40)

        
        self.date2 = Label(F1, font=("times new roman",15,"bold"), text="Calendar",bg=bg_color)
        self.date2.place(x=750, y=5)

        self.calendar.append(DateEntry(F1, font=("times new roman",15,"bold"), locale='en_GB',state="readonly",width=10))
        self.calendar[-1].place(x=855, y=20, anchor="w")

        
        btn_changepass = Button(F1, text="ChangePassword",relief=RAISED,width =15,height=1, font=("times new roman",14,"bold"),bg="red",foreground="white",command=self.change_pasw).place(x=1145,y=20,anchor="w")
        btn_logout = Button(F1, text="Logout",relief=RAISED,width =15,height=1, font=("times new roman",14,"bold"),bg="light green",foreground="black", command=self.logout).place(x=1145,y=60,anchor="w")

        lbl2 = Label(F1,bg=bg_color)
        lbl2.place(x=25,y=10)

        F2 = LabelFrame(self,bd=10,relief=GROOVE,bg=bg_color)
        F2.place(x=0,y=100,width=150,height=670 )

        F21 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F21.place(x=0,y=0,width=130,height=133 )
        
        F22 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F22.place(x=0,y=133,width=130,height=133)
        
        F23 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F23.place(x=0,y=266,width=130,height=133 )
        
        F24 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F24.place(x=0,y=399,width=130,height=133)
        
        F25 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F25.place(x=0,y=532,width=130,height=133)

        self.U_mange = PhotoImage(file="Pics\\User_Det.png")
        self.donor_b = ImageTk.PhotoImage(file="Pics\\Blood Donar.jpg")
        self.b_bank = ImageTk.PhotoImage(file="Pics\Blood Bank Search.jpg")    
        self.p_donar = ImageTk.PhotoImage(file="Pics\Plasma.png")
        self.exit = ImageTk.PhotoImage(file="Pics\\Exit.jpg")
        
        btn_U_det = Button(F21,image= self.U_mange,bg=bg_color,relief=RAISED,width =115,height=120,command=self.U_det).place(x=0,y=60,anchor="w")
        btn_blood_donor = Button(F22,image= self.donor_b,bg=bg_color,relief=RAISED,width =115,height=120,command=self.Blood_Donar ).place(x=0,y=60,anchor="w")
        btn_blood_bank = Button(F23,relief=RAISED,bg=bg_color,image=self.b_bank,width =115,height=120,command=self.Blood_Bank ).place(x=0,y=60,anchor="w")
        btn_Plasma = Button(F24,relief=RAISED,image=self.p_donar,bg=bg_color,width =115,height=120, command=self.Plasma).place(x=0,y=60,anchor="w")
        btn_Exit = Button(F25,relief=RAISED,bg=bg_color,image=self.exit,width =115,height=120, command=self.Exit).place(x=0,y=60,anchor="w")

        #------------------------------F3--------------------------------
        F3 = LabelFrame(self,bd=5,relief=FLAT,bg="light gray")
        F3.place(x=150,y=100,relwidth=1,height=60 )
        lbl_1= Label(F3,text="Dashboard / Hospital",font=("comic sans",15,"italic"),bg="light gray")
        lbl_1.place(x=0,y=10)

        btn_User = Button(F3, bd=5, relief=GROOVE, bg="red", fg="white", font=("",15,"bold"), text= "User View",command=self.User_Check)
        btn_User.place(x=1000,y=0)

        self.conn=sqlite3.connect("plasma.db")
        self.c=self.conn.cursor()
        

        F4 = LabelFrame(self,bd=10,relief=GROOVE,bg="#DC143C")
        F4.place(x=300,y=170,width=400,height=250 )

        F41 = LabelFrame(F4,bd=5,relief=SUNKEN,bg="#DC143C")
        F41.place(x=0,y=0,width=380,height=60 )
        lbl_2= Label(F41,text="Total Users",fg="#FFFFFF",bg="#DC143C",font=("times new roman",25,"bold"))
        lbl_2.place(x=0,y=0)

        
        F42 = LabelFrame(F4,bd=5,relief=GROOVE)
        F42.place(x=0,y=60,width=380,height=180 )

        text1=Text(F42,bd=5, font=("times new roman",30,"bold"))
        self.c.execute("SELECT COUNT(*) FROM user")
        self.results1 = ((self.c).fetchall())        
        text1.insert(INSERT,("\n             Total\n           Users: "))
        text1.insert(INSERT,self.results1)
        text1.place(x=0,y=0,width=370,height=170)
        text1.configure(state="disabled")
                        

        F5 = LabelFrame(self,bd=10,relief=GROOVE)
        F5.place(x=800,y=170,width=400,height=250 )

        F51 = LabelFrame(F5,bd=5,relief=SUNKEN, bg="#3B9C9C")
        F51.place(x=0,y=0,width=380,height=60 )
        lbl_3= Label(F51,text="Last Login",fg="#FFFFFF",bg="#3B9C9C",font=("times new roman",30,"bold"))
        lbl_3.place(x=0,y=0)

        
        F52 = LabelFrame(F5,bd=5,relief=GROOVE)
        F52.place(x=0,y=60,width=380,height=180 )

        with open("Temp1.txt","r+") as file:
            self.read1=file.read()
        text2=Text(F52,bd=5, fg="white",font=("times new roman",15,"bold"),bg="#151B54")
        self.c.execute("SELECT * FROM Last_Login_hospital WHERE HID =\""+str(self.read1)+"\"")
        self.results2 = ((self.c).fetchall())        
        text2.insert(INSERT,(""))
        if self.results2:
            for i in self.results2:
                a=i    
            #self.EmpID.set(i[0])  
            text2.insert(INSERT,("\nUID                     :   "+str(i[0]+" ")))
            text2.insert(INSERT,("\nEmail                   :   "+str(i[1])+"\n"))
            text2.insert(INSERT,("Last Login Time :   "+str(i[2])+"\n"))
            text2.insert(INSERT,("Last Login Date :   "+str(i[3])+"\n"))

            text2.place(x=0,y=0,width=370,height=170)
            text2.configure(state="disabled")

        
        
        F6 = LabelFrame(self,bd=10,relief=GROOVE)
        F6.place(x=300,y=450,width=400,height=250 )

        F61 = LabelFrame(F6,bd=5,relief=SUNKEN,fg="#FFFFFF",bg="black")
        F61.place(x=0,y=0,width=380,height=60 )
        lbl_4= Label(F61,text="Total Hospitals",bg="black",fg="#FFFFFF",font=("times new roman",30,"bold"))
        lbl_4.place(x=0,y=0)


        F62 = LabelFrame(F6,bd=5,relief=GROOVE)
        F62.place(x=0,y=60,width=380,height=180 )

        text3=Text(F62,bd=5, fg="white",font=("times new roman",30,"bold"),bg="#151B54")
        self.c.execute("SELECT COUNT(*) FROM hos")
        self.results3 = ((self.c).fetchall())        
        text3.insert(INSERT,("\n             Total\n         Hospitals: "))
        text3.insert(INSERT,self.results3)
        text3.place(x=0,y=0,width=370,height=170)
        text3.configure(state="disabled")

        
        
        F7 = LabelFrame(self,bd=10,relief=GROOVE)
        F7.place(x=800,y=450,width=400,height=250 )
        
        F71 = LabelFrame(F7,bd=5,relief=SUNKEN,bg="white")
        F71.place(x=0,y=0,width=380,height=60 )
        lbl_4= Label(F71,text="Developer",bg="white",font=("times new roman",30,"bold"),fg="#DC143C")
        lbl_4.place(x=0,y=0)


        F72 = LabelFrame(F7,bd=5,relief=RAISED)
        F72.place(x=0,y=60,width=380,height=180 )

        text7=Text(F72,bd=5,font=("times new roman",15, "italic"),fg="#FFFFFF", bg="#DC143C",relief=GROOVE)
        text7.insert(INSERT,("                       Developed By\n\nAditya Jha\nEmail Id:aj147ps@gmail.com\nAlternate Email Id:codewithajofficial14@gmail.com\nFollow on #codewithajofficial on insta "))
        text7.place(x=0,y=0,width=370,height=170)
        text7.configure(state="disabled")
        self.clock()

    def U_det(self):
        self.destroy()
        H_Manage().mainloop()
        
    def Blood_Donar(self):
        self.destroy()
        Bload_Search_hos().mainloop()
        
    
    def Blood_Bank(self):
        self.destroy()
        Bload_Bank_hos().mainloop()

    def Plasma(self):
        self.destroy()
        Plasma_Search_hos().mainloop()    
    
    def Exit(self):
        self.destroy()

    def User_Check(self):
        self.destroy
        User_Check_class().mainloop()

    
    def Exit(self):
        self.destroy()

    
    def logout(self):
        self.read1=StringVar()
        with open("Temp1.txt","r+") as file:
            self.read1=file.read()
            file.truncate()
    
        a=messagebox.askyesnocancel("Hey","Confirm again for Logout")
        if a>0:
            now = datetime.now()
            self.Time2=now.strftime('%H:%M:%S')

            self.today1= now.strftime("%d/%m/%Y")
            self.destroy()
            self.conn=sqlite3.connect("plasma.db")
            self.c=self.conn.cursor()
            y="UPDATE Last_Login_hospital set time=\""+str(self.Time2)+"\", date=\""+str(self.today1)+"\" where HID =\""+str(self.read1)+"\""
            #print(y)
            self.c.execute(y)
            self.conn.commit()
            root=Tk()
            clas=H_login(root)            
        else:
            pass



    def change_pasw(self):  
        self.root2 = Toplevel(self)  # Child Window "Tk() can Also be use here"
        self.root2.title("Change Password")
        self.root2.geometry("750x370+350+150")
        self.root2.configure(bg="black")
        photo1 = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
        self.root2.iconphoto(False, photo1)
        self.root2.grab_set() 
        self.root2.resizable(False, False)

        title_child = Label(self.root2, text="Reset Password", bg="#152238", fg="white",compound=LEFT, font=("Goudy Old Style", 48, "bold"), anchor="w").place(x=0, y=0, relwidth=1)
        
        phone_lbl = Label(self.root2, text="Phone No.", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=120)
        self.phone_ = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.phone_.place(x=260, y=120)
        
        current_lbl = Label(self.root2, text="Current Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=170)
        self.current_ = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.current_.place(x=260, y=170)
        
        pass_lbl = Label(self.root2, text="New Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=220)
        self.pass_ = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.pass_.place(x=260, y=220)
        
        passcon_lbl = Label(self.root2, text="Confirm Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=270)
        self.passcon = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.passcon.place(x=260, y=270)
        
        Reset_btn = Button(self.root2, text="Reset", font=("times new roman", 18, "bold"), activebackground="blue",activeforeground="white", bg="blue", fg="white", cursor="hand2", command=self.reset)
        Reset_btn.place(x=495, y=310, width=140, height=30) 

      
        
    def reset(self):
        with open("Temp.txt","r+") as file:
            self.read1=file.read()
        #print(self.read1)
        self.passw = self.pass_.get()
        self.passconw = self.passcon.get()
        self.current2_=self.current_.get()
        self.phone_2=self.phone_.get()
        
        self.conn = sqlite3.connect("plasma.db")
        self.c = self.conn.cursor()
        self.c.execute("SELECT Password from user WHERE Phone_No=" +self.phone_2)
        self.data = self.c.fetchall()
        if self.data==[]:
            return messagebox.showerror("Error"," Current Password not Matched to Your mail Id" , parent=self.root2)
        else:
            for i in self.data:
                    #print(i[0])
                    self.c.execute("SELECT Email from user WHERE Phone_No=" +self.phone_2)
                    self.data = self.c.fetchall()
                    for j in self.data:
                        a=str(j[0])
                    if i[0] == self.current2_:
                        self.OTP_Forget=str(random.randint(100000,999999))
                        send = smtplib.SMTP("smtp.gmail.com", 587)  # Create session for Gmail
                        send.starttls()  # transport layer

                        msg = EmailMessage()
                        msg["Subject"] = "OTP"
                        msg["From"] = "aj147ps@gmail.com"
                        msg["To"] = a
                        msg.set_content("Hi! your OTP for reset password: "+"\'"+str(self.OTP_Forget)+"\'")        
                            
                        try:
                            send.login("aj147ps@gmail.com","xcavbfayvnthixwy")
                        except smtplib.SMTPAuthenticationError:
                            messagebox.showerror("Error","Error Occur Otp Not")    

                        try:
                            try:
                                try:                                
                                    
                                    send.send_message(msg)
                                    messagebox.showinfo("Mailed","OTP Sent to Your Mail Id") 
                                    self.root2.destroy()
                                    self.root3 = Toplevel(self)  # Child Window "Tk() can Also be use here"
                                    self.root3.title("Verification")
                                    self.root3.geometry("750x320+350+150")
                                    self.root3.configure(bg="black")
                                    photo4 = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
                                    self.root3.iconphoto(False, photo4)
                                    self.root3.grab_set() 
                                    self.root3.resizable(False, False)
                                
                                    title_child = Label(self.root3, text="Reset Password", bg="#152238", fg="white",compound=LEFT, font=("Goudy Old Style", 48, "bold"), anchor="w").place(x=0, y=0, relwidth=1)
                                    otp_lbl = Label(self.root3, text="Enter OTP", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=120)
                                    self.otp_ = Entry(self.root3, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
                                    self.otp_.place(x=260, y=120)
                                    
                                    Reset_btn = Button(self.root3, text="Reset", font=("times new roman", 18, "bold"), activebackground="blue",activeforeground="white", bg="blue", fg="white", cursor="hand2", command=self.reset1)
                                    Reset_btn.place(x=495, y=260, width=140, height=30) 
                        
                                except smtplib.SMTPRecipientsRefused:
                                    messagebox.showerror("Mailed","Mail Not Sent")
                            except smtplib.SMTPException:
                                messagebox.showerror("Mailed","Mail Not Sent")
                        except smtplib.SMTPConnectError:
                            messagebox.showerror("Error","Connection Error")
                    else:
                        return messagebox.showerror("Error","Contact No. have not given Mail Id")

    def reset1(self):
        self.one_ = self.otp_.get()
        #print(self.one_)
        if str(self.one_)==str(self.OTP_Forget):
            if len(str(self.passw))>=8:
                if self.passw == self.passconw:
                    y= f"UPDATE user SET Password = {str(self.passw)} WHERE Phone_No = {str(self.phone_2)}"
                    self.c.execute(str(y))
                    self.conn.commit()
                    self.conn.close()
                    self.OTP_Forget=""
                    messagebox.showinfo("Info", "Successfully Changed!!", parent=self.root3)
                    self.root3.destroy()                    
                else:
                    return messagebox.showerror("Error", "Password Cann't Changed  password  and confirm password not match!!", parent=self.root3)
            else:
                return messagebox.showerror("Error", "Password should be of minimum 8 Characters", parent=self.root3)
        else:
            return messagebox.showerror("Error", "OTP Entered is Wrong", parent=self.root3)

    def clock(self):

        self.h = str(time.strftime("%H"))
        self.m = str(time.strftime("%M"))
        self.s = str(time.strftime("%S"))

        if int(self.h)<15 and int(self.m)>0:
            self.lbl_abv.config(text="PM")

        if int(self.h)>=15 and int(self.h)<20 and int(self.m)>0:
            self.lbl_abv.config(text="PM")
        
        if int(self.h)>=20 and int(self.h)<24 and int(self.m)>0:
            self.lbl_abv.config(text="PM")

        if int(self.h)>12 and int(self.h)<15 and int(self.m)>0:
            self.lbl_abv.config(text="PM")

        if int(self.h)>0 and int(self.h)<12 and int(self.m)>0:
            self.lbl_abv.config(text="AM")

         
        self.lbl_hr.config(text = self.h)
        self.lbl_min.config(text = self.m)
        self.lbl_sec.config(text = self.s)
        self.lbl_hr.after(200,self.clock)

class U_Manage(Tk):
    def __init__(self,*arg):       # Constructors
        Tk.__init__(self,*arg)
        photo = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
        self.iconphoto(False, photo)

        self.title("Plasma Finder".center(420))  # title for Window 
        self.configure(background = "black")  # background color for window 
        self.geometry("1360x768+0+0")
        photo = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
        self.iconphoto(False, photo)

        bg_color ="#FFFFF6"
        
     
        self.bg_icon = ImageTk.PhotoImage(file="Pics\\1 (1).jpg")
        bg_lbl = Label(self, image = self.bg_icon).pack(fill=Y) # we put image into our window
        
        self.hos_icon=ImageTk.PhotoImage(file="Pics\\1 (2) copy.jpg")
                
        
        F1 = LabelFrame(self,bd=10,relief=GROOVE,bg=bg_color)
        F1.place(x=0,relwidth=1,height=100 )

        lbl = Label(F1,text="Plasma Finder", compound=LEFT, image=self.hos_icon,bg=bg_color, font= ("times new roman",20,"bold")).place(x=0, y=5)

        self.lbl_hr = Label(F1,text="12" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_hr.place(x=890, y=40)
        
        self.lbl_COLON = Label(F1,text=":" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_COLON.place(x=915, y=40)
       
       
        self.lbl_min = Label(F1,text="12" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_min.place(x=925, y=40)
       
        self.lbl_COLON = Label(F1,text=":" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_COLON.place(x=950, y=40)
       
        self.lbl_sec = Label(F1,text="12" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_sec.place(x=960, y=40)
        

        self.lbl_abv = Label(F1,text="AM" , font = ("times new roman", 13,"bold"),bg=bg_color)
        self.lbl_abv.place(x=985, y=43)
       
       
        self.font=("times new roman",20,"bold")
        self.calendar = []

        ntpClient = ntplib.NTPClient()
        response = ntpClient.request('pool.ntp.org')
        a=ctime(response.tx_time)
        b=[a[i:i+10] for i in range(0, len(a), 10)]
        c=str(b[0])
        d=str(b[2])

        self.date = Label(F1, font=("times new roman",15,"bold"), text=c, bg=bg_color)
        self.date.place(x=740, y=40)

        self.date1 = Label(F1, font=("times new roman",15,"bold"), text=d,bg=bg_color)
        self.date1.place(x=840, y=40)

        
        self.date2 = Label(F1, font=("times new roman",15,"bold"), text="Calendar",bg=bg_color)
        self.date2.place(x=750, y=5)

        self.calendar.append(DateEntry(F1, font=("times new roman",15,"bold"), locale='en_GB',state="readonly",width=10))
        self.calendar[-1].place(x=855, y=20, anchor="w")

        
        btn_changepass = Button(F1, text="ChangePassword",relief=RAISED,width =15,height=1, font=("times new roman",14,"bold"),bg="red",foreground="white",command=self.change_pasw).place(x=1145,y=20,anchor="w")
        btn_logout = Button(F1, text="Logout",relief=RAISED,width =15,height=1, font=("times new roman",14,"bold"),bg="light green",foreground="black", command=self.logout).place(x=1145,y=60,anchor="w")

        lbl2 = Label(F1,bg=bg_color)
        lbl2.place(x=25,y=10)

        F2 = LabelFrame(self,bd=10,relief=GROOVE,bg=bg_color)
        F2.place(x=0,y=100,width=150,height=670 )

        F21 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F21.place(x=0,y=0,width=130,height=133 )
        
        F22 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F22.place(x=0,y=133,width=130,height=133)
        
        F23 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F23.place(x=0,y=266,width=130,height=133 )
        
        F24 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F24.place(x=0,y=399,width=130,height=133)
        
        F25 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F25.place(x=0,y=532,width=130,height=133)

        self.U_mange = PhotoImage(file="Pics\\User_Det.png")
        self.donor_b = ImageTk.PhotoImage(file="Pics\\Blood Donar.jpg")
        self.b_bank = ImageTk.PhotoImage(file="Pics\Blood Bank Search.jpg")    
        self.p_donar = ImageTk.PhotoImage(file="Pics\Plasma.png")
        self.exit = ImageTk.PhotoImage(file="Pics\\Exit.jpg")
        
        btn_U_det = Button(F21,image= self.U_mange,bg=bg_color,relief=RAISED,width =115,height=120,command=self.U_det).place(x=0,y=60,anchor="w")
        btn_blood_donor = Button(F22,image= self.donor_b,bg=bg_color,relief=RAISED,width =115,height=120,command=self.Blood_Donar ).place(x=0,y=60,anchor="w")
        btn_blood_bank = Button(F23,relief=RAISED,bg=bg_color,image=self.b_bank,width =115,height=120,command=self.Blood_Bank ).place(x=0,y=60,anchor="w")
        btn_Plasma = Button(F24,relief=RAISED,image=self.p_donar,bg=bg_color,width =115,height=120, command=self.Plasma).place(x=0,y=60,anchor="w")
        btn_Exit = Button(F25,relief=RAISED,bg=bg_color,image=self.exit,width =115,height=120, command=self.Exit).place(x=0,y=60,anchor="w")

        F3 = LabelFrame(self,bd=5,relief=FLAT,bg="light gray")
        F3.place(x=150,y=100,relwidth=1,height=30 )
        lbl_1= Label(F3,text="Dashboard / User",font=("comic sans",15,"italic"),bg="light gray")
        lbl_1.place(x=0,y=0)
        home_btn = Button(F3, text="Home",bd=5,relief=GROOVE, font=("",7,"bold"), fg="white", bg="blue", command=self.Home)
        home_btn.place(x=300,y=-2)

        self.UID = StringVar()
        self.Name = StringVar()
        self.Email = StringVar()
        self.pass_ = StringVar()
        self.contact = StringVar()
        self.code = IntVar()
        self.BloodID = StringVar()
        self.branchID = StringVar()
        
        self.FM1 = Frame(self,bd=5,relief=RAISED)
        self.FM1.place(x=430,y=160,width=700,height=550 )



        FM11 =Frame(self.FM1,bd=5,relief=RAISED,bg="yellow")
        FM11.place(x=0,y=0,relwidth=1,height=60 )
        lbl_FM11= Label(FM11,text="Manage User Data",font=("times new roman",30,"bold"),fg="black",bg="yellow")
        lbl_FM11.place(x=20,y=0)

        lblID_roll=Label(FM11,text="UID",bg="yellow",font=("times new roman",18,"bold"))
        lblID_roll.place(x=400,y=25,anchor="w")
        txtID_roll=Entry(FM11, width=17, textvariable=self.UID,font=("times new roman",15,"bold"),bd=5,relief=GROOVE,state="readonly")
        txtID_roll.place(x=485,y=25,anchor="w")






        FM12 =Frame(self.FM1,bd=10,relief=SUNKEN,bg="#074463")
        FM12.place(x=0,y=440,relwidth=1,height=80 )

        
        
        btn_update2 = Button(FM12,relief=GROOVE,width=8, font=("times new roman",18,"bold"),bd=6,text="Update",command=self.add).grid(row=0,column=1,pady=6,padx=50,sticky="nesw")        
        btn_Delete = Button(FM12,relief=GROOVE, width=8,font=("times new roman",18,"bold"),bd=6,text="Delete",command=self.delete).grid(row=0,column=2,pady=6,padx=50,sticky="nesw")
        btn_Clear = Button(FM12,relief=GROOVE, width=8,font=("times new roman",18,"bold"),bd=6,text="Clear",command=self.clear).grid(row=0,column=3,pady=6,padx=50,sticky="nesw")        

       

        lbl_roll=Label(self.FM1,text="Name",font=("times new roman",18,"bold"),bg="#F5F5F5")
        lbl_roll.place(x=0,y=90,anchor="w")
        txt_roll=Entry(self.FM1,  width=17, textvariable=self.Name,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.place(x=120,y=90,anchor="w")

        lbl_roll=Label(self.FM1,text="Email",bg="#F5F5F5",font=("times new roman",18,"bold"))
        lbl_roll.place(x=0,y=140,anchor="w")
        txt_roll=Entry(self.FM1, width=17,textvariable=self.Email, state="readonly",font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.place(x=120,y=140,anchor="w")
        
        lbl_roll=Label(self.FM1,text="Password",bg="#F5F5F5",font=("times new roman",18,"bold"))
        lbl_roll.place(x=0,y=190,anchor="w")
        txt_roll=Entry(self.FM1, width=17,textvariable=self.pass_, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.place(x=120,y=190,anchor="w")

        lbl_roll=Label(self.FM1,text="Contact",bg="#F5F5F5",font=("times new roman",18,"bold"))
        lbl_roll.place(x=0, y=240, anchor="w")
        self.code.set(0)
        combo_code = OptionMenu(self.FM1, self.code,"+93","+355","+213","+1684","+376","+244","+1264","+672","+1268","+54","+374","+297","+61","+880","+32","+226","+359","+387","+1246","+681","+590","+1441","+673","+591","+973","+257","+229","+975","+1876","+267","+685","+599","+55","+1242","+441534","+375","+501","+7","+250","+381","+670","+262","+993","+992","+40","+690","+245","+1671","+502","+30","+240","+590","+81","+592","+441481","+594","+995","+1473","+44","+241","+503","+224","+220","+299","+350","+233","+968","+216","+962","+385","+509","+36","+852""+504","+58","+1787","+1939","+970","+680","+351","+47","+595","+964","+507","+689","+675","+51","+92","+63","+870","+48","+508","+260","+212","+372","+20","+27","+593","+39","+84","+677","+251","+252","+263","+966","+34","+291","+382","+373","+261","+590","+212","+377","+998","+95","+223","+853","+976","+692","+389","+230","+356","+265","+960","+596","+1670","+1664","+222","+441624","+256","+255","+60","+52","+972","+33","+246","+290","+358","+679","+500","+691","+298","+505","+31","+47","+264","+678","+687","+227","+672","+234","+64","+977","+674","+683","+682","+225","+41","+57","+86","+237","+56","+61","+1","+242","+236","+243","+420","+357","+61","+506","+599","+238","+53","+268","+963","+599","+996","+254","+211","+597","+686","+855","+1869","+269","+239","+421","+82","+386","+850","+965","+221","+378","+232","+248","+7","+1345","+65","+46","+249","+1809","1-829","+1767","+253","+45","+1-284","+49","+967","+213","+1","+598","+262","+1","+961","+1758","+856","+688","+886","+1868","+90","+94","+423","+371","+676","+370","+352","+231","+266","+66","+228","+235","+1649","+218","+379","+1784","+971","+376","+1268","+93","+1264","+1340","+354","+98","+374","+355","+244","+1684","+54","+61","+43","+297","+91","+35818","+994","+353","+62","+380","+974","+258" )
        combo_code.place(x=118,y=240,anchor="w")
        txt_roll=Entry(self.FM1, width=14, textvariable=self.contact, font=("times new roman",12,"bold"),bd=5,relief=GROOVE)
        txt_roll.place(x=175,y=240,anchor="w")


        blood_grp=Label(self.FM1,text="Blood Group", font=("times new roman",18,"bold"),bg="#F5F5F5")
        blood_grp.place(x=0,y=290, anchor="w")
        blood_grp_1=ttk.Combobox(self.FM1, textvariable=self.BloodID,width=17, font=("times new roman",13,"bold"),state='readonly')
        blood_grp_1['values']=("A+","B+","AB+","O+","A-","B-","AB-","O-")
        blood_grp_1.place(x=140,y=290, anchor="w")
        
        Donar_lb=Label(self.FM1,text="Want to Be Donor", font=("times new roman",18,"bold"),bg="#F5F5F5")
        Donar_lb.place(x=0, y=345, anchor="w")
        combo_Donor=ttk.Combobox(self.FM1, width=17,textvariable=self.branchID, font=("times new roman",13,"bold"),state='readonly')
        combo_Donor['values']=("Yes","No")
        combo_Donor.place(x=200, y=345, anchor="w")

        with open("Temp.txt","r+") as file:
            self.read2=str(file.read())
        self.conn=sqlite3.connect("plasma.db")
        self.c = self.conn.cursor()
        # c.execute("SELECT Email from user WHERE UID="+str(c))
        self.cmd = "SELECT Email from user WHERE UID = '" +self.read2 + "'"

        self.c.execute(self.cmd)
        self.data=self.c.fetchall()
        if self.data:
            for i in self.data:
                    a=str(i[0])
        self.c.execute(self.cmd)
        self.Email.set(a)
            

        self.UID.set(self.read2)
        self.clock()
    
    def add(self):

        if self.Name.get()=="" and self.pass_.get()=="" and self.Email.get()=="" and self.contact.get()=="" and self.code.get()==0 and self.BloodID.get()=="" and self.branchID.get()=="" :
            return messagebox.showerror("Error!","All Feilds Required")
        
        if self.Name.get()=='':
            return messagebox.showinfo('Error','Enter a Name')
        
        if self.Email.get()=='':
            return messagebox.showinfo('Error','Enter a Email address')

        if "@" not in self.Email.get():
            return messagebox.showwarning("Warrning","Email should have '@' Character")

            
        if self.pass_.get()=='':
            return messagebox.showinfo('Error','Enter a password')

        if len(str(self.pass_.get()))<8:
            return messagebox.showwarning("Warning","Password should be Minimum 8 charactrs")
        
        if self.contact.get()=='':
            return messagebox.showinfo('Error','Enter a contact')
        
        try:
            tmp=self.contact.get()
            int(tmp)
        except ValueError:
            return messagebox.showinfo('Error','Contact No. Should Be Integer')
        
        if len(self.contact.get()+str(self.code.get()))<10 and len(self.contact.get()+str(self.code.get()))>15:
            return messagebox.showinfo('Error','Enter a valid contact')      
        
        if self.code.get()==0:
            return messagebox.showinfo('Error','Choose Country Code')

        else:
            try:    
                self.con2 = str(region_code_for_country_code(self.code.get()))
                self.conn=sqlite3.connect("plasma.db")
                self.c=self.conn.cursor()
                self.c.execute("CREATE TABLE IF NOT EXISTS user_details(UID TEXT PRIMARY KEY ,Name TEXT, B_Group TEXT  , W_D TEXT )")
                    
                self.c.execute("INSERT INTO user_details (UID, Name, B_Group, W_D ) VALUES (?,?,?,?)",(self.UID.get(),self.Name.get(),str(self.BloodID.get()),self.branchID.get()))
                y=\
                        """UPDATE user SET UID  =\"""" + self.UID.get()+\
                        """\" , Email    =\""""+ self.Email.get()+\
                        """\" , Country_Code =\""""+ str(self.code.get())+\
                        """\" , Country   =\""""+ str(self.con2)+\
                        """\" , Phone_No  =\""""+ str(self.contact.get()) +\
                        """\" , Password  =\""""+ self.pass_.get() +\
                        """ \""""
                y=y+" WHERE UID= '" +self.UID.get() + "'"
                #print(str(y))              
                self.c.execute(y)
                self.conn.commit()
                messagebox.showinfo("Info"," Data Updated")
                self.conn.commit()
                self.conn.close()
                self.clear()
            except Exception:
                return messagebox.showerror("Error!!","Somthing went wrong not able to add data try again ")
            self.clear()        
    
        
    
    def delete(self):
        try:
            self.conn=sqlite3.connect("plasma.db")
            self.c=self.conn.cursor()
            self.c.execute("SELECT * from user WHERE UID= '"+str(self.UID.get()+ "'"))
            self.data=self.c.fetchall()
            if self.data:
                self.c.execute("DELETE FROM user WHERE UID = '" +str(self.UID.get()+ "'"))
                self.c.execute("DELETE FROM user_details WHERE UID = '" +str(self.UID.get()+ "'"))
                try:
                    self.c.execute("DELETE FROM Blood_Donor_Approved WHERE UID = '" +str(self.UID.get()+ "'"))
                except Exception:
                    pass
                try:
                    self.c.execute("DELETE FROM Plasma_Donar WHERE UID = '" +str(self.UID.get()+ "'"))
                except Exception:
                    pass

                self.conn.commit()
                self.conn.close()
                messagebox.showinfo("Info","Succesfully Deleted")
                self.clear()
            else:
                messagebox.showinfo("Info","Data not Exist")
                self.destroy()
                root=Tk()
                clas=U_login(root)
                win1.new=clas


        except sqlite3.Error as error:
            messagebox.showerror("error","Failed to update sqlite table")

    def clear(self):
        with open("Temp.txt","r+") as file:
            self.read2=str(file.read())
        self.conn=sqlite3.connect("plasma.db")
        self.c = self.conn.cursor()
        # c.execute("SELECT Email from user WHERE UID="+str(c))
        self.cmd = "SELECT Email from user WHERE UID = '" +self.read2 + "'"

        self.c.execute(self.cmd)
        self.data=self.c.fetchall()
        if self.data:
            for i in self.data:
                    a=str(i[0])
        self.c.execute(self.cmd)
        self.Email.set(a)
            

        self.UID.set(self.read2)
        self.Name.set("")
        self.Email.set(a)
        self.pass_.set("")
        self.contact.set("")
        self.code.set(0)
        self.BloodID.set("")
        self.branchID.set("")
        
    def Home(self):
        self.destroy()
        User_Page().mainloop()

    def U_det(self):
        self.destroy()
        U_Manage().mainloop()
        
    def Blood_Donar(self):
        self.destroy()
        Bload_Search().mainloop()
        
    
    def Blood_Bank(self):
        self.destroy()
        Bload_Bank().mainloop()

    def Plasma(self):
        self.destroy()
        Plasma_Search().mainloop()    
    
    def Exit(self):
        self.destroy()

    
    def logout(self):
        self.read1=StringVar()
        with open("Temp.txt","r+") as file:
            self.read1=file.read()
            file.truncate()
    
        a=messagebox.askyesnocancel("Hey","Confirm again for Logout")
        if a>0:
            now = datetime.now()
            self.Time2=now.strftime('%H:%M:%S')

            self.today1= now.strftime("%d/%m/%Y")
            self.destroy()
            self.conn=sqlite3.connect("plasma.db")
            self.c=self.conn.cursor()
            y="UPDATE Last_Login_User set last_login_time=\""+str(self.Time2)+"\", last_login_date=\""+str(self.today1)+"\" where UID =\""+str(self.read1)+"\""
            #print(y)
            self.c.execute(y)
            self.conn.commit()
            root=Tk()
            clas=U_login(root)            
        else:
            pass



    def change_pasw(self):  
        self.root2 = Toplevel(self)  # Child Window "Tk() can Also be use here"
        self.root2.title("Change Password")
        self.root2.geometry("750x370+350+150")
        self.root2.configure(bg="black")
        photo1 = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
        self.root2.iconphoto(False, photo1)
        self.root2.grab_set() 
        self.root2.resizable(False, False)

        title_child = Label(self.root2, text="Reset Password", bg="#152238", fg="white",compound=LEFT, font=("Goudy Old Style", 48, "bold"), anchor="w").place(x=0, y=0, relwidth=1)
        
        phone_lbl = Label(self.root2, text="Phone No.", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=120)
        self.phone_ = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.phone_.place(x=260, y=120)
        
        current_lbl = Label(self.root2, text="Current Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=170)
        self.current_ = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.current_.place(x=260, y=170)
        
        pass_lbl = Label(self.root2, text="New Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=220)
        self.pass_ = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.pass_.place(x=260, y=220)
        
        passcon_lbl = Label(self.root2, text="Confirm Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=270)
        self.passcon = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.passcon.place(x=260, y=270)
        
        Reset_btn = Button(self.root2, text="Reset", font=("times new roman", 18, "bold"), activebackground="blue",activeforeground="white", bg="blue", fg="white", cursor="hand2", command=self.reset)
        Reset_btn.place(x=495, y=310, width=140, height=30) 

      
        
    def reset(self):
        with open("Temp.txt","r+") as file:
            self.read1=file.read()
        #print(self.read1)
        self.passw = self.pass_.get()
        self.passconw = self.passcon.get()
        self.current2_=self.current_.get()
        self.phone_2=self.phone_.get()
        
        self.conn = sqlite3.connect("plasma.db")
        self.c = self.conn.cursor()
        self.c.execute("SELECT Password from user WHERE Phone_No=" +self.phone_2)
        self.data = self.c.fetchall()
        if self.data==[]:
            return messagebox.showerror("Error"," Current Password not Matched to Your mail Id" , parent=self.root2)
        else:
            for i in self.data:
                    #print(i[0])
                    self.c.execute("SELECT Email from user WHERE Phone_No=" +self.phone_2)
                    self.data = self.c.fetchall()
                    for j in self.data:
                        a=str(j[0])
                    if i[0] == self.current2_:
                        self.OTP_Forget=str(random.randint(100000,999999))
                        send = smtplib.SMTP("smtp.gmail.com", 587)  # Create session for Gmail
                        send.starttls()  # transport layer

                        msg = EmailMessage()
                        msg["Subject"] = "OTP"
                        msg["From"] = "aj147ps@gmail.com"
                        msg["To"] = a
                        msg.set_content("Hi! your OTP for reset password: "+"\'"+str(self.OTP_Forget)+"\'")        
                            
                        try:
                            send.login("aj147ps@gmail.com","xcavbfayvnthixwy")
                        except smtplib.SMTPAuthenticationError:
                            messagebox.showerror("Error","Error Occur Otp Not")    

                        try:
                            try:
                                try:                                
                                    
                                    send.send_message(msg)
                                    messagebox.showinfo("Mailed","OTP Sent to Your Mail Id") 
                                    self.root2.destroy()
                                    self.root3 = Toplevel(self)  # Child Window "Tk() can Also be use here"
                                    self.root3.title("Verification")
                                    self.root3.geometry("750x320+350+150")
                                    self.root3.configure(bg="black")
                                    photo4 = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
                                    self.root3.iconphoto(False, photo4)
                                    self.root3.grab_set() 
                                    self.root3.resizable(False, False)
                                
                                    title_child = Label(self.root3, text="Reset Password", bg="#152238", fg="white",compound=LEFT, font=("Goudy Old Style", 48, "bold"), anchor="w").place(x=0, y=0, relwidth=1)
                                    otp_lbl = Label(self.root3, text="Enter OTP", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=120)
                                    self.otp_ = Entry(self.root3, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
                                    self.otp_.place(x=260, y=120)
                                    
                                    Reset_btn = Button(self.root3, text="Reset", font=("times new roman", 18, "bold"), activebackground="blue",activeforeground="white", bg="blue", fg="white", cursor="hand2", command=self.reset1)
                                    Reset_btn.place(x=495, y=260, width=140, height=30) 
                        
                                except smtplib.SMTPRecipientsRefused:
                                    messagebox.showerror("Mailed","Mail Not Sent")
                            except smtplib.SMTPException:
                                messagebox.showerror("Mailed","Mail Not Sent")
                        except smtplib.SMTPConnectError:
                            messagebox.showerror("Error","Connection Error")
                    else:
                        return messagebox.showerror("Error","Contact No. have not given Mail Id")

    def reset1(self):
        self.one_ = self.otp_.get()
        #print(self.one_)
        if str(self.one_)==str(self.OTP_Forget):
            if len(str(self.passw))>=8:
                if self.passw == self.passconw:
                    y= f"UPDATE user SET Password = {str(self.passw)} WHERE Phone_No = {str(self.phone_2)}"
                    self.c.execute(str(y))
                    self.conn.commit()
                    self.conn.close()
                    self.OTP_Forget=""
                    messagebox.showinfo("Info", "Successfully Changed!!", parent=self.root3)
                    self.root3.destroy()                    
                else:
                    return messagebox.showerror("Error", "Password Cann't Changed  password  and confirm password not match!!", parent=self.root3)
            else:
                return messagebox.showerror("Error", "Password should be of minimum 8 Characters", parent=self.root3)
        else:
            return messagebox.showerror("Error", "OTP Entered is Wrong", parent=self.root3)

    def clock(self):

        self.h = str(time.strftime("%H"))
        self.m = str(time.strftime("%M"))
        self.s = str(time.strftime("%S"))

        if int(self.h)<15 and int(self.m)>0:
            self.lbl_abv.config(text="PM")

        if int(self.h)>=15 and int(self.h)<20 and int(self.m)>0:
            self.lbl_abv.config(text="PM")
        
        if int(self.h)>=20 and int(self.h)<24 and int(self.m)>0:
            self.lbl_abv.config(text="PM")

        if int(self.h)>12 and int(self.h)<15 and int(self.m)>0:
            self.lbl_abv.config(text="PM")

        if int(self.h)>0 and int(self.h)<12 and int(self.m)>0:
            self.lbl_abv.config(text="AM")

         
        self.lbl_hr.config(text = self.h)
        self.lbl_min.config(text = self.m)
        self.lbl_sec.config(text = self.s)
        self.lbl_hr.after(200,self.clock)

class Bload_Bank(Tk):
    def __init__(self,*arg):       # Constructors
        Tk.__init__(self,*arg)
        photo = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
        self.iconphoto(False, photo)

        self.title("Plasma Finder".center(420))  # title for Window 
        self.configure(background = "black")  # background color for window 
        self.geometry("1360x768+0+0")
        photo = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
        self.iconphoto(False, photo)

        bg_color ="#FFFFF6"
        
     
        self.bg_icon = ImageTk.PhotoImage(file="Pics\\1 (1).jpg")
        bg_lbl = Label(self, image = self.bg_icon).pack(fill=Y) # we put image into our window
        
        self.hos_icon=ImageTk.PhotoImage(file="Pics\\1 (2) copy.jpg")
                
        
        F1 = LabelFrame(self,bd=10,relief=GROOVE,bg=bg_color)
        F1.place(x=0,relwidth=1,height=100 )

        lbl = Label(F1,text="Plasma Finder", compound=LEFT, image=self.hos_icon,bg=bg_color, font= ("times new roman",20,"bold")).place(x=0, y=5)

        self.lbl_hr = Label(F1,text="12" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_hr.place(x=890, y=40)
        
        self.lbl_COLON = Label(F1,text=":" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_COLON.place(x=915, y=40)
       
       
        self.lbl_min = Label(F1,text="12" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_min.place(x=925, y=40)
       
        self.lbl_COLON = Label(F1,text=":" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_COLON.place(x=950, y=40)
       
        self.lbl_sec = Label(F1,text="12" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_sec.place(x=960, y=40)
        

        self.lbl_abv = Label(F1,text="AM" , font = ("times new roman", 13,"bold"),bg=bg_color)
        self.lbl_abv.place(x=985, y=43)
       
       
        self.font=("times new roman",20,"bold")
        self.calendar = []

        ntpClient = ntplib.NTPClient()
        response = ntpClient.request('pool.ntp.org')
        a=ctime(response.tx_time)
        b=[a[i:i+10] for i in range(0, len(a), 10)]
        c=str(b[0])
        d=str(b[2])

        self.date = Label(F1, font=("times new roman",15,"bold"), text=c, bg=bg_color)
        self.date.place(x=740, y=40)

        self.date1 = Label(F1, font=("times new roman",15,"bold"), text=d,bg=bg_color)
        self.date1.place(x=840, y=40)

        
        self.date2 = Label(F1, font=("times new roman",15,"bold"), text="Calendar",bg=bg_color)
        self.date2.place(x=750, y=5)

        self.calendar.append(DateEntry(F1, font=("times new roman",15,"bold"), locale='en_GB',state="readonly",width=10))
        self.calendar[-1].place(x=855, y=20, anchor="w")

        
        btn_changepass = Button(F1, text="ChangePassword",relief=RAISED,width =15,height=1, font=("times new roman",14,"bold"),bg="red",foreground="white",command=self.change_pasw).place(x=1145,y=20,anchor="w")
        btn_logout = Button(F1, text="Logout",relief=RAISED,width =15,height=1, font=("times new roman",14,"bold"),bg="light green",foreground="black", command=self.logout).place(x=1145,y=60,anchor="w")

        lbl2 = Label(F1,bg=bg_color)
        lbl2.place(x=25,y=10)

        F2 = LabelFrame(self,bd=10,relief=GROOVE,bg=bg_color)
        F2.place(x=0,y=100,width=150,height=670 )

        F21 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F21.place(x=0,y=0,width=130,height=133 )
        
        F22 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F22.place(x=0,y=133,width=130,height=133)
        
        F23 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F23.place(x=0,y=266,width=130,height=133 )
        
        F24 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F24.place(x=0,y=399,width=130,height=133)
        
        F25 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F25.place(x=0,y=532,width=130,height=133)

        self.U_mange = PhotoImage(file="Pics\\User_Det.png")
        self.donor_b = ImageTk.PhotoImage(file="Pics\\Blood Donar.jpg")
        self.b_bank = ImageTk.PhotoImage(file="Pics\Blood Bank Search.jpg")    
        self.p_donar = ImageTk.PhotoImage(file="Pics\Plasma.png")
        self.exit = ImageTk.PhotoImage(file="Pics\\Exit.jpg")
        
        btn_U_det = Button(F21,image= self.U_mange,bg=bg_color,relief=RAISED,width =115,height=120,command=self.U_det).place(x=0,y=60,anchor="w")
        btn_blood_donor = Button(F22,image= self.donor_b,bg=bg_color,relief=RAISED,width =115,height=120,command=self.Blood_Donar ).place(x=0,y=60,anchor="w")
        btn_blood_bank = Button(F23,relief=RAISED,bg=bg_color,image=self.b_bank,width =115,height=120,command=self.Blood_Bank ).place(x=0,y=60,anchor="w")
        btn_Plasma = Button(F24,relief=RAISED,image=self.p_donar,bg=bg_color,width =115,height=120, command=self.Plasma).place(x=0,y=60,anchor="w")
        btn_Exit = Button(F25,relief=RAISED,bg=bg_color,image=self.exit,width =115,height=120, command=self.Exit).place(x=0,y=60,anchor="w")

        F3 = LabelFrame(self,bd=5,relief=FLAT,bg="light gray")
        F3.place(x=150,y=100,relwidth=1,height=30 )
        lbl_1= Label(F3,text="Dashboard / User",font=("comic sans",15,"italic"),bg="light gray")
        lbl_1.place(x=0,y=0)
        home_btn = Button(F3, text="Home",bd=5,relief=GROOVE, font=("",7,"bold"), fg="white", bg="blue", command=self.Home)
        home_btn.place(x=300,y=-2)

        self.F4 =Frame(self,bd=10,relief=SUNKEN,bg="white")
        self.F4.place(x=180,y=200,width=1130,height=500 )
        
        self.searchby = StringVar()
        self.searchby1 = StringVar()

        lb_search=Label(self,text="Search By", font=("times new roman",15,"bold"))
        lb_search.place(x=180 ,y=185, anchor="w")
        combo_search=ttk.Combobox(self, textvariable=self.searchby,width=17, font=("times new roman",16,"bold"),state='readonly')
        combo_search['values']=("HID")
        combo_search.place(x=273, y=185, anchor="w")
        
        search=Entry(self, textvariable=self.searchby1,width=17,bd=5,relief=GROOVE, font=("times new roman",16,"bold"))
        search.place(x=490, y=185, anchor="w")

        lb_search_btn=Button(self,text="Search By", bd=6, relief=GROOVE,command=self.search,font=("times new roman",15,"bold"),fg="yellow",bg="dark blue")
        lb_search_btn.place(x=695 ,y=183, height=30,anchor="w")
        
        lb_search_btn=Button(self,text="Search All", bd=6, relief=GROOVE,command=self.search1,font=("times new roman",15,"bold"),fg="yellow",bg="dark blue")
        lb_search_btn.place(x=835 ,y=183, height=30,anchor="w")
        
        lb_search_btn=Button(self,text="Clear", bd=6, relief=GROOVE,command=self.clear1,font=("times new roman",15,"bold"),fg="yellow",bg="dark blue")
        lb_search_btn.place(x=1110 ,y=183, height=30, width=200,anchor="w")

        Table_Frame=Frame(self.F4,bd=4, relief=RIDGE)
        Table_Frame.place(x=15,y=0,width=1080,height=480)

        scroll_x=Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame, orient=VERTICAL)
        scroll_x1=Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y1=Scrollbar(Table_Frame, orient=VERTICAL)
        self.Bloold_Bank_table=ttk.Treeview(Table_Frame,columns=("HID" ,"A+"  , "B+"  , "AB+", "O+"  , "A-"  , "B-" , "AB-"  , "O-"   ),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Bloold_Bank_table.xview)
        scroll_y.config(command=self.Bloold_Bank_table.yview)

        
        self.Bloold_Bank_table.heading("HID", text="HID")
        self.Bloold_Bank_table.heading("A+", text="A+")
        self.Bloold_Bank_table.heading("B+", text="B+")
        self.Bloold_Bank_table.heading("AB+", text="AB+")
        self.Bloold_Bank_table.heading("O+", text="O+")
        self.Bloold_Bank_table.heading("A-", text="A-")
        self.Bloold_Bank_table.heading("B-", text="B-")
        self.Bloold_Bank_table.heading("AB-", text="AB-")
        self.Bloold_Bank_table.heading("O-", text="O-")
    
    
        self.Bloold_Bank_table['show']='headings'
        self.fetch_data()
        self.clock()
          
    def Home(self):
        self.destroy()
        User_Page().mainloop()

    def U_det(self):
        self.destroy()
        U_Manage().mainloop()
        
    def Blood_Donar(self):
        self.destroy()
        Bload_Search().mainloop()
        
    
    def Blood_Bank(self):
        self.destroy()
        Bload_Bank().mainloop()

    def Plasma(self):
        self.destroy()
        Plasma_Search().mainloop()    
    
    def Exit(self):
        self.destroy()

        
    def search(self):
        
        if self.searchby.get()=="" and self.searchby1.get()=="":
            return messagebox.showwarning("Warning","Fields should be filled")
        if self.searchby.get()=="" :
            return messagebox.showwarning("Warning","Shearch By Option Should be filled")
        if self.searchby1.get()=="":
            return messagebox.showwarning("Warning","Search box should be filled")
        
        else:
            if self.searchby.get()=="HID":
                try:
                    self.Bloold_Bank_table.column("HID", width=150)
                    self.Bloold_Bank_table.column("A+", width=100)
                    self.Bloold_Bank_table.column("B+", width=100)
                    self.Bloold_Bank_table.column("AB+", width=100)
                    self.Bloold_Bank_table.column("O+", width=100)
                    self.Bloold_Bank_table.column("A-", width=100)
                    self.Bloold_Bank_table.column("B-", width=100)
                    self.Bloold_Bank_table.column("AB-", width=100)
                    self.Bloold_Bank_table.column("O-", width=100)


                    self.Bloold_Bank_table['show']='headings'

                    self.Bloold_Bank_table.pack(fill=BOTH,expand=1)
                    self.Bloold_Bank_table.bind("<ButtonRelease-1>",self.getcursor)
                    self.conn=sqlite3.connect("plasma.db")
                    self.c=self.conn.cursor()
                    self.c.execute("select * from Blood_Bank where HID = '"+ self.searchby1.get()+"'")
                    rows=self.c.fetchall()
                    if len(rows)!=0:
                            self.Bloold_Bank_table.delete(*self.Bloold_Bank_table.get_children())
                            for row in rows:
                                    self.Bloold_Bank_table.insert('',END,values=row)
                            self.conn.commit()
                            self.conn.close()
                    else:
                        return messagebox.showerror("Error","HID No Not Exist")        
                except Exception:
                    return messagebox.showerror("Error", "Something Wrong")
                self.conn.close()
            else:
                return messagebox.showerror("Error", "No Such Option")
            
    def search1(self):
        self.Bloold_Bank_table.column("HID", width=150)
        self.Bloold_Bank_table.column("A+", width=100)
        self.Bloold_Bank_table.column("B+", width=100)
        self.Bloold_Bank_table.column("AB+", width=100)
        self.Bloold_Bank_table.column("O+", width=100)
        self.Bloold_Bank_table.column("A-", width=100)
        self.Bloold_Bank_table.column("B-", width=100)
        self.Bloold_Bank_table.column("AB-", width=100)
        self.Bloold_Bank_table.column("O-", width=100)
    
    
        self.Bloold_Bank_table['show']='headings'
    
        self.Bloold_Bank_table.pack(fill=BOTH,expand=1)
        self.Bloold_Bank_table.bind("<ButtonRelease-1>",self.getcursor)
        self.fetch_data()

    def fetch_data(self):
        self.conn=sqlite3.connect("plasma.db")
        self.c=self.conn.cursor()
        self.c.execute("select * from Blood_Bank")
        rows=self.c.fetchall()
        if len(rows)!=0:
                self.Bloold_Bank_table.delete(*self.Bloold_Bank_table.get_children())
                for row in rows:
                        self.Bloold_Bank_table.insert('',END,values=row)
                self.conn.commit()
        self.conn.close()

    def getcursor(self,ev):
        cursor_row=self.Bloold_Bank_table.focus()
        Content=self.Bloold_Bank_table.item(cursor_row)
        row=Content['values']

        self.Bloold_Bank_table.set(row[0])
        self.Bloold_Bank_table.set(row[1])
        self.Bloold_Bank_table.set(row[2])
        self.Bloold_Bank_table.set(row[3])
        self.Bloold_Bank_table.set(row[4])
        self.Bloold_Bank_table.set(row[5])
        self.Bloold_Bank_table.set(row[6])        
        self.Bloold_Bank_table.set(row[7])
        self.Bloold_Bank_table.set(row[8])
        
    def clear1(self):
        self.Bloold_Bank_table.delete(*self.Bloold_Bank_table.get_children())
        self.searchby.set("")
        self.searchby1.set("")

    
    
    def logout(self):
        self.read1=StringVar()
        with open("Temp.txt","r+") as file:
            self.read1=file.read()
            file.truncate()
    
        a=messagebox.askyesnocancel("Hey","Confirm again for Logout")
        if a>0:
            now = datetime.now()
            self.Time2=now.strftime('%H:%M:%S')

            self.today1= now.strftime("%d/%m/%Y")
            self.destroy()
            self.conn=sqlite3.connect("plasma.db")
            self.c=self.conn.cursor()
            y="UPDATE Last_Login_User set last_login_time=\""+str(self.Time2)+"\", last_login_date=\""+str(self.today1)+"\" where UID =\""+str(self.read1)+"\""
            #print(y)
            self.c.execute(y)
            self.conn.commit()
            root=Tk()
            clas=U_login(root)            
        else:
            pass



    def change_pasw(self):  
        self.root2 = Toplevel(self)  # Child Window "Tk() can Also be use here"
        self.root2.title("Change Password")
        self.root2.geometry("750x370+350+150")
        self.root2.configure(bg="black")
        photo1 = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
        self.root2.iconphoto(False, photo1)
        self.root2.grab_set() 
        self.root2.resizable(False, False)

        title_child = Label(self.root2, text="Reset Password", bg="#152238", fg="white",compound=LEFT, font=("Goudy Old Style", 48, "bold"), anchor="w").place(x=0, y=0, relwidth=1)
        
        phone_lbl = Label(self.root2, text="Phone No.", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=120)
        self.phone_ = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.phone_.place(x=260, y=120)
        
        current_lbl = Label(self.root2, text="Current Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=170)
        self.current_ = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.current_.place(x=260, y=170)
        
        pass_lbl = Label(self.root2, text="New Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=220)
        self.pass_ = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.pass_.place(x=260, y=220)
        
        passcon_lbl = Label(self.root2, text="Confirm Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=270)
        self.passcon = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.passcon.place(x=260, y=270)
        
        Reset_btn = Button(self.root2, text="Reset", font=("times new roman", 18, "bold"), activebackground="blue",activeforeground="white", bg="blue", fg="white", cursor="hand2", command=self.reset)
        Reset_btn.place(x=495, y=310, width=140, height=30) 

      
        
    def reset(self):
        with open("Temp.txt","r+") as file:
            self.read1=file.read()
        #print(self.read1)
        self.passw = self.pass_.get()
        self.passconw = self.passcon.get()
        self.current2_=self.current_.get()
        self.phone_2=self.phone_.get()
        
        self.conn = sqlite3.connect("plasma.db")
        self.c = self.conn.cursor()
        self.c.execute("SELECT Password from user WHERE Phone_No=" +self.phone_2)
        self.data = self.c.fetchall()
        if self.data==[]:
            return messagebox.showerror("Error"," Current Password not Matched to Your mail Id" , parent=self.root2)
        else:
            for i in self.data:
                    #print(i[0])
                    self.c.execute("SELECT Email from user WHERE Phone_No=" +self.phone_2)
                    self.data = self.c.fetchall()
                    for j in self.data:
                        a=str(j[0])
                    if i[0] == self.current2_:
                        self.OTP_Forget=str(random.randint(100000,999999))
                        send = smtplib.SMTP("smtp.gmail.com", 587)  # Create session for Gmail
                        send.starttls()  # transport layer

                        msg = EmailMessage()
                        msg["Subject"] = "OTP"
                        msg["From"] = "aj147ps@gmail.com"
                        msg["To"] = a
                        msg.set_content("Hi! your OTP for reset password: "+"\'"+str(self.OTP_Forget)+"\'")        
                            
                        try:
                            send.login("aj147ps@gmail.com","xcavbfayvnthixwy")
                        except smtplib.SMTPAuthenticationError:
                            messagebox.showerror("Error","Error Occur Otp Not")    

                        try:
                            try:
                                try:                                
                                    
                                    send.send_message(msg)
                                    messagebox.showinfo("Mailed","OTP Sent to Your Mail Id") 
                                    self.root2.destroy()
                                    self.root3 = Toplevel(self)  # Child Window "Tk() can Also be use here"
                                    self.root3.title("Verification")
                                    self.root3.geometry("750x320+350+150")
                                    self.root3.configure(bg="black")
                                    photo4 = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
                                    self.root3.iconphoto(False, photo4)
                                    self.root3.grab_set() 
                                    self.root3.resizable(False, False)
                                
                                    title_child = Label(self.root3, text="Reset Password", bg="#152238", fg="white",compound=LEFT, font=("Goudy Old Style", 48, "bold"), anchor="w").place(x=0, y=0, relwidth=1)
                                    otp_lbl = Label(self.root3, text="Enter OTP", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=120)
                                    self.otp_ = Entry(self.root3, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
                                    self.otp_.place(x=260, y=120)
                                    
                                    Reset_btn = Button(self.root3, text="Reset", font=("times new roman", 18, "bold"), activebackground="blue",activeforeground="white", bg="blue", fg="white", cursor="hand2", command=self.reset1)
                                    Reset_btn.place(x=495, y=260, width=140, height=30) 
                        
                                except smtplib.SMTPRecipientsRefused:
                                    messagebox.showerror("Mailed","Mail Not Sent")
                            except smtplib.SMTPException:
                                messagebox.showerror("Mailed","Mail Not Sent")
                        except smtplib.SMTPConnectError:
                            messagebox.showerror("Error","Connection Error")
                    else:
                        return messagebox.showerror("Error","Contact No. have not given Mail Id")

    def reset1(self):
        self.one_ = self.otp_.get()
        #print(self.one_)
        if str(self.one_)==str(self.OTP_Forget):
            if len(str(self.passw))>=8:
                if self.passw == self.passconw:
                    y= f"UPDATE user SET Password = {str(self.passw)} WHERE Phone_No = {str(self.phone_2)}"
                    self.c.execute(str(y))
                    self.conn.commit()
                    self.conn.close()
                    self.OTP_Forget=""
                    messagebox.showinfo("Info", "Successfully Changed!!", parent=self.root3)
                    self.root3.destroy()                    
                else:
                    return messagebox.showerror("Error", "Password Cann't Changed  password  and confirm password not match!!", parent=self.root3)
            else:
                return messagebox.showerror("Error", "Password should be of minimum 8 Characters", parent=self.root3)
        else:
            return messagebox.showerror("Error", "OTP Entered is Wrong", parent=self.root3)

    def clock(self):

        self.h = str(time.strftime("%H"))
        self.m = str(time.strftime("%M"))
        self.s = str(time.strftime("%S"))

        if int(self.h)<15 and int(self.m)>0:
            self.lbl_abv.config(text="PM")

        if int(self.h)>=15 and int(self.h)<20 and int(self.m)>0:
            self.lbl_abv.config(text="PM")
        
        if int(self.h)>=20 and int(self.h)<24 and int(self.m)>0:
            self.lbl_abv.config(text="PM")

        if int(self.h)>12 and int(self.h)<15 and int(self.m)>0:
            self.lbl_abv.config(text="PM")

        if int(self.h)>0 and int(self.h)<12 and int(self.m)>0:
            self.lbl_abv.config(text="AM")

         
        self.lbl_hr.config(text = self.h)
        self.lbl_min.config(text = self.m)
        self.lbl_sec.config(text = self.s)
        self.lbl_hr.after(200,self.clock)

class Bload_Search(Tk):
    def __init__(self,*arg):       # Constructors
        Tk.__init__(self,*arg)
        photo = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
        self.iconphoto(False, photo)

        self.title("Plasma Finder".center(420))  # title for Window 
        self.configure(background = "black")  # background color for window 
        self.geometry("1360x768+0+0")
        photo = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
        self.iconphoto(False, photo)

        bg_color ="#FFFFF6"
        
     
        self.bg_icon = ImageTk.PhotoImage(file="Pics\\1 (1).jpg")
        bg_lbl = Label(self, image = self.bg_icon).pack(fill=Y) # we put image into our window
        
        self.hos_icon=ImageTk.PhotoImage(file="Pics\\1 (2) copy.jpg")
                
        
        F1 = LabelFrame(self,bd=10,relief=GROOVE,bg=bg_color)
        F1.place(x=0,relwidth=1,height=100 )

        lbl = Label(F1,text="Plasma Finder", compound=LEFT, image=self.hos_icon,bg=bg_color, font= ("times new roman",20,"bold")).place(x=0, y=5)

        self.lbl_hr = Label(F1,text="12" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_hr.place(x=890, y=40)
        
        self.lbl_COLON = Label(F1,text=":" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_COLON.place(x=915, y=40)
       
       
        self.lbl_min = Label(F1,text="12" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_min.place(x=925, y=40)
       
        self.lbl_COLON = Label(F1,text=":" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_COLON.place(x=950, y=40)
       
        self.lbl_sec = Label(F1,text="12" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_sec.place(x=960, y=40)
        

        self.lbl_abv = Label(F1,text="AM" , font = ("times new roman", 13,"bold"),bg=bg_color)
        self.lbl_abv.place(x=985, y=43)
       
       
        self.font=("times new roman",20,"bold")
        self.calendar = []

        ntpClient = ntplib.NTPClient()
        response = ntpClient.request('pool.ntp.org')
        a=ctime(response.tx_time)
        b=[a[i:i+10] for i in range(0, len(a), 10)]
        c=str(b[0])
        d=str(b[2])

        self.date = Label(F1, font=("times new roman",15,"bold"), text=c, bg=bg_color)
        self.date.place(x=740, y=40)

        self.date1 = Label(F1, font=("times new roman",15,"bold"), text=d,bg=bg_color)
        self.date1.place(x=840, y=40)

        
        self.date2 = Label(F1, font=("times new roman",15,"bold"), text="Calendar",bg=bg_color)
        self.date2.place(x=750, y=5)

        self.calendar.append(DateEntry(F1, font=("times new roman",15,"bold"), locale='en_GB',state="readonly",width=10))
        self.calendar[-1].place(x=855, y=20, anchor="w")

        
        btn_changepass = Button(F1, text="ChangePassword",relief=RAISED,width =15,height=1, font=("times new roman",14,"bold"),bg="red",foreground="white",command=self.change_pasw).place(x=1145,y=20,anchor="w")
        btn_logout = Button(F1, text="Logout",relief=RAISED,width =15,height=1, font=("times new roman",14,"bold"),bg="light green",foreground="black", command=self.logout).place(x=1145,y=60,anchor="w")

        lbl2 = Label(F1,bg=bg_color)
        lbl2.place(x=25,y=10)

        F2 = LabelFrame(self,bd=10,relief=GROOVE,bg=bg_color)
        F2.place(x=0,y=100,width=150,height=670 )

        F21 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F21.place(x=0,y=0,width=130,height=133 )
        
        F22 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F22.place(x=0,y=133,width=130,height=133)
        
        F23 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F23.place(x=0,y=266,width=130,height=133 )
        
        F24 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F24.place(x=0,y=399,width=130,height=133)
        
        F25 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F25.place(x=0,y=532,width=130,height=133)

        self.U_mange = PhotoImage(file="Pics\\User_Det.png")
        self.donor_b = ImageTk.PhotoImage(file="Pics\\Blood Donar.jpg")
        self.b_bank = ImageTk.PhotoImage(file="Pics\Blood Bank Search.jpg")    
        self.p_donar = ImageTk.PhotoImage(file="Pics\Plasma.png")
        self.exit = ImageTk.PhotoImage(file="Pics\\Exit.jpg")
        
        btn_U_det = Button(F21,image= self.U_mange,bg=bg_color,relief=RAISED,width =115,height=120,command=self.U_det).place(x=0,y=60,anchor="w")
        btn_blood_donor = Button(F22,image= self.donor_b,bg=bg_color,relief=RAISED,width =115,height=120,command=self.Blood_Donar ).place(x=0,y=60,anchor="w")
        btn_blood_bank = Button(F23,relief=RAISED,bg=bg_color,image=self.b_bank,width =115,height=120,command=self.Blood_Bank ).place(x=0,y=60,anchor="w")
        btn_Plasma = Button(F24,relief=RAISED,image=self.p_donar,bg=bg_color,width =115,height=120, command=self.Plasma).place(x=0,y=60,anchor="w")
        btn_Exit = Button(F25,relief=RAISED,bg=bg_color,image=self.exit,width =115,height=120, command=self.Exit).place(x=0,y=60,anchor="w")

        F3 = LabelFrame(self,bd=5,relief=FLAT,bg="light gray")
        F3.place(x=150,y=100,relwidth=1,height=30 )
        lbl_1= Label(F3,text="Dashboard / User",font=("comic sans",15,"italic"),bg="light gray")
        lbl_1.place(x=0,y=0)
        home_btn = Button(F3, text="Home",bd=5,relief=GROOVE, font=("",7,"bold"), fg="white", bg="blue", command=self.Home)
        home_btn.place(x=300,y=-2)

        self.F4 =Frame(self,bd=10,relief=SUNKEN,bg="white")
        self.F4.place(x=180,y=200,width=1130,height=500 )
        
        self.searchby = StringVar()
        self.searchby1 = StringVar()

        lb_search=Label(self,text="Search By", font=("times new roman",15,"bold"))
        lb_search.place(x=180 ,y=185, anchor="w")
        combo_search=ttk.Combobox(self, textvariable=self.searchby,width=17, font=("times new roman",16,"bold"),state='readonly')
        combo_search['values']=("UID","B_Group")
        combo_search.place(x=273, y=185, anchor="w")
        
        search=Entry(self, textvariable=self.searchby1,width=17,bd=5,relief=GROOVE, font=("times new roman",16,"bold"))
        search.place(x=490, y=185, anchor="w")

        lb_search_btn=Button(self,text="Search By", bd=6, relief=GROOVE,command=self.search,font=("times new roman",15,"bold"),fg="yellow",bg="dark blue")
        lb_search_btn.place(x=695 ,y=183, height=30,anchor="w")
        
        lb_search_btn=Button(self,text="Search All", bd=6, relief=GROOVE,command=self.search1,font=("times new roman",15,"bold"),fg="yellow",bg="dark blue")
        lb_search_btn.place(x=835 ,y=183, height=30,anchor="w")
        
        lb_search_btn=Button(self,text="Clear", bd=6, relief=GROOVE,command=self.clear1,font=("times new roman",15,"bold"),fg="yellow",bg="dark blue")
        lb_search_btn.place(x=1110 ,y=183, height=30, width=200,anchor="w")

        Table_Frame=Frame(self.F4,bd=4, relief=RIDGE)
        Table_Frame.place(x=15,y=0,width=1080,height=480)

        scroll_x=Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame, orient=VERTICAL)
        scroll_x1=Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y1=Scrollbar(Table_Frame, orient=VERTICAL)
        self.Bloold_Bank_table=ttk.Treeview(Table_Frame,columns=("UID" , "B_Group"  , "Phone_No"   ),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Bloold_Bank_table.xview)
        scroll_y.config(command=self.Bloold_Bank_table.yview)

        
        self.Bloold_Bank_table.heading("UID", text="UID")
        self.Bloold_Bank_table.heading("B_Group", text="B_Group")
        self.Bloold_Bank_table.heading("Phone_No", text="Phone_No")

        self.Bloold_Bank_table.column("UID", width=150)
        self.Bloold_Bank_table.column("B_Group", width=150)
        self.Bloold_Bank_table.column("Phone_No", width=150)
        
    
        self.Bloold_Bank_table['show']='headings'
        
        self.fetch_data()
        self.clock()

          
    def Home(self):
        self.destroy()
        User_Page().mainloop()

    def U_det(self):
        self.destroy()
        U_Manage().mainloop()
        
    def Blood_Donar(self):
        self.destroy()
        Bload_Search().mainloop()
        
    
    def Blood_Bank(self):
        self.destroy()
        Bload_Bank().mainloop()

    def Plasma(self):
        self.destroy()
        Plasma_Search().mainloop()    
    
    def Exit(self):
        self.destroy()

        
    def search(self):
        
        if self.searchby.get()=="" and self.searchby1.get()=="":
            return messagebox.showwarning("Warning","Fields should be filled")
        if self.searchby.get()=="" :
            return messagebox.showwarning("Warning","Shearch By Option Should be filled")
        if self.searchby1.get()=="":
            return messagebox.showwarning("Warning","Search box should be filled")
        
        else:
            
            if self.searchby.get()=="UID":        
                try:
                    self.Bloold_Bank_table.column("UID", width=150)
                    self.Bloold_Bank_table.column("B_Group", width=150)
                    self.Bloold_Bank_table.column("Phone_No", width=150)
                    
                
                    self.Bloold_Bank_table['show']='headings'
                
                    self.Bloold_Bank_table.pack(fill=BOTH,expand=1)
                    self.Bloold_Bank_table.bind("<ButtonRelease-1>",self.getcursor)
                    self.fetch_data()

                    self.conn=sqlite3.connect("plasma.db")
                    self.c=self.conn.cursor()
                    self.c.execute("select * from Blood_Donor_Approved where UID = '"+ self.searchby1.get()+"'")
                    rows=self.c.fetchall()
                    if len(rows)!=0:
                            self.Bloold_Bank_table.delete(*self.Bloold_Bank_table.get_children())
                            for row in rows:
                                    self.Bloold_Bank_table.insert('',END,values=row)
                            self.conn.commit()
                            self.conn.close()
                    else:
                        return messagebox.showerror("Error","UID No Not Exist")        
                except Exception:
                    return messagebox.showerror("Error", "Something Wrong")
                self.conn.close()
            
            elif self.searchby.get()=="B_Group":
                try:
                    self.Bloold_Bank_table.column("B_Group", width=150)
                    self.Bloold_Bank_table.column("Phone_No", width=150)
                    
                
                    self.Bloold_Bank_table['show']='headings'
                
                    self.Bloold_Bank_table.pack(fill=BOTH,expand=1)
                    self.Bloold_Bank_table.bind("<ButtonRelease-1>",self.getcursor)
                    self.fetch_data()

                    self.conn=sqlite3.connect("plasma.db")
                    self.c=self.conn.cursor()
                    self.c.execute("select * from Blood_Donor_Approved where B_group = '"+ self.searchby1.get()+"'")
                    rows=self.c.fetchall()
                    if len(rows)!=0:
                            self.Bloold_Bank_table.delete(*self.Bloold_Bank_table.get_children())
                            for row in rows:
                                    self.Bloold_Bank_table.insert('',END,values=row)
                            self.conn.commit()
                            self.conn.close()
                    else:
                        return messagebox.showerror("Error","Bloood Group Not Available ")        
                except Exception:
                    return messagebox.showerror("Error", "Something Wrong")
                self.conn.close()

            else:
                return messagebox.showerror("Error", "No Such Option")
            
            
    def search1(self):
        self.Bloold_Bank_table.column("UID", width=150)
        self.Bloold_Bank_table.column("B_Group", width=150)
        self.Bloold_Bank_table.column("Phone_No", width=150)
        
    
        self.Bloold_Bank_table['show']='headings'
    
        self.Bloold_Bank_table.pack(fill=BOTH,expand=1)
        self.Bloold_Bank_table.bind("<ButtonRelease-1>",self.getcursor)
        self.fetch_data()

    def fetch_data(self):
        self.conn=sqlite3.connect("plasma.db")
        self.c=self.conn.cursor()
        self.c.execute("select * from Blood_Donor_Approved")
        rows=self.c.fetchall()
        if len(rows)!=0:
                self.Bloold_Bank_table.delete(*self.Bloold_Bank_table.get_children())
                for row in rows:
                        self.Bloold_Bank_table.insert('',END,values=row)
                self.conn.commit()
        self.conn.close()

    def getcursor(self,ev):
        cursor_row=self.Bloold_Bank_table.focus()
        Content=self.Bloold_Bank_table.item(cursor_row)
        row=Content['values']

        self.Bloold_Bank_table.set(row[0])
        self.Bloold_Bank_table.set(row[1])
        self.Bloold_Bank_table.set(row[2])
        
    def clear1(self):
        self.Bloold_Bank_table.delete(*self.Bloold_Bank_table.get_children())
        self.searchby.set("")
        self.searchby1.set("")

    
    
    def logout(self):
        self.read1=StringVar()
        with open("Temp.txt","r+") as file:
            self.read1=file.read()
            file.truncate()
    
        a=messagebox.askyesnocancel("Hey","Confirm again for Logout")
        if a>0:
            now = datetime.now()
            self.Time2=now.strftime('%H:%M:%S')

            self.today1= now.strftime("%d/%m/%Y")
            self.destroy()
            self.conn=sqlite3.connect("plasma.db")
            self.c=self.conn.cursor()
            y="UPDATE Last_Login_User set last_login_time=\""+str(self.Time2)+"\", last_login_date=\""+str(self.today1)+"\" where UID =\""+str(self.read1)+"\""
            #print(y)
            self.c.execute(y)
            self.conn.commit()
            root=Tk()
            clas=U_login(root)            
        else:
            pass



    def change_pasw(self):  
        self.root2 = Toplevel(self)  # Child Window "Tk() can Also be use here"
        self.root2.title("Change Password")
        self.root2.geometry("750x370+350+150")
        self.root2.configure(bg="black")
        photo1 = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
        self.root2.iconphoto(False, photo1)
        self.root2.grab_set() 
        self.root2.resizable(False, False)

        title_child = Label(self.root2, text="Reset Password", bg="#152238", fg="white",compound=LEFT, font=("Goudy Old Style", 48, "bold"), anchor="w").place(x=0, y=0, relwidth=1)
        
        phone_lbl = Label(self.root2, text="Phone No.", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=120)
        self.phone_ = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.phone_.place(x=260, y=120)
        
        current_lbl = Label(self.root2, text="Current Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=170)
        self.current_ = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.current_.place(x=260, y=170)
        
        pass_lbl = Label(self.root2, text="New Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=220)
        self.pass_ = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.pass_.place(x=260, y=220)
        
        passcon_lbl = Label(self.root2, text="Confirm Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=270)
        self.passcon = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.passcon.place(x=260, y=270)
        
        Reset_btn = Button(self.root2, text="Reset", font=("times new roman", 18, "bold"), activebackground="blue",activeforeground="white", bg="blue", fg="white", cursor="hand2", command=self.reset)
        Reset_btn.place(x=495, y=310, width=140, height=30) 

      
        
    def reset(self):
        with open("Temp.txt","r+") as file:
            self.read1=file.read()
        #print(self.read1)
        self.passw = self.pass_.get()
        self.passconw = self.passcon.get()
        self.current2_=self.current_.get()
        self.phone_2=self.phone_.get()
        
        self.conn = sqlite3.connect("plasma.db")
        self.c = self.conn.cursor()
        self.c.execute("SELECT Password from user WHERE Phone_No=" +self.phone_2)
        self.data = self.c.fetchall()
        if self.data==[]:
            return messagebox.showerror("Error"," Current Password not Matched to Your mail Id" , parent=self.root2)
        else:
            for i in self.data:
                    #print(i[0])
                    self.c.execute("SELECT Email from user WHERE Phone_No=" +self.phone_2)
                    self.data = self.c.fetchall()
                    for j in self.data:
                        a=str(j[0])
                    if i[0] == self.current2_:
                        self.OTP_Forget=str(random.randint(100000,999999))
                        send = smtplib.SMTP("smtp.gmail.com", 587)  # Create session for Gmail
                        send.starttls()  # transport layer

                        msg = EmailMessage()
                        msg["Subject"] = "OTP"
                        msg["From"] = "aj147ps@gmail.com"
                        msg["To"] = a
                        msg.set_content("Hi! your OTP for reset password: "+"\'"+str(self.OTP_Forget)+"\'")        
                            
                        try:
                            send.login("aj147ps@gmail.com","xcavbfayvnthixwy")
                        except smtplib.SMTPAuthenticationError:
                            messagebox.showerror("Error","Error Occur Otp Not")    

                        try:
                            try:
                                try:                                
                                    
                                    send.send_message(msg)
                                    messagebox.showinfo("Mailed","OTP Sent to Your Mail Id") 
                                    self.root2.destroy()
                                    self.root3 = Toplevel(self)  # Child Window "Tk() can Also be use here"
                                    self.root3.title("Verification")
                                    self.root3.geometry("750x320+350+150")
                                    self.root3.configure(bg="black")
                                    photo4 = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
                                    self.root3.iconphoto(False, photo4)
                                    self.root3.grab_set() 
                                    self.root3.resizable(False, False)
                                
                                    title_child = Label(self.root3, text="Reset Password", bg="#152238", fg="white",compound=LEFT, font=("Goudy Old Style", 48, "bold"), anchor="w").place(x=0, y=0, relwidth=1)
                                    otp_lbl = Label(self.root3, text="Enter OTP", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=120)
                                    self.otp_ = Entry(self.root3, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
                                    self.otp_.place(x=260, y=120)
                                    
                                    Reset_btn = Button(self.root3, text="Reset", font=("times new roman", 18, "bold"), activebackground="blue",activeforeground="white", bg="blue", fg="white", cursor="hand2", command=self.reset1)
                                    Reset_btn.place(x=495, y=260, width=140, height=30) 
                        
                                except smtplib.SMTPRecipientsRefused:
                                    messagebox.showerror("Mailed","Mail Not Sent")
                            except smtplib.SMTPException:
                                messagebox.showerror("Mailed","Mail Not Sent")
                        except smtplib.SMTPConnectError:
                            messagebox.showerror("Error","Connection Error")
                    else:
                        return messagebox.showerror("Error","Contact No. have not given Mail Id")

    def reset1(self):
        self.one_ = self.otp_.get()
        #print(self.one_)
        if str(self.one_)==str(self.OTP_Forget):
            if len(str(self.passw))>=8:
                if self.passw == self.passconw:
                    y= f"UPDATE user SET Password = {str(self.passw)} WHERE Phone_No = {str(self.phone_2)}"
                    self.c.execute(str(y))
                    self.conn.commit()
                    self.conn.close()
                    self.OTP_Forget=""
                    messagebox.showinfo("Info", "Successfully Changed!!", parent=self.root3)
                    self.root3.destroy()                    
                else:
                    return messagebox.showerror("Error", "Password Cann't Changed  password  and confirm password not match!!", parent=self.root3)
            else:
                return messagebox.showerror("Error", "Password should be of minimum 8 Characters", parent=self.root3)
        else:
            return messagebox.showerror("Error", "OTP Entered is Wrong", parent=self.root3)

    def clock(self):

        self.h = str(time.strftime("%H"))
        self.m = str(time.strftime("%M"))
        self.s = str(time.strftime("%S"))

        if int(self.h)<15 and int(self.m)>0:
            self.lbl_abv.config(text="PM")

        if int(self.h)>=15 and int(self.h)<20 and int(self.m)>0:
            self.lbl_abv.config(text="PM")
        
        if int(self.h)>=20 and int(self.h)<24 and int(self.m)>0:
            self.lbl_abv.config(text="PM")

        if int(self.h)>12 and int(self.h)<15 and int(self.m)>0:
            self.lbl_abv.config(text="PM")

        if int(self.h)>0 and int(self.h)<12 and int(self.m)>0:
            self.lbl_abv.config(text="AM")

         
        self.lbl_hr.config(text = self.h)
        self.lbl_min.config(text = self.m)
        self.lbl_sec.config(text = self.s)
        self.lbl_hr.after(200,self.clock)

class Plasma_Search(Tk):
    def __init__(self,*arg):       # Constructors
        Tk.__init__(self,*arg)
        photo = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
        self.iconphoto(False, photo)

        self.title("Plasma Finder".center(420))  # title for Window 
        self.configure(background = "black")  # background color for window 
        self.geometry("1360x768+0+0")
        photo = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
        self.iconphoto(False, photo)

        bg_color ="#FFFFF6"
        
     
        self.bg_icon = ImageTk.PhotoImage(file="Pics\\1 (1).jpg")
        bg_lbl = Label(self, image = self.bg_icon).pack(fill=Y) # we put image into our window
        
        self.hos_icon=ImageTk.PhotoImage(file="Pics\\1 (2) copy.jpg")
                
        
        F1 = LabelFrame(self,bd=10,relief=GROOVE,bg=bg_color)
        F1.place(x=0,relwidth=1,height=100 )

        lbl = Label(F1,text="Plasma Finder", compound=LEFT, image=self.hos_icon,bg=bg_color, font= ("times new roman",20,"bold")).place(x=0, y=5)

        self.lbl_hr = Label(F1,text="12" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_hr.place(x=890, y=40)
        
        self.lbl_COLON = Label(F1,text=":" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_COLON.place(x=915, y=40)
       
       
        self.lbl_min = Label(F1,text="12" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_min.place(x=925, y=40)
       
        self.lbl_COLON = Label(F1,text=":" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_COLON.place(x=950, y=40)
       
        self.lbl_sec = Label(F1,text="12" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_sec.place(x=960, y=40)
        

        self.lbl_abv = Label(F1,text="AM" , font = ("times new roman", 13,"bold"),bg=bg_color)
        self.lbl_abv.place(x=985, y=43)
       
       
        self.font=("times new roman",20,"bold")
        self.calendar = []

        ntpClient = ntplib.NTPClient()
        response = ntpClient.request('pool.ntp.org')
        a=ctime(response.tx_time)
        b=[a[i:i+10] for i in range(0, len(a), 10)]
        c=str(b[0])
        d=str(b[2])

        self.date = Label(F1, font=("times new roman",15,"bold"), text=c, bg=bg_color)
        self.date.place(x=740, y=40)

        self.date1 = Label(F1, font=("times new roman",15,"bold"), text=d,bg=bg_color)
        self.date1.place(x=840, y=40)

        
        self.date2 = Label(F1, font=("times new roman",15,"bold"), text="Calendar",bg=bg_color)
        self.date2.place(x=750, y=5)

        self.calendar.append(DateEntry(F1, font=("times new roman",15,"bold"), locale='en_GB',state="readonly",width=10))
        self.calendar[-1].place(x=855, y=20, anchor="w")

        
        btn_changepass = Button(F1, text="ChangePassword",relief=RAISED,width =15,height=1, font=("times new roman",14,"bold"),bg="red",foreground="white",command=self.change_pasw).place(x=1145,y=20,anchor="w")
        btn_logout = Button(F1, text="Logout",relief=RAISED,width =15,height=1, font=("times new roman",14,"bold"),bg="light green",foreground="black", command=self.logout).place(x=1145,y=60,anchor="w")

        lbl2 = Label(F1,bg=bg_color)
        lbl2.place(x=25,y=10)

        F2 = LabelFrame(self,bd=10,relief=GROOVE,bg=bg_color)
        F2.place(x=0,y=100,width=150,height=670 )

        F21 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F21.place(x=0,y=0,width=130,height=133 )
        
        F22 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F22.place(x=0,y=133,width=130,height=133)
        
        F23 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F23.place(x=0,y=266,width=130,height=133 )
        
        F24 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F24.place(x=0,y=399,width=130,height=133)
        
        F25 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F25.place(x=0,y=532,width=130,height=133)

        self.U_mange = PhotoImage(file="Pics\\User_Det.png")
        self.donor_b = ImageTk.PhotoImage(file="Pics\\Blood Donar.jpg")
        self.b_bank = ImageTk.PhotoImage(file="Pics\Blood Bank Search.jpg")    
        self.p_donar = ImageTk.PhotoImage(file="Pics\Plasma.png")
        self.exit = ImageTk.PhotoImage(file="Pics\\Exit.jpg")
        
        btn_U_det = Button(F21,image= self.U_mange,bg=bg_color,relief=RAISED,width =115,height=120,command=self.U_det).place(x=0,y=60,anchor="w")
        btn_blood_donor = Button(F22,image= self.donor_b,bg=bg_color,relief=RAISED,width =115,height=120,command=self.Blood_Donar ).place(x=0,y=60,anchor="w")
        btn_blood_bank = Button(F23,relief=RAISED,bg=bg_color,image=self.b_bank,width =115,height=120,command=self.Blood_Bank ).place(x=0,y=60,anchor="w")
        btn_Plasma = Button(F24,relief=RAISED,image=self.p_donar,bg=bg_color,width =115,height=120, command=self.Plasma).place(x=0,y=60,anchor="w")
        btn_Exit = Button(F25,relief=RAISED,bg=bg_color,image=self.exit,width =115,height=120, command=self.Exit).place(x=0,y=60,anchor="w")

        F3 = LabelFrame(self,bd=5,relief=FLAT,bg="light gray")
        F3.place(x=150,y=100,relwidth=1,height=30 )
        lbl_1= Label(F3,text="Dashboard / User",font=("comic sans",15,"italic"),bg="light gray")
        lbl_1.place(x=0,y=0)
        home_btn = Button(F3, text="Home",bd=5,relief=GROOVE, font=("",7,"bold"), fg="white", bg="blue", command=self.Home)
        home_btn.place(x=300,y=-2)

        self.F4 =Frame(self,bd=10,relief=SUNKEN,bg="white")
        self.F4.place(x=180,y=200,width=1130,height=500 )
        
        self.searchby = StringVar()
        self.searchby1 = StringVar()

        lb_search=Label(self,text="Search By", font=("times new roman",15,"bold"))
        lb_search.place(x=180 ,y=185, anchor="w")
        combo_search=ttk.Combobox(self, textvariable=self.searchby,width=17, font=("times new roman",16,"bold"),state='readonly')
        combo_search['values']=("UID","B_Group")
        combo_search.place(x=273, y=185, anchor="w")
        
        search=Entry(self, textvariable=self.searchby1,width=17,bd=5,relief=GROOVE, font=("times new roman",16,"bold"))
        search.place(x=490, y=185, anchor="w")

        lb_search_btn=Button(self,text="Search By", bd=6, relief=GROOVE,command=self.search,font=("times new roman",15,"bold"),fg="yellow",bg="dark blue")
        lb_search_btn.place(x=695 ,y=183, height=30,anchor="w")
        
        lb_search_btn=Button(self,text="Search All", bd=6, relief=GROOVE,command=self.search1,font=("times new roman",15,"bold"),fg="yellow",bg="dark blue")
        lb_search_btn.place(x=835 ,y=183, height=30,anchor="w")
        
        lb_search_btn=Button(self,text="Clear", bd=6, relief=GROOVE,command=self.clear1,font=("times new roman",15,"bold"),fg="yellow",bg="dark blue")
        lb_search_btn.place(x=1110 ,y=183, height=30, width=200,anchor="w")

        Table_Frame=Frame(self.F4,bd=4, relief=RIDGE)
        Table_Frame.place(x=15,y=0,width=1080,height=480)

        scroll_x=Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame, orient=VERTICAL)
        scroll_x1=Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y1=Scrollbar(Table_Frame, orient=VERTICAL)
        self.Bloold_Bank_table=ttk.Treeview(Table_Frame,columns=("UID" , "Blood_Group"  , "Phone_No"   ),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Bloold_Bank_table.xview)
        scroll_y.config(command=self.Bloold_Bank_table.yview)

        
        self.Bloold_Bank_table.heading("UID", text="UID")
        self.Bloold_Bank_table.heading("Blood_Group", text="Blood_Group")
        self.Bloold_Bank_table.heading("Phone_No", text="Phone_No")

        self.Bloold_Bank_table.column("UID", width=150)
        self.Bloold_Bank_table.column("Blood_Group", width=150)
        self.Bloold_Bank_table.column("Phone_No", width=150)
        
    
        self.Bloold_Bank_table['show']='headings'
        
        self.fetch_data()
        self.clock()
          
    def Home(self):
        self.destroy()
        User_Page().mainloop()

    def U_det(self):
        self.destroy()
        U_Manage().mainloop()
        
    def Blood_Donar(self):
        self.destroy()
        Bload_Search().mainloop()
        
    
    def Blood_Bank(self):
        self.destroy()
        Bload_Bank().mainloop()

    def Plasma(self):
        self.destroy()
        Plasma_Search().mainloop()    
    
    def Exit(self):
        self.destroy()

        
    def search(self):
        
        if self.searchby.get()=="" and self.searchby1.get()=="":
            return messagebox.showwarning("Warning","Fields should be filled")
        if self.searchby.get()=="" :
            return messagebox.showwarning("Warning","Shearch By Option Should be filled")
        if self.searchby1.get()=="":
            return messagebox.showwarning("Warning","Search box should be filled")
        
        else:
            
            if self.searchby.get()=="UID":        
                try:
                    self.Bloold_Bank_table.column("UID", width=150)
                    self.Bloold_Bank_table.column("Blood_Group", width=150)
                    self.Bloold_Bank_table.column("Phone_No", width=150)
                    
                
                    self.Bloold_Bank_table['show']='headings'
                
                    self.Bloold_Bank_table.pack(fill=BOTH,expand=1)
                    self.Bloold_Bank_table.bind("<ButtonRelease-1>",self.getcursor)
                    self.fetch_data()

                    self.conn=sqlite3.connect("plasma.db")
                    self.c=self.conn.cursor()
                    self.c.execute("select * from Plasma_Donar where UID = '"+ self.searchby1.get()+"'")
                    rows=self.c.fetchall()
                    if len(rows)!=0:
                            self.Bloold_Bank_table.delete(*self.Bloold_Bank_table.get_children())
                            for row in rows:
                                    self.Bloold_Bank_table.insert('',END,values=row)
                            self.conn.commit()
                            self.conn.close()
                    else:
                        return messagebox.showerror("Error","UID No Not Exist")        
                except Exception:
                    return messagebox.showerror("Error", "Something Wrong")
                self.conn.close()
            
            elif self.searchby.get()=="B_Group":
                try:
                    self.Bloold_Bank_table.column("UID", width=150)
                    self.Bloold_Bank_table.column("Blood_Group", width=150)
                    self.Bloold_Bank_table.column("Phone_No", width=150)
                    
                
                    self.Bloold_Bank_table['show']='headings'
                
                    self.Bloold_Bank_table.pack(fill=BOTH,expand=1)
                    self.Bloold_Bank_table.bind("<ButtonRelease-1>",self.getcursor)
                    self.fetch_data()

                    self.conn=sqlite3.connect("plasma.db")
                    self.c=self.conn.cursor()
                    self.c.execute("select * from Plasma_Donar WHERE Blood_Group = '"+ self.searchby1.get()+"'")
                    rows=self.c.fetchall()
                    if len(rows)!=0:
                            self.Bloold_Bank_table.delete(*self.Bloold_Bank_table.get_children())
                            for row in rows:
                                    self.Bloold_Bank_table.insert('',END,values=row)
                            self.conn.commit()
                            self.conn.close()
                    else:
                        return messagebox.showerror("Error","Bloood Group Not Available ")        
                except Exception:
                    return messagebox.showerror("Error", "Something Wrong")
                self.conn.close()

            else:
                return messagebox.showerror("Error", "No Such Option")
            
            
    def search1(self):
        self.Bloold_Bank_table.column("UID", width=150)
        self.Bloold_Bank_table.column("Blood_Group", width=150)
        self.Bloold_Bank_table.column("Phone_No", width=150)
        
    
        self.Bloold_Bank_table['show']='headings'
    
        self.Bloold_Bank_table.pack(fill=BOTH,expand=1)
        self.Bloold_Bank_table.bind("<ButtonRelease-1>",self.getcursor)
        self.fetch_data()


    def fetch_data(self):
        self.conn=sqlite3.connect("plasma.db")
        self.c=self.conn.cursor()
        self.c.execute("select * from Plasma_Donar")
        rows=self.c.fetchall()
        if len(rows)!=0:
                self.Bloold_Bank_table.delete(*self.Bloold_Bank_table.get_children())
                for row in rows:
                        self.Bloold_Bank_table.insert('',END,values=row)
                self.conn.commit()
        self.conn.close()

    def getcursor(self,ev):
        cursor_row=self.Bloold_Bank_table.focus()
        Content=self.Bloold_Bank_table.item(cursor_row)
        row=Content['values']

        self.Bloold_Bank_table.set(row[0])
        self.Bloold_Bank_table.set(row[1])
        self.Bloold_Bank_table.set(row[2])
        
    def clear1(self):
        self.Bloold_Bank_table.delete(*self.Bloold_Bank_table.get_children())
        self.searchby.set("")
        self.searchby1.set("")

    
    
    def logout(self):
        self.read1=StringVar()
        with open("Temp.txt","r+") as file:
            self.read1=file.read()
            file.truncate()
    
        a=messagebox.askyesnocancel("Hey","Confirm again for Logout")
        if a>0:
            now = datetime.now()
            self.Time2=now.strftime('%H:%M:%S')

            self.today1= now.strftime("%d/%m/%Y")
            self.destroy()
            self.conn=sqlite3.connect("plasma.db")
            self.c=self.conn.cursor()
            y="UPDATE Last_Login_User set last_login_time=\""+str(self.Time2)+"\", last_login_date=\""+str(self.today1)+"\" where UID =\""+str(self.read1)+"\""
            #print(y)
            self.c.execute(y)
            self.conn.commit()
            root=Tk()
            clas=U_login(root)            
        else:
            pass



    def change_pasw(self):  
        self.root2 = Toplevel(self)  # Child Window "Tk() can Also be use here"
        self.root2.title("Change Password")
        self.root2.geometry("750x370+350+150")
        self.root2.configure(bg="black")
        photo1 = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
        self.root2.iconphoto(False, photo1)
        self.root2.grab_set() 
        self.root2.resizable(False, False)

        title_child = Label(self.root2, text="Reset Password", bg="#152238", fg="white",compound=LEFT, font=("Goudy Old Style", 48, "bold"), anchor="w").place(x=0, y=0, relwidth=1)
        
        phone_lbl = Label(self.root2, text="Phone No.", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=120)
        self.phone_ = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.phone_.place(x=260, y=120)
        
        current_lbl = Label(self.root2, text="Current Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=170)
        self.current_ = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.current_.place(x=260, y=170)
        
        pass_lbl = Label(self.root2, text="New Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=220)
        self.pass_ = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.pass_.place(x=260, y=220)
        
        passcon_lbl = Label(self.root2, text="Confirm Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=270)
        self.passcon = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.passcon.place(x=260, y=270)
        
        Reset_btn = Button(self.root2, text="Reset", font=("times new roman", 18, "bold"), activebackground="blue",activeforeground="white", bg="blue", fg="white", cursor="hand2", command=self.reset)
        Reset_btn.place(x=495, y=310, width=140, height=30) 

      
        
    def reset(self):
        with open("Temp.txt","r+") as file:
            self.read1=file.read()
        #print(self.read1)
        self.passw = self.pass_.get()
        self.passconw = self.passcon.get()
        self.current2_=self.current_.get()
        self.phone_2=self.phone_.get()
        
        self.conn = sqlite3.connect("plasma.db")
        self.c = self.conn.cursor()
        self.c.execute("SELECT Password from user WHERE Phone_No=" +self.phone_2)
        self.data = self.c.fetchall()
        if self.data==[]:
            return messagebox.showerror("Error"," Current Password not Matched to Your mail Id" , parent=self.root2)
        else:
            for i in self.data:
                    #print(i[0])
                    self.c.execute("SELECT Email from user WHERE Phone_No=" +self.phone_2)
                    self.data = self.c.fetchall()
                    for j in self.data:
                        a=str(j[0])
                    if i[0] == self.current2_:
                        self.OTP_Forget=str(random.randint(100000,999999))
                        send = smtplib.SMTP("smtp.gmail.com", 587)  # Create session for Gmail
                        send.starttls()  # transport layer

                        msg = EmailMessage()
                        msg["Subject"] = "OTP"
                        msg["From"] = "aj147ps@gmail.com"
                        msg["To"] = a
                        msg.set_content("Hi! your OTP for reset password: "+"\'"+str(self.OTP_Forget)+"\'")        
                            
                        try:
                            send.login("aj147ps@gmail.com","xcavbfayvnthixwy")
                        except smtplib.SMTPAuthenticationError:
                            messagebox.showerror("Error","Error Occur Otp Not")    

                        try:
                            try:
                                try:                                
                                    
                                    send.send_message(msg)
                                    messagebox.showinfo("Mailed","OTP Sent to Your Mail Id") 
                                    self.root2.destroy()
                                    self.root3 = Toplevel(self)  # Child Window "Tk() can Also be use here"
                                    self.root3.title("Verification")
                                    self.root3.geometry("750x320+350+150")
                                    self.root3.configure(bg="black")
                                    photo4 = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
                                    self.root3.iconphoto(False, photo4)
                                    self.root3.grab_set() 
                                    self.root3.resizable(False, False)
                                
                                    title_child = Label(self.root3, text="Reset Password", bg="#152238", fg="white",compound=LEFT, font=("Goudy Old Style", 48, "bold"), anchor="w").place(x=0, y=0, relwidth=1)
                                    otp_lbl = Label(self.root3, text="Enter OTP", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=120)
                                    self.otp_ = Entry(self.root3, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
                                    self.otp_.place(x=260, y=120)
                                    
                                    Reset_btn = Button(self.root3, text="Reset", font=("times new roman", 18, "bold"), activebackground="blue",activeforeground="white", bg="blue", fg="white", cursor="hand2", command=self.reset1)
                                    Reset_btn.place(x=495, y=260, width=140, height=30) 
                        
                                except smtplib.SMTPRecipientsRefused:
                                    messagebox.showerror("Mailed","Mail Not Sent")
                            except smtplib.SMTPException:
                                messagebox.showerror("Mailed","Mail Not Sent")
                        except smtplib.SMTPConnectError:
                            messagebox.showerror("Error","Connection Error")
                    else:
                        return messagebox.showerror("Error","Contact No. have not given Mail Id")

    def reset1(self):
        self.one_ = self.otp_.get()
        #print(self.one_)
        if str(self.one_)==str(self.OTP_Forget):
            if len(str(self.passw))>=8:
                if self.passw == self.passconw:
                    y= f"UPDATE user SET Password = {str(self.passw)} WHERE Phone_No = {str(self.phone_2)}"
                    self.c.execute(str(y))
                    self.conn.commit()
                    self.conn.close()
                    self.OTP_Forget=""
                    messagebox.showinfo("Info", "Successfully Changed!!", parent=self.root3)
                    self.root3.destroy()                    
                else:
                    return messagebox.showerror("Error", "Password Cann't Changed  password  and confirm password not match!!", parent=self.root3)
            else:
                return messagebox.showerror("Error", "Password should be of minimum 8 Characters", parent=self.root3)
        else:
            return messagebox.showerror("Error", "OTP Entered is Wrong", parent=self.root3)

    def clock(self):

        self.h = str(time.strftime("%H"))
        self.m = str(time.strftime("%M"))
        self.s = str(time.strftime("%S"))

        if int(self.h)<15 and int(self.m)>0:
            self.lbl_abv.config(text="PM")

        if int(self.h)>=15 and int(self.h)<20 and int(self.m)>0:
            self.lbl_abv.config(text="PM")
        
        if int(self.h)>=20 and int(self.h)<24 and int(self.m)>0:
            self.lbl_abv.config(text="PM")

        if int(self.h)>12 and int(self.h)<15 and int(self.m)>0:
            self.lbl_abv.config(text="PM")

        if int(self.h)>0 and int(self.h)<12 and int(self.m)>0:
            self.lbl_abv.config(text="AM")

         
        self.lbl_hr.config(text = self.h)
        self.lbl_min.config(text = self.m)
        self.lbl_sec.config(text = self.s)
        self.lbl_hr.after(200,self.clock)

class User_Check_class(Tk):
    def __init__(self,*arg):       # Constructors
        Tk.__init__(self,*arg)
        photo = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
        self.iconphoto(False, photo)

        self.title("Plasma Finder".center(420))  # title for Window 
        self.configure(background = "black")  # background color for window 
        self.geometry("1360x768+0+0")
        photo = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
        self.iconphoto(False, photo)

        bg_color ="#FFFFF6"
        
     
        self.bg_icon = ImageTk.PhotoImage(file="Pics\\1 (1).jpg")
        bg_lbl = Label(self, image = self.bg_icon).pack(fill=Y) # we put image into our window
        
        self.hos_icon=ImageTk.PhotoImage(file="Pics\\1 (2) copy.jpg")
                
        
        F1 = LabelFrame(self,bd=10,relief=GROOVE,bg=bg_color)
        F1.place(x=0,relwidth=1,height=100 )

        lbl = Label(F1,text="Plasma Finder", compound=LEFT, image=self.hos_icon,bg=bg_color, font= ("times new roman",20,"bold")).place(x=0, y=5)

        self.lbl_hr = Label(F1,text="12" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_hr.place(x=890, y=40)
        
        self.lbl_COLON = Label(F1,text=":" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_COLON.place(x=915, y=40)
       
       
        self.lbl_min = Label(F1,text="12" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_min.place(x=925, y=40)
       
        self.lbl_COLON = Label(F1,text=":" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_COLON.place(x=950, y=40)
       
        self.lbl_sec = Label(F1,text="12" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_sec.place(x=960, y=40)
        

        self.lbl_abv = Label(F1,text="AM" , font = ("times new roman", 13,"bold"),bg=bg_color)
        self.lbl_abv.place(x=985, y=43)
       
       
        self.font=("times new roman",20,"bold")
        self.calendar = []

        ntpClient = ntplib.NTPClient()
        response = ntpClient.request('pool.ntp.org')
        a=ctime(response.tx_time)
        b=[a[i:i+10] for i in range(0, len(a), 10)]
        c=str(b[0])
        d=str(b[2])

        self.date = Label(F1, font=("times new roman",15,"bold"), text=c, bg=bg_color)
        self.date.place(x=740, y=40)

        self.date1 = Label(F1, font=("times new roman",15,"bold"), text=d,bg=bg_color)
        self.date1.place(x=840, y=40)

        
        self.date2 = Label(F1, font=("times new roman",15,"bold"), text="Calendar",bg=bg_color)
        self.date2.place(x=750, y=5)

        self.calendar.append(DateEntry(F1, font=("times new roman",15,"bold"), locale='en_GB',state="readonly",width=10))
        self.calendar[-1].place(x=855, y=20, anchor="w")

        
        btn_changepass = Button(F1, text="ChangePassword",relief=RAISED,width =15,height=1, font=("times new roman",14,"bold"),bg="red",foreground="white",command=self.change_pasw).place(x=1145,y=20,anchor="w")
        btn_logout = Button(F1, text="Logout",relief=RAISED,width =15,height=1, font=("times new roman",14,"bold"),bg="light green",foreground="black", command=self.logout).place(x=1145,y=60,anchor="w")

        lbl2 = Label(F1,bg=bg_color)
        lbl2.place(x=25,y=10)

        F2 = LabelFrame(self,bd=10,relief=GROOVE,bg=bg_color)
        F2.place(x=0,y=100,width=150,height=670 )

        F21 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F21.place(x=0,y=0,width=130,height=133 )
        
        F22 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F22.place(x=0,y=133,width=130,height=133)
        
        F23 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F23.place(x=0,y=266,width=130,height=133 )
        
        F24 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F24.place(x=0,y=399,width=130,height=133)
        
        F25 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F25.place(x=0,y=532,width=130,height=133)

        self.U_mange = PhotoImage(file="Pics\\User_Det.png")
        self.donor_b = ImageTk.PhotoImage(file="Pics\\Blood Donar.jpg")
        self.b_bank = ImageTk.PhotoImage(file="Pics\Blood Bank Search.jpg")    
        self.p_donar = ImageTk.PhotoImage(file="Pics\Plasma.png")
        self.exit = ImageTk.PhotoImage(file="Pics\\Exit.jpg")
        
        btn_U_det = Button(F21,image= self.U_mange,bg=bg_color,relief=RAISED,width =115,height=120,command=self.U_det).place(x=0,y=60,anchor="w")
        btn_blood_donor = Button(F22,image= self.donor_b,bg=bg_color,relief=RAISED,width =115,height=120,command=self.Blood_Donar ).place(x=0,y=60,anchor="w")
        btn_blood_bank = Button(F23,relief=RAISED,bg=bg_color,image=self.b_bank,width =115,height=120,command=self.Blood_Bank ).place(x=0,y=60,anchor="w")
        btn_Plasma = Button(F24,relief=RAISED,image=self.p_donar,bg=bg_color,width =115,height=120, command=self.Plasma).place(x=0,y=60,anchor="w")
        btn_Exit = Button(F25,relief=RAISED,bg=bg_color,image=self.exit,width =115,height=120, command=self.Exit).place(x=0,y=60,anchor="w")

        F3 = LabelFrame(self,bd=5,relief=FLAT,bg="light gray")
        F3.place(x=150,y=100,relwidth=1,height=30 )
        lbl_1= Label(F3,text="Dashboard / Hospital",font=("comic sans",15,"italic"),bg="light gray")
        lbl_1.place(x=0,y=00)

        btn_User = Button(F3, bd=5, relief=GROOVE, bg="red", fg="white", font=("",7,"bold"), text= "User View",command=self.User_Check)
        btn_User.place(x=1000,y=0)
        home_btn = Button(F3, text="Home",bd=5,relief=GROOVE, font=("",7,"bold"), fg="white", bg="blue", command=self.Home)
        home_btn.place(x=300,y=0)

        self.W_D=StringVar()
        self.Phone=StringVar()
        self.C_D_Plasma= StringVar()
        self.C_D_Blood=StringVar()
        self.UID=StringVar()
        self.bloodgrp =StringVar()
        self.searchby =StringVar()
        self.searchval = StringVar()
        
        self.F4 = Frame(self,bd=5,relief=FLAT)
        self.F4.place(x=151,y=132,relwidth=1,height=600)
        lbl_1= Label(self.F4,text="Manage User Data",fg="#008080",font=("geometric sans-serif",30,"bold"))
        lbl_1.place(x=0,y=0)
    
        seprator1_style = ttk.Style()
        separator1 = ttk.Separator(self.F4, orient='horizontal',style="Line.TSeparator")
        separator1.place(x=0,width=700,y=50)
        seprator1_style.configure("Line.TSeparator")
       
        lbl_roll=Label(self.F4,text="UID",font=("times new roman",18,"bold"),bg="#F5F5F5")
        lbl_roll.place(x=0,y=90,anchor="w")
        txt_roll=Entry(self.F4, textvariable=self.UID,state="readonly", width=17, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.place(x=170,y=90,anchor="w")

        lbl_roll=Label(self.F4,text="Phone",bg="#F5F5F5",font=("times new roman",18,"bold"))
        lbl_roll.place(x=0,y=140,anchor="w")
        txt_roll=Entry(self.F4,width=17, state="readonly",textvariable=self.Phone,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.place(x=170,y=140,anchor="w")
        
        lbl_roll=Label(self.F4,text="W_D",bg="#F5F5F5",font=("times new roman",18,"bold"))
        lbl_roll.place(x=0,y=190,anchor="w")
        txt_roll=Entry(self.F4, textvariable=self.W_D,width=17, state="readonly",font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.place(x=170,y=190,anchor="w")


        lbl_roll=Label(self.F4,text="C_D_Plasma",bg="#F5F5F5",font=("times new roman",20,"bold"))
        lbl_roll.place(x=0, y=240, anchor="w")

        combo_class = OptionMenu(self.F4, self.C_D_Plasma,"Yes","No")
        combo_class.place(x=168,y=240,anchor="w")
        combo_class.configure(width=23,relief=RAISED,bg="grey")
        
        lbl_roll=Label(self.F4,text="C_D_Blood",bg="#F5F5F5",font=("times new roman",18,"bold"))
        lbl_roll.place(x=0,y=290,anchor="w")
        combo_class = OptionMenu(self.F4, self.C_D_Blood,"Yes","No")
        combo_class.place(x=168,y=290,anchor="w")
        combo_class.configure(width=23,relief=RAISED,bg="grey")

        lbl_roll=Label(self.F4,text="Blood Group",bg="#F5F5F5",font=("times new roman",18,"bold"))
        lbl_roll.place(x=380,y=190,anchor="w")
        txt_roll=Entry(self.F4, textvariable=self.bloodgrp, width=10, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.place(x=540,y=190,anchor="w")
        
        
        F5 =Frame(self.F4,bd=10,relief=SUNKEN,bg="white")
        F5.place(x=0,y=350,width=700,height=80 )

        btn_update2 = Button(F5,relief=GROOVE,width=8, font=("times new roman",18,"bold"),bg="navy blue",fg="yellow",bd=6,text="Update",command=self.update).grid(row=0,column=0,pady=6,padx=50,sticky="nesw")        
        btn_Delete = Button(F5,relief=GROOVE, width=8,font=("times new roman",18,"bold"),bg="navy blue",fg="yellow",bd=6,text="Delete",command=self.delete).grid(row=0,column=1,pady=6,padx=50,sticky="nesw")
        btn_Clear = Button(F5,relief=GROOVE, width=15,font=("times new roman",13,"bold"),bg="navy blue",fg="yellow",bd=6,text="Clear ALL",command=self.clear).grid(row=0,column=2,pady=6,padx=50,sticky="nesw") 

        seprator2_style = ttk.Style()
        separator2 = ttk.Separator(self.F4, orient='vertical',style="Line.TSeparator")
        separator2.place(x=700,height=590,y=0)
        seprator2_style.configure("Line.TSeparator")

        lb_search=Label(self.F4,text="Search By", font=("times new roman",15,"bold"),bg="#F5F5F5")
        lb_search.place(x=0 ,y=500, anchor="w")
        combo_search=ttk.Combobox(self.F4, textvariable=self.searchby,width=17, font=("times new roman",13,"bold"),state='readonly')
        combo_search['values']=("UID","B_Group")
        combo_search.place(x=140, y=500, anchor="w")

        lb_search2=Entry(self.F4,textvariable=self.searchval,width=15,relief=SUNKEN,bd=5,font=("times new roman",15,"bold"),bg="#F5F5F5")
        lb_search2.place(x=360, y=500, anchor="w")
        

        btn_searchall = Button(self.F4,relief=RAISED,width=30,font=("times new roman",10,"bold"),bg="navy blue",fg="white",bd=6, text="Search All",command=self.search)
        btn_searchall.place(x=0,y=550,anchor="w")
        btn_search = Button(self.F4,relief=RAISED,width=30,font=("times new roman",10,"bold"),bg="navy blue",fg="white",bd=6,text="Search",command=self.search_data)        
        btn_search.place(x=400,y=550,anchor="w")

        F6 =Frame(self.F4,bd=10,relief=SUNKEN,bg="white")
        F6.place(x=720,y=40,width=475,height=500 )

        Table_Frame=Frame(F6,bd=4, relief=RIDGE,bg=bg_color)
        Table_Frame.place(x=0,y=0,width=455,height=480)

        scroll_x=Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame, orient=VERTICAL)
        self.user_table=ttk.Treeview(Table_Frame,columns=("UID" ,"Name"  , "B_Group"  , "W_D" ),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.user_table.xview)
        scroll_y.config(command=self.user_table.yview)

        self.user_table.heading("UID", text="UID")
        self.user_table.heading("Name", text="Name")
        self.user_table.heading("B_Group", text="B_Group")
        self.user_table.heading("W_D", text="W_D")
        
        self.user_table.column("UID", width=80)
        self.user_table.column("Name", width=200)
        self.user_table.column("B_Group", width=200)
        self.user_table.column("W_D", width=300)     
     
        self.user_table['show']='headings'
        self.clock()

    def search(self):
                
        self.user_table.column("UID", width=80)
        self.user_table.column("Name", width=200)
        self.user_table.column("B_Group", width=200)
        self.user_table.column("W_D", width=300)     
     
        self.user_table['show']='headings'

        self.user_table.pack(fill=BOTH,expand=1)
        self.user_table.bind("<ButtonRelease-1>",self.getcursor)
        self.fetch_data()

    def search_data(self):
        if self.searchby.get()=="" and self.searchval.get()=="":
            return messagebox.showwarning("Warning","Fields should be filled")
        if self.searchby.get()=="" :
            return messagebox.showwarning("Warning","Shearch By Option Should be filled")
        if self.searchval.get()=="":
            return messagebox.showwarning("Warning","Search box should be filled")
        
        else:
            if self.searchby.get() == "UID":
                self.user_table.column("UID", width=80)
                self.user_table.column("Name", width=200)
                self.user_table.column("B_Group", width=200)
                self.user_table.column("W_D", width=300)     
            
                self.user_table['show']='headings'

                self.user_table.pack(fill=BOTH,expand=1)
                self.user_table.bind("<ButtonRelease-1>",self.getcursor)
                self.fetch_data()

                self.conn=sqlite3.connect("plasma.db")
                self.c=self.conn.cursor()
                self.c.execute("select * from user_details where UID= '"+self.searchval.get()+"'")
                rows=self.c.fetchall()
                if len(rows)!=0:
                        self.user_table.delete(*self.user_table.get_children())
                        for row in rows:
                                self.user_table.insert('',END,values=row)
                        self.conn.commit()
                        self.conn.close()

                else:
                    return messagebox.showerror("Error","UID Not Exist")        

            if self.searchby.get() == "B_Group":
                self.user_table.column("UID", width=80)
                self.user_table.column("Name", width=200)
                self.user_table.column("B_Group", width=200)
                self.user_table.column("W_D", width=300)     
            
                self.user_table['show']='headings'

                self.user_table.pack(fill=BOTH,expand=1)
                self.user_table.bind("<ButtonRelease-1>",self.getcursor)
                self.fetch_data()

                self.conn=sqlite3.connect("plasma.db")
                self.c=self.conn.cursor()
                self.c.execute("select * from user_details where B_Group= '"+self.searchval.get()+"'")
                rows=self.c.fetchall()
                if len(rows)!=0:
                        self.user_table.delete(*self.user_table.get_children())
                        for row in rows:
                                self.user_table.insert('',END,values=row)
                        self.conn.commit()
                        self.conn.close()

                else:
                    return messagebox.showerror("Error","Blood Group Not Exist")   
    
    def fetch_data(self):
        self.conn=sqlite3.connect("plasma.db")
        self.c=self.conn.cursor()
        self.c.execute("select * from user_details")
        rows=self.c.fetchall()
        if len(rows)!=0:
                self.user_table.delete(*self.user_table.get_children())
                for row in rows:
                        self.user_table.insert('',END,values=row)
                self.conn.commit()
        self.conn.close()

    def getcursor(self,ev):
        cursor_row=self.user_table.focus()
        Content=self.user_table.item(cursor_row)
        row=Content['values']
        #print(row)
        a = row[0]
        self.UID.set(a)
        self.bloodgrp.set(row[2])
        self.W_D.set(row[3])
        self.conn=sqlite3.connect("plasma.db")
        self.c = self.conn.cursor()
        self.cmd = "SELECT Phone_No from user WHERE UID = '" +a+"'" 
        self.c.execute(self.cmd)
        self.data=self.c.fetchall()
        if self.data:
            for i in self.data:
                    a=str(i[0])
        self.c.execute(self.cmd)
        self.Phone.set(a)        

    def update(self):
        self.conn=sqlite3.connect("plasma.db")
        self.c=self.conn.cursor()
        if self.C_D_Blood.get()=="Yes" and self.C_D_Plasma.get()=="Yes":
            self.c.execute("SELECT * from Plasma_Donar WHERE UID= '"+self.UID.get()+"'")
            self.data=self.c.fetchall()
            if self.data:
                return messagebox.showerror("Error","UID Already Exist")
            else:
                self.c.execute("INSERT INTO Plasma_Donar (UID, Blood_Group, Phone_No ) VALUES (?,?,?)",(self.UID.get(),self.bloodgrp.get(),str(self.Phone.get())))
            
            self.c.execute("SELECT * from Blood_Donor_Approved WHERE UID= '"+self.UID.get()+"'")
            self.data=self.c.fetchall()
            if self.data:
                return messagebox.showerror("Error","UID Already Exist")
            else:
                self.c.execute("INSERT INTO Blood_Donor_Approved (UID, B_Group, Phone_No ) VALUES (?,?,?)",(self.UID.get(),self.bloodgrp.get(),str(self.Phone.get())))
        
        elif self.C_D_Blood.get()=="Yes" and self.C_D_Plasma.get()=="No":
            self.c.execute("SELECT * from Blood_Donor_Approved WHERE UID= '"+self.UID.get()+"'")
            self.data=self.c.fetchall()
            if self.data:
                return messagebox.showerror("Error","UID Already Exist")
            else:
                self.c.execute("INSERT INTO Blood_Donor_Approved (UID, B_Group, Phone_No ) VALUES (?,?,?)",(self.UID.get(),self.bloodgrp.get(),str(self.Phone.get())))

        elif self.C_D_Blood.get()=="No" and self.C_D_Plasma.get()=="Yes":
            self.c.execute("SELECT * from Plasma_Donar WHERE UID= '"+self.UID.get()+"'")
            self.data=self.c.fetchall()
            if self.data:
                return messagebox.showerror("Error","UID Already Exist")
            else:
                self.c.execute("INSERT INTO Plasma_Donar (UID, Blood_Group, Phone_No ) VALUES (?,?,?)",(self.UID.get(),self.bloodgrp.get(),str(self.Phone.get())))
            
        self.conn.commit()
        messagebox.showinfo("Error"," Data  Updated")
        self.conn.close()


            
    def delete(self):
        if self.UID.get()=="":
            return messagebox("Error","Select User to be Deleted")
        try:
            self.conn=sqlite3.connect("plasma.db")
            self.c=self.conn.cursor()
            self.c.execute("DELETE FROM user_details WHERE UID = '" +self.UID.get()+"'")
            self.c.execute("DELETE FROM user WHERE UID = '" +self.UID.get()+"'")
            try:
                self.c.execute("DELETE FROM Plasma_Donar WHERE UID = '" +self.UID.get()+"'")
            except Exception:
                pass
            try:
                self.c.execute("DELETE FROM Blood_Donor_Approved WHERE UID = '" +self.UID.get()+"'")
            except Exception:
                pass                
            self.conn.commit()
            self.conn.close()
            messagebox.showinfo("Info","Succesfully Deleted")
            self.clear()
        except sqlite3.Error as error:
            messagebox.showerror("error","Failed to update sqlite table")
 
    def clear(self):
        self.W_D.set("")
        self.Phone.set("")
        self.C_D_Plasma.set("")
        self.C_D_Blood.set("")
        self.UID.set("")
        self.bloodgrp.set("")
        self.searchby.set("")
        self.searchval.set("")
        self.user_table.delete(*self.user_table.get_children())
    
    def Home(self):
        self.destroy()
        Hospital_Page().mainloop()

    def U_det(self):
        self.destroy()
        H_Manage().mainloop()
        
    def Blood_Donar(self):
        self.destroy()
        Bload_Search_hos().mainloop()
        
    
    def Blood_Bank(self):
        self.destroy()
        Bload_Bank_hos().mainloop()

    def Plasma(self):
        self.destroy()
        Plasma_Search_hos().mainloop()    
    
    def User_Check(self):
        self.destroy()
        User_Check_class().mainloop()
    
    def Exit(self):
        self.destroy()
    
    def logout(self):
        self.read1=StringVar()
        with open("Temp1.txt","r+") as file:
            self.read1=file.read()
            file.truncate()
    
        a=messagebox.askyesnocancel("Hey","Confirm again for Logout")
        if a>0:
            now = datetime.now()
            self.Time2=now.strftime('%H:%M:%S')

            self.today1= now.strftime("%d/%m/%Y")
            self.destroy()
            self.conn=sqlite3.connect("plasma.db")
            self.c=self.conn.cursor()
            y="UPDATE Last_Login_hospital set time=\""+str(self.Time2)+"\", date=\""+str(self.today1)+"\" where HID =\""+str(self.read1)+"\""
            #print(y)
            self.c.execute(y)
            self.conn.commit()
            root=Tk()
            clas=H_login(root)            
        else:
            pass



    def change_pasw(self):  
        self.root2 = Toplevel(self)  # Child Window "Tk() can Also be use here"
        self.root2.title("Change Password")
        self.root2.geometry("750x370+350+150")
        self.root2.configure(bg="black")
        photo1 = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
        self.root2.iconphoto(False, photo1)
        self.root2.grab_set() 
        self.root2.resizable(False, False)

        title_child = Label(self.root2, text="Reset Password", bg="#152238", fg="white",compound=LEFT, font=("Goudy Old Style", 48, "bold"), anchor="w").place(x=0, y=0, relwidth=1)
        
        phone_lbl = Label(self.root2, text="Phone No.", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=120)
        self.phone_ = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.phone_.place(x=260, y=120)
        
        current_lbl = Label(self.root2, text="Current Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=170)
        self.current_ = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.current_.place(x=260, y=170)
        
        pass_lbl = Label(self.root2, text="New Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=220)
        self.pass_ = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.pass_.place(x=260, y=220)
        
        passcon_lbl = Label(self.root2, text="Confirm Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=270)
        self.passcon = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.passcon.place(x=260, y=270)
        
        Reset_btn = Button(self.root2, text="Reset", font=("times new roman", 18, "bold"), activebackground="blue",activeforeground="white", bg="blue", fg="white", cursor="hand2", command=self.reset)
        Reset_btn.place(x=495, y=310, width=140, height=30) 

      
        
    def reset(self):
        with open("Temp1.txt","r+") as file:
            self.read1=file.read()
        #print(self.read1)
        self.passw = self.pass_.get()
        self.passconw = self.passcon.get()
        self.current2_=self.current_.get()
        self.phone_2=self.phone_.get()
        
        self.conn = sqlite3.connect("plasma.db")
        self.c = self.conn.cursor()
        self.c.execute("SELECT Password from hos WHERE Phone_No=" +self.phone_2)
        self.data = self.c.fetchall()
        if self.data==[]:
            return messagebox.showerror("Error"," Current Password not Matched to Your mail Id" , parent=self.root2)
        else:
            for i in self.data:
                    #print(i[0])
                    self.c.execute("SELECT Email from hos WHERE Phone_No=" +self.phone_2)
                    self.data = self.c.fetchall()
                    for j in self.data:
                        a=str(j[0])
                    if i[0] == self.current2_:
                        self.OTP_Forget=str(random.randint(100000,999999))
                        send = smtplib.SMTP("smtp.gmail.com", 587)  # Create session for Gmail
                        send.starttls()  # transport layer

                        msg = EmailMessage()
                        msg["Subject"] = "OTP"
                        msg["From"] = "aj147ps@gmail.com"
                        msg["To"] = a
                        msg.set_content("Hi! your OTP for reset password: "+"\'"+str(self.OTP_Forget)+"\'")        
                            
                        try:
                            send.login("aj147ps@gmail.com","xcavbfayvnthixwy")
                        except smtplib.SMTPAuthenticationError:
                            messagebox.showerror("Error","Error Occur Otp Not")    

                        try:
                            try:
                                try:                                
                                    
                                    send.send_message(msg)
                                    messagebox.showinfo("Mailed","OTP Sent to Your Mail Id") 
                                    self.root2.destroy()
                                    self.root3 = Toplevel(self)  # Child Window "Tk() can Also be use here"
                                    self.root3.title("Verification")
                                    self.root3.geometry("750x320+350+150")
                                    self.root3.configure(bg="black")
                                    photo4 = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
                                    self.root3.iconphoto(False, photo4)
                                    self.root3.grab_set() 
                                    self.root3.resizable(False, False)
                                
                                    title_child = Label(self.root3, text="Reset Password", bg="#152238", fg="white",compound=LEFT, font=("Goudy Old Style", 48, "bold"), anchor="w").place(x=0, y=0, relwidth=1)
                                    otp_lbl = Label(self.root3, text="Enter OTP", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=120)
                                    self.otp_ = Entry(self.root3, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
                                    self.otp_.place(x=260, y=120)
                                    
                                    Reset_btn = Button(self.root3, text="Reset", font=("times new roman", 18, "bold"), activebackground="blue",activeforeground="white", bg="blue", fg="white", cursor="hand2", command=self.reset1)
                                    Reset_btn.place(x=495, y=260, width=140, height=30) 
                        
                                except smtplib.SMTPRecipientsRefused:
                                    messagebox.showerror("Mailed","Mail Not Sent")
                            except smtplib.SMTPException:
                                messagebox.showerror("Mailed","Mail Not Sent")
                        except smtplib.SMTPConnectError:
                            messagebox.showerror("Error","Connection Error")
                    else:
                        return messagebox.showerror("Error","Contact No. have not given Mail Id")

    def reset1(self):
        self.one_ = self.otp_.get()
        #print(self.one_)
        if str(self.one_)==str(self.OTP_Forget):
            if len(str(self.passw))>=8:
                if self.passw == self.passconw:
                    y= f"UPDATE hos SET Password = {str(self.passw)} WHERE Phone_No = {str(self.phone_2)}"
                    self.c.execute(str(y))
                    self.conn.commit()
                    self.conn.close()
                    self.OTP_Forget=""
                    messagebox.showinfo("Info", "Successfully Changed!!", parent=self.root3)
                    self.root3.destroy()                    
                else:
                    return messagebox.showerror("Error", "Password Cann't Changed  password  and confirm password not match!!", parent=self.root3)
            else:
                return messagebox.showerror("Error", "Password should be of minimum 8 Characters", parent=self.root3)
        else:
            return messagebox.showerror("Error", "OTP Entered is Wrong", parent=self.root3)

    
    def clock(self):

        self.h = str(time.strftime("%H"))
        self.m = str(time.strftime("%M"))
        self.s = str(time.strftime("%S"))

        if int(self.h)<15 and int(self.m)>0:
            self.lbl_abv.config(text="PM")

        if int(self.h)>=15 and int(self.h)<20 and int(self.m)>0:
            self.lbl_abv.config(text="PM")
        
        if int(self.h)>=20 and int(self.h)<24 and int(self.m)>0:
            self.lbl_abv.config(text="PM")

        if int(self.h)>12 and int(self.h)<15 and int(self.m)>0:
            self.lbl_abv.config(text="PM")

        if int(self.h)>0 and int(self.h)<12 and int(self.m)>0:
            self.lbl_abv.config(text="AM")

         
        self.lbl_hr.config(text = self.h)
        self.lbl_min.config(text = self.m)
        self.lbl_sec.config(text = self.s)
        self.lbl_hr.after(200,self.clock)

class H_Manage(Tk):
    def __init__(self,*arg):       # Constructors
        Tk.__init__(self,*arg)
        photo = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
        self.iconphoto(False, photo)

        self.title("Plasma Finder".center(420))  # title for Window 
        self.configure(background = "black")  # background color for window 
        self.geometry("1360x768+0+0")
        photo = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
        self.iconphoto(False, photo)

        bg_color ="#FFFFF6"
        
     
        self.bg_icon = ImageTk.PhotoImage(file="Pics\\1 (1).jpg")
        bg_lbl = Label(self, image = self.bg_icon).pack(fill=Y) # we put image into our window
        
        self.hos_icon=ImageTk.PhotoImage(file="Pics\\1 (2) copy.jpg")
                
        
        F1 = LabelFrame(self,bd=10,relief=GROOVE,bg=bg_color)
        F1.place(x=0,relwidth=1,height=100 )

        lbl = Label(F1,text="Plasma Finder", compound=LEFT, image=self.hos_icon,bg=bg_color, font= ("times new roman",20,"bold")).place(x=0, y=5)

        self.lbl_hr = Label(F1,text="12" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_hr.place(x=890, y=40)
        
        self.lbl_COLON = Label(F1,text=":" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_COLON.place(x=915, y=40)
       
       
        self.lbl_min = Label(F1,text="12" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_min.place(x=925, y=40)
       
        self.lbl_COLON = Label(F1,text=":" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_COLON.place(x=950, y=40)
       
        self.lbl_sec = Label(F1,text="12" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_sec.place(x=960, y=40)
        

        self.lbl_abv = Label(F1,text="AM" , font = ("times new roman", 13,"bold"),bg=bg_color)
        self.lbl_abv.place(x=985, y=43)
       
       
        self.font=("times new roman",20,"bold")
        self.calendar = []

        ntpClient = ntplib.NTPClient()
        response = ntpClient.request('pool.ntp.org')
        a=ctime(response.tx_time)
        b=[a[i:i+10] for i in range(0, len(a), 10)]
        c=str(b[0])
        d=str(b[2])

        self.date = Label(F1, font=("times new roman",15,"bold"), text=c, bg=bg_color)
        self.date.place(x=740, y=40)

        self.date1 = Label(F1, font=("times new roman",15,"bold"), text=d,bg=bg_color)
        self.date1.place(x=840, y=40)

        
        self.date2 = Label(F1, font=("times new roman",15,"bold"), text="Calendar",bg=bg_color)
        self.date2.place(x=750, y=5)

        self.calendar.append(DateEntry(F1, font=("times new roman",15,"bold"), locale='en_GB',state="readonly",width=10))
        self.calendar[-1].place(x=855, y=20, anchor="w")

        
        btn_changepass = Button(F1, text="ChangePassword",relief=RAISED,width =15,height=1, font=("times new roman",14,"bold"),bg="red",foreground="white",command=self.change_pasw).place(x=1145,y=20,anchor="w")
        btn_logout = Button(F1, text="Logout",relief=RAISED,width =15,height=1, font=("times new roman",14,"bold"),bg="light green",foreground="black", command=self.logout).place(x=1145,y=60,anchor="w")

        lbl2 = Label(F1,bg=bg_color)
        lbl2.place(x=25,y=10)

        F2 = LabelFrame(self,bd=10,relief=GROOVE,bg=bg_color)
        F2.place(x=0,y=100,width=150,height=670 )

        F21 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F21.place(x=0,y=0,width=130,height=133 )
        
        F22 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F22.place(x=0,y=133,width=130,height=133)
        
        F23 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F23.place(x=0,y=266,width=130,height=133 )
        
        F24 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F24.place(x=0,y=399,width=130,height=133)
        
        F25 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F25.place(x=0,y=532,width=130,height=133)

        self.U_mange = PhotoImage(file="Pics\\User_Det.png")
        self.donor_b = ImageTk.PhotoImage(file="Pics\\Blood Donar.jpg")
        self.b_bank = ImageTk.PhotoImage(file="Pics\Blood Bank Search.jpg")    
        self.p_donar = ImageTk.PhotoImage(file="Pics\Plasma.png")
        self.exit = ImageTk.PhotoImage(file="Pics\\Exit.jpg")
        
        btn_U_det = Button(F21,image= self.U_mange,bg=bg_color,relief=RAISED,width =115,height=120,command=self.U_det).place(x=0,y=60,anchor="w")
        btn_blood_donor = Button(F22,image= self.donor_b,bg=bg_color,relief=RAISED,width =115,height=120,command=self.Blood_Donar ).place(x=0,y=60,anchor="w")
        btn_blood_bank = Button(F23,relief=RAISED,bg=bg_color,image=self.b_bank,width =115,height=120,command=self.Blood_Bank ).place(x=0,y=60,anchor="w")
        btn_Plasma = Button(F24,relief=RAISED,image=self.p_donar,bg=bg_color,width =115,height=120, command=self.Plasma).place(x=0,y=60,anchor="w")
        btn_Exit = Button(F25,relief=RAISED,bg=bg_color,image=self.exit,width =115,height=120, command=self.Exit).place(x=0,y=60,anchor="w")
        
        F3 = LabelFrame(self,bd=5,relief=FLAT,bg="light gray")
        F3.place(x=150,y=100,relwidth=1,height=60 )
        lbl_1= Label(F3,text="Dashboard / Hospital",font=("comic sans",15,"italic"),bg="light gray")
        lbl_1.place(x=0,y=10)

        btn_User = Button(F3, bd=5, relief=GROOVE, bg="red", fg="white", font=("",15,"bold"), text= "User View",command=self.User_Check)
        btn_User.place(x=1000,y=0)
        home_btn = Button(F3, text="Home",bd=5,relief=GROOVE, font=("",15,"bold"), fg="white", bg="blue", command=self.Home)
        home_btn.place(x=300,y=0)

        self.HID = StringVar()
        self.City = StringVar()
        self.State = StringVar()
        self.postal_code = StringVar()
        self.Building_no = StringVar()
        self.Email = StringVar()
        
        self.FM1 = Frame(self,bd=5,relief=RAISED)
        self.FM1.place(x=430,y=200,width=700,height=430 )



        FM11 =Frame(self.FM1,bd=5,relief=RAISED,bg="yellow")
        FM11.place(x=0,y=0,relwidth=1,height=60 )
        lbl_FM11= Label(FM11,text="Manage Hos Data",font=("times new roman",30,"bold"),fg="black",bg="yellow")
        lbl_FM11.place(x=20,y=0)

        lblID_roll=Label(FM11,text="HID",bg="yellow",font=("times new roman",18,"bold"))
        lblID_roll.place(x=400,y=25,anchor="w")
        txtID_roll=Entry(FM11, width=17, textvariable=self.HID,font=("times new roman",15,"bold"),bd=5,relief=GROOVE,state="readonly")
        txtID_roll.place(x=485,y=25,anchor="w")

        FM12 =Frame(self.FM1,bd=10,relief=SUNKEN,bg="#074463")
        FM12.place(x=0,y=340,relwidth=1,height=80 )
        
        btn_update2 = Button(FM12,relief=GROOVE,width=8, font=("times new roman",18,"bold"),bd=6,text="Update",command=self.add).grid(row=0,column=1,pady=6,padx=50,sticky="nesw")        
        btn_Delete = Button(FM12,relief=GROOVE, width=8,font=("times new roman",18,"bold"),bd=6,text="Delete",command=self.delete).grid(row=0,column=2,pady=6,padx=50,sticky="nesw")
        btn_Clear = Button(FM12,relief=GROOVE, width=8,font=("times new roman",18,"bold"),bd=6,text="Clear",command=self.clear).grid(row=0,column=3,pady=6,padx=50,sticky="nesw")        

        lbl_roll=Label(self.FM1,text="State",font=("times new roman",18,"bold"),bg="#F5F5F5")
        lbl_roll.place(x=0,y=90,anchor="w")
        txt_roll=Entry(self.FM1,  width=17, textvariable=self.State,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.place(x=150,y=90,anchor="w")

        lbl_roll=Label(self.FM1,text="City",bg="#F5F5F5",font=("times new roman",18,"bold"))
        lbl_roll.place(x=0,y=140,anchor="w")
        txt_roll=Entry(self.FM1, width=17,textvariable=self.City, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.place(x=150,y=140,anchor="w")
        
        lbl_roll=Label(self.FM1,text="Buliding No.",bg="#F5F5F5",font=("times new roman",18,"bold"))
        lbl_roll.place(x=0,y=190,anchor="w")
        txt_roll=Entry(self.FM1, width=17,textvariable=self.Building_no, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.place(x=150,y=190,anchor="w")

        lbl_roll=Label(self.FM1,text="Postal Code",bg="#F5F5F5",font=("times new roman",18,"bold"))
        lbl_roll.place(x=0, y=240, anchor="w")
        txt_roll=Entry(self.FM1, width=17,textvariable=self.postal_code, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.place(x=150,y=240,anchor="w")
  
        Donar_lb=Label(self.FM1,text="Email", font=("times new roman",18,"bold"),bg="#F5F5F5")
        Donar_lb.place(x=0, y=290, anchor="w")
        Email=Entry(self.FM1, width=17,textvariable=self.Email, font=("times new roman",15,"bold"),state='readonly')
        Email.place(x=150, y=290, anchor="w")

        with open("Temp1.txt","r+") as file:
            self.read2=str(file.read())
        self.conn=sqlite3.connect("plasma.db")
        self.c = self.conn.cursor()
        # c.execute("SELECT Email from user WHERE UID="+str(c))
        self.cmd = "SELECT Email from hos WHERE HID = '" +self.read2 + "'"

        self.c.execute(self.cmd)
        self.data=self.c.fetchall()
        if self.data:
            for i in self.data:
                    a=str(i[0])
        self.c.execute(self.cmd)
        self.Email.set(a)
            

        self.HID.set(self.read2)
        self.clock()
    
    def add(self):

        if self.City.get()=="" and self.State.get()=="" and self.Email.get()=="" and self.postal_code.get()=="" and self.Building_no.get()== "" :
            return messagebox.showerror("Error!","All Feilds Required")
        
        if self.State.get()=='':
            return messagebox.showinfo('Error','Enter a State')
        
        if self.City.get()=='':
            return messagebox.showinfo('Error','Enter a City')

        if self.postal_code.get()=='':
            return messagebox.showinfo('Error','Enter a Postal Code')

        if self.Building_no.get()=='':
            return messagebox.showinfo('Error','Building Number')
        
        else:
            try:    
                self.conn=sqlite3.connect("plasma.db")
                self.c=self.conn.cursor()
                self.c.execute("CREATE TABLE IF NOT EXISTS hos_details(HID TEXT PRIMARY KEY ,City TEXT, State TEXT  , Postal_Code TEXT, Building_No )")
                self.c.execute("INSERT INTO hos_details (HID, City, State, Postal_Code, Building_no) VALUES (?,?,?,?,?)",(self.HID.get(),self.City.get(),str(self.State.get()),self.postal_code.get(), self.Building_no.get()))
                messagebox.showinfo("Info"," Data Updated")
                self.conn.commit()
                self.conn.close()
                self.clear()
            except Exception:
                return messagebox.showerror("Error!!","Somthing went wrong not able to add data try again ")
            self.clear()        
    
    def delete(self):
        try:
            self.conn=sqlite3.connect("plasma.db")
            self.c=self.conn.cursor()
            self.c.execute("SELECT * from hos WHERE HID= '"+str(self.HID.get()+ "'"))
            self.data=self.c.fetchall()
            if self.data:
                self.c.execute("DELETE FROM hos_details WHERE HID = '" +str(self.HID.get()+ "'"))
                self.c.execute("DELETE FROM hos WHERE HID = '" +str(self.HID.get()+ "'"))
                self.c.execute("DELETE FROM Blood_Bank WHERE HID = '" +str(self.HID.get()+ "'"))
                self.conn.commit()
                self.conn.close()
                messagebox.showinfo("Info","Succesfully Deleted")
                self.clear()
            else:
                messagebox.showinfo("Info","Data not Exist")
                self.destroy()
                root=Tk()
                clas=H_login(root)
                win1.new=clas

        except sqlite3.Error as error:
            messagebox.showerror("error","Failed to update sqlite table")

    def clear(self):
        with open("Temp1.txt","r+") as file:
            self.read2=str(file.read())
        self.conn=sqlite3.connect("plasma.db")
        self.c = self.conn.cursor()
        # c.execute("SELECT Email from user WHERE UID="+str(c))
        self.cmd = "SELECT Email from hos WHERE HID = '" +self.read2 + "'"

        self.c.execute(self.cmd)
        self.data=self.c.fetchall()
        if self.data:
            for i in self.data:
                    a=str(i[0])
        self.c.execute(self.cmd)
        self.Email.set(a)
            

        self.HID.set(self.read2)
        self.City.set("")
        self.Email.set(a)
        self.State.set("")
        self.postal_code.set("")
        self.Building_no.set("")

          
    def Home(self):
        self.destroy()
        Hospital_Page().mainloop()

    def U_det(self):
        self.destroy()
        H_Manage().mainloop()
        
    def Blood_Donar(self):
        self.destroy()
        Bload_Search_hos().mainloop()
        
    
    def Blood_Bank(self):
        self.destroy()
        Bload_Bank_hos().mainloop()

    def Plasma(self):
        self.destroy()
        Plasma_Search_hos().mainloop()    

    def User_Check(self):
        self.destroy()
        User_Check_class().mainloop()

    def Exit(self):
        self.destroy()

    
    def logout(self):
        self.read1=StringVar()
        with open("Temp1.txt","r+") as file:
            self.read1=file.read()
            file.truncate()
    
        a=messagebox.askyesnocancel("Hey","Confirm again for Logout")
        if a>0:
            now = datetime.now()
            self.Time2=now.strftime('%H:%M:%S')

            self.today1= now.strftime("%d/%m/%Y")
            self.destroy()
            self.conn=sqlite3.connect("plasma.db")
            self.c=self.conn.cursor()
            y="UPDATE Last_Login_hospital set time=\""+str(self.Time2)+"\", date=\""+str(self.today1)+"\" where HID =\""+str(self.read1)+"\""
            #print(y)
            self.c.execute(y)
            self.conn.commit()
            root=Tk()
            clas=H_login(root)            
        else:
            pass



    def change_pasw(self):  
        self.root2 = Toplevel(self)  # Child Window "Tk() can Also be use here"
        self.root2.title("Change Password")
        self.root2.geometry("750x370+350+150")
        self.root2.configure(bg="black")
        photo1 = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
        self.root2.iconphoto(False, photo1)
        self.root2.grab_set() 
        self.root2.resizable(False, False)

        title_child = Label(self.root2, text="Reset Password", bg="#152238", fg="white",compound=LEFT, font=("Goudy Old Style", 48, "bold"), anchor="w").place(x=0, y=0, relwidth=1)
        
        phone_lbl = Label(self.root2, text="Phone No.", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=120)
        self.phone_ = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.phone_.place(x=260, y=120)
        
        current_lbl = Label(self.root2, text="Current Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=170)
        self.current_ = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.current_.place(x=260, y=170)
        
        pass_lbl = Label(self.root2, text="New Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=220)
        self.pass_ = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.pass_.place(x=260, y=220)
        
        passcon_lbl = Label(self.root2, text="Confirm Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=270)
        self.passcon = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.passcon.place(x=260, y=270)
        
        Reset_btn = Button(self.root2, text="Reset", font=("times new roman", 18, "bold"), activebackground="blue",activeforeground="white", bg="blue", fg="white", cursor="hand2", command=self.reset)
        Reset_btn.place(x=495, y=310, width=140, height=30) 

      
        
    def reset(self):
        with open("Temp1.txt","r+") as file:
            self.read1=file.read()
        #print(self.read1)
        self.passw = self.pass_.get()
        self.passconw = self.passcon.get()
        self.current2_=self.current_.get()
        self.phone_2=self.phone_.get()
        
        self.conn = sqlite3.connect("plasma.db")
        self.c = self.conn.cursor()
        self.c.execute("SELECT Password from hos WHERE Phone_No=" +self.phone_2)
        self.data = self.c.fetchall()
        if self.data==[]:
            return messagebox.showerror("Error"," Current Password not Matched to Your mail Id" , parent=self.root2)
        else:
            for i in self.data:
                    #print(i[0])
                    self.c.execute("SELECT Email from hos WHERE Phone_No=" +self.phone_2)
                    self.data = self.c.fetchall()
                    for j in self.data:
                        a=str(j[0])
                    if i[0] == self.current2_:
                        self.OTP_Forget=str(random.randint(100000,999999))
                        send = smtplib.SMTP("smtp.gmail.com", 587)  # Create session for Gmail
                        send.starttls()  # transport layer

                        msg = EmailMessage()
                        msg["Subject"] = "OTP"
                        msg["From"] = "aj147ps@gmail.com"
                        msg["To"] = a
                        msg.set_content("Hi! your OTP for reset password: "+"\'"+str(self.OTP_Forget)+"\'")        
                            
                        try:
                            send.login("aj147ps@gmail.com","xcavbfayvnthixwy")
                        except smtplib.SMTPAuthenticationError:
                            messagebox.showerror("Error","Error Occur Otp Not")    

                        try:
                            try:
                                try:                                
                                    
                                    send.send_message(msg)
                                    messagebox.showinfo("Mailed","OTP Sent to Your Mail Id") 
                                    self.root2.destroy()
                                    self.root3 = Toplevel(self)  # Child Window "Tk() can Also be use here"
                                    self.root3.title("Verification")
                                    self.root3.geometry("750x320+350+150")
                                    self.root3.configure(bg="black")
                                    photo4 = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
                                    self.root3.iconphoto(False, photo4)
                                    self.root3.grab_set() 
                                    self.root3.resizable(False, False)
                                
                                    title_child = Label(self.root3, text="Reset Password", bg="#152238", fg="white",compound=LEFT, font=("Goudy Old Style", 48, "bold"), anchor="w").place(x=0, y=0, relwidth=1)
                                    otp_lbl = Label(self.root3, text="Enter OTP", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=120)
                                    self.otp_ = Entry(self.root3, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
                                    self.otp_.place(x=260, y=120)
                                    
                                    Reset_btn = Button(self.root3, text="Reset", font=("times new roman", 18, "bold"), activebackground="blue",activeforeground="white", bg="blue", fg="white", cursor="hand2", command=self.reset1)
                                    Reset_btn.place(x=495, y=260, width=140, height=30) 
                        
                                except smtplib.SMTPRecipientsRefused:
                                    messagebox.showerror("Mailed","Mail Not Sent")
                            except smtplib.SMTPException:
                                messagebox.showerror("Mailed","Mail Not Sent")
                        except smtplib.SMTPConnectError:
                            messagebox.showerror("Error","Connection Error")
                    else:
                        return messagebox.showerror("Error","Contact No. have not given Mail Id")

    def reset1(self):
        self.one_ = self.otp_.get()
        #print(self.one_)
        if str(self.one_)==str(self.OTP_Forget):
            if len(str(self.passw))>=8:
                if self.passw == self.passconw:
                    y= f"UPDATE hos SET Password = {str(self.passw)} WHERE Phone_No = {str(self.phone_2)}"
                    self.c.execute(str(y))
                    self.conn.commit()
                    self.conn.close()
                    self.OTP_Forget=""
                    messagebox.showinfo("Info", "Successfully Changed!!", parent=self.root3)
                    self.root3.destroy()                    
                else:
                    return messagebox.showerror("Error", "Password Cann't Changed  password  and confirm password not match!!", parent=self.root3)
            else:
                return messagebox.showerror("Error", "Password should be of minimum 8 Characters", parent=self.root3)
        else:
            return messagebox.showerror("Error", "OTP Entered is Wrong", parent=self.root3)

    def clock(self):

        self.h = str(time.strftime("%H"))
        self.m = str(time.strftime("%M"))
        self.s = str(time.strftime("%S"))

        if int(self.h)<15 and int(self.m)>0:
            self.lbl_abv.config(text="PM")

        if int(self.h)>=15 and int(self.h)<20 and int(self.m)>0:
            self.lbl_abv.config(text="PM")
        
        if int(self.h)>=20 and int(self.h)<24 and int(self.m)>0:
            self.lbl_abv.config(text="PM")

        if int(self.h)>12 and int(self.h)<15 and int(self.m)>0:
            self.lbl_abv.config(text="PM")

        if int(self.h)>0 and int(self.h)<12 and int(self.m)>0:
            self.lbl_abv.config(text="AM")

         
        self.lbl_hr.config(text = self.h)
        self.lbl_min.config(text = self.m)
        self.lbl_sec.config(text = self.s)
        self.lbl_hr.after(200,self.clock)

class Bload_Bank_hos(Tk):
    def __init__(self,*arg):       # Constructors
        Tk.__init__(self,*arg)
        photo = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
        self.iconphoto(False, photo)

        self.title("Plasma Finder".center(420))  # title for Window 
        self.configure(background = "black")  # background color for window 
        self.geometry("1360x768+0+0")
        photo = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
        self.iconphoto(False, photo)

        bg_color ="#FFFFF6"
        
     
        self.bg_icon = ImageTk.PhotoImage(file="Pics\\1 (1).jpg")
        bg_lbl = Label(self, image = self.bg_icon).pack(fill=Y) # we put image into our window
        
        self.hos_icon=ImageTk.PhotoImage(file="Pics\\1 (2) copy.jpg")
                
        
        F1 = LabelFrame(self,bd=10,relief=GROOVE,bg=bg_color)
        F1.place(x=0,relwidth=1,height=100 )

        lbl = Label(F1,text="Plasma Finder", compound=LEFT, image=self.hos_icon,bg=bg_color, font= ("times new roman",20,"bold")).place(x=0, y=5)

        self.lbl_hr = Label(F1,text="12" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_hr.place(x=890, y=40)
        
        self.lbl_COLON = Label(F1,text=":" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_COLON.place(x=915, y=40)
       
       
        self.lbl_min = Label(F1,text="12" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_min.place(x=925, y=40)
       
        self.lbl_COLON = Label(F1,text=":" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_COLON.place(x=950, y=40)
       
        self.lbl_sec = Label(F1,text="12" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_sec.place(x=960, y=40)
        

        self.lbl_abv = Label(F1,text="AM" , font = ("times new roman", 13,"bold"),bg=bg_color)
        self.lbl_abv.place(x=985, y=43)
       
       
        self.font=("times new roman",20,"bold")
        self.calendar = []

        ntpClient = ntplib.NTPClient()
        response = ntpClient.request('pool.ntp.org')
        a=ctime(response.tx_time)
        b=[a[i:i+10] for i in range(0, len(a), 10)]
        c=str(b[0])
        d=str(b[2])

        self.date = Label(F1, font=("times new roman",15,"bold"), text=c, bg=bg_color)
        self.date.place(x=740, y=40)

        self.date1 = Label(F1, font=("times new roman",15,"bold"), text=d,bg=bg_color)
        self.date1.place(x=840, y=40)

        
        self.date2 = Label(F1, font=("times new roman",15,"bold"), text="Calendar",bg=bg_color)
        self.date2.place(x=750, y=5)

        self.calendar.append(DateEntry(F1, font=("times new roman",15,"bold"), locale='en_GB',state="readonly",width=10))
        self.calendar[-1].place(x=855, y=20, anchor="w")

        
        btn_changepass = Button(F1, text="ChangePassword",relief=RAISED,width =15,height=1, font=("times new roman",14,"bold"),bg="red",foreground="white",command=self.change_pasw).place(x=1145,y=20,anchor="w")
        btn_logout = Button(F1, text="Logout",relief=RAISED,width =15,height=1, font=("times new roman",14,"bold"),bg="light green",foreground="black", command=self.logout).place(x=1145,y=60,anchor="w")

        lbl2 = Label(F1,bg=bg_color)
        lbl2.place(x=25,y=10)

        F2 = LabelFrame(self,bd=10,relief=GROOVE,bg=bg_color)
        F2.place(x=0,y=100,width=150,height=670 )

        F21 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F21.place(x=0,y=0,width=130,height=133 )
        
        F22 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F22.place(x=0,y=133,width=130,height=133)
        
        F23 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F23.place(x=0,y=266,width=130,height=133 )
        
        F24 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F24.place(x=0,y=399,width=130,height=133)
        
        F25 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F25.place(x=0,y=532,width=130,height=133)

        self.U_mange = PhotoImage(file="Pics\\User_Det.png")
        self.donor_b = ImageTk.PhotoImage(file="Pics\\Blood Donar.jpg")
        self.b_bank = ImageTk.PhotoImage(file="Pics\Blood Bank Search.jpg")    
        self.p_donar = ImageTk.PhotoImage(file="Pics\Plasma.png")
        self.exit = ImageTk.PhotoImage(file="Pics\\Exit.jpg")
        
        btn_U_det = Button(F21,image= self.U_mange,bg=bg_color,relief=RAISED,width =115,height=120,command=self.U_det).place(x=0,y=60,anchor="w")
        btn_blood_donor = Button(F22,image= self.donor_b,bg=bg_color,relief=RAISED,width =115,height=120,command=self.Blood_Donar ).place(x=0,y=60,anchor="w")
        btn_blood_bank = Button(F23,relief=RAISED,bg=bg_color,image=self.b_bank,width =115,height=120,command=self.Blood_Bank ).place(x=0,y=60,anchor="w")
        btn_Plasma = Button(F24,relief=RAISED,image=self.p_donar,bg=bg_color,width =115,height=120, command=self.Plasma).place(x=0,y=60,anchor="w")
        btn_Exit = Button(F25,relief=RAISED,bg=bg_color,image=self.exit,width =115,height=120, command=self.Exit).place(x=0,y=60,anchor="w")
        
        F3 = LabelFrame(self,bd=5,relief=FLAT,bg="light gray")
        F3.place(x=150,y=100,relwidth=1,height=60 )
        lbl_1= Label(F3,text="Dashboard / Hospital",font=("comic sans",15,"italic"),bg="light gray")
        lbl_1.place(x=0,y=10)

        btn_User = Button(F3, bd=5, relief=GROOVE, bg="red", fg="white", font=("",15,"bold"), text= "User View",command=self.User_Check)
        btn_User.place(x=1000,y=0)
        home_btn = Button(F3, text="Home",bd=5,relief=GROOVE, font=("",15,"bold"), fg="white", bg="blue", command=self.Home)
        home_btn.place(x=300,y=0)




        self.F4 =Frame(self,bd=10,relief=SUNKEN,bg="white")
        self.F4.place(x=180,y=200,width=1130,height=500 )
        
        self.searchby = StringVar()
        self.searchby1 = StringVar()

        lb_search=Label(self,text="Search By", font=("times new roman",15,"bold"))
        lb_search.place(x=180 ,y=185, anchor="w")
        combo_search=ttk.Combobox(self, textvariable=self.searchby,width=17, font=("times new roman",16,"bold"),state='readonly')
        combo_search['values']=("HID")
        combo_search.place(x=273, y=185, anchor="w")
        
        search=Entry(self, textvariable=self.searchby1,width=17,bd=5,relief=GROOVE, font=("times new roman",16,"bold"))
        search.place(x=490, y=185, anchor="w")

        lb_search_btn=Button(self,text="Search By", bd=6, relief=GROOVE,command=self.search,font=("times new roman",15,"bold"),fg="yellow",bg="dark blue")
        lb_search_btn.place(x=695 ,y=183, height=30,anchor="w")
        
        lb_search_btn=Button(self,text="Search All", bd=6, relief=GROOVE,command=self.search1,font=("times new roman",15,"bold"),fg="yellow",bg="dark blue")
        lb_search_btn.place(x=835 ,y=183, height=30,anchor="w")
        
        lb_search_btn=Button(self,text="Clear", bd=6, relief=GROOVE,command=self.clear1,font=("times new roman",15,"bold"),fg="yellow",bg="dark blue")
        lb_search_btn.place(x=1110 ,y=183, height=30, width=200,anchor="w")

        Table_Frame=Frame(self.F4,bd=4, relief=RIDGE)
        Table_Frame.place(x=15,y=0,width=1080,height=480)

        scroll_x=Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame, orient=VERTICAL)
        scroll_x1=Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y1=Scrollbar(Table_Frame, orient=VERTICAL)
        self.Bloold_Bank_table=ttk.Treeview(Table_Frame,columns=("HID" ,"A+"  , "B+"  , "AB+", "O+"  , "A-"  , "B-" , "AB-"  , "O-"   ),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Bloold_Bank_table.xview)
        scroll_y.config(command=self.Bloold_Bank_table.yview)

        
        self.Bloold_Bank_table.heading("HID", text="HID")
        self.Bloold_Bank_table.heading("A+", text="A+")
        self.Bloold_Bank_table.heading("B+", text="B+")
        self.Bloold_Bank_table.heading("AB+", text="AB+")
        self.Bloold_Bank_table.heading("O+", text="O+")
        self.Bloold_Bank_table.heading("A-", text="A-")
        self.Bloold_Bank_table.heading("B-", text="B-")
        self.Bloold_Bank_table.heading("AB-", text="AB-")
        self.Bloold_Bank_table.heading("O-", text="O-")
    
    
        self.Bloold_Bank_table['show']='headings'
        self.fetch_data()
        self.clock()
          
    def Home(self):
        self.destroy()
        Hospital_Page().mainloop()

    def U_det(self):
        self.destroy()
        H_Manage().mainloop()
        
    def Blood_Donar(self):
        self.destroy()
        Bload_Search_hos().mainloop()
        
    
    def Blood_Bank(self):
        self.destroy()
        Bload_Bank_hos().mainloop()

    def Plasma(self):
        self.destroy()
        Plasma_Search_hos().mainloop()    

    def User_Check(self):
        self.destroy()
        User_Check_class().mainloop()

    def Exit(self):
        self.destroy()

        
    def search(self):
        
        if self.searchby.get()=="" and self.searchby1.get()=="":
            return messagebox.showwarning("Warning","Fields should be filled")
        if self.searchby.get()=="" :
            return messagebox.showwarning("Warning","Shearch By Option Should be filled")
        if self.searchby1.get()=="":
            return messagebox.showwarning("Warning","Search box should be filled")
        
        else:
            if self.searchby.get()=="HID":
                try:
                    self.Bloold_Bank_table.column("HID", width=150)
                    self.Bloold_Bank_table.column("A+", width=100)
                    self.Bloold_Bank_table.column("B+", width=100)
                    self.Bloold_Bank_table.column("AB+", width=100)
                    self.Bloold_Bank_table.column("O+", width=100)
                    self.Bloold_Bank_table.column("A-", width=100)
                    self.Bloold_Bank_table.column("B-", width=100)
                    self.Bloold_Bank_table.column("AB-", width=100)
                    self.Bloold_Bank_table.column("O-", width=100)


                    self.Bloold_Bank_table['show']='headings'

                    self.Bloold_Bank_table.pack(fill=BOTH,expand=1)
                    self.Bloold_Bank_table.bind("<ButtonRelease-1>",self.getcursor)
                    self.conn=sqlite3.connect("plasma.db")
                    self.c=self.conn.cursor()
                    self.c.execute("select * from Blood_Bank where HID = '"+ self.searchby1.get()+"'")
                    rows=self.c.fetchall()
                    if len(rows)!=0:
                            self.Bloold_Bank_table.delete(*self.Bloold_Bank_table.get_children())
                            for row in rows:
                                    self.Bloold_Bank_table.insert('',END,values=row)
                            self.conn.commit()
                            self.conn.close()
                    else:
                        return messagebox.showerror("Error","HID No Not Exist")        
                except Exception:
                    return messagebox.showerror("Error", "Something Wrong")
                self.conn.close()
            else:
                return messagebox.showerror("Error", "No Such Option")
            
    def search1(self):
        self.Bloold_Bank_table.column("HID", width=150)
        self.Bloold_Bank_table.column("A+", width=100)
        self.Bloold_Bank_table.column("B+", width=100)
        self.Bloold_Bank_table.column("AB+", width=100)
        self.Bloold_Bank_table.column("O+", width=100)
        self.Bloold_Bank_table.column("A-", width=100)
        self.Bloold_Bank_table.column("B-", width=100)
        self.Bloold_Bank_table.column("AB-", width=100)
        self.Bloold_Bank_table.column("O-", width=100)
    
    
        self.Bloold_Bank_table['show']='headings'
    
        self.Bloold_Bank_table.pack(fill=BOTH,expand=1)
        self.Bloold_Bank_table.bind("<ButtonRelease-1>",self.getcursor)
        self.fetch_data()

    def fetch_data(self):
        self.conn=sqlite3.connect("plasma.db")
        self.c=self.conn.cursor()
        self.c.execute("select * from Blood_Bank")
        rows=self.c.fetchall()
        if len(rows)!=0:
                self.Bloold_Bank_table.delete(*self.Bloold_Bank_table.get_children())
                for row in rows:
                        self.Bloold_Bank_table.insert('',END,values=row)
                self.conn.commit()
        self.conn.close()

    def getcursor(self,ev):
        cursor_row=self.Bloold_Bank_table.focus()
        Content=self.Bloold_Bank_table.item(cursor_row)
        row=Content['values']

        self.Bloold_Bank_table.set(row[0])
        self.Bloold_Bank_table.set(row[1])
        self.Bloold_Bank_table.set(row[2])
        self.Bloold_Bank_table.set(row[3])
        self.Bloold_Bank_table.set(row[4])
        self.Bloold_Bank_table.set(row[5])
        self.Bloold_Bank_table.set(row[6])        
        self.Bloold_Bank_table.set(row[7])
        self.Bloold_Bank_table.set(row[8])
        
    def clear1(self):
        self.Bloold_Bank_table.delete(*self.Bloold_Bank_table.get_children())
        self.searchby.set("")
        self.searchby1.set("")

    
    
    def logout(self):
        self.read1=StringVar()
        with open("Temp1.txt","r+") as file:
            self.read1=file.read()
            file.truncate()
    
        a=messagebox.askyesnocancel("Hey","Confirm again for Logout")
        if a>0:
            now = datetime.now()
            self.Time2=now.strftime('%H:%M:%S')

            self.today1= now.strftime("%d/%m/%Y")
            self.destroy()
            self.conn=sqlite3.connect("plasma.db")
            self.c=self.conn.cursor()
            y="UPDATE Last_Login_hospital set time=\""+str(self.Time2)+"\", date=\""+str(self.today1)+"\" where HID =\""+str(self.read1)+"\""
            #print(y)
            self.c.execute(y)
            self.conn.commit()
            root=Tk()
            clas=H_login(root)            
        else:
            pass



    def change_pasw(self):  
        self.root2 = Toplevel(self)  # Child Window "Tk() can Also be use here"
        self.root2.title("Change Password")
        self.root2.geometry("750x370+350+150")
        self.root2.configure(bg="black")
        photo1 = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
        self.root2.iconphoto(False, photo1)
        self.root2.grab_set() 
        self.root2.resizable(False, False)

        title_child = Label(self.root2, text="Reset Password", bg="#152238", fg="white",compound=LEFT, font=("Goudy Old Style", 48, "bold"), anchor="w").place(x=0, y=0, relwidth=1)
        
        phone_lbl = Label(self.root2, text="Phone No.", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=120)
        self.phone_ = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.phone_.place(x=260, y=120)
        
        current_lbl = Label(self.root2, text="Current Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=170)
        self.current_ = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.current_.place(x=260, y=170)
        
        pass_lbl = Label(self.root2, text="New Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=220)
        self.pass_ = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.pass_.place(x=260, y=220)
        
        passcon_lbl = Label(self.root2, text="Confirm Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=270)
        self.passcon = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.passcon.place(x=260, y=270)
        
        Reset_btn = Button(self.root2, text="Reset", font=("times new roman", 18, "bold"), activebackground="blue",activeforeground="white", bg="blue", fg="white", cursor="hand2", command=self.reset)
        Reset_btn.place(x=495, y=310, width=140, height=30) 

      
        
    def reset(self):
        with open("Temp1.txt","r+") as file:
            self.read1=file.read()
        #print(self.read1)
        self.passw = self.pass_.get()
        self.passconw = self.passcon.get()
        self.current2_=self.current_.get()
        self.phone_2=self.phone_.get()
        
        self.conn = sqlite3.connect("plasma.db")
        self.c = self.conn.cursor()
        self.c.execute("SELECT Password from hos WHERE Phone_No=" +self.phone_2)
        self.data = self.c.fetchall()
        if self.data==[]:
            return messagebox.showerror("Error"," Current Password not Matched to Your mail Id" , parent=self.root2)
        else:
            for i in self.data:
                    #print(i[0])
                    self.c.execute("SELECT Email from hos WHERE Phone_No=" +self.phone_2)
                    self.data = self.c.fetchall()
                    for j in self.data:
                        a=str(j[0])
                    if i[0] == self.current2_:
                        self.OTP_Forget=str(random.randint(100000,999999))
                        send = smtplib.SMTP("smtp.gmail.com", 587)  # Create session for Gmail
                        send.starttls()  # transport layer

                        msg = EmailMessage()
                        msg["Subject"] = "OTP"
                        msg["From"] = "aj147ps@gmail.com"
                        msg["To"] = a
                        msg.set_content("Hi! your OTP for reset password: "+"\'"+str(self.OTP_Forget)+"\'")        
                            
                        try:
                            send.login("aj147ps@gmail.com","xcavbfayvnthixwy")
                        except smtplib.SMTPAuthenticationError:
                            messagebox.showerror("Error","Error Occur Otp Not")    

                        try:
                            try:
                                try:                                
                                    
                                    send.send_message(msg)
                                    messagebox.showinfo("Mailed","OTP Sent to Your Mail Id") 
                                    self.root2.destroy()
                                    self.root3 = Toplevel(self)  # Child Window "Tk() can Also be use here"
                                    self.root3.title("Verification")
                                    self.root3.geometry("750x320+350+150")
                                    self.root3.configure(bg="black")
                                    photo4 = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
                                    self.root3.iconphoto(False, photo4)
                                    self.root3.grab_set() 
                                    self.root3.resizable(False, False)
                                
                                    title_child = Label(self.root3, text="Reset Password", bg="#152238", fg="white",compound=LEFT, font=("Goudy Old Style", 48, "bold"), anchor="w").place(x=0, y=0, relwidth=1)
                                    otp_lbl = Label(self.root3, text="Enter OTP", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=120)
                                    self.otp_ = Entry(self.root3, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
                                    self.otp_.place(x=260, y=120)
                                    
                                    Reset_btn = Button(self.root3, text="Reset", font=("times new roman", 18, "bold"), activebackground="blue",activeforeground="white", bg="blue", fg="white", cursor="hand2", command=self.reset1)
                                    Reset_btn.place(x=495, y=260, width=140, height=30) 
                        
                                except smtplib.SMTPRecipientsRefused:
                                    messagebox.showerror("Mailed","Mail Not Sent")
                            except smtplib.SMTPException:
                                messagebox.showerror("Mailed","Mail Not Sent")
                        except smtplib.SMTPConnectError:
                            messagebox.showerror("Error","Connection Error")
                    else:
                        return messagebox.showerror("Error","Contact No. have not given Mail Id")

    def reset1(self):
        self.one_ = self.otp_.get()
        #print(self.one_)
        if str(self.one_)==str(self.OTP_Forget):
            if len(str(self.passw))>=8:
                if self.passw == self.passconw:
                    y= f"UPDATE hos SET Password = {str(self.passw)} WHERE Phone_No = {str(self.phone_2)}"
                    self.c.execute(str(y))
                    self.conn.commit()
                    self.conn.close()
                    self.OTP_Forget=""
                    messagebox.showinfo("Info", "Successfully Changed!!", parent=self.root3)
                    self.root3.destroy()                    
                else:
                    return messagebox.showerror("Error", "Password Cann't Changed  password  and confirm password not match!!", parent=self.root3)
            else:
                return messagebox.showerror("Error", "Password should be of minimum 8 Characters", parent=self.root3)
        else:
            return messagebox.showerror("Error", "OTP Entered is Wrong", parent=self.root3)

    def clock(self):

        self.h = str(time.strftime("%H"))
        self.m = str(time.strftime("%M"))
        self.s = str(time.strftime("%S"))

        if int(self.h)<15 and int(self.m)>0:
            self.lbl_abv.config(text="PM")

        if int(self.h)>=15 and int(self.h)<20 and int(self.m)>0:
            self.lbl_abv.config(text="PM")
        
        if int(self.h)>=20 and int(self.h)<24 and int(self.m)>0:
            self.lbl_abv.config(text="PM")

        if int(self.h)>12 and int(self.h)<15 and int(self.m)>0:
            self.lbl_abv.config(text="PM")

        if int(self.h)>0 and int(self.h)<12 and int(self.m)>0:
            self.lbl_abv.config(text="AM")

         
        self.lbl_hr.config(text = self.h)
        self.lbl_min.config(text = self.m)
        self.lbl_sec.config(text = self.s)
        self.lbl_hr.after(200,self.clock)

class Bload_Search_hos(Tk):
    def __init__(self,*arg):       # Constructors
        Tk.__init__(self,*arg)
        photo = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
        self.iconphoto(False, photo)

        self.title("Plasma Finder".center(420))  # title for Window 
        self.configure(background = "black")  # background color for window 
        self.geometry("1360x768+0+0")
        photo = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
        self.iconphoto(False, photo)

        bg_color ="#FFFFF6"
        
     
        self.bg_icon = ImageTk.PhotoImage(file="Pics\\1 (1).jpg")
        bg_lbl = Label(self, image = self.bg_icon).pack(fill=Y) # we put image into our window
        
        self.hos_icon=ImageTk.PhotoImage(file="Pics\\1 (2) copy.jpg")
                
        
        F1 = LabelFrame(self,bd=10,relief=GROOVE,bg=bg_color)
        F1.place(x=0,relwidth=1,height=100 )

        lbl = Label(F1,text="Plasma Finder", compound=LEFT, image=self.hos_icon,bg=bg_color, font= ("times new roman",20,"bold")).place(x=0, y=5)

        self.lbl_hr = Label(F1,text="12" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_hr.place(x=890, y=40)
        
        self.lbl_COLON = Label(F1,text=":" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_COLON.place(x=915, y=40)
       
       
        self.lbl_min = Label(F1,text="12" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_min.place(x=925, y=40)
       
        self.lbl_COLON = Label(F1,text=":" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_COLON.place(x=950, y=40)
       
        self.lbl_sec = Label(F1,text="12" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_sec.place(x=960, y=40)
        

        self.lbl_abv = Label(F1,text="AM" , font = ("times new roman", 13,"bold"),bg=bg_color)
        self.lbl_abv.place(x=985, y=43)
       
       
        self.font=("times new roman",20,"bold")
        self.calendar = []

        ntpClient = ntplib.NTPClient()
        response = ntpClient.request('pool.ntp.org')
        a=ctime(response.tx_time)
        b=[a[i:i+10] for i in range(0, len(a), 10)]
        c=str(b[0])
        d=str(b[2])

        self.date = Label(F1, font=("times new roman",15,"bold"), text=c, bg=bg_color)
        self.date.place(x=740, y=40)

        self.date1 = Label(F1, font=("times new roman",15,"bold"), text=d,bg=bg_color)
        self.date1.place(x=840, y=40)

        
        self.date2 = Label(F1, font=("times new roman",15,"bold"), text="Calendar",bg=bg_color)
        self.date2.place(x=750, y=5)

        self.calendar.append(DateEntry(F1, font=("times new roman",15,"bold"), locale='en_GB',state="readonly",width=10))
        self.calendar[-1].place(x=855, y=20, anchor="w")

        
        btn_changepass = Button(F1, text="ChangePassword",relief=RAISED,width =15,height=1, font=("times new roman",14,"bold"),bg="red",foreground="white",command=self.change_pasw).place(x=1145,y=20,anchor="w")
        btn_logout = Button(F1, text="Logout",relief=RAISED,width =15,height=1, font=("times new roman",14,"bold"),bg="light green",foreground="black", command=self.logout).place(x=1145,y=60,anchor="w")

        lbl2 = Label(F1,bg=bg_color)
        lbl2.place(x=25,y=10)

        F2 = LabelFrame(self,bd=10,relief=GROOVE,bg=bg_color)
        F2.place(x=0,y=100,width=150,height=670 )

        F21 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F21.place(x=0,y=0,width=130,height=133 )
        
        F22 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F22.place(x=0,y=133,width=130,height=133)
        
        F23 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F23.place(x=0,y=266,width=130,height=133 )
        
        F24 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F24.place(x=0,y=399,width=130,height=133)
        
        F25 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F25.place(x=0,y=532,width=130,height=133)

        self.U_mange = PhotoImage(file="Pics\\User_Det.png")
        self.donor_b = ImageTk.PhotoImage(file="Pics\\Blood Donar.jpg")
        self.b_bank = ImageTk.PhotoImage(file="Pics\Blood Bank Search.jpg")    
        self.p_donar = ImageTk.PhotoImage(file="Pics\Plasma.png")
        self.exit = ImageTk.PhotoImage(file="Pics\\Exit.jpg")
        
        btn_U_det = Button(F21,image= self.U_mange,bg=bg_color,relief=RAISED,width =115,height=120,command=self.U_det).place(x=0,y=60,anchor="w")
        btn_blood_donor = Button(F22,image= self.donor_b,bg=bg_color,relief=RAISED,width =115,height=120,command=self.Blood_Donar ).place(x=0,y=60,anchor="w")
        btn_blood_bank = Button(F23,relief=RAISED,bg=bg_color,image=self.b_bank,width =115,height=120,command=self.Blood_Bank ).place(x=0,y=60,anchor="w")
        btn_Plasma = Button(F24,relief=RAISED,image=self.p_donar,bg=bg_color,width =115,height=120, command=self.Plasma).place(x=0,y=60,anchor="w")
        btn_Exit = Button(F25,relief=RAISED,bg=bg_color,image=self.exit,width =115,height=120, command=self.Exit).place(x=0,y=60,anchor="w")

        F3 = LabelFrame(self,bd=5,relief=FLAT,bg="light gray")
        F3.place(x=150,y=100,relwidth=1,height=60 )
        lbl_1= Label(F3,text="Dashboard / Hospital",font=("comic sans",15,"italic"),bg="light gray")
        lbl_1.place(x=0,y=10)

        btn_User = Button(F3, bd=5, relief=GROOVE, bg="red", fg="white", font=("",15,"bold"), text= "User View",command=self.User_Check)
        btn_User.place(x=1000,y=0)
        home_btn = Button(F3, text="Home",bd=5,relief=GROOVE, font=("",15,"bold"), fg="white", bg="blue", command=self.Home)
        home_btn.place(x=300,y=0)

        self.F4 =Frame(self,bd=10,relief=SUNKEN,bg="white")
        self.F4.place(x=180,y=200,width=1130,height=500 )
        
        self.searchby = StringVar()
        self.searchby1 = StringVar()

        lb_search=Label(self,text="Search By", font=("times new roman",15,"bold"))
        lb_search.place(x=180 ,y=185, anchor="w")
        combo_search=ttk.Combobox(self, textvariable=self.searchby,width=17, font=("times new roman",16,"bold"),state='readonly')
        combo_search['values']=("UID","B_Group")
        combo_search.place(x=273, y=185, anchor="w")
        
        search=Entry(self, textvariable=self.searchby1,width=17,bd=5,relief=GROOVE, font=("times new roman",16,"bold"))
        search.place(x=490, y=185, anchor="w")

        lb_search_btn=Button(self,text="Search By", bd=6, relief=GROOVE,command=self.search,font=("times new roman",15,"bold"),fg="yellow",bg="dark blue")
        lb_search_btn.place(x=695 ,y=183, height=30,anchor="w")
        
        lb_search_btn=Button(self,text="Search All", bd=6, relief=GROOVE,command=self.search1,font=("times new roman",15,"bold"),fg="yellow",bg="dark blue")
        lb_search_btn.place(x=835 ,y=183, height=30,anchor="w")
        
        lb_search_btn=Button(self,text="Clear", bd=6, relief=GROOVE,command=self.clear1,font=("times new roman",15,"bold"),fg="yellow",bg="dark blue")
        lb_search_btn.place(x=1110 ,y=183, height=30, width=200,anchor="w")

        Table_Frame=Frame(self.F4,bd=4, relief=RIDGE)
        Table_Frame.place(x=15,y=0,width=1080,height=480)

        scroll_x=Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame, orient=VERTICAL)
        scroll_x1=Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y1=Scrollbar(Table_Frame, orient=VERTICAL)
        self.Bloold_Bank_table=ttk.Treeview(Table_Frame,columns=("UID" , "B_Group"  , "Phone_No"   ),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Bloold_Bank_table.xview)
        scroll_y.config(command=self.Bloold_Bank_table.yview)

        
        self.Bloold_Bank_table.heading("UID", text="UID")
        self.Bloold_Bank_table.heading("B_Group", text="B_Group")
        self.Bloold_Bank_table.heading("Phone_No", text="Phone_No")

        self.Bloold_Bank_table.column("UID", width=150)
        self.Bloold_Bank_table.column("B_Group", width=150)
        self.Bloold_Bank_table.column("Phone_No", width=150)
        
    
        self.Bloold_Bank_table['show']='headings'
        
        self.fetch_data()
        self.clock()
          
    def Home(self):
        self.destroy()
        Hospital_Page().mainloop()

    def U_det(self):
        self.destroy()
        H_Manage().mainloop()
        
    def Blood_Donar(self):
        self.destroy()
        Bload_Search_hos().mainloop()
        
    
    def Blood_Bank(self):
        self.destroy()
        Bload_Bank_hos().mainloop()

    def Plasma(self):
        self.destroy()
        Plasma_Search_hos().mainloop()    
    
    def User_Check(self):
        self.destroy()
        User_Check_class().mainloop()

    def Exit(self):
        self.destroy()

        
    def search(self):
        
        if self.searchby.get()=="" and self.searchby1.get()=="":
            return messagebox.showwarning("Warning","Fields should be filled")
        if self.searchby.get()=="" :
            return messagebox.showwarning("Warning","Shearch By Option Should be filled")
        if self.searchby1.get()=="":
            return messagebox.showwarning("Warning","Search box should be filled")
        
        else:
            
            if self.searchby.get()=="UID":        
                try:
                    self.Bloold_Bank_table.column("UID", width=150)
                    self.Bloold_Bank_table.column("B_Group", width=150)
                    self.Bloold_Bank_table.column("Phone_No", width=150)
                    
                
                    self.Bloold_Bank_table['show']='headings'
                
                    self.Bloold_Bank_table.pack(fill=BOTH,expand=1)
                    self.Bloold_Bank_table.bind("<ButtonRelease-1>",self.getcursor)
                    self.fetch_data()

                    self.conn=sqlite3.connect("plasma.db")
                    self.c=self.conn.cursor()
                    self.c.execute("select * from Blood_Donor_Approved where UID = '"+ self.searchby1.get()+"'")
                    rows=self.c.fetchall()
                    if len(rows)!=0:
                            self.Bloold_Bank_table.delete(*self.Bloold_Bank_table.get_children())
                            for row in rows:
                                    self.Bloold_Bank_table.insert('',END,values=row)
                            self.conn.commit()
                            self.conn.close()
                    else:
                        return messagebox.showerror("Error","UID No Not Exist")        
                except Exception:
                    return messagebox.showerror("Error", "Something Wrong")
                self.conn.close()
            
            elif self.searchby.get()=="B_Group":
                try:
                    self.Bloold_Bank_table.column("B_Group", width=150)
                    self.Bloold_Bank_table.column("Phone_No", width=150)
                    
                
                    self.Bloold_Bank_table['show']='headings'
                
                    self.Bloold_Bank_table.pack(fill=BOTH,expand=1)
                    self.Bloold_Bank_table.bind("<ButtonRelease-1>",self.getcursor)
                    self.fetch_data()

                    self.conn=sqlite3.connect("plasma.db")
                    self.c=self.conn.cursor()
                    self.c.execute("select * from Blood_Donor_Approved where B_group = '"+ self.searchby1.get()+"'")
                    rows=self.c.fetchall()
                    if len(rows)!=0:
                            self.Bloold_Bank_table.delete(*self.Bloold_Bank_table.get_children())
                            for row in rows:
                                    self.Bloold_Bank_table.insert('',END,values=row)
                            self.conn.commit()
                            self.conn.close()
                    else:
                        return messagebox.showerror("Error","Bloood Group Not Available ")        
                except Exception:
                    return messagebox.showerror("Error", "Something Wrong")
                self.conn.close()

            else:
                return messagebox.showerror("Error", "No Such Option")
            
            
    def search1(self):
        self.Bloold_Bank_table.column("UID", width=150)
        self.Bloold_Bank_table.column("B_Group", width=150)
        self.Bloold_Bank_table.column("Phone_No", width=150)
        
    
        self.Bloold_Bank_table['show']='headings'
    
        self.Bloold_Bank_table.pack(fill=BOTH,expand=1)
        self.Bloold_Bank_table.bind("<ButtonRelease-1>",self.getcursor)
        self.fetch_data()

    def fetch_data(self):
        self.conn=sqlite3.connect("plasma.db")
        self.c=self.conn.cursor()
        self.c.execute("select * from Blood_Donor_Approved")
        rows=self.c.fetchall()
        if len(rows)!=0:
                self.Bloold_Bank_table.delete(*self.Bloold_Bank_table.get_children())
                for row in rows:
                        self.Bloold_Bank_table.insert('',END,values=row)
                self.conn.commit()
        self.conn.close()

    def getcursor(self,ev):
        cursor_row=self.Bloold_Bank_table.focus()
        Content=self.Bloold_Bank_table.item(cursor_row)
        row=Content['values']

        self.Bloold_Bank_table.set(row[0])
        self.Bloold_Bank_table.set(row[1])
        self.Bloold_Bank_table.set(row[2])
        
    def clear1(self):
        self.Bloold_Bank_table.delete(*self.Bloold_Bank_table.get_children())
        self.searchby.set("")
        self.searchby1.set("")

    
    
    def logout(self):
        self.read1=StringVar()
        with open("Temp1.txt","r+") as file:
            self.read1=file.read()
            file.truncate()
    
        a=messagebox.askyesnocancel("Hey","Confirm again for Logout")
        if a>0:
            now = datetime.now()
            self.Time2=now.strftime('%H:%M:%S')

            self.today1= now.strftime("%d/%m/%Y")
            self.destroy()
            self.conn=sqlite3.connect("plasma.db")
            self.c=self.conn.cursor()
            y="UPDATE Last_Login_hospital set time=\""+str(self.Time2)+"\", date=\""+str(self.today1)+"\" where HID =\""+str(self.read1)+"\""
            #print(y)
            self.c.execute(y)
            self.conn.commit()
            root=Tk()
            clas=H_login(root)            
        else:
            pass



    def change_pasw(self):  
        self.root2 = Toplevel(self)  # Child Window "Tk() can Also be use here"
        self.root2.title("Change Password")
        self.root2.geometry("750x370+350+150")
        self.root2.configure(bg="black")
        photo1 = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
        self.root2.iconphoto(False, photo1)
        self.root2.grab_set() 
        self.root2.resizable(False, False)

        title_child = Label(self.root2, text="Reset Password", bg="#152238", fg="white",compound=LEFT, font=("Goudy Old Style", 48, "bold"), anchor="w").place(x=0, y=0, relwidth=1)
        
        phone_lbl = Label(self.root2, text="Phone No.", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=120)
        self.phone_ = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.phone_.place(x=260, y=120)
        
        current_lbl = Label(self.root2, text="Current Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=170)
        self.current_ = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.current_.place(x=260, y=170)
        
        pass_lbl = Label(self.root2, text="New Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=220)
        self.pass_ = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.pass_.place(x=260, y=220)
        
        passcon_lbl = Label(self.root2, text="Confirm Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=270)
        self.passcon = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.passcon.place(x=260, y=270)
        
        Reset_btn = Button(self.root2, text="Reset", font=("times new roman", 18, "bold"), activebackground="blue",activeforeground="white", bg="blue", fg="white", cursor="hand2", command=self.reset)
        Reset_btn.place(x=495, y=310, width=140, height=30) 

      
        
    def reset(self):
        with open("Temp1.txt","r+") as file:
            self.read1=file.read()
        #print(self.read1)
        self.passw = self.pass_.get()
        self.passconw = self.passcon.get()
        self.current2_=self.current_.get()
        self.phone_2=self.phone_.get()
        
        self.conn = sqlite3.connect("plasma.db")
        self.c = self.conn.cursor()
        self.c.execute("SELECT Password from hos WHERE Phone_No=" +self.phone_2)
        self.data = self.c.fetchall()
        if self.data==[]:
            return messagebox.showerror("Error"," Current Password not Matched to Your mail Id" , parent=self.root2)
        else:
            for i in self.data:
                    #print(i[0])
                    self.c.execute("SELECT Email from hos WHERE Phone_No=" +self.phone_2)
                    self.data = self.c.fetchall()
                    for j in self.data:
                        a=str(j[0])
                    if i[0] == self.current2_:
                        self.OTP_Forget=str(random.randint(100000,999999))
                        send = smtplib.SMTP("smtp.gmail.com", 587)  # Create session for Gmail
                        send.starttls()  # transport layer

                        msg = EmailMessage()
                        msg["Subject"] = "OTP"
                        msg["From"] = "aj147ps@gmail.com"
                        msg["To"] = a
                        msg.set_content("Hi! your OTP for reset password: "+"\'"+str(self.OTP_Forget)+"\'")        
                            
                        try:
                            send.login("aj147ps@gmail.com","xcavbfayvnthixwy")
                        except smtplib.SMTPAuthenticationError:
                            messagebox.showerror("Error","Error Occur Otp Not")    

                        try:
                            try:
                                try:                                
                                    
                                    send.send_message(msg)
                                    messagebox.showinfo("Mailed","OTP Sent to Your Mail Id") 
                                    self.root2.destroy()
                                    self.root3 = Toplevel(self)  # Child Window "Tk() can Also be use here"
                                    self.root3.title("Verification")
                                    self.root3.geometry("750x320+350+150")
                                    self.root3.configure(bg="black")
                                    photo4 = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
                                    self.root3.iconphoto(False, photo4)
                                    self.root3.grab_set() 
                                    self.root3.resizable(False, False)
                                
                                    title_child = Label(self.root3, text="Reset Password", bg="#152238", fg="white",compound=LEFT, font=("Goudy Old Style", 48, "bold"), anchor="w").place(x=0, y=0, relwidth=1)
                                    otp_lbl = Label(self.root3, text="Enter OTP", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=120)
                                    self.otp_ = Entry(self.root3, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
                                    self.otp_.place(x=260, y=120)
                                    
                                    Reset_btn = Button(self.root3, text="Reset", font=("times new roman", 18, "bold"), activebackground="blue",activeforeground="white", bg="blue", fg="white", cursor="hand2", command=self.reset1)
                                    Reset_btn.place(x=495, y=260, width=140, height=30) 
                        
                                except smtplib.SMTPRecipientsRefused:
                                    messagebox.showerror("Mailed","Mail Not Sent")
                            except smtplib.SMTPException:
                                messagebox.showerror("Mailed","Mail Not Sent")
                        except smtplib.SMTPConnectError:
                            messagebox.showerror("Error","Connection Error")
                    else:
                        return messagebox.showerror("Error","Contact No. have not given Mail Id")

    def reset1(self):
        self.one_ = self.otp_.get()
        #print(self.one_)
        if str(self.one_)==str(self.OTP_Forget):
            if len(str(self.passw))>=8:
                if self.passw == self.passconw:
                    y= f"UPDATE hos SET Password = {str(self.passw)} WHERE Phone_No = {str(self.phone_2)}"
                    self.c.execute(str(y))
                    self.conn.commit()
                    self.conn.close()
                    self.OTP_Forget=""
                    messagebox.showinfo("Info", "Successfully Changed!!", parent=self.root3)
                    self.root3.destroy()                    
                else:
                    return messagebox.showerror("Error", "Password Cann't Changed  password  and confirm password not match!!", parent=self.root3)
            else:
                return messagebox.showerror("Error", "Password should be of minimum 8 Characters", parent=self.root3)
        else:
            return messagebox.showerror("Error", "OTP Entered is Wrong", parent=self.root3)
    
    def clock(self):

        self.h = str(time.strftime("%H"))
        self.m = str(time.strftime("%M"))
        self.s = str(time.strftime("%S"))

        if int(self.h)<15 and int(self.m)>0:
            self.lbl_abv.config(text="PM")

        if int(self.h)>=15 and int(self.h)<20 and int(self.m)>0:
            self.lbl_abv.config(text="PM")
        
        if int(self.h)>=20 and int(self.h)<24 and int(self.m)>0:
            self.lbl_abv.config(text="PM")

        if int(self.h)>12 and int(self.h)<15 and int(self.m)>0:
            self.lbl_abv.config(text="PM")

        if int(self.h)>0 and int(self.h)<12 and int(self.m)>0:
            self.lbl_abv.config(text="AM")

         
        self.lbl_hr.config(text = self.h)
        self.lbl_min.config(text = self.m)
        self.lbl_sec.config(text = self.s)
        self.lbl_hr.after(200,self.clock)

class Plasma_Search_hos(Tk):
    def __init__(self,*arg):       # Constructors
        Tk.__init__(self,*arg)
        photo = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
        self.iconphoto(False, photo)

        self.title("Plasma Finder".center(420))  # title for Window 
        self.configure(background = "black")  # background color for window 
        self.geometry("1360x768+0+0")
        photo = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
        self.iconphoto(False, photo)

        bg_color ="#FFFFF6"
        
     
        self.bg_icon = ImageTk.PhotoImage(file="Pics\\1 (1).jpg")
        bg_lbl = Label(self, image = self.bg_icon).pack(fill=Y) # we put image into our window
        
        self.hos_icon=ImageTk.PhotoImage(file="Pics\\1 (2) copy.jpg")
                
        
        F1 = LabelFrame(self,bd=10,relief=GROOVE,bg=bg_color)
        F1.place(x=0,relwidth=1,height=100 )

        lbl = Label(F1,text="Plasma Finder", compound=LEFT, image=self.hos_icon,bg=bg_color, font= ("times new roman",20,"bold")).place(x=0, y=5)

        self.lbl_hr = Label(F1,text="12" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_hr.place(x=890, y=40)
        
        self.lbl_COLON = Label(F1,text=":" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_COLON.place(x=915, y=40)
       
       
        self.lbl_min = Label(F1,text="12" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_min.place(x=925, y=40)
       
        self.lbl_COLON = Label(F1,text=":" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_COLON.place(x=950, y=40)
       
        self.lbl_sec = Label(F1,text="12" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_sec.place(x=960, y=40)
        

        self.lbl_abv = Label(F1,text="AM" , font = ("times new roman", 13,"bold"),bg=bg_color)
        self.lbl_abv.place(x=985, y=43)
       
       
        self.font=("times new roman",20,"bold")
        self.calendar = []

        ntpClient = ntplib.NTPClient()
        response = ntpClient.request('pool.ntp.org')
        a=ctime(response.tx_time)
        b=[a[i:i+10] for i in range(0, len(a), 10)]
        c=str(b[0])
        d=str(b[2])

        self.date = Label(F1, font=("times new roman",15,"bold"), text=c, bg=bg_color)
        self.date.place(x=740, y=40)

        self.date1 = Label(F1, font=("times new roman",15,"bold"), text=d,bg=bg_color)
        self.date1.place(x=840, y=40)

        
        self.date2 = Label(F1, font=("times new roman",15,"bold"), text="Calendar",bg=bg_color)
        self.date2.place(x=750, y=5)

        self.calendar.append(DateEntry(F1, font=("times new roman",15,"bold"), locale='en_GB',state="readonly",width=10))
        self.calendar[-1].place(x=855, y=20, anchor="w")

        
        btn_changepass = Button(F1, text="ChangePassword",relief=RAISED,width =15,height=1, font=("times new roman",14,"bold"),bg="red",foreground="white",command=self.change_pasw).place(x=1145,y=20,anchor="w")
        btn_logout = Button(F1, text="Logout",relief=RAISED,width =15,height=1, font=("times new roman",14,"bold"),bg="light green",foreground="black", command=self.logout).place(x=1145,y=60,anchor="w")

        lbl2 = Label(F1,bg=bg_color)
        lbl2.place(x=25,y=10)

        F2 = LabelFrame(self,bd=10,relief=GROOVE,bg=bg_color)
        F2.place(x=0,y=100,width=150,height=670 )

        F21 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F21.place(x=0,y=0,width=130,height=133 )
        
        F22 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F22.place(x=0,y=133,width=130,height=133)
        
        F23 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F23.place(x=0,y=266,width=130,height=133 )
        
        F24 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F24.place(x=0,y=399,width=130,height=133)
        
        F25 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F25.place(x=0,y=532,width=130,height=133)

        self.U_mange = PhotoImage(file="Pics\\User_Det.png")
        self.donor_b = ImageTk.PhotoImage(file="Pics\\Blood Donar.jpg")
        self.b_bank = ImageTk.PhotoImage(file="Pics\Blood Bank Search.jpg")    
        self.p_donar = ImageTk.PhotoImage(file="Pics\Plasma.png")
        self.exit = ImageTk.PhotoImage(file="Pics\\Exit.jpg")
        
        btn_U_det = Button(F21,image= self.U_mange,bg=bg_color,relief=RAISED,width =115,height=120,command=self.U_det).place(x=0,y=60,anchor="w")
        btn_blood_donor = Button(F22,image= self.donor_b,bg=bg_color,relief=RAISED,width =115,height=120,command=self.Blood_Donar ).place(x=0,y=60,anchor="w")
        btn_blood_bank = Button(F23,relief=RAISED,bg=bg_color,image=self.b_bank,width =115,height=120,command=self.Blood_Bank ).place(x=0,y=60,anchor="w")
        btn_Plasma = Button(F24,relief=RAISED,image=self.p_donar,bg=bg_color,width =115,height=120, command=self.Plasma).place(x=0,y=60,anchor="w")
        btn_Exit = Button(F25,relief=RAISED,bg=bg_color,image=self.exit,width =115,height=120, command=self.Exit).place(x=0,y=60,anchor="w")

        F3 = LabelFrame(self,bd=5,relief=FLAT,bg="light gray")
        F3.place(x=150,y=100,relwidth=1,height=60 )
        lbl_1= Label(F3,text="Dashboard / Hospital",font=("comic sans",15,"italic"),bg="light gray")
        lbl_1.place(x=0,y=10)

        btn_User = Button(F3, bd=5, relief=GROOVE, bg="red", fg="white", font=("",15,"bold"), text= "User View",command=self.User_Check)
        btn_User.place(x=1000,y=0)
        home_btn = Button(F3, text="Home",bd=5,relief=GROOVE, font=("",15,"bold"), fg="white", bg="blue", command=self.Home)
        home_btn.place(x=300,y=0)

        self.F4 =Frame(self,bd=10,relief=SUNKEN,bg="white")
        self.F4.place(x=180,y=200,width=1130,height=500 )
        
        self.searchby = StringVar()
        self.searchby1 = StringVar()

        lb_search=Label(self,text="Search By", font=("times new roman",15,"bold"))
        lb_search.place(x=180 ,y=185, anchor="w")
        combo_search=ttk.Combobox(self, textvariable=self.searchby,width=17, font=("times new roman",16,"bold"),state='readonly')
        combo_search['values']=("UID","B_Group")
        combo_search.place(x=273, y=185, anchor="w")
        
        search=Entry(self, textvariable=self.searchby1,width=17,bd=5,relief=GROOVE, font=("times new roman",16,"bold"))
        search.place(x=490, y=185, anchor="w")

        lb_search_btn=Button(self,text="Search By", bd=6, relief=GROOVE,command=self.search,font=("times new roman",15,"bold"),fg="yellow",bg="dark blue")
        lb_search_btn.place(x=695 ,y=183, height=30,anchor="w")
        
        lb_search_btn=Button(self,text="Search All", bd=6, relief=GROOVE,command=self.search1,font=("times new roman",15,"bold"),fg="yellow",bg="dark blue")
        lb_search_btn.place(x=835 ,y=183, height=30,anchor="w")
        
        lb_search_btn=Button(self,text="Clear", bd=6, relief=GROOVE,command=self.clear1,font=("times new roman",15,"bold"),fg="yellow",bg="dark blue")
        lb_search_btn.place(x=1110 ,y=183, height=30, width=200,anchor="w")

        Table_Frame=Frame(self.F4,bd=4, relief=RIDGE)
        Table_Frame.place(x=15,y=0,width=1080,height=480)

        scroll_x=Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame, orient=VERTICAL)
        scroll_x1=Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y1=Scrollbar(Table_Frame, orient=VERTICAL)
        self.Bloold_Bank_table=ttk.Treeview(Table_Frame,columns=("UID" , "Blood_Group"  , "Phone_No"   ),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Bloold_Bank_table.xview)
        scroll_y.config(command=self.Bloold_Bank_table.yview)

        
        self.Bloold_Bank_table.heading("UID", text="UID")
        self.Bloold_Bank_table.heading("Blood_Group", text="Blood_Group")
        self.Bloold_Bank_table.heading("Phone_No", text="Phone_No")

        self.Bloold_Bank_table.column("UID", width=150)
        self.Bloold_Bank_table.column("Blood_Group", width=150)
        self.Bloold_Bank_table.column("Phone_No", width=150)
        
    
        self.Bloold_Bank_table['show']='headings'
        
        self.fetch_data()

        self.clock()
    def Home(self):
        self.destroy()
        Hospital_Page().mainloop()

    def U_det(self):
        self.destroy()
        H_Manage().mainloop()
        
    def Blood_Donar(self):
        self.destroy()
        Bload_Search_hos().mainloop()
        
    
    def Blood_Bank(self):
        self.destroy()
        Bload_Bank_hos().mainloop()

    def Plasma(self):
        self.destroy()
        Plasma_Search_hos().mainloop()    
    
    def User_Check(self):
        self.destroy()
        User_Check_class().mainloop()
    
    def Exit(self):
        self.destroy()

        
    def search(self):
        
        if self.searchby.get()=="" and self.searchby1.get()=="":
            return messagebox.showwarning("Warning","Fields should be filled")
        if self.searchby.get()=="" :
            return messagebox.showwarning("Warning","Shearch By Option Should be filled")
        if self.searchby1.get()=="":
            return messagebox.showwarning("Warning","Search box should be filled")
        
        else:
            
            if self.searchby.get()=="UID":        
                try:
                    self.Bloold_Bank_table.column("UID", width=150)
                    self.Bloold_Bank_table.column("Blood_Group", width=150)
                    self.Bloold_Bank_table.column("Phone_No", width=150)
                    
                
                    self.Bloold_Bank_table['show']='headings'
                
                    self.Bloold_Bank_table.pack(fill=BOTH,expand=1)
                    self.Bloold_Bank_table.bind("<ButtonRelease-1>",self.getcursor)
                    self.fetch_data()

                    self.conn=sqlite3.connect("plasma.db")
                    self.c=self.conn.cursor()
                    self.c.execute("select * from Plasma_Donar where UID = '"+ self.searchby1.get()+"'")
                    rows=self.c.fetchall()
                    if len(rows)!=0:
                            self.Bloold_Bank_table.delete(*self.Bloold_Bank_table.get_children())
                            for row in rows:
                                    self.Bloold_Bank_table.insert('',END,values=row)
                            self.conn.commit()
                            self.conn.close()
                    else:
                        return messagebox.showerror("Error","UID No Not Exist")        
                except Exception:
                    return messagebox.showerror("Error", "Something Wrong")
                self.conn.close()
            
            elif self.searchby.get()=="B_Group":
                try:
                    self.Bloold_Bank_table.column("UID", width=150)
                    self.Bloold_Bank_table.column("Blood_Group", width=150)
                    self.Bloold_Bank_table.column("Phone_No", width=150)
                    
                
                    self.Bloold_Bank_table['show']='headings'
                
                    self.Bloold_Bank_table.pack(fill=BOTH,expand=1)
                    self.Bloold_Bank_table.bind("<ButtonRelease-1>",self.getcursor)
                    self.fetch_data()

                    self.conn=sqlite3.connect("plasma.db")
                    self.c=self.conn.cursor()
                    self.c.execute("select * from Plasma_Donar WHERE Blood_Group = '"+ self.searchby1.get()+"'")
                    rows=self.c.fetchall()
                    if len(rows)!=0:
                            self.Bloold_Bank_table.delete(*self.Bloold_Bank_table.get_children())
                            for row in rows:
                                    self.Bloold_Bank_table.insert('',END,values=row)
                            self.conn.commit()
                            self.conn.close()
                    else:
                        return messagebox.showerror("Error","Bloood Group Not Available ")        
                except Exception:
                    return messagebox.showerror("Error", "Something Wrong")
                self.conn.close()

            else:
                return messagebox.showerror("Error", "No Such Option")
            
            
    def search1(self):
        self.Bloold_Bank_table.column("UID", width=150)
        self.Bloold_Bank_table.column("Blood_Group", width=150)
        self.Bloold_Bank_table.column("Phone_No", width=150)
        
    
        self.Bloold_Bank_table['show']='headings'
    
        self.Bloold_Bank_table.pack(fill=BOTH,expand=1)
        self.Bloold_Bank_table.bind("<ButtonRelease-1>",self.getcursor)
        self.fetch_data()

    def fetch_data(self):
        self.conn=sqlite3.connect("plasma.db")
        self.c=self.conn.cursor()
        self.c.execute("select * from Plasma_Donar")
        rows=self.c.fetchall()
        if len(rows)!=0:
                self.Bloold_Bank_table.delete(*self.Bloold_Bank_table.get_children())
                for row in rows:
                        self.Bloold_Bank_table.insert('',END,values=row)
                self.conn.commit()
        self.conn.close()

    def getcursor(self,ev):
        cursor_row=self.Bloold_Bank_table.focus()
        Content=self.Bloold_Bank_table.item(cursor_row)
        row=Content['values']

        self.Bloold_Bank_table.set(row[0])
        self.Bloold_Bank_table.set(row[1])
        self.Bloold_Bank_table.set(row[2])
        
    def clear1(self):
        self.Bloold_Bank_table.delete(*self.Bloold_Bank_table.get_children())
        self.searchby.set("")
        self.searchby1.set("")

    
    
    def logout(self):
        self.read1=StringVar()
        with open("Temp1.txt","r+") as file:
            self.read1=file.read()
            file.truncate()
    
        a=messagebox.askyesnocancel("Hey","Confirm again for Logout")
        if a>0:
            now = datetime.now()
            self.Time2=now.strftime('%H:%M:%S')

            self.today1= now.strftime("%d/%m/%Y")
            self.destroy()
            self.conn=sqlite3.connect("plasma.db")
            self.c=self.conn.cursor()
            y="UPDATE Last_Login_hospital set time=\""+str(self.Time2)+"\", date=\""+str(self.today1)+"\" where HID =\""+str(self.read1)+"\""
            #print(y)
            self.c.execute(y)
            self.conn.commit()
            root=Tk()
            clas=H_login(root)            
        else:
            pass



    def change_pasw(self):  
        self.root2 = Toplevel(self)  # Child Window "Tk() can Also be use here"
        self.root2.title("Change Password")
        self.root2.geometry("750x370+350+150")
        self.root2.configure(bg="black")
        photo1 = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
        self.root2.iconphoto(False, photo1)
        self.root2.grab_set() 
        self.root2.resizable(False, False)

        title_child = Label(self.root2, text="Reset Password", bg="#152238", fg="white",compound=LEFT, font=("Goudy Old Style", 48, "bold"), anchor="w").place(x=0, y=0, relwidth=1)
        
        phone_lbl = Label(self.root2, text="Phone No.", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=120)
        self.phone_ = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.phone_.place(x=260, y=120)
        
        current_lbl = Label(self.root2, text="Current Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=170)
        self.current_ = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.current_.place(x=260, y=170)
        
        pass_lbl = Label(self.root2, text="New Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=220)
        self.pass_ = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.pass_.place(x=260, y=220)
        
        passcon_lbl = Label(self.root2, text="Confirm Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=270)
        self.passcon = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.passcon.place(x=260, y=270)
        
        Reset_btn = Button(self.root2, text="Reset", font=("times new roman", 18, "bold"), activebackground="blue",activeforeground="white", bg="blue", fg="white", cursor="hand2", command=self.reset)
        Reset_btn.place(x=495, y=310, width=140, height=30) 

      
        
    def reset(self):
        with open("Temp1.txt","r+") as file:
            self.read1=file.read()
        #print(self.read1)
        self.passw = self.pass_.get()
        self.passconw = self.passcon.get()
        self.current2_=self.current_.get()
        self.phone_2=self.phone_.get()
        
        self.conn = sqlite3.connect("plasma.db")
        self.c = self.conn.cursor()
        self.c.execute("SELECT Password from hos WHERE Phone_No=" +self.phone_2)
        self.data = self.c.fetchall()
        if self.data==[]:
            return messagebox.showerror("Error"," Current Password not Matched to Your mail Id" , parent=self.root2)
        else:
            for i in self.data:
                    #print(i[0])
                    self.c.execute("SELECT Email from hos WHERE Phone_No=" +self.phone_2)
                    self.data = self.c.fetchall()
                    for j in self.data:
                        a=str(j[0])
                    if i[0] == self.current2_:
                        self.OTP_Forget=str(random.randint(100000,999999))
                        send = smtplib.SMTP("smtp.gmail.com", 587)  # Create session for Gmail
                        send.starttls()  # transport layer

                        msg = EmailMessage()
                        msg["Subject"] = "OTP"
                        msg["From"] = "aj147ps@gmail.com"
                        msg["To"] = a
                        msg.set_content("Hi! your OTP for reset password: "+"\'"+str(self.OTP_Forget)+"\'")        
                            
                        try:
                            send.login("aj147ps@gmail.com","xcavbfayvnthixwy")
                        except smtplib.SMTPAuthenticationError:
                            messagebox.showerror("Error","Error Occur Otp Not")    

                        try:
                            try:
                                try:                                
                                    
                                    send.send_message(msg)
                                    messagebox.showinfo("Mailed","OTP Sent to Your Mail Id") 
                                    self.root2.destroy()
                                    self.root3 = Toplevel(self)  # Child Window "Tk() can Also be use here"
                                    self.root3.title("Verification")
                                    self.root3.geometry("750x320+350+150")
                                    self.root3.configure(bg="black")
                                    photo4 = ImageTk.PhotoImage(file = "Pics\\Icon.ico")
                                    self.root3.iconphoto(False, photo4)
                                    self.root3.grab_set() 
                                    self.root3.resizable(False, False)
                                
                                    title_child = Label(self.root3, text="Reset Password", bg="#152238", fg="white",compound=LEFT, font=("Goudy Old Style", 48, "bold"), anchor="w").place(x=0, y=0, relwidth=1)
                                    otp_lbl = Label(self.root3, text="Enter OTP", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=120)
                                    self.otp_ = Entry(self.root3, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
                                    self.otp_.place(x=260, y=120)
                                    
                                    Reset_btn = Button(self.root3, text="Reset", font=("times new roman", 18, "bold"), activebackground="blue",activeforeground="white", bg="blue", fg="white", cursor="hand2", command=self.reset1)
                                    Reset_btn.place(x=495, y=260, width=140, height=30) 
                        
                                except smtplib.SMTPRecipientsRefused:
                                    messagebox.showerror("Mailed","Mail Not Sent")
                            except smtplib.SMTPException:
                                messagebox.showerror("Mailed","Mail Not Sent")
                        except smtplib.SMTPConnectError:
                            messagebox.showerror("Error","Connection Error")
                    else:
                        return messagebox.showerror("Error","Contact No. have not given Mail Id")

    def reset1(self):
        self.one_ = self.otp_.get()
        #print(self.one_)
        if str(self.one_)==str(self.OTP_Forget):
            if len(str(self.passw))>=8:
                if self.passw == self.passconw:
                    y= f"UPDATE hos SET Password = {str(self.passw)} WHERE Phone_No = {str(self.phone_2)}"
                    self.c.execute(str(y))
                    self.conn.commit()
                    self.conn.close()
                    self.OTP_Forget=""
                    messagebox.showinfo("Info", "Successfully Changed!!", parent=self.root3)
                    self.root3.destroy()                    
                else:
                    return messagebox.showerror("Error", "Password Cann't Changed  password  and confirm password not match!!", parent=self.root3)
            else:
                return messagebox.showerror("Error", "Password should be of minimum 8 Characters", parent=self.root3)
        else:
            return messagebox.showerror("Error", "OTP Entered is Wrong", parent=self.root3)

    
    def clock(self):

        self.h = str(time.strftime("%H"))
        self.m = str(time.strftime("%M"))
        self.s = str(time.strftime("%S"))

        if int(self.h)<15 and int(self.m)>0:
            self.lbl_abv.config(text="PM")

        if int(self.h)>=15 and int(self.h)<20 and int(self.m)>0:
            self.lbl_abv.config(text="PM")
        
        if int(self.h)>=20 and int(self.h)<24 and int(self.m)>0:
            self.lbl_abv.config(text="PM")

        if int(self.h)>12 and int(self.h)<15 and int(self.m)>0:
            self.lbl_abv.config(text="PM")

        if int(self.h)>0 and int(self.h)<12 and int(self.m)>0:
            self.lbl_abv.config(text="AM")

         
        self.lbl_hr.config(text = self.h)
        self.lbl_min.config(text = self.m)
        self.lbl_sec.config(text = self.s)
        self.lbl_hr.after(200,self.clock)

app = win1()
app.mainloop()
