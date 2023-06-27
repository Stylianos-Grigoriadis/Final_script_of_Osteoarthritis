import pandas as pd
import matplotlib.pyplot as plt

force_files =  ['subject1','subject3','subject7','subject8',
                'subject9','subject10','subject11','subject12','subject14','subject15','subject16','subject17','subject18','subject19'
                ,'subject20','subject21','subject22','subject23','subject24','subject25']

knee = ['R','L','L','R','R','L','L','R','R','L','R','R','R','R','R','R','L','L','R','L']
# type 0 : parap, type 1 : MV
Type = [0,1,0,1,1,1,0,0,0,1,1,0,1,0,1,0,1,1,0,0]
Healthy_pre = []
Healthy_post = []
Healthy_2w = []
Healthy_month = []
Surgery_pre = []
Surgery_post = []
Surgery_2w = []
Surgery_month = []

for i in range(len((force_files))):
    try:
        #print(force_files[i])
        df_pre = pd.read_excel('data\{f}.xlsx'.format(f=force_files[i]),sheet_name='Pre-surgery',header=[1,2])
        df_post = pd.read_excel('data\{f}.xlsx'.format(f=force_files[i]), sheet_name='Post-surgery',header=[1,2])
        df_2w = pd.read_excel('data\{f}.xlsx'.format(f=force_files[i]), sheet_name='2 weeks',header=[1,2])
        df_month = pd.read_excel('data\{f}.xlsx'.format(f=force_files[i]), sheet_name='4 weeks',header=[1,2])
        #print(df_month)
        if knee[i]=='L':
            left = 'Left S'
            right = 'Right'
            leg = 'Left'
        else:
            left = 'Left'
            right = 'Right S'
            leg = 'Right'
        #print(knee[i],right,left)
        Left_max_pre = (df_pre[left]['Max'].dropna())
        Right_max_pre = (df_pre[right]['Max'].dropna())

        Left_max_post = (df_post[left]['Max'].dropna())
        Right_max_post = (df_post[right]['Max'].dropna())

        Left_max_2w = (df_post[left]['Max'].dropna())
        Right_max_2w = (df_post[right]['Max'].dropna())

        Left_max_month = (df_month[left]['Max'].dropna())
        Right_max_month = (df_month[right]['Max'].dropna())

        if leg == 'Left':
            Healthy_pre.append(Right_max_pre)
            Healthy_post.append(Right_max_post)
            Healthy_2w.append(Right_max_post)
            Healthy_month.append(Right_max_month)

            Surgery_pre.append(Left_max_pre)
            Surgery_post.append(Left_max_post)
            Surgery_2w.append(Left_max_post)
            Surgery_month.append(Left_max_month)
        else:
            Healthy_pre.append(Left_max_pre)
            Healthy_post.append(Left_max_post)
            Healthy_2w.append(Left_max_post)
            Healthy_month.append(Left_max_month)

            Surgery_pre.append(Right_max_pre)
            Surgery_post.append(Right_max_post)
            Surgery_2w.append(Right_max_post)
            Surgery_month.append(Right_max_month)
    except:
        Healthy_pre.append('NONE')
        Healthy_post.append('NONE')
        Healthy_2w.append('NONE')
        Healthy_month.append('NONE')

        Surgery_pre.append('NONE')
        Surgery_post.append('NONE')
        Surgery_2w.append('NONE')
        Surgery_month.append('NONE')

measurements = [Healthy_pre, Healthy_post, Healthy_2w, Healthy_month, Surgery_pre, Surgery_post, Surgery_2w, Surgery_month]

Total_ext = []
Total_flex = []
for m in measurements:
    Extension = []
    Flexion = []
    Ext1 = []
    Ext2 = []
    Flex1 = []
    Flex2 = []
    for i in m:
        if isinstance(i,str):
            Ext1.append('nan')
            Ext2.append('nan')
            Flex1.append('nan')
            Flex2.append('nan')
        else:
            Ext1.append(i[0])
            Ext2.append(i[1])
            Flex1.append(i[2])
            Flex2.append(i[3])
    for e1,e2,f1,f2 in zip(Ext1,Ext2,Flex1,Flex2):
        extension = [e1,e2]
        flexion = [f1,f2]
        Extension.append(max(extension))
        Flexion.append(max(flexion))
    Total_ext.append(Extension)
    Total_flex.append(Flexion)



df_results = pd.DataFrame({'Subject':force_files,
                           'Extension_Healthy_pre':Total_ext[0],'Extension_Healthy_post':Total_ext[1],'Extension_Healthy_2w':Total_ext[3], 'Extension_Healthy_month':Total_ext[3],
                           'Extension_Surgery_pre':Total_ext[4],'Extension_Surgery_post':Total_ext[5],'Extension_Surgery_2w':Total_ext[6], 'Extension_Surgery_month':Total_ext[7],
                           'Flexion_Healthy_pre':Total_flex[0],'Flexion_Healthy_post':Total_flex[1],'Flexion_Healthy_2w':Total_flex[3],  'Flexion_Healthy_month':Total_flex[3],
                           'Flexion_Surgery_pre':Total_flex[4],'Flexion_Surgery_post':Total_flex[5],'Flexion_Surgery_2w':Total_flex[6],  'Flexion_Surgery_month':Total_flex[7],
                           'Surgery Type (0:Parap,1:MV)':Type})

writer = pd.ExcelWriter('ForceRes all.xlsx')
df_results.to_excel(writer)
writer.close()