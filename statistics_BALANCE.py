import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_excel('for final stats\StanceRes all.xlsx')


x = df[df['variable']=='x']
y = df[df['variable']=='y']
td = df[df['variable']=='TD']

MV_x = x[x['Type(0Parap,1MV)']==1]
MV_y = y[y['Type(0Parap,1MV)']==1]
MV_td = td[td['Type(0Parap,1MV)']==1]

Parap_x = x[x['Type(0Parap,1MV)']==0]
Parap_y = y[y['Type(0Parap,1MV)']==0]
Parap_td = td[td['Type(0Parap,1MV)']==0]

repeated_measures = ['preH', 'postH', '2wH', 'monthH','preS', 'postS', '2wS', 'monthS','pre', 'post', '2w', 'month']

def between_subjects(groupA,groupB):
    norm_p_A = stats.shapiro(groupA)[1]
    norm_p_B = stats.shapiro(groupB)[1]
    print(norm_p_A)
    print(norm_p_B)
    # Check if both series have normal distribution
    if norm_p_B>0.05 and norm_p_A>0.05:
        # If both have normal distribution, peroform ttest
        res = stats.ttest_ind(groupA,groupB)
    else:
        # If at least one has p value less than 0.05, perform non parametric tests
        res = stats.mannwhitneyu(groupA,groupB, method='asymptotic')
    print(res)

def within_subjects(groupA,groupB):
    norm_p_A = stats.shapiro(groupA)[1]
    norm_p_B = stats.shapiro(groupB)[1]
    print(norm_p_A)
    print(norm_p_B)
    # Check if both series have normal distribution
    if norm_p_B>0.05 and norm_p_A>0.05:
        # If both have normal distribution, peroform ttest
        res = stats.ttest_rel(groupA,groupB)
    else:
        # If at least one has p value less than 0.05, perform non parametric tests
        res = stats.wilcoxon(groupA,groupB)
    print(res)



within_subjects(Parap_td['preH'],Parap_td['2wH'])
within_subjects(MV_td['preH'],MV_td['2wH'])