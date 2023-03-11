from tkinter import *
import tkinter as tk
import mysql.connector
from tkinter import messagebox
from PIL import Image,ImageTk
import datetime as dt
from time import strftime
from tkinter import filedialog
import socket
import time

con = mysql.connector.connect(host = "localhost",user="root",password="vulcan@123")
cur = con.cursor(buffered=True)
print("------>",cur)
try:
    cur.execute("use vasd_9090")
except:
    cur.execute("create database vasd_9090")
    cur.execute("user vasd_9090")
    
try:
    cur.execute("describe vasd_9090")
except:
    cur.execute("create table vasd_9090(id int primary key auto_increment , name varchar(20) , email varchar(20) , pwd varchar(20))")

win=Tk()
win.state("zoomed")
win.configure(bg="#838996")
win.title("Gati-X")
win.resizable(width=True,height=True)
imgs=Image.open("vulcan.jpg")
imgs = imgs.resize((130,90))
imgs_tk=ImageTk.PhotoImage(imgs,master=win)
l=Label(win,image=imgs_tk,bg="#838996")
l.place(relx=.0,rely=-.01)

img=Image.open("gati.png")
img = img.resize((180,180))
img_tk=ImageTk.PhotoImage(img,master=win)
l=Label(win,image=img_tk,bg="#838996")
l.place(relx=.45,rely=-.06)

# imges=Image.open("E:/Gati_X/gati.png")
# imges = imges.resize((300,600))
# imgs_tk=ImageTk.PhotoImage(imges,master=win)
# print("iiiiiiiiiiiii",imgs_tk)
# l=Label(win,image=imgs_tk)
# l.place(x=0,y=0)

date = dt.datetime.now()
# Create Label to display the Date
label = Label(win, text=f"{date:%A, %B %d, %Y}",bg="#838996" , font="Calibri, 14")
label.place(relx=.80,rely=.0)

def my_time():
    time_string = strftime('%H:%M:%S %p') # time format 
    l1.config(text=time_string)
    l1.after(1000,my_time) # time delay of 1000 milliseconds 
	
my_font=('times',12,'bold') # display size and style
l1=Label(win,font=my_font,bg='#838996')
l1.place(relx=.80,rely=.04)
my_time()

def login_page():
    frm=Frame(win) 
    frm.configure(bg="#BCC6CC")
    frm.place(x=0,y=82,relwidth=1,relheight=.9)
    footer_f1 = Label(frm, text="Powered by: VULCAN Advance Intelligence Computing Pvt.Ltd",font=('Arial',10,'bold') , anchor="center",bg='#838996')
    footer_f1.place(x=0,y=560,relwidth=1,relheight=.1) 
    
    def fp():
        frm.destroy()
        forgot_pass_screen()
        
    
    
    def login():
        name=e_user.get()
        print("----------->name",name)
        pwd=e_pass.get()
        print("----------->psw",pwd)
        if(len(name)==0 or len(pwd)==0):
            messagebox.showwarning("Validation","Plz fill both field")
            return
        
        cur.execute('select * from vasd_9090 where name =  "%s" AND pwd ="%s" '%(name,pwd ) )
        rows = cur.fetchall() # Retrieve all restults into a list of tuples
        if (rows == []):
        # The query returned no results, thus the user-password pair does not exist in the DB
            print("Incorrect username or password.")
            messagebox.showwarning("Validation","Please Enter Currect Password")
            return ""
        else:
            row = rows[0]
            print("Welcome", row[1]) # Print "Welcome <name>"
            home_page()
            return row[0] # Return username
        
        # elif(cur.execute('select * from vasd_9090 where name =  "%s" AND pwd = "%s"'%(name,pwd))):
        #     messagebox.showwarning("Validation","Please Enter Currect Password")
        # else:     
        # home_page()

    # def reset():
    #     e_user.delete(0,"end")
    #     e_pass.delete(0,"end")
    #     e_user.focus()
    
    lbl_user=Label(frm,text="User Name",font=('Arial',14,'bold'),bg='#BCC6CC')
    lbl_user.place(relx=.3,rely=.1)

    e_user=Entry(frm,font=('Arial',14,'bold'),bd=3)
    e_user.place(relx=.42,rely=.1)
    # e_user.insert(0, "Enter any Text")
    e_user.focus()
   
    lbl_pass=Label(frm,text="Password",font=('Arial',14,'bold'),bg='#BCC6CC')
    lbl_pass.place(relx=.3,rely=.25)

    e_pass=Entry(frm,font=('Arial',14,'bold'),bd=3,show="*")
    e_pass.place(relx=.42,rely=.25)
    
    btn_login=Button(frm,text=" login ",font=('Arial',14,'bold'),bd=3,command=login)
    btn_login.place(relx=.44,rely=.4)
    
    # btn_reset=Button(frm,text="reset",font=('Arial',14,'bold'),bd=3,command=reset)
    # btn_reset.place(relx=.47,rely=.4)
    
    btn_signup=Button(frm,text="SingUp",font=('Arial',14,'bold'),bd=3,command=signup)
    btn_signup.place(relx=.51,rely=.4)
    
    btn_fp=Button(frm,text="forgot password",font=('Arial',14,'bold'),bd=3,width=16,command=fp)
    btn_fp.place(relx=.43,rely=.55)
    
