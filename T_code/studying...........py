import pandas as pd
import numpy as np

test1 = pd.DataFrame({"id" : [1,2,3,4,5] ,"midterm":[60,80,70,90,85]})
test2 = pd.DataFrame({"id" : [1,2,3,4,5] ,"final" : [70,83,65,95,80]})

total = pd.merge(test1,test2,how="left",on="id")
total

name = pd.DataFrame({"nclass":[1,2,3,4,5],
                    "teacher":["kim","lee","park","choi","jung"]})
name

exam = pd.read_csv("exam.csv")
exam

group_all = pd.merge(exam,name,how="left",on="nclass")
group_all

mpg_raw = pd.read_csv("mpg.csv")
mpg = mpg_raw.copy()
fuel = pd.DataFrame({"fl":["c","d","e","p","r"],\
"price_fl" : [2.35,2.38,2.11,2.76,2.22]})
mpg.columns
mpg = pd.merge(mpg,fuel,how="left",on="fl")
mpg[["model","fl","price_fl"]].head()

mpg
mpg.groupby(["manufacturer","drv"])\
            .agg(mean_cty =("cty","mean"))
