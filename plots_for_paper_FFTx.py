import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('FFT.xlsx')
print(df)
x = df[df['Feature']=='x95']
print(x)

x_MV = x[x['Surgerytype']==1]
x_Parap = x[x['Surgerytype']==0]
print(x_Parap)
print(x_MV)

x_MV_Healthy_pre = x_MV['Healthy_pre'].mean()
x_MV_Surgery_pre = x_MV['Surgery_pre'].mean()
x_MV_Both_pre = x_MV['Both_pre'].mean()

x_MV_Healthy_post = x_MV['Healthy_post'].mean()
x_MV_Surgery_post = x_MV['Surgery_post'].mean()
x_MV_Both_post= x_MV['Both_post'].mean()

x_Parap_Healthy_pre = x_Parap['Healthy_pre'].mean()
x_Parap_Surgery_pre = x_Parap['Surgery_pre'].mean()
x_Parap_Both_pre = x_Parap['Both_pre'].mean()

x_Parap_Healthy_post = x_Parap['Healthy_post'].mean()
x_Parap_Surgery_post = x_Parap['Surgery_post'].mean()
x_Parap_Both_post= x_Parap['Both_post'].mean()

# plt.rcParams.update({'font.size':16})
# plt.rcParams['errorbar.capsize']=10
# plt.title('Power Spectum at ML Axis')
# plt.ylabel('Freq at 95% of Power (Hz)')

# plt.plot([x_MV_Healthy_pre,x_MV_Healthy_post],label='MV',color='blue',lw=2)
# plt.plot([x_Parap_Healthy_pre,x_Parap_Healthy_post],label='Parap',color='orange',lw=2)
#
# plt.plot([2,3],[x_MV_Surgery_pre,x_MV_Surgery_post],color='blue',lw=2)
# plt.plot([2,3],[x_Parap_Surgery_pre,x_Parap_Surgery_post],color='orange',lw=2)
#
# plt.plot([4,5],[x_MV_Both_pre,x_MV_Both_post],color='blue',lw=2)
# plt.plot([4,5],[x_Parap_Both_pre,x_Parap_Both_post],color='orange',lw=2)
#
# plt.errorbar(x=0,y=x_MV_Healthy_pre,yerr=x_MV['Healthy_pre'].std(),ecolor='blue',lw=3)
# plt.errorbar(x=1,y=x_MV_Healthy_post,yerr=x_MV['Healthy_post'].std(),ecolor='blue',lw=3)
#
# plt.errorbar(x=0,y=x_Parap_Healthy_pre,yerr=x_Parap['Healthy_pre'].std(),ecolor='orange',lw=3)
# plt.errorbar(x=1,y=x_Parap_Healthy_post,yerr=x_Parap['Healthy_post'].std(),ecolor='orange',lw=3)
#
# plt.errorbar(x=2,y=x_MV_Surgery_pre,yerr=x_MV['Surgery_pre'].std(),ecolor='blue',lw=3)
# plt.errorbar(x=3,y=x_MV_Surgery_post,yerr=x_MV['Surgery_post'].std(),ecolor='blue',lw=3)
#
# plt.errorbar(x=2,y=x_Parap_Surgery_pre,yerr=x_Parap['Surgery_pre'].std(),ecolor='orange',lw=3)
# plt.errorbar(x=3,y=x_Parap_Surgery_post,yerr=x_Parap['Surgery_post'].std(),ecolor='orange',lw=3)
#
# plt.errorbar(x=4,y=x_MV_Both_pre,yerr=x_MV['Both_pre'].std(),ecolor='blue',lw=3)
# plt.errorbar(x=5,y=x_MV_Both_post,yerr=x_MV['Both_post'].std(),ecolor='blue',lw=3)
#
# plt.errorbar(x=4,y=x_Parap_Both_pre,yerr=x_Parap['Both_pre'].std(),ecolor='orange',lw=3)
# plt.errorbar(x=5,y=x_Parap_Both_post,yerr=x_Parap['Both_post'].std(),ecolor='orange',lw=3)
import matplotlib.patches as mpatches
from cycler import cycler
from matplotlib import rcParams

rcParams['axes.prop_cycle'] = cycler(color='k')
plt.rcParams.update({"font.size": 16})
pre_ticks = [1]
post_ticks = [2]


Pre_plot = plt.violinplot(dataset=[x_MV['Both_pre']], positions=pre_ticks, showextrema=True, showmeans=True)
Post_plot = plt.violinplot(dataset=[x_MV['Both_post']], positions=post_ticks, showextrema=True, showmeans=True)

plt.xticks(ticks=[1,2], labels=['pre','post'])
red_patch = mpatches.Patch(color='red',alpha=0.6)
blue_patch = mpatches.Patch(color='blue',alpha=0.6)

plt.title('Power Spectum at ML Axis')
plt.ylabel('Freq at 95% of Power (Hz)')

for y in Pre_plot['bodies']:
    y.set_facecolor('blue')
    y.set_alpha(0.6)

for z in Post_plot['bodies']:
    z.set_facecolor('red')
    z.set_alpha(0.6)

plt.tight_layout()
plt.show()