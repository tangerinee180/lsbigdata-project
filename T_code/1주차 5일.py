import math
import numpy as np

a = (1,2,3)
a

a=[1,2,3]
a

#soft copy
b = a
b[1] = 4
a
b

id(a)
id(b)

#deep copy
a=[1,2,3]
a
id(a)
b=a[:]
b=a.copy()
id(b)
a[1]=4
a
b


x=4
math.sqrt(x)

sqrt_val = math.sqrt(16)
print("16의 제곱근은 : ",sqrt_val)

exp_val = math.exp(5)
print("e^5 값은? :",exp_val)

log_val = math.log(10,10)
print("10의 밑 10 로그값은 :",log_val)



def normal_pdf(x,mu,sigma) :
  part1 =1/(sigma*math.sqrt(2*math.pi))
  part2 =math.exp(-(x-mu)**2/(2*sigma**2))
  return part1*part2

normal_pdf(3,3,1)

def f(x,y,z) :
  return (x**2 + math.sqrt(y) + math.sin(z))*math.exp(x)

f(2,9,math.pi/2)

def y(x) :
  return math.cos(x)+math.sin(x)*math.exp(x)

y(math.pi)

a = np.array([1,2,3,4,5])
b = np.array(["apple","banana","orange"])
c = np.array(["True","False","True","True"])

a
a[2:]
a[1:4]
type(a)

x = np.empty(3)
x
x[0]=1
x[1]=2
x[2]=3
x
type(x[1])

vec1 = np.array([1,2,3,4,5])
vec1= np.arange(100)
vec1

vec1 = np.arange(1,101,0.5)
vec1
vec3 = np.arange(0,-100,-1)

vec3 = -np.arange(0,100,1)
vec3
vec2 = np.arange(10)
vec2

l_space1 = np.linspace(100,1,100)
l_space1
type(l_space1[0])
linear_space2 = np.linspace(0,1,5,endpoint=False)

np.repeat(vec1,5)

# repeat vs. tile
vec1 = np.arange(5)
np.repeat(vec1,3)
np.tile(vec1,3)

vec1 + vec1

$35672 이하 홀수들의 합은

vec4 = np.arange(1,35673,2)
x = np.arange(1,35673,2)
x.sum()
vec4
sum(vec4)
len(x)
x.shape


b = np.array([[1,2,3],[4,5,6]])
len(b)
b.shape
size = b.size

a=np.array([1,2])
b=np.array([1,2,3,4])

np.tile(a,2) + b
np.repeat(a,2) + b
b==3

len(np.arange(3,35675,7))

sum(np.arange(1,35672)%7 == 3)
(np.arange(1,35672,7)%7).count(3)
