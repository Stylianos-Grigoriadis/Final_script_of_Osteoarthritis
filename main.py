# First do the force
import pandas as pd
from tkinter import filedialog
import matplotlib.pyplot as plt

# select the force file you want to analyse
# df_force = filedialog.askopenfilename(initialdir="C:\\",
#                                       # initioaldir = "Which directory will the program open",
#                                       title="Select CMV File",
#                                       # title = "Title",
#                                       filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
# for i in range(len(df_force)):
#     try:
#         df_force['Time'][i] = float(df_force['Time'][i])
#         df_force['Data'][i] = float(df_force['Data'][i])
#     except:
#         pass
# sens = []
# muscle = []
# for i in range(len(df_force)):
#     if df_force['Time'][i] == 'Device: Sens':
#         sens.append(i)
#
#     if df_force['Time'][i] == 'Device: Muscle':
#         muscle.append(i)

filename = filedialog.askopenfilename(initialdir="C:\\",
                                      # initioaldir = "Which directory will the program open",
                                      title="Select CSV File",
                                      # title = "Title",
                                      filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
df_CoP = pd.read_csv(filename,
                     delimiter=',',
                     decimal='.',
                     thousands=',',
                     skiprows=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                     header=None)
print(df_CoP)
list_X_coordinates_left_plate = []
list_Y_coordinates_left_plate = []
for i in range(len(df_CoP[1])):
    F_all = df_CoP[1][i] + df_CoP[2][i] + df_CoP[3][i] + df_CoP[4][i]
    x_coordinate = (120 / 2) * (
            1 + (((df_CoP[2][i] + df_CoP[3][i]) - (df_CoP[1][i] + df_CoP[4][i])) / F_all))
    x_coordinate -= 60
    list_X_coordinates_left_plate.append(x_coordinate)
    y_coordinate = (260 / 2) * (
            1 + (((df_CoP[4][i] + df_CoP[3][i]) - (df_CoP[1][i] + df_CoP[2][i])) / F_all))
    y_coordinate -= 130
    list_Y_coordinates_left_plate.append(y_coordinate)
print(list_X_coordinates_left_plate)
print(list_Y_coordinates_left_plate)
list_X_coordinates_right_plate = []
list_Y_coordinates_right_plate = []
for i in range(len(df_CoP[1])):
    F_all = df_CoP[6][i] + df_CoP[7][i] + df_CoP[8][i] + df_CoP[9][i]
    x_coordinate = (120 / 2) * (
            1 + (((df_CoP[7][i] + df_CoP[8][i]) - (df_CoP[6][i] + df_CoP[9][i])) / F_all))
    x_coordinate -= 60
    list_X_coordinates_right_plate.append(x_coordinate)
    y_coordinate = (260 / 2) * (
            1 + (((df_CoP[9][i] + df_CoP[8][i]) - (df_CoP[6][i] + df_CoP[7][i])) / F_all))
    y_coordinate -= 130
    list_Y_coordinates_right_plate.append(y_coordinate)
list_X_coordinates_left_plate_to_create_both_plates = []
list_X_coordinates_right_plate_to_create_both_plates = []
for i in range(len(list_X_coordinates_left_plate)):
    list_X_coordinates_left_plate_to_create_both_plates.append(list_X_coordinates_left_plate[i] - 60)
    list_X_coordinates_right_plate_to_create_both_plates.append(list_X_coordinates_right_plate[i] + 60)
list_X_coordinates_both_plates = []
list_Y_coordinates_both_plates = []
for i in range(len(list_X_coordinates_left_plate)):
    list_X_coordinates_both_plates.append((list_X_coordinates_right_plate_to_create_both_plates[i] + list_X_coordinates_left_plate_to_create_both_plates[i])/2)
    list_Y_coordinates_both_plates.append((list_Y_coordinates_right_plate[i]+list_Y_coordinates_left_plate[i])/2)

plt.plot(list_X_coordinates_right_plate_to_create_both_plates, list_Y_coordinates_right_plate, label='Rigth leg')
plt.plot(list_X_coordinates_left_plate_to_create_both_plates, list_Y_coordinates_left_plate, label='Left leg')
plt.plot(list_X_coordinates_both_plates, list_Y_coordinates_both_plates, label='Both legs')
plt.legend()
plt.show()

