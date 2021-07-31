from csv import reader
import csv
import operator
from os import read
import math
import matplotlib.pyplot as plt


def Main():

    # scoping the csv file to be accessible by the functions
    def CSV():

        with open(r'/home/seanr/Downloads/programming-20210731T025856Z-001/programming/sgallelectricity_dataset (4).csv', 'r') as read_obj:

            # setting them as global variables so they are accessible within different functions
            global list_sorted
            global list_main

            # setting up sorted list and main list to be retrievable
            reader_csv = reader(read_obj, delimiter=',')
            list_sorted = sorted(
                reader_csv, key=operator.itemgetter(0), reverse=True)
            main_list = list(list_sorted)

    CSV()

    # init view
    try:
        # main options
        options = int(input(
            "1: Show full data of pedestrian crossing\n2: Display the number of pedestrian crossings by city in 2015\n3: Select city to display different functions \n4: Graph plotting\n5: Quit\nEnter a number from 1 to 5: "))
        if options < 1 or options > 5:
            print("Please put a valid number!")
            Main()
    except:
        print("Enter an integer!")
        Main()

    # init data
    if options == 1:

        # printing every line in the csv file
        for eachline in sortedList:
            print(eachline)
        Main()

    #  display number of pedestrian crossings by city in 2015
    if options == 2:

        for i in range(6):

            print(main_list[0][i]+": "+main_list[5][i])

        Main()

    # display mean of the number of pedestrian crossings for the 7-year span of 2013 to 2019.
    if options == 3:

        # for loop to show labels
        for i in range(1, 7):

            print(str(i)+": "+main_list[0][i])

        # calculate mean function and display the years and the number of pedestrian crossings if the number of pedestrian crossingshas decreased by at least 7% over the previous year
        def MeanCalculation_D():

            citySelection2a = int(input("Select city: "))
            sum = 0

            # get values from 2013 to 2019
            for i in range(1, 8):

                sum += int(main_list[i][citySelection2a])

            avg_pedestrians = sum / i
            print(str(math.floor(avg_pedestrians)) +
                  " is the average pedestrian crossings for "+main_list[0][citySelection2a])

            # if city exceeds average
            for j in range(1, 8):

                if int(main_list[j][citySelection2a]) > avg_pedestrians:

                    print(
                        main_list[j][0]+" exceeded the mean pedestrian crossing with a value of "+main_list[j][citySelection2a])

            # data starts from 2019 so list order has to be reversed
            for h in range(9, 1, -1):

                # check if the decrement % is atleast 7% from the previous year
                if int(main_list[h][citySelection2a]) <= int(main_list[h+1][citySelection2a]) * 0.93:

                    print(main_list[h][0]+" had a decrease of at least 7%")

        MeanCalculation_D()
        Main()

    if options == 4:

        graph_options = int(
            input("1: Eagle Pass + Progreso, Hidalgo vs Year\n2: El Paso, Laredo vs Year\nChoose which graph to show: "))

        if graph_options == 1:

            x_axis = []
            y_axis = []
            y_axis_2 = []

            for k in range(10, 0, -1):

                # year
                x = int(main_list[k][0])
                x_axis.append(x)
                # hidalgo
                y = int(main_list[k][4])
                # eagle pass + progreso
                y_axis.append(y)
                z = int(main_list[k][2]) + int(main_list[k][6])
                y_axis_2.append(z)

            plt.plot(x_axis, y_axis_2, label='Eagle Pass + Progreso')
            plt.plot(x_axis, y_axis, label='Hidalgo')
            plt.ylabel('Pedestrian Crossing')
            plt.xlabel('Years')
            plt.title('Eagle Pass + Progreso, Hidalgo vs Year')
            plt.legend()
            plt.show()

        if graph_options == 2:

            x_axis_2 = []
            y_axis_2_1 = []
            y_axis_2_2 = []

            for l in range(10, 0, -1):

                # year
                a = int(main_list[l][0])
                x_axis_2.append(a)
                # el paso
                b = int(main_list[l][3])
                y_axis_2_1.append(b)
                # laredo
                c = int(main_list[l][5])
                y_axis_2_2.append(c)

            plt.bar(x_axis_2, y_axis_2_1, label='El Paso')
            plt.bar(x_axis_2, y_axis_2_2, label='Laredo')
            plt.ylabel('Pedestrian Crossing')
            plt.xlabel('Years')
            plt.title('Eagle Pass + Progreso, Hidalgo vs Year')
            plt.legend()
            plt.show()

        Main()

    if options == 5:

        exit()


Main()
