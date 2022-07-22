import csv
import numpy as np
import matplotlib.pyplot as plt

Dataset = ""


# Read data from dataset and store it in a list
def readData():
    global Dataset
    Dataset = list(csv.reader(open("data/sgallelectricity_dataset.csv")))


# Menu 1 Code
def option1():
    global Dataset
    types = []
    print("The monthly consumption in May : ")
    print("----------------------------------------")
    for ind, data in enumerate(Dataset):
        if data[0] == "Month":
            types = data[1:]
        if data[0] == "May":
            val = data[1:]
            for i in range(len(types)):
                sp = 25 - len(types[i])
                sp = sp * " "
                sp = sp + "|"
                print("|", types[i], sp, val[i], "|")
    print("----------------------------------------")


# Menu 2 Code
def option2(dwtype):
    global Dataset
    value = ""
    avg1, avg2 = np.zeros((3, 512*512), dtype=np.float32), np.zeros((3, 512*512), dtype=np.float32)
    month1 = ["Apr", "May", "Jun"]
    month2 = ["Oct", "Nov", "Dec"]
    print("----------------------------------------------------")
    for ind, data in enumerate(Dataset):
        if data[0] == "Month":
            if dwtype in data[1:]:
                value = data.index(dwtype)
            else:
                print("Dwelling Type given not found !!")
                break

        if data[0] == "Apr":
            avg1[0:] = float(data[value])
        elif data[0] == "May":
            avg1[1:] = float(data[value])
        elif data[0] == "Jun":
            avg1[2:] = float(data[value])

        elif data[0] == "Oct":
            avg2[0:] = float(data[value])
        elif data[0] == "Nov":
            avg2[1:] = float(data[value])
        elif data[0] == "Dec":
            avg2[2:] = float(data[value])

    if value:
        print("Apr to Jun ", np.mean(avg1))
        indices = np.where(avg1 == avg1.max())
        print("Maximum", np.max(avg1), "in", month1[indices[0][0]])

        print("Oct to Dec ", np.mean(avg2))
        indices = np.where(avg2 == avg2.max())
        print("Maximum", np.max(avg2), "in", month2[indices[0][0]])
    print("----------------------------------------------------")


# Menu 3 Code
def option3(dwtype):
    global Dataset
    value = ""
    sums = 0
    print("----------------------------------------------------")
    for ind, data in enumerate(Dataset):
        if data[0] == "Month":
            if dwtype in data[1:]:
                value = data.index(dwtype)
            else:
                print("Dwelling Type given not found !!")
                break

        else:
            sums = sums + float(data[value])

    if value:
        annual = sums/12
        lim = (annual*6)/100
        print("Annual average for the type", dwtype, "is", annual)
        print("Months in which the monthly electricity consumption is at least 6% (" + str(lim) + ") higher than the annual mean electricity consumption: ")
        print()
        for ind, data in enumerate(Dataset):
            if data[0] != "Month":
                if float(data[value]) >= lim:
                    print("|", data[0], "|", data[value], "|")
    print("----------------------------------------------------")


# Display Line Chart
def disp_linechart(months, PAC, LP):
    # Title and the x, y label
    plt.title("Private Apts/Condo, Landed Properties vs Months")
    plt.xlabel("Months")
    plt.ylabel("Electricity Consumption (GWh)")

    # Plot the line chart
    plt.plot(months, PAC, label="Private Apts/Condo")
    plt.plot(months, LP, label="Landed Properties")

    # Display the year as x axis label
    plt.xticks(months)

    plt.legend(loc="upper left")
    plt.show()


# Display Bar Chart
def disp_barchart(PH, TE, months):
    X_axis = np.arange(len(months))

    plt.bar(X_axis - 0.2, PH, 0.4, label='Public Housing')
    plt.bar(X_axis + 0.2, TE, 0.4, label='Total Electricity Consumption')

    plt.xticks(X_axis, months)
    plt.xlabel("Months")
    plt.ylabel("Electricity Consumption (GWh)")
    plt.title("Total Electricity Consumption, Public Housing vs Month")
    plt.legend()
    plt.show()


# Menu 4 Code
def option4():
    global Dataset
    # Get Chart Data
    PAC, LP, months = [], [], []
    PH, TE, TES = [], [], 0

    for ind, data in enumerate(Dataset):
        if data[0] != "Month":
            months.append(data[0])
            PAC.append(float(data[2]))
            LP.append(float(data[3]))

            PH.append(float(data[1]))
            for j in data[1:]:
                TES = TES + float(j)

            TE.append(TES)

    # Line Chart
    disp_linechart(months, PAC, LP)

    # Bar Chart
    disp_barchart(PH, TE, months)