def home_page():
    frm=Frame(win)
    frm.configure(bg="#BCC6CC")
    frm.place(x=0,y=82,relwidth=1,relheight=.9)
 
    def clients(): 
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        print("---------->",clientSocket)

        # Connect to the server

        # clientSocket.connect(("127.0.0.1",9090));
        clientSocket.connect(("192.168.0.7",4001));
        
        if(dis_connect_btn["text"]=="Disconnect"):
            clientSocket.close()
            dis_connect_btn.configure(text="Connect")
            messagebox.showwarning("Validation","Please Click Again")
        else:
            dis_connect_btn.configure(text="Disconnect")
        # clientSocket.connect(("192.168.0.7",4001));
        # Send data to server
        data = "|C|0-0|128-128|\r\n"
        # time.sleep(4)
        clientSocket.send(data.encode())
        # data = "|T|25-50|123456dergfe789|1|6|1|0|\r\n"
        # data = "|T|20-35|Welcome To Vulcan|1|2|1|0|\r\n"
        data="|T|0-20|"
        er=input("any char => ")
        data+=er
        data+="|1|2|1|0\r\n"
        clientSocket.send(data.encode())
        # Receive data from server
        
        dataFromServer = clientSocket.recv(1024);
        print("////////",dataFromServer)
        # Print to the console
        print(dataFromServer.decode());
         
    btn_home=Button(frm,text="  Home  ",font=('Arial',14,'bold'),bd=1,bg='#F8F9F9')
    btn_home.place(relx=.01,rely=.1)
    
    btn_disp_con=Button(frm,text="Dis Con ",font=('Arial',14,'bold'),bd=1,command=display_confige)
    btn_disp_con.place(relx=.01,rely=.2)
    
    btn_data_log=Button(frm,text="Data log",font=('Arial',14,'bold'),bd=1,command=display_log)
    btn_data_log.place(relx=.01,rely=.4)
    
    btn_disp_test=Button(frm,text="Dis Test",font=('Arial',14,'bold'),bd=1,command=display_test)
    btn_disp_test.place(relx=.01,rely=.3)
    
    lbl_display_ip=Label(frm,text="Display IP",font=('Arial',9,'bold'),bg='#BCC6CC')
    lbl_display_ip.place(relx=.20,rely=.1)

    e_display_ip=Entry(frm,font=('Arial',9,'bold'),bd=3)
    e_display_ip.place(relx=.26,rely=.1)
    e_display_ip.insert(0, "192.168.0.7")
    e_display_ip.focus()
    
    lbl_display_port=Label(frm,text="Display Port",font=('Arial',9,'bold'),bg='#BCC6CC')
    lbl_display_port.place(relx=.53,rely=.1)

    e_display_port=Entry(frm,font=('Arial',9,'bold'),bd=3)
    e_display_port.place(relx=.60,rely=.1)
    e_display_port.insert(0, "4001")
    e_display_port.focus()
    
    lbl_radar_config=Label(frm,text="R Config",font=('Arial',9,'bold'),bg='#BCC6CC')
    lbl_radar_config.place(relx=.20,rely=.3)

    e_radar_config=Entry(frm,font=('Arial',9,'bold'),bd=3)
    e_radar_config.place(relx=.26,rely=.3)
    e_radar_config.focus()
    
    lbl_radar_road=Label(frm,text="R Boad ",font=('Arial',9,'bold'),bg='#BCC6CC')
    lbl_radar_road.place(relx=.53,rely=.3)

    e_radar_road=Entry(frm,font=('Arial',9,'bold'),bd=3)
    e_radar_road.place(relx=.60,rely=.3)
    e_radar_road.focus()
    
    dis_connect_btn=Button(frm,text="Connect",font=('Arial',14,'bold'),bd=3,command=clients)   
    dis_connect_btn.place(relx=.44,rely=.4)
    
    lbl_radar_speed=Label(frm,text="  R Speed ",font=('Arial',9,'bold'),bg='#BCC6CC')
    lbl_radar_speed.place(relx=.38,rely=.6)

    e_radar_speed=Entry(frm,font=('Arial',9,'bold'),bd=3,state=DISABLED)
    e_radar_speed.place(relx=.43,rely=.6)
    e_radar_speed.focus()
    
    lbl_vehical_dir=Label(frm,text="Vehical Dir ",font=('Arial',9,'bold'),bg='#BCC6CC')
    lbl_vehical_dir.place(relx=.38,rely=.7)

    e_vehical_dir=Entry(frm,font=('Arial',9,'bold'),bd=3)
    e_vehical_dir.place(relx=.43,rely=.7)
    e_vehical_dir.focus()
   
    footer_f1 = Label(frm, text="Powered by: VULCAN Advance Intelligence Computing Pvt.Ltd",font=('Arial',10,'bold') , anchor="center",bg='#838996')
    footer_f1.place(x=0,y=570,relwidth=1,relheight=.1)

    
