import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import os
#!pip install scikit-learn

# 데이터 타입
x = 15.34
print(x, "는", type(x),"형식입니다.",sep="")

a = "Hello, world!"
b = 'python programming'

print(a,type(a))
print(b,type(b))

#"""         """
ml_str = """This is 
multiple 
String."""

print(ml_str,type(ml_str))

# 문자열 결합
greeting = "안녕" + " " + "파이썬!"
print("결합 된 문자열:", greeting)
# 문자열 반복
laugh = "하" * 3
print("반복 문자열:", laugh)


fruit = ["apple","banana","cherry"]
type(fruit)

numbers = [1,2,3,4,5]
type(numbers)

mixed_list = [1,"Hello",[1,2,3]]
type(mixed_list)


tu = (10,20,30) #tu = 10,20,30 과 동일
b_int = (42)
b_int
type(b_int)
b_tp = (42,24,13)
b_tp
type(b_tp)
b_tp = (10,24,30)

a_ls = [10,20,30,40,50]
a_ls[1] = 25
a_ls[2:] 
a_ls[2:5]
a_ls
a_tp = (10,20,30,40,50)
a_tp[1] = 25
a_tp[3:] #해당 인덱스 이상
a_tp[:3] #해당 인덱스 미만

def min_max(numbers) :
  return [min(numbers),max(numbers)]

nums = [1,2,3,4,5]
result = min_max(nums)
type(result)

print("Min,Max 는",result)

person = {
'name': 'John',
'age': 30,
'city': 'New York'
}
print("Person:", person)

person.update({'name':'bob',"age":'25'})

print("Person:", person)




person2 = {
  "name" : "용규",
  "age" : (28,20),
  "사는곳" : ["한국","의정부시","안산시"]
}

person2.get('age')[0]
per2_age = person2.get("나이")
per2_age[0]

print("Person =",person)
print("Person2 =",person2)
print("Names ? =",person2["name"],person["name"],sep = " ")

# 집합 생성 예제
fruits = {'apple', 'banana', 'cherry', 'apple'}
print("Fruits set:", fruits) # 중복 'apple'은 제거됨
type(fruits)
# 빈 집합 생성
empty_set = set()
print("Empty set:", empty_set)

empty_set.add("apple")
empty_set.add("apple")
empty_set.add("apple")
empty_set.add("banana")
empty_set.add("apple")
empty_set.add("apple")
empty_set.remove("banana")
empty_set.discard("banana")

empty_set
other_fruits = {'berry', 'cherry'}
union_fruits = fruits.union(other_fruits)
intersection_fruits = fruits.intersection(other_fruits)
print("Union of fruits:", union_fruits)
print("Intersection of fruits:", intersection_fruits)

p = True
q = False
print(p, type(p))
print(q, type(q))
print(p + p)

is_active = True
is_greater = 10 > 5 # True 반환
is_equal = (10 == 5) # False 반환
print("Is active:", is_active)
print("Is 10 greater than 5?:", is_greater)
print("Is 10 equal to 5?:", is_equal)


# 조건문
a=3
if (a==2) :
  print("a는 2와 같습니다.")
else:
  print("a는 2와 같지 않습니다.")
  
  
# 숫자형을 문자열형으로 변환
num = 123
str_num = str(num)
print("문자열:", str_num, type(str_num))
# 문자열형을 숫자형(실수)으로 변환
num_again = float(str_num)
print("숫자형:", num_again, type(num_again))

#리스트와 튜플 변환
lst = [1,2,3]
print("리스트:",lst)
tup = tuple(lst)
print("튜플:",tup,type(tup))

# 딕셔너리로 변환 시, 일반적으로 집합 요소를 키 또는 값으로 사용
dict_from_set = {key: True for key in set_example}
print("Dictionary from set:", dict_from_set)

set_example = {'a', 'b', 'c'}
set_example2 = {'x','y','z'}

dict_from_set = {key in set_example2 for item in set_example}
print("Dictionary from set:", dict_from_set)
#-------------------------------------------------교과서

print(os.getcwd())

df_exam = pd.read_csv('exam.csv')
df_exam

var=['a','a','b','c']
var
sns.countplot(x = var)
plt.show()
plt.clf()

df = sns.load_dataset("titanic")
df
sns.countplot(data=df,x='sex')
sns.countplot(data=df,x='class',hue='alive')
sns.countplot(data=df,
              x='class',
              hue='alive',
              orient="h")
plt.show()
plt.clf()
from sklearn import metrics 
import sklearn.metrics 

