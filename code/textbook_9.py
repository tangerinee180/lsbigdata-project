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
#group_name = ['아기', '십대', '이십대', '삼십대', '사십대', '오십대', '육십대', '칠십대',\
#'팔십대', '구십대','노인']
group_name2 = ((np.arange(11)*10).astype(str) + "대")
group_name2[0] = "아기"
welfare['age_group'] = pd.cut(welfare['age'], bins=cut_lim, labels=group_name2)


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

##참고
welfare.dropna(subset ="income")\
                .groupby("sex",as_index=False)[["income"]].agg(["mean","std"])



sns.barplot(data=sex_age_income,x="age_group",y="percent96_income",hue="sex")
plt.show()
plt.clf()

#9-6장

import pandas as pd
import numpy as np
import seaborn as sns    
import matplotlib.pyplot as plt    
import math
import scipy.stats

welfare["code_job"]
welfare["code_job"].value_counts()

list_job = pd.read_excel("data/Koweps_Codebook_2019.xlsx",sheet_name="직종코드")
list_job.head()


welfare = welfare.merge(list_job,how="left",on="code_job")
welfare.dropna(subset=["job","income"])[["income","job"]]

job_income = welfare.dropna(subset=["job","income"])\
.query("sex=='female'")\
.groupby("job",as_index=False).agg(mean_income=("income","mean"))

job_income.head()

top10 = job_income.sort_values("mean_income",ascending=False).head(10)

plt.rcParams.update({"font.family":"Malgun Gothic"})

sns.barplot(data = top10, x= "mean_income",y="job",hue="job")
plt.show()
plt.clf()




#normalize 가 핵심
df = welfare.query("marriage_type!=5").groupby("religion",as_index=False\
.["marriage_type"].value_counts(normalize=True)\
df.query("marriage_type == 1")


df.groupby("job",as_index=False).agg(proportion=df["proportion"]*100).round(1)

df

