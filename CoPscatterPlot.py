import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

files = ['subject1CoP','subject2CoP','subject3CoP','subject6CoP','subject7CoP','subject8CoP']
surgery = ['Right','Right','Left','Right','Left','Right']
surgery_type = ['Parapatellar','Parapatellar','Midvastus','Parapatellar','Parapatellar','Midvastus']
sheet_names = ["Pre-surgery","Post-surgery","2 weeks","4 weeks","3 months"]

for file,knee,typ in zip(files,surgery,surgery_type):
    # CopX = []
    # CopY = []
    # CopXR = []
    # CopYR = []
    # CopXL = []
    # CopYL = []
    plt.rcParams.update({'font.size': 24})
    fig, axs = plt.subplots(2, 3)
    for sn in sheet_names:
        dfc = pd.read_excel('{f}.xlsx'.format(f=file), sheet_name=sn, skiprows=[0], header=[0, 1, 2])['CoP']
        if knee == 'Right':
            CopX = (dfc['Both']['x (mm)'])
            CopY = (dfc['Both']['y (mm)'])
            CopXR=(dfc['Right S']['x (mm)'])
            CopYR=(dfc['Right S']['y (mm)'])
            CopXL=(dfc['Left']['x (mm)'])
            CopYL=(dfc['Left']['y (mm)'])
        else:
            CopX=(dfc['Both']['x (mm)'])
            CopY=(dfc['Both']['y (mm)'])
            CopXR=(dfc['Right']['x (mm)'])
            CopYR=(dfc['Right']['y (mm)'])
            CopXL=(dfc['Left S']['x (mm)'])
            CopYL=(dfc['Left S']['y (mm)'])
        # CopX = [i - CopX.mean() for i in CopX]
        # CopY = [i - CopY.mean() for i in CopY]
        # CopXR = [i - CopXR.mean() for i in CopXR]
        # CopYR = [i - CopYR.mean() for i in CopYR]
        # CopXL = [i - CopXL.mean() for i in CopXL]
        # CopYL = [i - CopYL.mean() for i in CopYL]
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

        if j == 0:
            axs[i, j].set_ylabel('Displacement (mm)')
        # if i ==1:
        #     axs[i, j].set_xlabel('Displacement (mm)')
        print((CopX))
        if ((i==1 and j ==1) or (i==0 and j ==2) or (i==1 and j ==0)) and False:

            axs[i, j].annotate(text='not yet meassured', xy=(0.1,0.5))

        else:
            if knee == 'Right':
                fig.suptitle(file[:-3] + ' ' + typ)
                axs[i, j].set_ylim([-130, 90])
                axs[i, j].set_xlim([-130, 90])
                axs[i, j].set_title(sn)
                axs[i, j].plot(CopX, CopY, label='Both',lw = 4)
                axs[i, j].plot(CopXR, CopYR, label='Surgery',lw = 4)
                axs[i, j].plot(CopXL, CopYL, label='Healthy',lw = 4)
                axs[i, j].legend()
            else:
                fig.suptitle(file[:-3] + ' ' + typ)
                axs[i, j].set_ylim([-130, 90])
                axs[i, j].set_xlim([-130, 90])
                axs[i, j].set_title(sn)
                axs[i, j].plot(CopX, CopY, label='Both', lw=4)
                axs[i, j].plot(CopXR, CopYR, label='Healthy', lw=4)
                axs[i, j].plot(CopXL, CopYL, label='Surgery', lw=4)
                axs[i, j].legend()


    plt.show()