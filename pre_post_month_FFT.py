import pandas as pd
import matplotlib.pyplot as plt
import os
from numpy.fft import fft, fftfreq

force_files =  ['subject1','subject3','subject7','subject8',
                'subject9','subject10','subject11','subject12','subject14','subject15','subject16','subject17','subject18','subject19'
                ,'subject20','subject21','subject22','subject23','subject24','subject25']

knee = ['R','L','L','R','R','L','L','R','R','L','R','R','R','R','R','R','L','L','R','L']
# type 0 : parap, type 1 : MV
type = [0,1,0,1,1,1,0,0,0,1,1,0,1,0,1,0,1,1,0,0]
#fs = 75


def FFT(var,fs):
    dt = 1 / fs
    freqs = fftfreq(len(var), dt)
    mask = freqs > 0
    Y = fft(var)
    pSpec = 2 * ((abs(Y) / len(var)) ** 2)

    f = freqs[mask]
    a = pSpec[mask]

    sumA=[0]
    for i in range(1,len(a)):
        sumA.append(a[i]+sumA[i-1])

    prec90= []
    prec95 = []
    prec99 = []
    percA = [(sumA[i] / sumA[-1])*100 for i in range(len(sumA))]
    for p in percA:
        prec90.append(abs(p - 90))
        prec95.append(abs(p - 95))
        prec99.append(abs(p - 99))
    for i in range(len(percA)):
        if prec90[i]==min(prec90):
            index90 = i
        if prec95[i]==min(prec95):
            index95 = i
        if prec99[i]==min(prec99):
            index99 = i



    return f[index90],f[index95],f[index99]



