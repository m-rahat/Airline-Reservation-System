import css
from tkinter import messagebox
from tkinter import *
import tkinter as tk
import sqlite3
import DB_UTIL as db

sort_by_global = "Airline_ID"


def polulate_Inbound( origin ):#............................................................................
	
	#conn = sqlite3.connect('Flight.db')

	#cursor = conn.execute("SELECT * FROM Flights")

	conn = db.db_connect()
	cursor = conn.execute("SELECT * FROM Flights WHERE To_Airport = ?", (origin,))

	content = ""
		
	for row in cursor:
		content = content +"ID:"+ str(row[0]) +"  "+  str(row[1]) +"  "+ str(row[2]) +"  "+ str(row[3]) +"  "+ str(row[4])  \
					  	  +"  "+  str(row[5]) +"  "+ str(row[6]) +"  "+ str(row[7]) +"  "+ '\n' 

	conn.close()
	return content
#------------------------------------------------------------------------------------------
def polulate_Outbound( origin ):#............................................................................

	#conn = sqlite3.connect('Flight.db')

	conn = db.db_connect()
	#cursor = conn.execute("SELECT * FROM Flights")
	cursor = conn.execute("SELECT * FROM Flights WHERE From_Airport = ?", (origin,))

	content = ""
		
	for row in cursor:
		content = content +"ID:"+ str(row[0]) +"  "+  str(row[1]) +"  "+ str(row[2]) +"  "+ str(row[3]) +"  "+ str(row[4])  \
					  	  +"  "+  str(row[5]) +"  "+ str(row[6]) +"  "+ str(row[7]) +"  "+ '\n' 
	conn.close()
	return content
#------------------------------------------------------------------------------------------
def get_table_colNames():#............................................................................................

	sqlite_file = 'Flight.db'
	table_name = 'Flights'
	#conn = sqlite3.connect(sqlite_file)
	conn = db.db_connect()
	c = conn.cursor()
	c.execute('PRAGMA TABLE_INFO({})'.format(table_name))
	# collect names in a list
	names = [tup[1] for tup in c.fetchall()]

	conn.close()
	return names
#---------------------------------------------------------------------------------------------------------------------








def init( origin , direction):#........................................................................


	#print( 'Welcome to '+ origin )

	port_window.title('Inbound Airport '+origin)    	#Main port_window title


	if direction=='in':
		x_screen = (port_window.winfo_screenwidth() // 2) - (css.frame_center_W) - 600
	elif direction=='out':
		x_screen = (port_window.winfo_screenwidth() // 2) - (css.frame_center_W) + 600

	y_screen = (port_window.winfo_screenheight() // 2) - (css.frame_center_H) - 140

	port_window.geometry("{}x{}+{}+{}".format( css.frame_width , 970 , x_screen , y_screen ))	#Main window size & position
	port_window.config(bg=css.color_bg_reservations)
	port_window.resizable(False,False) 

	port_window.lift()

	print( get_table_colNames() )


	# --- WELCOME USERNAME LABEL widget
	label_1 = Label( port_window , width=60 , text='' , fg=css.color_text , bg=css.color_bg_reservations )
	label_1.place( x=css.frame_center_W , y=40 , anchor='n' )
	label_1.config( font=( "Helvetica", 20 , "normal" ) )	# normal, bold, roman, italic, underline, and overstrike
	label_1.config( text=str( 'Welcome to ' + origin ) )	#display the entered date


	# --- INBOUND FLIGHTs LABEL widget ---
	label_2 = Label( port_window , width=60 , text='' , fg=css.color_text , bg=css.color_bg_reservations )
	label_2.place( x=css.frame_center_W-200 , y=90 , anchor='n' )
	label_2.config( font=( "Helvetica", 20 , "normal" ) )	# normal, bold, roman, italic, underline, and overstrike
	label_2.config( text=str( 'Arriving Flights' ) )	#display the entered date


	# --- INBOUND FLIGHTs TEXT widget ---
	comments_1 = Text( port_window , width=80 , height=15 , fg=css.color_text , bg=css.color_bg_newSession  )
	comments_1.config( font=( "Helvetica", 14 , "normal" ) )
	comments_1.place( x=css.frame_center_W , y=120 , anchor='n' ) # n, ne, e, se, s, sw, w, nw, center

	quote = polulate_Inbound( origin )	# this must be adjusted to ONLY show bookings made via Search Engine
	comments_1.insert(tk.END, quote)
	comments_1.configure(state='disabled')


	# --- OUTBOUND FLIGHTs LABEL widget ---
	label_2 = Label( port_window , width=60 , text='' , fg=css.color_text , bg=css.color_bg_reservations )
	label_2.place( x=css.frame_center_W-200 , y=450 , anchor='n' )
	label_2.config( font=( "Helvetica", 20 , "normal" ) )	# normal, bold, roman, italic, underline, and overstrike
	label_2.config( text=str( 'Departing Flights' ) )	#display the entered date


	# --- OUTBOUND FLIGHTs TEXT widget ---
	comments_2 = Text( port_window , width=80 , height=15 , fg=css.color_text , bg=css.color_bg_newSession  )
	comments_2.config( font=( "Helvetica", 14 , "normal" ) )
	comments_2.place( x=css.frame_center_W , y=480 , anchor='n' ) # n, ne, e, se, s, sw, w, nw, center

	quote = polulate_Outbound( origin )	# this must be adjusted to ONLY show bookings made via Search Engine
	comments_2.insert(tk.END, quote)
	comments_2.configure(state='disabled')


	# --- Current Date LABEL widget
	label_date = Label(port_window, width=30, text='', fg=css.color_text, bg=css.color_bg_reservations)
	label_date.place(x=css.frame_center_W, y=950, anchor='center')
	label_date.config(font=("Helvetica", 20, "normal"))  # normal, bold, roman, italic, underline, and overstrike
	label_date.config(text=str(css.show_date))  # display the entered date
    # -------------------------------------------------------



	

	port_window.protocol("WM_DELETE_WINDOW", on_closing)


	get_table_colNames()


	port_window.mainloop()



	
def on_closing():#.........................................................................
	port_window.destroy()
    # if messagebox.askokcancel("Quit", "Do you want to quit?"):
    #     port_window.destroy()
#------------------------------------------------------------------------------------------




















