import pandas as pd
import numpy as np    
import matplotlib.pyplot as plt    

#데이터 탐색 함수
#head()
#tail()
#info()
#describe()
#.shape

exam = pd.read_csv("data/exam.csv")
exam.info()
exam.head()
exam.describe()
exam.shape()

type(exam)
var = [1,2,3]
type(var)
exam2 = exam.copy()
exam2 = exam2.rename(columns={"nclass":"class"})
exam2

exam2["total"] = exam2['math'] + exam2["science"] + exam2["english"]
exam2


exam2["test"] = np.where(exam2["total"]>200,"pass","fail")
exam2["test"].value_counts().plot.bar(rot=0)
plt.show()
plt.clf()



df = pd.DataFrame({'lab':['A',"B","C"],'val':[10,20,30]})
df
ax = df.plot.bar(x='lab',y='val')
plt.show()
plt.clf()

exam2["test2"] = np.where(exam2["total"]>=200,"A",np.where(exam2["total"]>=100,"B","C"))
exam2
exam2["test2"] = exam2["total"].apply(lambda x :"A" if x >= 200 else ("B" if x>=100 else "C"))

exam2["test2"].isin(["A","C"])

#a = np.random.choice(np.arange(1,4),size = 200,replace=True,p =np.array([2/5,2/5,1/5]))
a = np.random.choice(np.arange(1,4),size = 100,replace=True,p = np.array([2/5,2/5,1/5]))
