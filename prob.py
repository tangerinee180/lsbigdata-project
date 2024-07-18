#확률 변수 => 대문자, 숫자(관측값) => x1,x2,x3(아래첨자 사용)
import numpy as np
#균일 확률 변수 만들기
a = np.random.rand(1)
a

def myf(x):
    random_values = np.random.rand(x)
    for value in random_values:
        print(value)
    return random_values

def myf2(x):
    random_values = np.random.rand(x)
    return x, random_values

myf(4)
myf2(5)

#베르누이 확률 변수 모수:p 만들어 보세요
def Y(p,num):
    result_list = []
    for _ in range(num) :
        st = np.random.rand(1)
        if st > p:
            x = 1
        else:
            x = 0
        result_list.append(x) 
    return np.array(result_list)

def Y2(num,p):
    x = np.random.rand(num)
    return np.where(x<p,1,0)

Y(0.4,100).mean()
Y2(4,0.2)
Y2(10000,0.5).mean()

#새로운 확률 변수
#가질 수 있는 값 0,1,2
#20%,50%,30%
def New(num):
    ns = np.random.rand(num)
    return np.where(ns<0.2,0,np.where(ns<0.7,1,2))
New(100)

def New2(num):
    result = []
    for _ in range(num):
        st = np.random.rand(1)
        if st <0.2:
            x= 0
        elif 0.2<st<0.7:
            x=1
        else:
            x=2
        result.append(x)
    return np.array(result)

New(100)
New2(100)
