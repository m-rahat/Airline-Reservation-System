import datetime
import sqlite3
import pandas
import tkcalendar
import css
from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar,DateEntry
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
import os
from os import path

import DB_UTIL as db
#import numpy as np


sort_by_global = "Flight_ID" 
from_airport_global = "all"
to_airport_global = "all"
cal_selected_date = ""
entered_Flight_ID_numb = 0

collected_IDs = set()



# def populate_window():#...............................................................................................

# 	conn = sqlite3.connect('Flight.db')

# 	if from_airport_global=="all" and to_airport_global=="all":

# 		sqlcode = "Select * from Flights WHERE Date >= ?" + " ORDER BY " + sort_by_global + " ASC"
# 		cursor = conn.execute(sqlcode, (cal_selected_date,)).fetchall()

# 	elif from_airport_global=="all":
# 		cursor = conn.execute("SELECT * FROM Flights WHERE To_Airport = ? AND Date >= ? ORDER BY "+sort_by_global+" ASC", (to_airport_global, cal_selected_date))

# 	elif to_airport_global=="all":
# 		cursor = conn.execute("SELECT * FROM Flights WHERE From_Airport = ? AND Date >= ? ORDER BY "+sort_by_global+" ASC", (from_airport_global, cal_selected_date))
# 	else:
# 		cursor = conn.execute("SELECT * FROM Flights WHERE From_Airport = ? AND To_Airport = ? AND DATE >= ? \
# 						   ORDER BY "+sort_by_global+" ASC", (from_airport_global,to_airport_global, cal_selected_date))

# 	content = ""
		
# 	for row in cursor:
# 		collected_IDs.add(row[0])

# 		content = content +"ID:"+ str(row[0]) +"  "+  str(row[1]) +"  "+ str(row[2]) +"  "+ str(row[3]) +"  "+ str(row[4])  \
# 					  	  +"  "+  str(row[5]) +"  "+ str(row[6]) +"  "+ str(row[7]) +"  "+ str(row[8]) +"  "+ str(row[9]) +"  "+ '\n' 
# 	conn.close()

# 	#print( collected_IDs )
# 	return content
# #---------------------------------------------------------------------------------------------------------------------
def populate_window():#...............................................................................................

	#conn = sqlite3.connect('Flight.db')
	conn = db.db_connect()

	if from_airport_global=="all" and to_airport_global=="all":

		sqlcode = "Select * from Flights WHERE Date >= ?" + " ORDER BY " + sort_by_global + " ASC"
		cursor = conn.execute(sqlcode, (cal_selected_date,)).fetchall()

	elif from_airport_global=="all":
		cursor = conn.execute("SELECT * FROM Flights WHERE To_Airport = ? AND Date >= ? ORDER BY "+sort_by_global+" ASC", (to_airport_global, cal_selected_date))

	elif to_airport_global=="all":
		cursor = conn.execute("SELECT * FROM Flights WHERE From_Airport = ? AND Date >= ? ORDER BY "+sort_by_global+" ASC", (from_airport_global, cal_selected_date))
	else:
		cursor = conn.execute("SELECT * FROM Flights WHERE From_Airport = ? AND To_Airport = ? AND DATE >= ? \
						   ORDER BY "+sort_by_global+" ASC", (from_airport_global,to_airport_global, cal_selected_date))

	content = ""

	collected_IDs.clear()

	for row in cursor:
		collected_IDs.add(row[0])

		content = content +"ID:"+ str(row[0]) +"  "+  str(row[1]) +"  "+ str(row[2]) +"  "+ str(row[3]) +"  "+ str(row[4])  \
					  	  +"  "+  str(row[5]) +"  "+ str(row[6]) +"  "+ str(row[7]) +"  "+ str(row[8]) + " " + '\n'
	conn.close()

	print(content)
	print(len(collected_IDs))

	return content
#---------------------------------------------------------------------------------------------------------------------


