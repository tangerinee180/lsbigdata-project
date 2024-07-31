import pandas as pd
import numpy as np
import seaborn as sns    
import matplotlib.pyplot as plt    
import math
from scipy.stats import norm
raw_welfare = pd.read_spss("data/Koweps_hpwc14_2019_beta2.sav")

welfare = raw_welfare.copy()

welfare.shape
welfare.describe()

welfare.rename(columns = {
        "h14_g3"    : "sex",
        "h14_g4"    : "birth",
        "h14_g10"   : "marriage_type",
        "h14_g11"   : "religion",
        "p1402_8aq1": "income",
        "h14_eco9"  : "code_job",
        "h14_reg7"  : "code_region"},inplace = True)

welfare = welfare[["sex","birth","marriage_type",\
"religion","income","code_job","code_region"]]

welfare.shape

welfare["sex"].dtypes
welfare.loc[0,"sex"] = 2.0
welfare["sex"].value_counts()



welfare["sex"] = np.where(welfare["sex"]==1,"male","female")
welfare["sex"].value_counts()

welfare["income"].describe()
welfare["income"].isna().sum()
welfare["income"].sum()
sex_income = welfare.dropna(subset="income").groupby("sex",as_index=False).agg(mean_income=("income","mean"))

sex_income

sns.barplot(data=sex_income,x="sex",y="mean_income",hue='sex')
sns.lineplot(data)
plt.show()
plt.clf()

#숙제: 위 그래프에서 각 성별 95% 신뢰 구간 계산 후 그리기

temp = welfare.dropna(subset="income").groupby("sex",as_index=False).agg(mean_income=("income","mean"),
                                                                              var_income =("income",'var'),
                                                                              len_income =("income","count"))

temp["left_ci"]= temp['mean_income'] - norm.ppf(0.975,0,1)*np.sqrt(temp['var_income']/(temp["len_income"]))
temp["right_ci"]= temp['mean_income'] + norm.ppf(0.975,0,1)*np.sqrt(temp['var_income']/(temp["len_income"]))
temp

sns.barplot(data=sex_income,x="sex",y="mean_income",hue='sex')
plt.plot([0, 0], [temp.iloc[0]["left_ci"], temp.iloc[0]["right_ci"]], color='black', linewidth=2)
plt.plot([1, 1], [temp.iloc[1]["left_ci"], temp.iloc[1]["right_ci"]], color='black', linewidth=2)
plt.show()
plt.clf()



###
welfare["birth"].describe()
sns.histplot(data=welfare,x="birth")
plt.show()
plt.clf()




welfare["birth"].isna().sum()
welfare = welfare.assign(age = 2019 - welfare["birth"] +1)
sns.histplot(data=welfare,x="age")
plt.show()
plt.clf()

age_income =welfare.dropna(subset="income").groupby("age",as_index=False).agg(mean_income=("income","mean"))
sns.lineplot(data=age_income,x="age",y="mean_income")

age_income =welfare.dropna(subset="income").groupby("age",as_index=False).agg(mean_income=("income","mean"))

age_income
#나이별 income 칼럼 na 개수
"welfare.groupby("age", as_index=False).agg(lambda x: x.isna().sum())[["age","income"]]"

my_df = welfare.assign(income_na = welfare["income"].isna()).groupby("age",as_index=False).agg(na = ("income_na","sum"))



sns.lineplot(data=my_df,x="age",y="na")
plt.show()
plt.clf()


welfare["age"].head()

welfare = welfare.assign(ageg = np.where(welfare["age"]<30,"young",np.where(welfare["age"]<=59,"middle",'old')))
welfare["ageg"].value_counts()

sns.countplot(data=welfare,x="ageg",hue="ageg")
plt.show()
plt.clf()

ageg_income = welfare.groupby("ageg",as_index=False).agg(mean_income=("income","mean"))

sns.barplot(data=ageg_income,x="ageg",y="mean_income",hue="ageg")
plt.show()
plt.clf()

sns.barplot(data=ageg_income,x="ageg",y="mean_income",hue="ageg",\
order = ["young","middle","old"])
plt.show()
plt.clf()



cut_lim = [0] + [i*10 + 9 for i in range(0,11)]
cut_lim = [0, 9, 19, 29, 39, 49, 59, 69, 79, 89, 99,109]
#group_name = ['아기', '십대', '이십대', '삼십대', '사십대', '오십대', '육십대', '칠십대',\
#'팔십대', '구십대','노인']
group_name2 = ((np.arange(12)*10).astype(str) + "대")
group_name2[0] = "아기"
welfare['age_group'] = pd.cut(welfare['age'], bins=cut_lim, labels=group_name2)

welfare['age_group']

age_income = welfare.groupby("age_group",as_index=False)\
.agg(mean_income=("income","mean"))

sns.barplot(data=age_income,x="age_group",y="mean_income")
plt.show()
plt.clf()

welfare["age_group"] = welfare["age_group"].astype('object')
#sex_age_income = welfare.dropna(subset=["income"]).groupby(["ageg","sex"],as_index=False).agg(mean_income=("income","mean"))
#판다스 데이터 프레임을 다룰 때 , 변수의 타입이 
#카테고리로 설정되어 있는 경우, groupby+agg 콤보
#안먹힘 그래서 object type으로 바꿔주고 수행
sex_age_income2 = welfare.groupby(["age_group","sex"],as_index=False).agg(mean_income=("income","mean")).dropna(subset="mean_income")

sex_age_income2.reset_index(drop=True,inplace=True)
sex_age_income2

sns.barplot(data=sex_age_income2,x="age_group",y="mean_income",hue="sex")
plt.show()
plt.clf()

'''# 함수 짜보기?
def custom_mean(series,dropna=True):
    if dropna:
        return print(series,"hi")
    else :
        return print(series,"bye")
'''

sex_age_income = welfare.dropna(subset=["income"])\
.groupby(["age_group","sex"],as_index=False).agg(mean_income=("income","mean"),\
percent96_income=("income", lambda x: x.quantile(0.96)))


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




