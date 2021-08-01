from csv import reader
import matplotlib.pyplot as plot
from numpy import double
import pandas as pd


def Start():

    def CSV():

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
            "1: Show full data of monthly electricity consumptions\n2: Display the monthly electricity consumptions of all dwelling types in march (units in GWh)\n3: Select dwelling type to display program functions\n4: Graphs\n5: Quit\n\n"
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

        for i in range(5):

            print(list_main[0][i]+": "+list_main[3][i])

        Start()

    if menuOptions == 3:

        # there is a +1 because range() includes the first number until where it stops e.g. range(1, 4) will give numbers 1, 2 and 3 because it stops at 4
        for i in range(1, 4+1):

            print(str(i)+": "+list_main[0][i])

        def DwellingFunction():

            dwellingSelection = int(input("Select dwelling type: "))
            sum1 = 0  # initalise the sum for the average later
            sum2 = 0
            # list to find the highest electricity consumption in given period
            list1 = []
            list2 = []

            # get values from jan to apr
            for j in range(1, 5):

                sum1 += double(list_main[j][dwellingSelection])
                list1.append(double(list_main[j][dwellingSelection]))

            #  values for sep to dec
            for k in range(9, 13):

                sum2 += double(list_main[k][dwellingSelection])
                list2.append(double(list_main[k][dwellingSelection]))

            # avg consumption from jan to apr based on dwelling selection
            avgConsumption1 = sum1 / j
            # avg consumption from jan to apr based on dwelling selection
            avgConsumption2 = sum2 / j

            # max value from each period
            maxValue1 = max(list1)
            maxValue2 = max(list2)

            print(str(round(avgConsumption1)) +
                  "GWh is the average electricity consumption for "+list_main[0][dwellingSelection]+" from Jan to Apr"+"\n"+str(round(avgConsumption2))+"GWh is the average electricity consumption for "+list_main[0][dwellingSelection]+" from Sep to Dec")
            print(str("The maximum electricity consumption for the period of Jan to Apr is " +
                  str(maxValue1)+"GWh and it is in the month of "+list_main[list1.index(maxValue1) + 1][0]))
            print(str("The maximum electricity consumption for the period of Sep to Dec is " +
                  str(maxValue2)+"GWh and it is in the month of "+list_main[list2.index(maxValue2) + 9][0]))

            # init var
            sumForAvg = 0

            # the 6% qn
            for h in range(1, 13):

                # find annual average
                sumForAvg += double(list_main[h][dwellingSelection])

            annualAvg = sumForAvg / h

            for g in range(1, 13):

                if double(list_main[g][dwellingSelection]) <= annualAvg * 0.94:

                    print(str(list_main[g][0])+" has an electricity consumption of "+str(
                        list_main[g][dwellingSelection])+" which is at least 6% lower than the annual average of "+str(annualAvg))

        DwellingFunction()
        Start()

    if menuOptions == 4:

        x_axis = []
        y_axis_1 = []
        y_axis_2 = []

        for p in range(1, 13):

            # month
            x = list_main[p][0]
            x_axis.append(x)
            # private apts
            y1 = list_main[p][2]
            y_axis_1.append(y1)
            # landed
            y2 = list_main[p][3]
            y_axis_2.append(y2)

        graphSelecton = int(
            input("1: Line Plots\n2: Bar Plot (Landed Property)\n3: Bar Plot(Private Apt/Condo)\n\n"))

        if graphSelecton == 1:

            plot.plot(x_axis, y_axis_2, label='Landed Property')
            plot.plot(x_axis, y_axis_1, label='Private Apt/Condo')
            plot.ylabel('Electricity Consumption')
            plot.xlabel('Months')
            plot.title('Private Apt/Condo, Landed Property vs Month')
            plot.legend()
            plot.show()

        if graphSelecton == 2:

            plot.bar(x_axis, y_axis_2, label='Landed Property')
            plot.ylabel('Electricity Consumption')
            plot.xlabel('Months')
            plot.title('Private Apt/Condo, Landed Property vs Month')
            plot.legend()
            plot.show()

        if graphSelecton == 3:

            plot.bar(x_axis, y_axis_1, label='Private Apt/Condo')
            plot.ylabel('Electricity Consumption')
            plot.xlabel('Months')
            plot.title('Private Apt/Condo, Landed Property vs Month')
            plot.legend()
            plot.show()

        Start()

    if menuOptions == 5:

        quit()


Start()
