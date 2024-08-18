import numpy as np



# 리스트 예제
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "apple", 3.5, True]
print("과일 리스트:", fruits)
print("숫자 리스트:", numbers)
print("혼합 리스트:", mixed)

empty_list1 = []
empty_list2 = list()
print("빈 리스트 1:", empty_list1)
print("빈 리스트 2:", empty_list2)


# 초기값을 가진 리스트 생성
numbers = [1, 2, 3, 4, 5]
range_list = list(range(5))
print("숫자 리스트:", numbers)
print("range() 함수로 생성한 리스트:", range_list)


# 다양한 타입의 리스트 생성
mixed_list = [1, "apple", 3.5, True]
print("혼합 리스트:", mixed_list)

# 리스트 접근 및 슬라이싱
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# 인덱싱
first_fruit = fruits[0]
last_fruit = fruits[-1]
print("첫 번째 과일:", first_fruit)
3
print("마지막 과일:", last_fruit)
# 슬라이싱
some_fruits = fruits[1:4]
print("일부 과일:", some_fruits)


# 리스트 원소 수정
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print("수정된 과일 리스트:", fruits)

# 리스트 내포(comprehension)
#1. 대괄호로 쌓여져 있다 -> 리스트다
#2. 넣고 싶은 수식표현을 x를 사용해서 표현
#3. for .. in .. 을 사용해서 원소 정보 제공
squares = [x**2 for x in range(10)]
print("제곱 리스트:", squares)

list(range(10))

#numpy 어레이 와도 가능
my_squares = [x**3 for x in np.array([3,5,2,15])]
my_squares

#pandas 시리즈 와도 가능?
import pandas as pd
exam =pd.read_csv("data/exam.csv")
list = [x**3 for x in exam['math']]

list1 = [1,2,3]
list2 = [4,5,6]

combinedlist = list1 + list2

numbers = [5,2,3]
repeated_list = [c]
repeated_list = [x for x in numbers for _ in range(3)]
repeated_list
repeated_list

# _ 는 앞에 나온 값을 가리킴


#for 루프 문법
#for i in 범위 : 
#작동 방식

for i in range(5):
    print(i**2)

#리스트를 하나 만들어서
#for 루프를 사용해서 2,4,6,8,....,20의 수를 채워 넣어 보세요
list = []
for x in range(1,11):
    list.append(x*2)
list

[i for i in range(2,21,2)]
mylist=list(range(1,11))

[x for x in range(3)]
mylist_b=[2,4,6,8,10,12,14,16,18,20]
list2= [0] *10
for i in range(1,11):
    list2[i] = (i)*2
list2

#mylist
#for i in range(1,11):

for i in range(10):
    mylist[i] = mylist_b[i]
mylist

#퀴즈:mylist_b의 홀수 번째에 있는 숫자들만 mylist
mylist_b=[2,4,6,8,10,12,14,16,18,20]
list2= [0] *5
for i in range(5):
    list2[i] = mylist_b[2i]
list2

for x in [5,2,3]:
    for y in range(3):
        print(x)

#리스트 컴프리핸션으로 바꾸는 방법
#바깥은 무조건 대괄호로 묶어줌 : 리스트로 반환하기 위함
#for 루프의 : 는 생략
#실행 부분을 먼저 써준다.
#결과를 받는 부분 제외시킴
[]

for i in range(5):
    print('hello')
    
    

for i in [0,1,2]:
    for j in [0,1]:
        print(i+j)
numbers = [1,2,3]
[i for i in numbers for j in range(4)]


fruits = ["apple","apple", "banana", "cherry"]
print("banana가 리스트에 포함되어 있나요?", "banana" in fruits)
print("grape가 리스트에 포함되어 있나요?", "grape" in fruits)

#[x == "banana" for x in fruits]
mylist=[]
for x in fruits:
    mylist.append(x == "banana")
index_list =[]
fruits = ["apple", "banana", "cherry"]
for x in range(len(fruits)):
    if fruits[x] == "banana":
        index_list.append(x)
index_list

np.where(np.array(fruits) =="banana")[0][0] 
#원소 거꾸로 써주기
fruits = ["apple","apple", "banana", "cherry"]
fruits.reverse()

#원소 맨끝에 붙여주기
fruits.append("pineapple")
fruits

fruits = ["apple", "banana", "cherry"]
fruits.extend(["date", "elderberry"])
print("extend() 후 리스트:", fruits)
#원소삽입
fruits.insert(2,"test")
fruits

#원소제거
fruits.remove("test")

import numpy as np
# 넘파이 배열 생성
fruits = np.array(["apple", "banana", "cherry", "apple", "pineapple"])
# 제거할 항목 리스트
items_to_remove = np.array(["banana", "apple"])
# 불리언 마스크 생성
mask = ~np.isin(fruits, ["banana", "apple"])
np.isin(fruits, items_to_remove)
# 불리언 마스크를 사용하여 항목 제거
filtered_fruits = fruits[mask]
print("remove() 후 배열:", filtered_fruits)


mylist_b=[1,2,3,4,5,6,7,8,9,0]
xx = []
for i in range(len(mylist_b)):
    if i % 2 == 0:
        xx.append(mylist_b[i])
xx

mylist_b=[2,4,6,80,10,12,24,35,23,20,100]
mylist=[0]*5
len(mylist)
for i in range(len(mylist_b)):
    if mylist_b[i]%2==0:
    print("ff")
    mylist[i]=mylist_b[2*i]

np.random.choice(3,20,replace=False)
np.random.random_integers(1,28,28)
import pandas as pd
old_seat = np.arange(1, 29)
np.random.seed(20240729)

new_seat = np.random.choice(old_seat,28,replace=False)

df = pd.DataFrame({"old_seat":old_seat,
                   "new_seat":new_seat })

df.to_csv("result.csv")

a = np.linspace(-100,100,1000)
b= a*2
#plt.plot 
x = np.linspace(0,8,2)
y= x*2
plt.plot(a,b)
plt.show()
plt.grid()
plt.clf()

plt.plot(x,y)

#y=x^2
a = np.linspace(0,8,3)
b = a*a

plt.plot(a,b)

a = np.linspace(-10,10,1000)
b = a*a


#plt.axis('equal')
plt.xlim(-40,40)
plt.ylim(0,40)
plt.plot(a,b)
plt.grid()
plt.gca()

plt.show()
plt.clf()




