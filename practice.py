import DB_UTIL as db
#import numpy as np

con = db.db_connect()

#"""
#Here, I simply test the functionality of the DB. Give it a shot
db.create_flights('MANEMARS', '3030-30-30', '22:30:30', 'Area51', 'MarsRover', 1, 0, 'ON-TIME')
a = db.get_Flights('To_Airport')
print(a)

#db.queryexec("DELETE FROM Cust_Flight;")
#con.commit()

#print(db.book_a_flight('paul', 1, 'GUI'))
#print(db.book_a_flight('paul', 420, 'SEARCH'))
db.cancel_flight_admin(420)

#Now check reservations
print('\n\n')
print(db.get_full_user_reservation('paul'))

db.cancel_reservation_passenger('paul', 420)
print(db.get_full_user_reservation('paul'))

#"""
#Lets test my new work here
#for i in range(1, 10):
#print(db.get_user_reservation('paul'))
#flight_from_jfk = db.queryexec("SELECT * FROM Flights WHERE From_Airport = 'KJFK-New York' ORDER BY Airline_Name ASC")
#print(flight_from_jfk)
#"""
con.close()