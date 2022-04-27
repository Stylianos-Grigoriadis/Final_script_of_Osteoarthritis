import pandas as pd
from tkinter import filedialog
import matplotlib.pyplot as plt
import tkinter as tk
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
    sens=[]
    muscle=[]
    for i in range(len(df)):
        if df['Time'][i]=='Device: Sens':
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

        for t,d in zip(df['Time'][sens_i+2:], df['Data'][sens_i+2:]):
            if isinstance(t,str):
                break
            else:
                sens_temp.append(t)
                sens_temp_d.append(d)
        sens_data.append(sens_temp_d)
        sens_time.append(sens_temp)

    # For muscle
    muscle_data=[]
    muscle_time=[]

    for muscle_i in muscle:
        muscle_temp=[]
        muscle_temp_d = []

        for t,d in zip(df['Time'][muscle_i+2:],df['Data'][muscle_i+2:]):
            if isinstance(t,str):
                break
            else:
                muscle_temp.append(t)
                muscle_temp_d.append(d)
        muscle_data.append(muscle_temp_d)
        muscle_time.append(muscle_temp)

    # create 4 (one for each repetition) lists with 3 lists each
    ext1=[sens_time[0],sens_data[0],muscle_data[0]]
    ext2=[sens_time[1],sens_data[1],muscle_data[1]]
    flex1=[sens_time[2],sens_data[2],muscle_data[2]]
    flex2=[sens_time[3],sens_data[3],muscle_data[3]]

    # merge the above lists in one 12-item list (one item for each time-series)
    for i in ext2:
        ext1.append(i)
    for i in flex1:
        ext1.append(i)
    for i in flex2:
        ext1.append(i)

    # Transform the list to Dataframe, Transpose it and set column name

    final=pd.DataFrame(ext1)
    final=final.T
    final.columns=['Ext1 Time','Ext1 Sens','Ext1 Muscle',
                   'Ext2 Time','Ext2 Sens','Ext2 Muscle',
                   'Flex1 Time','Flex1 Sens','Flex1 Muscle',
                   'Flex2 Time','Flex2 Sens','Flex2 Muscle']
    #print(final)

    #write the Dataframe to .xlsx file
    '''writer=pd.ExcelWriter('new.xlsx')
    final.to_excel(writer)
    writer.save()
    writer.close()'''
    return final

