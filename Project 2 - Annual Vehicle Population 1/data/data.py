import csv
import numpy as np
import matplotlib.pyplot as plt

Dataset = ""


# Read data from dataset and store it in a list
def readData():
    global Dataset
    Dataset = list(csv.reader(open("data/annualmvpop_dataset (1).csv")))


# Menu 1 Code
def option1():
    global Dataset
    print("Vehicle Population by fuel type for the year 2010 : ")
    print("-----------------------------------------")
    for i in enumerate(Dataset):
        if i[0] == 0:
            continue
        sp = 8 - len(i[1][5])
        sp = sp * " "
        sp = sp + "|"
        sp2 = 26 - len(i[1][0])
        sp2 = sp2 * " "
        sp2 = sp2 + "|"
        print("|", i[1][5], sp, i[1][0], sp2)
    print("-----------------------------------------")


# Menu 2 Code
def option2(fuel):
    global Dataset
    fuel_list = []
    for i in Dataset:
        if fuel == i[0]:
            fuel_list = i
    if len(fuel_list) > 0:
        fuel_list = fuel_list[1:7]
        for i in range(len(fuel_list)):
            fuel_list[i] = int(fuel_list[i])
        print()
        print("Mean = ", np.mean(fuel_list))
        print()
        print("-----------------")
        for i in fuel_list:
            if i > np.mean(fuel_list):
                print("|", Dataset[0][fuel_list.index(i) + 1], "|", i, "|")
        print("-----------------")
    else:
        print("Given City Not Found !!")


# Menu 3 Code
def option3(fuel):
    global Dataset
    fuel_list = []
    for i in Dataset:
        if fuel == i[0]:
            fuel_list = i
    if len(fuel_list) > 0:
        temp = False
        for i in range(1, len(fuel_list)):
            if i == 1:
                continue
            ele1 = int(fuel_list[i])
            ele2 = int(fuel_list[i-1])
            ele_limit = (ele2 * 15)/100
            ele2 = ele_limit + ele2
            if ele1 >= ele2:
                sp = 8 - len(str(ele1))
                sp = sp * " "
                temp = True
                print(ele1, sp, "in", "    ", Dataset[0][i])
            else:
                if not temp:
                    temp = False
        if not temp:
            print("No Years Found with 15% increase than the previous year.")
    else:
        print("Given City Not Found !!")


# Return data for a given dataset pattern
def retDatafromds(dataset):
    temp_list = []
    for col_index, data in enumerate(dataset):
        if col_index == 0:
            continue
        temp_list.append(int(data))

    return temp_list


# Display Line Chart
def disp_linechart(year, PE, PC):
    # Title and the x, y label
    plt.title("Petrol-Electric and Petrol-CNG vehicle population")
    plt.xlabel("Year")
    plt.ylabel("Vehicle Population")

    # Plot the line chart
    plt.plot(year, PE, label="Petrol-Electric")
    plt.plot(year, PC, label="Petrol-CNG")

    # Display the year as x axis label
    plt.xticks(year)

    plt.legend(loc="upper left")
    plt.show()


# Display Bar Chart
def disp_barchart(year, PC, PE):
    bar_width = 0.3

    # Title and the x, y label
    plt.title("Petrol-Electric and Petrol-CNG vehicle population")
    plt.xlabel("Year")
    plt.ylabel("Vehicle Population")

    # plot the bar
    plt.bar(np.arange(len(PC)), PC, width=bar_width, label="Petrol-CNG")
    plt.bar(np.arange(len(PE)) + bar_width, PE, width=bar_width,
            label="Petrol-Electric")

    # Display the year as x axis label
    plt.xticks(np.arange(len(PE)) + (bar_width / 2), year)

    plt.legend(loc="upper left")
    plt.show()


# Menu 4 Code
def option4():
    global Dataset
    # Get Chart Data
    year, PE, PC = [], [], []
    # get all years
    year = retDatafromds(Dataset[0])
    # get Petrol-Electric
    PE = retDatafromds(Dataset[6])
    # get Petrol-CNG
    PC = retDatafromds(Dataset[5])

    # Line Chart
    disp_linechart(year, PE, PC)
    # Bar Chart
    disp_barchart(year, PC, PE)
