from scipy.stats import ttest_1samp
t_statistic, p_value = ttest_1samp(sample, popmean=10, alternative='two-sided')
print("t􀼡statistic:", t_statistic)
print("p􀼡value:", p_value)


import pandas as pd
sample = [9.76, 11.1, 10.7, 10.72, 11.8, 6.15, 10.52,
14.83, 13.03, 16.46, 10.84, 12.45]
gender = ["Female"]*7 + ["Male"]*5
my_tab2 = pd.DataFrame({"score": sample, "gender": gender})
my_tab2

from scipy.stats import ttest_ind
male = my_tab2[my_tab2['gender'] =='Male']
female = my_tab2[my_tab2['gender'] == 'Female']
t_statistic, p_value = ttest_ind(female['score'], male['score'], equal_var=True)
print("t-statistic: ",t_statistic)
print("p-value",p_value)

import numpy as np    
import pandas as pd
tab3 = pd.read_csv('./data/tab3.csv')
tab3_data = tab3.pivot_table(index='id',columns='group',values='score')
tab3_data['score_diff'] = tab3_data['after'] - tab3_data['before']
test3_data = tab3_data[['score_diff']]
test3_data
#
tab1=tab3[["id","score"]]
tab1["id"]=np.arange(1,13)
tab2 = pd.DataFrame({"id" : np.arange(1,13),
                     "score" : tab3["score"]})
tab2["gender"] = np.where(tab2["id"].isin(np.arange(1,8)),"female","male")

"""
tab1 = pd.DataFrame({"id" : np.arange(1,13),
                     "score" : tab3["score"]})
tab2 = tab1.assign(gender=["female"]*7 + ["male"]*5)
"""

from scipy.stats import t
from scipy.stats import norm
#1 표본 t검정 (그룹1개)
#귀무가설 vs. 대립가설
#H0 : mu = 10 vs. Ha mu != 10
#유의수준 5%로 설정
#t 검정을 하는 이유 -> 모분산 모름, 표본 작음
from scipy.stats import ttest_1samp

mean1 = tab1["score"].mean()
n = len(tab1)
score = tab1["score"]
tab1_var = np.var(score)
tab1_sn = np.std(score, ddof=1) / np.sqrt(n)

t_value = (mean1 - 10)/(tab1_sn)

p_value = norm.cdf(mean1, loc=10, scale=tab1_sn)

10 + t.ppf(0.975,df=n-1) * tab1_sn
10 - t.ppf(0.975,df=n-1) * tab1_sn
result = ttest_1samp(score, popmean=10, alternative='two-sided')

t_value = result[0]
p_value = result[1]
len(result)
ci=result.confidence_interval(confidence_level=0.95)
''' 
귀무 가설에 따라 모평균을 10으로 가정하고 표본 평균이 나올 수 있는 확률을 구한 뒤
유의 수준에 따라 가설의 참 여부 파악.
p_value 즉 유의확률이 유의수준 0.05 보다 크니까 귀무 가설을 기각할 수 없다.
귀무 가설이 참일 때(모평균이 10일 때), 11.53이 관찰될 확률이 6.48%이므로,
이것은 우리가 생각하는 보기 힘들다고 판단하는 기준인
0.05(유의수준) 보다 크므로, 귀무가설을 거짓이라 판단하기 힘들다.
유의확률 0.0648이 유의 수준 0.05보다 크므로
귀무가설을 기각하지 못한다.
'''

#2표본 t 검정 (그룹2) 분산 같고, 다를때
#분산 같을 경우 : 독립 2표본 t검정
#분산 다를 경우 : 웰치스 t 검정
##귀무가설 vs 대립가설
##H0 mu_m = mu_f vs. Ha: mu_m >mu_f
##유의수준 1%로 설정, 두 그룹의 분산은 같다고 가정한다.

tab2

#alternative="less"의 의미는 대립가설이
#첫번째 입력그룹의 평균이 두번째 입력 그룹 평균보다 작다.
#고 설정된 경우를 나타냄.
m_tab2 = tab2[tab2['gender'] =='male']
f_tab2 = tab2[tab2['gender'] == 'female']
result = ttest_ind(m_tab2['score'], f_tab2['score'],alternative="greater" ,equal_var=True)
result2 = ttest_ind(m_tab2['score'], f_tab2['score'],alternative="less" ,equal_var=True)
result.statistic
result.pvalue
#유의확률을 의미하는 pvalue의 값이 0.0074~ 로 설정한 유의수준 0.01 보다 작기 때문에
#귀무 가설을 기각한다.



#대응 표본 t 검정(짝지을 수 있는 표본)
##귀무가설 vs 대립가설
##H0:mu_before = mu_after vs. Ha: mu_after > mu_before
##H0:mu_d=0 vs. Ha: mu_d>0
##mu_d = mu_after - mu_before
##유의수준 1퍼센트
##mu_d로 변환해서 1표본 t 검정 가능

tab4 = tab3.copy()
tab4.loc[2,"group"] = "ffff"
tab4 = tab4.pivot_table(index='id',columns='group',values='score')
tab3_data = tab3.pivot_table(index='id',columns='group',values='score')

tab3_data['score_diff'] = tab3_data['after'] - tab3_data['before']
test3_data = tab3_data[['score_diff']]
test3_data
result = ttest_1samp(test3_data['score_diff'], popmean=0, alternative='two-sided')
result.confidence_interval()
result.pvalue
result.statistic
result._alternative
#long_form = tab3_data.reset_index().melt

#연습1
df = pd.DataFrame({"id":[1,2,3],
              "A" :[10,20,30],
              "B" :[40,50,60]})

df_melted = df.melt(id_vars="id",
     value_vars=["A","B"],
     var_name="group",
     value_name="score")

df

df_melted.pivot_table(columns="group",
                      values="score")

#연습2
import seaborn as sns
tips = sns.load_dataset("tips")
#tips.pivot_table(index="id",columns="day",values="tip")
index_list= list(tips.columns.delete(4))
tips.reset_index(drop=False).pivot_table(index=["index"],columns="day",values="tip").reset_index()
#요일별로 펼치고 싶은 경우

tab3.melt(id_vars="id",
     value_var=["A","B"],
     var_name="group,
     value_name="score")


# mu_d에 대응하는 표본으로 변환
tab3_data = tab3.pivot_table(index='id', 
                             columns='group',
                             values='score').reset_index()

tab3_data['score_diff'] = tab3_data['after'] - tab3_data['before']
test3_data = tab3_data[['score_diff']]
test3_data

from scipy.stats import ttest_1samp

result = ttest_1samp(test3_data["score_diff"], popmean=0, alternative='greater')
t_value=result[0] # t 검정통계량
p_value=result[1] # 유의확률 (p-value)
t_value; p_value

long_form = tab3_data.reset_index().melt(id_vars='id', value_vars=['before', 'after'], var_name='group', value_name='score')
