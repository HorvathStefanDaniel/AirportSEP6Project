import csv

def parseAirlines():
    with open('airlines.csv', newline='') as csvAirlines:
        reader = csv.reader(csvAirlines, delimiter=',', quotechar='|')
        for row in reader:
            print(', '.join(row))

def parseAirports():
    with open('airports.csv', newline='') as csvAirports:
        reader = csv.reader(csvAirports, delimiter=',', quotechar='|')
        for row in reader:
            print(', '.join(row))

def parseFlights():
    with open('flights.csv', newline='') as csvFlights:
        reader = csv.reader(csvFlights, delimiter=',', quotechar='|')
        for row in reader:
            print(', '.join(row))

def parsePlanes():
    with open('planes.csv', newline='') as csvPlanes:
        reader = csv.reader(csvPlanes, delimiter=',', quotechar='|')
        for row in reader:
            print(', '.join(row))

def parseWeather():
    with open('weather.csv', newline='') as csvWeather:
        reader = csv.reader(csvWeather, delimiter=',', quotechar='|')
        for row in reader:
            print(', '.join(row))

parseAirlines()
print('\n')
parseAirports()