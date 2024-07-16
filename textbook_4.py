import pandas as pd
import numpy as np    


#df_exam = pd.read_excel("data/excel_exam.xlsx",sheet_name="Sheet2" or 2)
df_exam = pd.read_excel("data/excel_exam.xlsx")
df_exam

len(df_exam)
df_exam.size
df_exam.shape
df_exam.describe
df_exam.info
df_exam.tail()
df_exam.head()

?pd.read_excel

df_exam["total"] = df_exam["math"] + df_exam["english"] + df_exam["science"]

df_exam["mean"] = round(df_exam["total"]/3,1)
?round
df_exam

df_exam[df_exam["math"]>50][df_exam["english"]>50]

df_exam[(df_exam["math"]>50) & (df_exam["english"]>50)]

df_exam[(df_exam["math"]>sum(df_exam["math"])/len(df_exam))&
(df_exam["english"]< sum(df_exam["english"])/len(df_exam))]

df_exam["nclass"]==3
df_nc3 = df_exam[df_exam["nclass"]==3]
df_nc3[["math","english","science"]]
df_nc3[2:4]
df_nc3.iloc[2]

a=np.array([4,2,5,3,6])
a[3]

df_exam[1:16:2]

df_exam.sort_values("math",ascending=False)

df_exam.sort_values(["nclass","math"],ascending=[True,False])

np.where(df_exam["nclass"]==3,"good","bad")
#두개 반환 값 차이 tuple 과 numpy.ndarray
np.where(a>3)
np.where(a>3,"Up","Down")

type(np.where(a>3))
type(np.where(a>3,"Up","Down"))

df_exam["UpDown"] = np.where(df_exam["math"]>50,"Up","Down")
df_exam

df_exam["test"] = np.where(df_exam["mean"]>70,"Pass","Fail")

df = pd.read_csv("data/exam.csv")

df.describe
df.columns
df.sort_values("math",ascending=False)
df.sort_values(["math","english"],ascending=[False,False])



exam = pd.read_csv("data/exam.csv")
exam.assign(test = np.where(exam['science']>=60,"pass","fail"))
exam.assign(total = lambda x : x["math"] + x["science"] + x["english"]).sort_values("math")
long_name = pd.read_csv("data/exam.csv")
long_name = long_name.assign(total = long_name["math"] +long_name["english"]+long_name["science"],
mean = lambda x : x["total"]/3
)
long_name
long_name["total"] = long_name["math"] +long_name["english"]+long_name["science"]

df = pd.read_csv("data/exam.csv")
df.agg(mean_math=("math","mean"))
df.groupby("nclass").agg(mean_math=("math","mean"))
df.groupby("nclass",as_index = False).agg(mean_math = ("math","mean"))
#mean(),std()   ,sum(), median(),min(), max(), count()
#평균   표준편차 합계   중앙값  최소값 최대값 빈도(개수)

df.groupby("nclass").mean()
df.groupby("nclass").agg(mean_math =("math","mean"))
df.drop(columns = ["math","english"])
df["nclass"]
df[["nclass"]]
df[["id","nclass"]]
df
df.query("nclass == 1")\
[["math","english"]].head()

#정렬하기
exam = pd.read_csv("data/exam.csv")
exam.sort_values("math")

exam.sort_values("math",ascending=False)
exam.sort_values(["math","english"],ascending=[True,False])

mpg = pd.read_csv("data/mpg.csv")
mpg.groupby(["manufacturer",'drv']).agg(mean_cty = ("cty","mean"))
mpg.query("manufacturer == 'audi'").groupby(["drv"]).agg(n = ('drv','count'))

# 요약을 하는 .agg()
exam2 = long_name
exam2.agg(mean_math = ("math","mean"))
exam2.groupby("nclass")
exam2.groupby("nclass").agg(mean_math = ("math","mean"))
exam2.groupby("nclass").agg(mean_math = ("math",'mean'),
mean_sci = ("science",'mean'),mean_eng = ("english",'mean'))

mpg_raw = pd.read_csv("data/mpg.csv")
mpg2 = mpg_raw
mpg2.columns
mpg2.query("category == 'suv'").assign(cty = (mpg2["hwy"]+mpg2["cty"])/2).groupby("manufacturer").agg(mean_two = ("cty","mean")).sort_values("mean_two",ascending=False).head()
