import pandas as pd
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import SpanSelector
import statistics


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