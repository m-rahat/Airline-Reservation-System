import css
from tkinter import messagebox
from tkinter import *
import tkinter as tk
import sqlite3
import DB_UTIL as db

x = 120

collected_IDs = set()
entered_Flight_ID_numb = 0
user_name = ""


def entry_ID_click(entry_ID):#.........................................................................................
    entry_ID.delete('0', 'end')  # delete everything from index 0 to last
    entry_ID.config(fg=css.color_text)  # adjust text color to active
# ---------------------------------------------------------------------------------------------------------------------
def enter_keyboardkKey( entry_ID , cancel_btn ):  # ...................................................................
    print("Enterd value: " + str(entry_ID.get()))
    r_window.focus()
# ---------------------------------------------------------------------------------------------------------------------
def fetch_one_record(flight_numb, label, cancel_Btn):#..................................................................

    #sqlite_file = 'Flight.db'
    table_name = 'Flights'
    #conn = sqlite3.connect(sqlite_file)
    conn = db.db_connect()
    cursor = conn.cursor()

    # cursor.execute("SELECT Flight_ID FROM Flights WHERE Flight_ID = ?", (flight_numb,))
    cursor.execute("SELECT * FROM Flights WHERE Flight_ID = ?", (flight_numb,))
    data = cursor.fetchall()  # data=cursor.fetchone()
    if len(data) == 0:
        label.config(text="Flight ID: " + str(flight_numb) + " Does Not Exist")
    else:
        flight = "Flight ID:" + str(data[0][0]) + "  " + str(data[0][2]) + "  "

        time = str(data[0][3])
        if time.endswith(':00'):
            time = time[:-3]

        flight = flight + time +"  "+ "from:"+str(data[0][4]) +"  to:"+str(data[0][5]) +"  seats:"+str(data[0][6]) \
                  +"  fare:$"+str(data[0][7])  +"  status:"+str(data[0][8])

        label.config(text=flight)

        cancel_Btn.config(state='normal')
        cancel_Btn.config(text="Cancel Flight")

        btn_visibility_toggle(cancel_Btn, True)
# ---------------------------------------------------------------------------------------------------------------------
def entry_ID_check(entry_ID, label , cancel_Btn):#.....................................................................

    print("entry ID check")

    if '' == entry_ID.get():
        entry_ID.insert(0, 'test')
        entry_ID.config(fg=css.color_placeholder)

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
            fetch_one_record(flight_number,label, cancel_Btn)
            entered_Flight_ID_numb = flight_number
        else:
            messagebox.showerror("Error", "Entered ID is not provided above!")
# ---------------------------------------------------------------------------------------------------------------------
def btn_visibility_toggle( btn , want_visible ):#......................................................................
	if want_visible:
		btn.place( x=(css.frame_width+140)/2 , y=450 , anchor='center')
	else:
		btn.pack_forget()
# ---------------------------------------------------------------------------------------------------------------------
def btn_click_cancelFlight(label, btn, comments, user):#...............................................................
    print("Cancel FLIGHT")
    if messagebox.askokcancel("Cancel", "Are you sure you want to cancel this flight?"):
        btn.config(state='disabled')
        btn.config(text="Flight Cancelled!")

        print("CANCEL BUTTON CLICKED")
        print(css.global_user)
        print(entered_Flight_ID_numb)

        global user_name

        if user_name == 'search_admin':
            print("here1")
            messagebox.showerror("ERROR", "SEARCH ADMIN CANNOT CANCEL A FLIGHT")
        elif user_name == 'airline_admin':
            print("here2")
            db.cancel_flight_admin(entered_Flight_ID_numb)
            populate_airline_admin_gui(comments, label, user)
        else:
            print("here3")
            db.cancel_reservation_passenger(css.global_user, entered_Flight_ID_numb)
            populate_customer_reservations_gui(comments, user)

        #populate_customer_reservations_gui(comments, user)
# ---------------------------------------------------------------------------------------------------------------------
def create_NEW_Flight( username ):#....................................................................................

    import new_flight
    new_flight.f_window = Toplevel(r_window)  # new f_window - child of r_window
    new_flight.init(username,'reservations')
# ---------------------------------------------------------------------------------------------------------------------


# def polulate_customer():#..............................................................................................
#     quote = """HAMLET: To be, or not to be--that is the question:
# 	Whether 'tis nobler in the mind to suffer
# 	The slings and arrows of outrageous fortune
# 	Or to take arms against a sea of troubles
# 	And by opposing end them. To die, to sleep--
# 	No more--and by a sleep to say we end
# 	The heartache, and the thousand natural shockss
# 	That flesh is heir to. 'Tis a consummation
# 	Devoutly to be wished."""

#     return quote


