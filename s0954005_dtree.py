import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing, tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
clf = tree.DecisionTreeClassifier(random_state=0)

#讀取資料
data = pd.read_csv("taipei.csv")
#replace
data.fillna({'受傷程度': 0},inplace=True)
data.fillna({'飲酒情形': 0},inplace=True)

#濾除酒駕、無法測量的
data = data[data['受傷程度']!=1]
data = data[data['飲酒情形']<10]
#濾除天氣過爛的
# data = data[data['天候']>5]
#濾除光線過暗的
data = data[data['光線']>1]
#導入資料
# X = data[['光線']]
X = data[['天候']]
# X = data[['飲酒情形']]
y = data[["受傷程度"]]
#訓練
X_train, X_test, y_Train, y_test = train_test_split(X, y, test_size=0.45, random_state=2)
#trainer
dtree =tree.DecisionTreeClassifier()
clf = dtree.fit(X_train, y_Train)
print("準確率 :", dtree.score(X_test, y_test))

plt.figure()
plot_tree(clf, filled=True,fontsize=7)
plt.show()