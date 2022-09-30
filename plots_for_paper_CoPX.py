import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel(r'Stance Evaluation Results.xlsx',sheet_name='Sheet1')
print(df)

x = df[df['Feature']=='x']
print(x)
y=df[df['Feature']=='y']
y_MV = y[y['Surgerytype']==1]
y_Parap = y[y['Surgerytype']==0]
y_MV_Both_pre = y_MV['Bothpre'].mean()
y_MV_Both_post = y_MV['Bothpost'].mean()
y_Parap_Both_pre= y_Parap['Bothpre'].mean()
y_Parap_Both_post= y_Parap['Bothpost'].mean()


x_MV = x[x['Surgerytype']==1]
x_Parap = x[x['Surgerytype']==0]



x_MV_Healthy_pre = x_MV['Healthypre'].mean()
x_MV_Surgery_pre = x_MV['Surgerypre'].mean()
x_MV_Both_pre = x_MV['Bothpre'].mean()

x_MV_Healthy_post = x_MV['Healthypost'].mean()
x_MV_Surgery_post = x_MV['Surgerypost'].mean()
x_MV_Both_post= x_MV['Bothpost'].mean()

x_Parap_Healthy_pre = x_Parap['Healthypre'].mean()
x_Parap_Surgery_pre = x_Parap['Surgerypre'].mean()
x_Parap_Both_pre = x_Parap['Bothpre'].mean()

x_Parap_Healthy_post = x_Parap['Healthypost'].mean()
x_Parap_Surgery_post = x_Parap['Surgerypost'].mean()
x_Parap_Both_post= x_Parap['Bothpost'].mean()

plt.rcParams.update({'font.size':16})
plt.rcParams['errorbar.capsize']=10
plt.title('ML axis CoP')
plt.ylabel('IQR (mm)')

# plt.plot([x_MV_Healthy_pre,x_MV_Healthy_post],label='MV',color='blue',lw=2)
# plt.plot([x_Parap_Healthy_pre,x_Parap_Healthy_post],label='Parap',color='orange',lw=2)
#
# plt.plot([2,3],[x_MV_Surgery_pre,x_MV_Surgery_post],color='blue',lw=2)
# plt.plot([2,3],[x_Parap_Surgery_pre,x_Parap_Surgery_post],color='orange',lw=2)

# plt.plot([2,3],[y_MV_Both_pre,y_MV_Both_post],color='blue',lw=2,label='MV')
# plt.plot([2,3],[y_Parap_Both_pre,y_Parap_Both_post],color='orange',lw=2,label='Parap')

plt.plot([4,5],[x_MV_Both_pre,x_MV_Both_post],color='blue',lw=2,label='MV')
plt.plot([4,5],[x_Parap_Both_pre,x_Parap_Both_post],color='orange',lw=2,label='Parap')

# plt.errorbar(x=0,y=x_MV_Healthy_pre,yerr=x_MV['Healthypre'].std(),ecolor='blue',lw=3)
# plt.errorbar(x=1,y=x_MV_Healthy_post,yerr=x_MV['Healthypost'].std(),ecolor='blue',lw=3)
#
# plt.errorbar(x=0,y=x_Parap_Healthy_pre,yerr=x_Parap['Healthypre'].std(),ecolor='orange',lw=3)
# plt.errorbar(x=1,y=x_Parap_Healthy_post,yerr=x_Parap['Healthypost'].std(),ecolor='orange',lw=3)
#
# plt.errorbar(x=2,y=x_MV_Surgery_pre,yerr=x_MV['Surgerypre'].std(),ecolor='blue',lw=3)
# plt.errorbar(x=3,y=x_MV_Surgery_post,yerr=x_MV['Surgerypost'].std(),ecolor='blue',lw=3)
#
# plt.errorbar(x=2,y=x_Parap_Surgery_pre,yerr=x_Parap['Surgerypre'].std(),ecolor='orange',lw=3)
# plt.errorbar(x=3,y=x_Parap_Surgery_post,yerr=x_Parap['Surgerypost'].std(),ecolor='orange',lw=3)

plt.errorbar(x=4,y=x_MV_Both_pre,yerr=x_MV['Bothpre'].std(),ecolor='blue',lw=3)
plt.errorbar(x=5,y=x_MV_Both_post,yerr=x_MV['Bothpost'].std(),ecolor='blue',lw=3)

plt.errorbar(x=4,y=x_Parap_Both_pre,yerr=x_Parap['Bothpre'].std(),ecolor='orange',lw=3)
plt.errorbar(x=5,y=x_Parap_Both_post,yerr=x_Parap['Bothpost'].std(),ecolor='orange',lw=3)




#plt.xticks([0,0.5,1,2,2.5,3,4,4.5,5],['pre','\nHealthy','post','pre', '\nSurgery','post','pre', '\nBoth','post'])
plt.xticks([4,5],['pre','post'])
plt.tight_layout()
plt.legend()
plt.show()