def display_confige():
    frm=Frame(win)
    frm.configure(bg="#BCC6CC")
    frm.place(x=0,y=82,relwidth=1,relheight=.9)
    
    btn_home=Button(frm,text="  Home  ",font=('Arial',14,'bold'),bd=1,command=home_page)
    btn_home.place(relx=.01,rely=.1)
    
    btn_disp=Button(frm,text="Dis Con ",font=('Arial',14,'bold'),bd=1,command=display_confige)
    btn_disp.place(relx=.01,rely=.2)
    
    btn_data_log=Button(frm,text="Data log",font=('Arial',14,'bold'),bd=1,command=display_log)
    btn_data_log.place(relx=.01,rely=.4)
    
    btn_disp_test=Button(frm,text="Dis Test",font=('Arial',14,'bold'),bd=1,command=display_test)
    btn_disp_test.place(relx=.01,rely=.3)
    
    lbl_disp_id=Label(frm,text="C.D IP",font=('Arial',9,'bold'),bg='#BCC6CC')
    lbl_disp_id.place(relx=.20,rely=.1)

    e_disp_id=Entry(frm,font=('Arial',9,'bold'),bd=3)
    e_disp_id.place(relx=.26,rely=.1)
    e_disp_id.focus()
    
    lbl_dips_port=Label(frm,text="D Port",font=('Arial',9,'bold'),bg='#BCC6CC')
    lbl_dips_port.place(relx=.53,rely=.1)

    e_dips_port=Entry(frm,font=('Arial',9,'bold'),bd=3)
    e_dips_port.place(relx=.60,rely=.1)
    e_dips_port.focus()
    
    lbl_disp_subnet=Label(frm,text="C.D Subnet",font=('Arial',9,'bold'),bg='#BCC6CC')
    lbl_disp_subnet.place(relx=.20,rely=.2)

    e_disp_subnet=Entry(frm,font=('Arial',9,'bold'),bd=3)
    e_disp_subnet.place(relx=.26,rely=.2)
    e_disp_subnet.focus()
    
    lbl_gateway=Label(frm,text="Gateway",font=('Arial',9,'bold'),bg='#BCC6CC')
    lbl_gateway.place(relx=.53,rely=.2)

    e_gateway=Entry(frm,font=('Arial',9,'bold'),bd=3)
    e_gateway.place(relx=.60,rely=.2)
    e_gateway.focus()
    
    lbl_dns=Label(frm,text="DNS",font=('Arial',9,'bold'),bg='#BCC6CC')
    lbl_dns.place(relx=.20,rely=.3)

    e_dns=Entry(frm,font=('Arial',9,'bold'),bd=3)
    e_dns.place(relx=.26,rely=.3)
    e_dns.focus()

    lbl_server_dns=Label(frm,text="S.DNS",font=('Arial',9,'bold'),bg='#BCC6CC')
    lbl_server_dns.place(relx=.53,rely=.3)

    e_server_dns=Entry(frm,font=('Arial',9,'bold'),bd=3)
    e_server_dns.place(relx=.60,rely=.3)
    e_server_dns.focus()
    
     
    dis_submit_btn=Button(frm,text="Submit",font=('Arial',14,'bold'),bd=3,)
    dis_submit_btn.place(relx=.44,rely=.4)
    
    
    
    footer_f1 = Label(frm, text="Powered by: VULCAN Advance Intelligence Computing Pvt.Ltd",font=('Arial',10,'bold') , anchor="center",bg='#838996')
    footer_f1.place(x=0,y=570,relwidth=1,relheight=.1)
