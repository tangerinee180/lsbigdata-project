import pandas as pd
import numpy as np

#데이터 전처리 함수
#query()
#df[]
#sort_values()
#groupby()
#assign()
#agg()
#merge()
#concat()



exam = pd.read_csv("data/exam.csv")

#조건에 맞는 행을 걸러내는 .query
#exam[["nclass"]==1]

exam.query("nclass == 1")
exam.query("nclass != 1")

exam.query("math > 50")
exam[exam["math"] > 50]
exam.query("math < 50")
exam.query('english >= 50')
exam.query("english <= 80")

exam.query("nclass == 1 & math >= 50")
exam.query("nclass == 2 & english >= 80")
exam.query("math >= 90 | english >= 90")
exam.query("english < 90 | science < 50")
exam.query("nclass == 1 | nclass == 3 | nclass == 5")

exam.query("nclass in [1,3,5]")
#exam.query("nclass not in [2,4]")
#exam[~exam["nlcass"].isin([1,2])]
