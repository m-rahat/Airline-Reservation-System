import tkinter as tk
from tkinter import messagebox
import css
import DB_UTIL as db



global_airline_Name = ""
global_from_Airport = ""
global_to_Airport = ""
global_time_entry = ""
global_day_entry = ""
global_mon_entry = ""
global_year_entry = ""
global_fare_entry = ""
global_capacity_entry = ""


#Menu selections
from_airport_global = ""
to_airport_global = ""
airline_global = ""


# ---------------------------------------------------------------------------------------------------------------------
def entry_click( entry_id , entry_widget ):#...........................................................................

	if entry_id == 'Airline Name':
		entry_widget.delete('0', 'end')
		entry_widget.config( fg=css.color_text )

	elif entry_id == 'From Airport':
		entry_widget.delete('0', 'end')
		entry_widget.config( fg=css.color_text )

	elif entry_id == 'To Airport':
		entry_widget.delete('0', 'end')
		entry_widget.config( fg=css.color_text )

	elif entry_id == 'Departure Time':
		entry_widget.delete('0', 'end')
		entry_widget.config( fg=css.color_text )

	elif entry_id == 'day':
		entry_widget.delete('0', 'end')
		entry_widget.config( fg=css.color_text )

	elif entry_id == 'mon':
		entry_widget.delete('0', 'end')
		entry_widget.config( fg=css.color_text )

	elif entry_id == 'year':
		entry_widget.delete('0', 'end')
		entry_widget.config( fg=css.color_text )

	elif entry_id == 'Fare':
		entry_widget.delete('0', 'end')
		entry_widget.config( fg=css.color_text )

	elif entry_id == 'Capacity':
		entry_widget.delete('0', 'end')
		entry_widget.config( fg=css.color_text )
# ---------------------------------------------------------------------------------------------------------------------
def entry_check( entry_id , entry_widget , save_Btn ):#................................................................

	global global_airline_Name ; global global_from_Airport ; global global_to_Airport
	global global_time_entry ; global global_day_entry ; global global_mon_entry
	global global_year_entry ; global global_fare_entry ; global global_capacity_entry

	if entry_id == 'Airline Name':
		if '' == entry_widget.get():
			entry_widget.insert(0, 'Airline Name')
			entry_widget.config( fg=css.color_placeholder )
			global_airline_Name = ""
		else:
			global_airline_Name = entry_widget.get() 

	elif entry_id == 'From Airport':
		if '' == entry_widget.get():
			entry_widget.insert(0, 'From Airport')
			entry_widget.config( fg=css.color_placeholder )
			global_from_Airport = ""
		else:
			global_from_Airport = entry_widget.get()

	elif entry_id == 'To Airport':
		if '' == entry_widget.get():
			entry_widget.insert(0, 'To Airport')
			entry_widget.config( fg=css.color_placeholder )
			global_to_Airport = ""
		else:
			global_to_Airport = entry_widget.get()

	elif entry_id == 'Departure Time':
		if '' == entry_widget.get():
			entry_widget.insert(0, 'Departure Time')
			entry_widget.config( fg=css.color_placeholder )
			global_time_entry = ""
		else:
			global_time_entry = entry_widget.get()

	elif entry_id == 'day':
		if '' == entry_widget.get():
			entry_widget.insert(0, 'day')
			entry_widget.config( fg=css.color_placeholder )
			global_day_entry = ""
		else:
			global_day_entry = entry_widget.get()

	elif entry_id == 'mon':
		if '' == entry_widget.get():
			entry_widget.insert(0, 'mon')
			entry_widget.config( fg=css.color_placeholder )
			global_mon_entry = ""
		else:
			global_mon_entry = entry_widget.get()

	elif entry_id == 'year':
		if '' == entry_widget.get():
			entry_widget.insert(0, 'year')
			entry_widget.config( fg=css.color_placeholder )
			global_year_entry = ""
		else:
			global_year_entry = entry_widget.get()

	elif entry_id == 'Fare':
		if '' == entry_widget.get():
			entry_widget.insert(0, 'Fare')
			entry_widget.config( fg=css.color_placeholder )
			global_fare_entry = ""
		else:
			global_fare_entry = entry_widget.get()

	elif entry_id == 'Capacity':
		if '' == entry_widget.get():
			entry_widget.insert(0, 'Capacity')
			entry_widget.config( fg=css.color_placeholder )
			global_capacity_entry = ""
		else:
			global_capacity_entry = entry_widget.get()


	if (global_airline_Name != "" and global_from_Airport != "" and global_to_Airport != "" and global_time_entry  != ""
		and global_day_entry != "" and global_mon_entry != "" and global_year_entry != "" and global_fare_entry != ""
		and global_capacity_entry != ""):

		save_Btn.place( x=(css.frame_width+140)/2 , y=550 , anchor='center') 
	else: 
		save_Btn.place( x=(css.frame_width+140)/2 , y=-100 , anchor='center') 
