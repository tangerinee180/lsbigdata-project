import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

#column, variable, row, case
df = pd.DataFrame({'name'  : ['김김','나나','박박','이이'],
'eng'  : [90,80,60,70],
'math' : [50,60,100,20]})
  
df
df['eng']
sum(df['eng'])
min(df['eng'])

df2 = pd.DataFrame({'fruit' : ['apple','strawberry','watermelon'],'price':[1800,1500,3000],'sales':[24,38,13]})
df2

print(sum(df2["price"]/4))

print(sum(df2["sales"]/len(df2)))

df_exam = pd.read_excel("excel_exam.xlsx")
df_exam

sum(df_exam["math"])/len(df_exam)
sum(df_exam["math"])/len(df_exam["id"])

df_exam_novar = pd.read_excel('excel_exam_novar.xlsx',header = None)
df_exam_novar

df_exam_page = pd.read_excel("excel_exam.xlsx",sheet_name = 0)
df_exam_page

df2

df2.to_csv("output_fruits_noindex.csv",index=False)

exam = pd.read_csv("exam.csv")
exam
exam.head(10)
exam.tail()
exam.shape
exam.info()
exam.describe()


mpg = pd.read_csv("mpg.csv")
mpg
mpg.info()

# drv 구동방식 / displ 배기량 / cyl 실린더 개수 / trans 변속기 종류 / cty 도시 연비
# hwy 고속도로 연비 / f1 연료 종류

mpg.describe(include = 'all')

# top 최빈값 freq 최빈값 빈도

new_mpg = mpg.copy()
new_mpg

new_mpg = new_mpg.rename(columns = {'model' : 'car_model'})
new_mpg
new_mpg = new_mpg.rename(columns = {'cty':'city','hwy':'highway'})
new_mpg

new_mpg["total"] = (new_mpg["city"]+new_mpg["highway"])/2
sum(new_mpg['total'])/len(new_mpg)
new_mpg['total'].describe()
new_mpg['total'].plot.hist()
plt.show()
plt.clf()
nm['test'] = np.where(new_mpg['total']>20,'pass','fail')

nm = new_mpg.copy()
nm.head()
counts_test = nm['test'].value_counts()
counts_test.plot.bar(rot=0)

plt.clf()
plt.show()


nm['grade'] = np.where(new_mpg['total']>=30,'A',np.where(new_mpg['total']>=20,"B","C"))
nm
nm['grade'].value_counts()

counts_test = nm['grade'].value_counts()
counts_test.plot.bar(rot=0)
count_grade = nm['grade'].value_counts().sort_index()
count_grade
count_grade.plot.bar(rot=0)

nm['size'] = np.where((nm['category'] == 'compact') or
(nm['category'] == 'subcompact') or
(nm['category'] == '2seater'),'small','large')
nm.info()
#??

nm = nm.rename(columns = {'class':'category'})
nm
nm['size'] = np.where((nm['category'] == 'compact') |
(nm['category'] == 'subcompact') |
(nm['category'] == '2seater'),'small','large')
nm
nm['size'] = np.where((nm['category'].isin(["compact","subcompact",'2seater']),'small','large')
nm
