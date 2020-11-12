import datetime
import sqlite3
from os import path
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

import css

import DB_UTIL as db

airline = ""
results = Text()
collected_IDs = set()
entered_Flight_ID_numb = 0


def populate_window(value):  # .........................................................................................

    conn = db.db_connect()
    sqlcode = "SELECT * FROM FLIGHTS WHERE Airline_Name = ?"

    cursor = conn.execute(sqlcode, (value,))

    content = ""

    for row in cursor:
        collected_IDs.add(row[0])

        content = content + "ID:" + str(row[0]) + "  " + str(row[1]) + "  " + str(row[2]) + "  " + str(
            row[3]) + "  " + str(row[4]) \
                  + "  " + str(row[5]) + "  " + str(row[6]) + "  " + str(row[7]) + "  " + str(
            row[8]) + "  " + "  " + '\n'
    conn.close()
    return content
# ---------------------------------------------------------------------------------------------------------------------
def from_selection(value):#............................................................................................
    # print(value)
    global airline
    airline = value

    collected_IDs.clear()

    data = populate_window(value)
    print(data)
    results.config(state=NORMAL)
    results.delete('1.0', END)
    results.insert(END, data)
    results.configure(state='disabled')
# ---------------------------------------------------------------------------------------------------------------------
def entry_ID_click(entry_ID):#.........................................................................................

    entry_ID.delete('0', 'end')  # delete everything from index 0 to last
    entry_ID.config(fg=css.color_text)  # adjust text color to active
# ---------------------------------------------------------------------------------------------------------------------
def enter_keyboardkKey(
        entry_ID):  # .................................................................................................
    print("Enterd value: " + str(entry_ID.get()))
    a_window.focus()
# ---------------------------------------------------------------------------------------------------------------------
def entry_ID_check(entry_ID, label, book_Btn):  # .....................................................................

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
            fetch_one_record(flight_number, label, book_Btn)
        else:
            messagebox.showerror("Error", "Entered ID is not provided above!")
# ---------------------------------------------------------------------------------------------------------------------
def fetch_one_record(flight_numb, label, book_Btn):  # ................................................................

    # sqlite_file = 'Flight.db'
    table_name = 'Flights'
    # conn = sqlite3.connect(sqlite_file)
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

        flight = flight + time + "  " + "from:" + str(data[0][4]) + "  to:" + str(data[0][5]) + "  seats:" + str(
            data[0][6]) \
                 + "  fare:$" + str(data[0][7]) + "  status:" + str(data[0][8])

        label.config(text=flight)

        btn_visibility_toggle(book_Btn, True)
    conn.close()
# ---------------------------------------------------------------------------------------------------------------------
def btn_click_bookFlight(label, btn):  # .............................................................................
    print("Book FLIGHT")

    if css.global_user == "please log-in":
        messagebox.showerror("Error", "You must log in first in Main Menu")
        return

    if messagebox.askokcancel("Book", "Are you sure you want to book this flight?"):
        # label.config(text="Flight Booked!")
        btn.config(state='disabled')
        btn.config(text="Flight Booked!")

    print(css.global_user)
    print(entered_Flight_ID_numb)

    db.book_a_flight(css.global_user, entered_Flight_ID_numb, "AIRLINE_GUI")
# ---------------------------------------------------------------------------------------------------------------------
def btn_visibility_toggle(book_Btn, want_visible):
    if want_visible:
        book_Btn.config(text='Book Flight')
        book_Btn.config(state='normal')  # must be active, disabled, or normal
        book_Btn.place(x=(css.frame_width + 80) / 2, y=455 + 120, anchor='center')
    else:
        book_Btn.pack_forget()


# ---------------------------------------------------------------------------------------------------------------------
def get_table_colNames():#.............................................................................................

    sqlite_file = 'Flight.db'
    table_name = 'Flights'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute('PRAGMA TABLE_INFO({})'.format(table_name))
    # collect names in a list
    names = [tup[1] for tup in c.fetchall()]

    conn.close()
    return names
# ---------------------------------------------------------------------------------------------------------------------