def from_selection( value ):
	print(value)
	global from_airport_global
	from_airport_global = value

def to_selection( value ):
	print(value)
	global to_airport_global
	to_airport_global = value

def sort_selection( value ):
	print(value)
	global sort_by_global
	sort_by_global = value


#---------------------------------------------------------------------------------------------------------------------
def get_table_colNames():#............................................................................................

	#sqlite_file = 'Flight.db'
	table_name = 'Flights'
	conn = db.db_connect()
	c = conn.cursor()
	c.execute('PRAGMA TABLE_INFO({})'.format(table_name))
	# collect names in a list
	names = [tup[1] for tup in c.fetchall()]

	conn.close()

	return names
#---------------------------------------------------------------------------------------------------------------------
# def get_FROM_Airports():#.............................................................................................
# 	# extract all VALID FROM Airport names into a list 
# #---------------------------------------------------------------------------------------------------------------------
# def get_TO_Airports():#...............................................................................................
# 	# extract all VALID TO Airport names into a list 
# #---------------------------------------------------------------------------------------------------------------------
def entry_ID_click(entry_ID):#.........................................................................................

	entry_ID.delete('0', 'end')				# delete everything from index 0 to last
	entry_ID.config( fg=css.color_text )	# adjust text color to active
#---------------------------------------------------------------------------------------------------------------------
def enter_keyboardkKey(entry_ID):#.....................................................................................
	print( "Enterd value: " + str(entry_ID.get()) )
	se_window.focus()	
#---------------------------------------------------------------------------------------------------------------------
def entry_ID_check(entry_ID , label , book_Btn):#.....................................................................
	
	print("entry ID check")

	if '' == entry_ID.get():
		entry_ID.insert(0, 'test')
		entry_ID.config( fg=css.color_placeholder )	

	try:
		flight_number = int(entry_ID.get())
	except ValueError:
		print("not a valid integer")
	else:
		print("entered value is: ", flight_number)

		# CHECK if the entered flight_number is among those displayed in the Text widget

		if flight_number in collected_IDs:
			global entered_Flight_ID_numb
			entered_Flight_ID_numb = flight_number
			fetch_one_record( flight_number,label , book_Btn )
		else:
			messagebox.showerror("Error", "Entered ID is not provided above!")

#---------------------------------------------------------------------------------------------------------------------
def fetch_one_record( flight_numb , label , book_Btn ):#..............................................................

	#sqlite_file = 'Flight.db'
	table_name = 'Flights'

	conn = db.db_connect()
	cursor = conn.cursor()

	#cursor.execute("SELECT Flight_ID FROM Flights WHERE Flight_ID = ?", (flight_numb,))
	cursor.execute("SELECT * FROM Flights WHERE Flight_ID = ?", (flight_numb,))
	data=cursor.fetchall()		#data=cursor.fetchone()
	if len(data)==0:
		#print( "flight number:"+str(flight_numb)+" does not exist")
		label.config( text="Flight ID: "+str(flight_numb)+" Does Not Exist" )
	else:

		flight = "Flight ID:" + str(data[0][0]) + "  " + str(data[0][2]) + "  "
		time = str(data[0][3])
		if time.endswith(':00'):
			time = time[:-3]

		flight = flight + time +"  "+ "from:"+str(data[0][4]) +"  to:"+str(data[0][5]) +"  seats:"+str(data[0][6]) \
                 +"  fare:$"+str(data[0][7])  +"  status:"+str(data[0][8])

		label.config(text=flight)


		btn_visibility_toggle( book_Btn , True)
	conn.close()
