import csv
import numpy as np
import matplotlib.pyplot as plt

Dataset = ""


# Read data from dataset and store it in a list
def readData():
    global Dataset
    Dataset = list(csv.reader(open("data/brdrxingusc_dataset (5).csv")))


# Menu 1 Code
def option1():
    global Dataset
    print("Number of Bus Passengers crossing the border in 2006 : ")
    print("-----------------------------------------")
    for i in enumerate(Dataset):
        if i[0] == 1:
            print(i[1][7], i[1][0])

    print("-----------------------------------------")


# Menu 2 Code
def option2(types):
    global Dataset
    type_list = []
    for i in enumerate(Dataset):
        if i[1][0] == types:
            type_list = i[1][1:]
            break
    type_list = [int(i) for i in type_list]
    if len(type_list) > 0:
        year = Dataset[0][1:]
        y1 = year[4:9]
        y2 = year[6:11]

        print("------------------------------------------------------")
        print("Mean for 2004 to 2008 for " + types + " = ", np.mean(type_list[4:9]))
        print("Mean for 2006 to 2010 for " + types + " = ", np.mean(type_list[6:11]))
        print()
        print("The minimum number of travelers in different types of transport mode in each of the periods and the years that the minimum occurs : ")
        for mode in enumerate(Dataset):
            if mode[0] == 0:
                continue
            main_list = mode[1][1:]
            main_list = [int(i) for i in main_list]
            m1_min = np.amin(main_list[4:9])
            m2_min = np.amin(main_list[6:11])
            print("Minimum in 2004 to 2008 for " + mode[1][0] + " = ", m1_min, " in ", y1[main_list[4:9].index(m1_min)])
            print("Minimum in 2006 to 2010 for " + mode[1][0] + " = ", m2_min, " in ", y2[main_list[6:11].index(m2_min)])
        print("------------------------------------------------------")

    else:
        print("Given Type Not Found !!")


# Menu 3 Code
def option3(types):
    global Dataset
    type_list = []
    for i in enumerate(Dataset):
        if i[1][0] == types:
            type_list = i[1][1:]
            break
    type_list = [int(i) for i in type_list]
    print("------------------------------------------------------")
    if len(type_list) > 0:
        year = Dataset[0][1:]
        avg_val = np.mean(type_list)
        print("Mean number of travelers from 2000 to 2012 for {} is: {}".format(types, avg_val))
        print()
        for mode in enumerate(Dataset):
            if mode[0] == 0:
                continue
            print("Travellers in {} that are less than the mean value {}".format(mode[1][0], avg_val))
            c = 0
            for travel in enumerate(mode[1][1:]):
                if float(travel[1]) < avg_val:
                    print("{} in {}".format(travel[1], year[travel[0]]))
                    c = c + 1

            if c == 0:
                print("None")

    else:
        print("Given Type Not Found !!")

    print("------------------------------------------------------")

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

