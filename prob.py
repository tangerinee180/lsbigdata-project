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
np.random.randint(0,32,5).reshape(-1,5)


def New(num,p):
    ns = np.random.rand(num)
    pc = p.cumsum()
    return np.where(ns<pc[0],0,np.where((ns<pc[1]),1,2))

New(100,p)



#p와 result 가 같은 size 로 주어졌을 때 구할 수 있는 함수
p = np.array([0.2,0.5,0.3])
result = [0,1,2]


def Real_New(num,p,result):
    final = []
    ns = np.random.rand(num)
    pc = p.cumsum()
    for y in ns :
        for i,x in enumerate(pc) :
            if x > y:
                final.append(result[i])
                break
    return final
import numpy as np
#enumerate()
p = np.array([0.2, 0.5, 0.3])
result = [0, 1, 2]

def Real_New2(num, p, result):
    final = []
    ns = np.random.rand(num)
    pc = p.cumsum()  
    for y in ns:
        a = 0  
        for x in pc:  
            if x > y:
                final.append(result[a])  
                break
            a += 1  
    return final

Real_New(30,p,result)
Real_New2(30,p,result)                
                

def New2(num):
    result = []
    for _ in range(num):
        st = np.random.rand(1)
        if st <=0.2:
            x= 0
        elif st<=0.7:
            x=1
        else:
            x=2
        result.append(x)
    return np.array(result)

New(100)
New2(100)
1*2/6 + 2*2/6 + 3*1/6

#E(X)
sum(np.arange(4)*np.array([1,2,2,1])/6)

#X 가 
#X ~Bernulli(p)