def init():  # .......................................................................................................

    print(get_table_colNames())

    # -- GETTING THE DATE HERE THAT'S ALL
    with open('entered_data.txt', 'r') as text:  # create an output text file
        for line in text:
            entry = line

    items = line.split()

    entered_day = int(items[0].strip())  # remove whitespace characters i.e. '\n' at the start/end
    entered_mon = int(items[1].strip())
    entered_year = int(items[2].strip())
    date = datetime.datetime(entered_year, entered_mon, entered_day)  # year , month , day
    cal_selected_date = str(date.date())

    a_window.title('Airlines')  # Main window title
    x_screen = (a_window.winfo_screenwidth() // 2) - (css.frame_center_W)
    y_screen = (a_window.winfo_screenheight() // 2) - (css.frame_center_H)

    width = css.frame_width + 80

    a_window.geometry("{}x{}+{}+{}".format(width, css.frame_hight, x_screen, y_screen))  # Main window size & position
    a_window.config(bg=css.color_bg_newSession)
    a_window.resizable(False, False)

    x = 120

    # HERE IS CODE FOR THE IMAGE. USE SUITABLE IMAGE ANG FILENAME HERE PLEASE
    logo1 = PhotoImage(file='airlines.png')
    l_logo = Label(a_window, image=logo1, bg=css.color_bg_currentDate)
    l_logo.image = logo1
    l_logo.place(x=width / 2, y=10, anchor='n')

    a_window.protocol("WM_DELETE_WINDOW", on_closing)

    # HERE IS THE CODE FOR THE ADMIN BUTTON
    # --- LOG-IN BUTTON widget ---
    login_Btn = Button(a_window, width=10, text='admin', fg=css.color_text, bg=css.color_btn)
    login_Btn.config(highlightbackground=css.color_bg_newSession)
    login_Btn.config(font=("Helvetica", 15, "bold"))
    login_Btn.config(bd=8, relief='raised')  # flat, groove, raised, ridge, solid, or sunken
    login_Btn.config(command=btn_click_LogIn)  # calls btn_click_LogIn() when the button is clicked
    login_Btn.place(x=120, y=26, anchor='center')

    # HERE IS THE CODE FOR DISPLAY LABEL
    label_1 = Label(a_window, width=60, text='', fg=css.color_text, bg=css.color_bg_newSession)
    label_1.place(x=css.frame_center_W, y=128 + x, anchor='center')
    label_1.config(font=("Helvetica", 18, "normal"))  # normal, bold, roman, italic, underline, and overstrike
    label_1.config(text=str('AVAILABLE FLIGHTS FOR YOUR SELECTED AIRLINE'))

    # CONNECT TO DATABASE AND UPDATE THE AIRLINE LIST
    # conn = sqlite3.connect('Flight.db');

    conn = db.db_connect()

    sqlcode = "SELECT AIRLINENAME FROM AIRLINES"
    cursor = conn.execute(sqlcode).fetchall()
    airline_option_List = []
    for row in cursor:
        airline_option_List.append(row[0])
    conn.close()

    variable1 = StringVar(a_window)
    variable1.set("AIRLINES")  # default value
    from_airport = OptionMenu(a_window, variable1, *airline_option_List, command=from_selection)
    from_airport.config(font=("Helvetica", 16))
    from_airport.config(bg=css.color_bg_newSession, width=15, fg=css.color_text)
    from_airport.place(x=120, y=52, anchor='center')

    # --- RESULTS TEXT BOX widget ---
    global results
    results = Text(a_window, width=90, height=12, fg=css.color_text, bg=css.color_bg_reservations, yscrollcommand=set())
    results.config(font=("Helvetica", 15, "normal"))
    results.config(state=NORMAL)
    results.place(x=width/2, y=244 + x, anchor='center')
    results.insert(END, "RESULTS HERE")
    results.configure(state='disabled')

    # --- ENTER FLIGHT ID widget ---
    label_2 = Label(a_window, width=20, text='', fg=css.color_text, bg=css.color_bg_newSession)
    label_2.place(x=css.frame_center_W - 60, y=380 + x, anchor='center')
    label_2.config(font=("Helvetica", 20, "normal"))  # normal, bold, roman, italic, underline, and overstrike
    label_2.config(text=str('Enter Flight ID'))

    # --- FLIGHT ID ENTRY widget ---
    entry_ID = Entry(a_window, show=None, width=5, bg='#FFFFFF', fg=css.color_placeholder, exportselection=0,
                     justify='center')
    entry_ID.config(font=("Helvetica", 20, "normal"))
    entry_ID.bind('<Return>', lambda args: enter_keyboardkKey(entry_ID))
    # entry_ID.bind('<KeyRelease>', lambda args: enter_keyboardkKey(entry_ID) ) # for dynamic realtime feedback capture
    entry_ID.bind("<FocusIn>", lambda args: entry_ID_click(entry_ID))
    entry_ID.bind("<FocusOut>", lambda args: entry_ID_check(entry_ID, label_3, book_Btn))
    entry_ID.insert(0, '0')
    entry_ID.place(x=css.frame_center_W + 48, y=380 + x, anchor='center')  # alternative to entry_ID.pack()
    # entry_ID.focus_set() # to automatically focus on the widget at start up

    # --- SELECTED FLIGHT ID widget ---
    label_3 = Label(a_window, width=110, text='', fg=css.color_text, bg=css.color_bg_newSession)
    label_3.place(x=width / 2, y=420 + x, anchor='center')
    label_3.config(font=("Helvetica", 16, "normal"))  # normal, bold, roman, italic, underline, and overstrike
    label_3.config(text='')

    # --- BOOK FLIGHT BUTTON widget ---
    book_Btn = Button(a_window, width=15, text='Book Flight', fg=css.color_text, bg=css.color_btn, relief='ridge')
    book_Btn.config(highlightbackground=css.color_bg_newSession)
    book_Btn.config(font=("Helvetica", 20, "bold"))
    book_Btn.config(bd=8, relief='raised')  # flat, groove, raised, ridge, solid, or sunken
    book_Btn.config(command=lambda: btn_click_bookFlight(label_3, book_Btn))

    # --- LOGGED IN USER LABEL widget ---
    label_user = Label(a_window, width=15, text='', fg=css.color_text, bg=css.color_bg_newSession)
    label_user.place(x=width - 140, y=26, anchor='center')
    label_user.config(font=("Helvetica", 16, "bold"))  # normal, bold, roman, italic, underline, and overstrike
    label_user.config(text=str("user: " + css.global_user))

    btn_visibility_toggle(book_Btn, False)


def on_closing():  # .........................................................................
    a_window.destroy()


#   if messagebox.askokcancel("Quit", "Do you want to quit?"):
#      a_window.destroy()
# ------------------------------------------------------------------------------------------


# ------------------COPY PASTED CODE FOR ADMIN BUTTON---------------------------------
def btn_click_LogIn():  # ....................................................................

    username = simpledialog.askstring("Input", "username?", parent=a_window)

    a_window.lift()

    if username is not None:
        print(username)

        if path.exists('passwords/' + username + '.txt'):

            entry = ''
            with open('passwords/' + username + '.txt', 'r') as text:  # create an output text file
                for line in text:
                    entry = line

            items = line.split()
            stored_password = items[0].strip()

            password = simpledialog.askstring("Input", "password?", parent=a_window)
            a_window.lift()

            if password is not None:

                if stored_password == password:
                    print('correct password: ' + password)

                    # ACCESS personal files here

                    import reservations
                    reservations.r_window = Toplevel(a_window)  # new r_window - child of a_window
                    reservations.init(username, 'airline_gui')


                else:
                    messagebox.showerror("Error", "wrong password")
            else:
                messagebox.showerror("Error", "You did not provide password")
        else:
            messagebox.showerror("Error", "wrong username")
    else:
        messagebox.showerror("Error", "You did not provide username")

    a_window.grab_set()
    a_window.focus()
    a_window.grab_release()
    # -------------------------------------------------------------------------------------------
