import pandas as pd
import numpy as np

df = pd.DataFrame({ "sex" : ["M","F",np.nan,"M","F"],\
                    "score" : [5,4,3,4,np.nan]})

pd.isna(df)


df["score"]+1
pd.isna(df).sum()

#결측치 제거

df.dropna(subset = "score") #score 변수에서 결측치 제거
df.dropna(subset = ["score","sex"]) # 여러 변수 결측치 제거법
df.dropna() #아묻따 제거

exam=pd.read_csv("data/exam.csv")

#데이터 프레임 location 을 사용한 인덱싱
#exam.loc[행 인덱스,열 인덱스]
exam.iloc[0,2]
exam.loc[[2,4,7],["math"]] =np.nan

#exam.iloc[[2,7,4],2] = np.nan

df
df.loc[[df["score"] ==3],["score"]] = 4
df
#수학 점수 50점 이하인 학생들 점수 50점으로 상향 조정!
exam = pd.read_csv("data/exam.csv")
exam["math"]=np.where(exam["math"]<=50,50,exam["math"])
exam.loc[exam["math"]<=50,"math"] = 50

exam
#영어 점수 90점 이상 90점으로 하향 조정(iloc 사용)
#iloc 무조건 숫자 벡터만 조회 가능
exam.iloc[exam[exam["english"] >= 90].index,3]

exam.iloc[np.array(exam["english"]>=90),3]
#np.where은 튜플이라 [0] 으로 np 어레이 꺼내옴
exam.iloc[np.where(exam["english"]>=90)[0],3]

#math 점수 50점 이하 - 로 변경
exam.iloc[np.array(exam["math"]<=50),2] = "-"
exam.loc[exam["math"]<=50,"math"] = "-"

#"-" 결측치를 수학 점수 평균으로 바꾸고 싶은 경우

mean_math = int(exam[exam["math"] != "-"]["math"].mean())
exam.loc[exam["math"] == "-","math"] = mean_math
exam.iloc[np.where(exam['math']=="-")[0],2]=mean_math
exam
exam.query('math not in ["-"]')["math"].mean()

math_mean = int(exam[exam["math"] != "-"]["math"].mean())
exam["math"] = np.where(exam["math"]=="-",math_mean,exam["math"])
exam

array = exam["math"]
vector = np.array([np.nan if x == "-" else float(x) for x in array ])
vector = np.array([float(x) if x != "-" else np.nan for x in array ])
int(np.nanmean(vector))
exam["math"] = vector
exam = exam["math"].replace(np.nan,math_mean)
exam

math_mean = int(exam[exam["math"] != "-"]["math"].mean())
exam = exam["math"].replace("-",math_mean)
