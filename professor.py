import datetime
import sqlite3
import pandas
import tkcalendar
import css
from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
import os
from os import path
import tkinter as tk

import DB_UTIL as db



global_airline_Name = ""
global_airport_Name = ""

# ---------------------------------------------------------------------------------------------------------------------
def entry_click( entry_id , entry_widget ):#...........................................................................

    if entry_id == 'Airline Name':
        entry_widget.delete('0', 'end')
        entry_widget.config( fg=css.color_text )

    elif entry_id == 'Airport Name':
        entry_widget.delete('0', 'end')
        entry_widget.config( fg=css.color_text )
# ---------------------------------------------------------------------------------------------------------------------
def entry_check( entry_id , entry_widget , save_Btn ):#................................................................

    global global_airline_Name ; global global_airport_Name 

    if entry_id == 'Airline Name':
        if '' == entry_widget.get():
            entry_widget.insert(0, 'Airline Name')
            entry_widget.config( fg=css.color_placeholder )
            global_airline_Name = ""
        else:
            global_airline_Name = entry_widget.get() 

    elif entry_id == 'Airport Name':
        if '' == entry_widget.get():
            entry_widget.insert(0, 'Airport Name')
            entry_widget.config( fg=css.color_placeholder )
            global_airport_Name = ""
        else:
            global_airport_Name = entry_widget.get()


    # if (global_airline_Name != "" and global_airport_Name):

    #     save_Btn.place( x=(css.frame_width+140)/2 , y=550 , anchor='center') 
    # else: 
    #     save_Btn.place( x=(css.frame_width+140)/2 , y=-100 , anchor='center') 
# ---------------------------------------------------------------------------------------------------------------------
def enter_keyboardkKey( entry_ID ):  # ................................................................................
    print("Enterd value: " + str(entry_ID.get()))
    p_window.focus()
# ---------------------------------------------------------------------------------------------------------------------
def btn_click_createAirline(create_btn):#..............................................................................
    create_btn.config(state='disabled')
    create_btn.config(text="Airline Created!")

    db.create_airlines(global_airline_Name)
# ---------------------------------------------------------------------------------------------------------------------
def btn_click_createAirport(create_btn):#..............................................................................
    create_btn.config(state='disabled')
    create_btn.config(text="Airport Created!")

    db.create_airports(global_airport_Name, 'Some-City', 'Some-Country')
# ---------------------------------------------------------------------------------------------------------------------





def init():#............................................................................................................
    p_window.title('Professor View')  # Main window title
    x_screen = (p_window.winfo_screenwidth() // 2) - (css.frame_center_W)
    y_screen = (p_window.winfo_screenheight() // 2) - (css.frame_center_H)

    width = css.frame_width

    p_window.geometry("{}x{}+{}+{}".format(css.frame_width, css.frame_hight, x_screen, y_screen))  # Main window size & position
    p_window.config(bg=css.color_bg_newSession)
    p_window.resizable(False, False)


    # --- IMAGE LABEL widget ---
    logo1 = PhotoImage(file = 'construction.png')
    l_logo = Label(p_window, image=logo1, bg=css.color_bg_currentDate)
    l_logo.image = logo1
    #l_logo.place(x=width/2, y = 120, anchor='center')
    l_logo.place(x=width/2, y = 20, anchor='n')



    # --- AIRLINE NAME ENTRY widget ---
    airline_Name = tk.Entry( p_window, show=None, width=25, bg="#FFFFFF", fg=css.color_placeholder, exportselection=0, justify='center')
    airline_Name.config( font=( "Helvetica", 20 , "bold" ) )
    airline_Name.bind("<FocusIn>", lambda args: entry_click('Airline Name',airline_Name))
    airline_Name.bind("<FocusOut>", lambda args: entry_check('Airline Name',airline_Name,create_Airline_btn))
    airline_Name.insert(0, 'Airline Name')
    airline_Name.bind('<Return>', lambda args: enter_keyboardkKey(airline_Name))
    airline_Name.place( x=width/2 , y=300 , anchor='n')  


    # --- CREATE AIRLINE BUTTON widget ---
    create_Airline_btn = tk.Button(p_window, width=20, text='Create Airline', fg=css.color_text, bg=css.color_btn, relief='ridge')
    create_Airline_btn.config( highlightbackground=css.color_bg_newSession )
    create_Airline_btn.config(font=("Helvetica", 20, "bold"))
    create_Airline_btn.config(bd=8, relief='raised')  # flat, groove, raised, ridge, solid, or sunken
    create_Airline_btn.config( command=lambda: btn_click_createAirline(create_Airline_btn) ) 
    create_Airline_btn.place(x=css.frame_center_W, y=370, anchor='center') 



    # --- AIRPORT NAME ENTRY widget ---
    airport_Name = tk.Entry( p_window, show=None, width=25, bg="#FFFFFF", fg=css.color_placeholder, exportselection=0, justify='center')
    airport_Name.config( font=( "Helvetica", 20 , "bold" ) )
    airport_Name.bind("<FocusIn>", lambda args: entry_click('Airport Name',airport_Name))
    airport_Name.bind("<FocusOut>", lambda args: entry_check('Airport Name',airport_Name,create_Airport_btn))
    airport_Name.insert(0, 'Airport Name')
    airport_Name.bind('<Return>', lambda args: enter_keyboardkKey(airport_Name))
    airport_Name.place( x=width/2 , y=450 , anchor='n') 


    # --- CREATE AIRLINE BUTTON widget ---
    create_Airport_btn = tk.Button(p_window, width=20, text='Create Airport', fg=css.color_text, bg=css.color_btn, relief='ridge')
    create_Airport_btn.config( highlightbackground=css.color_bg_newSession )
    create_Airport_btn.config(font=("Helvetica", 20, "bold"))
    create_Airport_btn.config(bd=8, relief='raised')  # flat, groove, raised, ridge, solid, or sunken
    create_Airport_btn.config( command=lambda: btn_click_createAirport(create_Airport_btn) ) 
    create_Airport_btn.place(x=css.frame_center_W, y=520, anchor='center') 





















    p_window.protocol("WM_DELETE_WINDOW", on_closing)


def on_closing():  # .........................................................................
    # if messagebox.askokcancel("Quit", "Do you want to exit search engine?"):
    #     se_window.destroy()
    p_window.destroy()







































