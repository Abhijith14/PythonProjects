# import functions from data.py
from data.data import *


# Display Menu function
def displayMenu():
    print()
    # Display main menu
    print("""=============================
Border Crossing Vehicles 2
================================================================================================================================================
    1.Display the number of Bus Passengers crossing the border in 2006.
    2.Mean value for the travelers indifferent types of transport mode for each of the two 5-year spans of 2004 to 2008 and 2006 to 2010 and the minimum number of travelers in different types of transport mode in each of the periods and the years that the minimum occurs.
    3.Find the mean number of travelers for the whole 13-year period. Display the travelers in different types of transport mode and the corresponding years that are lower than the mean value.
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
