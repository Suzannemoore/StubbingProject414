"""**********************************************************************************************************
Suzanne Moore
CSC 414 G001
9/22/2020
USM

Using a self-selected programming language and menu display method create a stubbed code file and executable.

Requirements:

1.Your menu shall contain at least 10 menu items
2.Your menu shall contain an exit item selection
3.Your menu shall contain an error response for invalid entry
4.Your menu shall display a message indicating that an item is incomplete when selected
5.Your menu shall be continuously displayed until the exit item is selected.
6.The item selection method is up to the developer
7.Provide a test results document showing the correct execution via output display captures.

In this program we be asking a user to select a state and provide the information:
                            Capital
                            Unemployment Rate
                            Governor
                            Population

 - using if…elif…else Statements with a function for each individual state with a individual function

********************************************************************************************************"""

# user will select one of the states (number choice)
# to  see the information we provide

def states():
    print("1. Mississippi")
    print("2. Florida")
    print("3. Texas")
    print("4. California")
    print("5. Utah")
    print("6. Vermont")
    print("7. Alabama")
    print("8. Louisiana")
    print("9. New Jersey")
    print("10. Iowa\n")


# Mississippi function
def missi():
    print("Mississippi population is incomplete\n")


# Florida function
def florida():
    print("Florida population is incomplete\n")


# Texas function
def texas():
    print("Texas population is incomplete\n")


# California function
def cali():
    print("California unemployment Rate is incomplete\n")


# Utah function
def utah():
    print("Utah unemployment Rate is incomplete\n")


# Vermont function
def verm():
    print("Vermont population is incomplete\n")


# Alabama function
def alab():
    print("Alabama capital is incomplete\n")


# Louisiana function
def louisi():
    print("Louisiana capital is incomplete\n")


# New Jersey function
def newJ():
    print("New Jersey's current governor is incomplete\n")


# Iowa function
def iowa():
    print("Iowa's current governor is incomplete\n")


# The exit function. Ask user if they really want to exit if yes(y) then exit
# if no(n) then back to the menu
def toExit():
    print("You have selected to Exit the program. Goodbye")
    exit()


# set the while loop to true
looping = True
# while looping ask the user to enter in a state and give information
while looping:
    # ask the user to select a state to see the given information
    print("Please type in the number for the select state or 11 to EXIT")
    states()
    # get the user choice
    userSelection = int(input())
    # if…elif…else Statements with a function for each individual state with a individual function
    if userSelection == 1:
        missi()
    elif userSelection == 2:
        florida()
    elif userSelection == 3:
        texas()
    elif userSelection == 4:
        cali()
    elif userSelection == 5:
        utah()
    elif userSelection == 6:
        verm()
    elif userSelection == 7:
        alab()
    elif userSelection == 8:
        louisi()
    elif userSelection == 9:
        newJ()
    elif userSelection == 10:
        iowa()
    elif userSelection == 11:
        toExit()
    else:
        # show user invalid choice ask again for input
        print("Invalid Choice.")
