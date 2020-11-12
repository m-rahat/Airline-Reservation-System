from tkinter import *  	# import everything from tkinter package
from tkinter import ttk
import tkinter as tk
import _tkinter
from tkinter import messagebox

import css



import datetime
now = datetime.datetime.now()
enteredDate = datetime.datetime.now()



def launch_session():#.....................................................................

	#subprocess.call(['python3' , 'new_session.py'])
	reset_entry( 'day' ) ; reset_entry( 'month' ) ; reset_entry( 'year' ) 

	import new_session
	new_session.window = Toplevel( root_frame ) # new window - child of root_frame 

	new_session.init()
	#root_frame.lower()

	return
#------------------------------------------------------------------------------------------
def btn_click_saveCurrentDate():#..........................................................
#	print("Button Clicked")

	entered_day = Entry_day.get().strip() #remove whitespace characters i.e. '\n' at the start/end
	entered_mon = Entry_mon.get().strip()
	entered_year = Entry_year.get().strip()

	if entered_day=='day' or entered_day=='' :
		messagebox.showinfo( title='Day Entry', message='please enter day')
		reset_entry( 'day' )
		return
	if entered_mon=='month' or entered_mon=='' :
		messagebox.showinfo( title='Month Entry', message='please enter a month')
		reset_entry( 'month' )
		return
	if entered_year=='year' or entered_year=='' :
		messagebox.showinfo( title='Year Entry', message='please enter a year')
		reset_entry( 'year' )
		return

	try:
		enteredDate = datetime.datetime( int(entered_year), int(entered_mon), int(entered_day) ) #; print( enteredDate )
		date = enteredDate.strftime("%A, %b %d %Y")
		css.show_date = date
		label_1.config( text=str(date) )	#display the entered date

		output = open( 'entered_data.txt' , 'w+' )	#create an output text file
		output.write( entered_day +' '+entered_mon+' '+entered_year )	#write entered data to the file
		output.close()

		launch_session()

	except ValueError:
		messagebox.showinfo( title='Date Error', message='invalid date - try again')
		reset_entry( 'day' ) ; reset_entry( 'month' ) ; reset_entry( 'year' )
		return

	# Entry_day.config( fg=color_placeholder )
	# Entry_mon.config( fg=color_placeholder )
	# Entry_year.config( fg=color_placeholder )
#------------------------------------------------------------------------------------------
def entry_click( entry_id ):#..............................................................
	#print("Entry Clicked")

	if entry_id == 'day':
		Entry_day.delete('0', 'end')
		Entry_day.config( fg=css.color_text )

	elif entry_id == 'mon':
		Entry_mon.delete('0', 'end')
		Entry_mon.config( fg=css.color_text )

	elif entry_id == 'year':
		Entry_year.delete('0', 'end')
		Entry_year.config( fg=css.color_text )
#------------------------------------------------------------------------------------------
def entry_check( entry_id ):#..............................................................
	#print("Entry Check Clicked")

	if entry_id == 'day':
		if '' == Entry_day.get():
			Entry_day.insert(0, 'day')
			Entry_day.config( fg=css.color_placeholder )			
	elif entry_id == 'mon':
		if '' == Entry_mon.get():
			Entry_mon.insert(0, 'month')
			Entry_mon.config( fg=css.color_placeholder )
	elif entry_id == 'year':
		if '' == Entry_year.get():
			Entry_year.insert(0, 'year')
			Entry_year.config( fg=css.color_placeholder )
#------------------------------------------------------------------------------------------
def reset_entry( entry_id ):#..............................................................

	if entry_id == 'day':
		Entry_day.delete('0', 'end')	#clear the entered string from the Entry window from index 0 to last
		Entry_day.insert(0, 'day')		#write 'day' into the Entry window
		Entry_day.config( fg=css.color_placeholder )

	elif entry_id == 'month':
		Entry_mon.delete('0', 'end') 
		Entry_mon.insert(0, 'month')	
		Entry_mon.config( fg=css.color_placeholder )

	elif entry_id == 'year':
		Entry_year.delete('0', 'end')
		Entry_year.insert(0, 'year')
		Entry_year.config( fg=css.color_placeholder )

	root_frame.focus()
#------------------------------------------------------------------------------------------
# def hide_me(event):#.......................................................................
#     event.widget.pack_forget()
# #------------------------------------------------------------------------------------------
def on_closing():#.........................................................................
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root_frame.destroy()
#------------------------------------------------------------------------------------------
def enter_keyboardkKey( entry_ID ):  # ................................................................................
    print("Enterd value: " + str(entry_ID.get()))
    root_frame.focus()
