#-*- coding: utf-8 -*-
import sys, os
import math
import time, operator
import matplotlib.pyplot as plt
import numpy as np
import re, pylab
import pandas as pd
from matplotlib import font_manager, rc

time_rank_list =[]
time_dic={} 
cnt_list = []
time_list = []

pre_cnt_list=[] # not log 
pre_time_rank_list=[] # not log

start_time = time.time()

name_path = "C:\\Users\\uhjin\\Desktop".decode('utf-8')

for (path, dir, files) in os.walk(name_path):
    for filename in files:
        try:
            b = time.strftime("%Y/%m/%d %H:%M:%S",time.localtime(os.path.getmtime(path +'\\'+ filename)))
            if not b in time_dic:
                time_dic[b] = 0
            time_dic[b] = time_dic[b] + 1
        except:
            print path +'\\'+ filename + ": ERROR"
 
sorted_time_list = sorted(time_dic.items(), key=operator.itemgetter(1), reverse = True)

for i in range(len(sorted_time_list)):
    pre_cnt_list.append((float(sorted_time_list[i][1])))
    cnt_list.append(math.log(float(sorted_time_list[i][1])))
    time_list.append(pd.to_datetime(sorted_time_list[i][0], format='%Y/%m/%d %H:%M:%S')) 

end_time = time.time()
print end_time - start_time


print "ok"

start_time = time.time()

for i in range(len(time_list)):  # not log
   pre_time_rank_list.append(i+1)
   time_rank_list.append(math.log(float(i+1)))

fig = plt.figure(figsize=(10, 5))

plt.subplot(1,2,2)
plt.plot(pre_time_rank_list,pre_cnt_list,'b+')
plt.title(name_path)

plt.subplot(1,2,1)
plt.plot(time_rank_list, cnt_list,'b+')
plt.title(name_path)

end_time = time.time()
print end_time - start_time

from scipy import stats, polyval
from pylab import plot, title, show, legend

slope, intercept, r, p, std = stats.linregress(time_rank_list, cnt_list)
ry = polyval([slope, intercept], time_rank_list)

print(slope, intercept, r, p, std)
print(ry)
plot(time_rank_list, cnt_list, 'k.')
plot(time_rank_list, ry, 'r.-')
title('regression')

legend(['original', 'regression'])

show()

plt.show()
plt.close()