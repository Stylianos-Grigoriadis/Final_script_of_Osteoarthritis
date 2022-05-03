import pandas as pd
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import SpanSelector
import statistics


time_period = ["Pre-surgery","Post-surgery","2 weeks","4 weeks"]
name = input("What is the name of the Excel file") + ".xlsx"
Surgery_Leg = input("In which leg did the surgery took place")
while not Surgery_Leg == "Left" and not Surgery_Leg == "Right":
    Surgery_Leg = input("Write Left or Right")

for t in time_period:
    def csv_transform(df):
        for i in range(len(df)):
            try:
                df['Time'][i] = float(df['Time'][i])
                df['Data'][i] = float(df['Data'][i])
            except:
                pass

        # Find the row in which the value is 'Device: Sens' and 'Device: Muscle' and append those in two lists
        sens = []
        muscle = []
        for i in range(len(df)):
            if df['Time'][i] == 'Device: Sens':
                sens.append(i)

            if df['Time'][i] == 'Device: Muscle':
                muscle.append(i)

        # Start iterating through the columns and keep the data and time to separate lists.
        # The iteration will start from the rows with: 'Device: Sens' and 'Device: Muscle' and
        # will end when a string value is found

        # For sens
        sens_data = []
        sens_time = []
        for sens_i in sens:
            sens_temp = []
            sens_temp_d = []

            for t, d in zip(df['Time'][sens_i + 2:], df['Data'][sens_i + 2:]):
                if isinstance(t, str):
                    break
                else:
                    sens_temp.append(t)
                    sens_temp_d.append(d)
            sens_data.append(sens_temp_d)
            sens_time.append(sens_temp)

        # For muscle
        muscle_data = []
        muscle_time = []

        for muscle_i in muscle:
            muscle_temp = []
            muscle_temp_d = []

            for t, d in zip(df['Time'][muscle_i + 2:], df['Data'][muscle_i + 2:]):
                if isinstance(t, str):
                    break
                else:
                    muscle_temp.append(t)
                    muscle_temp_d.append(d)
            muscle_data.append(muscle_temp_d)
            muscle_time.append(muscle_temp)

        # create 4 (one for each repetition) lists with 3 lists each
        ext1 = [sens_time[0], sens_data[0], muscle_data[0]]
        ext2 = [sens_time[1], sens_data[1], muscle_data[1]]
        flex1 = [sens_time[2], sens_data[2], muscle_data[2]]
        flex2 = [sens_time[3], sens_data[3], muscle_data[3]]

        # merge the above lists in one 12-item list (one item for each time-series)
        for i in ext2:
            ext1.append(i)
        for i in flex1:
            ext1.append(i)
        for i in flex2:
            ext1.append(i)

        # Transform the list to Dataframe, Transpose it and set column name

        final = pd.DataFrame(ext1)
        final = final.T
        final.columns = ['Ext1 Time', 'Ext1 Sens', 'Ext1 Muscle',
                         'Ext2 Time', 'Ext2 Sens', 'Ext2 Muscle',
                         'Flex1 Time', 'Flex1 Sens', 'Flex1 Muscle',
                         'Flex2 Time', 'Flex2 Sens', 'Flex2 Muscle']
        # print(final)

        # write the Dataframe to .xlsx file
        return final


    Left_df_force = filedialog.askopenfilename(initialdir="C:\\",
                                               # initioaldir = "Which directory will the program open",
                                               title="Select the " + t + " CMV File For Left leg",
                                               # title = "Title",
                                               filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
    left_df = pd.read_csv(Left_df_force, header=None, delimiter=',', decimal='.', names=['Time', 'Data'])

    left_newdf = csv_transform(left_df)
    print(left_newdf)
    Left_Columns_names = left_newdf.columns
    fig = plt.figure(figsize=(8, 12))
    fig.suptitle('Select the area in which the Force will be processed ', fontsize=16)

    ax1 = fig.add_subplot(511)
    ax1.set_title('Extension 1')
    ax1.plot(left_newdf['Ext1 Sens'], label='Sens')
    ax1.plot(left_newdf['Ext1 Muscle'], label='Muscle')

    ax2 = fig.add_subplot(512)
    ax2.set_title('Extension 2')
    ax2.plot(left_newdf['Ext2 Sens'], label='Sens')
    ax2.plot(left_newdf['Ext2 Muscle'], label='Muscle')

    ax3 = fig.add_subplot(513)
    ax3.set_title('Flexion 1')
    ax3.plot(left_newdf['Flex1 Sens'], label='Sens')
    ax3.plot(left_newdf['Flex1 Muscle'], label='Muscle')

    ax4 = fig.add_subplot(514)
    ax4.set_title('flexion 2')
    ax4.plot(left_newdf['Flex2 Sens'], label='Sens')
    ax4.plot(left_newdf['Flex2 Muscle'], label='Muscle')

    # lists to use in the on_select def
    Left_Ext1_Time = left_newdf['Ext1 Time'].tolist()
    Left_Ext1_Muscle = left_newdf['Ext1 Muscle'].tolist()
    Left_Ext2_Time = left_newdf['Ext2 Time'].tolist()
    Left_Ext2_Muscle = left_newdf['Ext2 Muscle'].tolist()
    Left_Flex1_Time = left_newdf['Flex1 Time'].tolist()
    Left_Flex1_Muscle = left_newdf['Flex1 Muscle'].tolist()
    Left_Flex2_Time = left_newdf['Flex2 Time'].tolist()
    Left_Flex2_Muscle = left_newdf['Flex2 Muscle'].tolist()


    def Left_on_select_1(ymin, ymax):
        global Left_this_Force1, Left_min_Force1, Left_max_Force1, Left_mean_Force_1, Left_standard_deviation_1, Left_Time1
        Left_this_Force1 = Left_Ext1_Muscle[int(ymin):int(ymax)]
        Left_this_Time1 = Left_Ext1_Time[int(ymin):int(ymax)]
        Left_min_Force1 = min(Left_this_Force1)
        Left_max_Force1 = max(Left_this_Force1)
        Left_mean_Force_1 = np.mean(Left_this_Force1)
        Left_standard_deviation_1 = statistics.stdev(Left_this_Force1)

        print("Average Force output of Ext1 was", Left_mean_Force_1)
        print("Standard deviation of the Force output of Ext1 was", Left_standard_deviation_1)
        print("Minimum Force output of Ext1 was", Left_min_Force1)
        print("Maximum Force output of Ext1 was", Left_max_Force1)
        Left_min_Time1 = min(Left_this_Time1)
        Left_max_Time1 = max(Left_this_Time1)
        Left_Time1 = Left_max_Time1 - Left_min_Time1
        print("Time in which the force is selected in Ext1 is ", Left_Time1)


    def Left_on_select_2(ymin, ymax):
        global Left_this_Force2, Left_min_Force2, Left_max_Force2, Left_mean_Force_2, Left_standard_deviation_2, Left_Time2
        Left_this_Force2 = Left_Ext2_Muscle[int(ymin):int(ymax)]
        Left_this_Time2 = Left_Ext2_Time[int(ymin):int(ymax)]
        Left_min_Force2 = min(Left_this_Force2)
        Left_max_Force2 = max(Left_this_Force2)
        Left_mean_Force_2 = np.mean(Left_this_Force2)
        Left_standard_deviation_2 = statistics.stdev(Left_this_Force2)

        print("Average Force output of Ext2 was", Left_mean_Force_2)
        print("Standard deviation of the Force output of Ext2 was", Left_standard_deviation_2)
        print("Minimum Force output of Ext2 was", Left_min_Force2)
        print("Maximum Force output of Ext2 was", Left_max_Force2)
        Left_min_Time2 = min(Left_this_Time2)
        Left_max_Time2 = max(Left_this_Time2)
        Left_Time2 = Left_max_Time2 - Left_min_Time2
        print("Time in which the force is selected in Ext2 is ", Left_Time2)


    def Left_on_select_3(ymin, ymax):
        global Left_this_Force3, Left_min_Force3, Left_max_Force3, Left_mean_Force_3, Left_standard_deviation_3, Left_Time3
        Left_this_Force3 = Left_Flex1_Muscle[int(ymin):int(ymax)]
        Left_this_Time3 = Left_Flex1_Time[int(ymin):int(ymax)]
        Left_min_Force3 = min(Left_this_Force3)
        Left_max_Force3 = max(Left_this_Force3)
        Left_mean_Force_3 = np.mean(Left_this_Force3)
        Left_standard_deviation_3 = statistics.stdev(Left_this_Force3)

        print("Average Force output of Flex1 was", Left_mean_Force_3)
        print("Standard deviation of the Force output of Flex1 was", Left_standard_deviation_3)
        print("Minimum Force output of Flex1 was", Left_min_Force3)
        print("Maximum Force output of Flex1 was", Left_max_Force3)
        Left_min_Time3 = min(Left_this_Time3)
        Left_max_Time3 = max(Left_this_Time3)
        Left_Time3 = Left_max_Time3 - Left_min_Time3
        print("Time in which the force is selected in Flex1 is ", Left_Time3)


    def Left_on_select_4(ymin, ymax):
        global Left_this_Force4, Left_min_Force4, Left_max_Force4, Left_mean_Force_4, Left_standard_deviation_4, Left_Time4
        Left_this_Force4 = Left_Flex2_Muscle[int(ymin):int(ymax)]
        Left_this_Time4 = Left_Flex2_Time[int(ymin):int(ymax)]
        Left_min_Force4 = min(Left_this_Force4)
        Left_max_Force4 = max(Left_this_Force4)
        Left_mean_Force_4 = np.mean(Left_this_Force4)
        Left_standard_deviation_4 = statistics.stdev(Left_this_Force4)

        print("Average Force output of Flex2 was", Left_mean_Force_4)
        print("Standard deviation of the Force output of Flex2 was", Left_standard_deviation_4)
        print("Minimum Force output of Flex2 was", Left_min_Force4)
        print("Maximum Force output of Flex2 was", Left_max_Force4)
        Left_min_Time4 = min(Left_this_Time4)
        Left_max_Time4 = max(Left_this_Time4)
        Left_Time4 = Left_max_Time4 - Left_min_Time4
        print("Time in which the force is selected in Flex2 is ", Left_Time4)


    Left_span1 = SpanSelector(ax1, Left_on_select_1, 'horizontal', useblit=True, interactive=True,
                              props=dict(alpha=0.5, facecolor='red'))
    Left_span2 = SpanSelector(ax2, Left_on_select_2, 'horizontal', useblit=True, interactive=True,
                              props=dict(alpha=0.5, facecolor='red'))
    Left_span3 = SpanSelector(ax3, Left_on_select_3, 'horizontal', useblit=True, interactive=True,
                              props=dict(alpha=0.5, facecolor='red'))
    Left_span4 = SpanSelector(ax4, Left_on_select_4, 'horizontal', useblit=True, interactive=True,
                              props=dict(alpha=0.5, facecolor='red'))

    plt.subplots_adjust(left=0.1,
                        bottom=0.1,
                        right=0.9,
                        top=0.9,
                        wspace=0.4,
                        hspace=0.4)
    plt.legend()
    plt.show()


    # Do the same for the right leg
    def csv_transform(df):
        for i in range(len(df)):
            try:
                df['Time'][i] = float(df['Time'][i])
                df['Data'][i] = float(df['Data'][i])
            except:
                pass

        # Find the row in which the value is 'Device: Sens' and 'Device: Muscle' and append those in two lists
        sens = []
        muscle = []
        for i in range(len(df)):
            if df['Time'][i] == 'Device: Sens':
                sens.append(i)

            if df['Time'][i] == 'Device: Muscle':
                muscle.append(i)

        # Start iterating through the columns and keep the data and time to separate lists.
        # The iteration will start from the rows with: 'Device: Sens' and 'Device: Muscle' and
        # will end when a string value is found

        # For sens
        sens_data = []
        sens_time = []
        for sens_i in sens:
            sens_temp = []
            sens_temp_d = []

            for t, d in zip(df['Time'][sens_i + 2:], df['Data'][sens_i + 2:]):
                if isinstance(t, str):
                    break
                else:
                    sens_temp.append(t)
                    sens_temp_d.append(d)
            sens_data.append(sens_temp_d)
            sens_time.append(sens_temp)

        # For muscle
        muscle_data = []
        muscle_time = []

        for muscle_i in muscle:
            muscle_temp = []
            muscle_temp_d = []

            for t, d in zip(df['Time'][muscle_i + 2:], df['Data'][muscle_i + 2:]):
                if isinstance(t, str):
                    break
                else:
                    muscle_temp.append(t)
                    muscle_temp_d.append(d)
            muscle_data.append(muscle_temp_d)
            muscle_time.append(muscle_temp)

        # create 4 (one for each repetition) lists with 3 lists each
        ext1 = [sens_time[0], sens_data[0], muscle_data[0]]
        ext2 = [sens_time[1], sens_data[1], muscle_data[1]]
        flex1 = [sens_time[2], sens_data[2], muscle_data[2]]
        flex2 = [sens_time[3], sens_data[3], muscle_data[3]]

        # merge the above lists in one 12-item list (one item for each time-series)
        for i in ext2:
            ext1.append(i)
        for i in flex1:
            ext1.append(i)
        for i in flex2:
            ext1.append(i)

        # Transform the list to Dataframe, Transpose it and set column name

        final = pd.DataFrame(ext1)
        final = final.T
        final.columns = ['Ext1 Time', 'Ext1 Sens', 'Ext1 Muscle',
                         'Ext2 Time', 'Ext2 Sens', 'Ext2 Muscle',
                         'Flex1 Time', 'Flex1 Sens', 'Flex1 Muscle',
                         'Flex2 Time', 'Flex2 Sens', 'Flex2 Muscle']

        return final

    Right_df_force = filedialog.askopenfilename(initialdir="C:\\",
                                                # initioaldir = "Which directory will the program open",
                                                title="Select the  " + t + "  CMV File for the Right leg",
                                                # title = "Title",
                                                filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
    Right_df = pd.read_csv(Right_df_force, header=None, delimiter=',', decimal='.', names=['Time', 'Data'])


    Right_newdf = csv_transform(Right_df)
    print(Right_newdf)
    Right_Columns_names = Right_newdf.columns
    fig = plt.figure(figsize=(8, 12))
    fig.suptitle('Select the area in which the Force will be processed ', fontsize=16)

    ax1 = fig.add_subplot(511)
    ax1.set_title('Extension 1')
    ax1.plot(Right_newdf['Ext1 Sens'], label='Sens')
    ax1.plot(Right_newdf['Ext1 Muscle'], label='Muscle')

    ax2 = fig.add_subplot(512)
    ax2.set_title('Extension 2')
    ax2.plot(Right_newdf['Ext2 Sens'], label='Sens')
    ax2.plot(Right_newdf['Ext2 Muscle'], label='Muscle')

    ax3 = fig.add_subplot(513)
    ax3.set_title('Flexion 1')
    ax3.plot(Right_newdf['Flex1 Sens'], label='Sens')
    ax3.plot(Right_newdf['Flex1 Muscle'], label='Muscle')

    ax4 = fig.add_subplot(514)
    ax4.set_title('flexion 2')
    ax4.plot(Right_newdf['Flex2 Sens'], label='Sens')
    ax4.plot(Right_newdf['Flex2 Muscle'], label='Muscle')

    # lists to use in the on_select def
    Right_Ext1_Time = Right_newdf['Ext1 Time'].tolist()
    Right_Ext1_Muscle = Right_newdf['Ext1 Muscle'].tolist()
    Right_Ext2_Time = Right_newdf['Ext2 Time'].tolist()
    Right_Ext2_Muscle = Right_newdf['Ext2 Muscle'].tolist()
    Right_Flex1_Time = Right_newdf['Flex1 Time'].tolist()
    Right_Flex1_Muscle = Right_newdf['Flex1 Muscle'].tolist()
    Right_Flex2_Time = Right_newdf['Flex2 Time'].tolist()
    Right_Flex2_Muscle = Right_newdf['Flex2 Muscle'].tolist()


    def Right_on_select_1(ymin, ymax):
        global Right_this_Force1, Right_min_Force1, Right_max_Force1, Right_mean_Force_1, Right_standard_deviation_1, Right_Time1
        Right_this_Force1 = Right_Ext1_Muscle[int(ymin):int(ymax)]
        Right_this_Time1 = Right_Ext1_Time[int(ymin):int(ymax)]
        Right_min_Force1 = min(Right_this_Force1)
        Right_max_Force1 = max(Right_this_Force1)
        Right_mean_Force_1 = np.mean(Right_this_Force1)
        Right_standard_deviation_1 = statistics.stdev(Right_this_Force1)

        print("Average Force output of Ext1 was", Right_mean_Force_1)
        print("Standard deviation of the Force output of Ext1 was", Right_standard_deviation_1)
        print("Minimum Force output of Ext1 was", Right_min_Force1)
        print("Maximum Force output of Ext1 was", Right_max_Force1)
        Right_min_Time1 = min(Right_this_Time1)
        Right_max_Time1 = max(Right_this_Time1)
        Right_Time1 = Right_max_Time1 - Right_min_Time1
        print("Time in which the force is selected in Ext1 is ", Right_Time1)


    def Right_on_select_2(ymin, ymax):
        global Right_this_Force2, Right_min_Force2, Right_max_Force2, Right_mean_Force_2, Right_standard_deviation_2, Right_Time2
        Right_this_Force2 = Right_Ext2_Muscle[int(ymin):int(ymax)]
        Right_this_Time2 = Right_Ext2_Time[int(ymin):int(ymax)]
        Right_min_Force2 = min(Right_this_Force2)
        Right_max_Force2 = max(Right_this_Force2)
        Right_mean_Force_2 = np.mean(Right_this_Force2)
        Right_standard_deviation_2 = statistics.stdev(Right_this_Force2)

        print("Average Force output of Ext2 was", Right_mean_Force_2)
        print("Standard deviation of the Force output of Ext2 was", Right_standard_deviation_2)
        print("Minimum Force output of Ext2 was", Right_min_Force2)
        print("Maximum Force output of Ext2 was", Right_max_Force2)
        Right_min_Time2 = min(Right_this_Time2)
        Right_max_Time2 = max(Right_this_Time2)
        Right_Time2 = Right_max_Time2 - Right_min_Time2
        print("Time in which the force is selected in Ext2 is ", Right_Time2)


    def Right_on_select_3(ymin, ymax):
        global Right_this_Force3, Right_min_Force3, Right_max_Force3, Right_mean_Force_3, Right_standard_deviation_3, Right_Time3
        Right_this_Force3 = Right_Flex1_Muscle[int(ymin):int(ymax)]
        Right_this_Time3 = Right_Flex1_Time[int(ymin):int(ymax)]
        Right_min_Force3 = min(Right_this_Force3)
        Right_max_Force3 = max(Right_this_Force3)
        Right_mean_Force_3 = np.mean(Right_this_Force3)
        Right_standard_deviation_3 = statistics.stdev(Right_this_Force3)

        print("Average Force output of Flex1 was", Right_mean_Force_3)
        print("Standard deviation of the Force output of Flex1 was", Right_standard_deviation_3)
        print("Minimum Force output of Flex1 was", Right_min_Force3)
        print("Maximum Force output of Flex1 was", Right_max_Force3)
        Right_min_Time3 = min(Right_this_Time3)
        Right_max_Time3 = max(Right_this_Time3)
        Right_Time3 = Right_max_Time3 - Right_min_Time3
        print("Time in which the force is selected in Flex1 is ", Right_Time3)


    def Right_on_select_4(ymin, ymax):
        global Right_this_Force4, Right_min_Force4, Right_max_Force4, Right_mean_Force_4, Right_standard_deviation_4, Right_Time4
        Right_this_Force4 = Right_Flex2_Muscle[int(ymin):int(ymax)]
        Right_this_Time4 = Right_Flex2_Time[int(ymin):int(ymax)]
        Right_min_Force4 = min(Right_this_Force4)
        Right_max_Force4 = max(Right_this_Force4)
        Right_mean_Force_4 = np.mean(Right_this_Force4)
        Right_standard_deviation_4 = statistics.stdev(Right_this_Force4)

        print("Average Force output of Flex2 was", Right_mean_Force_4)
        print("Standard deviation of the Force output of Flex2 was", Right_standard_deviation_4)
        print("Minimum Force output of Flex2 was", Right_min_Force4)
        print("Maximum Force output of Flex2 was", Right_max_Force4)
        Right_min_Time4 = min(Right_this_Time4)
        Right_max_Time4 = max(Right_this_Time4)
        Right_Time4 = Right_max_Time4 - Right_min_Time4
        print("Time in which the force is selected in Flex2 is ", Right_Time4)


    Right_span1 = SpanSelector(ax1, Right_on_select_1, 'horizontal', useblit=True, interactive=True,
                               props=dict(alpha=0.5, facecolor='red'))
    Right_span2 = SpanSelector(ax2, Right_on_select_2, 'horizontal', useblit=True, interactive=True,
                               props=dict(alpha=0.5, facecolor='red'))
    Right_span3 = SpanSelector(ax3, Right_on_select_3, 'horizontal', useblit=True, interactive=True,
                               props=dict(alpha=0.5, facecolor='red'))
    Right_span4 = SpanSelector(ax4, Right_on_select_4, 'horizontal', useblit=True, interactive=True,
                               props=dict(alpha=0.5, facecolor='red'))

    plt.subplots_adjust(left=0.1,
                        bottom=0.1,
                        right=0.9,
                        top=0.9,
                        wspace=0.4,
                        hspace=0.4)
    plt.legend()
    plt.show()
    if Surgery_Leg == "Left":
        Column_1 = ["Left S", "Extension 1"]
        for i in range(len(Left_this_Force1)):
            Column_1.append(Left_this_Force1[i])
        Column_2 = ["Left S", "Extension 2"]
        for i in range(len(Left_this_Force2)):
            Column_2.append(Left_this_Force2[i])
        Column_3 = ["Left S", "Flexion 1"]
        for i in range(len(Left_this_Force3)):
            Column_3.append(Left_this_Force3[i])
        Column_4 = ["Left S", "Flexion 2"]
        for i in range(len(Left_this_Force4)):
            Column_4.append(Left_this_Force4[i])
        Column_5 = ["Right", "Extension 1"]
        for i in range(len(Right_this_Force1)):
            Column_5.append(Right_this_Force1[i])
        Column_6 = ["Right", "Extension 2"]
        for i in range(len(Right_this_Force2)):
            Column_6.append(Right_this_Force2[i])
        Column_7 = ["Right", "Flexion 1"]
        for i in range(len(Right_this_Force3)):
            Column_7.append(Right_this_Force3[i])
        Column_8 = ["Right", "Flexion 2"]
        for i in range(len(Right_this_Force4)):
            Column_8.append(Right_this_Force4[i])
        Column_9 = [""]
        Column_10 = ["Left S", "", "Extension 1", "Extension 2", "Flexion 1", "Flexion 2"]
        Column_11 = ["Left S", "Average", Left_mean_Force_1, Left_mean_Force_2, Left_mean_Force_3, Left_mean_Force_4]
        Column_12 = ["Left S", "Sd", Left_standard_deviation_1, Left_standard_deviation_2, Left_standard_deviation_3,
                     Left_standard_deviation_4]
        Column_13 = ["Left S", "Max", Left_max_Force1, Left_max_Force2, Left_max_Force3, Left_max_Force4]
        Column_14 = ["Left S", "Min", Left_min_Force1, Left_min_Force2, Left_min_Force3, Left_min_Force4]
        Column_15 = ["Left S", "Time", Left_Time1, Left_Time2, Left_Time3, Left_Time4]
        Column_16 = [""]
        Column_17 = ["Right", "", "Extension 1", "Extension 2", "Flexion 1", "Flexion 2"]
        Column_18 = ["Right", "Average", Right_mean_Force_1, Right_mean_Force_2, Right_mean_Force_3, Right_mean_Force_4]
        Column_19 = ["Right", "Sd", Right_standard_deviation_1, Right_standard_deviation_2, Right_standard_deviation_3,
                     Right_standard_deviation_4]
        Column_20 = ["Right", "Max", Right_max_Force1, Right_max_Force2, Right_max_Force3, Right_max_Force4]
        Column_21 = ["Right", "Min", Right_min_Force1, Right_min_Force2, Right_min_Force3, Right_min_Force4]
        Column_22 = ["Right", "Time", Right_Time1, Right_Time2, Right_Time3, Right_Time4]
    else:
        Column_1 = ["Left", "Extension 1"]
        for i in range(len(Left_this_Force1)):
            Column_1.append(Left_this_Force1[i])
        Column_2 = ["Left", "Extension 2"]
        for i in range(len(Left_this_Force2)):
            Column_2.append(Left_this_Force2[i])
        Column_3 = ["Left", "Flexion 1"]
        for i in range(len(Left_this_Force3)):
            Column_3.append(Left_this_Force3[i])
        Column_4 = ["Left", "Flexion 2"]
        for i in range(len(Left_this_Force4)):
            Column_4.append(Left_this_Force4[i])
        Column_5 = ["Right S", "Extension 1"]
        for i in range(len(Right_this_Force1)):
            Column_5.append(Right_this_Force1[i])
        Column_6 = ["Right S", "Extension 2"]
        for i in range(len(Right_this_Force2)):
            Column_6.append(Right_this_Force2[i])
        Column_7 = ["Right S", "Flexion 1"]
        for i in range(len(Right_this_Force3)):
            Column_7.append(Right_this_Force3[i])
        Column_8 = ["Right S", "Flexion 2"]
        for i in range(len(Right_this_Force4)):
            Column_8.append(Right_this_Force4[i])
        Column_9 = [""]
        Column_10 = ["Left", "", "Extension 1", "Extension 2", "Flexion 1", "Flexion 2"]
        Column_11 = ["Left", "Average", Left_mean_Force_1, Left_mean_Force_2, Left_mean_Force_3, Left_mean_Force_4]
        Column_12 = ["Left", "Sd", Left_standard_deviation_1, Left_standard_deviation_2, Left_standard_deviation_3,
                     Left_standard_deviation_4]
        Column_13 = ["Left", "Max", Left_max_Force1, Left_max_Force2, Left_max_Force3, Left_max_Force4]
        Column_14 = ["Left", "Min", Left_min_Force1, Left_min_Force2, Left_min_Force3, Left_min_Force4]
        Column_15 = ["Left", "Time", Left_Time1, Left_Time2, Left_Time3, Left_Time4]
        Column_16 = [""]
        Column_17 = ["Right S", "", "Extension 1", "Extension 2", "Flexion 1", "Flexion 2"]
        Column_18 = ["Right S", "Average", Right_mean_Force_1, Right_mean_Force_2, Right_mean_Force_3, Right_mean_Force_4]
        Column_19 = ["Right S", "Sd", Right_standard_deviation_1, Right_standard_deviation_2, Right_standard_deviation_3,
                     Right_standard_deviation_4]
        Column_20 = ["Right S", "Max", Right_max_Force1, Right_max_Force2, Right_max_Force3, Right_max_Force4]
        Column_21 = ["Right S", "Min", Right_min_Force1, Right_min_Force2, Right_min_Force3, Right_min_Force4]
        Column_22 = ["Right S", "Time", Right_Time1, Right_Time2, Right_Time3, Right_Time4]

    result_list = [Column_1, Column_2, Column_3, Column_4,
                   Column_5, Column_6, Column_7, Column_8,
                   Column_9, Column_10, Column_11, Column_12,
                   Column_13, Column_14, Column_15, Column_16,
                   Column_17, Column_18, Column_19, Column_20,
                   Column_21, Column_22]
    Excel_Both_legs_df = pd.DataFrame(result_list)
    Excel_Both_legs_df = Excel_Both_legs_df.T

    if t == "Pre-surgery":
        with pd.ExcelWriter(name) as writer:
            Excel_Both_legs_df.to_excel(writer, sheet_name=t)
    else:
        with pd.ExcelWriter(name, mode="a", engine="openpyxl") as writer:
            Excel_Both_legs_df.to_excel(writer, sheet_name=t)


