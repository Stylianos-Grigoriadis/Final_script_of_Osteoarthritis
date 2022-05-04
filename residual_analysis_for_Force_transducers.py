import pandas as pd
import matplotlib.pyplot as plt
import math
import lib_Milonas
from scipy import signal
import numpy as np
from matplotlib.widgets import Slider
from matplotlib.widgets import TextBox

# Fs = Sampling Frequency
fs = 75


# df = pd.read_csv('C:\Python_projects\Final_script_of_Osteoarthritis\stance evaluation_Μαλουτα Παρθένα  21Φεβ22_09_43_34.csv')
# print(df)
#
# Transducers_names_in_columns = ['CHANNEL_1','CHANNEL_2','CHANNEL_3','CHANNEL_4','CHANNEL_1.1','CHANNEL_2.1','CHANNEL_3.1','CHANNEL_4.1',]
# for ch in Transducers_names_in_columns:
#     f1 = df[ch]
#
#     R_fc = []
#     fc2 = []
#
#     for fc in range(1,20):
#         f1_filtered = lib_Milonas.Butterworth(Fs,fc,f1)
#         # Winter equation (3.9)
#         sum=0
#         differences = []
#         for xi,xi_hat in zip(f1,f1_filtered):
#             x_diff = xi-xi_hat
#             differences.append(x_diff)
#             sum+=(x_diff)**2
#         sum=sum/len(f1)
#         R_fc.append(math.sqrt(sum))
#         # plt.title(fc)
#         # plt.plot(f1_filtered,label='filtered')
#         # plt.plot(f1,label='raw')
#         # plt.legend()
#         # plt.show()
#
#     plt.plot(R_fc,label=ch)
# plt.legend()
# plt.show()
def create_a_df_for_all_the_residuals(df):

    for i in column_name_to_be_filtered:
        R_fc = []
        if i == 0 or i == 5 or i ==10:
            pass
        elif i == 1:
            f1 = df[i]
            for fc in range(1, 20):
                w = fc / (fs / 2)
                b, a = signal.butter(4, w, 'low')
                f1_filtered = signal.filtfilt(b, a, f1)
                #find the residuals
                sum = 0
                differences = []
                for xi, xi_hat in zip(f1, f1_filtered):
                    x_diff = xi-xi_hat
                    differences.append(x_diff)
                    sum+=(x_diff)**2
                sum=sum/len(f1)
                R_fc.append(math.sqrt(sum))

            df_residuals_of_a_single_trial = pd.DataFrame(data=R_fc,columns = [1])
            # print(df_residuals_of_a_single_trial)
        else:
            f1 = df[i]
            for fc in range(1, 20):
                w = fc / (fs / 2)
                b, a = signal.butter(4, w, 'low')
                f1_filtered = signal.filtfilt(b, a, f1)
                # find the residuals
                sum = 0
                differences = []
                for xi, xi_hat in zip(f1, f1_filtered):
                    x_diff = xi - xi_hat
                    differences.append(x_diff)
                    sum += (x_diff) ** 2
                sum = sum / len(f1)
                R_fc.append(math.sqrt(sum))

            df_residuals_of_a_single_trial[i] = R_fc
            # print(df_residuals_of_a_single_trial)
            # print(type(df_residuals_of_a_single_trial))
            #return df_residuals_of_a_single_trial
    # print(df_residuals_of_a_single_trial.columns)
    # print(df_residuals_of_a_single_trial)
    # print(type(df_residuals_of_a_single_trial))
    list_of_average_residual = []
    for j in range(0,19):
        average_residual = (df_residuals_of_a_single_trial[1][j]+df_residuals_of_a_single_trial[2][j]+df_residuals_of_a_single_trial[3][j]+df_residuals_of_a_single_trial[4][j]+df_residuals_of_a_single_trial[6][j]+df_residuals_of_a_single_trial[7][j]+df_residuals_of_a_single_trial[8][j]+df_residuals_of_a_single_trial[9][j])/8

        list_of_average_residual.append(average_residual)
    return list_of_average_residual
# print(list_of_average_residual)
# plt.plot(list_of_average_residual)
# plt.show()

