# y = 2x +3 그리기

import pandas as pd
import numpy as np
import seaborn as sns    
import matplotlib.pyplot as plt    
import math
import scipy.stats
from scipy.stats import norm
import sklearn.linear_model
from scipy.optimize import minimize    
from sklearn.linear_model import LinearRegression
from scipy.stats import t

#np.random.seed(20240805)
x = np.linspace(0,100,400)
y = x*2+3

epsilon_i = norm.rvs(loc=0,scale=100,size=20)
obs_x = np.random.choice(np.arange(100),20)
obs_y = 2 * obs_x  + 3 + epsilon_i

plt.plot(x,y,label="y = 2x+3",color="black")
plt.scatter(obs_x,obs_y,color="blue",s=3)

#빨강색 선 그리기

model = LinearRegression()
obs_x = obs_x.reshape(-1,1)
model.fit(obs_x,obs_y)

a1 = model.coef_
b1 = model.intercept_


plt.plot(x,x*a1 + b1,color="red")
plt.show()

plt.clf()

#!pip install statsmodels
import statsmodels.api as sm

obs_x = sm.add_constant(obs_x)
model = sm.OLS(obs_y,obs_x).fit()
print(model.summary())


#8.79/np.sqrt(20)
#시그마 8.79
 18 - 1.96/np.sqrt(20)*8.79
#p 밸류 = 유의 확률(p밸류가 작을 수록 영가설을 반박할 확률이 커진다.)
# 귀무 가설(영가설) vs 대립 가설
# 귀무 가설이란 내가 반박해야하는 가설 
# 대립 가설이란 내가 주장해야하는 가설
#검사의 경우 피고인은 유죄다 => 대립가설
c = 1 - norm.cdf(18,loc=10,scale=8.79/np.sqrt(20))

'''#N ~(10,1.96^2)
#x1,``````,xn       모 표준편차 시그마 제곱



(U0 - mu)/np.sqrt

'''
'''
표준편차 시그마 모를때
귀무가설 vs 대립가설
t = (x바 - u0)/(s/np.sqrt(n))
주어진 t로 유의 확률 계산(t분포 n-1 활용)
유의 수준과 비교하여 귀무가설 기각할 지 결정

'''
'''
신형 자동차의 에너지 소비효율 등급
슬통 자동자는 매해 출시되는 신형 자동차의 에너지 소비효율 등급을 1등급으로 유지하고 있다. 22
년 개발된 신형 모델이 한국 자동차 평가원에서 설정한 에너지 소비 효율등급 1등급을 받을 수 있을지
검정하려한다. 평가원에 따르면 1등급의 기준은 평균 복합 에너지 소비효율이 16.0 이상인 경우 부여
한다고 한다.
다음은 신형 자동차 15대의 복합 에너지소비효율 측정한 결과이다.
15.078, 15.752, 15.549, 15.56, 16.098, 13.277, 15.462, 16.116, 15.214, 16.93, 14.118, 14.927,
15.382, 16.709, 16.804
표본에 의하여 판단해볼때, 현대자동차의 신형 모델은 에너지 효율 1등급으로 판단할 수 있을지
판단해보시오. (유의수준 1%로 설정)
1. 검정을 위한 가설을 명확하게 서술하시오.
2. 검정통계량 계산하시오.
3. p‑value을 구하세요.
4. 현대자동차의 신형 모델의 평균 복합 에너지 소비효율에 대하여 95% 신뢰구간을 구해보세요.
'''

#1등급의 기준은 평균 복합 에너지 소비효율이 16.0
#1. H0 : mu>=16 , Ha: mu1<16
a = np.array([15.078, 15.752, 15.549, 15.56, 16.098, 13.277, 15.462, 16.116, 15.214, 16.93, 14.118, 14.927,
15.382, 16.709, 16.804])
a_mean = a.mean()
n = len(a)
a_var = np.var(a)
a_sn = np.std(a, ddof=1) / np.sqrt(15)

#2. 
t_value = (a_mean - 16)/(np.std(a, ddof=1) / np.sqrt(15))

#p_value
p_value = norm.cdf(a_mean, loc=16, scale=(x_std / np.sqrt(15)))


16 + t.ppf(0.975,df=n-1) * np.std(a,ddof=1)/np.sqrt(n)
16 - t.ppf(0.975,df=n-1) * np.std(a,ddof=1)/np.sqrt(n)
