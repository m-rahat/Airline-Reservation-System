from tkinter import *
from tkinter import messagebox as mBox
from tkinter import simpledialog
import datetime

import tkinter as tk

import os
from os import path

import css


def init():  # ...............................................................................

    window.title('Main Menu')  # Main window title
    x_screen = (window.winfo_screenwidth() // 2) - (css.frame_center_W)
    y_screen = (window.winfo_screenheight() // 2) - (css.frame_center_H)

    window.geometry(
        "{}x{}+{}+{}".format(css.frame_width, css.frame_hight, x_screen, y_screen))  # Main window size & position
    window.config(bg=css.color_bg_newSession)
    window.resizable(False, False)

    create_LogIn_directory()

    # read in the entered global date .............................
    entry = ''
    with open('entered_data.txt', 'r') as text:  # create an output text file
        for line in text:
            entry = line

    items = line.split()

    entered_day = int(items[0].strip())  # remove whitespace characters i.e. '\n' at the start/end
    entered_mon = int(items[1].strip())
    entered_year = int(items[2].strip())

    date = datetime.datetime(entered_year, entered_mon, entered_day)  # year , month , day
    print(date)

    show_date = date.strftime("%A, %b %d %Y")

    # --- Current Date LABEL widget
    label_1 = Label(window, width=30, text='', fg=css.color_text, bg=css.color_bg_newSession)
    label_1.place(x=css.frame_center_W, y=610, anchor='center')
    label_1.config(font=("Helvetica", 20, "normal"))  # normal, bold, roman, italic, underline, and overstrike
    # label_1.config(text=str(show_date))  # display the entered date
    label_1.config(text=str(css.show_date))  # display the entered date
    # -------------------------------------------------------

    # --- Search Engine BUTTON widget ---
    Btn_1 = Button(window, width=20, text='Search Engine', fg=css.color_text, bg=css.color_btn, relief='ridge')
    Btn_1.config(font=("Helvetica", 26, "bold"))
    Btn_1.config(bd=8, relief='raised')  # flat, groove, raised, ridge, solid, or sunken
    Btn_1.config(command=btn_click_SearchEngine)  # calls btn_click_SearchEngine() when the button is clicked
    Btn_1.place(x=css.frame_center_W, y=50, anchor='center')

    # --- LOG-IN BUTTON widget ---
    Btn_2 = Button(window, width=20, text='Log in', fg=css.color_text, bg=css.color_btn, relief='ridge')
    Btn_2.config(font=("Helvetica", 26, "bold"))
    Btn_2.config(bd=8, relief='raised')  # flat, groove, raised, ridge, solid, or sunken
    # Btn_2.config(command=btn_click_LogIn)  # calls btn_click_LogIn() when the button is clicked
    Btn_2.config(command=lambda: btn_click_LogIn(label_user))
    Btn_2.place(x=css.frame_center_W, y=110, anchor='center')

    # --- Airlines BUTTON widget ---
    Btn_3 = Button(window, width=20, text='Airlines', fg=css.color_text, bg=css.color_btn, relief='ridge')
    Btn_3.config(font=("Helvetica", 26, "bold"))
    Btn_3.config(bd=8, relief='raised')  # flat, groove, raised, ridge, solid, or sunken
    Btn_3.config(command=btn_click_Airlines)  # calls btn_click_Airlines() when the button is clicked
    Btn_3.place(x=css.frame_center_W, y=170, anchor='center')

    # --- Airports BUTTON widget ---
    Btn_4 = Button(window, width=20, text='Airports', fg=css.color_text, bg=css.color_btn, relief='ridge')
    Btn_4.config(font=("Helvetica", 26, "bold"))
    Btn_4.config(bd=8, relief='raised')  # flat, groove, raised, ridge, solid, or sunken
    Btn_4.config(command=btn_click_Airports)  # calls btn_click_Airports() when the button is clicked
    Btn_4.place(x=css.frame_center_W, y=230, anchor='center')

    # --- NEW USER BUTTON widget ---
    Btn_5 = Button(window, width=20, text='Create Account', fg=css.color_text, bg=css.color_btn, relief='ridge')
    Btn_5.config(font=("Helvetica", 26, "bold"))
    Btn_5.config(bd=8, relief='raised')  # flat, groove, raised, ridge, solid, or sunken
    Btn_5.config(command=btn_click_NewUser)  # calls btn_click_NewUser() when the button is clicked
    Btn_5.place(x=css.frame_center_W, y=290, anchor='center')

    # --- LOGGED IN USER LABEL widget ---
    label_user = Label(window, width=15, text='', fg=css.color_text, bg=css.color_bg_newSession)
    label_user.place(x=css.frame_width - 100, y=26, anchor='center')
    label_user.config(font=("Helvetica", 16, "bold"))  # normal, bold, roman, italic, underline, and overstrike
    label_user.config(text=str("user: " + css.global_user))

    # --- NEW USER BUTTON widget ---
    Btn_6 = Button(window, width=16, text='view reservations', fg=css.color_text, bg=css.color_btn, relief='ridge')
    Btn_6.config(highlightbackground=css.color_bg_newSession)
    Btn_6.config(font=("Helvetica", 14, "normal"))
    Btn_6.config(bd=8, relief='raised')  # flat, groove, raised, ridge, solid, or sunken
    Btn_6.config(
        command=lambda: btn_click_view_reservations(label_user))  # calls btn_click_NewUser() when the button is clicked
    Btn_6.place(x=css.frame_width - 100, y=50, anchor='center')

    # --- Airports BUTTON widget ---
    Btn_7 = Button(window, width=20, text='prof.Mane Mode', fg=css.color_text, bg=css.color_btn, relief='ridge')
    Btn_7.config(font=("Helvetica", 26, "bold"))
    Btn_7.config(bd=8, relief='raised')  # flat, groove, raised, ridge, solid, or sunken
    Btn_7.config(command=btn_click_professors_view)  # calls btn_click_Airports() when the button is clicked
    Btn_7.place(x=css.frame_center_W, y=350, anchor='center')

    window.protocol("WM_DELETE_WINDOW", on_closing)


# --------------------------------------------------------------------------------------------------------------------
def on_closing():  # .................................................................................................
    window.destroy()
    # if mBox.askokcancel("Quit", "Do you want to quit?"):
    #     window.destroy()


# --------------------------------------------------------------------------------------------------------------------
def btn_click_LogIn(label_user):  # ................................................................................

    username = simpledialog.askstring("Input", "username?", parent=window)
    window.lift()

    if username is not None:
        print(username)

        if path.exists('passwords/' + username + '.txt'):

            entry = ''
            with open('passwords/' + username + '.txt', 'r') as text:  # create an output text file
                for line in text:
                    entry = line

            items = line.split()
            stored_password = items[0].strip()

            password = simpledialog.askstring("Input", "password?", parent=window)
            window.lift()

            if password is not None:

                if stored_password == password:
                    print('correct password: ' + password)

                    # ACCESS personal files here
                    css.global_user = username

                    label_user.config(text=str("user: " + css.global_user))

                    import reservations
                    reservations.r_window = Toplevel(window)  # new r_window - child of window
                    reservations.init(username, 'new_session')


                else:
                    messagebox.showerror("Error", "wrong password")
            else:
                messagebox.showerror("Error", "You did not provide password")
        else:
            messagebox.showerror("Error", "wrong username")
    else:
        messagebox.showerror("Error", "You did not provide username")

    window.grab_set()
    window.focus()
    window.grab_release()


# --------------------------------------------------------------------------------------------------------------------
def btn_click_NewUser():  # ..........................................................................................

    while True:
        username = simpledialog.askstring("Input", "create username", parent=window)
        window.lift()

        if not path.exists('passwords/' + str(username) + '.txt'):
            break
        else:
            messagebox.showerror("Error", "username already exists")

    if username is not None:
        print(username)

        password = simpledialog.askstring("Input", "create password", parent=window)
        window.lift()

        if password is not None:
            print(password)
            output = open('passwords/' + username + '.txt', 'w+')  # create an output text file
            output.write(password)  # write entered data to the file
            output.close()
        else:
            messagebox.showerror("Error", "You did not provide password")
    else:
        messagebox.showerror("Error", "You did not provide username")

    window.grab_set()
    window.focus()
    window.grab_release()


# --------------------------------------------------------------------------------------------------------------------
def create_LogIn_directory():  # .....................................................................................
    path = "passwords"
    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s " % path)


# --------------------------------------------------------------------------------------------------------------------
def btn_click_SearchEngine():  # .....................................................................................

    import search_engine
    search_engine.se_window = Toplevel(window)  # new se_window - child of window
    search_engine.init()


# window.grab_set()
# window.focus()
# window.grab_release()
# --------------------------------------------------------------------------------------------------------------------
def btn_click_Airlines():  # .........................................................................................

    import airlines
    airlines.a_window = Toplevel(window)  # new a_window - child of window
    airlines.init()

    # window.grab_set()
    # window.focus()
    # window.grab_release()


# --------------------------------------------------------------------------------------------------------------------
def btn_click_Airports():  # .........................................................................................

    import airports
    airports.ap_window = Toplevel(window)  # new ap_window - child of window

    # airports.ap_window.grab_set()
    airports.init()
    # airports.ap_window.grab_release()

    # window.focus()


# --------------------------------------------------------------------------------------------------------------------
def btn_click_view_reservations(label_user):  # ....................................................................

    if css.global_user == "please log-in":
        messagebox.showerror("Error", "You must log in first")
        return
    else:
        import reservations
        reservations.r_window = Toplevel(window)  # new r_window - child of window
        reservations.init(css.global_user, 'new_session')


# --------------------------------------------------------------------------------------------------------------------

def btn_click_professors_view():
    print("CLICKED ON PROFESSORS VIEW")
    import professor
    professor.p_window = Toplevel(window)  # new se_window - child of window
    professor.init()

# --------------------------------------------------------------------------------------------------------------------


# panes = ttk.Notebook( window )
# panes.pack()
# pane0 = ttk.Frame( panes )
# pane1 = ttk.Frame( panes )
# pane2 = ttk.Frame( panes )
# panes.add( pane0 , text="Search" )
# panes.add( pane1 , text="Airports" )
# panes.add( pane2 , text="Airlines" )
# pane3 = ttk.Frame( panes )
# panes.insert( 0 , pane3 , text = 'Log in' )
# print( panes.tab(1))
# ttk.Button( pane0 , text = 'Click Me').pack()


# window.option_add('*tearOff' , False)
# menuBar = Menu( window )
# window.config( menu = menuBar )
# file = Menu( menuBar )
# edit = Menu( menuBar )
# help_ = Menu( menuBar )
# menuBar.add_cascade( menu = file, label = 'File' )
# menuBar.add_cascade( menu = edit, label = 'Edit' )
# menuBar.add_cascade( menu = help_, label = 'Help' )
# file.add_command( label='New' , command = lambda: print('new file'))


