list_of_CoP_name_files = ["C:\Python_projects\Final_script_of_Osteoarthritis\Test of residuals\stance evaluation_Μαλουτα Παρθένα  21Φεβ22_09_43_34.csv",
                          "C:\Python_projects\Final_script_of_Osteoarthritis\Test of residuals\stance evaluation_Μαλουτα Παρθένα  25Φεβ22_09_41_01.csv",
                          "C:\Python_projects\Final_script_of_Osteoarthritis\Test of residuals\stance evaluation_Μαλουτα Παρθένα  11Mar22_10_17_50.csv",
                          "C:\Python_projects\Final_script_of_Osteoarthritis\Test of residuals\stance evaluation_Μαλουτα Παρθένα  29Mar22_10_39_21.csv",
                          "C:\Python_projects\Final_script_of_Osteoarthritis\Test of residuals\stance evaluation_Παπαδόπουλος  Ιωάννης   28Feb22_10_01_17.csv",
                          "C:\Python_projects\Final_script_of_Osteoarthritis\Test of residuals\stance evaluation_Παπαδόπουλος  Ιωάννης   04Mar22_09_12_16.csv",
                          "C:\Python_projects\Final_script_of_Osteoarthritis\Test of residuals\stance evaluation_Παπαδόπουλος  Ιωάννης   21Mar22_10_00_59.csv",
                          "C:\Python_projects\Final_script_of_Osteoarthritis\Test of residuals\stance evaluation_Παπαδόπουλος  Ιωάννης   04Απρ22_10_36_52.csv",
                          "C:\Python_projects\Final_script_of_Osteoarthritis\Test of residuals\stance evaluation_Μπατζακη Πολυξένη   14Mar22_09_51_45.csv",
                          "C:\Python_projects\Final_script_of_Osteoarthritis\Test of residuals\stance evaluation_Μπατζακη Πολυξένη   18Mar22_09_51_40.csv",
                          "C:\Python_projects\Final_script_of_Osteoarthritis\Test of residuals\stance evaluation_Μπατζακη Πολυξένη   03Απρ22_19_16_50.csv",
                          "C:\Python_projects\Final_script_of_Osteoarthritis\Test of residuals\stance evaluation_Μπατζακη Πολυξένη   20Απρ22_09_49_12.csv",
                          "C:\Python_projects\Final_script_of_Osteoarthritis\Test of residuals\stance evaluation_Χανδολιας  Χρήστος   28Mar22_10_17_41.csv",
                          "C:\Python_projects\Final_script_of_Osteoarthritis\Test of residuals\stance evaluation_Χανδολιας  Χρήστος   03Apr22_10_31_38.csv",
                          "C:\Python_projects\Final_script_of_Osteoarthritis\Test of residuals\stance evaluation_Χανδολιας  Χρήστος   15Apr22_08_57_33.csv",]

for i in range(len(list_of_CoP_name_files)):
    # print(list_of_CoP_name_files[i])
    df = pd.read_csv(list_of_CoP_name_files[i],
        delimiter=',',
        decimal='.',
        thousands=',',
        skiprows=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
        header=None)
    column_name_to_be_filtered = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # print(i)
    residual = create_a_df_for_all_the_residuals(df)
    if i == 0:
        df_residuals_of_all_the_trials = pd.DataFrame(data=residual, columns=[0])
    else:
        df_residuals_of_all_the_trials[i] = residual
print(df_residuals_of_all_the_trials)
Names_of_labels_for_plotting = ["Μαλούτα Pre","Μαλούτα Post","Μαλούτα 2 weeks","Μαλούτα 4 weeks","Παπαδόπουλος Pre","Παπαδόπουλος Post","Παπαδόπουλος 2 weeks","Παπαδόπουλος 4 weeks","Μπατζάκη Pre","Μπατζάκη Post","Μπατζάκη 2 weeks","Μπατζάκη 4 weeks","Χανδολιάς Pre","Χανδολιάς Post","Χανδολιάς 2 weeks"]
# for i in range(len(df_residuals_of_all_the_trials.columns)):
#     plt.plot(df_residuals_of_all_the_trials[i],label = Names_of_labels_for_plotting[i])

plt.plot(df_residuals_of_all_the_trials[0],label = Names_of_labels_for_plotting[0],color="red",linestyle="solid")
plt.plot(df_residuals_of_all_the_trials[1],label = Names_of_labels_for_plotting[1],color="red",linestyle="dotted")
plt.plot(df_residuals_of_all_the_trials[2],label = Names_of_labels_for_plotting[2],color="red",linestyle="dashed")
plt.plot(df_residuals_of_all_the_trials[3],label = Names_of_labels_for_plotting[3],color="red",linestyle=(0, (3, 5, 1, 5)))
plt.plot(df_residuals_of_all_the_trials[4],label = Names_of_labels_for_plotting[4],color="black",linestyle="solid")
plt.plot(df_residuals_of_all_the_trials[5],label = Names_of_labels_for_plotting[5],color="black",linestyle="dotted")
plt.plot(df_residuals_of_all_the_trials[6],label = Names_of_labels_for_plotting[6],color="black",linestyle="dashed")
plt.plot(df_residuals_of_all_the_trials[7],label = Names_of_labels_for_plotting[7],color="black",linestyle=(0, (3, 5, 1, 5)))
plt.plot(df_residuals_of_all_the_trials[8],label = Names_of_labels_for_plotting[8],color="blue",linestyle="solid")
plt.plot(df_residuals_of_all_the_trials[9],label = Names_of_labels_for_plotting[9],color="blue",linestyle="dotted")
plt.plot(df_residuals_of_all_the_trials[10],label = Names_of_labels_for_plotting[10],color="blue",linestyle="dashed")
plt.plot(df_residuals_of_all_the_trials[11],label = Names_of_labels_for_plotting[11],color="blue",linestyle=(0, (3, 5, 1, 5)))
plt.plot(df_residuals_of_all_the_trials[12],label = Names_of_labels_for_plotting[12],color="green",linestyle="solid")
plt.plot(df_residuals_of_all_the_trials[13],label = Names_of_labels_for_plotting[13],color="green",linestyle="dotted")
plt.plot(df_residuals_of_all_the_trials[14],label = Names_of_labels_for_plotting[14],color="green",linestyle="dashed")
# axfreq = plt.axes([0.162, 0, 0.705, 0.05])
# amp_slider = Slider(
#     ax = axfreq,
#     label="Amplitude",
#     valmin=0,
#     valmax=18,
#     orientation="horizontal")
# def update(val):
#     plt.lines.Line2D(xdata = 0.6,ydata = val)
# amp_slider.on_changed(update)
plt.legend()
plt.show()