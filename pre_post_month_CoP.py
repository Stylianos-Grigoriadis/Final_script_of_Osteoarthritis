import pandas as pd
import matplotlib.pyplot as plt

force_files =  ['subject1','subject3','subject7','subject8',
                'subject9','subject10','subject11','subject12','subject14','subject15','subject16','subject17','subject18','subject19'
                ,'subject20','subject21','subject22','subject23','subject24','subject25']

knee = ['R','L','L','R','R','L','L','R','R','L','R','R','R','R','R','R','L','L','R','L']
# type 0 : parap, type 1 : MV
type = [0,1,0,1,1,1,0,0,0,1,1,0,1,0,1,0,1,1,0,0]
print(len(type))


Weight_Surgery_pre = []
Weight_Surgery_post = []
Weight_Surgery_2w = []
Weight_Surgery_month = []

IQR_x_preS = []
IQR_x_postS = []
IQR_x_2wS = []
IQR_x_monthS = []

IQR_y_preS = []
IQR_y_postS = []
IQR_y_2wS = []
IQR_y_monthS = []

IQR_x_preH = []
IQR_x_postH = []
IQR_x_2wH = []
IQR_x_monthH = []

IQR_y_preH = []
IQR_y_postH = []
IQR_y_2wH = []
IQR_y_monthH = []

IQRx_pre = []
IQRx_post = []
IQRx_2w = []
IQRx_month = []

IQRy_pre = []
IQRy_post = []
IQRy_2w = []
IQRy_month = []

TD_preS = []
TD_postS = []
TD_2wS = []
TD_monthS = []

TD_preH = []
TD_postH = []
TD_2wH = []
TD_monthH = []

TD_pre = []
TD_post = []
TD_2w = []
TD_month = []

for i in range(len((force_files))):
    #print(force_files[i])
    df_pre = pd.read_excel('data\{f}CoP.xlsx'.format(f=force_files[i]), sheet_name='Pre-surgery', header=[1])
    df_post = pd.read_excel('data\{f}CoP.xlsx'.format(f=force_files[i]), sheet_name='Post-surgery', header=[1])
    df_2w = pd.read_excel('data\{f}CoP.xlsx'.format(f=force_files[i]), sheet_name='2 weeks', header=[1])
    df_month = pd.read_excel('data\{f}CoP.xlsx'.format(f=force_files[i]), sheet_name='4 weeks', header=[1])

    if knee[i] == 'L':
        left = 'Left S'
        right = 'Right'
        leg = 'Left'
    else:
        left = 'Left'
        right = 'Right S'
        leg = 'Right'
    #print(df_pre)
    Left_pre = (df_pre['Average Force (kg)'][0])
    Right_pre = (df_pre['Average Force (kg)'][1])

    Left_post = (df_post['Average Force (kg)'][0])
    Right_post = (df_post['Average Force (kg)'][1])

    Left_2w = (df_2w['Average Force (kg)'][0])
    Right_2w = (df_2w['Average Force (kg)'][1])

    Left_month = (df_month['Average Force (kg)'][0])
    Right_month = (df_month['Average Force (kg)'][1])


    if leg == 'Left':


        Weight_Surgery_pre.append(Left_pre / (Right_pre + Left_pre) * 100)
        Weight_Surgery_post.append(Left_post / (Right_post + Left_post) * 100)
        Weight_Surgery_2w.append(Left_2w / (Right_2w + Left_2w) * 100)
        Weight_Surgery_month.append(Left_month / (Right_month + Left_month) * 100)

        IQR_x_preS.append(df_pre['IQR x (mm)'][0])
        IQR_x_postS.append(df_post['IQR x (mm)'][0])
        IQR_x_2wS.append(df_2w['IQR x (mm)'][0])
        IQR_x_monthS.append(df_month['IQR x (mm)'][0])

        IQR_y_preS.append(df_pre['IQR y (mm)'][0])
        IQR_y_postS.append(df_post['IQR y (mm)'][0])
        IQR_y_2wS.append(df_2w['IQR y (mm)'][0])
        IQR_y_monthS.append(df_month['IQR y (mm)'][0])

        IQR_x_preH.append(df_pre['IQR x (mm)'][1])
        IQR_x_postH.append(df_post['IQR x (mm)'][1])
        IQR_x_2wH.append(df_2w['IQR x (mm)'][1])
        IQR_x_monthH.append(df_month['IQR x (mm)'][1])

        IQR_y_preH.append(df_pre['IQR y (mm)'][1])
        IQR_y_postH.append(df_post['IQR y (mm)'][1])
        IQR_y_2wH.append(df_2w['IQR y (mm)'][1])
        IQR_y_monthH.append(df_month['IQR y (mm)'][1])

        TD_preS.append(df_pre['Travel distance (mm)'][0])
        TD_postS.append(df_post['Travel distance (mm)'][0])
        TD_2wS.append(df_2w['Travel distance (mm)'][0])
        TD_monthS.append(df_month['Travel distance (mm)'][0])

        TD_preH.append(df_pre['Travel distance (mm)'][1])
        TD_postH.append(df_post['Travel distance (mm)'][1])
        TD_2wH.append(df_2w['Travel distance (mm)'][1])
        TD_monthH.append(df_month['Travel distance (mm)'][1])

    else:


        Weight_Surgery_pre.append(Right_pre / (Right_pre + Left_pre) * 100)
        Weight_Surgery_post.append(Right_post / (Right_post + Left_post) * 100)
        Weight_Surgery_2w.append(Right_2w / (Right_2w + Left_2w) * 100)
        Weight_Surgery_month.append(Right_month / (Right_month + Left_month) * 100)

        IQR_x_preS.append(df_pre['IQR x (mm)'][1])
        IQR_x_postS.append(df_post['IQR x (mm)'][1])
        IQR_x_2wS.append(df_2w['IQR x (mm)'][1])
        IQR_x_monthS.append(df_month['IQR x (mm)'][1])

        IQR_y_preS.append(df_pre['IQR y (mm)'][1])
        IQR_y_postS.append(df_post['IQR y (mm)'][1])
        IQR_y_2wS.append(df_2w['IQR y (mm)'][1])
        IQR_y_monthS.append(df_month['IQR y (mm)'][1])

        IQR_x_preH.append(df_pre['IQR x (mm)'][0])
        IQR_x_postH.append(df_post['IQR x (mm)'][0])
        IQR_x_2wH.append(df_2w['IQR x (mm)'][0])
        IQR_x_monthH.append(df_month['IQR x (mm)'][0])

        IQR_y_preH.append(df_pre['IQR y (mm)'][0])
        IQR_y_postH.append(df_post['IQR y (mm)'][0])
        IQR_y_2wH.append(df_2w['IQR y (mm)'][0])
        IQR_y_monthH.append(df_month['IQR y (mm)'][0])

        TD_preS.append(df_pre['Travel distance (mm)'][1])
        TD_postS.append(df_post['Travel distance (mm)'][1])
        TD_2wS.append(df_2w['Travel distance (mm)'][1])
        TD_monthS.append(df_month['Travel distance (mm)'][1])

        TD_preH.append(df_pre['Travel distance (mm)'][0])
        TD_postH.append(df_post['Travel distance (mm)'][0])
        TD_2wH.append(df_2w['Travel distance (mm)'][0])
        TD_monthH.append(df_month['Travel distance (mm)'][0])

    TD_pre.append(df_pre['Travel distance (mm)'][2])
    TD_post.append(df_post['Travel distance (mm)'][2])
    TD_2w.append(df_2w['Travel distance (mm)'][2])
    TD_month.append(df_month['Travel distance (mm)'][2])

    IQRx_pre.append(df_pre['IQR x (mm)'][2])
    IQRx_post.append(df_post['IQR x (mm)'][2])
    IQRx_2w.append(df_2w['IQR x (mm)'][2])
    IQRx_month.append(df_month['IQR x (mm)'][2])

    IQRy_pre.append(df_pre['IQR y (mm)'][2])
    IQRy_post.append(df_post['IQR y (mm)'][2])
    IQRy_2w.append(df_2w['IQR y (mm)'][2])
    IQRy_month.append(df_month['IQR y (mm)'][2])

