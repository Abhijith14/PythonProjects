import csv
import numpy as np
import matplotlib.pyplot as plt
from operator import add

Dataset = ""


# Read data from dataset and store it in a list
def readData():
    global Dataset
    Dataset = list(csv.reader(open("data/brdrxingusc_dataset.csv")))


# Menu 1 Code
def option1():
    global Dataset
    print("Display the number of vehicles crossing border 2004 : ")
    print("-----------------------------------------")
    for i in enumerate(Dataset):
        if i[0] <= 1:
            continue

        print(i[1][5], i[1][0])

    print("-----------------------------------------")


# Menu 2 Code
def option2(type):
    global Dataset
    type_list = []
    for i in enumerate(Dataset):
        if i[0] == 0:
            continue
        if type == i[1][0]:
            type_list = i[1]
    if len(type_list) > 0:
        type_list = type_list[1:]
        year = Dataset[0][1:]
        for i in range(len(type_list)):
            type_list[i] = int(type_list[i])
        m1_list = type_list[2:6]
        m2_list = type_list[8:12]

        m1_max = np.amax(m1_list)
        m2_max = np.amax(m2_list)

        y1 = year[2:6]
        y2 = year[8:12]

        print("------------------------------------------------------")
        print("Mean for 2002 to 2005 = ", np.mean(m1_list))
        print("Mean for 2008 to 2011 = ", np.mean(m2_list))
        print("Maximum in 2002 to 2005 = ", m1_max, " in ", y1[m1_list.index(m1_max)])
        print("Maximum in 2008 to 2011 = ", m2_max, " in ", y2[m2_list.index(m2_max)])
        print("------------------------------------------------------")

    else:
        print("Given Type Not Found !!")


# Menu 3 Code
def option3(type):
    global Dataset
    type_list = []
    for i in enumerate(Dataset):
        if i[0] == 0:
            continue
        if type == i[1][0]:
            type_list = i[1]
    if len(type_list) > 0:
        type_list = type_list[1:]
        year = Dataset[0][1:]
        for i in range(len(type_list)):
            type_list[i] = int(type_list[i])

        ind_sort = np.argsort(type_list)
        for i in ind_sort[:3]:
            print(type_list[i], " in ", year[i])
    else:
        print("Given Type Not Found !!")


# Display Line Chart
def disp_linechart(year, BP, Bus):
    # Title and the x, y label
    plt.title("Bus Passengers, Bus vs Year")
    plt.xlabel("Year")
    plt.ylabel("Income")

    # Plot the line chart
    plt.plot(year, BP, label="Bus Passengers")
    plt.plot(year, Bus, label="Bus")

    # Display the year as x axis label
    plt.xticks(year)

    plt.legend(loc="upper left")
    plt.show()


# Display Bar Chart
def disp_barchart(year, PV, LT):
    bar_width = 0.3

    # Title and the x, y label
    plt.title("Personal Vehicles, Loaded Trucks vs Year")
    plt.xlabel("Year")
    plt.ylabel("Value")

    # plot the bar
    plt.bar(np.arange(len(PV)), PV, width=bar_width, label="Personal Vehicles")
    plt.bar(np.arange(len(LT)) + bar_width, LT, width=bar_width,
            label="Loaded Trucks")

    # Display the year as x axis label
    plt.xticks(np.arange(len(LT)) + (bar_width / 2), year)

    plt.legend(loc="upper left")
    plt.show()


# Return data for a given dataset pattern
def retDatafromds(position):
    global Dataset
    temp_list = []
    for i in enumerate(Dataset):
        if i[0] == position:
            temp_list = i[1][1:]

    for i in range(len(temp_list)):
        temp_list[i] = int(temp_list[i])

    return temp_list


# Menu 4 Code
def option4():
    global Dataset
    # Get Chart Data

    # get all years
    year = retDatafromds(0)
    # get Personal Vehicles
    PV = retDatafromds(3)
    # get Loaded Trucks
    LT = retDatafromds(4)
    # get Bus Passengers
    BP = retDatafromds(1)
    # get Bus
    Bus = retDatafromds(2)

    # Line Chart
    disp_linechart(year, BP, Bus)
    # Bar Chart
    disp_barchart(year, PV, LT)

