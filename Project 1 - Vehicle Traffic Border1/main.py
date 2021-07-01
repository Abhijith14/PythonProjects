# import functions from data.py
from data.data import *


# Display Menu function
def displayMenu():
    print()
    # Display main menu
    print("""=============================
Vehicle Traffic at Border 1    
================================================================================================================================================
    1.Display the number of vehicle crossings by city in 2012.
    2.Mean of vehicle-crossings from 2010 to 2015 and years and the number of vehicle crossings in that period which fall below the mean found.
    3.Vehicle crossings increased by at least 6% over the previous year.
    4.Display Chart
    5.Exit/Quit
================================================================================================================================================
    """)


# Main Function
def Main():
    readData()
    inputOp = True
    while inputOp:
        displayMenu()

        # Get Menu Input
        inputOp = input("Choose your menu : ")
        print()
        # Menu 1
        if inputOp == '1':
            option1()
        # Menu 2
        elif inputOp == '2':
            city = input("Enter city name : ")
            option2(city)
        # Menu 3
        elif inputOp == '3':
            city = input("Enter city name : ")
            option3(city)
        # Menu 4
        elif inputOp == '4':
            option4()
        # Menu 5
        elif inputOp == '5':
            quest = input("Are you sure ? (Y/N) : ")
            if quest == "Y":
                exit()
        # If nothing matches continue the loop
        else:
            continue


if __name__ == '__main__':
    Main()
