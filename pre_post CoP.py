import pandas as pd
import matplotlib.pyplot as plt
Cop_files = ['subject{n}CoP'.format(n=i) for i in range(1,14)]
participants = pd.read_excel(r'C:\Users\Βασίλης\OneDrive\Υπολογιστής\βασίλης\τεφαα\Biomechanics\Kinvent\Osteoarthitis\Participants.xlsx')

Weight_Surgery_pre = []
Weight_Surgery_post = []
IQR_x_preS = []
IQR_x_postS = []
IQR_y_preS = []
IQR_y_postS = []


IQR_x_preH = []
IQR_x_postH = []
IQR_y_preH = []
IQR_y_postH = []

IQRx_pre = []
IQRx_post = []
IQRy_pre = []
IQRy_post = []

TD_preS = []
TD_postS = []
TD_preH = []
TD_postH = []
TD_pre = []
TD_post = []



def assymetry_curve_2Timeseries(var1,var2):
    assymetry_curve = []
    for a,b in zip(var1,var2):
        assymetry_curve.append((a-b)/(a+b))
    mean_value = sum(assymetry_curve) / len(assymetry_curve)
    return assymetry_curve,mean_value

for i in range(len((Cop_files))):
    df_pre = pd.read_excel('data\{f}.xlsx'.format(f=Cop_files[i]),sheet_name='Pre-surgery',header=[1])
    df_post = pd.read_excel('data\{f}.xlsx'.format(f=Cop_files[i]), sheet_name='Post-surgery',header=[1])
    
    if participants['Χειρουργημένο γόνατο'][i]=='Αριστερό':
        left = 'Left S'
        right = 'Right'
        leg = 'Left'
    else:
        left = 'Left'
        right = 'Right S'
        leg = 'Right'

    Left_pre = (df_pre['Average Force (kg)'][0])
    Right_pre = (df_pre['Average Force (kg)'][1])

    Left_post = (df_post['Average Force (kg)'][0])
    Right_post = (df_post['Average Force (kg)'][1])




    if leg == 'Left':



        Weight_Surgery_pre.append(Left_pre / (Right_pre + Left_pre) * 100)
        Weight_Surgery_post.append(Left_post / (Right_post + Left_post) * 100)

        IQR_x_preS.append(df_pre['IQR x (mm)'][0])
        IQR_x_postS.append(df_post['IQR x (mm)'][0])

        IQR_y_preS.append(df_pre['IQR y (mm)'][0])
        IQR_y_postS.append(df_post['IQR y (mm)'][0])

        IQR_x_preH.append(df_pre['IQR x (mm)'][1])
        IQR_x_postH.append(df_post['IQR x (mm)'][1])

        IQR_y_preH.append(df_pre['IQR y (mm)'][1])
        IQR_y_postH.append(df_post['IQR y (mm)'][1])

        TD_preS.append(df_pre['Travel distance (mm)'][0])
        TD_postS.append(df_post['Travel distance (mm)'][0])

        TD_preH.append(df_pre['Travel distance (mm)'][1])
        TD_postH.append(df_post['Travel distance (mm)'][1])

    else:


        Weight_Surgery_pre.append(Right_pre / (Right_pre + Left_pre) * 100)
        Weight_Surgery_post.append(Right_post / (Right_post + Left_post) * 100)

        IQR_x_preS.append(df_pre['IQR x (mm)'][1])
        IQR_x_postS.append(df_post['IQR x (mm)'][1])

        IQR_y_preS.append(df_pre['IQR y (mm)'][1])
        IQR_y_postS.append(df_post['IQR y (mm)'][1])

        IQR_x_preH.append(df_pre['IQR x (mm)'][0])
        IQR_x_postH.append(df_post['IQR x (mm)'][0])

        IQR_y_preH.append(df_pre['IQR y (mm)'][0])
        IQR_y_postH.append(df_post['IQR y (mm)'][0])

        TD_preS.append(df_pre['Travel distance (mm)'][1])
        TD_postS.append(df_post['Travel distance (mm)'][1])

        TD_preH.append(df_pre['Travel distance (mm)'][0])
        TD_postH.append(df_post['Travel distance (mm)'][0])

    TD_pre.append(df_pre['Travel distance (mm)'][2])
    TD_post.append(df_post['Travel distance (mm)'][2])

    IQRx_pre.append(df_pre['IQR x (mm)'][2])
    IQRx_post.append(df_post['IQR x (mm)'][2])

    IQRy_pre.append(df_pre['IQR y (mm)'][2])
    IQRy_post.append(df_post['IQR y (mm)'][2])



df_results = pd.DataFrame({'IQR_x_preH':IQR_x_preH,'IQR_x_postH':IQR_x_postH,
                           'IQR_y_preH':IQR_y_preH,'IQR_y_postH':IQR_y_postH,
                           'IQR_x_preS':IQR_x_preS,'IQR_x_postS':IQR_x_postS,
                           'IQR_y_preS':IQR_y_preS,'IQR_y_postS':IQR_y_postS,
                           'IQRx_pre':IQRx_pre,'IQRx_post':IQRx_post,
                           'IQRy_pre':IQRy_pre,'IQRy_post':IQRy_post,
                           'TD_preS':TD_preS,'TD_postS':TD_postS,
                           'TD_preH':TD_preH,'TD_postH':TD_postH,
                           'TD_pre_total':TD_pre,'TD_post_total':TD_post,
                           'Weight_Surgery_pre':Weight_Surgery_pre,'Weight_Surgery_post':Weight_Surgery_post})
print(df_results)
writer = pd.ExcelWriter('LR IQR TD 2.xlsx')
df_results.to_excel(writer)
writer.save()
writer.close()

