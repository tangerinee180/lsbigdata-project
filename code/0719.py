import numpy as np
import matplotlib.pyplot as plt    

#예제 넘파이 배열 생성
np.random.seed(2024)
data = np.random.rand(10)

#히스토그램 그리기
#히스토그램이란? = 빈도표
plt.clf()
plt.hist(data,bins=4,alpha=0.7,color="blue")
plt.title("Histogram of Numpy Vector")
plt.xlabel("Value")
plt.ylabel("Frequency")
#plt.grid = 선 넣기 없애기
plt.grid(False)
plt.show()


np.random.rand(50000).reshape(-1,5).mean(axis=1)
data2 = np.random.rand(10000,5).mean(axis=1)


def qwer(num):
    list=[]
    for _ in range(num) :
        list.append(np.random.randint(0,32,5).mean())
    return np.array(list)
data1 = qwer(10000)


plt.hist(data2,bins=30,alpha=0.7,color="blue")
plt.title("Histogram of Numpy Vector")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()
plt.clf()
