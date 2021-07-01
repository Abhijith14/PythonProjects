import csv
import numpy as np
import matplotlib.pyplot as plt

Dataset = ""


# Read data from dataset and store it in a list
def readData():
    global Dataset
    Dataset = list(csv.reader(open("data/vehtrafficusc_dataset (1).csv")))


# Menu 1 Code
def option1():
    global Dataset
    print("The Number of Vehicle Vrossings by City in 2012 : ")
    print("--------------------------")
    for i in enumerate(Dataset):
        if i[0] == 0:
            continue
        sp = 14 - len(i[1][0])
        sp = sp * " "
        sp = sp + "|"
        print("|", i[1][0], sp, i[1][3], "|")
    print("--------------------------")


# Menu 2 Code
def option2(city):
    global Dataset
    city_list = []
    for i in Dataset:
        if city in i[0]:
            city_list = i
    if len(city_list) > 0:
        city_list = city_list[1:7]
        for i in range(len(city_list)):
            city_list[i] = int(city_list[i])

        print()
        print("Mean = ", np.mean(city_list))
        print()
        print("----------------")
        for i in city_list:
            if i < np.mean(city_list):
                print("|", Dataset[0][city_list.index(i) + 1], "|", i, "|")
        print("----------------")
    else:
        print("Given City Not Found !!")


# Menu 3 Code
def option3(city):
    global Dataset
    city_list = []
    for i in Dataset:
        if city in i[0]:
            city_list = i
    if len(city_list) > 0:
        for i in range(1, len(city_list)):
            if i == 1:
                continue
            ele1 = int(city_list[i])
            ele2 = int(city_list[i-1])
            ele_limit = (ele2 * 6)/100
            ele2 = ele_limit + ele2
            if ele1 >= ele2:
                print(ele1, "in", Dataset[0][i + 1])
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
def disp_linechart(year, Dan, Fron):
    # Title and the x, y label
    plt.title("Vehicle crossings from Danville, Frontier")
    plt.xlabel("Year")
    plt.ylabel("Vehicle Crossings")

    # Plot the line chart
    plt.plot(year, Dan, label="Danville")
    plt.plot(year, Fron, label="Frontier")

    # Display the year as x axis label
    plt.xticks(year)

    plt.legend(loc="upper left")
    plt.show()


# Display Bar Chart
def disp_barchart(year, Lau, Port):
    bar_width = 0.3

    # Title and the x, y label
    plt.title("Vehicle crossings from Laurier, Port Angeles")
    plt.xlabel("Year")
    plt.ylabel("Vehicle Crossings")

    # plot the bar
    plt.bar(np.arange(len(Lau)), Lau, width=bar_width, label="Laurier")
    plt.bar(np.arange(len(Port)) + bar_width, Port, width=bar_width,
            label="Port Angeles")

    # Display the year as x axis label
    plt.xticks(np.arange(len(Port)) + (bar_width / 2), year)

    plt.legend(loc="upper left")
    plt.show()


# Menu 4 Code
def option4():
    global Dataset
    # Get Chart Data
    year, Dan, Fron, Lau, Port = [], [], [], [], []
    # get all years
    year = retDatafromds(Dataset[0])
    # get Danville all vehicle crossings
    Dan = retDatafromds(Dataset[3])
    # get Frontier all vehicle crossings
    Fron = retDatafromds(Dataset[4])
    # get Laurier all vehicle crossings
    Lau = retDatafromds(Dataset[5])
    # get Port Angeles all vehicle crossings
    Port = retDatafromds(Dataset[6])

    # Line Chart
    disp_linechart(year, Dan, Fron)

    # Bar Chart
    disp_barchart(year, Lau, Port)
