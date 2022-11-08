import datetime
import pandas as pd
import matplotlib.pyplot as plt
##########################################################
data = pd.read_csv("taipei.csv")
#將受傷程度改為 受傷嚴重程度 5最嚴重，0是未有人傷亡
data['受傷程度'].replace([1,2,3,4,5], [5,4,3,2,1], inplace=True)
data.fillna({'受傷程度': 0},inplace=True)
#天候則是1~8，越高則是天氣越好
#光線為1~4，越高則愈亮，改為2~8(都成兩倍)
# data['光線'].replace([1,2,3,4], [2,4,6,8], inplace=True)
##########################################################
temp = data.loc[:,"發生年":"發生分"]
time = []
x = temp.to_string(header=False, index=False, index_names=False).split('\n')
vals = [''.join(ele.split()) for ele in x]
for row in x:
    s=''
    line = row.split()
    line[0] = str(int(line[0]) + 1911)
    for idx,j in enumerate(line):
        s += j.zfill(2)
        if idx == 2:
            s += " "
    # time.append(datetime.datetime.strptime(s, '%Y%m%d %H%M'))
    time.append(datetime.datetime.strptime(s, '%Y%m%d %H%M'))
data.drop(data.columns[[0, 1, 2, 3, 4]], inplace=True, axis=1)
data.insert(0, "時間", time)
##########################################################
data.drop(data.columns[1:9],inplace=True,axis=1)
data.drop(data.columns[3:21],inplace=True,axis=1)
data.drop(data.columns[4:],inplace=True,axis=1)
##########################################################
#受傷程度 光線 天候 時間
plt.style.use("ggplot")
data_i8 = data[data["天候"] == 8]
data_i7 = data[data["天候"] == 7]
data_i6 = data[data["天候"] == 6]
data_i5 = data[data["天候"] == 5]
data_i4 = data[data["天候"] == 4]
data_i3 = data[data["天候"] == 3]
data_i2 = data[data["天候"] == 2]
data_i1 = data[data["天候"] == 1]
plt.hist(data_i8['受傷程度'], bins='auto')
plt.hist(data_i7['受傷程度'], bins='auto')
plt.hist(data_i6['受傷程度'], bins='auto')
plt.hist(data_i5['受傷程度'], bins='auto')
plt.hist(data_i4['受傷程度'], bins='auto')
plt.hist(data_i3['受傷程度'], bins='auto')
plt.hist(data_i2['受傷程度'], bins='auto')
plt.hist(data_i1['受傷程度'], bins='auto')
plt.legend(labels=["i8","i7","i6","i5","i4","i3","i2","i1"], loc = 'best')
plt.show()
##########################################################