def display_log():
    frm=Frame(win)
    frm.configure(bg="#BCC6CC")
    frm.place(x=0,y=82,relwidth=1,relheight=.9)
    
    def open_file():
        opened_file_path=filedialog.askopenfilename(initialdir = "/",
                    title = "Select files",filetypes = (("TXT files","*.txt"),
                    ("All files","*.*")))
        print("file-------->",opened_file_path)
        if not opened_file_path:
            opened_file_path = ""
        return opened_file_path 
    # def radr_1():  
    #     INPUT = Output_1.get("1.0", "end-1c")
    #     print(INPUT)    
    #     if(INPUT == "120"):
    #         Output.insert(END, 'Correct')
    #     else:
    #         Output.insert(END, dttime)        
    # dttime = dt.datetime.now()
    
    btn_home=Button(frm,text="  Home  ",font=('Arial',14,'bold'),bd=1,command=home_page)
    btn_home.place(relx=.01,rely=.1)
    
    btn_disp=Button(frm,text="Dis Con ",font=('Arial',14,'bold'),bd=1,command=display_confige)
    btn_disp.place(relx=.01,rely=.2)
    
    btn_disp=Button(frm,text="Data log",font=('Arial',14,'bold'),bd=1,command=display_log)
    btn_disp.place(relx=.01,rely=.4)
    
    btn_disp_test=Button(frm,text="Dis Test",font=('Arial',14,'bold'),bd=1,command=display_test)
    btn_disp_test.place(relx=.01,rely=.3)
    
    lbl_acn = Button(frm, text="Gati-x Log",font=('Arial',14,'bold'),bd=1,command=open_file)
    lbl_acn.place(relx=.45,rely=.1)
    
    # b1=Button(win,text="RADAR-1",width=8,font=('Arial',14,"bold"),bd=3,command=hide_radar_1)
    # b1.place(relx=.31,rely=.4)
    # Output = Text(frm, height = 15,
    #     width = 45,
    #     bg = "#F8F9F9")
    # Output.place(relx=.28,rely=.4)
    def hide_radar_1():
        f = Frame(win)
        f.place(relx=.22,rely=.5)
        class Table:
            def __init__(self,f):
                # code for creating table
                for i in range(total_rows):
                    for j in range(total_columns):
                        if j==0:
                            self.e = Entry(f, width=4, fg='black',
                                        font=('Arial',13,'bold'))
                            
                            self.e.grid(row=i, column=j,sticky=E)
                            self.e.insert(END, lst[i][j])
                        else:
                                
                            self.e = Entry(f, width=25, fg='black',
                                        font=('Arial',13,'bold'))
                            
                            self.e.grid(row=i, column=j,sticky=E)
                            self.e.insert(END, lst[i][j])

        # take the data
        date = dt.datetime.now()
        lst = [(1,date,"40km"),
            (2,date,'40km'),
            (3,date,'40km'),
            (4,date,'40km'),
            (5,date,'40km')]

        # find total number of rows and
        # columns in list
        total_rows = len(lst)
        total_columns = len(lst[0])
        t = Table(f)
        print(t)

        lbl_acn=Label(frm,text="SR.",font=('Arial',9,'bold'),bg='#BCC6CC')
        lbl_acn.place(relx=.22,rely=.39)
        
        lbl_acn=Label(frm,text="Date Time",font=('Arial',9,'bold'),bg='#BCC6CC')
        lbl_acn.place(relx=.32,rely=.39)
        
        lbl_acn=Label(frm,text="Speed",font=('Arial',9,'bold'),bg='#BCC6CC')
        lbl_acn.place(relx=.44,rely=.39)
    b1=Button(win,text="RADAR-1",width=8,font=('Arial',14,"bold"),bd=3,command=hide_radar_1)
    b1.place(relx=.31,rely=.4)

    # e_user=Entry(frm,font=('Arial',9,'bold'),bd=3)
    # e_user.place(relx=.26,rely=.3)
    # e_user.focus()
    
    def hide():
        f1= Frame(win)
        f1.place(relx=.59,rely=.5)
        class Table:
            def __init__(self,f1):
                # code for creating table
                for i in range(total_rows):
                    for j in range(total_columns):
                        if j==0:
                            self.e = Entry(f1, width=4, fg='black',
                                        font=('Arial',13,'bold'))
                            
                            self.e.grid(row=i, column=j,sticky=E)
                            self.e.insert(END, lst[i][j])
                        else:
                            self.e = Entry(f1, width=25, fg='black',
                                    font=('Arial',13,'bold'))
                        
                            self.e.grid(row=i, column=j,sticky=E)
                            self.e.insert(END, lst[i][j])
        # take the data
        lst = [(1,'AA','Mumbai'),
            (2,'Aaryan','Pune'),
            (3,'Vaishnavi','Mumbai'),
            (4,'Rachna','Mumbai'),
            (5,'Shubham','Delhi')]
        # find total number of rows and
        # columns in list
        total_rows = len(lst)
        total_columns = len(lst[0])
        t = Table(f1)
        print(t)
        
        lbl_acn=Label(frm,text="SR.",font=('Arial',9,'bold'),bg='#BCC6CC')
        lbl_acn.place(relx=.60,rely=.39)
        
        lbl_acn=Label(frm,text="Date Time",font=('Arial',9,'bold'),bg='#BCC6CC')
        lbl_acn.place(relx=.65,rely=.39)
        
        lbl_acn=Label(frm,text="Speed",font=('Arial',9,'bold'),bg='#BCC6CC')
        lbl_acn.place(relx=.79,rely=.39)
        
    b2=Button(win,text="RADAR-2",width=8,font=('',14,"bold"),bd=3,command=hide)
    b2.place(relx=.65,rely=.4) 

    footer_f1 = Label(frm, text="Powered by: VULCAN Advance Intelligence Computing Pvt.Ltd",font=('Arial',10,'bold') , anchor="center",bg='#838996')
    footer_f1.place(x=0,y=570,relwidth=1,relheight=.1)
    
