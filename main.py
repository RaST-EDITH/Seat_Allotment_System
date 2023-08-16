import os
from tkinter import *
import openpyxl as oxl
from tkinter import ttk
import customtkinter as ctk
from tabulate import tabulate
from PIL import Image ,ImageTk
from tkinter.messagebox import showerror

def Imgo(file,w,h) :

    # Image processing
    img=Image.open(file)
    pht=ImageTk.PhotoImage(img.resize((w,h), Image.Resampling.LANCZOS ))
    return pht

def change(can,page) :

    # Switching canvas
    can.destroy()
    page()

def hel() :

    # Pop up window
    showerror(title="Info",message="INVALID ENTRY")

def not_allow() :

    # Pop up window
    showerror(title="Info",message="SLOT FULL")

def compare_rec(app_no,pw_dob) :

    # Comparing ID and password
    global rec
    wb=oxl.load_workbook( os.path.join( os.getcwd(), "Data_Files\\student_data.xlsx") )
    ws=wb["Sheet1"]
    for i in range(2,ws.max_row+1) :
        flag=0
        x=ws[f"B{i}"]
        y=ws[f"L{i}"]
        if app_no == str(x.value) and pw_dob == y.value :
            flag=1
            rec=i
            break
    if flag==1 :
        change(frpa, secondpage)

    else :
        hel()

def secondpage():

    global scpa

    # Data managing
    wb=oxl.load_workbook( os.path.join( os.getcwd(), "Data_Files\\student_data.xlsx") )
    ws=wb["Sheet1"]
    scpa=Canvas(root,width=1560,height=810,borderwidth=0)
    scpa.pack(fill="both",expand=True)

    # JSS logo image
    jss_image=Imgo( os.path.join( os.getcwd(), "Images\\jss.png"),160,140)

    # Background Image
    back2_image=Imgo( os.path.join( os.getcwd(), "Background\\front2b.jpg"),1700,810)
    scpa.create_image(0,0,image=back2_image,anchor="nw")

    # Welocome Text
    scpa.create_text( 220, 100-10, text="Welcome ,", font=("Book Antiqua",26,"bold"), anchor="nw", fill="#ff512a")
    scpa.create_text( 460, 80-10, text=ws[f"C{rec}"].value, font=("Book Antiqua",38,"bold"), anchor="nw", fill="#ff512a")

    # Profile page window
    pro=Imgo( os.path.join( os.getcwd(), "Images\\profile.jpg"),220,170)
    pro_bt=ctk.CTkButton(master=root,image=pro, text="Profile", text_font=("Book Antiqua",22,"bold"), compound="top",
                         corner_radius=10, bg_color="#fafafa", fg_color="#2d435b", hover_color="#fdbf38", text_color="white",
                         width=230, height=200, border_width=0, command= lambda : change(scpa,propage))
    pro_bt_win=scpa.create_window(420,200-10,anchor="nw",window=pro_bt)

    # Slot page window
    slot=Imgo( os.path.join( os.getcwd(), "Images\\clo.png"),220,170)
    slot_bt=ctk.CTkButton(master=root,image=slot, text="Slot Booking", text_font=("Book Antiqua",22,"bold"), compound="top",
                         corner_radius=10, bg_color="#fafafa", fg_color="#2d435b", hover_color="#fdbf38", text_color="white",
                         width=230, height=200, border_width=0, command= lambda : change(scpa,slotpage))
    slot_bt_win=scpa.create_window(740,200-10,anchor="nw",window=slot_bt)

    # Document page window
    doc=Imgo( os.path.join( os.getcwd(), "Images\\doc_img2.png"),220,170)
    doc_bt=ctk.CTkButton(master=root,image=doc, text="Documents", text_font=("Book Antiqua",22,"bold"), compound="top",
                         corner_radius=10, bg_color="#fafafa", fg_color="#2d435b", hover_color="#fdbf38", text_color="white",
                         width=230, height=200, border_width=0, command= lambda : change(scpa,docpage))
    doc_bt_win=scpa.create_window(1060,200-10,anchor="nw",window=doc_bt)

    root.mainloop()

def firstpage() :

    global user,pwrd,frpa

    # Defining Structure
    frpa=Canvas( root, width = wid, height = hgt, bg = "black", highlightcolor = "#3c5390", borderwidth = 0 )
    frpa.pack( fill = "both", expand = True )

    # Image on top
    jss_image = Imgo(os.path.join( os.getcwd(), "Images\\jss.png"), 135, 135)
    # Background Image
    back_image = Imgo(os.path.join( os.getcwd(), "Background\\front2a.jpg"), 1700, 810)
    entry_image = Imgo(os.path.join( os.getcwd(), "Images\\front22.png"), 550, 370)
    frpa.create_image( 0, 0, image = back_image , anchor = "nw")
    frpa.create_image(30, 20, image = jss_image, anchor = "nw")
    frpa.create_image(750, 150, image = entry_image, anchor = "nw")
    frpa.create_image(750, 350, image = entry_image, anchor = "nw")

    # Heading
    frpa.create_text(915,80,text="JSS ACADEMY OF TECHNICAL EDUCATION, NOIDA",font=("Book Antiqua",34,"bold"),fill="red")
    frpa.create_text(1025,180,text="JSS ADMISSION",font=("Book Antiqua",28,"bold"),fill="#0b4bf5")##0b4bf5
    frpa.create_text(970,305,text="Username",font=("Book Antiqua",22,"bold"),fill="white")
    frpa.create_text(970,505,text="Password",font=("Book Antiqua",22,"bold"),fill="white")
    
    # Entry of username and password
    user = ctk.CTkEntry( master = frpa, 
                          placeholder_text = "Roll Number", text_font = ( "Book Antiqua", 20, "bold" ), 
                           width = 230, height = 30, corner_radius = 10,
                            placeholder_text_color = "white", text_color = "white", 
                             fg_color = "#ffca62", bg_color = "#ffa900", 
                              border_color = "#162d50", border_width = 0)
    user_win = frpa.create_window( 880, 355, anchor = "nw", window = user )

    pwrd = ctk.CTkEntry( master = frpa, 
                          placeholder_text = "DOB(dd/mm/yyyy)", text_font = ( "Book Antiqua", 20, "bold" ), 
                           width = 250, height = 30, corner_radius = 10,
                            placeholder_text_color = "white", text_color = "white", 
                             fg_color = "#ffca62", bg_color = "#ffa900", 
                              border_color = "#162d50", border_width = 0, show = "*" )
    pwrd_win = frpa.create_window( 875, 555, anchor = "nw", window = pwrd )

    # Login button
    log_bt=ctk.CTkButton(master=root, text="Login", text_font=("Book Antiqua",25,"bold"), width=30, height=20,
                         corner_radius=15, text_color="white", bg_color="#dadada", fg_color="#162d50", 
                         hover_color="#0c3f8c", border_width=0, command = lambda : compare_rec( user.get(), pwrd.get()) )
    log_bt_win=frpa.create_window(960,675,anchor="nw",window=log_bt)

    root.mainloop()

if __name__ == "__main__" :

    # Defining Main theme of all widgets
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    wid = 1350
    hgt = 650

    global root
    root=ctk.CTk()
    root.title("JSS Counselling System")
    root.iconbitmap(os.path.join( os.getcwd(), "Images\\icon.ico"))
    root.geometry("1350x650+100+80")
    root.resizable(False,False)
    firstpage()