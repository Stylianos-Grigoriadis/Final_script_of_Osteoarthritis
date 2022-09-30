import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

files = ['subject1CoP','subject2CoP','subject3CoP','subject6CoP','subject7CoP','subject8CoP']
surgery = ['Right','Right','Left','Right','Left','Right']
surgery_type = ['Parapatellar','Parapatellar','Midvastus','Parapatellar','Parapatellar','Midvastus']
sheet_names = ["Pre-surgery","Post-surgery","2 weeks","4 weeks","3 months"]

# for file,knee in zip(files,surgery):
#     for sn in sheet_names:
#         df = pd.read_excel('{f}.xlsx'.format(f=file),sheet_name=sn,skiprows=[0],header=[0,1,2])
#         print(df)
#         plt.plot(df['CoP']['Both']['x (mm)'],df['CoP']['Both']['y (mm)'],label=sn)
#     plt.legend()
#     plt.show()



for file,knee,typ in zip(files,surgery,surgery_type):
    data = []
    dataS = []
    sd = []
    sds = []
    weight = []
    CopX = []
    CopY = []
    #plt.rcParams.update({'font.size': 18})
    #fig, axs = plt.subplots(2, 2)
    for sn in sheet_names:
        df = pd.read_excel('{f}.xlsx'.format(f=file),sheet_name=sn,skiprows=[0],header=[0])
        # dfc = pd.read_excel('{f}.xlsx'.format(f=file), sheet_name=sn, skiprows=[0], header=[0, 1, 2])['CoP']
        # copx = [i - dfc['Both']['x (mm)'].mean() for i in dfc['Both']['x (mm)']]
        # copy = [i - dfc['Both']['y (mm)'].mean() for i in dfc['Both']['y (mm)']]
        # CopX.append(copx)
        # CopY.append(copy)
        try:
            weight.append(df['Average Force (kg)'][2])
            if knee == 'Right':
                data.append((df['Average Force (kg)'][0]))
                dataS.append((df['Average Force (kg)'][1]))
                sds.append(df['Stdev Force (kg)'][1])
                sd.append(df['Stdev Force (kg)'][0])
            else:
                dataS.append((df['Average Force (kg)'][0]))
                data.append((df['Average Force (kg)'][1]))
                sds.append(df['Stdev Force (kg)'][0])
                sd.append(df['Stdev Force (kg)'][1])
        except:
            weight.append(1)
            if knee == 'Right':
                data.append(0)
                dataS.append(0)
                sds.append(0)
                sd.append(0)
            else:
                dataS.append(0)
                data.append(0)
                sds.append(0)
                sd.append(0)



    #fig,axs = plt.subplots(1,2)
    print(file,sn)

    data = [(i / w )*100 for i,w in zip(data,weight)]
    dataS = [(i / w )*100 for i,w in zip(dataS,weight)]
    sd = [(i / w )*100 for i,w in zip(sd,weight)]
    sds = [(i / w )*100 for i,w in zip(sds,weight)]
    X = np.arange(5)
    plt.rcParams.update({'font.size': 24})
    plt.title(file[:-3] + ' ' + typ)
    plt.bar(X + 0, data, width=0.25, yerr=sd, label='Healthy', capsize=8)
    plt.bar(X + 0.25, dataS, width=0.25, yerr=sds, label='Surgery', capsize=8)
    plt.xticks([0,1,2,3,4],sheet_names)
    plt.ylabel('Weight Distribution (%)')
    plt.legend()
    plt.show()

    # for x,y,n in zip(CopX,CopY,sheet_names):
    #     plt.plot(x,y,label=n)
    # plt.legend()
    # plt.show()