def display_test():
    frm=Frame(win)
    frm.configure(bg="#BCC6CC")
    frm.place(x=0,y=82,relwidth=1,relheight=.9)
  
    def client_connect():
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        # print("---469------->",type(clientSocket))
        # Connect to the server
        # clientSocket.connect(("127.0.0.1",9090));
        clientSocket.connect(("192.168.0.7",4001));
        
        if(dis_test_submit_btn["text"]=="Disconnect"):
            clientSocket.close()
            e_y_asix.configure(text="Connect")
            e_x_asix.configure(text="Connect")
            dis_test_submit_btn.configure(text="Connect")
            # messagebox.showwarning("Validation","Please Click Again")
        else:
            dis_test_submit_btn.configure(text="Disconnect")
            # messagebox.showwarning('title', 'successfully connect')
            listbox.insert(END,'successfully connect')
        
        # Send data to server
        data = "|C|0-0|128-128|\r\n"
        # time.sleep(4)
        clientSocket.send(data.encode())
        # data = "|T|25-50|123456dergfe789|1|6|1|0|\r\n"
        # data = "|T|20-35|Welcome To Vulcan|1|2|1|0|\r\n"
        data="|T|0-20|"
        er=e_text.get()
        data+=er
        data+="|1|2|1|0\r\n"
        clientSocket.send(data.encode())
        # Receive data from server
        
        dataFromServer = clientSocket.recv(1024);
        print("////////",dataFromServer)
        # Print to the console
        print(dataFromServer.decode());
    
 

    def clear():
        e_dip_port.delete(0,"end")
        e_display_ip.delete(0,"end")
        e_x_asix.delete(0,"end")
        e_y_asix.delete(0,"end")
        e_text.delete(0,"end")
        listbox.delete(0,"end")
        e_display_ip.focus()
    
    btn_home=Button(frm,text="  Home  ",font=('Arial',14,'bold'),bd=1,command=home_page)
    btn_home.place(relx=.01,rely=.1)
    
    btn_disp=Button(frm,text="Dis Con ",font=('Arial',14,'bold'),bd=1,command=display_confige)
    btn_disp.place(relx=.01,rely=.2)
    
    btn_disp=Button(frm,text="Data log",font=('Arial',14,'bold'),bd=1,command=display_log)
    btn_disp.place(relx=.01,rely=.4)
    
    btn_disp_test=Button(frm,text="Dis Test",font=('Arial',14,'bold'),bd=1,command=display_test)
    btn_disp_test.place(relx=.01,rely=.3)
    
    lbl_display_ip=Label(frm,text="Display IP",font=('Arial',9,'bold'),bg='#BCC6CC')
    lbl_display_ip.place(relx=.20,rely=.1)

    e_display_ip=Entry(frm,font=('Arial',9,'bold'),bd=3)
    e_display_ip.place(relx=.26,rely=.1)
    e_display_ip.insert(0, "192.168.0.7")
    e_display_ip.focus()
    
    lbl_dip_port=Label(frm,text="Display Port",font=('Arial',9,'bold'),bg='#BCC6CC')
    lbl_dip_port.place(relx=.53,rely=.1)

    e_dip_port=Entry(frm,font=('Arial',9,'bold'),bd=3)
    e_dip_port.place(relx=.60,rely=.1)
    e_dip_port.insert(0, "4001")
    e_dip_port.focus()
    
    lbl_x_asix=Label(frm,text=" X ",font=('Arial',9,'bold'),bg='#BCC6CC')
    lbl_x_asix.place(relx=.20,rely=.2)

    e_x_asix=Entry(frm,font=('Arial',9,'bold'),bd=3)
    e_x_asix.place(relx=.26,rely=.2)
    e_x_asix.focus()
    # e_x_asix.insert(0, ' 0 ')
    # e_x_asix.bind("<Button-1>", click_x)
    # e_x_asix.bind("<Leave>", leave_x)
    
    lbl_y_asix=Label(frm,text=" Y ",font=('Arial',9,'bold'),bg='#BCC6CC')
    lbl_y_asix.place(relx=.53,rely=.2)

    e_y_asix=Entry(frm,font=('Arial',9,'bold'),bd=3)
    e_y_asix.place(relx=.60,rely=.2)
    e_y_asix.focus()
    # e_y_asix.insert(0, ' 0 ')
    # e_y_asix.bind("<Button-1>", click)
    # e_y_asix.bind("<Leave>", leave)
    
    lbl_font=Label(frm,text=" Font ",font=('Arial',9,'bold'),bg='#BCC6CC')
    lbl_font.place(relx=.20,rely=.3)
    
    options = [
    "Font_5x7",
    "Font_8x7",
    "Font_8x11",
    "Font_12x16",
    "Font_40x63",
    "Font_40x76"  
    ]
    
   
    clicked = StringVar()    # datatype of menu text
    clicked.set( "Font_5x7" )   # initial menu text
    drop = OptionMenu( frm , clicked , *options )   # Create Dropdown menu
    drop.place(relx=.26,rely=.3)
    
    lbl_color=Label(frm,text=" Color ",font=('Arial',9,'bold'),bg='#BCC6CC')
    lbl_color.place(relx=.53,rely=.3)
  
    options = [
    "RED",
    "GREEN",
    "BLUE",
    "YRLLOW",
    "MEGENTA",
    "CYAN",
    "WHITE"
    ]
    
    clicked = StringVar()   # datatype of menu text
    clicked.set( "RED" )     # initial menu text
    drop = OptionMenu( frm , clicked , *options )   # Create Dropdown menu
    drop.place(relx=.60,rely=.3)
  
    # def connect_fun():
    #     messagebox.showwarning('title', 'successfully connect')
        # listbox.insert(END,'successfully connect')
          
    dis_test_submit_btn=Button(frm,text="Connect",font=('Arial',14,'bold'),bd=3,command=client_connect)
    dis_test_submit_btn.place(relx=.33,rely=.4)
    
    dis_clear_dir_btn=Button(frm,text="Clear",font=('Arial',14,'bold'),bd=3,command=clear)
    dis_clear_dir_btn.place(relx=.44,rely=.4)
    
    lbl_text=Label(frm,text=" Text ",font=('Arial',11,'bold'),bg='#BCC6CC')
    lbl_text.place(relx=.20,rely=.6)

    e_text=Entry(frm,font=('Arial',11,'bold'),bd=3)
    e_text.place(relx=.26,rely=.6)
    e_text.focus()
    
    def send_fun(): 
        listbox.insert(END,e_text.get())   
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        # print("---469------->",type(clientSocket))
        
        # clientSocket.connect(("127.0.0.1",9090));
        clientSocket.connect(("192.168.0.7",4001));
        
        if(dis_test_submit_btn["text"]=="Disconnect"):
            clientSocket.close()
            # e_y_asix.configure(text="Connect")
            # e_x_asix.configure(text="Connect")
            dis_test_submit_btn.configure(text="Connect")
            # messagebox.showwarning("Validation","Please Click Again")
        else:
            dis_test_submit_btn.configure(text="Disconnect")
            # messagebox.showwarning('title', 'successfully connect')
            # listbox.insert(END,'successfully connect')
        
        # Send data to server
        data = "|C|0-0|128-128|\r\n"
        # time.sleep(4)
        clientSocket.send(data.encode())
        # data = "|T|25-50|123456dergfe789|1|6|1|0|\r\n"
        # data = "|T|20-35|Welcome To Vulcan|1|2|1|0|\r\n"
        data="|T|0-20|"
        er=e_text.get()
        data+=er
        data+="|1|2|1|0\r\n"
        clientSocket.send(data.encode())
        # Receive data from server
        
        dataFromServer = clientSocket.recv(1024);
        print("////////",dataFromServer)
        # Print to the console
        print(dataFromServer.decode());
       
    # Output = Text(frm, height = 5,
    #     width = 5,
    #     bg = "#F8F9F9")
    # # state=DISABLED
    # Output.place(relx=.40,rely=.7)
    
    dis_send=Button(frm,text="Send",font=('Arial',12,'bold'),bd=3,command=send_fun)
    dis_send.place(relx=.42,rely=.6)
    listbox = Listbox(frm, width=40, height=10, selectmode=MULTIPLE)
    # Function for printing the
    # selected listbox value(s)
    def selected_item(): 
        # Traverse the tuple returned by
        # curselection method and print
        # corresponding value(s) in the listbox
        for i in listbox.curselection():
            print(listbox.get(i))
            
    # Create a button widget and
    # map the command parameter to
    # selected_item function
    btn = Button(frm, text='Print Selected', command=selected_item)

    # Placing the button and listbox
    btn.pack(side='bottom')

    listbox.place(relx=.60,rely=.5)
    footer_f1 = Label(frm, text="Powered by: VULCAN Advance Intelligence Computing Pvt.Ltd",font=('Arial',10,'bold') , anchor="center",bg='#838996')
    footer_f1.place(x=0,y=570,relwidth=1,relheight=.1)

