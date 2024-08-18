import pandas as pd
import numpy as np
import seaborn as sns    
import matplotlib.pyplot as plt    
import math
import scipy.stats    


#직선의 방정식
#y=2x+3 의 그래프를 그려보세요!
a=2
b=3
x = np.linspace(-10,10,2000)
y = a*x + b

plt.plot(x,y,color="blue")
plt.axvline(0,color="black")
plt.axhline(0,color="black")
plt.xlim(-5,5)
plt.ylim(-5,5)
plt.show()
plt.clf()



house_train_raw = pd.read_csv("data/train.csv")
house_train = house_train_raw.copy()
house_train = house_train[["BedroomAbvGr","SalePrice"]].head(10)
house_train["SalePrice"] = house_train["SalePrice"]/1000
plt.scatter(x=house_train["BedroomAbvGr"],y=house_train["SalePrice"])

a= 63
b = 100
x = np.linspace(0, 5, 100)
y = a*x +b

house_train = pd.read_csv("data/train.csv")
my_df = house_train[["BedroomAbvGr", "SalePrice"]]
my_df["SalePrice"] = my_df["SalePrice"] / 1000
my_df["SalePrice"] = my_df["BedroomAbvGr"]*(my_df["SalePrice"].mean())+100
plt.scatter(x = my_df["BedroomAbvGr"], y = my_df["SalePrice"])
plt.plot(x,y, color="black")
plt.show()
plt.clf()



sub = pd.read_csv("data/sample_submission.csv")
sub["SalePrice"] = test["SalePrice"]
sub.to_csv("sub_prediction08011.csv", index=False)
-----------------------------------------------------------------------------
# 테스트 집 정보 가져오기
house_train = pd.read_csv("data/train.csv")
my_df = house_train[["BedroomAbvGr", "SalePrice"]]
my_df["SalePrice"] = my_df["SalePrice"] / 1000

sub = pd.read_csv("data/sample_submission.csv")
x = 16
y = 133.966
my_df["SalePrice"] = (x * my_df["BedroomAbvGr"] + y) * 1000

sub["SalePrice"] = my_df["SalePrice"]

sub.to_csv("sub_prediction084.csv", index=False)

plt.clf()
'''
#y_hat 구하기
y_hat = (a * house_train["BedroomAbvGr"]+b)*1000

y=house_train["SalePrice"]
#1
np.sum(np.abs(y - y_hat))
#2
np.sum((y-y_hat)**2)
house_train_raw = pd.read_csv("data/train.csv")
house_train = house_train_raw.copy()
house_train = house_train[["BedroomAbvGr","SalePrice"]]
house_train["SalePrice"] = house_train["SalePrice"]/1000
'''
house_train_raw = pd.read_csv("data/train.csv")
house_train = house_train_raw.copy()
house_train = house_train[["BedroomAbvGr","SalePrice"]]
house_train["SalePrice"] = house_train["SalePrice"]/1000

def linear_regression(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xx = sum(x_i ** 2 for x_i in x)
    sum_xy = sum(x_i * y_i for x_i in x for y_i in y)
    m = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x ** 2)
    b = (sum_y - m * sum_x) / n
    return m, b

!pip install scikit-learn

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 예시 데이터 (x와 y 벡터)
x = np.array([1, 3,2,1, 5]).reshape(-1, 1)  # x 벡터 (특성 벡터는 2차원 배열이어야 합니다)
y = np.array([1, 2, 3, 4, 5])  # y 벡터 (레이블 벡터는 1차원 배열입니다)

# 선형 회귀 모델 생성
model = LinearRegression()

# 모델 학습
model.fit(x, y) #자동으로 기울기, 절편 값을 구해줌

# 회귀 직선의 기울기와 절편
slope = model.coef_[0]
intercept = model.intercept_
print(f"기울기 (slope): {slope}")
print(f"절편 (intercept): {intercept}")

# 예측값 계산
y_pred = model.predict(x)

# 데이터와 회귀 직선 시각화
model.coef_
model.intercept_

