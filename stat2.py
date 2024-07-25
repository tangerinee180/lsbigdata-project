import numpy as np
import matplotlib.pyplot as plt



np.arange(33).sum()/33
a = np.unique((np.arange(33)-16)**2)
(a[1:]*2).sum()/33

(np.arange(33)*np.arange(33)).sum()/33
(np.arange(33)*np.arange(33)).sum()/33


#Var[x] = E[X^2] - (E[x])^2
(np.arange(33)*np.arange(33)).sum()/33

#X = [0,1,2,3]

X = np.arange(4)
px = np.array([1,2,2,1])/6
X*X
Ex = (X*px).sum()
E_x2 = (X*X*px).sum()
result = (E_x2 - Ex**2).sum()
sum((X-Ex)**2 * px)






px = np.concatenate((np.arange(1,51), np.arange(49,0,-1)))/2500
X = np.arange(99)
ex = (X*px).sum()
e_x2 = (X*X*px).sum()
varx = e_x2 - ex**2
list(range(50,-1,-1))
a = list(range(1, 51))
a.extend(list(range(49,0,-1)))
print(a)
#var 성질 곱해진 상수는 제곱해서 나오고,더해진 상수는 0처리
X = np.arange(4)*2
px = np.array([1,2,2,1])/6
X*X
Ex = (X*px).sum()
E_x2 = (X*X*px).sum()
result = (E_x2 - Ex**2).sum()
sum((X-Ex)**2 * px)

##분산은 시그마**2 
sd = 9.52
sd1 = np.sqrt(40)
np.sqrt(sd**2/10)
def what_is_sd(sd,n):
    return np.sqrt(sd**2/n)
#표본 평균 확률 변수 x바 는 모집단의 평균을 평균으로 가지고
#, 시그마 제곱을 표본 크기로 나눈 값을 분산으로 가지는 정규 분포를 따른다.

0.49    0.58      0.09
  0        1         2
 
p =[0.49,0.58,0.09]
x =[0,1,2]

from scipy.stats import binom
from scipy.stats import bernoulli
import math
import numpy as np
#확률질량함수 pmf
#확률 변수가 갖는 값에 해당하는 확률을 저장하고 있는 함수
# P(X=1)
bernoulli.pmf(1,0.3)
# P(X=0)
bernoulli.pmf(0,0.3)

#이항분포 X ~ P(X = k |n,p)
# n : 베르누이 확률 변수 더한 갯수
# p : 1이 나올 확률
# binom.pmf(k,n,p)

binom.pmf(0,n=2,p=0.3)
binom.pmf(1,n=2,p=0.3)
binom.pmf(2,n=2,p=0.3)

#X ~ B(n,p)

#list comp
result_lc = [binom.pmf(x,n=30,p=0.3) for x in range(31) ]
result_lc


#numpy
result_np = binom.pmf(np.arange(31),n=30,p=0.3)
result_np

a = "1,2%d,3,4"%6
a[3]
a[4]

def fact(n):
    if n in [0,1] :
        return 1
    else :
        return n * fact(n-1)
    
print(fact(54))
math.factorial(54)/math.factorial(26)*math.factorial(28)
math.log(fact(54)/fact(26)*fact(28))
#np.cumprod(np.arange(1,55))[-1]
#ln
log(a * b)

math.log(math.factorial(54))
sum(np.log((np.arange(1,55))))

sum(np.log((np.arange(1,55)))) - sum(np.log((np.arange(1,27)))) -sum(np. log((np.arange(1,29))))
a = np.log((np.arange(1,55)))) - sum(np.log((np.arange(1,27)))) -sum(np. log((np.arange(1,29))))
np.exp()

math.comb(2,0) * 0.3**0 * (1-0.3)**2
math.comb(2,1) * 0.3**1 * (1-0.3)**1
math.comb(2,2) * 0.3**2 * (1-0.3)**0

#P(x=k) = nCk * p**k * (1-p)**(n-k)
# pmf (확률 질량 함수) probability mass function
binom.pmf(0,2,0.3)
binom.pmf(1,2,0.3)
binom.pmf(2,2,0.3)

#X ~ B(n=10,p=0.36)
#P(X=4)

result2 = binom.pmf(np.arange(0,5),10,0.36)
sum(result2)

result3 = binom.pmf(np.arange(3,9),10,0.36)
sum(result3)

#X ~ B(30,0.2)
#X <4 ,25<=X
a = sum(binom.pmf(np.arange(0,4),30,0.2))+sum(binom.pmf(np.arange(25,31),30,0.2))
b = 1 - sum(binom.pmf(np.arange(4,25),30,0.2))

#rvs 함수 (random variates sample)
#표본 추출 함수
bernoulli.rvs(p=0.3,size=10)

binom.rvs(n=30,p=0.26,size=30)

