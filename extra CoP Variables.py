import pandas as pd
import math
import numpy as np

force_files =  ['subject1','subject3','subject7','subject8',
                'subject9','subject10','subject11','subject12','subject14','subject15','subject16','subject17','subject18','subject19'
                ,'subject20','subject21','subject22','subject23','subject24','subject25']

knee = ['R','L','L','R','R','L','L','R','R','L','R','R','R','R','R','R','L','L','R','L']
# type 0 : parap, type 1 : MV
type = [0,1,0,1,1,1,0,0,0,1,1,0,1,0,1,0,1,1,0,0]
def compute_vel(x,y):
    pass



mean_vel_pre = []
mean_vel_post = []
mean_vel_2w = []
mean_vel_month = []
for p,l in zip(force_files,knee):
    print(p)
    pre = pd.read_excel('data\{p}CoP.xlsx'.format(p=p),header=[1,2,3],sheet_name='Pre-surgery')
    post = pd.read_excel('data\{p}CoP.xlsx'.format( p=p), header=[1, 2, 3],sheet_name='Post-surgery')
    w2 = pd.read_excel('data\{p}CoP.xlsx'.format(p=p), header=[1, 2, 3], sheet_name='2 weeks')
    month = pd.read_excel('data\{p}CoP.xlsx'.format(p=p), header=[1, 2, 3], sheet_name='4 weeks')
    fs_pre = pre['Fs'].columns[0][0]
    fs_post = post['Fs'].columns[0][0]
    fs_w2 = w2['Fs'].columns[0][0]
    fs_month = month['Fs'].columns[0][0]
    vel_pre = []
    vel_post = []
    vel_2w = []
    vel_month = []
    for i in range(len(pre['CoP']['Both']['x (mm)']) - 1):
        euclid_distance_down = math.sqrt(
            (pre['CoP']['Both']['x (mm)'][i] - pre['CoP']['Both']['x (mm)'][i + 1]) ** 2 + (pre['CoP']['Both']['y (mm)'][i] - pre['CoP']['Both']['y (mm)'][i + 1]) ** 2)
        vel_pre.append(euclid_distance_down / (1 / fs_pre))

    for i in range(len(post['CoP']['Both']['x (mm)']) - 1):
        euclid_distance_down = math.sqrt(
            (post['CoP']['Both']['x (mm)'][i] - post['CoP']['Both']['x (mm)'][i + 1]) ** 2 + (post['CoP']['Both']['y (mm)'][i] - post['CoP']['Both']['y (mm)'][i + 1]) ** 2)
        vel_post.append(euclid_distance_down / (1 / fs_post))

    for i in range(len(w2['CoP']['Both']['x (mm)']) - 1):
        euclid_distance_down = math.sqrt(
            (w2['CoP']['Both']['x (mm)'][i] - w2['CoP']['Both']['x (mm)'][i + 1]) ** 2 + (w2['CoP']['Both']['y (mm)'][i] - w2['CoP']['Both']['y (mm)'][i + 1]) ** 2)
        vel_2w.append(euclid_distance_down / (1 / fs_w2))

    for i in range(len(month['CoP']['Both']['x (mm)']) - 1):
        euclid_distance_down = math.sqrt(
            (month['CoP']['Both']['x (mm)'][i] - month['CoP']['Both']['x (mm)'][i + 1]) ** 2 + (month['CoP']['Both']['y (mm)'][i] - month['CoP']['Both']['y (mm)'][i + 1]) ** 2)
        vel_month.append(euclid_distance_down / (1 / fs_month))
    mean_vel_pre.append(np.mean( vel_pre))
    mean_vel_post.append(np.mean( vel_post))
    mean_vel_2w.append(np.mean( vel_2w))
    mean_vel_month.append(np.mean( vel_month))
measurements = [mean_vel_pre, mean_vel_post, mean_vel_2w, mean_vel_month]
results = pd.DataFrame({'mean_vel_pre':mean_vel_pre,'mean_vel_post':mean_vel_post,'mean_vel_2w':mean_vel_2w,'mean_vel_month':mean_vel_month,})


results.to_excel('mean_vel.xlsx')












