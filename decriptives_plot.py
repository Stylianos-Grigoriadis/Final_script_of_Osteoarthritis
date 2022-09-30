import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

files = ['subject1','subject2','subject3','subject6','subject7','subject8']
surgery = ['Right','Right','Left','Right','Left','Right']
surgery_type = ['Parapatellar','Parapatellar','Midvastus','Parapatellar','Parapatellar','Midvastus']
sheet_names = ["Pre-surgery","Post-surgery","2 weeks","4 weeks","3 months"]


data_healthy_knee = {'Pre-surgery':[],
                     'Post-surgery':[],
                     '2 weeks':[],
                     '4 weeks':[]}
data_surgery_knee = {'Pre-surgery':[],
                     'Post-surgery':[],
                     '2 weeks':[],
                     '4 weeks':[]}
for file,knee,typ in zip(files,surgery,surgery_type):
    dataS = []
    data = []
    sd = []
    sds = []
    plt.rcParams.update({'font.size':18})
    fig, axs = plt.subplots(2, 3)
    for n,sn in enumerate(sheet_names):
        df = pd.read_excel('{f}.xlsx'.format(f=file),sheet_name=sn,skiprows=[0],header=[0,1])
        print(file,sn)
        if knee=='Right':
            left = ''
            right = ' S'
            data.append(df['Left' + left]['Average'][0:4])
            dataS.append(df['Right' + right]['Average'][0:4])
            sds.append(df['Right' + right]['Sd'][0:4])
            sd.append(df['Left' + left]['Sd'][0:4])
        else:
            left = ' S'
            right = ''
            data.append(df['Right' + right]['Average'][0:4])
            dataS.append(df['Left' + left]['Average'][0:4])
            sd.append(df['Right' + right]['Sd'][0:4])
            sds.append(df['Left' + left]['Sd'][0:4])

        print(data[0])
        print(type(data))
        print(len(data))

        X = np.arange(4)
        if sn == "Pre-surgery":
                i, j = 0, 0
        elif sn == "Post-surgery":
                i, j = 0, 1
        elif sn == "2 weeks":
                i, j = 0, 2
        elif sn == "4 weeks":
            i, j = 1, 0
        else:
            i, j = 1, 1
        try:
            axs[i,j].set_ylim([0,30.0])
            #axs[i,j].set_title(file + ' ' + sn)
            fig.suptitle(file + ' ' + typ)
            axs[i, j].set_title(sn)
            axs[i,j].bar(X + 0.00, data[n],yerr=sd[n], width=0.25, label='Healthy', capsize=2)
            axs[i,j].bar(X + 0.25, dataS[n],yerr=sds[n], width=0.25, label='Surgery', capsize=2)
            axs[i,j].legend()
            axs[i,j].set_xticks([0,1,2,3],['Ext1','Ext2','Flex1','Flex2'])
            axs[i, j].set_ylabel('Force (Kg)')
        except:
            axs[i,j].annotate(text='not yet meassured',xy=(0.1,10))
        #axs[2,2].annotate(text='@Biomecanics Lab Auth',xy=(0.1,0.5))
    plt.show()



