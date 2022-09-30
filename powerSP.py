import pandas as pd
import matplotlib.pyplot as plt
import os
from numpy.fft import fft, fftfreq

fs = 75
def FFT(var,fs,varname):
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
    plt.title(varname)
    plt.plot(f,a)
    plt.axvline(x=f[index90])
    plt.axvline(x=f[index95])
    plt.axvline(x=f[index99])
    #plt.show()


    return f[index90],f[index95],f[index99]



pre = pd.read_excel(r'C:\Users\Βασίλης\OneDrive\Υπολογιστής\βασίλης\τεφαα\Biomechanics\Kinvent\Osteoarthitis\Scripts\data\subject7CoP.xlsx',header=[1,2,3],sheet_name='Pre-surgery')



Surgery_pre_x = (pre['CoP']['Left S']['x (mm)'][30:])
Healthy_pre_x = (pre['CoP']['Right']['x (mm)'][30:])

Surgery_pre_y = (pre['CoP']['Left S']['y (mm)'][30:])
Healthy_pre_y = (pre['CoP']['Right']['y (mm)'][30:])



Both_pre_x = (pre['CoP']['Both']['x (mm)'][30:])


Both_pre_y = (pre['CoP']['Both']['y (mm)'][30:])


vars = [Surgery_pre_x, Healthy_pre_x, Surgery_pre_y, Healthy_pre_y, Both_pre_x, Both_pre_y]
var_names = ['Surgery_pre_x', 'Healthy_pre_x', 'Surgery_pre_y', 'Healthy_pre_y', 'Both_pre_x', 'Both_pre_y',
             'Surgery_post_x', 'Healthy_post_x', 'Surgery_post_y', 'Healthy_post_y', 'Both_post_x', 'Both_post_y']
fvars = []
fvar_names = []
for v, n in zip(vars, var_names):
    f90, f95, f99 = FFT(v, fs,n)
    print(n)
    print(f95)