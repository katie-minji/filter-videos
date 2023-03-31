# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 16:56:46 2023

@author: Lur Lab
"""

# =============================================================================
# fix the frequency check!!! (or just ignore)
# =============================================================================

import glob
import os

#check for tone single:    
path = r'Z:\Soo B\Katie\video files organixze\all\new\SD, 10s, trained'
file = glob.glob(path + '/**/*.txt')

for idx,x in enumerate(file):
    file[idx] = os.path.normpath(x)

mouse_code = 0
my_idx = 0
already_there = False
for my_file in file: 
    # if already_there == False:
    #     print("\n")
    already_there = False
    #print mouse name
    name = my_file.replace('\\', ' ')
    name = name.split()    
    for i in name:
        if 'wt' in i:
            if i == mouse_code:
                already_there = True
                my_idx += 1
            else:
                print(' ')
                print(f'total days: {my_idx}')
                print('\n\n')
                my_idx = 1 
                mouse_code = i
                print(mouse_code)
            break
    a = name[-1].replace('_', ' ')
    a = a.split()
    context = [x for x in a if 'Context' in x]
    try:
        print(context[0])
    except:
       print('manual context check') 
    
    with open(my_file) as f:
        lines = f.readlines()
    for idx, line in enumerate(lines):
        if 'shock #' in line:
            freq_index = idx+2
        if 'number of cycles' in line:
            cycle_index = idx
        if 'tone duration min max' in line:
            tone_duration_index = idx
        if 'initial delay' in line:
            initial_delay_index = idx
            
    #frequency
    temp = []
    for line in lines[freq_index:-1]:
        split = line.split()
        for x in split:
            temp.append(split[3])
    ele = temp[0]
    boolean = True
    for x in temp:
        if x != ele:
            boolean = False
    if boolean == False:
        print("more than 2 frequency, delete")
        
    #number of cycle
    line = lines[cycle_index]
    split = line.split()
    print(f"number of cycles: {split[3]}")
    #tone duration
    line = lines[tone_duration_index]
    split = line.split()
    if split[4] != split[5]:
        print("@@@ Error! min max doesn't match")
    else:
        print(f"tone duration: {split[4]}")
    #initial delay
    line = lines[initial_delay_index]
    split = line.split()
    if split[2] != '120.000':
        print('delay: {split[2]}, delete.')
        
print(f'total days: {my_idx}')




