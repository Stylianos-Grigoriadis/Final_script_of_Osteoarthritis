import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from cycler import cycler
from matplotlib import rcParams
import matplotlib.patches as mpatches

df = pd.read_excel(r'Stance Evaluation Results.xlsx',sheet_name='Sheet1')

TD = df[df['Feature']=='TD']
df = pd.read_excel(r'Stance Evaluation Results.xlsx',sheet_name='Sheet2')
Weight = df[df['Feature']=='Weight']
mVel = df[df['Feature']=='mVel']
print(TD)
print(Weight)

TD_MV = TD[TD['Surgerytype']==1]
TD_Parap = TD[TD['Surgerytype']==0]

Weight_MV = Weight[Weight['Surgerytype']==1]
Weight_Parap = Weight[Weight['Surgerytype']==0]

mVel_MV =  mVel[mVel['Surgerytype']==1]
mVel_Parap = mVel[mVel['Surgerytype']==0]

print(TD_MV)

Weight_MV_pre = Weight_MV['pre'].mean()
Weight_MV_post = Weight_MV['post'].mean()

Weight_Parap_pre = Weight_Parap['pre'].mean()
Weight_Parap_post = Weight_Parap['post'].mean()

mVel_MV_pre = mVel_MV['pre'].mean()
mVel_MV_post = mVel_MV['post'].mean()

mVel_Parap_pre = mVel_Parap['pre'].mean()
mVel_Parap_post = mVel_Parap['post'].mean()



# plt.rcParams.update({'font.size':16})
# plt.rcParams['errorbar.capsize']=10
# fig,(ax) = plt.subplots()
#
# ax.set_title('Weight Distribution')
# ax.set_ylabel('Weight on surgery leg \n(% of total weight)')
#
# ax.plot([Weight_MV_pre,Weight_MV_post],label='MV',color='blue',lw=2)
# ax.plot([Weight_Parap_pre,Weight_Parap_post],label='Parap',color='orange',lw=2)
#
# ax.errorbar(x=0,y=Weight_MV_pre,yerr=Weight_MV['pre'].std(),ecolor='blue',lw=3)
# ax.errorbar(x=1,y=Weight_MV_post,yerr=Weight_MV['post'].std(),ecolor='blue',lw=3)
# ax.errorbar(x=0,y=Weight_Parap_pre,yerr=Weight_Parap['pre'].std(),ecolor='orange',lw=3)
# ax.errorbar(x=1,y=Weight_Parap_post,yerr=Weight_Parap['post'].std(),ecolor='orange',lw=3)
# ax.set_xticks([0,1],['pre','post'])
#
# plt.tight_layout()
# plt.legend()
# plt.show()
# fig2,(ax1) = plt.subplots()
# ax1.set_title('Mean Velocity')
# ax1.set_ylabel('Velocity (m/s)')
#
# ax1.plot([mVel_MV_pre,mVel_MV_post],label='MV',color='blue',lw=2)
# ax1.plot([mVel_Parap_pre,mVel_Parap_post],label='Parap',color='orange',lw=2)
#
# ax1.errorbar(x=0,y=mVel_MV_pre,yerr=mVel_MV['pre'].std(),ecolor='blue',lw=3)
# ax1.errorbar(x=1,y=mVel_MV_post,yerr=mVel_MV['post'].std(),ecolor='blue',lw=3)
# ax1.errorbar(x=0,y=mVel_Parap_pre,yerr=mVel_Parap['pre'].std(),ecolor='orange',lw=3)
# ax1.errorbar(x=1,y=mVel_Parap_post,yerr=mVel_Parap['post'].std(),ecolor='orange',lw=3)
# ax1.set_xticks([0,1],['pre','post'])
# plt.tight_layout()
# plt.legend()
# plt.show()

