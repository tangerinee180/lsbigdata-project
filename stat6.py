import pandas as pd
import numpy as np
import seaborn as sns    
import matplotlib.pyplot as plt    
import math
import scipy.stats    

#X~n(3,7^2
from scipy.stats import norm
x =norm.ppf(0.25,3,7)

#X ~n(0,1^2)
z = norm.ppf(0.25,0,1)
#3 + z*7
#x = 3 +z*7
norm.cdf(5,3,7)

norm.cdf(2/7,0,1)

norm.ppf(0.975,0,1)
norm.ppf(0.025,0,1)



#표준 정규 분포에서 표본을 1000개 뽑은 후 히스토그램 -> pdf 겹쳐서 그리기 z

z = norm.rvs(0,1,1000)
sns.histplot(z,stat="density",color="gray")
z_lin = np.linspace(min(z),max(z),10000)
z_pdf = norm.pdf(z_lin,0,1)
plt.plot(z_lin,z_pdf,color="red")

#x ~(3,2)
x = z*np.sqrt(2)+3
sns.histplot(x,stat="density",color="gray")
x_lin = np.linspace(min(x),max(x),10000)
x_pdf = norm.pdf(x_lin,3,np.sqrt(2))
plt.plot(x_lin,x_pdf,color="blue")
plt.show()
plt.clf()


#정규분포 X ~(5,3^2)
c = norm.rvs(5,3,10000)
sns.histplot(c,stat="density",color="gray")

v= (c - 5)/3
v_lin = np.linspace(min(v),15,10000)
v_pdf = norm.pdf(v_lin,5,3)
plt.plot(v_lin,v_pdf,color="blue")

plt.show()
plt.clf()

'''
1) X 표본을 10개 뽑아서 표본 분산값 계산
2) X에서 표본 1000개 뽑음
3) 1번에서 계산한 s^2 값으로 시그마^2 를 대체한 표준화를 진행 -> Z
4) Z의 히스토그램 그리기 = 표준 정규분포 pdf 확인
'''
#random.random.seed
#1)
x_var = np.var(norm.rvs(5,3,10))
x_std = np.sqrt(x_var)
#2)
x = norm.rvs(5,3,1000) 
#3)
q = (x-5)/x_std
#4)
sns.histplot(q,stat="density",color="gray")
z=norm.rvs(0,1,10000)
z_lin = np.linspace(min(z),max(z),10000)
z_pdf = norm.pdf(z_lin,0,1)
plt.plot(z_lin,z_pdf,color="red")
plt.show()
plt.clf()

#t 분포에 대해서 알아보자!
#X ~ t(df)
#종모양 , 대칭분포, 중심 0
#모수 df : 자유도라고 부름 - 퍼짐을 나타내는 모수
#df 이 작으면 분산 커짐.
from scipy.stats import t

#t.ppf
#t.pdf
#t.cdf
#t.rvs
#자유도가 4인 5분포의 pdf를 그려보세요
plt.clf()
ta=norm.rvs(0,1,10000)
ta_lin = np.linspace(min(ta),max(ta),10000)
ta_pdf = t.pdf(ta_lin,df=1)
plt.plot(ta_lin,ta_pdf,color="red")


z = norm.rvs(0,1,1000)
z_lin = np.linspace(min(z),max(z),10000)
z_pdf = norm.pdf(z_lin,0,1)
plt.plot(z_lin,z_pdf,color="black")

plt.show()

#X ~ ?(mu,sigma^2)
#X bar ~ N(mu,sigma^2/n)
#X bar ~= t(n-1)(x_bar,s^2/n) 자유도가 n-1 인 t 분포

x = norm.rvs(loc=15,scale=3,size=16,random_state = 42)
x
n=len(x)

x_bar=x.mean()
n=len(x)
#모분산을 모를 때,평균에 대한 신뢰구간을 구해보자!
x_bar + t.ppf(0.975,df=n-1) * np.std(x,ddof=1)/np.sqrt(n)
x_bar - t.ppf(0.975,df=n-1) * np.std(x,ddof=1)/np.sqrt(n)

#모분산을 알때:
x_bar + norm.ppf(0.975,loc=0,scale=3) * 3 /np.sqrt(n)
x_bar - norm.ppf(0.975,loc=0,scale=3) * 3 /np.sqrt(n)