# print()
# print(len((IQRx_month)))
# print(len((IQRy_month)))
# print(len((Weight_Surgery_month)))
# print(len((TD_month)))
df_results = pd.DataFrame({'IQR_x_preH':IQR_x_preH,'IQR_x_postH':IQR_x_postH,'IQR_x_2wH':IQR_x_2wH,'IQR_x_monthH':IQR_x_monthH,
                           'IQR_y_preH':IQR_y_preH,'IQR_y_postH':IQR_y_postH,'IQR_y_2wH':IQR_y_2wH,'IQR_y_monthH':IQR_y_monthH,
                           'IQR_x_preS':IQR_x_preS,'IQR_x_postS':IQR_x_postS,'IQR_x_2wS':IQR_x_2wS,'IQR_x_monthS':IQR_x_monthS,
                           'IQR_y_preS':IQR_y_preS,'IQR_y_postS':IQR_y_postS,'IQR_y_2wS':IQR_y_2wS,'IQR_y_monthS':IQR_y_monthS,
                           'IQRx_pre':IQRx_pre,'IQRx_post':IQRx_post,'IQRx_2w':IQRx_2w,'IQRx_month':IQRx_month,
                           'IQRy_pre':IQRy_pre,'IQRy_post':IQRy_post,'IQRy_2w':IQRy_2w,'IQRy_month':IQRy_month,
                           'TD_preS':TD_preS,'TD_postS':TD_postS,'TD_2wS':TD_2wS,'TD_monthS':TD_monthS,
                           'TD_preH':TD_preH,'TD_postH':TD_postH,'TD_2wH':TD_2wH,'TD_monthH':TD_monthH,
                           'TD_pre_total':TD_pre,'TD_post_total':TD_post,'TD_2w_total':TD_2w,'TD_month_total':TD_month,
                           'Weight_Surgery_pre':Weight_Surgery_pre,'Weight_Surgery_post':Weight_Surgery_post,'Weight_Surgery_2w':Weight_Surgery_2w,'Weight_Surgery_month':Weight_Surgery_month,
                           'Type(0Parap,1MV)':type})
print(df_results)
writer = pd.ExcelWriter('StanceRes all.xlsx')
df_results.to_excel(writer)
writer.close()