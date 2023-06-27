import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import math
import numpy as np
from scipy.stats import iqr
from scipy import signal
import statistics


time_period = ["Pre-surgery","Post-surgery","2 weeks","4 weeks"]
#time_period = ["2 weeks"]
name = input("What is the name of the Excel file") + "CoP" + ".xlsx"
Surgery_Leg = input("In which leg did the surgery took place")

# force_files =  ['subject1','subject3','subject7','subject8',
#                 'subject9','subject10','subject11','subject12','subject14','subject15','subject16','subject17','subject18','subject19'
#                 ,'subject20','subject21','subject22','subject23','subject24','subject25']
#
# knee = ['R','L','L','R','R','L','L','R','R','L','R','R','R','R','R','R','L','L','R','L']


while not Surgery_Leg == "Left" and not Surgery_Leg == "Right":
    Surgery_Leg = input("Write Left or Right")
writer = pd.ExcelWriter(name)

for t in time_period:
    filename = filedialog.askopenfilename(initialdir="C:\\",
                                          # initioaldir = "Which directory will the program open",
                                          title="Select the " + t + " CMV File",
                                          # title = "Title",
                                          filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
    # filetypes = (("name files", "*.name")) <--- which types of file should the program see
    # if you choose the csv file you will see that the text that it returns is the path of the file
    # Therefore we can use it like this
    df = pd.read_csv(filename,
                                 delimiter=',',
                                 decimal='.',
                                 thousands=',',
                                 skiprows=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16] ,
                                 header=None)
    #print(df)
    #Begining of filtering proccess
    column_name_to_be_filtered = [0,1,2,3,4,5,6,7,8,9,10]
    for ch in column_name_to_be_filtered:
        if ch == 0 or ch == 5 or ch == 10:
            if ch == 0:
                df_filtered = pd.DataFrame(data=df[0])
                #print(df_filtered)
            elif ch == 5:
                df_filtered[5] = df[5]
                #print(df_filtered)
            elif ch == 10:
                df_filtered[10] = df[10]
                #print(df_filtered)
        else:
            #Insert each column in a series
            f1 = df[ch]
            # Set the Sampling Frequancy (fc) and the Cut-off Frequency (fc)
            #fs = 75
            fs = 1/(df[0][1]-df[0][0])
            #print('fs:',fs)
            fc = 5
            # the 3 lines below are for the Low Butterworth filter
            w = fc / (fs / 2)
            b, a = signal.butter(4, w, 'low')
            f1_filtered = signal.filtfilt(b, a, f1)
            df_filtered[ch] = f1_filtered
            #print(df_filtered)


    X = 120
    Y = 260
    list_X_coordinates_left_plate = []
    list_Y_coordinates_left_plate = []
    for i in range(len(df_filtered[1])):
        F_all = df_filtered[1][i] + df_filtered[2][i] + df_filtered[3][i] + df_filtered[4][i]
        x_coordinate = (X*(df_filtered[2][i]+df_filtered[3][i]))/F_all
        list_X_coordinates_left_plate.append(x_coordinate)
        y_coordinate = (Y*(df_filtered[3][i]+df_filtered[4][i]))/F_all
        list_Y_coordinates_left_plate.append(y_coordinate)

    list_X_coordinates_right_plate = []
    list_Y_coordinates_right_plate = []
    for i in range(len(df_filtered[1])):
        F_all = df_filtered[6][i] + df_filtered[7][i] + df_filtered[8][i] + df_filtered[9][i]
        x_coordinate = (X*(df_filtered[7][i]+df_filtered[8][i]))/F_all
        list_X_coordinates_right_plate.append(x_coordinate)
        y_coordinate = (Y*(df_filtered[8][i]+df_filtered[9][i]))/F_all
        list_Y_coordinates_right_plate.append(y_coordinate)

    print(list_Y_coordinates_right_plate)
    list_X_coordinates_left_plate_with_zero_at_the_middle_of_the_platform = []
    list_Y_coordinates_left_plate_with_zero_at_the_middle_of_the_platform = []
    list_X_coordinates_right_plate_with_zero_at_the_middle_of_the_platform = []
    list_Y_coordinates_right_plate_with_zero_at_the_middle_of_the_platform = []
    for i in range(len(list_X_coordinates_left_plate)):
        list_X_coordinates_left_plate_with_zero_at_the_middle_of_the_platform.append(list_X_coordinates_left_plate[i] - 60)
        list_Y_coordinates_left_plate_with_zero_at_the_middle_of_the_platform.append(list_Y_coordinates_left_plate[i] - 130)
        list_X_coordinates_right_plate_with_zero_at_the_middle_of_the_platform.append(list_X_coordinates_right_plate[i] - 60)
        list_Y_coordinates_right_plate_with_zero_at_the_middle_of_the_platform.append(list_Y_coordinates_right_plate[i] - 130)

    list_X_coordinates_left_plate_with_zero_at_the_middle_of_both_platforms = []
    list_X_coordinates_right_plate_with_zero_at_the_middle_of_both_platforms = []
    for i in range(len(list_X_coordinates_left_plate_with_zero_at_the_middle_of_the_platform)):
        list_X_coordinates_left_plate_with_zero_at_the_middle_of_both_platforms.append(list_X_coordinates_left_plate_with_zero_at_the_middle_of_the_platform[i] - 60)
        list_X_coordinates_right_plate_with_zero_at_the_middle_of_both_platforms.append(list_X_coordinates_right_plate_with_zero_at_the_middle_of_the_platform[i] + 60)


    list_X_coordinates_both_plates = []
    list_Y_coordinates_both_plates = []
    for i in range(len(list_X_coordinates_right_plate)):
        list_X_coordinates_both_plates.append((list_X_coordinates_left_plate_with_zero_at_the_middle_of_both_platforms[i] + list_X_coordinates_right_plate_with_zero_at_the_middle_of_both_platforms[i]) / 2)
        list_Y_coordinates_both_plates.append((list_Y_coordinates_left_plate_with_zero_at_the_middle_of_the_platform[i] + list_Y_coordinates_right_plate_with_zero_at_the_middle_of_the_platform[i]) / 2)



    #Variables that will be calculated are:
    #Travel Distance
    #Inter Quatrile Range (IQR)
    #Power Spectrum***
    #Max-min range
    #Weight distribution

    #Travel Distance
    Total_Travel_Distance_of_left_leg = 0
    Total_Travel_Distance_of_right_leg = 0
    Total_Travel_Distance_of_both_legs = 0
    for i in range(len(list_X_coordinates_left_plate_with_zero_at_the_middle_of_both_platforms)):
        if i == 0:
            pass
        else:
            Travel_Distance_of_left_leg = math.sqrt((list_X_coordinates_left_plate_with_zero_at_the_middle_of_both_platforms[i] - list_X_coordinates_left_plate_with_zero_at_the_middle_of_both_platforms[i-1])**2 + (list_Y_coordinates_left_plate_with_zero_at_the_middle_of_the_platform[i] - list_Y_coordinates_left_plate_with_zero_at_the_middle_of_the_platform[i-1])**2)
            Total_Travel_Distance_of_left_leg = Total_Travel_Distance_of_left_leg + Travel_Distance_of_left_leg

            Travel_Distance_of_right_leg = math.sqrt((list_X_coordinates_right_plate_with_zero_at_the_middle_of_both_platforms[i] - list_X_coordinates_right_plate_with_zero_at_the_middle_of_both_platforms[i-1])**2 + (list_Y_coordinates_right_plate_with_zero_at_the_middle_of_the_platform[i] - list_Y_coordinates_right_plate_with_zero_at_the_middle_of_the_platform[i-1])**2)
            Total_Travel_Distance_of_right_leg = Total_Travel_Distance_of_right_leg + Travel_Distance_of_right_leg

            Travel_Distance_of_both_legs = math.sqrt((list_X_coordinates_both_plates[i] - list_X_coordinates_both_plates[i-1])**2 + (list_Y_coordinates_both_plates[i] - list_Y_coordinates_both_plates[i-1])**2)
            Total_Travel_Distance_of_both_legs = Total_Travel_Distance_of_both_legs + Travel_Distance_of_both_legs

    print("Total Travel Distance of the Left leg was " + str(Total_Travel_Distance_of_left_leg))
    print("Total Travel Distance of the Right leg was " + str(Total_Travel_Distance_of_right_leg))
    print("Total Travel Distance of Both legs was " + str(Total_Travel_Distance_of_both_legs))

    #IQR
    array_of_left_leg_X = np.array([list_X_coordinates_left_plate_with_zero_at_the_middle_of_both_platforms])
    array_of_left_leg_Y = np.array([list_Y_coordinates_left_plate_with_zero_at_the_middle_of_the_platform])
    array_of_right_leg_X = np.array([list_X_coordinates_right_plate_with_zero_at_the_middle_of_both_platforms])
    array_of_right_leg_Y = np.array([list_Y_coordinates_right_plate_with_zero_at_the_middle_of_the_platform])
    array_of_both_legs_X = np.array([list_X_coordinates_both_plates])
    array_of_both_legs_Y = np.array([list_Y_coordinates_both_plates])

    IQR_of_left_leg_X = iqr(array_of_left_leg_X)
    IQR_of_left_leg_Y = iqr(array_of_left_leg_Y)
    IQR_of_right_leg_X = iqr(array_of_right_leg_X)
    IQR_of_right_leg_Y = iqr(array_of_right_leg_Y)
    IQR_of_both_legs_X = iqr(array_of_both_legs_X)
    IQR_of_both_legs_Y = iqr(array_of_both_legs_Y)
    print("IQR_of_Left_leg_X:" + str(IQR_of_left_leg_X))
    print("IQR_of_Left_leg_Y:" + str(IQR_of_left_leg_Y))
    print("IQR_of_Right_leg_X:" + str(IQR_of_right_leg_X))
    print("IQR_of_Right_leg_Y:" + str(IQR_of_right_leg_Y))
    print("IQR_of_Both_legs_X:" + str(IQR_of_both_legs_X))
    print("IQR_of_Both_legs_Y:" + str(IQR_of_both_legs_Y))


    plt.plot(list_X_coordinates_left_plate_with_zero_at_the_middle_of_both_platforms, list_Y_coordinates_left_plate_with_zero_at_the_middle_of_the_platform, label = "Left leg")
    plt.plot(list_X_coordinates_right_plate_with_zero_at_the_middle_of_both_platforms, list_Y_coordinates_right_plate_with_zero_at_the_middle_of_the_platform, label = "Right leg")
    plt.plot(list_X_coordinates_both_plates, list_Y_coordinates_both_plates, label = "Both leg")
    plt.legend()
    plt.show()

    #Min-max range
    Min_max_range_Left_X = abs(max(list_X_coordinates_left_plate_with_zero_at_the_middle_of_both_platforms) - min(list_X_coordinates_left_plate_with_zero_at_the_middle_of_both_platforms))
    Min_max_range_Left_Y = abs(max(list_Y_coordinates_left_plate_with_zero_at_the_middle_of_the_platform) - min(list_Y_coordinates_left_plate_with_zero_at_the_middle_of_the_platform))
    Min_max_range_Right_X = abs(max(list_X_coordinates_right_plate_with_zero_at_the_middle_of_both_platforms) - min(list_X_coordinates_right_plate_with_zero_at_the_middle_of_both_platforms))
    Min_max_range_Right_Y = abs(max(list_Y_coordinates_right_plate_with_zero_at_the_middle_of_the_platform) - min(list_Y_coordinates_right_plate_with_zero_at_the_middle_of_the_platform))
    Min_max_range_Both_X = abs(max(list_X_coordinates_both_plates) - min(list_X_coordinates_both_plates))
    Min_max_range_Both_Y = abs(max(list_Y_coordinates_both_plates) - min(list_Y_coordinates_both_plates))
    print("Min_max_range_Left_X" + str(Min_max_range_Left_X))
    print("Min_max_range_Left_Y" + str(Min_max_range_Left_Y))
    print("Min_max_range_Right_X" + str(Min_max_range_Right_X))
    print("Min_max_range_Right_Y" + str(Min_max_range_Right_Y))
    print("Min_max_range_Both_X" + str(Min_max_range_Both_X))
    print("Min_max_range_Both_Y" + str(Min_max_range_Both_Y))

    #Weight distribution
    #Create a list with the force output in each platform by adding the
    #Force of each transducer and then the whole force of both the platforms
    F_Left_leg = []
    F_Right_leg = []
    F_Both_legs = []
    for i in range(len(list_X_coordinates_both_plates)):
        F_Left_leg.append(df_filtered[1][i]+df_filtered[2][i]+df_filtered[3][i]+df_filtered[4][i])
        F_Right_leg.append(df_filtered[6][i]+df_filtered[7][i]+df_filtered[8][i]+df_filtered[9][i])
        F_Both_legs.append(F_Left_leg[i]+F_Right_leg[i])
    # print(F_Left_leg)
    # print(F_Right_leg)
    # print(F_Both_legs)
    # print(statistics.stdev(F_Both_legs))
    # plt.plot(F_Both_legs)
    # plt.show()
    Percentage_of_F_Left_leg = []
    Percentage_of_F_Right_leg = []

    for i in range(len(F_Left_leg)):
        Percentage_of_F_Left_leg.append((F_Left_leg[i] / F_Both_legs[i]) * 100)
        Percentage_of_F_Right_leg.append((F_Right_leg[i] / F_Both_legs[i]) * 100)

    #Average of Forces in left, right and both
    sum_Left = 0
    sum_Right = 0
    sum_Both = 0
    for i  in range(len(F_Left_leg)):
        sum_Left += F_Left_leg[i]
        sum_Right += F_Right_leg[i]
        sum_Both += F_Both_legs[i]
    Average_Left_leg = sum_Left / len(F_Left_leg)
    Average_Right_leg = sum_Right / len(F_Right_leg)
    Average_Both_legs = sum_Both / len(F_Both_legs)
    print("Average_Left_leg :" + str(Average_Left_leg))
    print("Average_Right_leg :" + str(Average_Right_leg))
    print("Average_Both_legs :" + str(Average_Both_legs))
    SD_Left_leg = statistics.stdev(F_Left_leg)
    SD_Right_leg = statistics.stdev(F_Right_leg)
    SD_Both_legs = statistics.stdev(F_Both_legs)
    print("SD_Left_leg :" + str(SD_Left_leg))
    print("SD_Right_leg :" + str(SD_Right_leg))
    print("SD_Both_legs :" + str(SD_Both_legs))
    #Creation of Excel File
    #Creation of Dataframe which will be turned into an excel file
    if Surgery_Leg == "Left":
        Column_1 = ["CoP", "Left S", "x (mm)"]
        for i in range(len(list_X_coordinates_left_plate_with_zero_at_the_middle_of_both_platforms)):
            Column_1.append(list_X_coordinates_left_plate_with_zero_at_the_middle_of_both_platforms[i])
        Column_2 = ["CoP", "Left S", "y (mm)"]
        for i in range(len(list_Y_coordinates_left_plate_with_zero_at_the_middle_of_the_platform)):
            Column_2.append(list_Y_coordinates_left_plate_with_zero_at_the_middle_of_the_platform[i])
        Column_3 = ["CoP", "Left S", "F (%)"]
        for i in range(len(Percentage_of_F_Left_leg)):
            Column_3.append(Percentage_of_F_Left_leg[i])
        Column_4 = ["CoP", "Right", "x (mm)"]
        for i in range(len(list_X_coordinates_right_plate_with_zero_at_the_middle_of_both_platforms)):
            Column_4.append(list_X_coordinates_right_plate_with_zero_at_the_middle_of_both_platforms[i])
        Column_5 = ["CoP", "Right", "y (mm)"]
        for i in range(len(list_Y_coordinates_right_plate_with_zero_at_the_middle_of_the_platform)):
            Column_5.append(list_Y_coordinates_right_plate_with_zero_at_the_middle_of_the_platform[i])
        Column_6 = ["CoP", "Right", "F (%)"]
        for i in range(len(Percentage_of_F_Right_leg)):
            Column_6.append(Percentage_of_F_Right_leg[i])
        Column_7 = ["CoP", "Both", "x (mm)"]
        for i in range(len(list_X_coordinates_both_plates)):
            Column_7.append(list_X_coordinates_both_plates[i])
        Column_8 = ["CoP", "Both", "y (mm)"]
        for i in range(len(list_Y_coordinates_both_plates)):
            Column_8.append(list_Y_coordinates_both_plates[i])
        Column_9 = [""]
        Column_10 = ["","Left S", "Right", "Both"]
        Column_11 = ["Average Force (kg)",Average_Left_leg, Average_Right_leg, Average_Both_legs]
        Column_12 = ["","Left S", "Right", "Both"]
        Column_13 = ["Stdev Force (kg)",SD_Left_leg, SD_Right_leg, SD_Both_legs]
        Column_14 = ["","Left S", "Right", "Both"]
        Column_15 = ["IQR x (mm)", IQR_of_left_leg_X, IQR_of_right_leg_X, IQR_of_both_legs_X]
        Column_16 = ["IQR y (mm)", IQR_of_left_leg_Y, IQR_of_right_leg_Y, IQR_of_both_legs_Y]
        Column_17 = ["", "Left S", "Right", "Both"]
        Column_18 = ["Travel distance (mm)",Total_Travel_Distance_of_left_leg, Total_Travel_Distance_of_right_leg, Total_Travel_Distance_of_both_legs]
        Column_19 = ["", "Left S", "Right", "Both"]
        Column_20 = ["Min to Max x (mm)", Min_max_range_Left_X, Min_max_range_Right_X, Min_max_range_Both_X]
        Column_21 = ["Min to Max y (mm)", Min_max_range_Left_Y, Min_max_range_Right_Y, Min_max_range_Both_Y]
    else:
        Column_1 = ["CoP", "Left", "x (mm)"]
        for i in range(len(list_X_coordinates_left_plate_with_zero_at_the_middle_of_both_platforms)):
            Column_1.append(list_X_coordinates_left_plate_with_zero_at_the_middle_of_both_platforms[i])
        Column_2 = ["CoP", "Left", "y (mm)"]
        for i in range(len(list_Y_coordinates_left_plate_with_zero_at_the_middle_of_the_platform)):
            Column_2.append(list_Y_coordinates_left_plate_with_zero_at_the_middle_of_the_platform[i])
        Column_3 = ["CoP", "Left", "F (%)"]
        for i in range(len(Percentage_of_F_Left_leg)):
            Column_3.append(Percentage_of_F_Left_leg[i])
        Column_4 = ["CoP", "Right S", "x (mm)"]
        for i in range(len(list_X_coordinates_right_plate_with_zero_at_the_middle_of_both_platforms)):
            Column_4.append(list_X_coordinates_right_plate_with_zero_at_the_middle_of_both_platforms[i])
        Column_5 = ["CoP", "Right S", "y (mm)"]
        for i in range(len(list_Y_coordinates_right_plate_with_zero_at_the_middle_of_the_platform)):
            Column_5.append(list_Y_coordinates_right_plate_with_zero_at_the_middle_of_the_platform[i])
        Column_6 = ["CoP", "Right S", "F (%)"]
        for i in range(len(Percentage_of_F_Right_leg)):
            Column_6.append(Percentage_of_F_Right_leg[i])
        Column_7 = ["CoP", "Both", "x (mm)"]
        for i in range(len(list_X_coordinates_both_plates)):
            Column_7.append(list_X_coordinates_both_plates[i])
        Column_8 = ["CoP", "Both", "y (mm)"]
        for i in range(len(list_Y_coordinates_both_plates)):
            Column_8.append(list_Y_coordinates_both_plates[i])
        Column_9 = [""]
        Column_10 = ["","Left", "Right S", "Both"]
        Column_11 = ["Average Force (kg)",Average_Left_leg, Average_Right_leg, Average_Both_legs]
        Column_12 = ["","Left", "Right S", "Both"]
        Column_13 = ["Stdev Force (kg)",SD_Left_leg, SD_Right_leg, SD_Both_legs]
        Column_14 = ["","Left", "Right S", "Both"]
        Column_15 = ["IQR x (mm)", IQR_of_left_leg_X, IQR_of_right_leg_X, IQR_of_both_legs_X]
        Column_16 = ["IQR y (mm)", IQR_of_left_leg_Y, IQR_of_right_leg_Y, IQR_of_both_legs_Y]
        Column_17 = ["", "Left", "Right S", "Both"]
        Column_18 = ["Travel distance (mm)",Total_Travel_Distance_of_left_leg, Total_Travel_Distance_of_right_leg, Total_Travel_Distance_of_both_legs]
        Column_19 = ["", "Left", "Right S", "Both"]
        Column_20 = ["Min to Max x (mm)", Min_max_range_Left_X, Min_max_range_Right_X, Min_max_range_Both_X]
        Column_21 = ["Min to Max y (mm)", Min_max_range_Left_Y, Min_max_range_Right_Y, Min_max_range_Both_Y]
    result_list = [Column_1, Column_2, Column_3, Column_4,
                       Column_5, Column_6, Column_7, Column_8,
                       Column_9,Column_10, Column_11, Column_12,
                       Column_13, Column_14, Column_15, Column_16,
                       Column_17, Column_18, Column_19, Column_20,
                       Column_21]
    Excel_Both_legs_df = pd.DataFrame(result_list)
    Excel_Both_legs_df = Excel_Both_legs_df.T
    Excel_Both_legs_df.to_excel(writer,sheet_name=t)


    # if t == "4 weeks":
    #     with pd.ExcelWriter(name) as writer:
    #         Excel_Both_legs_df.to_excel(writer, sheet_name=t)
    # else:
    #     with pd.ExcelWriter(name, mode="a", engine="openpyxl") as writer:
    #         Excel_Both_legs_df.to_excel(writer, sheet_name=t)

writer.close()
