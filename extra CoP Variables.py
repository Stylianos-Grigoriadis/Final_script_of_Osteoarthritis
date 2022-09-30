import pandas as pd
import matplotlib.pyplot as plt
import os
from numpy.fft import fft, fftfreq

fs = 75
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
    plt.plot(f,a)
    plt.axvline(x=f[index90])
    plt.axvline(x=f[index95])
    plt.axvline(x=f[index99])
    plt.show()


    return f[index90],f[index95],f[index99]










mean_vel_pre = []
mean_vel_post = []
for p in range(1,14):
    for file in os.listdir(r"C:\Users\Βασίλης\OneDrive\Υπολογιστής\βασίλης\τεφαα\Biomechanics\Kinvent\Osteoarthitis\subject{p}\pre".format(p=p)):
        if file.startswith("sta"):
            pre = pd.read_csv(r'C:\Users\Βασίλης\OneDrive\Υπολογιστής\βασίλης\τεφαα\Biomechanics\Kinvent\Osteoarthitis\subject{p}\pre\{f}'.format(p=p,f=file),nrows=5,names=['Name','values'])
            mean_vel_pre.append(pre['values'][4])

    for file in os.listdir(r"C:\Users\Βασίλης\OneDrive\Υπολογιστής\βασίλης\τεφαα\Biomechanics\Kinvent\Osteoarthitis\subject{p}\post".format(p=p)):
        if file.startswith("sta"):
            post = pd.read_csv(r'C:\Users\Βασίλης\OneDrive\Υπολογιστής\βασίλης\τεφαα\Biomechanics\Kinvent\Osteoarthitis\subject{p}\post\{f}'.format(p=p, f=file),nrows=5,names=['Name','values'])
            mean_vel_post.append(post['values'][4])


mean_vel_pre[2] = 3.9

# plt.plot(mean_vel_post,label='post')
# plt.title('mean velocity')
# plt.plot(mean_vel_pre,label='pre    ')
# plt.legend()
# plt.show()

f90_l = []
f95_l = []
f99_l = []
variables = []
path = r'C:\Users\Βασίλης\OneDrive\Υπολογιστής\βασίλης\τεφαα\Biomechanics\Kinvent\Osteoarthitis\Scripts\data'
participants = pd.read_excel(r'C:\Users\Βασίλης\OneDrive\Υπολογιστής\βασίλης\τεφαα\Biomechanics\Kinvent\Osteoarthitis\Participants.xlsx')
for p,l in zip(range(1,14),participants['Χειρουργημένο γόνατο']):
    print(l)
    pre = pd.read_excel('{path}\subject{p}CoP.xlsx'.format(path=path,p=p),header=[1,2,3],sheet_name='Pre-surgery')
    post = pd.read_excel('{path}\subject{p}CoP.xlsx'.format(path=path, p=p), header=[1, 2, 3],sheet_name='Post-surgery')



    if l=='Αριστερό':
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
        Surgery_pre_y = (pre['CoP'][left]['y (mm)'])
        Healthy_pre_y = (pre['CoP'][right]['y (mm)'])
        Surgery_post_y = (post['CoP'][left]['y (mm)'])
        Healthy_post_y = (post['CoP'][right]['y (mm)'])
    else:
        Surgery_pre_x = (pre['CoP'][right]['x (mm)'])
        Healthy_pre_x = (pre['CoP'][left]['x (mm)'])
        Surgery_post_x = (post['CoP'][right]['x (mm)'])
        Healthy_post_x = (post['CoP'][left]['x (mm)'])
        Surgery_pre_y = (pre['CoP'][left]['y (mm)'])
        Healthy_pre_y = (pre['CoP'][right]['y (mm)'])
        Surgery_post_y = (post['CoP'][left]['y (mm)'])
        Healthy_post_y = (post['CoP'][right]['y (mm)'])

    Both_pre_x = (pre['CoP']['Both']['x (mm)'])
    Both_post_x = (post['CoP']['Both']['x (mm)'])

    Both_pre_y = (pre['CoP']['Both']['y (mm)'])
    Both_post_y = (post['CoP']['Both']['y (mm)'])




    vars = [Surgery_pre_x,Healthy_pre_x,Surgery_pre_y,Healthy_pre_y,Both_pre_x,Both_pre_y,Surgery_post_x,Healthy_post_x,Surgery_post_y,Healthy_post_y,Both_post_x,Both_post_y]
    var_names = ['Surgery_pre_x','Healthy_pre_x','Surgery_pre_y','Healthy_pre_y','Both_pre_x','Both_pre_y','Surgery_post_x','Healthy_post_x','Surgery_post_y','Healthy_post_y','Both_post_x','Both_post_y']
    fvars = []
    fvar_names = []
    for v,n in zip(vars,var_names):

        f90, f95, f99 = FFT(v, fs)
        fvars.append(f90)
        fvars.append(f95)
        fvars.append(f99)
        fvar_names.append(n + '_f90')
        fvar_names.append(n + '_f95')
        fvar_names.append(n + '_f99')

    variables.append(fvars)

#writer = pd.ExcelWriter('FFT.xlsx')
results = pd.DataFrame(variables)
results.columns = fvar_names

#results_vel = pd.DataFrame({'mean_vel_pre':mean_vel_pre,'mean_vel_post':mean_vel_post})
#results_vel.to_excel(writer,sheet_name='Vel')
# results.to_excel(writer,sheet_name='Freq')
# writer.save()
# writer.close()


#print(res_vars)




