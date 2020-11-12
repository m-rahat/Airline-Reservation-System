"""
Lets pretend we want to make 6 airports, 7 customers, 8 flights, 5 airlines...or whatever number you wish for each
We need to create add these to the DB. I've created the necessary functions to do so in DB_UTIL.py 
All we need now, is to prepare that data so we can pass it into those functions
Simplest method might be to store all of these in a list or tuple, like so:
"""
customers = (
    ('BillyKid'),
    ('BigManeCashMane'),
    ('GandalfWizzboi'),
    ('studykid05'),
    ('JoeSchmo'),
    ('DuncanDonut'),
    ('BillGates')
) #I chose to use a tuple, since its immutable

airports = (
    ('KJFK', 'New York', 'USA'),
    ('KLAX', 'Los Angeles', 'California'),
    ('LFPG', 'Paris', 'France'),
    ('CYVR', 'Vancouver', 'Canada'),
    ('KMIA', 'Miami', 'USA'),
    ('MMUN', 'Cancun', 'Mexico')
) #MMUN, KJFK etc. are airport ICAO codes, I chose to write them properly but you can put whatever you wish.

airlines = (
    'American Airlines',
    'Alaskan Airways',
    'British Airways',
    'Lufthansa',
    'JetBlue'
)

flights = (
    ('Delta', '2019-12-02', '12:50:00', 'JFK', 'JKT', 150, 500, 'Avail'), 
    ('jetblue', '2019-12-03', '09:50:00', 'LHR', 'JKT', 150, 500, 'Avail'), 
    ('egyptair', '2019-12-25', '10:50:00', 'JFK', 'LHR', 150, 500, 'Avail'), 
    ('lufthansa', '2019-12-13', '10:50:00', 'JFK', 'JKT', 150, 500, 'Avail'), 
    ('finnair', '2019-12-19', '05:50:00', 'JFK', 'JKT', 150, 500, 'Avail'),
    ('aeromexico', '2019-12-18', '02:50:00', 'MAM', 'MEM', 150, 500, 'Avail'),
    ('quantas', '2019-12-20', '06:50:00', 'MARS', 'JUPITER', 150, 500, 'Avail'),
    ('british airways', '2019-12-12', '09:50:00', 'HOOVERDAM', 'AREA51', 150, 500, 'Booked')    
)

"""
Perhaps we can figure out a way to create a huge amount of these tuples and store in a file, then choose stuff randomly.
We can make this happen, pretty easily.
Now, we need to add these to the DB. LETS BEGIN
"""

import DB_UTIL
import randdata as rd
conobj = DB_UTIL.db_connect() #Connect to the DB

#So now that we're connected, lets start adding things.

#for i in range(0, len(customers)):
#    DB_UTIL.create_customer(conobj, customers[i])

for i in range(0, len(rd.airports)):
    DB_UTIL.create_airports(rd.airports[i][0], rd.airports[i][1], rd.airports[i][2])

for i in range(0, len(rd.airlines)):
    DB_UTIL.create_airlines(rd.airlines[i])

for i in range(0, len(rd.flights)):
    DB_UTIL.create_flights(rd.flights[i][0], rd.flights[i][1], rd.flights[i][2], rd.flights[i][3], rd.flights[i][4], rd.flights[i][5], rd.flights[i][6], rd.flights[i][7])

#Now, lets see if we've successfully added all these to the DB.

print(DB_UTIL.queryexec('SELECT * FROM Flights')) #This is hardcoded SQL, not the best way to do this, but it'll give us a glimpse at whether this works or not. Do avoid sing this though.

"""
If console returns something like:
$ python ex1.py
2.6.0
[(1, 'Paul', 'Pluszczewicz'), (2, 'Martin', 'Sendrowicz'), (3, 'Mohammed', 'Rahat'), (4, 'Sateesh', 'Mane'), (5, 'Joe', 'Schmo'), (6, 'Duncan', 'Donut'), (7, 'Bill', 'Gates')]

This means all is working well. Excellent!
"""
#conobj.commit()
conobj.close()