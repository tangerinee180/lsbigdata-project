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

import numpy as np

# 배열 a에서 임의의 원소 하나 선택
a = [1, 2, 3, 4, 5]
print(np.random.choice(a))  # 예: 3

# 배열 a에서 3개의 원소를 복원 추출로 선택
print(np.random.choice(a, size=3))  # 예: [4, 1, 3]

# 배열 a에서 3개의 원소를 비복원 추출로 선택
print(np.random.choice(a, size=3, replace=False))  # 예: [2, 5, 1]

# 배열 a에서 주어진 확률로 3개의 원소를 선택
probabilities = [0.1, 0.2, 0.3, 0.1, 0.3]
print(np.random.choice(a, size=3, p=probabilities))  # 예: [5, 3, 3]

# 다차원 배열에서 axis를 기준으로 샘플링
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.random.choice(b, size=2, axis=0))  # 예: [[7, 8, 9], [1, 2, 3]]



b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

type(b.shape[0])
# axis=0 기준으로 샘플링 (행 기준으로 샘플 선택)
sample_axis_0 = np.random.choice(b.shape[0], size=2, replace=False)
sample_axis_0
print(b[sample_axis_0, :])
# 예: [[7 8 9]
#      [1 2 3]]

# axis=1 기준으로 샘플링 (열 기준으로 샘플 선택)

sample_axis_1 = np.random.choice(3, size=2, replace=False)
sample_axis_1 = np.random.choice(b.shape[1], size=2, replace=False)
print(b[:, sample_axis_1])
