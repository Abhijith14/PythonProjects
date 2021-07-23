import csv
import numpy as np
import matplotlib.pyplot as plt
from operator import add

Dataset = ""


# Read data from dataset and store it in a list
def readData():
    global Dataset
    Dataset = list(csv.reader(open("data/sgactivedentists_dataset.csv")))


# Get all the headings of the dataset
def getCategories():
    list_cat = []
    global Dataset
    for i in enumerate(Dataset):
        if i[0] == 0:
            list_cat = i[1]
            break
    return list_cat


# Menu 1 Code
def option1():
    global Dataset
    print("Display the number of dentists by category in 2012 : ")
    print("-----------------------------------------")
    for i in enumerate(Dataset):
        if i[0] != 5:
            continue
        for j in range(len(i[1][1:])):
            print(i[1][1:][j], " in ", getCategories()[j+1])
    print("-----------------------------------------")


# Menu 2 Code
def option2(sector):
    t = False
    if sector == "Year":
        t = True
        print("Year can't be used as a sector!")

    global Dataset
    sect_list = []
    for i in enumerate(Dataset):
        if i[0] == 0:
            if sector in i[1][1:]:
                temp_list = i[1][1:]
                for j in Dataset:
                    sect_list.append(j[temp_list.index(sector) + 1])
    if len(sect_list) > 0:
        sect_list = sect_list[3:]
        for i in range(len(sect_list)):
            sect_list[i] = int(sect_list[i])

        year_list = []
        for i in enumerate(Dataset):
            if i[0] < 3:
                continue
            year_list.append(i[1][0])

        print("-------------------------------")
        print("Average = ", np.mean(sect_list))
        print("Maximum = ", np.amax(sect_list), " in ", year_list[sect_list.index(np.amax(sect_list))])
        print("-------------------------------")

    else:
        if not t:
            print("Given Sector Not Found !!")
        else:
            pass


# Menu 3 Code
def option3(category):
    t = False
    if category == "Year":
        t = True
        print("Year can't be used as a category!")

    global Dataset
    cat_list = []
    for i in enumerate(Dataset):
        if i[0] == 0:
            if category in i[1][1:]:
                temp_list = i[1][1:]
                for j in Dataset:
                    cat_list.append(j[temp_list.index(category) + 1])
    if len(cat_list) > 0:
        cat_list = cat_list[1:]
        for i in range(len(cat_list)):
            cat_list[i] = int(cat_list[i])

        year_list = []
        for i in enumerate(Dataset):
            if i[0] == 0:
                continue
            year_list.append(i[1][0])

        start = cat_list[0]
        maxP = 0
        ind = 0
        for i in range(len(cat_list[1:])):
            diff = cat_list[1:][i] - start
            p = diff/start
            p = p * 100
            if maxP < p:
                maxP = p
                ind = i
            start = cat_list[1:][i]
        print(maxP)
        print(ind)
    else:
        if not t:
            print("Given Category Not Found !!")
        else:
            pass


# Display Line Chart
def disp_linechart(year, total):
    # Title and the x, y label
    plt.title("Total Dental Specialists vs Year")
    plt.xlabel("Year")
    plt.ylabel("Value")

    # Plot the line chart
    plt.plot(year, total, label="Total Dental Specialists")

    # Display the year as x axis label
    plt.xticks(year)

    plt.legend(loc="upper left")
    plt.show()


# Return data for a given dataset pattern
def retDatafromds(position):
    global Dataset
    temp_list = []
    for i in enumerate(Dataset):
        if i[0] == 0:
            continue
        temp_list.append(int(i[1][position]))

    return temp_list


# Display Bar Chart
def disp_barchart(year, priGDP, pubGDP):
    bar_width = 0.3

    # Title and the x, y label
    plt.title("Private and Public General Dental Practitioners vs Year")
    plt.xlabel("Year")
    plt.ylabel("Value")

    # plot the bar
    plt.bar(np.arange(len(priGDP)), priGDP, width=bar_width, label="Private General Dental Practitioners")
    plt.bar(np.arange(len(pubGDP)) + bar_width, pubGDP, width=bar_width,
            label="Public General Dental Practitioners")

    # Display the year as x axis label
    plt.xticks(np.arange(len(pubGDP)) + (bar_width / 2), year)

    plt.legend(loc="upper left")
    plt.show()


# Menu 4 Code
def option4():
    global Dataset
    # Get Chart Data
    year = retDatafromds(0)
    priDS = retDatafromds(1)
    pubDS = retDatafromds(3)
    total = list(map(add, priDS, pubDS))

    priGDP = retDatafromds(2)
    pubGDP = retDatafromds(4)
    # Line Chart
    disp_linechart(year, total)
    # Bar Chart
    disp_barchart(year, priGDP, pubGDP)
