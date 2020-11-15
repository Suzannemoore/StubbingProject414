"""**********************************************************************************************************
Suzanne Moore
CSC 414 G001
11/9/2020
USM

In this program we be asking a user to enter in a city and state then provide the information:

                            API for:
                            Coordinates
                            Weather

                            Functions for:
                            Capital
                            Unemployment Rate
                            Governor
                            Population

 - using if…elif…else Statements with a function for each individual state with a individual function
********************************************************************************************************"""

# import request
import requests


# importing Image class from PIL package

# Mississippi function
def missi():
    print("\n--State Mississippi Current Details--")
    print("Population: 2,976,149")
    print("Income Rank: 50th")
    print("Capital: Jackson")
    print("Current Governor: Tate Reeves\n")


# Florida function
def florida():
    print("\n--State Florida Current Details--")
    print("Population: 21,477,737")
    print("Income Rank: 40th")
    print("Capital: Tallahassee")
    print("Current Governor: Ron DeSantis\n")


# Texas function
def texas():
    print("\n--State Texas Current Details--")
    print("Population: 28,995,881")
    print("Income Rank: 24th")
    print("Capital: Austin")
    print("Current Governor: Greg Abbott\n")


# California function
def cali():
    print("\n--State California Current Details--")
    print("Population: 39,512,223")
    print("Income Rank: 9th")
    print("Capital: Sacramento")
    print("Current Governor: Gavin Newsom\n")


# Utah function
def utah():
    print("\n--State Utah Current Details--")
    print("Population: 3,205,958")
    print("Income Rank: 14th")
    print("Capital: Salt Lake City")
    print("Current Governor: Gary Herbert\n")


# Vermont function
def verm():
    print("\n--State Vermont Current Details--")
    print("Population: 623,989")
    print("Income Rank: 28th")
    print("Capital: Montpelier")
    print("Current Governor: Phil Scott\n")


# Alabama function
def alab():
    print("\n--State Alabama Current Details--")
    print("Population: 4,903,185")
    print("Income Rank: 46th")
    print("Capital: Montgomery")
    print("Current Governor: Kay Ivey\n")


# Louisiana function
def louisi():
    print("\n--State Louisiana Current Details--")
    print("Population: 4,648,794")
    print("Income Rank: 48th")
    print("Capital: Baton Rouge")
    print("Current Governor: John Bel Edwards\n")


# New Jersey function
def newJ():
    print("\n--State New Jersey Current Details--")
    print("Population: 4,648,794")
    print("Income Rank: 48th")
    print("Capital: Baton Rouge")
    print("Current Governor: John Bel Edwards\n")


# Iowa function
def iowa():
    print("\n--State Iowa Current Details--")
    print("Population: 3,155,070")
    print("Income Rank: 26th")
    print("Capital: Des Moines")
    print("Current Governor: Kim Reynolds\n")


# function for API and looping
def weather_info():
    # set looping to true
    looping = True
    # list of states
    list_of_states = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California",
                      "Colorado", "Connecticut", "District ", "of Columbia", "Delaware", "Florida",
                      "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas",
                      "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota",
                      "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska",
                      "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma",
                      "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota",
                      "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin",
                      "West Virginia", "Wyoming"]

    # while the program is looping we will use number 1 to exit program
    while looping:
        # tell user to press 1 to exit the program
        print('--Enter 1 to EXIT program--')

        # while looping ask user for city and capitalize first letter
        city = input('Please enter a city: ').capitalize()

        # if city is 1 break loop
        if city == "1":
            print("You have selected to Exit the program. Goodbye.")
            exit()
            break

        # while looping ask user for city and capitalize first letter
        state = input('Please enter a state: ').capitalize()

        # if city is 1 break loop
        if state == "1":
            print("You have selected to Exit the program. Goodbye.")
            exit()
            break

        # if user enters in invalid state ask user to try again
        if state not in list_of_states:
            print("Invalid Choice for state! Please try again or 1 to exit program.")
            continue

        # weather API and KEY
        weather_api = 'http://api.openweathermap.org/data/2.5/weather?q='
        weather_key = '&appid=fc623e7c1bc984adfa3864bb04c2fc46'

        # show full api
        the_api = weather_api + str(city) + ',' + str(state) + weather_key

        # request
        the_request = requests.get(the_api)
        main_data = the_request.json()

        # city name
        city_name = main_data['name']
        # city coordinates
        city_coordinates = main_data['coord']
        # city weather
        city_weather = main_data['weather']
        city_weather = city_weather[0]

        # output to user city name and state
        print('\n--' + str(city_name) + ', ' + str(state) + ' Coordinates--')
        # city coordinates longitude and latitude
        print('Longitude: ' + str(city_coordinates['lon']))
        print('Latitude: ' + str(city_coordinates['lat']))

        # print weather description
        print('\n--' + str(city_name) + ', ' + str(state) + ' Weather--')
        print(city_weather['main'])
        print(city_weather['description'])

        # if states for functions
        if state == 'Mississippi':
            missi()
        elif state == 'Florida':
            florida()
        elif state == 'Texas':
            texas()
        elif state == 'California':
            cali()
        elif state == 'Utah':
            utah()
        elif state == 'Vermont':
            verm()
        elif state == 'Alabama':
            alab()
        elif state == 'Louisiana':
            louisi()
        elif state == 'New Jersey':
            newJ()
        elif state == 'Iowa':
            iowa()
        else:
            # show user invalid choice ask again for input
            print("No more additional information for this state.")