#---------------------------------------------------------------------------------------------------------------------
def btn_click_bookFlight( label , btn ):#.............................................................................
	print("Book FLIGHT")

	if css.global_user=="please log-in":
		messagebox.showerror("Error", "You must log in first in Main Menu")
		return


	if messagebox.askokcancel("Book", "Are you sure you want to book this flight?"):
		#label.config(text="Flight Booked!")
		btn.config(state='disabled')
		btn.config(text="Flight Booked!")

		###########################################################
		print("USER NAME:" + css.global_user)
		print("ENTERED FLIGHT NUMBER:" + str(entered_Flight_ID_numb))

		#conn = db.db_connect()
		#sqlcode_custflight= "INSERT INTO CUST_FLIGHT VALUES(?,?,?)"
		#sqlcode_updatecapacity = "UPDATE FLIGHTS SET CAPACITY = CAPACITY - 1 WHERE FLIGHT_ID = ?"
		#conn.execute(sqlcode_custflight, (css.global_user, entered_Flight_ID_numb, "SEARCH_ENGINE"))
		#conn.execute(sqlcode_updatecapacity, (entered_Flight_ID_numb,))
		#conn.close()

		db.book_a_flight(css.global_user, entered_Flight_ID_numb, "SEARCH_ENGINE")
		###########################################################
		#db.book_a_flight(con, 'Paul', 1, 'GUI')
		#db.book_a_flight(conn, css.global_user , entered_Flight_ID_numb , 'SEARCH')

#---------------------------------------------------------------------------------------------------------------------
def btn_visibility_toggle( btn , want_visible ):
	if want_visible:
		btn.place( x=(css.frame_width+140)/2 , y=785+120 , anchor='center')
	else:
		btn.pack_forget()
#---------------------------------------------------------------------------------------------------------------------


