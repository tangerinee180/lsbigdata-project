import numpy as np
import math

a = np.array([79.1, 68.8, 62.0, 74.4, 71.0, 60.6, 98.5, 86.4, 73.0, 40.8, 61.2, 68.7, 61.6, 67.7, 61.7, 66.8])
a_mean = a.mean()
#x바 = a_mean
#n = 16
#sigma = 6
#알파  == 신뢰구간에서 구함(1-신뢰구간 = 알파 )
#Z(a/2) = norm.ppf(0.95,0,scale=1)/np.sqrt(16)*6
len(x)

x_95 = a_mean + norm.ppf(0.95,0,scale=1)/np.sqrt(16)*6
y_95 = a_mean - norm.ppf(0.95,0,scale=1)/np.sqrt(16)*6

norm.ppf(0.95,0,scale=1)
print(y_95,x_95)

#X ~ n(3,5^2)
#x1,x2,x3,x4,'''',xn
#E[x^2]
x = norm.rvs(loc = 3,scale =5,size= 10000)

x2 = x*x

x2.mean()

#몬테 카를로 적분 : 확률변수의 기댓값을 구할 떄 (X^5)같이 구하기 어려운, 
#표본을 많이 뽑은 후 원하는 형태로 변형 후 평균은 계산해서 기대값을
#구하는 방법

#X ~ N(3,5^2)
#VAR(X) = 5^2
np.random.seed(20240729)
#표본 10만개 추출후 s^2 구하기
x = norm.rvs(loc=3,scale=5,size=100000)
x_mean = x.mean()
sum((x-x_mean)**2)
s2 = 1/(100000-1) * (sum((x-x_mean)**2))
s3 = 1/(100000) * (sum((x-x_mean)**2))
np.var(x,ddof=1)#n-1로 나누기(표본 분산)-위에가 정의랑 똑같음
#np.var(x,ddof=0)#n으로 나눈 값
s2,s3

x = norm.rvs(loc=3,scale=5,size=6)
np.var(x,ddof=1)
np.var(x,ddof=0)


x = norm.rvs(loc=3,scale=np.sqrt(7),size=20)
x_mean = x.mean()
sum((x-x_mean)**2)
s_2 = 1/(100000-1) * (sum((x-x_mean)**2))
k_2 = 1/(100000) * (sum((x-x_mean)**2))



표본 분산 계산 시 왜 n-1로 나누는지 알아보도록 하겠습니다.

균일분포 (3, 7)에서 20개의 표본을 뽑아서 분산을 2가지 방법으로 추정해보세요.

n-1로 나눈 것을 s_2, n으로 나눈 것을 k_2로 정의하고, s_2의 분포와 k_2의 분포를 그려주세요! (10000개 사용)
각 분포 그래프에 모분산의 위치에 녹색 막대를 그려주세요.
결과를 살펴보고, 왜 n-1로 나눈 것을 분산을 추정하는 지표로 사용하는 것이 타당한지 써주세요!