X ~ B(30,0.26)
Ex = 30*0.26 #E(X)=np
sum(binom.pmf(np.arange(0,31),30,0.26))
from scipy.stats import binom
from scipy.stats import bernoulli
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
PX =binom.pmf(np.arange(0,31),30,0.26)
X = np.arange(0,31)
plt.bar(X,PX)
plt.show()
df = pd.DataFrame({"X_values" : X,"P(X)":PX})
plt.bar(data = df , x = "X_values",y="P(X)")

# cdf : cumulative dist. function
# (누적확률분포 함수)
#F_X(x) = P(X<=x) // pdf => 연속확률변수
qx =binom.pmf(np.arange(0,5),30,0.26)
P
aa = binom.cdf(18,n=30,p=0.26) - binom.cdf(4,n=30,p=.26)
aa

paa = binom.cdf(19,n=30,p=0.26) - binom.cdf(13,n=30,p=0.26)
paa



x= np.arange(31)
prob_x = binom.pmf(x,n=30,p=0.3)
sns.barplot(prob_x,color="salmon")

x_1 = binom.rvs(n=30,p=0.26,size=1)
x_1
plt.scatter(x_1,0.002,color="red",zorder=100,s=5)
plt.axvline(7.8,color="blue",linestyle='--',linewidth=2)
plt.show()
plt.clf()


x= np.arange(31)
prob_x = binom.pmf(x,n=30,p=0.3)
sns.barplot(prob_x,color="salmon")

x_1 = binom.rvs(n=30,p=0.26,size=3)
x_1
plt.scatter(x_1,np.repeat(0.002,3),color="red",zorder=100,s=5)
plt.axvline(x=7.8,color="blue",linestyle='--',linewidth=2)
plt.show()
plt.clf()

    

x= np.arange(31)
prob_x = binom.pmf(x,n=30,p=0.3)
sns.barplot(prob_x,color="salmon")

x_1 = binom.rvs(n=30,p=0.26,size=10)
x_1
plt.scatter(x_1,np.repeat(0.002,10),color="red",zorder=100,s=5)
plt.axvline(x=7.8,color="blue",linestyle='--',linewidth=2)
plt.show()
plt.clf()

#pmf : x라는 값이 나오는 확률 구해줌
binom.pmf(x,n=30,p=0.3)
#rvs : 사이즈 x개의 표본 만들어줌(x1,x2,x3 가 30개)
binom.rvs(n=30,p=0.26,size=x)
#ppf : 왼쪽 끝에서 부터 확률이 0.7이 되는 값 찾아줌
binom.ppf(x,n=30,p=0.26)
#cdf : 왼쪽 끝에서부터 입력한 값까지의 확률의 합
binom.cdf(x,30,0.26)
#pdf 

#정규분포 loc = 뮤 , scale = 시그마
#모수란? 함수의 모양을 결정하는 파라미터들
from scipy.stats import norm

from scipy.stats import binom
from scipy.stats import bernoulli
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
norm.pdf(5,loc = 3,scale = 4)
k = np.linspace(-3,3,100)
y = norm.pdf(np.linspace(-3,3,100),loc=0,scale=1)
plt.plot(k,y,color='black')
plt.show()
plt.clf()


## mu (loc) : 분포의 중심 결정하는 모수 = E(X)

norm.pdf(0,loc = 0,scale = 1)

k = np.linspace(-3,3,100)
y = norm.pdf(np.linspace(-3,3,100),loc=2,scale=1)
plt.plot(k,y,color='black')
plt.show()
plt.clf()


## sigma (scale) : 표준편차 분포의 퍼짐을 결정하는 모수

norm.pdf(5,loc = 3,scale = 4)

k = np.linspace(-3,3,100)
y = norm.pdf(k,loc=0,scale=1)
y2 = norm.pdf(k,loc=0,scale=2)
y3 = norm.pdf(k,loc=0,scale=0.5)
plt.plot(k,y,color='black')
plt.plot(k,y2,color='red')
plt.plot(k,y3,color='blue')

plt.show()
plt.clf()

norm.cdf(0,0,1)
norm.cdf(2,0,1)
norm.cdf(5,0,1)
norm.cdf(100,0,1)
#-2<X<0.54
norm.cdf(0.54,0,1) - norm.cdf(-2,0,1)

#
1 - (norm.cdf(3,0,1) - norm.cdf(1,0,1))

#X ~ N(3,5**2) , P(3<x<5)
norm.cdf(5,3,5) - norm.cdf(3,3,5)

#위 확률 변수에서 표본 100개 뽑아보자!
norm.rvs(loc=3,scale=5,size=100)

x = norm.rvs(loc=3,scale=5,size=1000)
sum((x>3)&(x<5))

#평균 0 , 표준편차 1, 표본 1000개 0보다 작은 비율 확인
y = norm.rvs(loc=0,scale=1,size=1000)
np.mean(y<0)


x = norm.rvs(loc=3,scale=2,size=1000)
x
xmin,xmax = (x.min(),x.max())
x_values = np.linspace(xmin,xmax,100)
pdf_values = norm.pdf(x_values,loc=3,scale=2)
plt.plot(x_values,pdf_values,color="red",linewidth=2)


sns.histplot(x,stat = 'density')
plt.show()
plt.clf()

