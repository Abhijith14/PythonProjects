# import functions from data.py
from data.data import *


# Display Menu function
def displayMenu():
    print()
    # Display main menu
    print("""=============================
Singapore Museum Visitors  
================================================================================================================================================
    1.Display the visitor numbers of all museums in the year 2014.
    2.Mean of museum visitors from 2015 to 2019 and the (mean) value and the name of the museum that has the lowest mean.
    3.Of the user’s selected year, display the museums and their numbers of visitors, from the highest to the lowest number of visitors.
    4.Display Chart
    5.Exit/Quit
================================================================================================================================================
    """)


# Main Function
def Main():
    readData()
    while True:
        displayMenu()
        # Get Menu Input
        inputOp = input("Choose your menu : ")
        print()
        # Menu 1
        if inputOp == '1':
            option1()
        # Menu 2
        elif inputOp == '2':
            option2()
        # Menu 3
        elif inputOp == '3':
            year = input("Enter selected year : ")
            option3(year)
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
