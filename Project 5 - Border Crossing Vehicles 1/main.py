# import functions from data.py
from data.data import *


# Display Menu function
def displayMenu():
    print()
    # Display main menu
    print("""=============================
Border Crossing Vehicles 1
================================================================================================================================================
    1.Display the number of vehicles (i.e., excluding bus passengers) crossing the border in 2004.
    2.Mean value for each of the two 4-year spans of 2002 to 2005 and 2008 to 2011 and maximum number in each of the periods and the years that the maximum occurs.
    3.Display the three lowest border crossing numbers and the corresponding years that they occur.
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
            type_main = input("Enter Type : ")
            option2(type_main)
        # Menu 3
        elif inputOp == '3':
            type_main = input("Enter Type : ")
            option3(type_main)
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
