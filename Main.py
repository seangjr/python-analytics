from csv import reader
import csv
import operator
from os import read
import math
import matplotlib.pyplot as plot
from numpy import double
import pandas as pd


def Start():

    def CSV():

        # with open(r'/home/seanr/Downloads/programming-20210731T025856Z-001/programming/sgallelectricity_dataset (4).csv', 'r') as read_obj:

        #     # we use global so its accessible by the other functions
        #     global list_sorted
        #     global list_main

        #     # setting up sorted list and main list to be retrievable
        #     reader_csv = reader(read_obj, delimiter=',')
        #     list_sorted = sorted(
        #         reader_csv)
        #     list_main = list(list_sorted)
        with open('/home/seanr/Downloads/programming-20210731T025856Z-001/programming/sgallelectricity_dataset (4).csv', 'r') as read_obj:

            global list_main
            csv_reader = reader(read_obj)
            list_main = list(csv_reader)

        global reader_csv
        reader_csv = pd.read_csv(
            "/home/seanr/Downloads/programming-20210731T025856Z-001/programming/sgallelectricity_dataset (4).csv")
        reader_csv.head()

    CSV()

    # try is used to prevent user from entering anything other than integers or numbers that is beyond 1 to 5
    try:
        menuOptions = int(input(
            "1: Show full data of monthly electricity consumptions\n2: Display the monthly electricity consumptions of all dwelling types in march\n3: Select dwelling type to display program functions\n4: Graphs\n5: Quit\n\n"
        ))
        if menuOptions < 1 or menuOptions > 5:
            print("Invalid input")
            Start()
    except:
        print("Enter valid integer")
        Start()

    # initialise the appropriate list with full data
    if menuOptions == 1:

        # for line in list_sorted:
        #     print(line)
        print(reader_csv)
        Start()

    # select dwelling type e.g. landed prop.
    if menuOptions == 2:
        # there is a +1 because range() includes the first number until where it stops e.g. range(1, 4) will give numbers 1, 2 and 3 because it stops at 4
        for i in range(1, 4+1):

            print(str(i)+": "+list_main[0][i])

        def DwellingFunction():

            dwellingSelection = int(input("Select dwelling type: "))
            sum1 = 0  # initalise the sum for the average later
            sum2 = 0

            # get values from jan to apr
            for j in range(1, 5):

                sum1 += double(list_main[j][dwellingSelection])

            for k in range(9, 13):

                sum2 += double(list_main[k][dwellingSelection])

            avgConsumption1 = sum1 / j
            avgConsumption2 = sum2 / j
            print(str(round(avgConsumption1)) +
                  "GWh is the average electricity consumption for "+list_main[0][dwellingSelection]+" from Jan to Apr"+"\n"+str(round(avgConsumption2))+"GWh is the average electricity consumption for "+list_main[0][dwellingSelection]+" from Sep to Dec")
            print("The maximum electricity consumption for " +
                  list_main[0][dwellingSelection]+" from Jan to Apr is in the month of")
        DwellingFunction()
        Start()


Start()