def init():#..........................................................................................................

	#-- GETTING THE DATE HERE THAT'S ALL
	with open('entered_data.txt', 'r') as text:  # create an output text file
		for line in text:
			entry = line

	items = line.split()

	entered_day = int(items[0].strip())  # remove whitespace characters i.e. '\n' at the start/end
	entered_mon = int(items[1].strip())
	entered_year = int(items[2].strip())
	date = datetime.datetime(entered_year, entered_mon, entered_day)  # year , month , day
	cal_selected_date = str(date.date())


	# -- MAKING GUI

	se_window.title('Search Engine')    	#Main window title
	x_screen = (se_window.winfo_screenwidth() // 2) - (css.frame_center_W)
	y_screen = (se_window.winfo_screenheight() // 2) - (css.frame_center_H) - 140

	width = css.frame_width + 140


	se_window.geometry("{}x{}+{}+{}".format( width , 970 , x_screen , y_screen ))	#Main window size & position
	se_window.config(bg=css.color_bg_newSession)
	se_window.resizable(False,False)

	x=120

	logo1 = PhotoImage(file = 'se.png')
	l_logo = Label(se_window, image=logo1, bg=css.color_bg_currentDate)
	l_logo.image = logo1
	l_logo.place(x=width/2, y = 15+x, anchor='center')

	# --- WELCOME INSTRUCTIONS LABEL widget ---
	label_1 = Label( se_window , width=60 , text='' , fg=css.color_text , bg=css.color_bg_newSession )
	label_1.place( x=width/2 , y=160+x , anchor='center' )
	label_1.config( font=( "Helvetica", 20 , "normal" ) )	# normal, bold, roman, italic, underline, and overstrike
	label_1.config( text=str('Please select the airports and date, then click search') )


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
	from_option_List.insert(0,'all')

	variable1 = StringVar(se_window)
	variable1.set("FROM")  # default value
	from_airport = OptionMenu(se_window, variable1, *from_option_List , command=from_selection )
	from_airport.config( font=( "Helvetica", 15 ) )
	from_airport.config( bg=css.color_bg_newSession , width=12 , fg=css.color_text)
	from_airport.place(x=width/3-15, y=200+x, anchor='center')


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
	to_option_List.insert(0,'all')

	variable2 = StringVar(se_window)
	variable2.set("TO")
	to_airport = OptionMenu(se_window, variable2, *to_option_List , command=to_selection )
	to_airport.config( font=( "Helvetica", 15 ) )
	to_airport.config( bg=css.color_bg_newSession , width=12 , fg=css.color_text)
	to_airport.place(x=width/2, y=200+x, anchor='center')


	# --- SELECT SORTING OPTION MENU widget ---
	flights_table_names = get_table_colNames() ;
	sort_option_List = flights_table_names #e.g. sort_option_List = ["Airline_ID", "From_Airport" , "To_Airport" , "Airline" ]
	variable3 = StringVar(se_window)
	variable3.set("SORT BY")
	sort = OptionMenu(se_window, variable3, *sort_option_List , command=sort_selection  )
	sort.config( font=( "Helvetica", 15 ) )
	sort.config( bg=css.color_bg_newSession , width=12 , fg=css.color_text)
	sort.place(x=width-(width/3)+15, y=200+x, anchor='center')


	# CALENDAR SECTION ..................................................
	cal = Calendar(se_window,
				   font="Arial 14", selectmode='day',
				   year=entered_year, month=entered_mon, day=entered_day, showweeknumbers=False, mindate= date)


	# style = ttk.Style(cal)
	# style.theme_use('calm')
	cal.place(x = width/2, y=320+x, anchor='center')


	results = Text(se_window, width=90, height=10, fg=css.color_text, bg=css.color_bg_reservations, yscrollcommand = set())
	results.config(font=("Helvetica", 16, "normal"))
	results.config(state=NORMAL)
	results.place(x=width/2, y=575 + x, anchor='center')
	results.insert(END,"RESULTS WILL PRINT HERE")
	results.configure(state='disabled')

	def calendar_select():
		global cal_selected_date
		cal_selected_date = str(cal.selection_get())
		print(cal_selected_date)

	def print_search_results(): # MAKES THE SEARCH RESULTS AND ADDS IT TO THE MAIN GUI WINDOW
		calendar_select()
		content = populate_window()
		results.config(state=NORMAL)
		results.delete('1.0', END)
		results.insert(END,content)
		results.configure(state='disabled')	
		book_Btn.config(text='Book Flight')
		book_Btn.config(state='normal')		# must be active, disabled, or normal
	# END CALENDAR SECTION .............................................


	# --- ENTER FLIGHT ID widget
	label_2 = Label( se_window , width=20 , text='' , fg=css.color_text , bg=css.color_bg_newSession )
	label_2.place( x=(width/2)-60 , y=706+x , anchor='center' )
	label_2.config( font=( "Helvetica", 20 , "normal" ) )	# normal, bold, roman, italic, underline, and overstrike
	label_2.config( text=str('Enter Flight ID') )


	# --- FLIGHT ID ENTRY widget ---
	entry_ID = Entry( se_window, show=None, width=5, bg='#FFFFFF', fg=css.color_placeholder, exportselection=0, justify='center')
	entry_ID.config( font=( "Helvetica", 20 , "normal" ) )
	entry_ID.bind('<Return>', lambda args: enter_keyboardkKey(entry_ID) )
	#entry_ID.bind('<KeyRelease>', lambda args: enter_keyboardkKey(entry_ID) ) # for dynamic realtime feedback capture
	entry_ID.bind("<FocusIn>", lambda args: entry_ID_click( entry_ID))
	entry_ID.bind("<FocusOut>", lambda args: entry_ID_check(entry_ID,label_3,book_Btn))
	entry_ID.insert(0, '0')
	entry_ID.place( x=(width/2)+48 , y=705+x , anchor='center') # alternative to entry_ID.pack()
	#entry_ID.focus_set() # to automatically focus on the widget at start up


	# --- SELECTED FLIGHT ID widget ---
	label_3 = Label( se_window , width=85 , text='' , fg=css.color_text , bg=css.color_bg_newSession )
	label_3.place( x=width/2 , y=747+x , anchor='center' )
	label_3.config( font=( "Helvetica", 16 , "normal" ) )	# normal, bold, roman, italic, underline, and overstrike
	label_3.config( text='' )


	# --- SEARCH BUTTON widget ---
	searchButton = Button( se_window , width=15, text='SEARCH', fg=css.color_text, bg=css.color_btn )
	searchButton.config( highlightbackground=css.color_bg_newSession )
	searchButton.config( font=( "Helvetica", 20 , "bold" ) )
	searchButton.config( bd=8, relief='raised' )
	searchButton.config( command=print_search_results )
	searchButton.place( x=width/2 , y=445+x , anchor='center')


	# --- BOOK FLIGHT BUTTON widget ---
	book_Btn = Button( se_window , width=15, text='Book Flight', fg=css.color_text, bg=css.color_btn, relief='ridge' )
	book_Btn.config( highlightbackground=css.color_bg_newSession )
	book_Btn.config( font=( "Helvetica", 20 , "bold" ) )
	book_Btn.config( bd=8, relief='raised' )					# flat, groove, raised, ridge, solid, or sunken
	book_Btn.config( command=lambda: btn_click_bookFlight(label_3,book_Btn) )
	#book_Btn.config( command=book)
	#book_Btn.bind('<Button-1>', hide_me)
	#book_Btn.place( x=css.frame_center_W , y=785+x , anchor='center')
	btn_visibility_toggle( book_Btn , False)


	# --- LOG-IN BUTTON widget ---
	login_Btn = Button(se_window, width=10, text='admin', fg=css.color_text, bg=css.color_btn)
	login_Btn.config( highlightbackground=css.color_bg_newSession )
	login_Btn.config(font=("Helvetica", 15, "bold"))
	login_Btn.config(bd=8, relief='raised')  # flat, groove, raised, ridge, solid, or sunken
	login_Btn.config(command=btn_click_LogIn)  # calls btn_click_LogIn() when the button is clicked
	login_Btn.place(x=100, y=26, anchor='center')

	# --- LOGGED IN USER LABEL widget ---
	label_user = Label( se_window , width=15 , text='' , fg=css.color_text , bg=css.color_bg_newSession )
	label_user.place( x=width-100 , y=26 , anchor='center' )
	label_user.config( font=( "Helvetica", 16 , "bold" ) )	# normal, bold, roman, italic, underline, and overstrike
	label_user.config( text=str("user: "+css.global_user) )



	se_window.protocol("WM_DELETE_WINDOW", on_closing)

def on_closing():#.........................................................................
    # if messagebox.askokcancel("Quit", "Do you want to exit search engine?"):
    #     se_window.destroy()
    se_window.destroy()
#------------------------------------------------------------------------------------------
def btn_click_LogIn():  # ....................................................................

    username = simpledialog.askstring("Input", "username?", parent=se_window)

    se_window.lift()

    if username is not None:
        print(username)

        if path.exists('passwords/' + username + '.txt'):

            entry = ''
            with open('passwords/' + username + '.txt', 'r') as text:  # create an output text file
                for line in text:
                    entry = line

            items = line.split()
            stored_password = items[0].strip()

            password = simpledialog.askstring("Input", "password?", parent=se_window)
            se_window.lift()

            if password is not None:

                if stored_password == password:
                    print('correct password: ' + password)

                    # ACCESS personal files here

                    import reservations
                    reservations.r_window = Toplevel(se_window)  # new r_window - child of se_window

                    #reservations.r_window.grab_set()
					
                    reservations.init(username,'search_engine')
                    #reservations.r_window.grab_release()


                else:
                    messagebox.showerror("Error", "wrong password")
            else:
                messagebox.showerror("Error", "You did not provide password")
        else:
            messagebox.showerror("Error", "wrong username")
    else:
        messagebox.showerror("Error", "You did not provide username")

    se_window.grab_set()
    se_window.focus()
    se_window.grab_release()
# ------------------------------------------------------------------------------------------


























