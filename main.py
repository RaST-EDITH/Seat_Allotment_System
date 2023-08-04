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
    user=Entry(root,font=("Book Antiqua",20,"bold"),width=17,fg="white",bd=0,bg="#ffca62")
    pwrd=Entry(root,font=("Book Antiqua",20,"bold"),width=17,fg="white",bd=0,bg="#ffca62")
    user_win=frpa.create_window(890,355,anchor="nw",window=user)
    pwrd_win=frpa.create_window(890,555,anchor="nw",window=pwrd)
    user.insert(0, "Roll Number")
    pwrd.insert(0, "DOB(dd/mm/yyyy)")

    # Login button
    log_bt=ctk.CTkButton(master=root, text="Login", text_font=("Book Antiqua",25,"bold"), width=30, height=20,
                         corner_radius=15, text_color="white", bg_color="#dadada", fg_color="#162d50", 
                         hover_color="#0c3f8c", border_width=0, command = nxt_widg)
    log_bt_win=frpa.create_window(960,675,anchor="nw",window=log_bt)

    # binding entry boxes
    user.bind("<FocusIn>",ent_clr)
    user.bind("<FocusOut>",ent_place)
    pwrd.bind("<FocusIn>",ent_clr1)
    pwrd.bind("<FocusOut>",ent_place1)
    
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