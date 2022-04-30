import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
import pandas as pd


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
    x_coordinate = (X*(df[2]+df[3]))/F_all
    list_X_coordinates_left_plate.append(x_coordinate)
    y_coordinate = (Y*(df[3]+df[4]))/F_all
    list_Y_coordinates_left_plate.append(y_coordinate)

list_X_coordinates_right_plate = []
list_Y_coordinates_right_plate = []
for i in range(len(df[1])):
    F_all = df[6][i] + df[7][i] + df[8][i] + df[9][i]
    x_coordinate = (X*(df[7]+df[8]))/F_all
    list_X_coordinates_right_plate.append(x_coordinate)
    y_coordinate = (Y*(df[8]+df[9]))/F_all
    list_Y_coordinates_right_plate.append(y_coordinate)

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
    list_X_coordinates_both_plates.append(
        (list_X_coordinates_left_plate_with_zero_at_the_middle_of_both_platforms[i] + list_X_coordinates_right_plate_with_zero_at_the_middle_of_both_platforms[i]) / 2)
    list_Y_coordinates_both_plates.append(
        (list_Y_coordinates_left_plate_with_zero_at_the_middle_of_the_platform[i] + list_Y_coordinates_right_plate_with_zero_at_the_middle_of_the_platform[i]) / 2)

plt.plot(list_X_coordinates_left_plate_with_zero_at_the_middle_of_both_platforms, list_Y_coordinates_left_plate_with_zero_at_the_middle_of_the_platform)
plt.plot(list_X_coordinates_right_plate_with_zero_at_the_middle_of_both_platforms, list_Y_coordinates_right_plate_with_zero_at_the_middle_of_the_platform)
plt.plot(list_X_coordinates_both_plates, list_Y_coordinates_both_plates)
plt.show()

