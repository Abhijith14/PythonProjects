# import functions from data.py
from data.data import *


# Display Menu function
def displayMenu():
    print()
    # Display main menu
    print("""=============================
Singapore Electricity Consumption  
================================================================================================================================================
    1.Display the monthly electricity consumptions of all dwelling types in May.
    2.The average electricity consumption in each of the 4-month periods from Apr to Jun & from Oct to Dec and the maximum electricity consumption in each of the periods and the months in which it occurred.
    3.Display the electricity consumption and the months in which the monthly electricity consumption is at least 6% higher than the annual mean electricity consumption.
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
            Dwtype = input("Enter dwelling type : ")
            option2(Dwtype)
        # Menu 3
        elif inputOp == '3':
            Dwtype = input("Enter dwelling type : ")
            option3(Dwtype)
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
