import csv
import numpy as np
import matplotlib.pyplot as plt

Dataset = ""


# Read data from dataset and store it in a list
def readData():
    global Dataset
    Dataset = list(csv.reader(open("data/cpyincomesg_dataset.csv")))


# Menu 1 Code
def option1():
    global Dataset
    print("Display all information for the year 2011 : ")
    print("-----------------------------------------")
    for i in enumerate(Dataset):
        if i[0] != 5:
            continue

        print("Year                =   ", i[1][0])
        print("No of Companies     =   ", i[1][1])
        print("Total Income        =   ", i[1][2])
        print("Donations           =   ", i[1][3])
        print("Chargeable Income   =   ", i[1][4])
    print("-----------------------------------------")


# Menu 2 Code
def option2(category):
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
        cat_list = cat_list[7:]
        for i in range(len(cat_list)):
            cat_list[i] = int(cat_list[i])

        year_list = []
        for i in enumerate(Dataset):
            if i[0] < 7:
                continue
            year_list.append(i[1][0])

        print("-------------------------------")
        print("Average = ", np.mean(cat_list))
        print("Minimum = ", np.amin(cat_list), " in ", year_list[cat_list.index(np.amin(cat_list))])
        print("-------------------------------")
    else:
        if not t:
            print("Given Category Not Found !!")
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

        ind_sort = np.argsort(cat_list)
        ind_sort = ind_sort[::-1]

        for i in ind_sort[:3]:
            print(cat_list[i], " in ", year_list[i])

    else:
        if not t:
            print("Given Category Not Found !!")
        else:
            pass


# Return data for a given dataset pattern
def retDatafromds(position):
    global Dataset
    temp_list = []
    for i in enumerate(Dataset):
        if i[0] == 0:
            continue
        temp_list.append(int(i[1][position]))

    return temp_list


# Display Line Chart
def disp_linechart(year, CI, TI):
    # Title and the x, y label
    plt.title("Chargeable Income, Total Income vs Year")
    plt.xlabel("Year")
    plt.ylabel("Income")

    # Plot the line chart
    plt.plot(year, CI, label="Chargeable Income")
    plt.plot(year, TI, label="Total Income")

    # Display the year as x axis label
    plt.xticks(year)

    plt.legend(loc="upper left")
    plt.show()


# Display Bar Chart
def disp_barchart(year, NC, DO):
    bar_width = 0.3

    # Title and the x, y label
    plt.title("Number of Companies, Donations vs Year")
    plt.xlabel("Year")
    plt.ylabel("Value")

    # plot the bar
    plt.bar(np.arange(len(NC)), NC, width=bar_width, label="No of Companies")
    plt.bar(np.arange(len(DO)) + bar_width, DO, width=bar_width,
            label="Donations")

    # Display the year as x axis label
    plt.xticks(np.arange(len(DO)) + (bar_width / 2), year)

    plt.legend(loc="upper left")
    plt.show()



# Menu 4 Code
def option4():
    global Dataset
    # Get Chart Data

    # get all years
    year = retDatafromds(0)
    # get Chargeable Income
    CI = retDatafromds(4)
    # get Total Income
    TI = retDatafromds(2)
    # get Number of Companies
    NC = retDatafromds(1)
    # get Donations
    DO = retDatafromds(3)

    # Line Chart
    disp_linechart(year, CI, TI)
    # Bar Chart
    disp_barchart(year, NC, DO)

