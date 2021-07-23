# import functions from data.py
from data.data import *


# Display Menu function
def displayMenu():
    print()
    # Display main menu
    print("""=============================
Singapore Dentists 2
================================================================================================================================================
    1.Display the number of dentists by category in 2012.
    2.Average value in the 10-year span of 2010 to 2019 and display the maximum number of dentists in that period and the year in which it occurred.
    3.Display the highest percentage change and the year in which it occurred.
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
            category = input("Enter Sector : ")
            option2(category)
        # Menu 3
        elif inputOp == '3':
            category = input("Enter Category : ")
            option3(category)
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