def signup():   
    frm=Frame(win)
    frm.configure(bg="#BCC6CC")
    frm.place(x=0,y=82,relwidth=1,relheight=.9)
    
    # def back():
    #     frm.destroy()
    #     login_page()
    
    def get():
        a=e_user.get()
        p=e_pass.get()
        if(len(a)==0 or len(p)==0):
            messagebox.showwarning("Validation","Plz fill both field")
            return
        else:
           login_page()
        curdb = cur.execute(f" insert into vasd_9090(name,email,pwd) values('{e_user.get()}','{e_email.get()}','{e_pass.get()}')")
        print(curdb)
        if cur:
            messagebox.showinfo("Account","Your Account create successfully")
        con.commit()
    
    lbl_user=Label(frm,text="Singup",font=('Arial',14,'bold'),bg='#BCC6CC')
    lbl_user.place(relx=.5,rely=0)
    
    lbl_user=Label(frm,text="User Name",font=('Arial',14,'bold'),bg='#BCC6CC')
    lbl_user.place(relx=.3,rely=.1)

    e_user=Entry(frm,font=('Arial',14,'bold'),bd=3)
    e_user.place(relx=.42,rely=.1)

    lbl_email=Label(frm,text="Email",font=('Arial',14,'bold'),bg='#BCC6CC')
    lbl_email.place(relx=.3,rely=.4)

    e_email=Entry(frm,font=('Arial',14,'bold'),bd=3)
    e_email.place(relx=.42,rely=.4)
    
    lbl_pass=Label(frm,text="Password",font=('Arial',14,'bold'),bg='#BCC6CC')
    lbl_pass.place(relx=.3,rely=.25)

    e_pass=Entry(frm,font=('Arial',14,'bold'),bd=3,show="*")
    e_pass.place(relx=.42,rely=.25)
    
    btn_login=Button(frm,text="Submit",font=('Arial',14,'bold'),bd=3,command=get)
    btn_login.place(relx=.47,rely=.5)
    
    footer_f1 = Label(frm, text="Powered by: VULCAN Advance Intelligence Computing Pvt.Ltd",font=('Arial',10,'bold') , anchor="center",bg='gray')
    footer_f1.place(x=0,y=570,relwidth=1,relheight=.1)
    
  