plt.scatter(x, y, color='blue', label='실제 데이터')
plt.plot(x, y_pred, color='red', label='회귀 직선')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
plt.clf()



##################3
import pandas as pd
import numpy as np
import seaborn as sns    
import matplotlib.pyplot as plt    
import math
import scipy.stats
from sklearn.linear_model import LinearRegression

#필요한 데이터 불러오기
house_train = pd.read_csv("data/train.csv")
house_test = pd.read_csv("data/test.csv")
sub_df = pd.read_csv("data/sample_submission.csv")
my_df = house_train[["BedroomAbvGr", "SalePrice"]]

# 선형 회귀 모델 생성
model = LinearRegression()

x = np.array(my_df["BedroomAbvGr"]).reshape(-1,1)
y = my_df["SalePrice"]
# 모델 학습
model.fit(x, y) #자동으로 기울기, 절편 값을 구해줌

# 회귀 직선의 기울기와 절편
slope = model.coef_[0]
intercept = model.intercept_
print(f"기울기 (slope): {slope}")
print(f"절편 (intercept): {intercept}")

# 예측값 계산
y_pred = model.predict(x)

# 데이터와 회귀 직선 시각화
model.coef_
model.intercept_

plt.scatter(x, y, color='blue', label='실제 데이터')
plt.plot(x, y_pred, color='red', label='회귀 직선')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
plt.clf()
my_df['SalePrice'] =  y_pred
sub = pd.read_csv("data/sample_submission.csv")
sub["SalePrice"] = my_df['SalePrice']

sub.to_csv("sub_prediction085.csv", index=False)


# 회귀직선 구하기

import numpy as np
from scipy.optimize import minimize

def line_perform(par):
    y_hat=(par[0] * house_train["BedroomAbvGr"] + par[1]) * 1000
    y=house_train["SalePrice"]
    return np.sum(np.abs((y-y_hat)))

line_perform([36, 68])

# 초기 추정값
initial_guess = [0, 0]

#initial_guess 가 중요하다 - 아래로 볼록한 지점이 두세개 있을 경우


# 최소값 찾기
result = minimize(line_perform, initial_guess)

# 결과 출력
print("최소값:", result.fun)
print("최소값을 갖는 x 값:", result.x)



def my_f2(x,y):
    z=x**2+y**2+3
    return z



# ====================
# =====   옵션   =====
# ====================

import numpy as np
from scipy.optimize import minimize

# 최소값을 찾을 다변수 함수 정의
def my_f(x):
    return x**2 +3

def my_f2(x):
    z=x[0]**2+x[1]**2+3
    return z

def my_f3(x):
 return (x[0]-1)**2 + (x[1]-2)**2 + (x[2]-4)**2 + 7
# 초기 추정값
initial_guess = [0,0,0]

# 최소값 찾기
result = minimize(my_f3, initial_guess)

# 결과 출력
print("최소값:", result.fun)
print("최소값을 갖는 x 값:", result.x)

test_x = np.array(house_test["BedroomAbvGr"]).reshape(-1,1)
test_x
pred_y=model.predict(test_x)

sub = pd.read_csv("data/sample_submission.csv")
sub["SalePrice"] = pred_y

sub.to_csv("sub_prediction085.csv", index=False)

#### 이상치 제거후 그리기
house_train = pd.read_csv("data/train.csv")
house_test = pd.read_csv("data/test.csv")
sub_df = pd.read_csv("data/sample_submission.csv")


#house_train.query("GrLivArea>=4500")[["Id","GrLivArea","SalePrice"]]
house_train = house_train.query("GrLivArea<4500")[["Id","GrLivArea","SalePrice"]]

model = LinearRegression()

x = np.array(house_train["GrLivArea"]).reshape(-1,1)
y = house_train["SalePrice"]
# 모델 학습
model.fit(x, y) #자동으로 기울기, 절편 값을 구해줌

plt.rcParams.update({"figure.dpi": 150,
"figure.figsize": [8, 6],
"font.size": 11,
"font.family": "Malgun Gothic"})

