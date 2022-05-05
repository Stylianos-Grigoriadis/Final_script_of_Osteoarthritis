import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

files = ['subject1','subject2','subject3','subject6']
surgery = ['Right','Right','Left','Right']
sheet_names = ["Pre-surgery","Post-surgery","2 weeks","4 weeks"]

for file,knee in zip(files,surgery):
    for sn in sheet_names:
        df = pd.read_excel('{f}.xlsx'.format(f=file),sheet_name=sn,skiprows=[0],header=[0,1])

        if knee=='Right':
            left = ''
            right = ' S'
        else:
            left = ' S'
            right = ''
        dataL = df['Left' + left]['Average'][0:4]
        sdL = df['Left' + left]['Sd'][0:4]
        dataR = df['Right' + right]['Average'][0:4]
        sdR = df['Right' + right]['Sd'][0:4]

        data = [list(dataL), list(dataR)]
        print(data)

        X = np.arange(4)
        # fig = plt.figure()
        # ax = fig.add_axes([0, 0, 1, 1])
        plt.title(file + ' ' + sn)
        plt.bar(X + 0.00, data[0], width=0.25, label='Left')
        plt.bar(X + 0.25, data[1], width=0.25, label='Right S')
        plt.legend()
        plt.show()



