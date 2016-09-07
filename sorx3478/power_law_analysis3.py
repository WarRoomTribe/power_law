#-*- coding: utf-8 -*-
import sys, os
import math
import time, operator
import matplotlib.pyplot as plt
import numpy as np
import re, pylab
import pandas as pd
from matplotlib import font_manager, rc
#from scipy import stats, polyval

time_rank_list =[]
time_dic={} 
cnt_list = []
time_list = []


pre_cnt_list=[] # not log 
pre_time_rank_list=[] # not log


start_time = time.time()

name_path = "C:\\Users\\necta\\Desktop\\bob_homework".decode('utf-8')
#name_path = name_path.decode('utf-8').encode('utf-8')

for (path, dir, files) in os.walk(name_path):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        
        #print("%s/%s" % (path, filename))
        try:
            b = time.strftime("%Y/%m/%d %H:%M:%S",time.localtime(os.path.getmtime(path +'\\'+ filename)))
        except:
            print path +'\\'+ filename + " is error"
            continue
        if not b in time_dic:
            time_dic[b] = 1
        else:
            time_dic[b] = time_dic[b] + 1
   

sorted_time_list = sorted(time_dic.items(), key=operator.itemgetter(1), reverse = True)

"""
for i in range(len(sorted_time_list)):
    cnt_list.append(sorted_time_list[i][1])
    time_list.append(pd.to_datetime(sorted_time_list[i][0], format='%Y/%m/%d'))
"""
for i in range(len(sorted_time_list)):
    pre_cnt_list.append((float(sorted_time_list[i][1]))) # y modify -> cnt
#   time_list.append(pd.to_datetime(sorted_time_list[i][0], format='%Y/%m/%d %H:%M:%S')) 


for i in range(len(sorted_time_list)):
    cnt_list.append(math.log(float(sorted_time_list[i][1]))) # y modify -> cnt
    time_list.append(pd.to_datetime(sorted_time_list[i][0], format='%Y/%m/%d %H:%M:%S')) 


end_time = time.time()
print end_time - start_time



print "ok"

start_time = time.time()
"""
for i in range(len(cnt_list)):


   cnt_list[i]=math.log(cnt_list[i])
"""

for i in range(len(time_list)):  # not log
   pre_time_rank_list.append(i+1)


for i in range(len(time_list)):
   time_rank_list.append(math.log(float(i+1)))


#time_rank_list.sort(reverse=True)

fig = plt.figure(figsize=(10, 5))
plt.subplot(1,2,1)
#ax = fig.add_subplot(1,2,1)
#x = range(len(time_rank_list))


#plt.xticks(x,time_rank_list, rotation = 90)
#plt.plot(time_rank_list,cnt_list,'b+')
plt.plot(time_rank_list,cnt_list,'b+')
#ax.plot(x, cnt_list,'bo',markersize=2)
plt.title(name_path)


plt.subplot(1,2,2)
plt.plot(pre_time_rank_list,pre_cnt_list,'b+')
plt.title(name_path)

end_time = time.time()
print end_time - start_time

plt.show()


plt.close()