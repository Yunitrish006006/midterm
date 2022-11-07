import pandas as pd
import numpy as np
import datetime

ori_data = pd.read_csv("taipei.csv")
data = ori_data.loc[:, "發生年":"發生分"]

time = []

x = data.to_string(header=False, index=False, index_names=False).split('\n')
vals = [''.join(ele.split()) for ele in x]
# for i in vals:
#     time.append(datetime.datetime.strptime(i, '%Y%m%d%H%M'))     
for row in x:
    s=''
    line = row.split()
    line[0] = str(int(line[0]) + 1911)
    for idx,j in enumerate(line):
        s += j.zfill(2)
        if idx == 2:
            s += " "
    time.append(datetime.datetime.strptime(s, '%Y%m%d %H%M'))    

print(len(data), len(time))
data.drop(data.columns[[0, 1, 2, 3, 4]], inplace=True, axis=1)
data.insert(0, "時間", time)
print(data[:10])
