import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from cycler import cycler
from matplotlib import rcParams


df = pd.read_excel(r'Results pre post MAX 2.xlsx')
print(df)

ext = df[df['Feature ext-flex']=='ext']
flex = df[df['Feature ext-flex']=='flex']

extMV = ext[ext['Surgery Type (0:Parap,1:MV)']==1]
extParap = ext[ext['Surgery Type (0:Parap,1:MV)']==0]

flexMV = flex[flex['Surgery Type (0:Parap,1:MV)']==1]
flexParap = flex[flex['Surgery Type (0:Parap,1:MV)']==0]

ext_MV_Healthy_pre = extMV['Extension_Healthy_pre'].mean()
ext_MV_Healthy_post = extMV['Extension_Healthy_post'].mean()
ext_MV_Surgery_pre = extMV['Extension_Surgery_pre'].mean()
ext_MV_Surgery_post = extMV['Extension_Surgery_post'].mean()

ext_Parap_Healthy_pre = extParap['Extension_Healthy_pre'].mean()
ext_Parap_Healthy_post = extParap['Extension_Healthy_post'].mean()
ext_Parap_Surgery_pre = extParap['Extension_Surgery_pre'].mean()
ext_Parap_Surgery_post = extParap['Extension_Surgery_post'].mean()

flex_MV_Healthy_pre = flexMV['Extension_Healthy_pre'].mean()
flex_MV_Healthy_post = flexMV['Extension_Healthy_post'].mean()
flex_MV_Surgery_pre = flexMV['Extension_Surgery_pre'].mean()
flex_MV_Surgery_post = flexMV['Extension_Surgery_post'].mean()

flex_Parap_Healthy_pre = flexParap['Extension_Healthy_pre'].mean()
flex_Parap_Healthy_post = flexParap['Extension_Healthy_post'].mean()
flex_Parap_Surgery_pre = flexParap['Extension_Surgery_pre'].mean()
flex_Parap_Surgery_post = flexParap['Extension_Surgery_post'].mean()


# Ext Plot
plt.rcParams.update({'font.size':16})
plt.rcParams['errorbar.capsize']=10
plt.title('Knee Extension')
plt.ylabel('Force (kg)')

plt.plot([ext_MV_Surgery_pre,ext_MV_Surgery_post],label='MV',color='blue',lw=2)
plt.plot([ext_Parap_Surgery_pre,ext_Parap_Surgery_post],label='Parap',color='orange',lw=2)

plt.plot([2,3],[ext_MV_Healthy_pre,ext_MV_Healthy_post],color='blue',lw=2)
plt.plot([2,3],[ext_Parap_Healthy_pre,ext_Parap_Healthy_post],color='orange',lw=2)

plt.errorbar(x=0,y=ext_MV_Surgery_pre,yerr=extMV['Extension_Surgery_pre'].std(),ecolor='blue',lw=3)
plt.errorbar(x=1,y=ext_MV_Surgery_post,yerr=extMV['Extension_Surgery_post'].std(),ecolor='blue',lw=3)

plt.errorbar(x=0,y=ext_Parap_Surgery_pre,yerr=extParap['Extension_Surgery_pre'].std(),ecolor='orange',lw=3)
plt.errorbar(x=1,y=ext_Parap_Surgery_post,yerr=extParap['Extension_Surgery_post'].std(),ecolor='orange',lw=3)


plt.errorbar(x=2,y=ext_MV_Healthy_pre,yerr=extMV['Extension_Healthy_pre'].std(),ecolor='blue',lw=3)
plt.errorbar(x=3,y=ext_MV_Healthy_post,yerr=extMV['Extension_Healthy_post'].std(),ecolor='blue',lw=3)

plt.errorbar(x=2,y=ext_Parap_Healthy_pre,yerr=extParap['Extension_Healthy_pre'].std(),ecolor='orange',lw=3)
plt.errorbar(x=3,y=ext_Parap_Healthy_post,yerr=extParap['Extension_Healthy_post'].std(),ecolor='orange',lw=3)


plt.xticks([0,0.5,1,2,2.5,3],['pre','\nSurgery','post','pre', '\nHealthy','post'])
#plt.xticks([0.5,2.5],['\nSurgery', '\nHealthy'], minor=False)
plt.legend()
plt.show()


# Flex Plot
plt.rcParams.update({'font.size':16})
plt.rcParams['errorbar.capsize']=10
plt.title('Knee Flexion')
plt.ylabel('Force (kg)')

