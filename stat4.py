from scipy.stats import uniform
import numpy as np    
import seaborn as sns

#X ~ U(a,b) 균일분포 U의 모수 a는 시작점, b는 길이
#시작점이 0 이고 길이가 4 인 uniform 함수
uniform.rvs(loc=2,scale=4,size=1)

'''
uniform.pdf(x,loc=0,scale=1)
uniform.cdf(x,loc=0,scale=1)
uniform.ppf(x,loc=0,scale=1)
'''
#분산 구하는 함수
uniform.var(loc=2,scale=4)/n

uniform.expect(loc=2,scale=4)

x_lin = np.linspace(2,6,100)
x_values = uniform.pdf(a_lin,loc=2,scale=4)

plt.plot(x_lin,x_values,color="red",linewidth=2)

plt.show()
plt.clf()


uniform.cdf(3.25,2,4)

uniform.cdf(8.39,2,4)- uniform.cdf(5,2,4)

uniform.ppf(0.93,2,4)

#표본 20개 뽑아서 표본 평균 구하기
uniform.rvs(loc=2,scale=4,size=20,random_state = 42).mean()
a = uniform.rvs(loc=2,scale=4,size=20000,random_state = 42)
a = a.reshape(1000,-1)
a.mean()
blue_x = a.mean(axis=1)
sns.histplot(blue_x,stat="density")
plt.show()
plt.clf()


#X bar ~ N(4,uniform.var(loc=2,scale=4)**2/n)
from scipy.stats import norm
import numpy as np
x = uniform.rvs(loc=2,scale=6,size=1000)
xmin ,xmax = [min(blue_x),max(blue_x)]
x_values = np.linspace(xmin,xmax,100)
pdf_values = norm.pdf(x_values,loc=4,scale=np.sqrt(uniform.var(loc=2,scale=4)**2/20))
plt.plot(x_values,pdf_values,color="red",linewidth=2)
sns.histplot(blue_x,stat = 'density')
plt.show()
plt.clf()

#신뢰도 99% 구간 구하기 a b
norm.ppf(0.005,4,scale=np.sqrt(uniform.var(loc=2,scale=4)/20))
norm.ppf(0.995,4,scale=np.sqrt(uniform.var(loc=2,scale=4)/20))

#기대값 표현
plt.axvline(x=4,color="green",linewidth=2)

#표본 평균 점 찍기
x_1 = uniform.rvs(loc=2,scale=4,size=20).mean()
plt.scatter(x_1,0.002,color="blue",zorder=100,s=10)
# 1.96 = norm.ppf(0.975,0,1)
a = x_1+ 0.665
b = x_1 - 0.665
plt.axvline(x=a, color="blue", linewidth=1, linestyle="--")
plt.axvline(x=b, color="blue", linewidth=1, linestyle="--")

x_values = np.linspace(3,5,100)
pdf_values = norm.pdf(x_values,loc=4,scale=np.sqrt(uniform.var(loc=2,scale=4)**2/20))
plt.plot(x_values,pdf_values,color="red",linewidth=2)
plt.show()
plt.clf()

0.665/np.sqrt(uniform.var(loc=2,scale=4)**2/20)
