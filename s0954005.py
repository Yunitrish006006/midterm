import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

usecols = ['車種', '死亡人數', '受傷人數', '天候', '光線']
data = pd.read_csv("taipei.csv",usecols=usecols)



data_die = data.sort_values(by=['受傷人數','死亡人數'],ascending=[True,True]).copy()
plt.title("Population Growth") # title
plt.ylabel("wounded peoples") # y label
plt.xlabel("light condition in the environment") # x label
plt.plot(data_die['受傷人數'],data_die['光線'])
plt.show()