variables = []
for p,l in zip(force_files,knee):
    pre = pd.read_excel('data\{p}CoP.xlsx'.format(p=p),header=[1,2,3],sheet_name='Pre-surgery')
    post = pd.read_excel('data\{p}CoP.xlsx'.format( p=p), header=[1, 2, 3],sheet_name='Post-surgery')
    w2 = pd.read_excel('data\{p}CoP.xlsx'.format(p=p), header=[1, 2, 3], sheet_name='2 weeks')
    month = pd.read_excel('data\{p}CoP.xlsx'.format(p=p), header=[1, 2, 3], sheet_name='4 weeks')

    fs_pre = pre['Fs'].columns[0][0]
    fs_post = post['Fs'].columns[0][0]
    fs_w2 = w2['Fs'].columns[0][0]
    fs_month = month['Fs'].columns[0][0]

    print(fs_pre)
    print(fs_post)
    print(fs_w2)
    print(fs_month)

    print()

    if l=='L':
        left = 'Left S'
        right = 'Right'
        leg = 'Left'
    else:
        left = 'Left'
        right = 'Right S'
        leg = 'Right'

    if leg == 'Left':
        Surgery_pre_x = (pre['CoP'][left]['x (mm)'])
        Healthy_pre_x = (pre['CoP'][right]['x (mm)'])
        Surgery_post_x = (post['CoP'][left]['x (mm)'])
        Healthy_post_x = (post['CoP'][right]['x (mm)'])
        Surgery_2w_x = (w2['CoP'][left]['x (mm)'])
        Healthy_2w_x = (w2['CoP'][right]['x (mm)'])
        Surgery_month_x = (month['CoP'][left]['x (mm)'])
        Healthy_month_x = (month['CoP'][right]['x (mm)'])

        Surgery_pre_y = (pre['CoP'][left]['y (mm)'])
        Healthy_pre_y = (pre['CoP'][right]['y (mm)'])
        Surgery_post_y = (post['CoP'][left]['y (mm)'])
        Healthy_post_y = (post['CoP'][right]['y (mm)'])
        Surgery_2w_y = (w2['CoP'][left]['y (mm)'])
        Healthy_2w_y = (w2['CoP'][right]['y (mm)'])
        Surgery_month_y = (month['CoP'][left]['y (mm)'])
        Healthy_month_y = (month['CoP'][right]['y (mm)'])

    else:
        Surgery_pre_x = (pre['CoP'][right]['x (mm)'])
        Healthy_pre_x = (pre['CoP'][left]['x (mm)'])
        Surgery_post_x = (post['CoP'][right]['x (mm)'])
        Healthy_post_x = (post['CoP'][left]['x (mm)'])
        Surgery_2w_x = (w2['CoP'][right]['x (mm)'])
        Healthy_2w_x = (w2['CoP'][left]['x (mm)'])
        Surgery_month_x = (month['CoP'][right]['x (mm)'])
        Healthy_month_x = (month['CoP'][left]['x (mm)'])

        Surgery_pre_y = (pre['CoP'][left]['y (mm)'])
        Healthy_pre_y = (pre['CoP'][right]['y (mm)'])
        Surgery_post_y = (post['CoP'][left]['y (mm)'])
        Healthy_post_y = (post['CoP'][right]['y (mm)'])
        Surgery_2w_y = (w2['CoP'][right]['y (mm)'])
        Healthy_2w_y = (w2['CoP'][left]['y (mm)'])
        Surgery_month_y = (month['CoP'][left]['y (mm)'])
        Healthy_month_y = (month['CoP'][right]['y (mm)'])

    Both_pre_x = (pre['CoP']['Both']['x (mm)'])
    Both_post_x = (post['CoP']['Both']['x (mm)'])
    Both_2w_x = (w2['CoP']['Both']['x (mm)'])
    Both_month_x = (month['CoP']['Both']['x (mm)'])

    Both_pre_y = (pre['CoP']['Both']['y (mm)'])
    Both_post_y = (post['CoP']['Both']['y (mm)'])
    Both_2w_y = (w2['CoP']['Both']['y (mm)'])
    Both_month_y = (month['CoP']['Both']['y (mm)'])

    vars = [Surgery_pre_x,Healthy_pre_x,Surgery_pre_y,Healthy_pre_y,Both_pre_x,Both_pre_y,
            Surgery_post_x,Healthy_post_x,Surgery_post_y,Healthy_post_y,Both_post_x,Both_post_y,
            Surgery_2w_x, Healthy_2w_x, Surgery_2w_y, Healthy_2w_y, Both_2w_x, Both_2w_y,
            Surgery_month_x,Healthy_month_x,Surgery_month_y,Healthy_month_y,Both_month_x,Both_month_y]
    var_names = ['Surgery_pre_x','Healthy_pre_x','Surgery_pre_y','Healthy_pre_y','Both_pre_x','Both_pre_y',
                 'Surgery_post_x','Healthy_post_x','Surgery_post_y','Healthy_post_y','Both_post_x','Both_post_y',
                 'Surgery_2w_x', 'Healthy_2w_x', 'Surgery_2w_y', 'Healthy_2w_y', 'Both_2w_x', 'Both_2w_y',
                 'Surgery_month_x','Healthy_month_x','Surgery_month_y','Healthy_month_y','Both_month_x','Both_month_y']
    fvars = []
    fvar_names = []
    for v,n in zip(vars,var_names):
        if 'pre' in n:
            fs = fs_pre
        elif 'post' in n:
            fs = fs_pre
        elif '2w' in n:
            fs = fs_pre
        elif 'month' in n:
            fs = fs_pre

        f90, f95, f99 = FFT(v, fs)
        fvars.append(f90)
        fvars.append(f95)
        fvars.append(f99)
        fvar_names.append(n + '_f90')
        fvar_names.append(n + '_f95')
        fvar_names.append(n + '_f99')

    variables.append(fvars)
results = pd.DataFrame(variables)
results.columns = fvar_names
print(results)

# writer = pd.ExcelWriter('ResFFT_all.xlsx')
# results.to_excel(writer,sheet_name='Freq')
#
# writer.close()