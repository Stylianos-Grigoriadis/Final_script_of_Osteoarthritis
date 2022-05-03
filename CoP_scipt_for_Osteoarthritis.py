import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import math
import numpy as np
from scipy.stats import iqr
from scipy import signal


filename = filedialog.askopenfilename(initialdir="C:\\",
                                                       # initioaldir = "Which directory will the program open",
                                                       title="Select CSV File",
                                                       # title = "Title",
                                                       filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
            # filetypes = (("name files", "*.name")) <--- which types of file should the program see
            # if you choose the csv file you will see that the text that it returns is the path of the file
            # Therefore we can use it like this
df = pd.read_csv(filename,
                             delimiter=',',
                             decimal='.',
                             thousands=',',
                             skiprows=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                             header=None)
print(df)
#Begining of filtering proccess
column_name_to_be_filtered = [0,1,2,3,4,5,6,7,8,9,10]
for ch in column_name_to_be_filtered:
    if ch == 0 or ch == 5 or ch == 10:
        if ch == 0:
            df_filtered = pd.DataFrame(data=df[0])
            print(df_filtered)
        elif ch == 5:
            df_filtered[5] = df[5]
            print(df_filtered)
        elif ch == 10:
            df_filtered[10] = df[10]
            print(df_filtered)
    else:
        #Insert each column in a series
        f1 = df[ch]
        # Set the Sampling Frequancy (fc) and the Cut-off Frequency (fc)
        fs = 75
        fc = 3
        # the 3 lines below are for the Low Butterworth filter
        w = fc / (fs / 2)
        b, a = signal.butter(4, w, 'low')
        f1_filtered = signal.filtfilt(b, a, f1)
        df_filtered[ch] = f1_filtered
        print(df_filtered)


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
#Power Spectrum
#Max

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

print(Total_Travel_Distance_of_left_leg)
print(Total_Travel_Distance_of_right_leg)
print(Total_Travel_Distance_of_both_legs)

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
print(IQR_of_left_leg_X)
print(IQR_of_left_leg_Y)
print(IQR_of_right_leg_X)
print(IQR_of_right_leg_Y)
print(IQR_of_both_legs_X)
print(IQR_of_both_legs_Y)


plt.plot(list_X_coordinates_left_plate_with_zero_at_the_middle_of_both_platforms, list_Y_coordinates_left_plate_with_zero_at_the_middle_of_the_platform, label = "left leg")
plt.plot(list_X_coordinates_right_plate_with_zero_at_the_middle_of_both_platforms, list_Y_coordinates_right_plate_with_zero_at_the_middle_of_the_platform, label = "right leg")
plt.plot(list_X_coordinates_both_plates, list_Y_coordinates_both_plates, label = "both leg")
plt.legend()
plt.show()