plt.plot([flex_MV_Surgery_pre,flex_MV_Surgery_post],label='MV',color='blue',lw=2)
plt.plot([flex_Parap_Surgery_pre,flex_Parap_Surgery_post],label='Parap',color='orange',lw=2)

plt.plot([2,3],[flex_MV_Healthy_pre,flex_MV_Healthy_post],color='blue',lw=2)
plt.plot([2,3],[flex_Parap_Healthy_pre,flex_Parap_Healthy_post],color='orange',lw=2)

plt.errorbar(x=0,y=flex_MV_Surgery_pre,yerr=flexMV['Extension_Surgery_pre'].std(),ecolor='blue',lw=3)
plt.errorbar(x=1,y=flex_MV_Surgery_post,yerr=flexMV['Extension_Surgery_post'].std(),ecolor='blue',lw=3)

plt.errorbar(x=0,y=flex_Parap_Surgery_pre,yerr=flexParap['Extension_Surgery_pre'].std(),ecolor='orange',lw=3)
plt.errorbar(x=1,y=flex_Parap_Surgery_post,yerr=flexParap['Extension_Surgery_post'].std(),ecolor='orange',lw=3)


plt.errorbar(x=2,y=flex_MV_Healthy_pre,yerr=flexMV['Extension_Healthy_pre'].std(),ecolor='blue',lw=3)
plt.errorbar(x=3,y=flex_MV_Healthy_post,yerr=flexMV['Extension_Healthy_post'].std(),ecolor='blue',lw=3)

plt.errorbar(x=2,y=flex_Parap_Healthy_pre,yerr=flexParap['Extension_Healthy_pre'].std(),ecolor='orange',lw=3)
plt.errorbar(x=3,y=flex_Parap_Healthy_post,yerr=flexParap['Extension_Healthy_post'].std(),ecolor='orange',lw=3)


plt.xticks([0,0.5,1,2,2.5,3],['pre','\nSurgery','post','pre', '\nHealthy','post'])
#plt.xticks([0.5,2.5],['\nSurgery', '\nHealthy'], minor=False)
plt.legend()
plt.show()

# Plots no Healthy
plt.rcParams.update({'font.size':16})
plt.rcParams['errorbar.capsize']=10
plt.title('Knee under surgery')
plt.ylabel('Force (kg)')

plt.plot([ext_MV_Surgery_pre,ext_MV_Surgery_post],label='MV',color='blue',lw=2)
plt.plot([ext_Parap_Surgery_pre,ext_Parap_Surgery_post],label='Parap',color='orange',lw=2)

plt.errorbar(x=0,y=ext_MV_Surgery_pre,yerr=extMV['Extension_Surgery_pre'].std(),ecolor='blue',lw=3)
plt.errorbar(x=1,y=ext_MV_Surgery_post,yerr=extMV['Extension_Surgery_post'].std(),ecolor='blue',lw=3)

plt.errorbar(x=0,y=ext_Parap_Surgery_pre,yerr=extParap['Extension_Surgery_pre'].std(),ecolor='orange',lw=3)
plt.errorbar(x=1,y=ext_Parap_Surgery_post,yerr=extParap['Extension_Surgery_post'].std(),ecolor='orange',lw=3)

plt.plot([2,3],[flex_MV_Surgery_pre,flex_MV_Surgery_post],color='blue',lw=2)
plt.plot([2,3],[flex_Parap_Surgery_pre,flex_Parap_Surgery_post],color='orange',lw=2)

plt.errorbar(x=2,y=flex_MV_Surgery_pre,yerr=flexMV['Extension_Surgery_pre'].std(),ecolor='blue',lw=3)
plt.errorbar(x=3,y=flex_MV_Surgery_post,yerr=flexMV['Extension_Surgery_post'].std(),ecolor='blue',lw=3)

plt.errorbar(x=2,y=flex_Parap_Surgery_pre,yerr=flexParap['Extension_Surgery_pre'].std(),ecolor='orange',lw=3)
plt.errorbar(x=3,y=flex_Parap_Surgery_post,yerr=flexParap['Extension_Surgery_post'].std(),ecolor='orange',lw=3)

plt.xticks([0,0.5,1,2,2.5,3],['pre','\nExtension','post','pre', '\nFlexion','post'])
#plt.xticks([0.5,2.5],['\nSurgery', '\nHealthy'], minor=False)
plt.legend()
plt.show()