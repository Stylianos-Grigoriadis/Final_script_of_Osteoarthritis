import pandas as pd
import matplotlib.pyplot as plt
force_files = ['subject{n}'.format(n=i) for i in range(1,14)]
participants = pd.read_excel(r'C:\Users\Βασίλης\OneDrive\Υπολογιστής\βασίλης\τεφαα\Biomechanics\Kinvent\Osteoarthitis\Participants.xlsx')


Healthy_pre = []
Healthy_post = []
Surgery_pre = []
Surgery_post = []

for i in range(len((force_files))):
    df_pre = pd.read_excel('data\{f}.xlsx'.format(f=force_files[i]),sheet_name='Pre-surgery',header=[1,2])
    df_post = pd.read_excel('data\{f}.xlsx'.format(f=force_files[i]), sheet_name='Post-surgery',header=[1,2])
    if participants['Χειρουργημένο γόνατο'][i]=='Αριστερό':
        left = 'Left S'
        right = 'Right'
        leg = 'Left'
    else:
        left = 'Left'
        right = 'Right S'
        leg = 'Right'

    Left_max_pre = (df_pre[left]['Max'].dropna())
    Right_max_pre = (df_pre[right]['Max'].dropna())

    Left_max_post = (df_post[left]['Max'].dropna())
    Right_max_post = (df_post[right]['Max'].dropna())

    if leg == 'Left':
        Healthy_pre.append(Right_max_pre)
        Healthy_post.append(Right_max_post)
        Surgery_pre.append(Left_max_pre)
        Surgery_post.append(Left_max_post)
    else:
        Healthy_pre.append(Left_max_pre)
        Healthy_post.append(Left_max_post)
        Surgery_pre.append(Right_max_pre)
        Surgery_post.append(Right_max_post)
measurements = [Healthy_pre,
Healthy_post,
Surgery_pre,
Surgery_post]

Total_ext = []
Total_flex = []
for m in measurements:
    Extension = []
    Flexion = []
    Ext1 = [i[0] for i in m]
    Ext2 = [i[1] for i in m]
    Flex1 = [i[2] for i in m]
    Flex2 = [i[3] for i in m]

    for e1,e2,f1,f2 in zip(Ext1,Ext2,Flex1,Flex2):

        extension = [e1,e2]
        flexion = [f1,f2]
        Extension.append(max(extension))
        Flexion.append(max(flexion))
    Total_ext.append(Extension)
    Total_flex.append(Flexion)
Type = []
for type in participants['Τύπος Χειρουργείου']:
    if type=='MV':
        Type.append(1)
    else:
        Type.append(0)
df_results = pd.DataFrame({'Extension_Healthy_pre':Total_ext[0],'Extension_Healthy_post':Total_ext[1],
                           'Extension_Surgery_pre':Total_ext[2],'Extension_Surgery_post':Total_ext[3],
                           'Flexion_Healthy_pre':Total_flex[0],'Flexion_Healthy_post':Total_flex[1],
                           'Flexion_Surgery_pre':Total_flex[2],'Flexion_Surgery_post':Total_flex[3],
                           'Surgery Type (0:Parap,1:MV)':Type})
# writer = pd.ExcelWriter('Results pre post MAX 2.xlsx')
# df_results.to_excel(writer)
# writer.save()
# writer.close()


