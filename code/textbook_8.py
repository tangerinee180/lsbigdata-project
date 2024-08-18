import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt    
import plotly

mpg = pd.read_csv("data/mpg.csv")
mpg.shape
mpg


sns.scatterplot(data=mpg,
                x="displ",\
                y="hwy",\
                hue="drv")\
                .set(xlim=[3,6],ylim=[10,30])
plt.show()

#막대 그래프
df_mpg = mpg.groupby("drv",as_index=False)\
            .agg(mean_hwy=("hwy",'mean'))
#data frame 임
df_mpg
!pip install plotly
sns.barplot(data=df_mpg.sort_values("mean_hwy",ascending=True\
,x="drv",y="mean_hwy",hue="drv")
plt.show()

df_mpg2 = mpg.groupby("drv",as_index=False).agg(n=("drv","count"))
sns.barplot(data=df_mpg2,x="drv",y="n")
plt.show()
sns.countplot(data = mpg , x ="drv")
sns.countplot(data=mpg,x='drv',order["4","f","r"])

mpg["drv"].unique()


plt.clf()




#### 선그래프

economics = pd.read_csv("data/economics.csv")
ecoframe = economics.copy()

ecoframe.info()
ecoframe.columns

sns.lineplot(data=ecoframe,x="date",y="unemploy")
plt.show()
plt.clf()

ecoframe["date2"] = pd.to_datetime(ecoframe["date"])
ecoframe.info()

ecoframe["year"] = ecoframe["date2"].dt.year
ecoframe["date2"].dt.month
ecoframe["date2"].dt.day
ecoframe["date2"].dt.month_name()
ecoframe["date2"].dt.quarter
ecoframe["quarter"] = ecoframe["date2"].dt.quarter
ecoframe["date2"].dt.day_name()

ecoframe["date2"].dt.is_leap_year #윤년체크

sns.lineplot(data=ecoframe,x="year",y='psavert',errorbar=None)
sns.lineplot(data=ecoframe,x="year",y='unemploy',errorbar=None)
plt.show()
plt.clf()

#날짜 계산하기
ecoframe["date2"] + pd.DateOffset(month=1)

ecoframe["month"] = ecoframe["date2"].dt.month
frame1 = ecoframe.query("year == 2014")
sns.lineplot(data = frame1,x="month",y="psavert")
norm.ppf(0.975,0,1)
C = ecoframe.groupby("year",as_index=False).agg(mon_mean=("unemploy","mean")\
                                ,mon_std=("unemploy","std"),mon_count=("unemploy","count"))
C["left_ci"]= C['mon_mean'] - norm.ppf(0.975,0,1)*C['mon_std']/np.sqrt(C["mon_count"])
C["right_ci"]= C['mon_mean'] + norm.ppf(0.975,0,1)*C['mon_std']/np.sqrt(C["mon_count"])



def cal_std(values):
    mean = np.mean(values)
    var = np.sum((values - mean) ** 2) / (len(values) - 1)
    return np.sqrt(var)

year_std = ecoframe.groupby('year')['unemploy'].apply(cal_std).reset_index()
year_std.columns = ['year', 'mon_std']

CF = C

x= C["year"]
y =C["mon_mean"]
plt.plot(x,y,color="black")
plt.scatter(x,C['left_ci'],color="blue",s=1)
plt.scatter(x,C['right_ci'],color="red",s=1)

plt.show()
plt.clf()
sns.lineplot(data=CF,x="year",y="mon_mean")#errorbar=None
plt.show()

# 
house_train = pd.read_csv("data/train.csv")
house_train = house_train[["Id","YearBuilt","SalePrice"]]
house_train.info()
house_mean = house_train.groupby("YearBuilt",as_index=False).agg(price_mean=("SalePrice","mean"))
house_train["SalePrice"].mean()



house_test = pd.read_csv("data/test.csv")

house_test = pd.merge(house_test,house_mean,how="left",on="YearBuilt")

house_test.rename(columns={"price_mean":"SalePrice"},inplace=True)
sum(house_test["SalePrice"].isna())
#loc 함수 쓰는 법
house_test.loc[house_test["SalePrice"].isna()]['SalePrice']
house_test["SalePrice"]=house_test["SalePrice"].fillna(house_train["SalePrice"].mean())

#house_test["SalePrice"] = np.nan_to_num(house_test["SalePrice"],house_test['price_mean'].mean())
#house_test[house_test["price_mean"]==house_test['price_mean'].mean()]

#sub 데이터 불러오기
sub_df = pd.read_csv("data/sample_submission.csv")
sub_df

#SalePrice 바꿔치기
sub_df["SalePrice"] = house_test["SalePrice"]

sub_df.to_csv("data/submission.csv",index=False)


