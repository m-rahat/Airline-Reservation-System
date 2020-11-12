import sqlite3
from sqlite3 import Error
import os
from tkinter import *

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'flight.sqlite3')

def db_connect(db_path=DEFAULT_PATH):
    con = None
    try:
        con = sqlite3.connect(db_path)
        #print(sqlite3.version)
    except Error as e:
        print(e)
    return con
    
    
def cd_table(createsql):
    con = db_connect()
    try:
        cur = con.cursor()
        cur.execute(createsql)
    except Error as e:
        print(e)
    con.close()


def queryexec(querysql): #This is how you can run run RAW SQL to the database, I don't recommend getting too comfortable with this though ;)
    con = db_connect()
    try:
        cur = con.cursor()
        cur.execute(querysql)
    except Error as e:
        print(e)
    return cur.fetchall()
    con.close()


""" IGNORE
def create_customer(con, userName):
    query = 'INSERT INTO Customer (UserName) VALUES (?)'
    try:
        cur = con.cursor()
        cur.execute(query, (userName,))
    except Error as e:
        print(e)
    con.close()
"""
def create_airports(airportName, cityName, country):     # Method to add/create an airport
    con = db_connect()
    query = 'INSERT INTO Airports (AirportName, CityName, Country) VALUES (?, ?, ?)'
    try:
        cur = con.cursor()
        cur.execute(query, (airportName, cityName, country))
        con.commit()
    except Error as e:
        print(e)
    con.close()

def create_airlines(airlineName):  # Method to add/create an airline
    con = db_connect()
    query = 'INSERT INTO Airlines (AirlineName) VALUES (?)'
    try:
        cur = con.cursor()
        cur.execute(query, (airlineName,))
        con.commit()
    except Error as e:
        print(e)
    con.close()

def create_flights(airlineName, date, time, From_Airport, To_Airport, capacity, fare, status):    # Method to add/create a flight
    con = db_connect()
    #query = 'INSERT INTO Flights (AirlineID, Origin, Destination, CurrentPassengers, Capacity, FlightStatus, Fare, FlightDate, Departuretime, FlightTime) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    query = 'INSERT INTO Flights (Airline_Name, Date, Time, From_Airport, To_Airport, Capacity, Fare, Status) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
    try:
        cur = con.cursor()
        cur.execute(query, (airlineName, date, time, From_Airport, To_Airport, capacity, fare, status))
        con.commit()
    except Error as e:
        print(e)
    con.close()


def check_capacity(con, row):
    query = "SELECT Capacity FROM Flights WHERE Flight_ID=?"
    try:
        cur = con.cursor()
        cur.execute(query, (row,))
        res = cur.fetchall()
        return res[0][0]
    except Error as e:
        print(e)

#Lets add a way to add a customer to a flight

def book_a_flight(userName, flightID, method):
    con = db_connect()
    query = 'INSERT INTO Cust_Flight(UserName, Flight_ID, Method) VALUES(?, ?, ?);'
    flightval = check_capacity(con, flightID)
    #MAKE SURE YOU CHANGE CAPACITY
    query2 = "UPDATE Flights SET Capacity=? WHERE Flight_ID=?"
    if flightval > 0:
        try:
            cur = con.cursor()
            cur.execute(query, (userName, flightID, method))
            con.commit()
            flightval -= 1
            cur.execute(query2, (flightval, flightID))
            con.commit()
            con.close()
        except Error as e:
            print(e)
    else:
        con.close()
        messagebox.showerror("Error", "FLIGHT IS FULL")
        #return "Flight is full!"
    

def cancel_flight_admin(flightID):
    con = db_connect()
    query = "UPDATE Flights SET Status='Cancelled' WHERE Flight_ID=?"
    try:
        cur = con.cursor()
        cur.execute(query, (flightID,))
        con.commit()
    except Error as e:
        print(e)
    con.close()

def cancel_reservation_passenger(userName, flightID): #Delete row in cust_flight, and increase the capacity
    con = db_connect()
    query = "DELETE FROM Cust_Flight WHERE UserName=? AND Flight_ID=?"
    flightval = check_capacity(con, flightID)
    #MAKE SURE YOU CHANGE CAPACITY
    query2 = "UPDATE Flights SET Capacity=? WHERE Flight_ID=?"
   
    try:
        cur = con.cursor()
        cur.execute(query, (userName, flightID))
        con.commit()
        flightval += 1
        cur.execute(query2, (flightval, flightID))
        con.commit()
        con.close()
    except Error as e:
        print(e)
    
    con.close()
    #return "Flight is full!"

def get_user_reservation(userName):
    con = db_connect()
    query = "SELECT * FROM Cust_Flight WHERE UserName=?"
    try:
        cur = con.cursor()
        cur.execute(query, (userName,))
        res = cur.fetchall()
    except Error as e:
        print(e)
    con.close()
    return res

def get_full_user_reservation(userName):
    con = db_connect()
    query = "SELECT cf.UserName, cf.Flight_ID, f.Airline_Name, f.Date, f.Time, f.From_Airport, f.To_Airport, f.Capacity, f.Fare, f.Status FROM Cust_Flight AS cf INNER JOIN Flights AS f ON cf.Flight_ID = f.Flight_ID WHERE UserName=?"
    try:
        cur = con.cursor()
        cur.execute(query, (userName,))
        res = cur.fetchall()
    except Error as e:
        print(e)
    con.close()
    return res

def update_flight(flightID): #  Not Complete, please let me know if you need this guys
    con = db_connect()
    # We need to check if the flight exists
    query = "SELECT * FROM Flights WHERE Flight_ID=?"
    try:
        cur = con.cursor()
        cur.execute(query, (flightID,))
    except Error as e:
        print(e)
    con.close()

""" Not used 
def determineIDval(name):
    con = db_connect()
    query = "SELECT CustID FROM Customer WHERE UserName=?"
    try:
        cur = con.cursor()
        cur.execute(query, (name,))
        res = cur.fetchall()
        #res = res[0][0]
        return res[0][0]
    except Error as e:
        print(e)
    con.close()
"""

def get_Flights(order):
    con = db_connect()
    query = "SELECT * FROM Flights ORDER BY ? ASC"
    try:
        cur = con.cursor()
        cur.execute(query, (order,))
        res = cur.fetchall()
    except Error as e:
        print(e)
    con.close()
    return res