# ---------------------------------------------------------------------------------------------------------------------
def enter_keyboardkKey( entry_ID ):  # ................................................................................
    print("Enterd value: " + str(entry_ID.get()))
    f_window.focus()
# ---------------------------------------------------------------------------------------------------------------------
def btn_click_saveFlight(save_Btn,user):#..............................................................................
	save_Btn.config(state='disabled')
	save_Btn.config(text="Flight Created!")

	date = global_year_entry +"-"+ global_mon_entry +"-"+ global_day_entry

	db.create_flights(global_airline_Name, date, global_time_entry, global_from_Airport,
					  global_to_Airport, global_capacity_entry, global_fare_entry, 'ON-TIME')
# ---------------------------------------------------------------------------------------------------------------------
def from_selection( value ):#..........................................................................................
	print(value)
	global from_airport_global
	from_airport_global = value
# ---------------------------------------------------------------------------------------------------------------------
def to_selection( value ):#..........................................................................................
	print(value)
	global to_airport_global
	to_airport_global = value
# ---------------------------------------------------------------------------------------------------------------------
def airline_selection( value ):#..........................................................................................
	print(value)
	global airline_global
	airline_global = value
# ---------------------------------------------------------------------------------------------------------------------






def init(admin_name,parent):#............................................................................................

	f_window.title('Create New Flight')    	#Main window title
	x_screen = (f_window.winfo_screenwidth() // 2) - (css.frame_center_W)
	y_screen = (f_window.winfo_screenheight() // 2) - (css.frame_center_H)

	width = css.frame_width + 140

	f_window.geometry("{}x{}+{}+{}".format( width , css.frame_hight , x_screen , y_screen ))	#Main window size & position
	f_window.config(bg=css.color_bg_newSession)
	f_window.resizable(False,False)


	#--- SAVE BUTTON DECLARED HERE
	save_Btn = tk.Button(f_window, width=20, text='Create Flight', fg=css.color_text, bg=css.color_btn, relief='ridge')
	save_Btn.config( highlightbackground=css.color_bg_newSession )
	save_Btn.config(font=("Helvetica", 18, "bold"))
	save_Btn.config(bd=8, relief='raised')  # flat, groove, raised, ridge, solid, or sunken
	save_Btn.config( command=lambda: btn_click_saveFlight(save_Btn,admin_name) ) 

    
	# --- AIRLINE NAME ENTRY widget ---
	airline_Name = tk.Entry( f_window, show=None, width=25, bg="#FFFFFF", fg=css.color_placeholder, exportselection=0, justify='center')
	airline_Name.config( font=( "Helvetica", 20 , "bold" ) )
	airline_Name.bind("<FocusIn>", lambda args: entry_click('Airline Name',airline_Name))
	airline_Name.bind("<FocusOut>", lambda args: entry_check('Airline Name',airline_Name,save_Btn))
	airline_Name.insert(0, 'Airline Name')
	airline_Name.bind('<Return>', lambda args: enter_keyboardkKey(airline_Name))
	airline_Name.place( x=width/2 , y=50 , anchor='n')   


	# --- FROM AIRPORT widget ---
	from_Airport = tk.Entry( f_window, show=None, width=25, bg="#FFFFFF", fg=css.color_placeholder, exportselection=0, justify='center')
	from_Airport.config( font=( "Helvetica", 20 , "bold" ) )
	from_Airport.bind("<FocusIn>", lambda args: entry_click('From Airport',from_Airport))
	from_Airport.bind("<FocusOut>", lambda args: entry_check('From Airport',from_Airport,save_Btn))
	from_Airport.insert(0, 'From Airport')
	from_Airport.bind('<Return>', lambda args: enter_keyboardkKey(from_Airport))
	from_Airport.place( x=width/2 , y=100 , anchor='n') 


	# --- TO AIRPORT ENTRY widget ---
	to_Airport = tk.Entry( f_window, show=None, width=25, bg="#FFFFFF", fg=css.color_placeholder, exportselection=0, justify='center')
	to_Airport.config( font=( "Helvetica", 20 , "bold" ) )
	to_Airport.bind("<FocusIn>", lambda args: entry_click('To Airport',to_Airport))
	to_Airport.bind("<FocusOut>", lambda args: entry_check('To Airport',to_Airport,save_Btn))
	to_Airport.insert(0, 'To Airport')
	to_Airport.bind('<Return>', lambda args: enter_keyboardkKey(to_Airport))
	to_Airport.place( x=width/2 , y=150 , anchor='n') 


	# --- TIME ENTRY widget ---
	time_entry = tk.Entry( f_window, show=None, width=25, bg="#FFFFFF", fg=css.color_placeholder, exportselection=0, justify='center')
	time_entry.config( font=( "Helvetica", 20 , "bold" ) )
	time_entry.bind("<FocusIn>", lambda args: entry_click('Departure Time',time_entry))
	time_entry.bind("<FocusOut>", lambda args: entry_check('Departure Time',time_entry,save_Btn))
	time_entry.insert(0, 'Departure Time')
	time_entry.bind('<Return>', lambda args: enter_keyboardkKey(time_entry))
	time_entry.place( x=width/2 , y=200 , anchor='n') 


	# --- Day ENTRY widget ---
	day_entry = tk.Entry( f_window, show=None, width=25, bg="#FFFFFF", fg=css.color_placeholder, exportselection=0, justify='center')
	day_entry.config( font=( "Helvetica", 20 , "bold" ) )
	day_entry.bind("<FocusIn>", lambda args: entry_click('day',day_entry))
	day_entry.bind("<FocusOut>", lambda args: entry_check('day',day_entry,save_Btn))
	day_entry.insert(0, 'day')
	day_entry.bind('<Return>', lambda args: enter_keyboardkKey(day_entry))
	day_entry.place( x=width/2 , y=250 , anchor='n')                     


	# --- Month ENTRY widget ---
	mon_entry = tk.Entry( f_window, show=None, width=25, bg="#FFFFFF", fg=css.color_placeholder, exportselection=0, justify='center')
	mon_entry.config( font=( "Helvetica", 20 , "bold" ) )
	mon_entry.bind("<FocusIn>", lambda args: entry_click('mon',mon_entry))
	mon_entry.bind("<FocusOut>", lambda args: entry_check('mon',mon_entry,save_Btn))
	mon_entry.insert(0, 'month')
	mon_entry.bind('<Return>', lambda args: enter_keyboardkKey(mon_entry))
	mon_entry.place( x=width/2 , y=300 , anchor='n')


	# --- Year ENTRY widget ---
	year_entry = tk.Entry( f_window, show=None, width=25, bg="#FFFFFF", fg=css.color_placeholder, exportselection=0, justify='center')
	year_entry.config( font=( "Helvetica", 20 , "bold" ) )
	year_entry.bind("<FocusIn>", lambda args: entry_click('year',year_entry))
	year_entry.bind("<FocusOut>", lambda args: entry_check('year',year_entry,save_Btn))
	year_entry.insert(0, 'year')
	year_entry.bind('<Return>', lambda args: enter_keyboardkKey(year_entry))
	year_entry.place( x=width/2 , y=350 , anchor='n')


	# --- Fare ENTRY widget ---
	fare_entry = tk.Entry( f_window, show=None, width=25, bg="#FFFFFF", fg=css.color_placeholder, exportselection=0, justify='center')
	fare_entry.config( font=( "Helvetica", 20 , "bold" ) )
	fare_entry.bind("<FocusIn>", lambda args: entry_click('Fare',fare_entry))
	fare_entry.bind("<FocusOut>", lambda args: entry_check('Fare',fare_entry,save_Btn))
	fare_entry.insert(0, 'Fare')
	fare_entry.bind('<Return>', lambda args: enter_keyboardkKey(fare_entry))
	fare_entry.place( x=width/2 , y=400 , anchor='n')


	# --- Capacity ENTRY widget ---
	capacity_entry = tk.Entry( f_window, show=None, width=25, bg="#FFFFFF", fg=css.color_placeholder, exportselection=0, justify='center')
	capacity_entry.config( font=( "Helvetica", 20 , "bold" ) )
	capacity_entry.bind("<FocusIn>", lambda args: entry_click('Capacity',capacity_entry))
	capacity_entry.bind("<FocusOut>", lambda args: entry_check('Capacity',capacity_entry,save_Btn))
	capacity_entry.insert(0, 'Capacity')
	capacity_entry.bind('<Return>', lambda args: enter_keyboardkKey(capacity_entry))
	capacity_entry.place( x=width/2 , y=450 , anchor='n')


	conn = db.db_connect()
	sqlcode = "SELECT AIRPORTNAME FROM AIRPORTS"
	cursor = conn.execute(sqlcode).fetchall()
	from_option_List = []
	for row in cursor:
		from_option_List.append(row[0])
	conn.close()

	from_option_List.insert(0,'all')

	variable1 = tk.StringVar(f_window)
	variable1.set("FROM")  # default value
	from_airport = tk.OptionMenu(f_window, variable1, *from_option_List , command=from_selection )
	from_airport.config( font=( "Helvetica", 15 ) )
	from_airport.config( bg=css.color_bg_newSession , width=12 , fg=css.color_text)
	from_airport.place(x=width/3-100, y=100, anchor='n')


	conn = db.db_connect()
	sqlcode = "SELECT AIRPORTNAME FROM AIRPORTS"
	cursor = conn.execute(sqlcode).fetchall()
	to_option_List = []
	for row in cursor:
		to_option_List.append(row[0])
	conn.close()

	to_option_List.insert(0,'all')

	variable1 = tk.StringVar(f_window)
	variable1.set("TO")  # default value
	to_airport = tk.OptionMenu(f_window, variable1, *to_option_List , command=to_selection )
	to_airport.config( font=( "Helvetica", 15 ) )
	to_airport.config( bg=css.color_bg_newSession , width=12 , fg=css.color_text)
	to_airport.place(x=width/3-100, y=150, anchor='n')


	conn = db.db_connect()
	sqlcode = "SELECT AIRLINENAME FROM AIRLINES"
	cursor = conn.execute(sqlcode).fetchall()
	airline_option_List = []
	for row in cursor:
		airline_option_List.append(row[0])
	conn.close()

	airline_option_List.insert(0,'all')

	variable1 = tk.StringVar(f_window)
	variable1.set("AIRLINES")  # default value
	from_airport = tk.OptionMenu(f_window, variable1, *airline_option_List , command=airline_selection )
	from_airport.config( font=( "Helvetica", 15 ) )
	from_airport.config( bg=css.color_bg_newSession , width=12 , fg=css.color_text)
	from_airport.place(x=width/3-100, y=50, anchor='n')
















	f_window.protocol("WM_DELETE_WINDOW", on_closing)
# ---------------------------------------------------------------------------------------------------------------------	
def on_closing():#.....................................................................................................
	f_window.destroy()
    # if messagebox.askokcancel("Quit", "Do you want to quit?"):
    #     f_window.destroy()
# ---------------------------------------------------------------------------------------------------------------------




