df_force = filedialog.askopenfilename(initialdir="C:\\",
                                      # initioaldir = "Which directory will the program open",
                                       title="Select CMV File",
                                      # title = "Title",
                                       filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
df=pd.read_csv(df_force,header=None,delimiter=',',decimal='.',names=['Time','Data'])

# df=pd.read_csv('C:\Python_projects\Final_script_of_Osteoarthritis\muscle and sens_Παπαδόπουλος  Ιωάννης   Right.csv',header=None,delimiter=',',decimal='.',names=['Time','Data'])


print(df)
newdf = csv_transform(df)
print(newdf)
Columns_names = newdf.columns
print(Columns_names)
fig = plt.figure(figsize=(8, 12))
fig.suptitle('Select the area in which the Force will be processed ', fontsize=16)

ax1 = fig.add_subplot(411)
ax1.set_title('Extension 1')
ax1.plot(newdf['Ext1 Sens'], label='Sens')
ax1.plot(newdf['Ext1 Muscle'], label='Muscle')

ax2 = fig.add_subplot(412)
ax2.set_title('Extension 2')
ax2.plot(newdf['Ext2 Sens'], label='Sens')
ax2.plot(newdf['Ext2 Muscle'], label='Muscle')

ax3 = fig.add_subplot(413)
ax3.set_title('Flexion 1')
ax3.plot(newdf['Flex1 Sens'], label='Sens')
ax3.plot(newdf['Flex1 Muscle'], label='Muscle')

ax4 = fig.add_subplot(414)
ax4.set_title('flexion 2')
ax4.plot(newdf['Flex2 Sens'], label='Sens')
ax4.plot(newdf['Flex2 Muscle'], label='Muscle')


#lists to use in the on_select def
Ext1_Time = newdf['Ext1 Time'].tolist()
Ext1_Muscle = newdf['Ext1 Muscle'].tolist()
Ext2_Time = newdf['Ext2 Time'].tolist()
Ext2_Muscle = newdf['Ext2 Muscle'].tolist()
Flex1_Time = newdf['Flex1 Time'].tolist()
Flex1_Muscle = newdf['Flex1 Muscle'].tolist()
Flex2_Time = newdf['Flex2 Time'].tolist()
Flex2_Muscle = newdf['Flex2 Muscle'].tolist()

def on_select_1(ymin,ymax):
    this_Force1 = Ext1_Muscle[int(ymin):int(ymax)]
    print(type(this_Force1))
    this_Time1 = Ext1_Time[int(ymin):int(ymax)]
    min_Force1 = min(this_Force1)
    max_Force1 = max(this_Force1)
    mean_Force_1 = mean(this_Force1)
    standard_deviation_1 = statistics.stdev(this_Force1)

    print("Average Force output of Ext1 was", mean_Force_1)
    print("Standard deviation of the Force output of Ext1 was", standard_deviation_1)
    print("Minimum Force output of Ext1 was", min_Force1)
    print("Maximum Force output of Ext1 was", max_Force1)
    min_Time1 = min(this_Time1)
    max_Time1 = max(this_Time1)
    Time1 = max_Time1 - min_Time1
    print("Time in which the force is selected in Ext1 is ", Time1)

def on_select_2(ymin,ymax):
    this_Force2 = Ext2_Muscle[int(ymin):int(ymax)]
    this_Time2 = Ext2_Time[int(ymin):int(ymax)]
    min_Force2 = min(this_Force2)
    max_Force2 = max(this_Force2)
    mean_Force_2 = mean(this_Force2)
    standard_deviation_2 = statistics.stdev(this_Force2)

    print("Average Force output of Ext2 was", mean_Force_2)
    print("Standard deviation of the Force output of Ext2 was", standard_deviation_2)
    print("Minimum Force output of Ext2 was", min_Force2)
    print("Maximum Force output of Ext2 was", max_Force2)
    min_Time2 = min(this_Time2)
    max_Time2 = max(this_Time2)
    Time2 = max_Time2 - min_Time2
    print("Time in which the force is selected in Ext2 is ", Time2)

def on_select_3(ymin,ymax):
    this_Force3 = Flex1_Muscle[int(ymin):int(ymax)]
    this_Time3 = Flex1_Time[int(ymin):int(ymax)]
    min_Force3 = min(this_Force3)
    max_Force3 = max(this_Force3)
    mean_Force_3 = mean(this_Force3)
    standard_deviation_3 = statistics.stdev(this_Force3)

    print("Average Force output of Flex1 was", mean_Force_3)
    print("Standard deviation of the Force output of Flex1 was", standard_deviation_3)
    print("Minimum Force output of Flex1 was", min_Force3)
    print("Maximum Force output of Flex1 was", max_Force3)
    min_Time3 = min(this_Time3)
    max_Time3 = max(this_Time3)
    Time3 = max_Time3 - min_Time3
    print("Time in which the force is selected in Flex1 is ", Time3)

def on_select_4(ymin,ymax):
    this_Force4 = Flex2_Muscle[int(ymin):int(ymax)]
    this_Time4 = Flex2_Time[int(ymin):int(ymax)]
    min_Force4 = min(this_Force4)
    max_Force4 = max(this_Force4)
    mean_Force_4 = mean(this_Force4)
    standard_deviation_4 = statistics.stdev(this_Force4)

    print("Average Force output of Flex2 was", mean_Force_4)
    print("Standard deviation of the Force output of Flex2 was", standard_deviation_4)
    print("Minimum Force output of Flex2 was", min_Force4)
    print("Maximum Force output of Flex2 was", max_Force4)
    min_Time4 = min(this_Time4)
    max_Time4 = max(this_Time4)
    Time4 = max_Time4 - min_Time4
    print("Time in which the force is selected in Flex2 is ", Time4)

span1 = SpanSelector(ax1, on_select_1,'horizontal',useblit=True,interactive = True, props=dict(alpha=0.5, facecolor='red'))
span2 = SpanSelector(ax2, on_select_2,'horizontal',useblit=True,interactive = True, props=dict(alpha=0.5, facecolor='red'))
span3 = SpanSelector(ax3, on_select_3,'horizontal',useblit=True,interactive = True, props=dict(alpha=0.5, facecolor='red'))
span4 = SpanSelector(ax4, on_select_4,'horizontal',useblit=True,interactive = True, props=dict(alpha=0.5, facecolor='red'))




plt.legend()
plt.show()
