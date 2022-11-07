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
data['天候'].replace([1,2,3,4,5,6,7,8], [0,0,0,0,1,1,1,1], inplace=True)
data['光線'].replace([1,2,3,4], [0,0,1,1], inplace=True)
#導入資料
X = data[['天候','光線']]
y = data[["受傷程度"]]
#訓練
X_train, X_test, y_Train, y_test = train_test_split(X, y, test_size=0.1, random_state=1)
#trainer
dtree =tree.DecisionTreeClassifier()
clf = dtree.fit(X_train, y_Train)
print("準確率 :", dtree.score(X_test, y_test))

# preds= dtree.predict_proba(X=X_test)
# print(pd.crosstab(preds[:,0], columns=[X["willWait"],X_test["pat"]]))
plt.figure()
plot_tree(clf, filled=True,fontsize=12)
plt.show()