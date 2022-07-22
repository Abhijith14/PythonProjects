import csv
import numpy as np
import matplotlib.pyplot as plt

Dataset = ""


# Read data from dataset and store it in a list
def readData():
    global Dataset
    Dataset = list(csv.reader(open("data/museumvisitors_dataset.csv")))


# Menu 1 Code
def option1():
    global Dataset
    print("The visitors in the year 2014 : ")
    print("----------------------------------------------------")
    for ind, data in enumerate(Dataset):
        if ind == 0:  # ignore heading
            continue
        sp = 35 - len(data[0])
        sp = sp * " "
        sp = sp + "|"
        print("|", data[0], sp, data[2], "|")
    print("----------------------------------------------------")


# Menu 2 Code
def option2():
    global Dataset
    MeanVals = []
    MuseumVals = []
    print("The mean of visitors from 2015 to 2019 : ")
    print("----------------------------------------------------")
    for ind, data in enumerate(Dataset):
        if ind == 0:  # ignore heading
            continue
        sumVal = int(data[3]) + int(data[4]) + int(data[5]) + int(data[6]) + int(data[7])
        avgVal = sumVal/5
        MeanVals.append(avgVal)
        MuseumVals.append(data[0])
        sp = 35 - len(data[0])
        sp = sp * " "
        sp = sp + "|"
        print("|", data[0], sp, avgVal, "|")
    print("----------------------------------------------------")
    print("{} has the lowest mean with {} average visitors.".format(MuseumVals[MeanVals.index(min(MeanVals))], min(MeanVals)))
    print()


# Menu 3 Code
def option3(year):
    global Dataset
    value = ""
    dict_val = {}
    print("----------------------------------------------------")
    for ind, data in enumerate(Dataset):
        if ind == 0:  # ignore heading
            if year in data:
                value = data.index(year)
                continue
            else:
                print("Year given not found !!")
                break

        dict_val[data[0]] = int(data[value])

    dict_val = sorted(dict_val.items(), key=lambda kv: kv[1], reverse=True)

    for i in dict_val:
        sp = 35 - len(i[0])
        sp = sp * " "
        sp = sp + "|"
        if value:
            print("|", i[0], sp, i[1], "|")

    print("----------------------------------------------------")


# Display Line Chart
def disp_linechart(year, ACM, TPM):
    # Title and the x, y label
    plt.title("Visitor numbers of ACM, TPM vs Year")
    plt.xlabel("Year")
    plt.ylabel("Visitors")

    # Plot the line chart
    plt.plot(year, ACM, label="Asian Civilisations Museum")
    plt.plot(year, TPM, label="The Peranakan Museum")

    # Display the year as x axis label
    plt.xticks(year)

    plt.legend(loc="upper left")
    plt.show()


# Display Bar Chart
def disp_barchart(NMS):
    bar_width = 0.3
    NMS = np.array(NMS)
    seq = []
    NMS_sorted = np.sort(NMS)
    for i in NMS:
        result = np.where(NMS_sorted == i)
        for k in result:
            seq.append(int(k) + 1)

    # Title and the x, y label
    plt.title("The lowest to highest number of visitors to NMS vs their sequence number")
    plt.xlabel("Visitors to NMS")
    plt.ylabel("Sequence")

    # plot the bar
    plt.bar(np.arange(len(NMS)), seq, width=bar_width, label="NMS")

    # Display the year as x axis label
    plt.xticks(np.arange(len(NMS)) + (bar_width / 2), NMS)
    plt.legend(loc="upper left")
    plt.show()


# Menu 4 Code
def option4():
    global Dataset
    # Get Chart Data
    ACM, TPM, years = [], [], []
    NMS = []

    for ind, data in enumerate(Dataset):
        if ind == 0:  # ignore heading
            years = data[1:]
            continue

        if data[0] == "Asian Civilisations Museum":
            ACM = data[1:]
        elif data[0] == "The Peranakan Museum":
            TPM = data[1:]

        elif data[0] == "National Museum of Singapore":
            NMS = data[1:]

    # converting to integers
    ACM = [int(i) for i in ACM]
    TPM = [int(i) for i in TPM]
    years = [int(i) for i in years]
    NMS = [int(i) for i in NMS]

    # Line Chart
    disp_linechart(years, ACM, TPM)

    # Bar Chart
    disp_barchart(NMS)