def forgot_pass_screen():
    frm=Frame(win)
    frm.configure(bg="#95B9C7")
    frm.place(x=0,y=82,relwidth=1,relheight=.9)
    
    def back():
        frm.destroy()
        login_page()
    
    def get():
        pass
        # acn=e_user.get()
        # mob=e_mob.get()
        # email=e_email.get()
        
        # # con=sqlite3.connect(database="bank.sqlite")
        # # cur=con.cursor()
        # cur.execute("select pass from account where acc_no=? and email=? and mob=?",(acn,email,mob))
        # pwd=cur.fetchone()
        # if(pwd==None):
        #     messagebox.showerror("invalid","Invalid details")
        # else:
        #     messagebox.showinfo("Password",f"Your Pass:{pwd[0]}")
    
    btn_back=Button(frm,text="back",font=('Arial',14,'bold'),bd=3,bg='#FFFFFF',command=back)
    btn_back.place(relx=.01,rely=0)
    
    lbl_user=Label(frm,text="User Name",font=('Arial',14,'bold'),bg='#95B9C7')
    lbl_user.place(relx=.3,rely=.1)

    e_user=Entry(frm,font=('Arial',14,'bold'),bd=3)
    e_user.place(relx=.42,rely=.1)
    e_user.focus()
    
     
    lbl_mob=Label(frm,text="Mob",font=('Arial',14,'bold'),bg='#95B9C7')
    lbl_mob.place(relx=.3,rely=.25)

    e_mob=Entry(frm,font=('Arial',14,'bold'),bd=3)
    e_mob.place(relx=.42,rely=.25)
    
    lbl_email=Label(frm,text="Email",font=('Arial',14,'bold'),bg='#95B9C7')
    lbl_email.place(relx=.3,rely=.4)

    e_email=Entry(frm,font=('Arial',14,'bold'),bd=3)
    e_email.place(relx=.42,rely=.4)
    

    btn_get=Button(frm,text="get password",font=('Arial',14,'bold'),bd=3,command=get)
    btn_get.place(relx=.45,rely=.55)
    
    footer_f1 = Label(frm, text="Powered by: VULCAN Advance Intelligence Computing Pvt.Ltd",font=('Arial',10,'bold'), anchor="center",bg='#838996')
    footer_f1.place(x=0,y=570,relwidth=1,relheight=.1)
    
    def update_profile():
        frm=Frame(win)
        frm.configure(bg="#FFFFFF")
        frm.place(relx=.2,rely=.2,relwidth=.6,relheight=.7)
  
        def update():
            pass
            # name=e_name.get()
            # mob=e_mob.get()
            # email=e_email.get()
            # pwd=e_pass.get()
            
            # con=sqlite3.connect(database="bank.sqlite")
            # cur=con.cursor()
            # cur.execute("update account set name=?,mob=?,email=?,pass=? where acc_no=?",(name,mob,email,pwd,row[0]))
            # con.commit()
            # con.close()
            # messagebox.showinfo("Update","Profile Updated")
            # row[1]=name
            # frm.destroy()
            # welcome_screen()
                    
        lbl_name=Label(frm,text="Name",font=('Arial',20,'bold'),bg='#FFFFFF')
        lbl_name.place(relx=.3,rely=.1)

        e_name=Entry(frm,font=('Arial',20,'bold'),bd=5)
        e_name.place(relx=.42,rely=.1)
        e_name.focus()
        # e_name.insert(0,row[1])

        lbl_mob=Label(frm,text="Mob",font=('Arial',20,'bold'),bg='#FFFFFF')
        lbl_mob.place(relx=.3,rely=.25)

        e_mob=Entry(frm,font=('Arial',20,'bold'),bd=5)
        e_mob.place(relx=.42,rely=.25)
        # e_mob.insert(0,row[2])
        
        lbl_email=Label(frm,text="Email",font=('Arial',20,'bold'),bg='#FFFFFF')
        lbl_email.place(relx=.3,rely=.4)

        e_email=Entry(frm,font=('Arial',20,'bold'),bd=5)
        e_email.place(relx=.42,rely=.4)
        # e_email.insert(0,row[3])
        
        lbl_pass=Label(frm,text="Pass",font=('Arial',20,'bold'),bg='#FFFFFF')
        lbl_pass.place(relx=.3,rely=.55)

        e_pass=Entry(frm,font=('Arial',20,'bold'),bd=5)
        e_pass.place(relx=.42,rely=.55)
        # e_pass.insert(0,row[4])

        btn_get=Button(frm,text="update",font=('Arial',20,'bold'),bd=5,command=update)
        btn_get.place(relx=.4,rely=.7)
        
        footer_f1 = Label(frm, text="Powered by: VULCAN Advance Intelligence Computing Pvt.Ltd",font=('Arial',10,'bold') , anchor="center",bg='#838996')
        footer_f1.place(x=0,y=530,relwidth=1,relheight=.1)
    
login_page()
win.mainloop()









