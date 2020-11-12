import css
from tkinter import messagebox
from tkinter import *
import sqlite3
import tkinter as tk

import tkinter
import DB_UTIL as db






def init():#...............................................................................

	ap_window.title('Airports')    	#Main window title
	x_screen = (ap_window.winfo_screenwidth() // 2) - (css.frame_center_W)
	y_screen = (ap_window.winfo_screenheight() // 2) - (css.frame_center_H)

	ap_window.geometry("{}x{}+{}+{}".format( css.frame_width , css.frame_hight , x_screen , y_screen ))	#Main window size & position
	ap_window.config(bg=css.color_bg_newSession)
	ap_window.resizable(False,False) 

	x=120

	image = PhotoImage(file = 'airport.png')
	l_logo = Label(ap_window, image=image, bg=css.color_bg_currentDate)
	l_logo.image = image
	l_logo.place(x=css.frame_center_W, y = 15+x, anchor='center')


	# --- WELCOME INSTRUCTIONS LABEL widget ---
	label_1 = Label( ap_window , width=60 , text='' , fg=css.color_text , bg=css.color_bg_newSession )
	label_1.place( x=css.frame_center_W , y=170+x , anchor='center' )
	label_1.config( font=( "Helvetica", 20 , "normal" ) )	# normal, bold, roman, italic, underline, and overstrike
	label_1.config( text=str('Welcome traveler, please select your airport') )


	# --- SELECT FROM AIRPORT OPTION MENU widget ---
	#CONNECT TO DATABASE AND UPDATE THE FLIGHT LIST
	#conn = sqlite3.connect('Flight.db');

	conn = db.db_connect()

	sqlcode = "SELECT AIRPORTNAME FROM AIRPORTS"
	cursor = conn.execute(sqlcode).fetchall()
	from_option_List = []
	for row in cursor:
		from_option_List.append(row[0])
	conn.close()
	#from_option_List = ["all", "JFK", "LAG", "LAX", "DC", "DUB", "DFW"]	##### this must be populated from the SQLite3

	##### NEED THIS FUNCTION ################################################
	#PLEASE hardcode "all" as the 1st menu option
	#from_option_List = get_FROM_Airports()
	#########################################################################


	variable1 = StringVar(ap_window)
	variable1.set("FROM AIRPORT")  # default value
	from_airport = OptionMenu(ap_window, variable1, *from_option_List , command=from_selection )
	from_airport.config( font=( "Helvetica", 17 ) )
	from_airport.config( bg=css.color_bg_newSession , width=20 , fg=css.color_text)
	from_airport.place(x=css.frame_center_W-130, y=208+x, anchor='center')


	# --- SELECT TO AIRPORT OPTION MENU widget ---
	# CONNECT TO DATABASE AND UPDATE THE FLIGHT LIST
	#conn = sqlite3.connect('Flight.db');

	conn = db.db_connect()
	sqlcode = "SELECT AIRPORTNAME FROM AIRPORTS"
	cursor = conn.execute(sqlcode).fetchall()
	to_option_List = []
	for row in cursor:
		to_option_List.append(row[0])
	conn.close()
	#to_option_List = ["all", "JFK", "LAG", "LAX", "DC", "DUB", "DFW"]	##### this must be populated from the SQLite3

	##### NEED THIS FUNCTION ################################################
	#PLEASE hardcode "all" as the 1st menu option
	#to_option_List = get_TO_Airports()
	#########################################################################

	variable2 = StringVar(ap_window)
	variable2.set("TO AIRPORT")
	to_airport = OptionMenu(ap_window, variable2, *to_option_List , command=to_selection )
	to_airport.config( font=( "Helvetica", 17 ) )
	to_airport.config( bg=css.color_bg_newSession , width=20 , fg=css.color_text)
	to_airport.place(x=css.frame_center_W+130, y=208+x, anchor='center')


	# --- Current Date LABEL widget
	label_date = Label(ap_window, width=30, text='', fg=css.color_text, bg=css.color_bg_newSession)
	label_date.place(x=css.frame_center_W, y=610, anchor='center')
	label_date.config(font=("Helvetica", 20, "normal"))  # normal, bold, roman, italic, underline, and overstrike
	label_date.config(text=str(css.show_date))  # display the entered date
    # -------------------------------------------------------



	ap_window.protocol("WM_DELETE_WINDOW", on_closing)
	
def on_closing():#.........................................................................
	ap_window.destroy()
    # if messagebox.askokcancel("Quit", "Do you want to quit?"):
    #     ap_window.destroy()
#------------------------------------------------------------------------------------------



def from_selection( value ):#.........................................................................................
	print("selected:" + value)
	global from_airport_global
	from_airport_global = value

	import airport_in
	airport_in.port_window = Toplevel(ap_window)  # new port_window - child of ap_window
	airport_in.init( from_airport_global , 'in' )

#---------------------------------------------------------------------------------------------------------------------
def parentfunction():
	print('child closed')


	
def to_selection( value ):#.........................................................................................
	print("selected:" + value)
	global to_airport_global
	to_airport_global = value

	import airport_out
	airport_out.port_window = Toplevel(ap_window)  # new port_window - child of ap_window
	airport_out.init( to_airport_global , 'out' )

	
	#airport_out.port_window.lift()
	#airport_out.port_window.tkrise()
	#ap_window.withdraw()
#---------------------------------------------------------------------------------------------------------------------