# ---------------------------------------------------------------------------------------------------------------------


root_frame = tk.Tk()            		#Define a GUI window named root_frame
root_frame.title('Current Date')    	#Main window title
x_screen = (root_frame.winfo_screenwidth() // 2) - (css.frame_center_W)
y_screen = (root_frame.winfo_screenheight() // 2) - (css.frame_center_H)
root_frame.geometry("{}x{}+{}+{}".format( css.frame_width , css.frame_hight , x_screen , y_screen ))	#Main window size & position
root_frame.config(bg=css.color_bg_currentDate) 
root_frame.resizable(False,False) 									#Set the background color of root window

# --- Logo LABEL widget ---
logo =tk.PhotoImage(file = 'clock.png')       				#Define the picture of logo,but only supports '.png' and '.gif'
l_logo=tk.Label(root_frame,image = logo,bg=css.color_bg_currentDate) 		#Set a label to show the logo picture
l_logo.place( x=css.frame_center_W , y=140 , anchor='center')  	#Position the Logo Label in the center

# --- Enter Current Data LABEL widget ---
label_0 = tk.Label( root_frame , width=20 , text='Enter Current Date' , fg=css.color_text , bg=css.color_bg_currentDate )
label_0.place( x=css.frame_center_W , y=290 , anchor='center' )
label_0.config( font=( "Helvetica", 26 , "bold" ) )

# --- Day ENTRY widget ---
Entry_day = tk.Entry( root_frame, show=None, width=19, bg="#FFFFFF", fg=css.color_placeholder, exportselection=0, justify='center')
Entry_day.config( font=( "Helvetica", 26 , "bold" ) )
#Entry_day.bind("<FocusIn>", lambda args: Entry_day.delete('0', 'end'))
Entry_day.bind("<FocusIn>", lambda args: entry_click('day'))
Entry_day.bind("<FocusOut>", lambda args: entry_check('day'))
Entry_day.bind('<Return>', lambda args: enter_keyboardkKey(Entry_day))
Entry_day.insert(0, 'day')
Entry_day.place( x=css.frame_center_W , y=330 , anchor='center')                     

# --- Month ENTRY widget ---
Entry_mon = tk.Entry( root_frame, show=None, width=19, bg="#FFFFFF", fg=css.color_placeholder, exportselection=0, justify='center')
Entry_mon.config( font=( "Helvetica", 26 , "bold" ) )
Entry_mon.bind("<FocusIn>", lambda args: entry_click('mon'))
Entry_mon.bind("<FocusOut>", lambda args: entry_check('mon'))
Entry_mon.bind('<Return>', lambda args: enter_keyboardkKey(Entry_mon))
Entry_mon.insert(0, 'month')
Entry_mon.place( x=css.frame_center_W , y=380 , anchor='center')

# --- Year ENTRY widget ---
Entry_year = tk.Entry( root_frame, show=None, width=19, bg="#FFFFFF", fg=css.color_placeholder, exportselection=0, justify='center')
Entry_year.config( font=( "Helvetica", 26 , "bold" ) )
Entry_year.bind("<FocusIn>", lambda args: entry_click('year'))
Entry_year.bind("<FocusOut>", lambda args: entry_check('year'))
Entry_year.bind('<Return>', lambda args: enter_keyboardkKey(Entry_year))
Entry_year.insert(0, 'year')
Entry_year.place( x=css.frame_center_W , y=430 , anchor='center')

# --- Save Current Date BUTTON widget ---
Btn = tk.Button( root_frame , width=20, text='Save Current Date', fg=css.color_text, bg=css.color_btn, relief='ridge' )
Btn.config( font=( "Helvetica", 26 , "bold" ) )
Btn.config( bd=8, relief='raised' )					# flat, groove, raised, ridge, solid, or sunken
Btn.config( command=btn_click_saveCurrentDate )		# calls btn_click_saveCurrentDate() when the button is clicked
#Btn.bind('<Button-1>', hide_me)
Btn.place( x=css.frame_center_W , y=510 , anchor='center')

# --- Current Date LABEL widget
label_1 = tk.Label( root_frame , width=30 , text='' , fg=css.color_text , bg=css.color_bg_currentDate )
label_1.place( x=css.frame_center_W , y=610 , anchor='center' )
label_1.config( font=( "Helvetica", 20 , "normal" ) )	# normal, bold, roman, italic, underline, and overstrike



root_frame.protocol("WM_DELETE_WINDOW", on_closing)
root_frame.mainloop()





	










































