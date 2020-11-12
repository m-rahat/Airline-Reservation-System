from random import seed
from random import randint

seed(1)

airports = (
    'KJFK-New York',
    'KLGA-New York',
    'KLAX-Los Angeles',
    'LFPG-Paris',
    'CYVR-Vancouver',
    'KMIA-Miami',
    'MMUN-Cancun',
    'CYYZ-Toronto',
    'EHAM-Amsterdam',
    'KDFW-Dallas',
    'EDDH-Hamburg',
    'RJAA-Tokyo',
    'EGLL-London',
    'EDDB-Berlin',
    'LPPT-Lisbon',
    'LIRF-Rome',
    'KDEN-Denver',
    'KABQ-Albuquerque',
    'KATL-Atlanta',
    'ZBAA-Beijing',
    'EIDW-Dublin',
    'OMDB-Dubai'
)

airlines = (
    'American Airlines',
    'Alaska Airlines',
    'British Airways',
    'Lufthansa',
    'JetBlue',
    'Quantas',
    'Finnair',
    'United Airlines',
    'Southwest Airlines',
    'Aer Lingus',
    'Emirates',
    'JAL Japan Airlines',
    'Delta'
)

fares = ( #19
    150,
    200,
    250,
    300,
    250,
    400,
    450,
    500,
    500,
    550,
    600,
    650,
    700,
    750,
    800,
    850,
    900,
    950,
    1000
    )

capacity = ( #8
    75,
    150,
    225,
    150,
    275,
    325,
    350,
    400
    )

times = (
    '00:00:00',
    '01:00:00',
    '02:00:00',
    '03:00:00',
    '04:00:00',
    '05:00:00',
    '06:00:00',
    '07:00:00',
    '08:00:00',
    '09:00:00',
    '10:00:00',
    '11:00:00',
    '12:00:00',
    '13:00:00',
    '14:00:00',
    '15:00:00',
    '16:00:00',
    '17:00:00',
    '18:00:00',
    '19:00:00',
    '20:00:00',
    '21:00:00',
    '22:00:00',
    '23:00:00',
    '00:30:00',
    '01:30:00',
    '02:30:00',
    '03:30:00',
    '04:30:00',
    '05:30:00',
    '06:30:00',
    '07:30:00',
    '08:30:00',
    '09:30:00',
    '10:30:00',
    '11:30:00',
    '12:30:00',
    '13:30:00',
    '14:30:00',
    '15:30:00',
    '16:30:00',
    '17:30:00',
    '18:30:00',
    '19:30:00',
    '20:30:00',
    '21:30:00',
    '22:30:00',
    '23:30:00'
    )

reserve = ('Unavailable', 'Available')

flights = []
for i in range(0, 21):
    for y in range(0, 10):
        value = randint(0, 21)
        anotherval = randint(0, 12)
        fare = randint(0, 18)
        cap = randint(0, 7)
        tim = randint(0, 47)
        availbil = randint(0, 9)
        info = 1
        if availbil == 0:
            info = 0
        print("('"+ airlines[anotherval] + "', '0000-00-00', '" + times[tim] + "', '" + airports[i] + "', '" + airports[value] + "', " + str(fares[fare]) + ", " + str(capacity[cap]) + ", '" + reserve[info] + "'),")


