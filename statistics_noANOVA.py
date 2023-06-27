import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_excel('for final stats\ForceRes all.xlsx')
print(df)
ext_h = df[df['variable']=='Ext_healthy']
ext_s = df[df['variable']=='Ext_surgery']
flex_h = df[df['variable']=='Flex_healthy']
flex_s = df[df['variable']=='Flex_surgery']

MV_ext_h = ext_h[ext_h['Surgery Type (0:Parap,1:MV)']==1]
MV_ext_s = ext_s[ext_s['Surgery Type (0:Parap,1:MV)']==1]
MV_flex_h = flex_h[flex_h['Surgery Type (0:Parap,1:MV)']==1]
MV_flex_s = flex_s[flex_s['Surgery Type (0:Parap,1:MV)']==1]

Parap_ext_h = ext_h[ext_h['Surgery Type (0:Parap,1:MV)']==0]
Parap_ext_s = ext_s[ext_s['Surgery Type (0:Parap,1:MV)']==0]
Parap_flex_h = flex_h[flex_h['Surgery Type (0:Parap,1:MV)']==0]
Parap_flex_s = flex_s[flex_s['Surgery Type (0:Parap,1:MV)']==0]
print(ext_h.columns)
repeated_measures = ['pre', 'post', '2w', 'month']

for rm in repeated_measures:
    print(rm)
    print()
    MV_temp_ext_h = MV_ext_h[rm]
    MV_temp_ext_s = MV_ext_s[rm]
    MV_temp_flex_h = MV_flex_h[rm]
    MV_temp_flex_s = MV_flex_s[rm]
    
    Parap_temp_ext_h = Parap_ext_h[rm]
    Parap_temp_ext_s = Parap_ext_s[rm]
    Parap_temp_flex_h = Parap_flex_h[rm]
    Parap_temp_flex_s = Parap_flex_s[rm]

    print('MV_temp_ext_h: ',stats.normaltest(MV_temp_ext_h)[1])
    print('MV_temp_ext_s: ', stats.normaltest(MV_temp_ext_s)[1])
    print('MV_temp_flex_h: ', stats.normaltest(MV_temp_flex_h)[1])
    print('MV_temp_flex_s: ', stats.normaltest(MV_temp_flex_s)[1])

    if stats.normaltest(MV_temp_ext_h)[1] < 0.05:
        print('Not Normal')
    if stats.normaltest(MV_temp_ext_s)[1] < 0.05:
        print('Not Normal')
    if stats.normaltest(MV_temp_flex_h)[1] < 0.05:
        print('Not Normal')
    if stats.normaltest(MV_temp_flex_s)[1] < 0.05:
        print('Not Normal')

    print('Parap_temp_ext_h: ', stats.normaltest(Parap_temp_ext_h)[1])
    print('Parap_temp_ext_s: ', stats.normaltest(Parap_temp_ext_s)[1])
    print('Parap_temp_flex_h: ', stats.normaltest(Parap_temp_flex_h)[1])
    print('Parap_temp_flex_s: ', stats.normaltest(Parap_temp_flex_s)[1])


    if stats.normaltest(Parap_temp_ext_h)[1] < 0.05:
        print('Not Normal')
    if stats.normaltest(Parap_temp_ext_s)[1] < 0.05:
        print('Not Normal')
    if stats.normaltest(Parap_temp_flex_h)[1] < 0.05:
        print('Not Normal')
    if stats.normaltest(Parap_temp_flex_s)[1] < 0.05:
        print('Not Normal')
    print()