# # ------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------
def init(user, origin):  # .........................................................................

    print('welcome' + user)

    global user_name
    user_name = user

    r_window.title('Reservations')  # Main window title
    x_screen = (r_window.winfo_screenwidth() // 2) - (css.frame_center_W)
    y_screen = (r_window.winfo_screenheight() // 2) - (css.frame_center_H)

    width = css.frame_width + 140

    r_window.geometry("{}x{}+{}+{}".format(width, css.frame_hight, x_screen, y_screen))  # Main window size & position
    r_window.config(bg=css.color_bg_reservations)
    r_window.resizable(False, False)


    # --- WELCOME USERNAME LABEL widget
    label_1 = Label(r_window, width=60, text='', fg=css.color_text, bg=css.color_bg_reservations)
    label_1.place(x=width/2, y=20, anchor='n')
    label_1.config(font=("Helvetica", 20, "normal"))  # normal, bold, roman, italic, underline, and overstrike
    label_1.config(text=str('Welcome ' + user.capitalize() + ' here are your reservations:'))  # display the entered date


    # --- RESERVATIONs LIST TEST widget
    comments = Text(r_window, width=95, height=15, fg=css.color_text, bg=css.color_bg_newSession, yscrollcommand=set())
    comments.config(font=("Helvetica", 15, "normal"))
    comments.place(x=width/2, y=70, anchor='n')
    comments.configure(state="normal")


    #CANCEL BUTTON DECLARED HERE
    cancel_Btn = Button(r_window, width=20, text='Cancel Flight', fg=css.color_text, bg=css.color_btn, relief='ridge')
    cancel_Btn.config( highlightbackground=css.color_bg_newSession )
    cancel_Btn.config(font=("Helvetica", 18, "bold"))
    cancel_Btn.config(bd=8, relief='raised')  # flat, groove, raised, ridge, solid, or sunken
    cancel_Btn.config( command=lambda: btn_click_cancelFlight(label_3,cancel_Btn,comments,user) )

    if origin == "search_engine" and user == 'search_admin':
        populate_search_engine_admin_gui(comments, cancel_Btn)
    elif origin == "search_engine" and user != 'search_admin':
        messagebox.showerror("ERROR", "INVALID ADMIN")
        populate_customer_reservations_gui(comments, user)
    elif origin == "airline_gui" and user != "airline_admin":
        messagebox.showerror("ERROR", "INVALID ADMIN")
    elif origin == "airline_gui" and user == 'airline_admin':
        populate_airline_admin_gui(comments , label_1 , user )
    elif origin == "new_session":
        populate_customer_reservations_gui(comments, user)


    # --- ENTER FLIGHT ID widget
    label_2 = Label(r_window, width=20, text='', fg=css.color_text, bg=css.color_bg_reservations)
    label_2.place(x=css.frame_center_W - 60, y=250 + x, anchor='center')
    label_2.config(font=("Helvetica", 20, "normal"))  # normal, bold, roman, italic, underline, and overstrike
    label_2.config(text=str('Enter Flight ID'))


    # --- SELECTED FLIGHT ID widget ---
    label_3 = Label( r_window , width=85 , text='' , fg=css.color_text , bg=css.color_bg_reservations )
    label_3.place( x=width/2 , y=415 , anchor='center' )
    label_3.config( font=( "Helvetica", 16 , "normal" ) )   # normal, bold, roman, italic, underline, and overstrike
    label_3.config( text='' )


    # --- FLIGHT ID ENTRY widget ---
    entry_ID = Entry(r_window, show=None, width=5, bg='#FFFFFF', fg=css.color_placeholder, exportselection=0,
                     justify='center')
    entry_ID.config(font=("Helvetica", 20, "normal"))
    entry_ID.bind('<Return>', lambda args: enter_keyboardkKey(entry_ID,cancel_Btn))
    # entry_ID.bind('<KeyRelease>', lambda args: enter_keyboardkKey(entry_ID) ) # for dynamic realtime feedback capture
    entry_ID.bind("<FocusIn>", lambda args: entry_ID_click(entry_ID))
    entry_ID.bind("<FocusOut>", lambda args: entry_ID_check(entry_ID, label_3, cancel_Btn))
    entry_ID.insert(0, '0')
    entry_ID.place(x=css.frame_center_W + 48, y=250 + x, anchor='center')  # alternative to entry_ID.pack()
    # entry_ID.focus_set() # to automatically focus on the widget at start up

    if user == 'search_admin':
        btn_visibility_toggle(cancel_Btn, FALSE)

    r_window.protocol("WM_DELETE_WINDOW", on_closing)


def on_closing():  # ..................................................................................................
    r_window.destroy()
# if messagebox.askokcancel("Quit", "Do you want to quit?"):
#     r_window.destroy()
# ---------------------------------------------------------------------------------------------------------------------
def populate_airline_admin_gui(comments , welcome_label , user):#......................................................
    
    welcome_label.config(text=str('Welcome ' + user.capitalize() + ' here are ALL existing reservations:'))

    conn = db.db_connect()

    collected_IDs.clear()

    # sqlcode = "SELECT FLIGHTS.FLIGHT_ID, USERNAME, DATE, TIME, FROM_AIRPORT, TO_AIRPORT, STATUS FROM FLIGHTS_BOOKED INNER JOIN FLIGHTS WHERE FLIGHTS_BOOKED.Flight_ID = FLIGHTS.Flight_ID"
    sqlcode = "SELECT * FROM FLIGHTS INNER JOIN CUST_FLIGHT WHERE CUST_FLIGHT.Flight_ID = FLIGHTS.Flight_ID"
    cursor = conn.execute(sqlcode).fetchall()

    comments.delete(1.0, tk.END)

    content=""
    for row in cursor:
        collected_IDs.add(row[0])

        content = content +"ID:"+ str(row[0]) +"  "+  str(row[1]) +"  "+ str(row[2]) +"  "

        time = str(row[3])
        if time.endswith(':00'):
            time = time[:-3]

        content = content + time +"  "+  str(row[4]) +"  "+ str(row[5]) +"  "+ str(row[6]) +"  "+ str(row[7]) \
                  +"  "+ str(row[8]) +"  "+ str(row[9]) +"  "+ str(row[11]) + " " + '\n'

        comments.insert(tk.END, content)

    # --- Create FLIGHT BUTTON widget ---
    create_flight_Btn = Button(r_window, width=20, text='Create New Flight', fg=css.color_text, bg=css.color_btn, relief='ridge')
    create_flight_Btn.config(highlightbackground=css.color_bg_newSession)
    create_flight_Btn.config(font=("Helvetica", 18, "bold"))
    create_flight_Btn.config(bd=8, relief='raised')  # flat, groove, raised, ridge, solid, or sunken
    create_flight_Btn.place( x=(css.frame_width+140)/2 , y=490 , anchor='center')
    create_flight_Btn.config( command=lambda: create_NEW_Flight(user) )

    conn.close()

    # # --- CANCEL FLIGHT BUTTON widget ---
    # cancel_Btn = Button(r_window, width=15, text='Cancel Flight', fg=css.color_text, bg=css.color_btn, relief='ridge')
    # cancel_Btn.config(highlightbackground=css.color_bg_newSession)
    # cancel_Btn.config(font=("Helvetica", 20, "bold"))
    # cancel_Btn.config(bd=8, relief='raised')  # flat, groove, raised, ridge, solid, or sunken
    # cancel_Btn.config(command=lambda: btn_click_cancelFlight(cancel_Btn))  # calls btn_click_saveCurrentDate() when the button is clicked
# ---------------------------------------------------------------------------------------------------------------------
def populate_search_engine_admin_gui(comments, cancelbutton):#.........................................................

    conn = db.db_connect()

    collected_IDs.clear()

    sqlcode = "SELECT * FROM FLIGHTS INNER JOIN CUST_FLIGHT ON FLIGHTS.FLIGHT_ID = CUST_FLIGHT.Flight_ID WHERE METHOD =?"

    se = "SEARCH_ENGINE"
    cursor = conn.execute(sqlcode, (se,)).fetchall()

    for row in cursor:
        collected_IDs.add(row[0])

        reservations = str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(
            row[4]) + " " + str(row[5]) + " " + str(row[6]) + " " + str(row[7]) + " " + str(row[8]) + " " + str(
            row[9]) + " " + str(row[11]) + '\n'
        comments.insert(tk.END, reservations)

    conn.close()

# ---------------------------------------------------------------------------------------------------------------------
def populate_customer_reservations_gui(comments, username):#...........................................................

    conn = db.db_connect()
    collected_IDs.clear()

    sqlcode = "SELECT * FROM FLIGHTS INNER JOIN CUST_FLIGHT ON FLIGHTS.Flight_ID = CUST_FLIGHT.Flight_ID WHERE CUST_FLIGHT.USERNAME = ?"

    cursor = conn.execute(sqlcode, (username,)).fetchall()
    comments.delete(1.0, tk.END)

    for row in cursor:
        collected_IDs.add(row[0])

        reservations = str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(
            row[4]) + " " + str(row[5]) + " " + str(row[6]) + " " + str(row[7]) + " " + str(row[8]) + " " + str(
            row[9]) + " " + str(row[11]) + '\n'
        comments.insert(tk.END, reservations)

    conn.close()

    # --- CANCEL FLIGHT BUTTON widget ---
    cancel_Btn = Button(r_window, width=15, text='Cancel Flight', fg=css.color_text, bg=css.color_btn, relief='ridge')
    cancel_Btn.config(highlightbackground=css.color_bg_newSession)
    cancel_Btn.config(font=("Helvetica", 20, "bold"))
    cancel_Btn.config(bd=8, relief='raised')  # flat, groove, raised, ridge, solid, or sunken
    cancel_Btn.config(command=lambda: btn_click_cancelFlight(cancel_Btn))  # calls btn_click_saveCurrentDate() when the button is clicked
# ---------------------------------------------------------------------------------------------------------------------


















