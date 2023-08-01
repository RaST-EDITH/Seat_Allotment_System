from tkinter import *
import openpyxl as oxl
from tkinter import ttk
import customtkinter as ctk
from tabulate import tabulate
from PIL import Image ,ImageTk
from tkinter.messagebox import showerror

if __name__ == "__main__" :

    # Defining Main theme of all widgets
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    wid = 1350
    hgt = 650

    global root
    root=ctk.CTk()
    root.title("JSS Counselling System")
    root.iconbitmap("icon.ico")
    root.geometry("1350x650+100+80")
    root.resizable(False,False)
    firstpage()