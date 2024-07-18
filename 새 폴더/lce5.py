import numpy as np


x = np.empty(3)
print("빈 벡터 생성하기:", x)
# 배열 채우기
x[0] = 3
x[1] = 5
x[2] = 3
print("채워진 벡터:", x)

x = x + [0,1,2]
x
#np.arange([start, ]stop, [step, ]dtype=None)
#1. start: 배열의 시작값, 생략 시 0부터 시작합니다.
#2. stop: 배열 생성을 멈출 종료값, 이 값은 배열에 포함되지 않습니다.
#3. step: 각 배열 요소 간의 간격, 기본값은 1입니다.
#4. dtype: 배열의 데이터 타입을 명시적으로 지정, 생략 시 입력 데이터를 기반으로 유추합니다.

arr1 = np.arange(10)
print("Array from 0 to 9:", arr1)
arr2 = np.arange(0, 2, 0.5)
print("0부터 1.5까지 0.5 간격으로 발생:", arr2)

#numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
#1. start: 시퀀스의 시작값입니다.
#2. stop: 시퀀스의 종료값입니다. endpoint=True이면 이 값이 배열에 포함됩니다.
#3. num: 생성할 샘플의 수, 기본값은 50입니다.
#4. endpoint: True인 경우 stop이 마지막 샘플로 포함됩니다.
#5. retstep: True인 경우 결과와 함께 샘플 간의 간격도 반환됩니다.

#repeat, tile 차이점

linear_space1 = np.linspace(0, 1, 5)
linear_space1
print("0부터 1까지 5개 원소:", linear_space1)
linear_space2 = np.linspace(0, 1, 5, endpoint=False)
print("0부터 1까지 5개 원소, endpoint 제외:", linear_space2)

#np.repeat(a, repeats, axis=None)
#• a: 반복할 입력 배열입니다.
#• repeats: 각 요소를 반복할 횟수입니다.
#• axis: 반복을 적용할 축을 지정합니다. 기본값은 None으로, 배열을 평평하게 만든 후 반복합니다.


a = np.array([[1.0,2.0,3.0],[20,30,40],[4,5,6]])
b = 2.0
a*b
np.repeat(a,3,axis = 0)
np.repeat(a,3,axis = 1)
np.tile(a,3)
a.shape
#b.shape -> float 니까 shape 어트리뷰트 업슴


# 2차원 배열 생성
matrix = np.array([[ 0.0, 0.0, 0.0],
[10.0, 10.0, 10.0],
[20.0, 20.0, 20.0],
[30.0, 30.0, 30.0]])
matrix.shape
# 1차원 배열 생성
vector = np.array([1.0, 2.0, 3.0])
vector.shape
# 브로드캐스팅을 이용한 배열 덧셈
result = matrix + vector
print("브로드캐스팅 결과:\n", result)

# 세로 벡터 생성
vector2 = np.array([1.0, 2.0, 3.0, 4.0]).reshape(4, 1)
vector2
# 브로드캐스팅을 이용한 배열 덧셈
result2 = matrix + vector2
print("브로드캐스팅 결과:\n", result2)

#(4,3) + (3,0) = o
#(4,3) + (4,) = x
#(4,3) + (4,1) = o

np.random.seed(42)
a = np.random.randint(1,21,10)

print(a)
print(a[1])

a[2:5]
a[-1]
len(a)
a[-len(a)]
a[::2]
a[1:6:2]

1에서부터 1000사이 3의 배수의 합은?

numbers = list(range(1,1001))
sum(numbers[2:1000:3])
numbers[2:1000:3]

x = np.arange(3,1001)
sum(x[::3])
a
np.delete(a,[1,3])

a>3
a[a>6]


import pydataset

df = pydataset.data('mtcars')
np_df = np.array(df['mpg'])
df.info
model_names = np.array(df.index)
df["mpg"]

sum((np_df>=15) & (np_df< 25) )
sum(np_df >= np.mean(np_df))
#논리 연산자니까 sum 으로 구하기

sum((np_df < 15) | (np_df>=22))
np.random.seed(2024)
a = np.random.randint(1,10000,5)
b = np.array(["A","B","C","D","E"])
a

a[(a>2000)&(a<5000)]
b[(a>2000)&(a<5000)]

#15이상 20이하 자동차 모델
model_names[(np_df<=20) & (np_df>=15)]

#평균 mpg 보다 이상 자동차 개수
len(model_names[(np_df>=np.mean(np_df))])

np.random.seed(2024)
a = np.random.randint(1,26346,1000)

#처음으로 22000보다 큰 숫자가 나오는 위치는?
np.where(a>22000)[0][0]
#10,24651
a[10]
type(np.where(a>22000))
a[np.where(a>10000)][0]

c = np.array([[10000, 25000, 30000],
              [22000, 23000, 24000],
              [21000, 20000, 27000]])
np.where(c>22000)[1][3] == 2
np.where(a>10000)[0][49]
a[81]
#500보다 작은 숫자들 중 가장 마지막으로 나오는 숫자 위치와 그 숫자는 무엇인가요
np.where(a<500)[0][-1]
a[960]

a = np.array([20,np.nan,13,24,309])
np.nanmean(a)
?np.nan_to_num
np.nan_to_num(a,nan=0)

c
c[0][20000>0]=30000
c

def set():
    my_variable = None
    if my_variable == None :
        print("It is",my_variable)
set()  


b = np.nan
b
a
b+1
a+1

a_filtered = a[~np.isnan(a)]
a
a_filtered

str_vec = np.array(["사과","수박","참외","배"])
str_vec
str_vec[[0,2]]

mix_vec = np.array(["사과","배","12","참외"],dtype=str)
mix_vec

combined_vec = np.concatenate((str_vec,mix_vec))
combined_vec

col_stacked = np.column_stack((np.arange(1, 5), np.arange(12, 16)))
col_stacked

v_stacked2 = np.vstack((np.arange(1, 5), np.arange(12, 16)))
v_stacked2

vec1 = np.arange(1, 5)
vec2 = np.arange(12, 18)
z= np.resize(vec1,len(vec2))
z
np.vstack([z,vec2])

a = np.array([12,21,35,48,5])
a[0::2]

a= np.array([1,2,3,2,4,5,4,6])
np.unique(a)
a

#원소를 번갈아가면서 합치기
a = np.array([21, 31, 58])
b = np.array([24, 44, 67])
c = np.empty(len(a)+len(b))
c[0::2] = a
c[1::2] = b
c

type(c)
int_c = [int(x) for x in c]

print(int_c)
type(int_c[0])
