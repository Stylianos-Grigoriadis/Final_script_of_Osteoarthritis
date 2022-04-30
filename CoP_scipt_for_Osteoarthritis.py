import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import math
import numpy as np
from scipy.stats import iqr

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
X = 120
Y = 260
list_X_coordinates_left_plate = []
list_Y_coordinates_left_plate = []
for i in range(len(df[1])):
    F_all = df[1][i] + df[2][i] + df[3][i] + df[4][i]
    x_coordinate = (X*(df[2][i]+df[3][i]))/F_all
    list_X_coordinates_left_plate.append(x_coordinate)
    y_coordinate = (Y*(df[3][i]+df[4][i]))/F_all
    list_Y_coordinates_left_plate.append(y_coordinate)

list_X_coordinates_right_plate = []
list_Y_coordinates_right_plate = []
for i in range(len(df[1])):
    F_all = df[6][i] + df[7][i] + df[8][i] + df[9][i]
    x_coordinate = (X*(df[7][i]+df[8][i]))/F_all
    list_X_coordinates_right_plate.append(x_coordinate)
    y_coordinate = (Y*(df[8][i]+df[9][i]))/F_all
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


