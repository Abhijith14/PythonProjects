# import functions from data.py
from data.data import *


# Display Menu function
def displayMenu():
    print()
    # Display main menu
    print("""=============================
Income Singapore Companies 2 
================================================================================================================================================
    1.Display all information for the year 2011.
    2.Average value in the 6-year span of 2013 to 2018 and display the minimum value in that period and the year in which it occurred.
    3.display the three highest values and the years in which given category occurred.
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
            category = input("Enter Category : ")
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
