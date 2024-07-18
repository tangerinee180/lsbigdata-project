import pandas as pd

test1 = pd.DataFrame({'id':[1,2,3,4,5],"midterm":[60,80,70,90,85]})
test2 = pd.DataFrame({'id':[1,2,3,4,5],"final":[70,83,65,95,80]})
df = pd.read_csv("data/exam.csv")
name = pd.DataFrame({"nclass":[1,2,3,4,5],"teacher":["kim","lee","choi","park","jung"]})

#Left Join
total = pd.merge(test,test2,how="left",on="id")
total

#Right Join
total = pd.merge(test,test2,how="right",on="id")
total


#Inner Join
total = pd.merge(test,test2,how="inner",on="id")
total


#Outer Join
total = pd.merge(test,test2,how="outer",on="id")
total


total = pd.merge(test1,test2,how="left",on="id")
tot = pd.merge(df,name,how="left",on="nclass")
tot


score1 = pd.DataFrame({'id':[1,2,3,4,5],"score":[60,80,70,90,85]})
score2 = pd.DataFrame({'id':[6,7,8,9,10],"score":[70,83,65,95,80]})

group_all = pd.concat([score1,score2])# axis =1 치면 옆으로 붙음(id 열도 그대로 붙음)
group_all