y_pred = model.predict(x)
plt.scatter(x, y, color='blue', label='실제 데이터')
plt.plot(x,y_pred, color='red', label='회귀 직선')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
plt.clf()

# 회귀 직선의 기울기와 절편
slope = model.coef_[0]
intercept = model.intercept_
print(f"기울기 (slope): {slope}")
print(f"절편 (intercept): {intercept}")

test_x = np.array(house_test["GrLivArea"]).reshape(-1,1)
y_pred = model.predict(test_x)
house_test = y_pred
sub_df["SalePrice"] = y_pred

sub_df.to_csv("sub_predictionGR2.csv", index=False)





#
house_train = pd.read_csv("data/train.csv")
house_test = pd.read_csv("data/test.csv")
sub_df = pd.read_csv("data/sample_submission.csv")


#house_train.query("GrLivArea>=4500")[["Id","GrLivArea","SalePrice"]]
house_train = house_train.query("GrLivArea<4500")[["Id","GrLivArea","GarageArea","SalePrice"]]

model = LinearRegression()
#x = house_train[["GrLivArea","GarageArea"]]
x = np.array(house_train[["GrLivArea","GarageArea"]]).reshape(-1,2)
y = house_train["SalePrice"]
# 모델 학습
model.fit(x, y) #자동으로 기울기, 절편 값을 구해줌

slope = model.coef_
intercept = model.intercept_
print(f"기울기 (slope): {slope}")
print(f"절편 (intercept): {intercept}")

#테스트 데이터 예측
house_test = pd.read_csv("data/test.csv")

house_test = house_test[["Id","GrLivArea","GarageArea"]].fillna(house_test["GarageArea"].mean())
x = house_test["GrLivArea"]
y = house_test["GarageArea"]

#def myf4(x,y):
#    return slope[0]*x + slope[1]*y + intercept
#myf4(300,55)
#myf4(x,y)

x = np.array([x,y]).reshape(-1,2)

pred_y = model.predict(x)
len(pred_y)
sub_df["SalePrice"] = pred_y

sub_df.to_csv("sub_predictionGRgarage.csv", index=False)


##### 인트 플롯트 다 잡기 변수 별로 결측값 채우기.
#quantile,mean,mode,median
house_train = pd.read_csv("data/train.csv")
house_test = pd.read_csv("data/test.csv")
sub_df = pd.read_csv("data/sample_submission.csv")
x=house_train.select_dtypes(include=[int,float])
x = x.iloc[:,1:-1]
#x=x.drop(columns!=['id'])


model = LinearRegression()
#x = house_train[["GrLivArea","GarageArea"]]
pd.isna(x).sum()
x.isna().any()
# 결측치 확인
x.isna().sum()

'''
x["GarageYrBlt"] = x["GarageYrBlt"].fillna(x["GarageYrBlt"].mean())
x["LotFrontage"] = x["LotFrontage"].fillna(x["LotFrontage"].mean())
x["MasVnrArea"] = x["MasVnrArea"].fillna(x["MasVnrArea"].mean())
'''

x["LotFrontage"].fillna(x["LotFrontage"].mean(),inplace=True)
x["MasVnrArea"].fillna(x["MasVnrArea"].mean(),inplace=True)
x["GarageYrBlt"].fillna(x['GarageYrBlt'].mean(),inplace=True)
len(x.columns)
x = np.array(x)
y = house_train["SalePrice"]
# 모델 학습
model.fit(x, y) #자동으로 기울기, 절편 값을 구해줌

slope = model.coef_
intercept = model.intercept_

x2 = house_test.select_dtypes(include=[int,float])

pd.isna(x2).sum()
x2.isna().any()

#for i in x2.columns:
#    x2[i].fillna(x2[i],inplace=True)
x2 = x2.fillna(test_x.mean())

pd.isna(x2).sum()
x2.isna().any()
#x2.drop(columns=='Id')
x.shape
x2.shape

x2 = x2.iloc[:,1:]
x2 = np.array(x2)
pred_y = model.predict(x2)
    
sub_df["SalePrice"]=pred_y
sub_df.to_csv("sub_numeric2.csv", index=False)

