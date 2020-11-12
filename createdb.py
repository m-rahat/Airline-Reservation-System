import DB_UTIL

drops = ['DROP TABLE IF EXISTS Customer;', 'DROP TABLE IF EXISTS Airports;', 'DROP TABLE IF EXISTS Airlines;', 'DROP TABLE IF EXISTS Flights;', 'DROP TABLE IF EXISTS Cust_Flight;']

creates = [
    #'CREATE TABLE Customer(CustID INTEGER PRIMARY KEY AUTOINCREMENT, UserName NVARCHAR(50) NOT NULL);',
    'CREATE TABLE Airports(AirportID INTEGER PRIMARY KEY AUTOINCREMENT, AirportName NVARCHAR(50) NOT NULL, CityName NVARCHAR(50) NOT NULL, Country NVARCHAR(50) NOT NULL);',
    'CREATE TABLE Airlines(AirlineID INTEGER PRIMARY KEY AUTOINCREMENT, AirlineName NVARCHAR(50) NOT NULL);',
    #'CREATE TABLE Flights(FlightID INTEGER PRIMARY KEY AUTOINCREMENT, AirlineID INT NOT NULL, Origin INT NOT NULL, Destination INT NOT NULL, CurrentPassengers INT DEFAULT 0, Capacity INT NOT NULL, FlightStatus NUMERIC DEFAULT 1, Fare INT NOT NULL, FlightDate NUMERIC NOT NULL, DepartureTime NUMERIC NOT NULL, FlightTime NUMERIC NOT NULL, FOREIGN KEY(Origin) REFERENCES Airports(AirportID), FOREIGN KEY(Destination) REFERENCES Airports(AirportID), FOREIGN KEY(AirlineID) REFERENCES Airlines(AirlineID));',
    'CREATE TABLE Flights(Flight_ID INTEGER PRIMARY KEY AUTOINCREMENT, Airline_Name NVARCHAR(50), Date NUMERIC, Time NUMERIC, From_Airport NVARCHAR(50), To_Airport NVARCHAR(50), Capacity INT, Fare INT, Status NVARCHAR(50));',
    #'CREATE TABLE Cust_Flight(CustID INT NOT NULL, FlightID INT NOT NULL, GuiSearch NUMERIC NOT NULL, FOREIGN KEY (CustID) REFERENCES Customer(CustID) ON DELETE CASCADE, FOREIGN KEY (FlightID) REFERENCES Flights(FlightID) ON DELETE CASCADE);'
    'CREATE TABLE Cust_Flight(UserName NVARCHAR(50) NOT NULL, Flight_ID INT NOT NULL, Method NVARCHAR(50), FOREIGN KEY (Flight_ID) REFERENCES Flights(Flight_ID) ON DELETE CASCADE, PRIMARY KEY(UserName, Flight_ID));'
]

#myconnectionobject = DB_UTIL.db_connect()

for i in range(0, len(drops)):
    DB_UTIL.cd_table(drops[i])

for i in range(0, len(creates)):
    DB_UTIL.cd_table(creates[i])

get_tables = "SELECT name FROM sqlite_master WHERE type='table'"
print(DB_UTIL.queryexec(get_tables))