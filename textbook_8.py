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