# rcParams['axes.prop_cycle'] = cycler(color='k')
# plt.rcParams.update({"font.size": 16})
# fig3,(ax,ax2) = plt.subplots(1,2)
# datapre = [Weight['pre'],mVel['pre']]
# datapost = [Weight['post'],mVel['post']]
# # xTicks_names = ['Weight %', 'mean Vel']
# # xTicks = [1.5, 4.5]
# pre_ticks = [1, 4]
# post_ticks = [2, 5]
#
#
# Pre_plot = ax.violinplot(dataset=datapre, positions=pre_ticks, showextrema=True, showmeans=True)
# Post_plot = ax2.violinplot(dataset=datapost, positions=pre_ticks, showextrema=True, showmeans=True)
# #plt.xticks(ticks=xTicks, labels=xTicks_names)
# red_patch = mpatches.Patch(color='red',alpha=0.6)
# blue_patch = mpatches.Patch(color='blue',alpha=0.6)
# label=['Healthy','In pain']
#
# for y in Pre_plot['bodies']:
#     y.set_facecolor('blue')
#     y.set_alpha(0.6)
#
# for z in Post_plot['bodies']:
#     z.set_facecolor('red')
#     z.set_alpha(0.6)
#
# fake_handles = blue_patch,red_patch
# plt.legend(fake_handles, label, loc='upper center', bbox_to_anchor=(0.5, 1.10),
#           ncol=3, fancybox=True, shadow=True, prop={'size': 14})
#
# plt.tight_layout()
# plt.show()
# TD Plot


# TD_MV_pre = TD_MV['Healthypre'].mean()
# TD_MV_post = TD_MV['Healthypost'].mean()
# TD_Parap_pre = TD_Parap['Healthypre'].mean()
# TD_Parap_post = TD_Parap['Healthypost'].mean()
#
# plt.rcParams.update({'font.size':16})
# plt.rcParams['errorbar.capsize']=10
# plt.title('TD Both')
# plt.ylabel('Force (kg)')
#
# plt.plot([TD_MV_pre,TD_MV_post],label='MV',color='blue',lw=2)
# plt.plot([TD_Parap_pre,TD_Parap_post],label='Parap',color='orange',lw=2)
#
#
# plt.errorbar(x=0,y=TD_MV_pre,yerr=TD_MV['Healthypre'].std(),ecolor='blue',lw=3)
# plt.errorbar(x=1,y=TD_MV_post,yerr=TD_MV['Healthypost'].std(),ecolor='blue',lw=3)
#
# plt.errorbar(x=0,y=TD_Parap_pre,yerr=TD_MV['Healthypre'].std(),ecolor='orange',lw=3)
# plt.errorbar(x=1,y=TD_Parap_post,yerr=TD_MV['Healthypost'].std(),ecolor='orange',lw=3)
#
#
#
# plt.tight_layout()
# plt.legend()
# plt.show()


rcParams['axes.prop_cycle'] = cycler(color='k')
plt.rcParams.update({"font.size": 16})
# datapre = [Weight['pre'],mVel['pre']]
# datapost = [Weight['post'],mVel['post']]
pre_ticks = [1]
post_ticks = [2]


Pre_plot = plt.violinplot(dataset=[mVel['pre']], positions=pre_ticks, showextrema=True, showmeans=True)
Post_plot = plt.violinplot(dataset=[mVel['post']], positions=post_ticks, showextrema=True, showmeans=True)

plt.xticks(ticks=[1,2], labels=['pre','post'])
red_patch = mpatches.Patch(color='red',alpha=0.6)
blue_patch = mpatches.Patch(color='blue',alpha=0.6)
#label=['Healthy','In pain']
plt.title('CoP Mean Velocity')
plt.ylabel('Velocity (mm/s)')
for y in Pre_plot['bodies']:
    y.set_facecolor('blue')
    y.set_alpha(0.6)

for z in Post_plot['bodies']:
    z.set_facecolor('red')
    z.set_alpha(0.6)

# fake_handles = blue_patch,red_patch
# plt.legend(fake_handles, label, loc='upper center', bbox_to_anchor=(0.5, 1.10),
#           ncol=3, fancybox=True, shadow=True, prop={'size': 14})

plt.tight_layout()
plt.show()


